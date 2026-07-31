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

This document defines the normative boundary and document structure of Uncertainty Architecture (UA).

UA is an open specification for designing and governing **Thinking Systems**: software systems whose runtime behavior depends partly on probabilistic Model Judgment while consequential deterministic responsibilities, Constraints, evidence, decision rights, and corrective mechanisms remain explicit. Earlier UA publications used **Behavioral Software** and **Behavioral Applications** for this category.

UA treats reliability and governance as system properties produced by an approved Requirement, explicit Constraints, observable behavior, feedback, decision rights, viable control architecture, and controlled change rather than by model quality alone.

The specification addresses a controlled-object shift: uncertainty does not exist only in requirements, users, infrastructure, or delivery assumptions. A Thinking System may itself produce consequential runtime uncertainty through Model Judgment. UA connects organizational context, project authorization, delivery-level constraint realization and review, runtime enforcement and evidence, corrective action, and reauthorization around that changed object.

This file is the canonical entry point for the specification. It does not duplicate the detailed content of the modules it indexes.

## 2. Scope

The UA specification covers:

- the distinction between deterministic control logic and probabilistic Model Judgment;
- the controlled-object shift created when consequential runtime behavior is produced through Model Judgment;
- the relationship between product uncertainty, operational uncertainty, and runtime-judgment uncertainty;
- organizational control context, project control architecture and viability, delivery-level review, runtime control, and reauthorization as connected decision levels;
- the Control-Loop Capability Anatomy of Constraints, Sensors and evidence, Controllers and decision authority, and Actuators and corrective action;
- Constraint source, subject, scope, hard or soft strength, realization, enforcement point, failure behavior, evidence, change authority, and reassessment;
- project-level material risk scenarios, intended Judgment and authority, organizational and project Constraints, required capabilities, evidence feasibility, Human Authority, operating capacity, control economics, authorization, inheritance, and reauthorization;
- delivery-level realization and verification of inherited and local Constraints;
- functional placement of Model Judgment within a system or workflow;
- architectural boundaries around model-mediated behavior;
- reusable technical and socio-technical patterns;
- lightweight review patterns and practical artifacts connecting project decisions, Requirements, Judgment Nodes, Constraints, evidence, decision authority, release, and reassessment;
- project-level architectural veto when a credible, operable, or economically viable control boundary cannot be established;
- recurring model, Constraint, Sensor, Controller, Actuator, boundary, capacity, and governance failure modes;
- reference architectures that demonstrate possible compositions of the specification.

The specification does not prescribe:

- a particular model, vendor, framework, policy engine, orchestration platform, or deployment topology;
- four separate control-plane services or one tool per capability;
- a mandatory pipeline of Input Interpretation, Decision Logic, and Output Mediation;
- one universal Constraint catalogue, schema technology, or fail-open/fail-closed rule;
- replacement of Agile, Scrum, DevOps, QA, security, change management, or an organization's existing SDLC;
- one mandatory project lifecycle or Project Launch Gate protocol;
- a mandatory governance department, committee, or organizational structure;
- a separate Constraint Register, Judgment Node registry, or decision record for every readiness, completion, release, or project authorization decision;
- universal numerical thresholds for quality, risk, latency, cost, sample size, confidence, autonomy, or Constraint effectiveness;
- one universal risk score or control-cost formula;
- mandatory job titles or a single organizational structure;
- identical controls for every AI system;
- duplication of project risk, constraint architecture, economics, or organizational sources inside every delivery review;
- any reference implementation as the standard itself.

Constraints, controls, evidence, review depth, and records should be proportional to consequences, uncertainty, autonomy, authority, reversibility, exposure, feedback latency, enforcement difficulty, organizational capacity, and operating context.

## 3. Normative language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL**, when written in uppercase, indicate the strength of a requirement.

Examples, explanations, templates, technology catalogs, and rationale are informative unless explicitly stated otherwise.

## 4. Document status model

Every specification document SHOULD declare one of the following statuses:

- **Normative** — accepted specification content defining requirements, concepts, interfaces, responsibilities, or conformance expectations.
- **Draft normative** — proposed specification content under active development. It may change and MUST NOT be represented as stable.
- **Informative** — explanation, rationale, guidance, template, or example that supports the specification without creating requirements.
- **Reference** — a concrete architecture or implementation demonstrating one possible application of UA. It is not the standard itself.
- **Research** — source material, analysis, or synthesis that may inform future specification changes but is not automatically normative.
- **Historical** — superseded or archival material retained for traceability.

