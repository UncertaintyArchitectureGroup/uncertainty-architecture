---
title: Interface and Control Patterns
artifact_type: pattern-index
status: draft-normative
maturity: active
module: patterns
topics:
  - thinking-systems
  - model-judgment
  - uncertainty-boundary
  - control-loop
  - constraints
  - containment
  - evidence
  - fallback
  - escalation
  - human-authority
tags:
  - ua/module/patterns
  - ua/type/pattern-index
  - ua/status/draft-normative
  - ua/topic/thinking-systems
  - ua/topic/model-judgment
  - ua/topic/uncertainty-boundary
  - ua/topic/control-loop
  - ua/topic/constraints
  - ua/topic/containment
  - ua/topic/evidence
  - ua/topic/human-authority
canonical_for:
  - patterns-module
---

# Interface and Control Patterns

**Status:** Draft normative  
**Role:** Reusable architectural and socio-technical responses for recurring control problems

## Purpose

This module contains reusable patterns for engineering and operating the boundary between deterministic software responsibilities and probabilistic Model Judgment in Thinking Systems.

Patterns turn UA doctrine into reviewable design choices. They may arrange constraints, technical mechanisms, practical artifacts, responsibility bundles, evidence, economics, and repeatable decision processes when those elements jointly address a recurring control problem.

## Defines

This module defines or develops patterns for:

- separating Judgment Nodes from deterministic control logic;
- making a Judgment Node's purpose, inputs, authority, applicable constraints, realization, evidence, failure handling, and ownership explicit;
- preserving hard invariants around probabilistic behavior;
- expressing soft constraints without confusing them with guarantees;
- translating organizational and project constraints into delivery realization and runtime enforcement;
- validating, gating, retrying, containing, or escalating model outputs;
- maintaining traceability across model-mediated decisions and constraint changes;
- creating procedural interfaces between code, models, tools, Constraints, Human Authority, and corrective action;
- deciding whether a proposed Thinking System has a credible, operable, and economically viable project-level control architecture;
- mapping material risk scenarios to required Constraints, Sensors, Controllers, Actuators, Human Authority, capacity, economics, authorization, and reauthorization;
- connecting Requirements, Judgment Node boundaries, constraint realization, readiness, completion, release decisions, and runtime reassessment through a lightweight SMB-facing delivery review;
- passing an authorized project and constraint baseline into delivery reviews without duplicating the project risk and control model.

## Does not define

This module does not prescribe:

- one universal workflow, orchestration framework, constraint catalogue, or policy engine;
- a fixed implementation technology;
- a mandatory governance department, committee, or organizational structure;
- a mandatory Project Launch Gate meeting;
- a separate registry or document for every Constraint or Judgment Node;
- separate readiness, completion, release, responsibility, risk, financial, constraint, or project-decision artifacts when one coherent review record and linked evidence are sufficient;
- identical controls for systems with different consequences and operating contexts;
- reference architectures as mandatory deployment topologies;
- universal numerical thresholds for acceptable behavior;
- one universal risk score or control-cost formula;
- duplication of project-level assumptions inside every delivery review.

## Pattern expectations

A mature UA pattern should make the following explicit:

1. the recurring problem and operating context;
2. the uncertainty or failure mechanism being addressed;
3. the deterministic responsibilities and Constraints that must remain intact;
4. the proposed technical or socio-technical control structure;
5. the relevant Constraint, Sensor, Controller, and Actuator functions;
6. the artifacts, responsibility bundles, economics, or decision process required to operate it;
7. the evidence or signals needed;
8. escalation, fallback, containment, compensation, rollback, or recovery behavior;
9. important trade-offs and known limits.

Examples and working templates attached to a pattern are informative unless explicitly classified otherwise. Pattern records and review effort should be proportional to authority, downstream impact, constraint strength, exposure, feedback latency, reversibility, and failure consequences.

## Key concepts

- project control architecture and viability;
- project authorization and reauthorization;
- delivery inheritance and constraint realization;
- material risk scenarios;
- Judgment Node;
- Model Judgment placement;
- deterministic boundary;
- authority boundary;
- hard invariant;
- hard and soft Constraint;
- Constraint source, realization, failure behavior, evidence, and change authority;
- Control-Loop Capability Anatomy;
- procedural interface;
- validation and release gates;
- evidence and evaluation;
- control economics;
- responsibility bundles;
- Human Authority;
- fallback and escalation;
- containment of non-determinism;
- runtime reassessment.

