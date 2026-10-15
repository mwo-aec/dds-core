# 0001 — One core schema for every DDS

2026-10-15 · status: accepted (draft 0.1.0) · decided by: Machiel Odendaal

## Situation
Two DDS implementations had grown apart: DDS_forAEC (GA pilot; Not set/Borrowed/Seen/Confirmed labels, stages, Notion as the store) and the RaD add-in (Revit families; draft/active status, must/should, rule .md + .checks.json, base → firm/client → project layers). A third use, AI analysis of artefacts in general, needs the same method without Revit in it.

## Options
1. Keep each implementation's own format.
2. Make RaD's format the standard and fit DDS_forAEC to it.
3. A domain-free core schema both align to, with adapters per domain.

## Choice
Option 3. CODE is the cycle; Jobs-to-be-done captures and organises; AI distils and a person confirms; Express is the job done; the After-Action Review feeds back to Capture. Capture covers told, found and documented sources. Three separate labels: `basis`, `lifecycle`, `severity`. Field names follow RaD (camelCase), with `status` and `from` accepted as aliases. Plain Markdown and JSON Schema so any AI can use it; MCP tools are one way to capture, not the format.

## Consequences
- RaD adds `basis` to rules and writes capture runs and observations in the core format; checks keep their names in camelCase.
- DDS_forAEC's labels map one-to-one to `basis`; "stages" are job-map steps.
- New domains are adapters; the core schemas don't change for them.
- Outcomes are a new first-class item (in the job) and are what reviews measure against.
