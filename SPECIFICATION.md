---
title: Uncertainty Architecture Specification
artifact_type: specification-index
status: draft-normative
maturity: active
module: repository
topics:
  - thinking-systems
  - uncertainty-boundary
  - control-loop
  - constraints
  - conformance
tags:
  - ua/module/repository
  - ua/type/specification-index
  - ua/status/draft-normative
  - ua/topic/thinking-systems
  - ua/topic/uncertainty-boundary
  - ua/topic/control-loop
  - ua/topic/constraints
  - ua/topic/conformance
canonical_for:
  - specification-boundary
  - document-status-model
  - conformance-model
---

# Uncertainty Architecture Specification

**Status:** Draft specification index  
**Version:** 0.x  
**License:** CC BY 4.0

## 1. Purpose

This document defines the normative boundary and document structure of Uncertainty Architecture.

UA is an open specification for designing and governing **Thinking Systems**: software whose runtime behavior depends partly on probabilistic Model Judgment while consequential deterministic responsibilities, approved Constraints, evidence, decision rights, and corrective mechanisms remain explicit.

UA treats reliability and governance as system properties produced by Requirements, approved Constraints and their realizations, observable behavior, decision authority, effective Actuators, viable control economics, and controlled change rather than by model quality alone.

This file indexes the specification. It does not duplicate the detailed content of the modules it references.

## 2. Scope

The specification covers:

- the controlled-object shift created by consequential runtime Model Judgment;
- deterministic responsibilities, Model Judgment, and Uncertainty Boundaries;
- organizational, project, delivery, and runtime decision levels;
- Constraints and their realizations, Sensors, Controllers, and Actuators as four logical capability families;
- the distinction between a closed feedback loop and complete bounded UA control architecture;
- the distinction between Constraint and Constraint Realization;
- scoped Hard and Soft Constraint claims;
- project-level scenarios, Constraint architecture, capability feasibility, evidence, capacity, economics, authorization, inheritance, and reauthorization;
- delivery-level Judgment Nodes, Requirement, Operating Envelope, one canonical Constraint Realization Map, DoR, DoD, Release Gate, and reassessment;
- Human Authority, fallback, containment, compensation, rollback, escalation, and shutdown;
- reusable patterns, failure modes, and non-prescriptive reference architectures;
- Architectural Veto when credible and viable control cannot be established.

The specification does not prescribe:

- one model, vendor, framework, policy engine, evaluator, orchestration platform, or topology;
- four separate control-plane services or one tool per capability family;
- a mandatory Model Judgment pipeline;
- one universal Constraint catalogue, schema technology, fail-open/fail-closed rule, threshold, sample size, risk score, or control-cost formula;
- replacement of Agile, Scrum, DevOps, QA, security, change management, or an organization's SDLC;
- a mandatory governance department, committee, or organizational structure;
- separate Constraint Registers, Judgment Node registries, or decision records when the two living reviews and linked evidence are sufficient;
- mandatory job titles;
- any reference implementation as the standard itself.

Review depth and controls should be proportional to consequences, uncertainty, autonomy, authority, reversibility, exposure, feedback latency, realization difficulty, organizational capacity, and operating context.

## 3. Normative language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL**, when uppercase, indicate requirement strength.

Examples, explanations, templates, technology catalogues, and rationale are informative unless explicitly stated otherwise.

## 4. Document status model

Specification documents SHOULD declare one of these statuses:

- **Normative** — accepted specification content.
- **Draft normative** — proposed specification content under active review; it MUST NOT be represented as stable.
- **Informative** — explanation, guidance, template, or example without independent requirements.
- **Reference** — one concrete, non-mandatory application.
- **Research** — source material, analysis, or synthesis that may inform later decisions.
- **Historical** — archival or superseded material retained for traceability.

Explicit status takes precedence over directory name. `maturity` describes lifecycle within a status class and does not replace status.

## 5. Specification structure

### 5.1 Core doctrine

[`00-doctrine/`](00-doctrine/README.md) owns foundational meaning.