## Documents

- [`project-control-architecture-and-viability-review.md`](project-control-architecture-and-viability-review.md) — draft-normative project-level pattern connecting outcome, risk scenarios, intended Judgment and authority, constraint architecture, required capabilities, evidence feasibility, Human Authority, operating capacity, control economics, authorization, delivery inheritance, and reauthorization.
- [`project-control-architecture-and-viability-review-template.md`](project-control-architecture-and-viability-review-template.md) — informative living project-decision template implementing the project-level pattern without separate Project Launch Gate or Constraint Register records.
- [`judgment-node-boundary.md`](judgment-node-boundary.md) — draft-normative pattern for making consequential Model Judgment explicitly constrained, observable, and operable through a minimal or extended boundary.
- [`thinking-system-review.md`](thinking-system-review.md) — draft-normative SMB-facing delivery pattern connecting the inherited project baseline, Requirement, Judgment Nodes, constraint realization, full DoR and DoD extensions, release decision, responsibility bundles, and runtime reassessment.
- [`thinking-system-review-template.md`](thinking-system-review-template.md) — informative living template that records delivery realization, evidence, release, and reassessment without parallel registries.

## Canonical ownership across review levels

The [`Project Control Architecture and Viability Review`](project-control-architecture-and-viability-review.md) is the canonical owner of the project-level risk and consequence model, organizational constraint interpretation, project constraint architecture, intended Judgment and authority landscape, required control capabilities, evidence feasibility, Human Authority and operating capacity, control economics, project authorization, delivery inheritance package, and project reauthorization triggers.

The [`Thinking System Review`](thinking-system-review.md) is the canonical owner of delivery-level Judgment Nodes, Requirement, concrete constraint realization, model-mediated Definition of Ready, Definition of Done, deployment-specific Release Gate, responsibility bundles, and local reassessment for a bounded system, feature, or material change.

The project review authorizes and constrains the project boundary. Delivery reviews inherit that baseline by reference and refine local Judgment Nodes, Requirements, constraint realization, controls, evidence, and deployment scope. A delivery review must not silently broaden project authority, weaken an inherited hard Constraint, change its authoritative source, or rewrite project-level risk, capacity, or economic assumptions.

The templates mirror their owning patterns and must not be treated as independent protocols.

The Judgment Node Boundary pattern includes a compact SMB-facing card directly in the document. The same card is embedded in the Thinking System Review template; the repository does not maintain a separate `judgment-node-record.md` artifact.

The project authorization and delivery release decisions remain inside their respective versioned review artifacts. The repository does not require separate Project Launch Gate, Constraint Register, or Release Decision Record files for the default SMB adoption path.

Individual patterns should use the metadata and status conventions in [`DOCUMENT-METADATA.md`](../DOCUMENT-METADATA.md).

## Relationships

- [`00-doctrine/`](../00-doctrine/) provides the foundational distinctions used by the patterns, including [`Control-Loop Capability Anatomy`](../00-doctrine/control-loop-anatomy.md), [`Nested Control Lifecycle`](../00-doctrine/nested-control-lifecycle.md), [`Model Judgment Placement`](../00-doctrine/model-judgment-placement.md), and [`Requirements, Correctness, and Bugs`](../00-doctrine/requirements-correctness-and-bugs.md).
- [`02-ai-control-plane/`](../02-ai-control-plane/) develops Constraints, Sensors, Controllers, Actuators, Human Authority, and corrective capabilities through which project and delivery decisions are operated.
- [`02-ai-control-plane/01-constraints/`](../02-ai-control-plane/01-constraints/) defines constraint classes, realization, failure behavior, evidence, and authority.
- [`03-reference-architectures/`](../03-reference-architectures/) demonstrates possible combinations of patterns and capabilities.
- [`04-failure-modes/`](../04-failure-modes/) provides the failure mechanisms that patterns should mitigate.
- [`SPECIFICATION.md`](../SPECIFICATION.md) defines the status and normative boundary of this module.
