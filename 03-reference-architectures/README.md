---
title: Reference Architectures
artifact_type: reference-index
status: reference
maturity: active
module: reference-architectures
topics:
  - thinking-systems
  - model-judgment
  - uncertainty-boundary
  - ai-control-plane
  - containment
tags:
  - ua/module/reference-architectures
  - ua/type/reference-index
  - ua/status/reference
  - ua/topic/thinking-systems
  - ua/topic/model-judgment
  - ua/topic/uncertainty-boundary
  - ua/topic/ai-control-plane
canonical_for:
  - reference-architectures-module
---

# Reference Architectures

**Status:** Reference  
**Role:** Concrete, non-prescriptive compositions of UA concepts and patterns

## Purpose

This module contains concrete architectures that demonstrate how Uncertainty Architecture may be applied in real systems.

Reference architectures make abstract responsibilities visible: where Model Judgment occurs, which deterministic boundaries surround it, how evidence is collected, who or what controls change, and how failure is contained.

## Provides

This module provides:

- worked architectural compositions;
- completed illustrative applications of UA review patterns;
- examples of deterministic and probabilistic responsibility boundaries;
- possible distributions of AI Control Plane capabilities;
- implementation-oriented demonstrations of UA patterns;
- explicit assumptions, trade-offs, and unresolved design choices where available.

## Does not define

This module does not prescribe:

- a mandatory system topology;
- a required pipeline of Input Interpretation, Decision Logic, and Output Mediation;
- one preferred vendor, framework, or orchestration platform;
- universal controls or thresholds for every consequence level or operating context;
- conformance merely through copying an example;
- any reference implementation as the UA standard itself.

Illustrative evidence, dates, thresholds, and results in a worked reference are not production claims or UA defaults unless the document explicitly supplies independently verifiable evidence and the owning specification accepts the resulting decision.

## Reference expectations

A mature reference architecture should identify:

1. the operating context and intended outcomes;
2. where probabilistic judgment occurs;
3. the deterministic boundaries and invariants;
4. relevant actuators, sensors, and controllers;
5. decision authority and human involvement;
6. failure, escalation, rollback, and containment paths;
7. known assumptions, limits, and trade-offs.

Examples should link to canonical doctrine and patterns rather than redefine terms or duplicate complete operational checklists.

## Current scope

- [`judgment-placement-examples.md`](judgment-placement-examples.md) presents four minimal architectures: Input Interpretation only, Decision Logic only, Output Mediation only, and one composite Thinking System.
- [`worked-thinking-system-review-support-triage.md`](worked-thinking-system-review-support-triage.md) provides one fully populated, realistically bounded Thinking System Review for human-supervised support triage and grounded reply drafting. Its evidence is explicitly illustrative rather than a claim about a real deployment.
- Indranet remains an implementation-oriented expression of UA concepts. It is a reference, not the specification itself, and its design choices are not automatically normative.

## Suggested reader path

[`Model Judgment Placement`](../00-doctrine/model-judgment-placement.md)
→ [`Judgment Node Boundary`](../01-patterns/judgment-node-boundary.md)
→ [`Thinking System Review`](../01-patterns/thinking-system-review.md)
→ [`Judgment Placement Reference Architectures`](judgment-placement-examples.md)
→ [`Worked Support Triage Review`](worked-thinking-system-review-support-triage.md)

## Documents

- [`judgment-placement-examples.md`](judgment-placement-examples.md) — reference architectures showing isolated and composite placement classes with deterministic boundaries, authority, evidence, fallback, risks, and review focus.
- [`worked-thinking-system-review-support-triage.md`](worked-thinking-system-review-support-triage.md) — completed illustrative review covering three Judgment Nodes, a bounded experiment, full DoR and DoD decisions, residual risk, a human-supervised Release Gate, runtime control, and framework-application observations.

Individual reference architectures should declare `status: reference` and follow [`DOCUMENT-METADATA.md`](../DOCUMENT-METADATA.md).

## Relationships

- [`00-doctrine/`](../00-doctrine/) provides the conceptual foundation.
- [`01-patterns/`](../01-patterns/) provides reusable architectural and socio-technical building blocks.
- [`02-ai-control-plane/`](../02-ai-control-plane/) provides the control capability model used in compositions.
- [`04-failure-modes/`](../04-failure-modes/) provides failure mechanisms that references should address explicitly.
- [`SPECIFICATION.md`](../SPECIFICATION.md) defines why reference architectures remain outside the mandatory topology of the specification.