- [`uncertainty-in-the-controlled-object.md`](00-doctrine/uncertainty-in-the-controlled-object.md) — controlled-object rationale.
- [`control-loop-anatomy.md`](00-doctrine/control-loop-anatomy.md) — feedback closure, bounded operation, Constraints, Constraint Realizations, Sensors, Controllers, and Actuators.
- [`nested-control-lifecycle.md`](00-doctrine/nested-control-lifecycle.md) — decision ownership, inheritance, runtime evidence, and reassessment.
- [`requirements-correctness-and-bugs.md`](00-doctrine/requirements-correctness-and-bugs.md) — Requirement and diagnosis model.
- [`model-judgment-placement.md`](00-doctrine/model-judgment-placement.md) — functional placement of Model Judgment.
- [`glossary.md`](00-doctrine/glossary.md) — canonical vocabulary where entries exist.

### 5.2 Patterns

[`01-patterns/`](01-patterns/README.md) owns reusable socio-technical responses.

The [`Project Control Architecture and Viability Review`](01-patterns/project-control-architecture-and-viability-review.md) owns project-level scenarios, one canonical Project Constraint Architecture, capability feasibility, evidence, Human Authority, capacity, economics, authorization, inheritance, and reauthorization.

Its [`template`](01-patterns/project-control-architecture-and-viability-review-template.md) is informative.

The [`Judgment Node Boundary`](01-patterns/judgment-node-boundary.md) owns the reusable boundary around consequential Model Judgment.

The [`Thinking System Review`](01-patterns/thinking-system-review.md) owns delivery-level Judgment Nodes, Requirement, one canonical Constraint Realization Map, DoR, DoD, Release Gate, and local reassessment.

Its [`template`](01-patterns/thinking-system-review-template.md) is informative.

Project authorization and delivery release remain separate. Higher-level decisions flow downward by reference; invalidating evidence flows upward.

### 5.3 AI Control Plane

[`02-ai-control-plane/`](02-ai-control-plane/README.md) develops four logical capability families:

- [`00-actuators/`](02-ai-control-plane/00-actuators/) — execution of authorized change;
- [`01-constraints/`](02-ai-control-plane/01-constraints/) — approved Constraints and their realizations;
- [`02-sensors/`](02-ai-control-plane/02-sensors/) — evidence about behavior, outcomes, realization state, Actuator execution, and control health;
- [`03-controller/`](02-ai-control-plane/03-controller/) — comparison, interpretation, decision authority, and authorization of action.

The Constraints family is intentionally composite: the Constraint is the authoritative boundary object, while the Constraint Realization provides the operational mechanism.

The directory numbers are navigation only and do not prescribe a stack or execution order.

The informative [`Constraint Realization Catalog`](02-ai-control-plane/01-constraints/constraint-realization-catalog.md) names possible implementation mechanisms. Named products and libraries do not become requirements.

### 5.4 Reference architectures

[`03-reference-architectures/`](03-reference-architectures/README.md) shows non-prescriptive compositions.

References SHOULD identify approved Constraints, realizations, Sensors, Controllers, Actuators, Human Authority, failure behavior, and decision levels by function.

Reference architectures MUST NOT be treated as mandatory topology or proof of conformance.

### 5.5 Failure modes

[`04-failure-modes/`](04-failure-modes/README.md) records reusable mechanisms by which control is lost or becomes ineffective, including:

- missing or invalid Constraints;
- Constraint–realization collapse;
- Soft Constraint represented as hard;
- missing, bypassed, stale, conflicting, unavailable, or ineffective realizations;
- Sensor and evidence failure;
- Controller and authority failure;
- Actuator and corrective-path failure;
- open-loop operation;
- closed-loop but unbounded operation;
- capacity and economic non-viability.

## 6. Supporting material outside the specification

- [`content/research/`](content/research/index.md) — research, analysis, synthesis, and traceability.
- [`content/history/`](content/history/README.md) — chronology and preserved public context.
- [`content/raw/`](content/raw/README.md) — source snapshots.
- [`ROADMAP.md`](ROADMAP.md) — development direction.
- [`CHANGELOG.md`](CHANGELOG.md) — notable repository changes.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution workflow.
- [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) — metadata conventions.
- [`AGENTS.md`](AGENTS.md) — informative operational protocol for AI-assisted contributors.

