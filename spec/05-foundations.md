# 05 — Foundations: whose frameworks, and how we adapted them

version 0.1.0

DDS Core is assembled from established frameworks. None of them is ours; the way they are joined, and what each is used for, is. This page names each one, credits its authors, says what we take, and says what we changed. Read it before extending the method, so a change stays faithful to the source or departs from it on purpose.

| # | Framework | Authors / origin | Where it sits in DDS | What we take | How we adapted it |
|---|---|---|---|---|---|
| 1 | **CODE** — Capture, Organize, Distill, Express | Tiago Forte, *Building a Second Brain* (2022) | The whole cycle | Four phases from raw material to useful output | Applied to an organisation's way of working, not a personal notebook. *Express* means the job done, not a creative output. A fifth phase, **Review**, closes the loop |
| 2 | **Jobs to be Done** (JTBD) | Clayton M. Christensen et al., *Competing Against Luck* (2016); "Know Your Customers' Jobs to Be Done", HBR (2016) | Capture and Organise | People "hire" something to make progress on a job; study the job, not the person or the tool | The "customer" is the person doing the work inside the firm. "Hired" names who does each step today: person, script or AI |
| 3 | **Job stories** — *When … I want to … so I can …* | Intercom (Paul Adams and team, 2013); Alan Klement, *When Coffee and Kale Compete* (2016) | Capture (the job story) | Situation-first story format instead of role-first user stories | Used for work inside a practice; the story is told by the doer *and* the checker, and differences become findings |
| 4 | **Outcome-Driven Innovation**: the universal job map and desired outcome statements | Anthony W. Ulwick, *What Customers Want* (2005), *Jobs to be Done: Theory to Practice* (2016); Lance A. Bettencourt & Ulwick, "The Customer-Centered Innovation Map", HBR (2008) | Organise (job map), Distil (outcomes) | Eight stages: define, locate, prepare, confirm, execute, monitor, modify, conclude. Outcomes as measurable, solution-free statements | The job map is used as a **gap finder**: an empty stage becomes a question. Outcomes are capped at 3–7 per job (ODI often lists 50–150) so practitioners will maintain them. Outcomes are what the review measures against |
| 5 | **After-Action Review** (AAR) | United States Army, TC 25-20 *A Leader's Guide to After-Action Reviews* (1993) | Review | Four questions: what was supposed to happen, what happened, why the difference, what to sustain or improve | "What was supposed to happen" is answered from the job's outcomes and rules; "what happened" from the run's work record. Causes are a fixed list so each routes somewhere. Lessons never change the spec directly: they return to Capture as change requests a person approves |
| 6 | **Specification-Driven Development** (SDD) | Software practice, e.g. GitHub Spec Kit (2025); presented for AEC at Autodesk University 2026 (class BES1245) | The idea of the whole repository | A versioned specification that agents implement and humans review | Renamed **Design-Driven Specification**: the owner's design intent drives the spec, which drives the agent. The spec is built from captured practice, not written up front |
| 7 | **Plan–Do–Check–Act** | W. Edwards Deming (after Walter Shewhart); continual improvement in ISO 9001 | The loop as a quality cycle | Improvement is a cycle with a check step | Plan = Capture–Organise–Distil; Do = Express; Check = Review; Act = approved change requests |

Technical conventions, not frameworks: JSON Schema (draft 2020-12), JSON Lines for observations, Semantic Versioning for packs, YAML front-matter for rules.

---

## 1. CODE (Tiago Forte)

**Source.** Forte's CODE method describes how a person turns information into output: *Capture* what resonates, *Organize* for action, *Distill* to the essence, *Express* in your own work.

**What we take.** The four-phase arc, and the idea that capture is broad and organising is for action, not for filing.

