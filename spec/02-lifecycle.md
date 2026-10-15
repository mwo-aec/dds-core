# 02 — Lifecycle: phase contracts

version 0.1.0

Each phase has inputs, outputs, what AI may and may not do, and a definition of done. Sources for each phase's framework are in `05-foundations.md`. The loop is **Capture → Organise → Distil → Express → Review**, and Review feeds back into Capture.

---

## C · Capture

*Built on:* CODE *Capture* (Forte) · JTBD interview (Christensen) · job stories (Intercom; Klement). *Skill:* `skills/dds-capture`.

Gather everything that shows how the job is done.

**Three kinds of source**

| Kind | Examples | How it is read |
|---|---|---|
| **told** | interview, conversation, answer to a question, minutes, voice note | transcript → summarised by AI, quotes kept verbatim |
| **found** | family library, model, drawing set, scripts in use | a **harvester**: deterministic tool → observations |
| **documented** | protocol, standards manual, training video, checklist | read by AI or a person → observations with `method: ai-assisted` or `manual`; spot-checked |

**Inputs:** access to people, artefacts and documents; the job (if one exists yet).
**Outputs:** `SRC-` sources; `CAP-` capture runs; `OBS-` observations (JSONL).
**AI may:** run approved harvesters; transcribe and summarise told sources; read documents into observations; file sources.
**AI may not:** interpret during capture (no "this means…" in an observation); guess a value it could not read; copy confidential material into a public pack.
**Done when:** every source is filed with kind, medium, owner and confidentiality; every capture run lists what it read, its counts and its problems.

**The JTBD interview** (told sources): ask about the last real time the job was done, not how it should be done. Template: `templates/interview-jtbd.md`.

---

## O · Organise

*Built on:* the universal job map (Bettencourt & Ulwick). *Skill:* `skills/dds-organise`.

Put the job in order.

**Inputs:** sources and observations.
**Outputs:** a `JOB-` (method card). Part A: job story, told by, owner, outcomes (drafted), must-not-go-wrong. Part B: the job map (eight stages: define, locate, prepare, confirm, execute, monitor, modify, conclude), steps, tasks (`ai-does`, `ai-asks`, `person-decides`), who is hired now.
**AI may:** draft the job story from told sources; place steps on the job map; split steps into tasks; mark empty stages as gaps and raise a question for each.
**AI may not:** invent steps nobody described or nothing shows; set who is hired next without the owner.
**Done when:** every stage has a step or a gap with a question; the owner has read the job story and agreed it says what they do.

---

## D · Distil

*Built on:* CODE *Distill* (Forte) · desired outcome statements (Ulwick). *Skill:* `skills/dds-distil`.

Turn the job into outcomes, rules, checks and questions.

**Inputs:** the job; observations; documented sources.
**Outputs:**
- **Outcomes** (in the job): 3–7 measurable, tool-free statements ("Reduce the chance that …").
- **Rules** (`rules/<area>/<name>.md`): the rule in words, `## Why`, `## Examples`, `## Open questions`; front-matter per `rule` schema.
- **Checks** (`*.checks.json`): deterministic tests a script can run.
- **Questions** (`Q-`): one per gap, contradiction or missing why.

**How analysis works on observations** (any domain):
1. **Group** observations by subject kind and aspect.
2. **Find patterns**: dominant conventions (naming styles, prefixes, values, structures) with their share, e.g. "38 of 42 families use `TXT_` for text parameters".
3. **Find exceptions**: outliers, near-duplicates, conflicts. An exception is a question ("exception or mistake?"), not a rule.
4. **Draft rules** only from patterns with clear support. `basis: seen`, `evidence` citing a sample of observation ids and the counts.
5. **Draft checks** where the pattern is mechanical.
6. **Compare** with documented and told sources: agreement strengthens a rule; disagreement is a `contradiction` question.
7. **Ask** for intent: every rule drafted from found evidence carries at least one `intent` or `confirm` question until confirmed.

**AI may:** draft all of the above; label `seen`; run checks over observations to test a draft (conformance).
**AI may not:** label anything `confirmed`; drop an exception to make a pattern look cleaner; state a rule without evidence.
**Done when:** every outcome links to at least one rule or a question; every `seen` rule cites evidence; the standards owner has the questions.

**Confirming:** the standards owner answers questions and confirms rules. The answer is filed as a told source; the rule moves to `confirmed` with `confirmed.by/at/source`, through a change request if the pack is already in use.

---

## E · Express

*Built on:* CODE *Express* (Forte), read as the job done · Specification-Driven Development. *Skill:* `skills/dds-express`.

Do the job, against the specification.

**Inputs:** a request; the job; the resolved pack stack (see `03-packs-and-layers.md`); approved tools; resources.
**Outputs:** a `RUN-` with, per step, who did it, which tools, the result and the **work records**; the artefact(s) produced; questions raised.
**AI may:** do steps it is hired for; call approved tools; generate artefacts in a scratch location; run checks on what it made.
**AI may not:** write to the owner's design of record without the step's final yes; use a rule that is `retired`; treat `could-not-check` as a pass.
**Done when:** every step has a result and its work records; checks were run and their results recorded; the output is where the request said.

A run's readable form for people is the **procedure**: the job's steps, in order, with what "right" looks like. Same method, written for a person.

---

## AAR · Review

*Built on:* After-Action Review (US Army, TC 25-20) · PDCA (Deming). *Skill:* `skills/dds-review`.

Compare what happened with what was supposed to happen.

**Inputs:** the run and its work records; the job's outcomes and rules.
**Outputs:** a `REV-` with items; `CR-` change requests; new `Q-` questions.

**The four questions, per item**
1. **What was supposed to happen?** The outcome or rule (cite it).
2. **What actually happened?** From the work record (cite it).
3. **Why the difference?** One cause: `standard-gap`, `execution-error`, `mapping-gap`, `project-specific`, `preference`, `unknown`.
4. **What do we keep or change?** A change request or a question.

**Two depths:** *quick* (every run: accept, change or reject each finding; AI asks "why?" once, batched) and *deep* (early runs, and before handing more of a step to AI).

**Where causes go**

| Cause | Goes to |
|---|---|
| standard-gap | question to the standards owner → maybe a new rule |
| execution-error | the tool or step that failed; no rule change |
| mapping-gap | the adapter or tool |
| project-specific | a project pack, not the firm's |
| preference | ask the owner whether it's their standard; otherwise drop |
| unknown | question |

**AI may:** draft reviews from a person's markings; propose change requests; raise questions.
**AI may not:** count a review without a named person and stated scope; learn from changes made by others to things it did not touch; apply a change request.
**Done when:** every changed or rejected item has a cause; every cause has a destination.

**Back to Capture:** answers and approved changes are new captures. They pass through Organise and Distil like any other source, and the pack version goes up.
