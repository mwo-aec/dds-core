---
name: dds-review
description: Review phase of the DDS Loop — an After-Action Review of a run against the job's outcomes and rules, recording each item's verdict and cause, and turning lessons into change requests and questions that return to Capture. Use after a run, with the person who reviewed it.
---

# DDS · Review (After-Action Review)

**Framework:** After-Action Review (US Army, TC 25-20); Plan–Do–Check–Act (Deming) for the loop. See `spec/05-foundations.md`.

## Inputs
The run and its work records; the job's outcomes and rules; the reviewer's markings (accepted / changed / rejected), comments or a debrief transcript.

## Two depths
- **Quick** (every run): the reviewer marks each finding; you ask "why?" once, batched, for every changed or rejected item.
- **Deep** (early runs; before handing more of a step to AI): a sit-down debrief, recorded as a told source.

## For each reviewed item, the four questions
1. **What was supposed to happen?** Cite the outcome (`OUT-`) or rule.
2. **What actually happened?** Cite the work record.
3. **Why the difference?** Exactly one cause:
   | Cause | Goes to |
   |---|---|
   | `standard-gap` | question to the standards owner → maybe a new rule |
   | `execution-error` | the step or tool; no rule change |
   | `mapping-gap` | the adapter or tool |
   | `project-specific` | a project pack |
   | `preference` | ask the owner whether it's their standard |
   | `unknown` | a question |
4. **What do we keep or change?** `keep` and `change`; a change becomes a **change request** (`CR-`) or a **question** (`Q-`).

## Steps
1. Confirm the reviewer is named and the **scope** is stated; otherwise it isn't a review.
2. Record items per the four questions in `reviews/REV-*.json`.
3. Draft change requests (`status: proposed`) and questions.
4. Hand them to the owner. Approved changes and answers go back to **Capture** as new sources and pass through the loop again; the pack version goes up.

## Never
Apply a change request yourself. Learn from changes others made to things the run didn't touch. Count a review with no named person or scope. Judge the reviewer; review the AI's work.

## Done when
Every changed or rejected item has a cause; every cause has a destination; the review is valid.

**Next:** back to `dds-capture`.
