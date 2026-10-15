# 06 — Glossary

version 0.1.0 · Origin column: where the term comes from (see `05-foundations.md`). "DDS" = coined or defined here.

| Term | Meaning | Origin |
|---|---|---|
| **Adapter** | The domain-specific part: subject kinds, aspects, harvesters, check operations, generators, resources, analysis hints | DDS |
| **After-Action Review (AAR)** | The Review phase: four questions per item, measured against outcomes | US Army, adapted |
| **Aspect** | A dotted name for one fact about a subject: `name`, `parameter.group` | DDS |
| **Basis** | Where an item stands on evidence: `unset`, `borrowed`, `seen`, `confirmed` | DDS |
| **Borrowed** | Taken from a lower layer or a framework default, not yet checked for this owner | DDS |
| **Capture** | Phase 1: gather told, found and documented sources | Forte (CODE), adapted |
| **Capture run** | One pass of a harvester or capture session over a scope (`CAP-`) | DDS |
| **Cause** | Why a reviewed result differed: `standard-gap`, `execution-error`, `mapping-gap`, `project-specific`, `preference`, `unknown` | DDS, from AAR |
| **Change request** | A proposed change to a pack, approved by a person before it applies (`CR-`) | DDS |
| **Check** | A deterministic test of a rule, runnable by a script (`<rule>.<name>`) | DDS |
| **CODE** | Capture, Organise, Distil, Express: the phases of the loop | Forte |
| **Confirmed** | A named person with authority has confirmed the item; only a person can set it | DDS |
| **DDS (Design-Driven Specification)** | An owner's way of doing a job, written as a versioned specification agents act on and people review | DDS, from SDD |
| **DDS Core** | This framework: method, schemas, phase contracts, adapters | DDS |
| **DDS Loop** | Capture → Organise → Distil → Express → Review → (back to) Capture | DDS |
| **Deep review** | A deliberate debrief: early runs, and before handing more of a step to AI | AAR (formal review) |
| **Desired outcome** | A measurable, tool-free statement of success for the job (`OUT-`) | Ulwick (ODI), adapted |
| **Distil** | Phase 3: draft outcomes, rules, checks and questions from what was captured. AI distils, a person confirms | Forte (CODE), adapted |
| **Documented source** | Guidance someone wrote or recorded: protocol, manual, training video | DDS |
| **Evidence** | The observations, sources, runs or reviews an item rests on | DDS |
| **Express** | Phase 4: the job done by whoever is hired for each step, with work records | Forte (CODE), adapted |
| **Final yes** | A person must approve a step's result before it counts | DDS |
| **Found source** | An artefact the practice already made, read by a harvester | DDS |
| **Gap** | A job-map stage no step covers; always carries a question | DDS, from ODI |
| **Generator** | A tool that produces an artefact in the Express phase | DDS |
| **Harvester** | A deterministic, read-only tool that turns artefacts into observations | DDS |
| **Hired** | Who does a step: `person`, `script`, `ai`, `ai-with-person`; `now` and `next` | Christensen (JTBD), adapted |
| **Job** | What the owner needs done; the unit everything hangs from (`JOB-`) | Christensen (JTBD) |
| **Job map** | The job's steps placed on eight stages: define, locate, prepare, confirm, execute, monitor, modify, conclude | Ulwick / Bettencourt (ODI) |
| **Job story** | *When … I want to … so I can …* | Intercom; Klement |
| **Layer** | A pack's level: `base`, `firm`, `client`, `project`; higher layers add and override | DDS |
| **Lesson** | What a review learns; becomes a change request or a question | AAR, adapted |
| **Lifecycle** | Whether an item is in use: `draft`, `active`, `retired` (RaD: `status`) | DDS |
| **Method card** | The human view of a job: Part A the job (stable), Part B the method (current) | DDS |
| **Must not go wrong** | The emotional and social stakes of a job; marks where a person keeps the final yes | JTBD (emotional/social jobs), adapted |
| **Observation** | One fact read from a source: subject, aspect, value, extractor (`OBS-`) | DDS |
| **Organise** | Phase 2: put the job in order on the job map | Forte (CODE), adapted |
| **Outcome** | See desired outcome | |
| **Owner** | The person responsible for a job or a pack's content | DDS |
| **Pack** | One layer of a DDS on disk, described by `dds.json` | DDS |
| **Procedure** | The readable form of a job's method for people | DDS |
| **Question** | A gap, contradiction or missing why only a person can settle (`Q-`) | DDS |
| **Quick review** | The every-run review: accept, change or reject each finding | AAR (informal review) |
| **Resource** | A library or reference runs pull from: family library, parameter file, template (`RES-`) | DDS |
| **Review** | Phase 5, the AAR; also the record of one (`REV-`) | US Army, adapted |
| **Rule** | A clause the work must meet, with its basis, lifecycle and severity | DDS |
| **Run** | One time a job was done, with work records per step (`RUN-`) | DDS |
| **SDD (Specification-Driven Development)** | The software practice DDS adapts | Industry |
| **Seen** | Evidenced in the owner's own material but not confirmed; the highest basis AI may set | DDS |
| **Severity** | How strict: `must`, `should`, `may` | DDS (RaD) |
| **Source** | Anything captured: told, found or documented (`SRC-`) | DDS |
| **Standards owner** | The person with authority to confirm rules for a pack | DDS |
| **Step** | One part of the job on the job map (`STEP-`) | DDS, from ODI |
| **Subject** | The thing an observation or check is about; its kind comes from the adapter | DDS |
| **Task** | A piece of a step: `ai-does`, `ai-asks`, `person-decides` (`TASK-`) | DDS |
| **Told source** | A person's account: interview, answer, minutes | DDS |
| **Tool** | A registered script, MCP tool, skill or template for a known step (`TOOL-`) | DDS |
| **Unset** | Nobody has said yet | DDS |
| **Work record** | What a step leaves behind: image, structured read, calculation, step log, report, artefact | DDS |
