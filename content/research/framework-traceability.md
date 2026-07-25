---
title: Research-to-Framework Traceability
artifact_type: research-traceability
status: draft
created: 2026-07-24
updated: 2026-07-25
license: CC-BY-4.0
---

# Research-to-Framework Traceability

## Purpose

This document records how UA research may influence framework components without treating every historical statement as an approved requirement.

It prevents two opposite errors:

1. building methodology without preserving the research and reasoning behind it;
2. treating every statement from an article, talk, or working note as if it were already normative.

Traceability is a synthesis aid, not a mandatory ledger for every source or sentence.

## Status vocabulary

- **Research Finding** — a conclusion preserved from research material.
- **Candidate** — potentially suitable for translation into a framework component.
- **Needs Resolution** — terminology, evidence, scope, or contradiction must be resolved first.
- **Proposed for RFC** — mature enough for formal review.
- **Active** — accepted into the normative framework.
- **Superseded** — replaced by a later formulation.
- **Rejected** — considered and intentionally not adopted.

## Candidate framework areas

Traceability entries may point toward:

- **Doctrine** — foundational concepts and distinctions;
- **Pattern** — repeatable technical or socio-technical solution;
- **Operating Model** — decision rights, responsibilities, reviews, and escalation;
- **Reference Architecture** — concrete composition of multiple patterns;
- **Artifact** — canvas, checklist, registry, evidence record, risk map, or other reusable tool;
- **Failure Mode** — recurring mechanism of technical, semantic, operational, or organizational failure.

Lifecycle concerns may be represented across these areas rather than maintained as a separate top-level specification module unless the framework later adopts one explicitly.

## Traceability matrix

The historical publication corpus is preserved, but corpus-level synthesis is still in progress. Entries should be added when a finding is sufficiently clear to support a framework decision, terminology review, contradiction review, or future RFC.

The matrix does not need to be populated source by source before synthesis begins.

| Research finding | Source or synthesis | Candidate framework area | Status | Work required before normative adoption |
|---|---|---|---|---|

## Conflict and evolution register

This section records cross-source issues that cannot be resolved inside simple editorial preservation work.

| Topic | Earlier formulation | Later formulation | Current status | Resolution path |
|---|---|---|---|---|
| Primary system category | Behavioral Software / Behavioral Applications | Thinking Systems | Active | Use Thinking Systems in current framework documents; preserve legacy wording in historical sources with an explanatory terminology note |

Initial topics expected to require further review include:

- the relationship between Thinking Systems and agentic systems;
- Model Control Plane versus Model Context Protocol acronym conflict;
- AI Control Plane as platform, architectural layer, capability, or pattern vocabulary;
- actuators versus constraints as separate control categories;
- automated controller logic versus the socio-technical controller;
- specialized AI role titles versus responsibility bundles assigned to existing roles;
- illustrative evaluation thresholds versus risk-derived normative thresholds.

## Update rule

A research change may add findings and conflicts supported by a single source, multiple sources, a research note, or an explicit synthesis.

Entries should remain concise and decision-oriented. Detailed argument belongs in the supporting analysis or synthesis document.

Repository-wide terminology or methodology changes require separate deliberate framework review. A traceability entry alone does not activate a normative requirement.