A directory name does not by itself determine status. The explicit status in the document or its module index takes precedence.

The metadata field `maturity` may describe lifecycle state within a status class, such as `draft`, `active`, `stable`, or `superseded`. It does not replace document status. See [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md).

## 5. Specification structure

### 5.1 Core doctrine

[`00-doctrine/`](00-doctrine/README.md) defines the foundational concepts and distinctions on which the rest of UA depends.

- [`uncertainty-in-the-controlled-object.md`](00-doctrine/uncertainty-in-the-controlled-object.md) owns the rationale for UA and the changed controlled object.
- [`control-loop-anatomy.md`](00-doctrine/control-loop-anatomy.md) owns the relationship among Constraints, Sensors, Controllers, and Actuators as logical capability classes rather than physical services.
- [`nested-control-lifecycle.md`](00-doctrine/nested-control-lifecycle.md) owns decision levels, constraint inheritance, delivery realization, runtime evidence, and reauthorization.
- [`requirements-correctness-and-bugs.md`](00-doctrine/requirements-correctness-and-bugs.md) owns the mixed-system Requirement and diagnostic model.
- [`model-judgment-placement.md`](00-doctrine/model-judgment-placement.md) owns the functional placement taxonomy for Model Judgment.
- [`glossary.md`](00-doctrine/glossary.md) is the canonical vocabulary source for terms it currently defines.

Stable doctrine is expected to become normative; unfinished doctrine remains draft normative.

### 5.2 Patterns

[`01-patterns/`](01-patterns/README.md) contains reusable solutions for recurring technical and socio-technical control problems.

A pattern may arrange Constraints, technical mechanisms, artifacts, responsibility bundles, evidence, economics, and decision processes when those elements jointly address a recurring control problem. This does not create a separate top-level Operating Model module by implication.

The [`Project Control Architecture and Viability Review`](01-patterns/project-control-architecture-and-viability-review.md) is the canonical owner of the project-level material risk model, organizational Constraint interpretation, project-specific constraint architecture, intended Judgment and authority landscape, required capabilities, evidence feasibility, Human Authority and operating capacity, control economics, project authorization, delivery inheritance package, and project reauthorization triggers.

The [`Project Control Architecture and Viability Review Template`](01-patterns/project-control-architecture-and-viability-review-template.md) is its informative working representation. It keeps the project decision and constraint baseline in one living artifact and does not create separate Project Launch Gate or Constraint Register protocols.

The [`Judgment Node Boundary`](01-patterns/judgment-node-boundary.md) is the canonical reusable boundary for making consequential Model Judgment explicitly constrained, observable, and operable.

The [`Thinking System Review`](01-patterns/thinking-system-review.md) is the canonical owner of delivery-level Judgment Nodes, Requirement, concrete constraint realization, model-mediated Definition of Ready, Definition of Done, distinct Release Gate, responsibility bundles, and local reassessment.

The [`Thinking System Review Template`](01-patterns/thinking-system-review-template.md) is its informative working representation. It links the project decision and inherited Constraint baseline, records local realization, and does not create an additional conformance path.

The project review and delivery review are connected but do not share canonical ownership. Project-level authorization and Constraints flow downward by reference. Delivery and runtime evidence flows upward when it invalidates project risk, Constraint feasibility, authority, capacity, evidence, or economic assumptions.

### 5.3 AI Control Plane

[`02-ai-control-plane/`](02-ai-control-plane/README.md) defines the distributed capability model required to bound, observe, decide, and correct model-mediated behavior.

The four capability areas are:

- [`00-actuators/`](02-ai-control-plane/00-actuators/) — mechanisms that execute authorized changes;
- [`01-constraints/`](02-ai-control-plane/01-constraints/) — conditions and enforcement mechanisms that bound the reachable operating space;
- [`02-sensors/`](02-ai-control-plane/02-sensors/) — evidence about behavior, outcomes, Constraints, drift, and control health;
- [`03-controller/`](02-ai-control-plane/03-controller/) — interpretation, decision authority, Constraint-change authority, and corrective decisions.

The control plane is an architectural capability model, not necessarily a standalone product or infrastructure layer. Implementations MAY distribute or combine its functions across application code, platform services, evaluation systems, human workflows, release processes, and governance mechanisms.

