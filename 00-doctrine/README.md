---
title: Core Doctrine
artifact_type: doctrine
status: draft-normative
maturity: active
module: doctrine
topics:
  - thinking-systems
  - deterministic-core
  - model-judgment
  - uncertainty-boundary
  - control-loop
  - constraints
  - containment
tags:
  - ua/module/doctrine
  - ua/type/doctrine
  - ua/status/draft-normative
  - ua/topic/thinking-systems
  - ua/topic/deterministic-core
  - ua/topic/model-judgment
  - ua/topic/uncertainty-boundary
  - ua/topic/control-loop
  - ua/topic/constraints
canonical_for:
  - doctrine-module
---

# Core Doctrine

**Status:** Draft normative  
**Role:** Foundational vocabulary and architectural distinctions

## Purpose

This module defines the conceptual foundation used throughout Uncertainty Architecture (UA). It establishes how to reason about **Thinking Systems**: software systems whose runtime behavior depends partly on probabilistic Model Judgment while consequential boundaries, responsibilities, and corrective mechanisms remain explicit.

The doctrine provides the shared mental model needed to discuss uncertainty without treating model behavior as either ordinary deterministic code or uncontrollable magic.

## Defines

This module defines or develops the foundational distinctions behind:

- Thinking Systems;
- deterministic control logic and Model Judgment;
- the boundary between probabilistic behavior and deterministic system responsibilities;
- the controlled-object shift created when consequential runtime behavior is produced through Model Judgment;
- product, operational, and runtime-judgment uncertainty as related but distinct control problems;
- UA as a control lifecycle that complements product discovery, iterative delivery, DevOps, QA, security, and incident response;
- organizational context, project authorization, delivery-level review, and runtime reauthorization as connected control levels;
- decision ownership, constraint inheritance, realization, and upward reassessment across those levels;
- the Control-Loop Capability Anatomy of Constraints, Sensors, Controllers, and Actuators;
- the distinction between capability functions and physical implementation topology;
- functional placement of Model Judgment as Input Interpretation, Decision Logic, or Output Mediation;
- open-loop and closed-loop operating conditions;
- uncertainty containment rather than uncertainty elimination;
- the limits of policies, metrics, dashboards, or tools without complete capability and authority paths;
- the architectural importance of interfaces, invariants, constraints, feedback, and Human Authority;
- Requirements and Operating Envelopes in mixed deterministic and model-mediated systems;
- Correctness as satisfaction of the approved Requirement;
- Bugs as system-level Requirement violations;
- deterministic, model-mediated, and boundary-or-control sources of those violations;
- architectural veto as a valid engineering decision when a credible and viable control boundary cannot be established.

## Does not define

This module does not prescribe:

- a specific model, vendor, framework, or implementation stack;
- a mandatory three-stage Model Judgment pipeline or physical topology;
- four separate control-plane services;
- a complete runtime control-plane implementation;
- one universal constraint catalogue, policy engine, or schema technology;
- one universal set of controls, sample sizes, confidence levels, evaluation thresholds, risk scores, or control-cost formulas;
- detailed project or delivery review checklists;
- detailed Definition of Ready or Definition of Done checklists;
- a release protocol, evidence package, responsibility matrix, or mandatory Project Launch Gate;
- replacement of Agile, Scrum, DevOps, or an organization's existing SDLC;
- a mandatory organizational structure;
- a certification or conformance program.

Operational checklists, decision flows, practical records, and implementation examples are defined through reusable patterns, AI Control Plane capability areas, and reference material rather than embedded in doctrine.

## Key concepts

