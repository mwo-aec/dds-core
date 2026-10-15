---
id: DDS-NEST-001
title: Nested families
area: nesting
appliesTo: [all]
tags: [nesting, families]
severity: should
lifecycle: draft
basis: borrowed
version: 0.1.0
layer: digital-reframe
overrides: null
jobs: [JOB-CREATE-FAMILY]
outcomes: [OUT-FAM-03, OUT-FAM-04]
questions: [Q-NEST-LIB-001]
created: { by: { kind: person, name: Machiel Odendaal }, at: 2026-10-15, method: authored }
---
Placeholder rule, to be replaced with the Digital Reframe nesting method.

Nest a family as **shared** only when the project must schedule or tag it on its own (for example door hardware). Otherwise nest it as **non-shared**. Drive every nested instance's sizes from host parameters (associate them) instead of fixed values, and use a family-type parameter when users must swap the nested component.

## Why
Shared nested families appear in project schedules and add to file size. Unassociated nested parameters break when the host flexes.

## Examples
- Shared: door handle, sanitary fixture in a washroom group
- Non-shared: profile, leg, decorative panel

## Open questions
- Q-NEST-LIB-001: Where is the approved library nested components come from, and is it authoritative?
