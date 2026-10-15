# 03 — Packs and layers

version 0.1.0

## A pack on disk

```
<pack>/
  dds.json                         manifest (schema: pack)
  core.md                          what this pack is, for people; plain words
  jobs/<job>.json                  method cards (schema: job)
  rules/<area>/<name>.md           rule: YAML front-matter (schema: rule) + body
  rules/<area>/<name>.checks.json  its machine checks (schema: checks)
  questions/<id>.json              questions (schema: question)
  questions.md                     generated view of open questions, for people
  tools/<id>.json                  registered tools (schema: tool)
  sources/<id>.json                sources (schema: source)
  captures/<run>/capture.json      capture run (schema: capture-run)
  captures/<run>/observations.jsonl  one observation per line (schema: observation)
  runs/<id>.json                   runs (schema: run)
  reviews/<id>.json                reviews (schema: review)
  changes/<id>.json                change requests (schema: change)
```

Folders may be renamed through `dds.json` → `paths`. Confidential captures (client artefacts, recordings) belong outside a shared repository or in git-ignored folders; the source file records the path and hash.

## Rule file

```markdown
---
id: DDS-PARAM-003
title: Family identity parameters
area: parameters
appliesTo: [all]
severity: must
lifecycle: active
basis: confirmed
version: 1.1.0
layer: digital-reframe
overrides: null
outcomes: [OUT-FAM-01]
confirmed: { by: { kind: person, name: Machiel Odendaal, role: standards owner }, at: 2026-10-15 }
---
The rule, in words.

## Why
## Examples
## Open questions
```

## Layers

| Layer | Holds | Example |
|---|---|---|
| `base` | general standards, framework defaults | `digital-reframe` |
| `firm` / `client` | an organisation's standards | `client-acme` |
| `project` | one project's deviations | `project-2023-a059` |

**Resolution.** Load the stack lowest first. A rule in a higher layer with the same `id`, or naming a lower id in `overrides`, replaces it. A higher layer may retire a lower rule by overriding it with `lifecycle: retired`. Everything else adds. Jobs, tools and resources resolve the same way by id.

**Borrowing.** When a client pack is drafted from a harvest, base rules the client has no evidence for stay `borrowed`; rules evidenced in the client's material become `seen` client rules (overriding the base where they differ).

## Versions

Each pack has a semver version. Patch: wording. Minor: added or confirmed items. Major: a changed or retired `must`. A run records the exact versions it read.

## RaD compatibility

| RaD | DDS Core |
|---|---|
| `status: draft/active` | `lifecycle` (`status` accepted as alias) |
| `from` | `layer` (`from` accepted as alias) |
| *(none)* | `basis` — **add** |
| checks `Id/Target/Kind/Pattern/Values/Severity/Message` | same names, camelCase |
| `dds-draft/questions.md` | `questions/*.json` + generated `questions.md` |
| harvest run folder | capture run + `observations.jsonl` |