- **Thinking System** — a software system in which part of the runtime path or decision process is produced through model-mediated judgment while consequential deterministic responsibilities remain explicit.
- **Deterministic Core** — rules, invariants, permissions, data handling, and other responsibilities that must remain explicitly controlled.
- **Model Judgment** — interpretation, synthesis, classification, generation, planning, or action selection under uncertainty.
- **Controlled-object shift** — the change created when the engineered system itself produces consequential runtime uncertainty through Model Judgment rather than uncertainty existing only in requirements, users, environments, or delivery assumptions.
- **Nested Control Lifecycle** — the connected organizational, project, delivery, and runtime decision structure through which authoritative constraints and capabilities flow downward and invalidating evidence flows upward.
- **Control-Loop Capability Anatomy** — Constraints bound the operating space, Sensors produce evidence, Controllers interpret and authorize, and Actuators execute corrective change.
- **Constraint** — a condition intended to limit behavior or reduce the reachable operating space; it may be hard or soft and must remain connected to source, realization, failure behavior, evidence, and authority.
- **Model Judgment placement** — the functional role a Judgment Node performs as Input Interpretation, Decision Logic, Output Mediation, or a combination.
- **Uncertainty Boundary** — the interface at which deterministic responsibilities meet probabilistic judgment.
- **Containment** — limiting where uncertainty may propagate and defining what happens when behavior leaves acceptable bounds.
- **Requirement** — the approved operating contract for a system, feature, or change.
- **Operating Envelope** — the approved operating region within a Requirement; it is not the complete Requirement by itself.
- **Correctness** — the condition in which observed system behavior satisfies the approved Requirement.
- **Bug** — a violation of an approved Requirement caused or permitted by the implemented system.
- **Diagnostic sources** — Deterministic Defect, Model-Mediated Violation, and Boundary or Control Failure identify where a system-level Bug may originate.

The canonical wording for terms currently defined by UA is maintained in the [project glossary](glossary.md). Undefined or unresolved terms remain draft framework questions rather than implied requirements.

## Documents

- [`glossary.md`](glossary.md) — canonical draft-normative vocabulary for current UA terms.
- [`uncertainty-in-the-controlled-object.md`](uncertainty-in-the-controlled-object.md) — draft-normative rationale for UA, the changed controlled object, nested control levels, project authorization versus delivery release, runtime evidence, and architectural veto.
- [`control-loop-anatomy.md`](control-loop-anatomy.md) — draft-normative four-capability anatomy distinguishing Constraints, Sensors, Controllers, and Actuators from physical implementation topology.
- [`nested-control-lifecycle.md`](nested-control-lifecycle.md) — draft-normative operating model for decision ownership, constraint inheritance, runtime evidence, corrective action, and reauthorization across the four UA control levels.
- [`requirements-correctness-and-bugs.md`](requirements-correctness-and-bugs.md) — draft-normative relationship between Requirements, Operating Envelopes, Correctness, Bugs, evidence, and diagnosis in mixed deterministic and model-mediated systems.
- [`model-judgment-placement.md`](model-judgment-placement.md) — draft-normative functional taxonomy for locating Model Judgment as Input Interpretation, Decision Logic, or Output Mediation without prescribing a mandatory pipeline.

Process hypotheses, operational checklists, and historical terminology belong outside doctrine unless deliberately adopted as a foundational concept.

## Relationships

- [`01-patterns/project-control-architecture-and-viability-review.md`](../01-patterns/project-control-architecture-and-viability-review.md) operationalizes project-level risk scenarios, constraint architecture, control capability feasibility, evidence, Human Authority, operating capacity, economics, authorization, inheritance, and reauthorization.
- [`01-patterns/thinking-system-review.md`](../01-patterns/thinking-system-review.md) operationalizes delivery-level Judgment Nodes, Requirements, constraint realization, DoR, bounded experimentation, DoD, release, and local reassessment.
- [`01-patterns/judgment-node-boundary.md`](../01-patterns/judgment-node-boundary.md) makes consequential Model Judgment explicit, bounded, observable, and operable.
- [`02-ai-control-plane/`](../02-ai-control-plane/) develops Constraints, Sensors, Controllers, Actuators, and implementation-oriented control guidance.
- [`03-reference-architectures/`](../03-reference-architectures/) demonstrates possible compositions of the doctrine and patterns.
- [`04-failure-modes/`](../04-failure-modes/) records recurring mechanisms through which these distinctions are violated or lost.
- [`SPECIFICATION.md`](../SPECIFICATION.md) defines the status and normative boundary of this module.
