---
title: Research-to-Framework Traceability
artifact_type: research-traceability
status: draft
created: 2026-07-24
updated: 2026-07-24
license: CC-BY-4.0
---

# Research-to-Framework Traceability

## Purpose

This document records how reviewed UA research may influence future framework components.

It prevents two opposite errors:

1. building methodology without preserving the research and reasoning behind it;
2. treating every statement from an article as if it were already an approved requirement.

## Status vocabulary

- **Research Finding** — preserved conclusion from a reviewed source.
- **Candidate** — potentially suitable for translation into a framework component.
- **Needs Resolution** — terminology, evidence, scope, or contradiction must be resolved first.
- **Proposed for RFC** — mature enough for formal review.
- **Active** — accepted into the normative framework.
- **Superseded** — replaced by a later formulation.
- **Rejected** — considered and intentionally not adopted.

## Candidate framework areas

Traceability entries may point toward:

- **Doctrine** — foundational concepts and distinctions;
- **Lifecycle** — how teams analyze, design, build, release, operate, and recalibrate systems;
- **Pattern** — repeatable technical or socio-technical solution;
- **Operating Model** — decision rights, responsibilities, reviews, and escalation;
- **Reference Architecture** — concrete composition of multiple patterns;
- **Artifact** — canvas, checklist, registry, evidence record, risk map, or other reusable tool;
- **Failure Mode** — recurring mechanism of technical, semantic, operational, or organizational failure.

## Traceability matrix

No research source has been formally reviewed under this process yet.

Rows will be added source by source through separate Draft Pull Requests.

| Research finding | Primary source | Candidate framework area | Status | Work required before normative adoption |
|---|---|---|---|---|

## Conflict and evolution register

This section will record cross-source issues that cannot be resolved inside a single source review.

| Topic | Earlier formulation | Later formulation | Current status | Resolution path |
|---|---|---|---|---|

Initial topics expected to require review include:

- Behavioral Software / Behavioral Applications versus a possible Thinking Systems taxonomy;
- the relationship between Thinking Systems and agentic systems;
- Model Control Plane versus Model Context Protocol acronym conflict;
- AI Control Plane as platform, architectural layer, capability, or pattern vocabulary;
- actuators versus constraints as separate control categories;
- automated controller logic versus the socio-technical controller;
- specialized AI role titles versus responsibility bundles assigned to existing roles;
- illustrative evaluation thresholds versus risk-derived normative thresholds.

## Update rule

A source review pull request may add only the findings and conflicts supported by that source and its analysis.

Repository-wide terminology or methodology changes require separate review after the research series has been synthesized.
