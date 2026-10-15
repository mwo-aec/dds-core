---
name: dds-organise
description: Organise phase of the DDS Loop — turn captured sources into a job (method card) with a job story and a job map of steps and tasks, marking empty stages as gaps with questions. Use after capturing, or when a job's steps need restructuring.
---

# DDS · Organise

**Framework:** Jobs to be Done (Christensen); job stories (Intercom; Klement); the universal job map (Bettencourt & Ulwick). See `spec/05-foundations.md`.

**Goal:** one job, in order: what it is (Part A) and how it's done today (Part B).

## Inputs
Told sources first, then documented, then observations.

## Steps
1. **Name the job:** a verb and an object ("Create a Revit family").
2. **Job story** from told sources: `when` / `iWantTo` / `soICan`, in the teller's words. `basis: seen` until the owner agrees it.
3. **Told by:** everyone whose account shaped it. Where the doer's and checker's stories differ, raise a `contradiction` question.
4. **Must not go wrong:** from what people said they'd hate to see, or what would embarrass the firm.
5. **Job map:** place every described step on one of the eight stages: define, locate, prepare, confirm, execute, monitor, modify, conclude.
6. **Gaps:** for every stage with no step, set `gap` and raise a `gap` question to the doer. Expect *confirm*, *monitor* and *modify* to be the usual gaps.
7. **Hired:** for each step, who does it **now** (from the sources) and, only if the owner said so, **next**. Set `finalYes: true` on steps that touch a must-not-go-wrong.
8. **Tasks:** split steps into `ai-does`, `ai-asks`, `person-decides`.
9. **Work record:** for each step, what it must leave behind.
10. Write `jobs/JOB-*.json`; render the method card (`templates/method-card.md`) for people.
11. Send the owner the job story and the gaps to check.

## Never
Invent a step nobody described and nothing shows. Decide `hired.next` for the owner.

## Done when
Every stage has a step or a gap with a question; the owner has seen the job story.

**Next:** `dds-distil`.