The informative [`Constraint Realization Catalog`](02-ai-control-plane/01-constraints/constraint-realization-catalog.md) names possible mechanisms. Named products and libraries do not become specification requirements.

### 5.4 Reference architectures

[`03-reference-architectures/`](03-reference-architectures/README.md) contains concrete compositions showing how UA concepts and patterns may be applied.

Reference architectures SHOULD identify Constraints, Sensors, Controllers, Actuators, Human Authority, failure behavior, and decision levels by function rather than assuming one physical layer per capability.

[`judgment-placement-examples.md`](03-reference-architectures/judgment-placement-examples.md) shows Input Interpretation only, Decision Logic only, Output Mediation only, and one composite Thinking System.

[`worked-thinking-system-review-support-triage.md`](03-reference-architectures/worked-thinking-system-review-support-triage.md) applies the delivery review to one illustrative support scenario. Its synthesized evidence and thresholds are not production validation or UA defaults.

Reference architectures MUST NOT be treated as mandatory implementation topologies unless a separate normative document explicitly adopts a requirement they illustrate. Copying a reference architecture does not establish conformance.

### 5.5 Failure modes

[`04-failure-modes/`](04-failure-modes/README.md) records recurring mechanisms by which Thinking Systems lose structural, semantic, constraint, operational, economic, or organizational control.

The taxonomy distinguishes missing, soft-as-hard, unenforced, bypassed, stale, conflicting, unauthorized, unavailable, slow, or economically destructive Constraints; Sensor and evidence failure; Controller and authority failure; Actuator and corrective-path failure; open-loop connections; and socio-technical anti-patterns.

A taxonomy may be normative; individual examples and post-mortems are normally informative.

## 6. Supporting material outside the specification

The project uses one canonical namespace for each supporting-material type:

- [`content/research/`](content/research/index.md) — research publications, notes, analyses, synthesis, and research-to-framework traceability;
- [`content/history/`](content/history/README.md) — project history, public evidence, and superseded records;
- [`content/raw/`](content/raw/README.md) — preserved source snapshots;
- [`content/index.md`](content/index.md) — an informative publishing portal;
- [`ROADMAP.md`](ROADMAP.md) — planned evolution;
- [`CHANGELOG.md`](CHANGELOG.md) — repository-level record of material changes;
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution workflow and review expectations;
- [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) — informative metadata and tag conventions;
- [`AGENTS.md`](AGENTS.md) — informative repository orientation and editing guidance for AI contributors.

The `quartz/` source tree and related Node configuration are publishing infrastructure. They do not define UA concepts, requirements, governance, or conformance.

Content enters the normative specification only through an explicit framework decision and corresponding status change. Research findings, talks, articles, implementations, metadata, tags, recency, external attention, or agent-generated summaries do not modify normative authority by implication.

## 7. Conformance

UA conformance is currently defined at the level of explicit architectural and operational reasoning rather than product certification or use of one required template.

A system or design claiming alignment with UA SHOULD be able to identify:

1. where materially consequential Model Judgment occurs;
2. the functional placement of each Judgment Node;
3. which inputs and approved context each node receives;
4. which outputs, decisions, paths, actions, states, resources, or parties each node can affect;
5. which authority each node possesses;
6. the applicable organizational, project, and delivery Constraints;
7. the source, subject, scope, hard or soft strength, realization, failure behavior, evidence, and change authority for each material Constraint;
8. which deterministic responsibilities and Invariants remain outside Model Judgment;
9. how behavior, outcomes, Constraint state, violations, and control health are observed;
10. who or what acts as Controller and which decisions it owns;
11. which Actuators and corrective actions are available;
12. how fallback, containment, compensation, escalation, rollback, or shutdown occurs;
13. how decisions, Constraints, versions, assumptions, dependencies, and changes remain traceable;
14. which evidence triggers local reassessment, project reauthorization, or organizational review.

A system MUST NOT claim a hard Constraint when it relies only on probabilistic instruction without an explicit and justified enforcement boundary.

### 7.1 Project-level alignment

For a consequential proposed Thinking System project, the organization or team SHOULD be able to show an equivalent of:

