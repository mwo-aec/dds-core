---
id: DDS-PARAM-003
title: Family identity parameters
area: parameters
appliesTo: [all]
tags: [parameters, identity, data, authoring]
severity: must
lifecycle: active
basis: confirmed
version: 1.1.0
layer: digital-reframe
overrides: null
jobs: [JOB-CREATE-FAMILY]
outcomes: [OUT-FAM-01]
confirmed:
  by: { kind: person, name: Machiel Odendaal, role: standards owner }
  at: 2026-10-15
  note: Authored by the standards owner in RaD base DDS 0.2.0
  source: SRC-RAD-BASE-DDS
questions: [Q-PARAM-003-001]
created: { by: { kind: person, name: Machiel Odendaal }, at: 2026-10-15, method: authored }
---
Every family Digital Reframe authors carries these identity parameters. They are **family parameters**, not loaded from a shared parameter file. They are **type** parameters in the **Data** group (PG_DATA), and the fixed ones are locked with a formula so they can't be changed per type:

| Name | Data type | Value |
|---|---|---|
| `TXT_Company` | Text | formula `"Digital Reframe"` |
| `URL_Website` | URL | value `www.digitalreframe.tech` (URL parameters can't take a formula) |
| `TXT_Creator` | Text | formula `"Machiel Odendaal"` |
| `TXT_Origin` | Text | formula `"South Africa"` |
| `TXT_Cat Type` | Text | empty, filled in per family |

## Why
The family carries its own origin wherever it goes, without depending on a shared parameter file clients may not have. A formula stops the values drifting between types or being edited in the project.

## Examples
- Good: `TXT_Company` as a type parameter in Data with formula `"Digital Reframe"`.
- Bad: `Company` (no type code); `TXT_Company` loaded from a shared parameter file; `TXT_Company` as an instance parameter.

## Open questions
- Q-PARAM-003-001: Should `TXT_Creator` be the person who authored the family, or always the company owner?
