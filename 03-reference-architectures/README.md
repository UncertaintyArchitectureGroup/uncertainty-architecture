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
  - constraints
  - containment
tags:
  - ua/module/reference-architectures
  - ua/type/reference-index
  - ua/status/reference
  - ua/topic/thinking-systems
  - ua/topic/model-judgment
  - ua/topic/uncertainty-boundary
  - ua/topic/ai-control-plane
  - ua/topic/constraints
canonical_for:
  - reference-architectures-module
---

# Reference Architectures

**Status:** Reference  
**Role:** Concrete, non-prescriptive compositions of UA concepts and patterns

## Purpose

This module contains concrete architectures that demonstrate how Uncertainty Architecture may be applied in real systems.

Reference architectures make abstract responsibilities visible: where Model Judgment occurs, which deterministic responsibilities surround it, which Constraints bound the operating space, how Sensors expose behavior and control health, who or what acts as Controller, which Actuators can change operation, how project and delivery decisions connect, and how failure is contained.

## Provides

This module provides:

- worked architectural compositions;
- completed illustrative applications of UA review patterns;
- examples of deterministic and probabilistic responsibility boundaries;
- possible distributions of Constraints, Sensors, Controllers, and Actuators;
- implementation-oriented demonstrations of UA patterns;
- explicit assumptions, trade-offs, constraint inheritance, realization, reauthorization, and unresolved design choices where available.

## Does not define

This module does not prescribe:

- a mandatory system topology or four physical layers;
- a required pipeline of Input Interpretation, Decision Logic, and Output Mediation;
- one preferred vendor, framework, policy engine, or orchestration platform;
- one universal constraint catalogue;
- universal controls or thresholds for every consequence level or operating context;
- conformance merely through copying an example;
- any reference implementation as the UA standard itself.

Illustrative evidence, dates, thresholds, economics, technologies, and results in a worked reference are not production claims or UA defaults unless the document explicitly supplies independently verifiable evidence and the owning specification accepts the resulting decision.

## Reference expectations

A mature reference architecture should identify:

1. the operating context and intended outcomes;
2. the relevant organizational and project constraint sources;
3. where probabilistic judgment occurs;
4. the deterministic responsibilities and invariants;
5. the concrete constraint realizations and their failure behavior;
6. relevant Sensors and evidence;
7. the Controller and decision authority, including constraint-change authority;
8. Actuators and real corrective actions;
9. Human Authority, fallback, escalation, rollback, compensation, containment, and reauthorization paths;
10. known assumptions, limits, economics, operational friction, and trade-offs.

A reference must classify functions rather than products. A schema may realize a structural Constraint; its violation log may act as a Sensor; a feature flag may act as an Actuator; the person or software deciding a change may act as Controller. One component may perform several functions, and one function may be distributed.

A two-level worked application should distinguish project authorization from the delivery Release Gate, link the versioned authorization and constraint inheritance package, show delivery realization, and distinguish runtime evidence that remains local from evidence requiring project reauthorization or organizational review.

Examples should link to canonical doctrine and patterns rather than redefine terms or duplicate complete operational checklists.

## Current scope

- [`judgment-placement-examples.md`](judgment-placement-examples.md) presents four minimal architectures: Input Interpretation only, Decision Logic only, Output Mediation only, and one composite Thinking System. The examples identify capability functions without making their topologies mandatory.
- [`worked-thinking-system-review-support-triage.md`](worked-thinking-system-review-support-triage.md) provides one fully populated, realistically bounded delivery-level Thinking System Review for human-supervised support triage and grounded reply drafting. Its evidence is explicitly illustrative rather than a claim about a real deployment.
- A two-level project-and-delivery worked application is the next planned reference. It should trace at least one material Constraint from organizational source through project derivation, delivery realization, runtime evidence, and reauthorization.
- Indranet remains an implementation-oriented expression of UA concepts. It is a reference, not the specification itself, and its design choices are not automatically normative.

## Suggested reader path

[`Uncertainty in the Controlled Object`](../00-doctrine/uncertainty-in-the-controlled-object.md)
→ [`Control-Loop Capability Anatomy`](../00-doctrine/control-loop-anatomy.md)
→ [`Nested Control Lifecycle`](../00-doctrine/nested-control-lifecycle.md)
→ [`Project Control Architecture and Viability Review`](../01-patterns/project-control-architecture-and-viability-review.md)
→ [`Constraint Capabilities`](../02-ai-control-plane/01-constraints/)
→ [`Model Judgment Placement`](../00-doctrine/model-judgment-placement.md)
→ [`Judgment Node Boundary`](../01-patterns/judgment-node-boundary.md)
→ [`Thinking System Review`](../01-patterns/thinking-system-review.md)
→ [`Judgment Placement Reference Architectures`](judgment-placement-examples.md)
→ [`Worked Support Triage Review`](worked-thinking-system-review-support-triage.md)

## Documents

- [`judgment-placement-examples.md`](judgment-placement-examples.md) — reference architectures showing isolated and composite placement classes with Constraints, deterministic responsibilities, authority, evidence, corrective action, fallback, risks, and review focus.
- [`worked-thinking-system-review-support-triage.md`](worked-thinking-system-review-support-triage.md) — completed illustrative delivery review covering three Judgment Nodes, bounded experimentation, constraint realization, full DoR and DoD decisions, residual risk, a human-supervised Release Gate, runtime control, and framework-application observations.

Individual reference architectures should declare `status: reference` and follow [`DOCUMENT-METADATA.md`](../DOCUMENT-METADATA.md).

## Relationships

- [`00-doctrine/control-loop-anatomy.md`](../00-doctrine/control-loop-anatomy.md) defines the four logical capability classes.
- [`00-doctrine/nested-control-lifecycle.md`](../00-doctrine/nested-control-lifecycle.md) defines decision ownership, constraint inheritance, and evidence routing.
- [`01-patterns/project-control-architecture-and-viability-review.md`](../01-patterns/project-control-architecture-and-viability-review.md) provides the project-level constraint architecture, decision, and inheritance surface.
- [`01-patterns/thinking-system-review.md`](../01-patterns/thinking-system-review.md) provides the delivery-level realization, readiness, completion, release, and local reassessment surface.
- [`02-ai-control-plane/`](../02-ai-control-plane/) provides the capability model used in compositions.
- [`02-ai-control-plane/01-constraints/`](../02-ai-control-plane/01-constraints/) provides the constraint capability and implementation-oriented catalog.
- [`04-failure-modes/`](../04-failure-modes/) provides failure mechanisms that references should address explicitly.
- [`SPECIFICATION.md`](../SPECIFICATION.md) defines why reference architectures remain outside the mandatory topology of the specification.
