# DDS Core

**Design-Driven Specification: a framework for turning how work is done into a specification that people can review and any AI can follow.**

DDS Core is domain-free. It defines *what* to capture, *how* to organise and distil it, *how* work against it is recorded, and *how* reviews feed back into it. Adapters supply the domain: Revit families, Revit models, drawing sets, or anything else with artefacts and people who know how the work is done.

> *Creating clarity of our digital-complicated world.* (Digital Reframe)

## The DDS Loop

```
  Capture ──► Organise ──► Distil ──► Express ──► Review
  told ·        job story,    outcomes,    the job done   AAR: supposed vs
  found ·       job map,      rules,       by whoever is  happened, why,
  documented    steps, tasks  checks, Qs   hired per step keep / change
     ▲                                                        │
     └────────── answers and lessons return as new captures ──┘
```

| Phase | Built on | Who | Produces | Skill |
|---|---|---|---|---|
| **Capture** | CODE (Tiago Forte) · JTBD interview (Clayton Christensen) · job stories (Intercom; Alan Klement) | People tell; tools find; documents are read | Sources, observations | `dds-capture` |
| **Organise** | Universal job map (Lance Bettencourt & Anthony Ulwick) | AI drafts, the person checks | The job (method card) | `dds-organise` |
| **Distil** | CODE · desired outcome statements (Anthony Ulwick) | **AI drafts, a person confirms** | Outcomes, rules, checks, questions | `dds-distil` |
| **Express** | CODE · Specification-Driven Development | Whoever is hired for each step | Runs, work records | `dds-express` |
| **Review** | After-Action Review (US Army) · PDCA (W. Edwards Deming) | A named reviewer, with AI | Reviews, change requests | `dds-review` |

Who each framework belongs to, what we took and how we changed it: **[`spec/05-foundations.md`](spec/05-foundations.md)**.

## What's in this repository

| Path | What |
|---|---|
| `AGENTS.md` / `CLAUDE.md` | How an AI agent works in a DDS. Read first. |
| `spec/00-principles.md` | Twelve principles |
| `spec/01-information-types.md` | The fifteen information types, their id prefixes and the three labels |
| `spec/02-lifecycle.md` | Phase contracts: inputs, outputs, what AI may and may not do, done when |
| `spec/03-packs-and-layers.md` | Packs on disk; base → firm/client → project; RaD compatibility |
| `spec/04-adapters.md` | How a domain plugs in |
| `spec/05-foundations.md` | The frameworks we use, credited, and how we adapted them |
| `spec/06-glossary.md` | Every term, defined once, with its origin |
| `schemas/` | JSON Schemas (draft 2020-12) for every information type |
| `skills/` | One skill per phase, for any agent |
| `templates/` | Rule file, method card, JTBD interview |
| `adapters/revit-families/` | The first adapter (reference implementation: RaD) |
| `examples/` | Valid example packs: Revit families, Entity GA job |
| `decisions/` | Why things are the way they are |
| `tools/validate.py` | Validates a pack against the schemas |

## Quick start

```bash
pip install jsonschema referencing pyyaml
python tools/validate.py examples/revit-families-base examples/entity-ga
```

## The three labels

| Field | Values | Answers |
|---|---|---|
| `basis` | unset · borrowed · seen · confirmed | Where does it stand on evidence? AI can reach **seen**; only a person sets **confirmed**. |
| `lifecycle` | draft · active · retired | Is it in use? |
| `severity` | must · should · may | How strict is it? |

## Status

`0.1.0`, draft. Reference implementation: Digital Reframe's RaD add-in for Revit (family harvesting and generation). First applied instance: the General Arrangements pilot (DDS_forAEC).

## Credits

DDS Core stands on the work of Tiago Forte (CODE), Clayton M. Christensen (Jobs to be Done), Intercom and Alan Klement (job stories), Anthony W. Ulwick and Lance A. Bettencourt (Outcome-Driven Innovation), the United States Army (After-Action Review), W. Edwards Deming (PDCA), and the Specification-Driven Development community. Full references in `spec/05-foundations.md`. Assembled and adapted by Machiel Odendaal, Digital Reframe.

## Licence

To be decided before the repository is made public.
