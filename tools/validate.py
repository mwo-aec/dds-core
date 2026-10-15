#!/usr/bin/env python3
"""Validate a DDS pack against the DDS Core schemas.

Usage:  python tools/validate.py <pack-folder> [<pack-folder> ...]

Checks every file by its place in the pack (see spec/03-packs-and-layers.md),
then a few cross-file rules: unique ids, rule/check pairing, status/lifecycle
agreement, and references that don't resolve inside the pack (warnings, since
they may live in another layer).

Exit code 0 = no errors (warnings allowed), 1 = errors.
Requires: jsonschema, referencing, pyyaml.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = ROOT / "schemas"
BASE = "https://digitalreframe.tech/dds-core/schemas/"
ID_RE = re.compile(r"^[A-Z][A-Z0-9]*(-[A-Z0-9]+)*(\.[a-z0-9][a-z0-9-]*)*$")


def load_registry() -> Registry:
    reg = Registry()
    for p in SCHEMAS.glob("*.schema.json"):
        doc = json.loads(p.read_text(encoding="utf-8"))
        reg = reg.with_resource(doc["$id"], Resource.from_contents(doc))
    return reg


REGISTRY = load_registry()
_validators: dict[str, Draft202012Validator] = {}


def validator(name: str) -> Draft202012Validator:
    if name not in _validators:
        schema = REGISTRY.contents(BASE + f"{name}.schema.json")
        _validators[name] = Draft202012Validator(schema, registry=REGISTRY, format_checker=FormatChecker())
    return _validators[name]


def plain(obj):
    """YAML dates/datetimes -> ISO strings, recursively."""
    if isinstance(obj, (dt.datetime, dt.date)):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: plain(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [plain(v) for v in obj]
    return obj


def front_matter(text: str):
    if not text.startswith("---"):
        return None, text
    parts = text.split("\n---", 1)
    if len(parts) < 2:
        return None, text
    head = parts[0][3:]
    body = parts[1].lstrip("-\n")
    return plain(yaml.safe_load(head) or {}), body


def collect_refs(obj, out: set):
    """Collect every string that looks like an id under keys that hold refs."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in {"ref", "job", "run", "rule", "outcome", "step", "source", "captureRun", "check", "tool", "overrides"} and isinstance(v, str) and ID_RE.match(v):
                out.add(v)
            elif k in {"jobs", "outcomes", "rules", "sources", "questions", "relatesTo", "targets", "from", "inputs", "openQuestions", "changes", "tools"} and isinstance(v, list):
                out.update(x for x in v if isinstance(x, str) and ID_RE.match(x))
            collect_refs(v, out)
    elif isinstance(obj, list):
        for v in obj:
            collect_refs(v, out)


class Report:
    def __init__(self, pack: Path):
        self.pack, self.errors, self.warnings, self.files = pack, [], [], 0

    def err(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"{where}: {msg}")


def check(rep: Report, where: str, data, schema: str):
    rep.files += 1
    for e in sorted(validator(schema).iter_errors(data), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in e.path) or "(root)"
        rep.err(where, f"[{schema}] {loc}: {e.message}")


