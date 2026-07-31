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

Patterns turn UA doctrine into reviewable design choices. They may arrange technical mechanisms, practical artifacts, responsibility bundles, evidence, economics, and repeatable decision processes when those elements jointly address a recurring control problem.

## Defines

This module defines or develops patterns for:

- separating Judgment Nodes from deterministic control logic;
- making a Judgment Node's purpose, inputs, authority, constraints, evidence, failure handling, and ownership explicit;
- preserving hard invariants around probabilistic behavior;
- expressing soft constraints without confusing them with guarantees;
- validating, gating, retrying, containing, or escalating model outputs;
- maintaining traceability across model-mediated decisions;
- creating procedural interfaces between code, models, tools, and Human Authority;
- deciding whether a proposed Thinking System has a credible, operable, and economically viable project-level control architecture;
- mapping material risk scenarios to required controls, evidence, Human Authority, capacity, economics, authorization, and reauthorization;
- connecting Requirements, Judgment Node boundaries, readiness, completion, release decisions, and runtime reassessment through a lightweight SMB-facing delivery review;
- passing an authorized project baseline into delivery reviews without duplicating the project risk and control model.

## Does not define

This module does not prescribe:

- one universal workflow or orchestration framework;
- a fixed implementation technology;
- a mandatory governance department, committee, or organizational structure;
- a mandatory Project Launch Gate meeting;
- a separate registry or document for every Judgment Node;
- separate readiness, completion, release, responsibility, risk, financial, or project-decision artifacts when one coherent review record and linked evidence are sufficient;
- identical controls for systems with different consequences and operating contexts;
- reference architectures as mandatory deployment topologies;
- universal numerical thresholds for acceptable behavior;
- one universal risk score or control-cost formula;
- duplication of project-level assumptions inside every delivery review.

## Pattern expectations

A mature UA pattern should make the following explicit:

1. the recurring problem and operating context;
2. the uncertainty or failure mechanism being addressed;
3. the deterministic responsibilities that must remain intact;
4. the proposed technical or socio-technical control structure;
5. the artifacts, responsibility bundles, economics, or decision process required to operate it;
6. the evidence or signals needed;
7. escalation, fallback, containment, or recovery behavior;
8. important trade-offs and known limits.

Examples and working templates attached to a pattern are informative unless explicitly classified otherwise. Pattern records and review effort should be proportional to authority, downstream impact, exposure, feedback latency, reversibility, and failure consequences.

## Key concepts

- project control architecture and viability;
- project authorization and reauthorization;
- delivery inheritance;
- material risk scenarios;
- Judgment Node;
- Model Judgment placement;
- deterministic boundary;
- authority boundary;
- hard invariant;
- soft constraint;
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

- [`project-control-architecture-and-viability-review.md`](project-control-architecture-and-viability-review.md) — draft-normative project-level pattern connecting outcome, risk scenarios, intended Judgment and authority, required controls, evidence feasibility, Human Authority, operating capacity, control economics, authorization, delivery inheritance, and reauthorization.
- [`project-control-architecture-and-viability-review-template.md`](project-control-architecture-and-viability-review-template.md) — informative living project-decision template implementing the project-level pattern without a separate Project Launch Gate record.
- [`judgment-node-boundary.md`](judgment-node-boundary.md) — draft-normative pattern for making consequential Model Judgment explicit, bounded, observable, and operable through a minimal or extended boundary.
- [`thinking-system-review.md`](thinking-system-review.md) — draft-normative SMB-facing delivery pattern connecting the Requirement, Judgment Nodes, full DoR and DoD extensions, release decision, responsibility bundles, and runtime reassessment through one lightweight flow for a bounded system, feature, or material change.
- [`thinking-system-review-template.md`](thinking-system-review-template.md) — informative working template that implements the Thinking System Review as one living, versioned artifact.

## Canonical ownership across review levels

The [`Project Control Architecture and Viability Review`](project-control-architecture-and-viability-review.md) is the canonical owner of the project-level risk and consequence model, intended Judgment and authority landscape, required control capabilities, evidence feasibility, Human Authority and operating capacity, control economics, project authorization, delivery inheritance package, and project reauthorization triggers.

The [`Thinking System Review`](thinking-system-review.md) is the canonical owner of the delivery-level model-mediated Definition of Ready, Definition of Done, deployment-specific Release Gate, responsibility bundles, and local reassessment flow for a bounded system, feature, or material change.

The project review authorizes and constrains the project boundary. Delivery reviews inherit that baseline by reference and refine local Judgment Nodes, Requirements, controls, evidence, and deployment scope. A delivery review must not silently broaden project authority or rewrite project-level risk, capacity, or economic assumptions.

The templates mirror their owning patterns and must not be treated as independent protocols.

The Judgment Node Boundary pattern includes a compact SMB-facing card directly in the document. The same card is embedded in the Thinking System Review template; the repository does not maintain a separate `judgment-node-record.md` artifact.

The project authorization and delivery release decisions remain inside their respective versioned review artifacts. The repository does not require separate Project Launch Gate or Release Decision Record files for the default SMB adoption path.

Individual patterns should use the metadata and status conventions in [`DOCUMENT-METADATA.md`](../DOCUMENT-METADATA.md).

## Relationships

- [`00-doctrine/`](../00-doctrine/) provides the foundational distinctions used by the patterns, including [`Uncertainty in the Controlled Object`](../00-doctrine/uncertainty-in-the-controlled-object.md), the [`Model Judgment Placement`](../00-doctrine/model-judgment-placement.md) taxonomy, and the [`Requirements, Correctness, and Bugs`](../00-doctrine/requirements-correctness-and-bugs.md) model.
- [`02-ai-control-plane/`](../02-ai-control-plane/) provides the constraints, sensors, controllers, actuators, Human Authority, and corrective capabilities through which project and delivery decisions are operated.
- [`03-reference-architectures/`](../03-reference-architectures/) demonstrates possible combinations of patterns, including the [`Judgment Placement Reference Architectures`](../03-reference-architectures/judgment-placement-examples.md) and completed delivery-level review example.
- [`04-failure-modes/`](../04-failure-modes/) provides the failure mechanisms that patterns should mitigate.
- [`SPECIFICATION.md`](../SPECIFICATION.md) defines the status and normative boundary of this module.
