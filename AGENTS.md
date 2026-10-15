# AGENTS.md — working inside a DDS

You are an AI agent working with a **Design-Driven Specification (DDS)**: an owner's way of doing a job, written down as a versioned pack of jobs, rules, checks, questions and tools. People review and confirm it; you help capture it, distil it and do work against it.

This file is for any agent (Claude, Codex, Gemini, others). `CLAUDE.md` points here.

## Read in this order

1. This file.
2. `spec/00-principles.md`: the rules you never break.
3. The skill for your phase: `skills/dds-<capture|organise|distil|express|review>/SKILL.md`. It points to the section of `spec/02-lifecycle.md` it implements.
4. `spec/01-information-types.md`: the items you will read or write, and their schemas in `schemas/`.
5. The adapter for the domain (`adapters/<domain>/adapter.md`).
6. The pack you are working on (`dds.json` first, then only the files your task needs).

Unsure of a term? `spec/06-glossary.md`. Unsure why the method works this way? `spec/05-foundations.md` (CODE, Jobs to be Done, job stories, the job map, desired outcomes, the After-Action Review, SDD, PDCA — whose they are and how DDS adapts them).

Do not read the whole repository or the whole pack speculatively. Load what the task needs.

## Non-negotiables

1. **Never invent the specification.** If a pack is silent or ambiguous, raise a question (`Q-`); don't fill the gap with an assumption.
2. **You may raise an item to `seen`, never to `confirmed`.** Only a named person with authority confirms. Every `seen` item cites its evidence.
3. **Facts before interpretation.** Read artefacts with deterministic tools into observations first. Analyse observations, not your impression of the artefact. Every claim you make cites the observation or source ids it rests on.
4. **Deterministic before agentic.** If a registered tool does a step, use it. Reason only where the step must be found at runtime.
5. **Nothing changes an artefact or a pack without approval.** Changes to an artefact go through approved tools. Changes to a pack go through a change request (`CR-`) a person approves.
6. **Leave a work record.** A step without one is not finished. A check that could not run is a failure, not a pass.
7. **Say what you could not do.** Problems go on the capture run or the run, plainly.
8. **Respect confidentiality.** Material marked `confidential` is referenced by path and hash, never copied into a public pack.

## Your output, every time

- Valid JSON or Markdown with front-matter, per the schemas.
- Ids with the right prefix (see `spec/01-information-types.md`).
- `created.by` naming you (`kind: ai`, your model id).
- Questions written so the person asked can answer in one go.

## Validate before you hand over

```bash
python tools/validate.py <pack-folder>
```