def validate_pack(pack: Path) -> Report:
    rep = Report(pack)
    rel = lambda p: str(p.relative_to(pack))
    ids: dict[str, str] = {}
    refs: set[str] = set()

    def register(item_id, where):
        if not item_id:
            return
        if item_id in ids:
            rep.err(where, f"duplicate id {item_id} (also in {ids[item_id]})")
        ids[item_id] = where

    def load_json(p: Path):
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            rep.err(rel(p), f"invalid JSON: {e}")
            return None

    manifest = pack / "dds.json"
    if not manifest.exists():
        rep.err(str(pack), "no dds.json — not a pack")
        return rep
    m = load_json(manifest)
    if m is None:
        return rep
    check(rep, "dds.json", m, "pack")
    for r in m.get("resources", []):
        register(r.get("id"), "dds.json")
    paths = {"jobs": "jobs", "rules": "rules", "questions": "questions", "tools": "tools", "sources": "sources",
             "captures": "captures", "runs": "runs", "reviews": "reviews", "changes": "changes"}
    paths.update(m.get("paths", {}))

    simple = {"jobs": "job", "questions": "question", "tools": "tool", "sources": "source",
              "runs": "run", "reviews": "review", "changes": "change"}
    for key, schema in simple.items():
        for p in sorted((pack / paths[key]).glob("*.json")):
            d = load_json(p)
            if d is None:
                continue
            check(rep, rel(p), d, schema)
            register(d.get("id"), rel(p))
            collect_refs(d, refs)
            if schema == "job":
                for o in d.get("outcomes", []):
                    register(o.get("id"), rel(p))
                for stage in d.get("jobMap", []):
                    for s in stage.get("steps", []):
                        register(s.get("id"), rel(p))
                        for t in s.get("tasks", []):
                            register(t.get("id"), rel(p))

    rules_dir = pack / paths["rules"]
    rule_ids_by_stem: dict[Path, str] = {}
    for p in sorted(rules_dir.rglob("*.md")):
        fm, body = front_matter(p.read_text(encoding="utf-8"))
        if fm is None:
            rep.err(rel(p), "rule file has no YAML front-matter")
            continue
        check(rep, rel(p), fm, "rule")
        register(fm.get("id"), rel(p))
        collect_refs(fm, refs)
        rule_ids_by_stem[p.with_suffix("")] = fm.get("id")
        if "status" in fm and "lifecycle" in fm and fm["status"] != fm["lifecycle"]:
            rep.err(rel(p), "status and lifecycle disagree")
        for section in ("## Why", "## Examples"):
            if section not in body:
                rep.warn(rel(p), f"missing section '{section}'")
        if fm.get("layer") and fm.get("layer") != m.get("id") and fm.get("from") is None:
            rep.warn(rel(p), f"layer '{fm.get('layer')}' is not this pack ('{m.get('id')}')")
    for p in sorted(rules_dir.rglob("*.checks.json")):
        d = load_json(p)
        if d is None:
            continue
        check(rep, rel(p), d, "checks")
        stem = Path(str(p)[: -len(".checks.json")])
        rid = rule_ids_by_stem.get(stem)
        if rid is None:
            rep.err(rel(p), "no rule file beside this checks file")
        elif d.get("rule") != rid:
            rep.err(rel(p), f"rule '{d.get('rule')}' does not match the rule file id '{rid}'")
        for c in d.get("checks", []):
            register(c.get("id"), rel(p))
            if rid and not str(c.get("id", "")).startswith(rid + "."):
                rep.err(rel(p), f"check id {c.get('id')} should start with '{rid}.'")

    cap_dir = pack / paths["captures"]
    for cap in sorted(cap_dir.glob("*/capture.json")):
        d = load_json(cap)
        if d is None:
            continue
        check(rep, rel(cap), d, "capture-run")
        register(d.get("id"), rel(cap))
        collect_refs(d, refs)
        obs = cap.parent / "observations.jsonl"
        if obs.exists():
            obs_ids = set()
            for n, line in enumerate(obs.read_text(encoding="utf-8").splitlines(), 1):
                if not line.strip():
                    continue
                where = f"{rel(obs)}:{n}"
                try:
                    o = json.loads(line)
                except json.JSONDecodeError as e:
                    rep.err(where, f"invalid JSON: {e}")
                    continue
                check(rep, where, o, "observation")
                if o.get("id") in obs_ids:
                    rep.err(where, f"duplicate observation id {o.get('id')}")
                obs_ids.add(o.get("id"))
                ids.setdefault(o.get("id"), where)
                collect_refs(o, refs)

    for r in sorted(refs - set(ids)):
        rep.warn("references", f"{r} is not defined in this pack (fine if it lives in another layer)")
    return rep


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    failed = False
    for arg in argv[1:]:
        rep = validate_pack(Path(arg).resolve())
        print(f"\n== {arg}: {rep.files} items checked, {len(rep.errors)} errors, {len(rep.warnings)} warnings")
        for e in rep.errors:
            print("  ERROR  ", e)
        for w in rep.warnings:
            print("  warn   ", w)
        failed |= bool(rep.errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
