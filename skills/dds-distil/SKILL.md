---
name: dds-distil
description: Distil phase of the DDS Loop — analyse observations and sources into desired outcomes, rules (seen, with evidence), machine checks and questions for the standards owner. Use after a harvest or capture, to draft or extend a pack's rules. AI drafts; only a person confirms.
---

# DDS · Distil

**Framework:** CODE *Distill* (Forte); desired outcome statements (Ulwick). See `spec/05-foundations.md`.

**Rule of the phase:** **AI distils, a person confirms.** You may set `basis: seen` (with evidence). Never `confirmed`.

## Inputs
The job; observations (`observations.jsonl`); documented and told sources; lower-layer packs (for `borrowed` items).

## Steps
1. **Outcomes.** Draft 3–7 for the job: "Reduce the chance that …" / "Reduce the time it takes to …". No tool names. Source them from what people called good, bad or slow. `basis: seen` with evidence, or `unset`.
2. **Group** observations by subject kind and aspect.
3. **Patterns.** For each group, find the dominant convention and its share ("38 of 42 parameters of kind text start with `TXT_`"). Use a script for counting; don't estimate.
4. **Exceptions.** List outliers, near-duplicates and conflicts. Each is a question (`kind: exception`: "exception or mistake?"), never quietly dropped.
5. **Rules.** Draft a rule only where a pattern has clear support. Front-matter per `schemas/rule.schema.json`: `basis: seen`, `lifecycle: draft`, `evidence` citing counts and sample observation ids, `outcomes` it protects. Body: the rule, `## Why`, `## Examples` (good and bad, from real observations), `## Open questions`.
6. **Checks.** Where the rule is mechanical, write `*.checks.json` (required, forbidden, pattern, allowed-values, range, count, equals, unique).
7. **Test the draft.** Run the checks over the same observations (conformance). A rule that most of the owner's own work fails is probably wrong, or describes an old convention; ask.
8. **Compare** with documented and told sources. Agreement: note it in evidence. Disagreement: a `contradiction` question.
9. **Borrowed.** Lower-layer rules with no evidence either way stay `borrowed`; rules the evidence contradicts get a question, not an override.
10. **Questions.** Every `seen` rule carries at least one `confirm` or `intent` question. Write them so the person can answer in one go; offer options where they help.
11. Write `rules/`, `questions/`, and a `questions.md` view grouped by who must answer.

## Never
Label anything `confirmed`. State a rule without evidence. Drop an exception to make a pattern cleaner. Count by eye.

## Done when
Every outcome links to a rule or a question; every `seen` rule has evidence and a question; checks have been run over the observations and the results noted; the validator passes.

**Confirming (a person):** answers are filed as told sources; confirmed rules get `basis: confirmed` and `confirmed.by/at/source`, through a change request once the pack is in use.

**Next:** `dds-express`.