Research, talks, implementations, tags, recency, or summaries do not modify normative authority by implication.

## 7. Conformance

UA conformance is currently architectural and operational reasoning, not product certification.

A system or design claiming UA alignment SHOULD be able to identify:

1. where consequential Model Judgment occurs;
2. the placement and authority of each material Judgment Node;
3. applicable organizational, project, and delivery Constraints;
4. the source, subject, scope, claimed strength, and assumptions of each material Constraint;
5. the concrete Constraint Realization, active version, and enforcement or influence point;
6. failure, bypass, conflict, degraded, and unavailable behavior;
7. which deterministic responsibilities and Invariants remain outside Model Judgment;
8. how behavior, outcomes, realization state, Actuator execution, and control health are observed;
9. which Controller receives the reference conditions and evidence and which decisions it owns;
10. which Actuators execute authorized changes;
11. how fallback, containment, compensation, escalation, rollback, or shutdown occurs;
12. how project and delivery decisions, versions, assumptions, dependencies, and changes remain traceable;
13. which evidence triggers delivery reassessment, project reauthorization, or organizational review.

A system MUST NOT claim a Hard Constraint when its complete realized path does not deterministically prevent or reject violation within explicitly stated assumptions, scope, and enforcement boundaries.

A probabilistic detector, evaluator, prompt, model policy, or natural-language instruction is not a Hard Constraint by itself.

One source condition MUST NOT be represented as one mixed hard/soft Constraint record when different subjects, paths, or scopes have different guarantee strength. The claims SHOULD be separated so each is reviewable and traceable.

### 7.1 Project-level alignment

For a consequential proposed project, a team SHOULD be able to show an equivalent of:

- intended outcome, AI necessity, and non-AI alternatives;
- defined project boundary and intended Judgment authority;
- material scenarios connected to consequence, detectability, latency, reversibility, propagation, Constraint IDs, capability requirements, and residual decision effect;
- one canonical Project Constraint Architecture;
- required Constraint Realizations, Sensors, Controllers, Actuators, Human Authority, fallback, containment, compensation, rollback, and shutdown;
- evidence feasibility and blind spots;
- substantive Human Authority and sufficient capacity;
- control economics and viability;
- a project authorization outcome distinct from delivery release;
- a versioned inheritance package;
- reauthorization triggers.

Possible outcomes MAY include authorization, authorization with conditions, bounded research, redesign, escalation, deferral, or No-Go.

### 7.2 Delivery-level alignment

For consequential delivery work, a team SHOULD be able to show an equivalent of:

- a linked project decision and inherited Constraint baseline, or an explicit reason no project baseline exists;
- an approved Requirement and Operating Envelope;
- explicit Judgment Node boundaries;
- one canonical Constraint Realization Map;
- accurate and separately scoped Hard and Soft Constraint claims;
- tested failure, bypass, conflict, degraded, unavailable, and override behavior where material;
- evidence of activation, violations, false blocks, Actuator execution, and control health;
- a DoR decision distinguishing implementation from bounded experimentation;
- a DoD decision covering implementation and evidence completeness;
- a Release Gate distinct from DoD, with deployment scope, active realization versions, residual risk, conditions, and decision authority;
- runtime ownership, Controller authority, available Actuators, and reassessment triggers;
- evidence that delivery does not expand project authority or weaken an inherited Hard Constraint.

The provided templates are not mandatory. Equivalent records MAY be integrated into existing systems if the distinctions, authority, inheritance, and reassessment paths remain explicit and traceable.

The placement classes are not a mandatory pipeline. The four capability families are not mandatory physical services. Reference architectures do not add conformance requirements.

A claim of UA alignment MUST NOT imply certification, endorsement, or complete conformance unless a formal program is later established.

## 8. Change control

Normative and draft-normative changes SHOULD be:

- scoped to one coherent architectural decision;
- reviewable through a visible change set;
- linked to relevant research, evidence, or rationale;
- explicit about compatibility, path migration, supersession, and uncertainty;
- checked against glossary, doctrine, project and delivery patterns, AI Control Plane, references, failure modes, navigation, roadmap, changelog, and research traceability.

Source material becomes specification only through explicit framework review and a corresponding status-bearing change.