- the intended business outcome, non-AI alternative, and reason Model Judgment is needed;
- a defined project boundary and intended Judgment, autonomy, and authority landscape;
- material risk scenarios connected to consequence, detectability, feedback latency, reversibility, propagation, required Constraints and capabilities, and residual risk;
- applicable organizational Constraint sources and decision rights;
- project-specific Constraints with source or rationale, scope, strength, required realization, failure behavior, evidence, and change authority;
- deterministic Invariants and prohibited authority;
- required shared and project-specific Sensors, Controllers, Actuators, Human Authority, fallback, containment, rollback, compensation, and shutdown capabilities;
- evidence feasibility and material blind spots;
- substantive Human Authority and sufficient operational capacity;
- one-time and recurring Constraint and control costs, remaining exposure, and effect on the business case;
- a project authorization outcome distinct from delivery release;
- a versioned authorization and Constraint inheritance package;
- project reauthorization triggers after material change or runtime evidence.

The project outcome MAY authorize delivery, authorize with conditions, authorize only bounded research, require redesign, escalate, defer, or reject the AI path.

### 7.2 Delivery-level alignment

For consequential model-mediated delivery work, the system or team SHOULD also be able to show an equivalent of:

- a link to the applicable project decision and inherited Constraint baseline, or an explicit reason no project baseline exists;
- an approved Requirement and context-derived Operating Envelope;
- explicit Judgment Node boundaries;
- concrete realization and versioning of inherited and local Constraints;
- hard and soft claims kept distinct;
- tested failure, bypass, conflict, unavailable, degraded, and override behavior where material;
- evidence of Constraint activation, violations, false blocks, control health, and operational friction;
- a readiness decision distinguishing implementation from bounded experimentation;
- completion evidence covering deterministic, Constraint, behavioral, authority, resource, operational, and failure-handling responsibilities;
- a release decision distinct from completion, with deployment scope, active Constraints, residual risk, conditions, and decision authority;
- runtime ownership, Controller authority, available Actuators, and reassessment triggers;
- evidence that delivery does not silently expand project authority or weaken inherited hard Constraints.

UA does not require the provided project or delivery templates. Equivalent records and processes MAY be integrated into existing product, business-case, architecture, engineering, security, quality, financial, change-management, risk, policy, or incident systems, provided relevant distinctions, source authority, capability functions, inheritance, and reauthorization paths remain explicit and traceable.

The placement classes are a functional taxonomy, not a mandatory pipeline. The four control capabilities are logical functions, not a mandatory physical stack. Reference architectures may help a team reason about these distinctions but do not add conformance requirements.

A claim of UA alignment MUST NOT imply certification, endorsement, or complete conformance unless the project later establishes a formal conformance program.

## 8. Change control

Normative and draft-normative changes SHOULD be:

- scoped to one coherent architectural decision;
- reviewable through a visible change set;
- linked to relevant research, operational evidence, or design rationale;
- explicit about compatibility, path migration, supersession, and unresolved uncertainty;
- checked across all four decision levels and four control capabilities;
- reflected in the glossary, module indexes, research traceability, roadmap, and changelog when material.

Research findings, talks, articles, implementations, and external frameworks do not modify the specification by implication. Adoption requires an explicit normative decision following the current contribution and review workflow.

## 9. Current maturity

UA is in active development. The repository contains:

- a conceptual spine for Thinking Systems and the controlled-object shift;
- a canonical draft glossary;
- doctrine for the four-capability Control-Loop Anatomy and four-level Nested Control Lifecycle;
- a project-level Control Architecture and Viability Review pattern and template with embedded constraint architecture;
- a Model Judgment placement taxonomy and constrained Judgment Node Boundary;
- an SMB-facing delivery-level Thinking System Review pattern and template with project inheritance and concrete constraint realization;
- a reorganized AI Control Plane with dedicated Actuator, Constraint, Sensor, and Controller capability areas;
- an informative Constraint Realization Catalog;
- placement-focused reference architectures and one completed illustrative delivery review;
- research traceability and an expanded failure-mode taxonomy.

A two-level worked application tracing Constraints from organizational source through project derivation, delivery realization, runtime enforcement and evidence, and reauthorization remains incomplete. Real-team application, deeper risk and tolerance derivation, detailed control-economics methods, additional reference domains, and incident-loop evidence also remain incomplete.

Readers SHOULD follow the explicit status declared by each module or document. Reference architectures, technology catalogs, and clearly identified examples or templates remain **reference** or **informative**, not mandatory implementation requirements.
