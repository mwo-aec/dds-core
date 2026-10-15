---
name: dds-express
description: Express phase of the DDS Loop — do a job against a DDS pack stack, step by step, using approved tools, leaving a work record per step and running the checks. Use when asked to produce something (e.g. "make a family", "set up the GA views") that a DDS job covers.
---

# DDS · Express

**Framework:** CODE *Express* (Forte), read as "the job done"; Specification-Driven Development (agents implement the spec). See `spec/05-foundations.md`.

## Inputs
A request; the job; the pack stack (base → firm/client → project); approved tools; resources (e.g. the family library).

## Steps
1. **Resolve** the pack stack lowest first; higher layers override by id; ignore `retired`. Record the exact pack versions in the run.
2. **Match** the request to the job and its steps. If the request needs something the job doesn't cover, stop and raise a question.
3. **For each step**, in job-map order:
   - Do it only if you are **hired** for it (`hired.now` is `ai` or `ai-with-person`); otherwise hand it to the person and record that.
   - Use a registered **tool** where one exists; reason only where the step must be found at runtime.
   - Pull components from **resources** (libraries) rather than rebuilding them.
   - Work in a scratch location. Writing to the design of record needs the step's **final yes**.
   - Leave the step's **work record** (image, structured read, step log, report, artefact) and say what it cannot show.
   - Run the step's **checks**; record passed/failed. A check that cannot run is `could-not-check`, a failure.
   - Add a one-line **self-assessment** (for calibration only).
4. Write `runs/RUN-*.json` and hand the outputs and findings to the reviewer.

## Never
Use a rule the pack doesn't contain. Treat could-not-check as a pass. Change the design of record without the final yes. Leave a step without a work record.

## Done when
Every step has a result and work records; checks were run; outputs are where the request said; the run is valid.

**Next:** `dds-review`.
