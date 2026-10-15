---
name: dds-capture
description: Capture phase of the DDS Loop — gather told, found and documented sources for a job into a DDS pack (sources, capture runs, observations). Use when interviewing someone about how they work, harvesting artefacts, or reading protocols and videos.
---

# DDS · Capture

**Framework:** CODE *Capture* (Tiago Forte), widened to an organisation; the JTBD interview (Christensen) with job stories (Intercom; Klement). See `spec/05-foundations.md`.

**Goal:** everything that shows how the job is done, recorded faithfully, nothing interpreted yet.

## Inputs
- The pack (`dds.json`) and, if it exists, the job (`jobs/JOB-*.json`).
- Access to at least one of: a person, artefacts, documents.

## Three routes

### Told: a person explains
1. Run the interview in `templates/interview-jtbd.md`. Ask about the **last real time** the job was done.
2. File the recording or transcript as a source: `kind: told`, `medium: interview|transcript|message`, `toldBy`.
3. Keep quotes verbatim. Don't summarise into rules yet.
4. Interview at least the **doer** and the **checker** for each job.

### Found: an artefact shows it
1. Find the adapter's harvester (`adapters/<domain>/adapter.md`, `TOOL-` with `phase: capture`).
2. Run it read-only over the scope. Sample large libraries evenly.
3. Write `captures/<CAP-id>/capture.json` (scope, counts, outputs, **problems**) and `observations.jsonl`.
4. One observation = one subject, one aspect, one value, with the extractor. No meanings.
5. Mark client material `confidential`. Keep it out of shared repositories; record path and hash.

### Documented: someone wrote or recorded it
1. File the document or video as a source: `kind: documented`.
2. Where the content is factual and mechanical (a naming table, a parameter list), record it as observations with `extractor.method: ai-assisted` or `manual`.
3. Mark those observations for a spot-check before Distil relies on them.

## Outputs
`sources/SRC-*.json` · `captures/CAP-*/capture.json` · `captures/CAP-*/observations.jsonl`

## Never
- Interpret in an observation ("this means…").
- Guess a value you couldn't read; record a problem instead.
- Copy confidential material into a public pack.

## Done when
Every source has kind, medium, owner and confidentiality; every capture run lists scope, counts, outputs and problems; `python tools/validate.py <pack>` passes.

**Next:** `dds-organise`.
