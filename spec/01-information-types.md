# 01 — Information types

version 0.1.0

Everything in a DDS is one of these types. Each has an id prefix, a schema and a home in the pack.

| # | Type | Prefix | Schema | Phase | Made by | Lives in (default) |
|---|---|---|---|---|---|---|
| 1 | **Source** | `SRC-` | `source` | Capture | Anyone; filed by AI | `sources/*.json` |
| 2 | **Capture run** | `CAP-` | `capture-run` | Capture | Harvester or capture session | `captures/<run>/capture.json` |
| 3 | **Observation** | `OBS-` | `observation` | Capture | Deterministic tool (or a person) | `captures/<run>/observations.jsonl` |
| 4 | **Job** (method card) | `JOB-` | `job` | Organise | AI drafts, owner checks | `jobs/*.json` |
| 5 | **Outcome** | `OUT-` | inside `job` | Distil | AI drafts, owner confirms | in the job |
| 6 | **Step** | `STEP-` | inside `job` | Organise | AI drafts, person checks | in the job |
| 7 | **Task** | `TASK-` | inside `job` | Organise | AI | in the job |
| 8 | **Rule** | domain, e.g. `DDS-PARAM-003` | `rule` (front-matter) | Distil | AI drafts, standards owner confirms | `rules/<area>/<name>.md` |
| 9 | **Check** | `<rule-id>.<name>` | `checks` | Distil | AI or author | `rules/<area>/<name>.checks.json` |
| 10 | **Question** | `Q-` | `question` | Distil, answered in Capture | AI raises, a person answers | `questions/*.json` (+ `questions.md` view) |
| 11 | **Tool** (shorthand) | `TOOL-` | `tool` | Express (and Capture) | Author; approved by owner | `tools/*.json` |
| 12 | **Resource** | `RES-` | inside `pack` | Express | Owner | `dds.json` → `resources` |
| 13 | **Run** (+ work records) | `RUN-` | `run` | Express | Whoever is hired per step | `runs/*.json` |
| 14 | **Review** (AAR) | `REV-` | `review` | Review | Named reviewer, with AI | `reviews/*.json` |
| 15 | **Change request** (lesson) | `CR-` | `change` | Review | AI or person proposes; owner approves | `changes/*.json` |

The **pack manifest** (`dds.json`, schema `pack`) ties them together.

## Three labels, three questions

| Field | Values | Answers |
|---|---|---|
| `basis` | `unset` · `borrowed` · `seen` · `confirmed` | Where does it stand on evidence? |
| `lifecycle` (RaD: `status`) | `draft` · `active` · `retired` | Is it in use? |
| `severity` | `must` · `should` · `may` | How strict is it? |

- `unset`: nobody has said yet.
- `borrowed`: a default from a lower layer or the framework, not yet checked for this owner.
- `seen`: evidenced in the owner's own material (harvested, observed, drafted by AI); must cite evidence.
- `confirmed`: a named person with authority confirmed it; must carry `confirmed.by` and `confirmed.at`.

A rule can be `seen` and `active` (in use, reported as "seen, not yet confirmed"), or `confirmed` and `draft` (agreed, not yet switched on).

## Story

The job story (`When … I want to … so I can …`) lives in the job, Part A. The interviews and messages it came from are told sources.

## Ids

Upper-case segments joined by hyphens; a lower-case dotted suffix for a part of something (`DDS-PARAM-003.present`). Ids are never reused. A retired item keeps its id.
