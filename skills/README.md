# Skills — one per phase of the DDS Loop

Each skill is a self-contained instruction file (`SKILL.md`) an agent loads to do one phase. They are written for any agent; Claude loads them as skills, other agents can read them as prompts.

| Skill | Phase | Framework it applies | Produces |
|---|---|---|---|
| [`dds-capture`](dds-capture/SKILL.md) | Capture | CODE (Forte) · JTBD interview (Christensen; job stories) | Sources, capture runs, observations |
| [`dds-organise`](dds-organise/SKILL.md) | Organise | Job map (Ulwick / Bettencourt) | The job (method card) |
| [`dds-distil`](dds-distil/SKILL.md) | Distil | Desired outcomes (Ulwick) · CODE Distill | Outcomes, rules, checks, questions |
| [`dds-express`](dds-express/SKILL.md) | Express | CODE Express · SDD | Runs, work records, artefacts |
| [`dds-review`](dds-review/SKILL.md) | Review | After-Action Review (US Army) · PDCA (Deming) | Reviews, change requests, questions |

All five share the rules in `AGENTS.md`. Validate output with `python tools/validate.py <pack>`.
