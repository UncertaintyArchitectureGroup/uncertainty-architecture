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

> **UA navigation**
>
> [UA Home](../README.md) · [Specification](../SPECIFICATION.md)
>
> **Lifecycle:** [Organization / boundaries](nested-control-lifecycle.md#1-organizational-control-context) · [Project / architecture](../01-patterns/project-control-architecture-and-viability-review.md) · [Delivery / release](../01-patterns/thinking-system-review.md) · [Runtime / reassessment](nested-control-lifecycle.md#4-runtime-operation-and-reassessment)
>
> **Explore:** [Doctrine](README.md) · [Patterns](../01-patterns/) · [Control capabilities](../02-ai-control-plane/) · [Reference architectures](../03-reference-architectures/) · [Failure modes](../04-failure-modes/) · [Research](../content/research/index.md)

**Status:** Draft normative  
**Role:** Foundational vocabulary and architectural distinctions

## Purpose

This module defines the conceptual foundation used throughout Uncertainty Architecture. It establishes how to reason about **Thinking Systems**: software systems whose runtime behavior depends partly on probabilistic Model Judgment while consequential deterministic responsibilities, Constraints, decision rights, evidence, and corrective mechanisms remain explicit.

The doctrine provides the shared mental model needed to discuss uncertainty without treating model behavior as ordinary deterministic code or uncontrollable magic.

## Defines

This module defines or develops:

- Thinking Systems;
- deterministic responsibilities and Model Judgment;
- the Uncertainty Boundary;
- the controlled-object shift created when consequential runtime behavior is produced through Model Judgment;
- product, operational, and runtime-judgment uncertainty as related but distinct problems;
- UA as a control lifecycle complementing product discovery, iterative delivery, DevOps, QA, security, and incident response;
- organizational, project, delivery, and runtime decision levels;
- decision ownership, Constraint inheritance, realization, and upward reassessment;
- the Control-Loop Capability Anatomy of Constraints and their realizations, Sensors, Controllers, and Actuators;
- the distinction between a closed feedback loop and a complete bounded UA control architecture;
- the distinction between capability functions and physical topology;
- functional placement of Model Judgment;
- uncertainty containment rather than elimination;
- the limits of policies, metrics, dashboards, or tools without complete evidence, authority, and action paths;
- Requirements, Operating Envelopes, Correctness, and Bugs;
- Architectural Veto when a credible and viable control boundary cannot be established.

## Does not define

This module does not prescribe:

- a specific model, vendor, framework, or implementation stack;
- a mandatory Model Judgment pipeline or physical topology;
- four separate control-plane services;
- a complete runtime control-plane implementation;
- one universal Constraint catalogue, policy engine, schema technology, threshold, sample size, risk score, or control-cost formula;
- detailed project or delivery checklists;
- a mandatory release protocol, responsibility matrix, governance board, organizational structure, certification, or conformance program;
- replacement of Agile, Scrum, DevOps, or an organization's existing SDLC.

Operational checklists, decision flows, practical records, and implementation examples belong in patterns, AI Control Plane capability areas, and reference material.

## Key concepts

- **Thinking System** — a software system whose runtime behavior depends partly on probabilistic Model Judgment while consequential deterministic responsibilities, Constraints, decision rights, evidence, and corrective mechanisms remain explicit.
- **Deterministic Core** — rules, Invariants, permissions, data handling, and other responsibilities that must remain explicitly controlled.
- **Model Judgment** — interpretation, synthesis, classification, generation, planning, or action selection under uncertainty.
- **Controlled-object shift** — the change created when the engineered system itself produces consequential runtime uncertainty.
- **Nested Control Lifecycle** — the organizational, project, delivery, and runtime decision structure through which authoritative Constraints and capabilities flow downward and invalidating evidence flows upward.
- **Control-Loop Capability Anatomy** — four capability families: Constraints and their realizations, Sensors and evidence, Controllers and decision authority, and Actuators and corrective action.
- **Constraint** — an approved condition limiting the allowed operating space.
- **Constraint Realization** — the concrete mechanism implementing, enforcing, or influencing a Constraint for a defined scope.
- **Hard Constraint** — a scoped Constraint whose complete realized path deterministically prevents or rejects violation within stated assumptions, subject, path, scope, and enforcement boundaries.
- **Uncertainty Boundary** — the interface at which deterministic responsibilities meet probabilistic judgment.
- **Containment** — limiting where uncertainty or failure may propagate.
- **Requirement** — the approved operating contract for a system, feature, or change.
- **Operating Envelope** — the approved operating region within a Requirement.
- **Correctness** — satisfaction of the approved Requirement.
- **Bug** — a system-level violation of an approved Requirement.

Canonical wording belongs to the [`glossary`](glossary.md). Undefined or unresolved terms remain framework questions rather than implied requirements.

## Documents

- [`glossary.md`](glossary.md) — canonical vocabulary.
- [`uncertainty-in-the-controlled-object.md`](uncertainty-in-the-controlled-object.md) — controlled-object rationale and lifecycle need.
- [`control-loop-anatomy.md`](control-loop-anatomy.md) — four capability families, feedback closure, bounded operation, and capability relationships.
- [`nested-control-lifecycle.md`](nested-control-lifecycle.md) — decision ownership, inheritance, runtime evidence, and reauthorization.
- [`requirements-correctness-and-bugs.md`](requirements-correctness-and-bugs.md) — Requirements, Operating Envelopes, Correctness, Bugs, and diagnosis.
- [`model-judgment-placement.md`](model-judgment-placement.md) — Input Interpretation, Decision Logic, and Output Mediation.

## Relationships

- [`01-patterns/project-control-architecture-and-viability-review.md`](../01-patterns/project-control-architecture-and-viability-review.md) operationalizes project risk, Constraint architecture, capability feasibility, economics, authorization, and reauthorization.
- [`01-patterns/thinking-system-review.md`](../01-patterns/thinking-system-review.md) operationalizes delivery realization, DoR, DoD, Release Gate, and reassessment.
- [`01-patterns/judgment-node-boundary.md`](../01-patterns/judgment-node-boundary.md) makes consequential Model Judgment explicit and bounded.
- [`02-ai-control-plane/`](../02-ai-control-plane/) develops Constraints and their realizations, Sensors, Controllers, Actuators, and implementation-oriented guidance.
- [`03-reference-architectures/`](../03-reference-architectures/) demonstrates possible compositions.
- [`04-failure-modes/`](../04-failure-modes/) records recurring loss-of-control mechanisms.
- [`SPECIFICATION.md`](../SPECIFICATION.md) defines status and normative boundaries.