**How we adapted it.**
- *Capture* takes three kinds of source: **told** (a person explains), **found** (harvested from artefacts), **documented** (protocols, manuals, videos). Forte's capture is personal; ours is organisational and includes machine extraction.
- *Organise* is done against the **job**, not a folder system (Forte's PARA). The job map replaces PARA's projects/areas/resources/archives.
- *Distill* has a hard rule Forte doesn't need: **AI distils, a person confirms.** Distilled items carry a `basis` label; AI can reach `seen`, only a person reaches `confirmed`.
- *Express* is **the job done**: by a person, a script or AI, leaving a work record.
- **Review** is added as a fifth phase (from the AAR, below), because a specification that agents act on needs a feedback loop a personal notebook does not.

## 2. Jobs to be Done (Christensen)

**Source.** Customers "hire" products to make progress in a particular circumstance; understanding the job (functional, emotional, social) explains behaviour better than demographics or features.

**What we take.** Study the job, not the role or the tool. Jobs have functional, emotional and social sides. Things are "hired" for jobs.

**How we adapted it.**
- The job is done **inside** the practice, by its own people, for its own clients.
- **Hired** becomes a field on every step: `now` and `next` (person, script, AI, AI-with-person) plus `finalYes`. This is how the method shows where AI takes over, step by step.
- The emotional and social sides are captured as **must not go wrong**: they mark where a person keeps the final yes.

## 3. Job stories (Intercom; Klement)

**Source.** "When [situation], I want to [motivation], so I can [expected outcome]": a story that starts from the situation rather than a persona.

**What we take.** The format, verbatim, as the `jobStory` field (`when`, `iWantTo`, `soICan`).

**How we adapted it.** Stories are gathered from **several roles** for the same job (doer, checker, principal); where their stories differ is a finding. The story carries a `basis` label like everything else.

## 4. Outcome-Driven Innovation (Ulwick; Bettencourt & Ulwick)

**Source.** Every job can be mapped onto eight universal stages, and customers judge success by desired outcomes, measurable statements free of any solution (e.g. "minimise the time it takes to …").

**What we take.** The eight stages as the `jobMap` enum. Outcome statements as `outcomes`.

**How we adapted it.**
- The map is a **gap finder**. A stage with no step is recorded as `gap` with a question. (In practice, *confirm*, *monitor* and *modify* are the stages most often empty: checks before work, watching during work, and rework after comments.)
- Outcomes are **few** (3–7, max 12 in the schema), written as "Reduce the chance that …" / "Reduce the time it takes to …", and each links to rules or a question.
- Outcomes are not ranked by importance/satisfaction surveys as in ODI. They are the yardstick for the AAR.

## 5. After-Action Review (US Army)

**Source.** A structured, blame-free discussion after an event: what was supposed to happen, what actually happened, why there was a difference, what to sustain and improve.

**What we take.** The four questions, per reviewed item. Quick (informal) and deep (formal) reviews.

**How we adapted it.**
- **Supposed** is cited from the job's outcomes and rules; **happened** from the run's work records. Neither is from memory.
- **Why** is one of six causes (`standard-gap`, `execution-error`, `mapping-gap`, `project-specific`, `preference`, `unknown`), each with a destination.
- **Sustain/improve** becomes `keep` / `change`, and a change is a **change request** returned to Capture, never an edit to the spec.
- A review counts only with a **named reviewer and a stated scope**. It reviews the AI's work, not the reviewer.

## 6. Specification-Driven Development → Design-Driven Specification

**Source.** In SDD, a written specification is the source of truth; agents generate implementation from it; humans review against it.

**What we take.** Spec as source of truth, versioned; agents implement; humans review.

**How we adapted it.** The name is **Design-Driven Specification (DDS)**: in design practice the intent comes first and the spec is captured from how good work is already done, rather than written up front by an analyst. Specs are layered (base → firm/client → project), and every item says where it stands on evidence.

## 7. Plan–Do–Check–Act (Deming)

**Source.** Continual improvement as a repeating cycle; the basis of ISO 9001's improvement clause.

**How it maps.** Plan = Capture, Organise, Distil · Do = Express · Check = Review · Act = approved change requests. This lets a practice explain DDS to a quality auditor in terms they already use.

---

## What DDS adds of its own

- **Three labels, kept apart:** `basis` (unset · borrowed · seen · confirmed), `lifecycle` (draft · active · retired), `severity` (must · should · may).
- **Observations before interpretation:** harvesters write facts; analysis cites them.
- **Packs and layers:** base → firm/client → project, with overrides by id.
- **Adapters:** the core never names a host application.
- **Work records:** every step leaves evidence a review can compare against.
