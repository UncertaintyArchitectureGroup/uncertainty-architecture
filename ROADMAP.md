---
title: Uncertainty Architecture Roadmap
artifact_type: roadmap
status: informative
maturity: active
module: repository
topics:
  - repository-architecture
  - navigation
  - constraints
tags:
  - ua/module/repository
  - ua/type/roadmap
  - ua/status/informative
  - ua/topic/repository-architecture
  - ua/topic/navigation
  - ua/topic/constraints
canonical_for:
  - project-roadmap
---

# Uncertainty Architecture Roadmap

Uncertainty Architecture is being developed as a practical open specification for engineering and operating software that delegates part of its behavior to probabilistic Model Judgment.

This roadmap is the canonical detailed view of project direction. It distinguishes completed work, active work, near-term priorities, and later possibilities without attaching speculative dates.

## Status legend

- **Completed** — present in the repository and accepted as the current project baseline
- **Active** — currently being developed, applied, or consolidated
- **Next** — intended after the active work reaches a stable checkpoint
- **Later** — valuable, but not required for the current framework spine

## Phase 1 — Concept Validation

**Status: Completed**

Established the initial thesis and public evidence that AI-enabled systems require explicit engineering at the boundary between deterministic software and probabilistic Model Judgment.

Completed outcomes:

- initial Uncertainty Architecture publications;
- control-theory framing for AI governance;
- Deterministic Core and Model Judgment distinction;
- initial AI Control Plane concept;
- public and expert feedback;
- initial repository structure and licensing model.

## Phase 2 — Framework Spine

**Status: Active**

The objective is to consolidate existing research into a coherent, bounded specification that explains what UA governs, how its parts relate, and what remains non-normative.

### Completed in this phase

- Research Track established under `content/research/`;
- historical raw source snapshots preserved under `content/raw/`;
- five historical publications normalized and archived;
- provenance, source-intake, research-review, and research-to-framework traceability established;
- canonical specification boundary and document-status model established in `SPECIFICATION.md`;
- root README redesigned as the public landing page;
- primary module entry points normalized;
- **Thinking Systems** adopted as the current system-category term, with earlier terminology retained historically;
- supporting namespaces consolidated under `content/research/`, `content/history/`, and `content/raw/`;
- retired RFC governance material archived rather than left as an active process;
- repository consistency pass completed across canonical routes and status boundaries;
- canonical draft glossary established;
- controlled document metadata and hierarchical `ua/...` tags established;
- tool-neutral repository guidance established in `AGENTS.md`;
- Requirements, Operating Envelopes, Correctness, Bugs, and diagnostic sources established as mixed-system doctrine;
- Model Judgment Placement established as Input Interpretation, Decision Logic, and Output Mediation without a mandatory pipeline;
- Judgment Node Boundary established as a reusable pattern;
- Project Control Architecture and Viability Review established as the canonical project-level decision surface;
- Thinking System Review established as the canonical delivery-level review surface;
- one informative project review template and one informative delivery review template established as the two default living SMB artifacts;
- project baseline inheritance and upward reassessment established;
- organizational context, project authorization, delivery review, and runtime reauthorization established as four connected decision levels;
- architectural veto and `No-Go` recognized as valid engineering outcomes;
- placement-focused reference architectures and one completed illustrative delivery review added;
- slides 1–6 of *Designing Non-Deterministic Systems* translated through explicit framework review;
- source-derived framework changes connected to research-state reconciliation rather than a parallel worklog.

### Four-capability consolidation

The following framework decision is active in this phase:

- Constraints are a first-class AI Control Plane capability rather than an unresolved subtype or example of Actuators;
- [`Control-Loop Capability Anatomy`](00-doctrine/control-loop-anatomy.md) distinguishes Constraints, Sensors, Controllers, and Actuators as logical functions rather than mandatory physical services;
- [`Nested Control Lifecycle`](00-doctrine/nested-control-lifecycle.md) now explains authoritative Constraint inheritance, project derivation, delivery realization, runtime enforcement, evidence, and reauthorization;
- the AI Control Plane is reorganized into `00-actuators/`, `01-constraints/`, `02-sensors/`, and `03-controller/`;
- a draft-normative Constraint capability and informative realization catalog cover structural, authority, state, data, resource, environment, Human Authority, and soft behavioral mechanisms;
- the project review and template now include project constraint architecture, feasibility, evidence, authority, economics, inheritance, and reauthorization;
- the delivery review, template, and Judgment Node Boundary now include inherited source, local realization, hard or soft strength, failure behavior, evidence, configuration, change authority, and runtime reassessment;
- the failure taxonomy now includes missing, soft-as-hard, unenforced, bypassed, stale, conflicting, unauthorized, unavailable, slow, or economically destructive Constraints;
- README, AGENTS, specification navigation, and module indexes distinguish the four decision levels from the four capability classes;
- slide 12 is treated as research evidence for the capability distinction while its metaphor and named-tool mapping remain non-normative.

### Active and next milestones

- [ ] Complete repository-wide diagram, reference-architecture, and link review for the four-capability model.
- [ ] Build one two-level worked application connecting project authorization to one or more delivery reviews and runtime reauthorization.
- [ ] Trace at least one material Constraint from organizational source through project derivation, delivery realization, runtime enforcement and evidence, and reauthorization.
- [ ] Test project and delivery reviews through a real team or documented real system boundary.
- [ ] Complete cross-publication research synthesis.
- [ ] Identify stable concepts, later refinements, contradictions, and superseded claims.
- [ ] Refine canonical terminology where synthesis or application changes scope or meaning.
- [ ] Validate compatibility and proportionality through real-team applications and additional worked domains.

## Phase 3 — Patterns and Failure Modes

**Status: Active**

The objective is to turn the framework spine into reusable engineering guidance.

### Completed or active outcomes

- Judgment Node Boundary with proportional minimal and extended modes;
- compact Judgment Node card embedded in the pattern rather than a separate registry;
- project review pattern connecting outcome, risk scenarios, intended Judgment, Constraint architecture, required capabilities, evidence, Human Authority, operating capacity, economics, authorization, inheritance, and reauthorization;
- delivery review pattern connecting inherited Constraints, local realization, Requirements, Judgment Nodes, readiness, completion, release, runtime enforcement, and reassessment;
- explicit separation of project authorization, constraint realization, completion evidence, and deployment-specific residual-risk acceptance;
- scenario-based project risk mapping without a mandatory aggregate score;
- project authorization outcomes including delivery, conditions, bounded research, redesign, escalation, deferral, and No-Go;
- project reauthorization triggers for changes in autonomy, authority, Constraint feasibility, data, population, domain, deployment, capacity, economics, or evidence;
- placement reference architectures that isolate each functional Model Judgment class and show one composite system;
- a fully populated support-triage delivery review with three Judgment Nodes, bounded experimentation, DoR, DoD, residual risk, human-supervised release, runtime control, and reassessment;
- expanded failure-mode taxonomy covering Constraint, Sensor, Controller, Actuator, open-loop, socio-technical, capacity, and economic failure.

### Next outcomes

- a two-level worked project-and-delivery application with end-to-end Constraint traceability;
- containment, validation, retry, fallback, compensation, and escalation patterns;
- drift, dependency-change, and verification patterns;
- Human-in-the-Loop and Human-on-the-Loop patterns;
- operational examples and incident evidence for the failure taxonomy;
- explicit conditions where AI or a proposed autonomy level should not be used;
- deeper methods for deriving tolerances and hard Constraints from consequence, authority, detectability, reversibility, propagation, and capacity;
- additional worked domains and at least one real-team application.

## Phase 4 — Operating Model and Practical Artifacts

**Status: Active**

The objective is to make UA usable by small and medium-sized engineering teams without requiring a large governance organization.

### Completed or active outcomes

- one lightweight project-level review for feasibility, risk, Constraint architecture, capabilities, capacity, economics, authorization, inheritance, and reauthorization;
- one living project template containing decision summary, organizational context, Judgment landscape, scenario map, embedded Constraint architecture, capability map, evidence feasibility, Human Authority, control economics, authorization, inheritance, and decision history;
- one lightweight delivery review for framing, Constraint realization, implementation or bounded experimentation, completion, release, operation, and local reassessment;
- one living delivery template containing project inheritance, Judgment Node cards, concrete Constraint realization, full model-mediated DoR and DoD extensions, residual risk, active deployment Constraints, release decision, and reassessment history;
- responsibility bundles defined as responsibilities rather than mandatory job titles;
- versioned or immutable project and delivery snapshots used for traceability;
- explicit default that the SMB path does not require separate Constraint Registers, Judgment Node registries, governance-board protocols, readiness records, completion packages, responsibility matrices, risk maps, financial records, Project Launch Gate records, or Release Decision Records when the two reviews and linked evidence are sufficient;
- a four-level lifecycle connecting organizational context, project authorization, delivery realization and release, and runtime enforcement and reauthorization.

### Next outcomes

- one two-level worked example with Constraint inheritance and runtime evidence routing;
- real-team validation of both templates;
- risk, tolerance, and Constraint derivation guidance;
- deeper control-economics guidance covering ranges, sensitivity, enforcement maintenance, false blocks, Human Authority capacity, fallback load, latency, incident burden, and residual exposure;
- additional completed reviews across different domains, authority levels, and consequence profiles;
- adoption guidance based on practical feedback;
- incident, change, exception, and learning-loop refinements where application exposes concrete gaps.

A new top-level Operating Model module is not planned at this stage. Project and delivery responsibilities remain patterns and practical artifacts until several stable independent components justify a structural change.

## Phase 5 — Optional Tooling and Reference Implementations

**Status: Later**

Tooling is optional and must serve the specification rather than redefine it.

Possible outcomes:

- metadata and internal-link validation;
- repository checks for stale control-plane paths;
- example Constraint, prompt, policy, evaluation, and release manifests;
- reference control-plane implementations;
- executable Constraint realization examples;
- architecture demonstrations;
- reusable templates generated from stable specification components.

No universal SDK, platform, policy engine, or agent framework is planned.

## Current priority

The current draft contains two connected but separately owned control decisions:

1. **Project authorization:** whether a proposed Thinking System has a credible, operable, and economically viable Constraint and control architecture.
2. **Delivery release:** whether one bounded system, feature, or material change has correctly realized the inherited boundary, sufficient evidence, and acceptable residual risk for a specific deployment context.

The immediate priority is not another review artifact. It is to test inheritance, realization, enforcement, evidence, and feedback through one two-level worked application.

The expected sequence is:

```text
Controlled-object doctrine
→ Four-capability Control-Loop Anatomy
→ Project Constraint and Control Architecture Review
→ Delivery Thinking System Review with concrete realization
→ Two-level worked application
→ Real-team validation and refinement
```

The worked application should show:

- organizational Constraint sources, shared capabilities, and decision rights;
- project-level outcome, Judgment landscape, material scenarios, project Constraints, required Sensors, Controllers and Actuators, evidence and capacity analysis, economics, and authorization;
- a versioned authorization and Constraint inheritance package;
- one or more delivery reviews that implement and verify concrete realization around local Judgment Nodes;
- runtime enforcement state, violations, bypass attempts, false blocks, control-health evidence, Controller decisions, and Actuator execution;
- evidence that remains local versus evidence that triggers project reauthorization or organizational review;
- how duplication and parallel registries are avoided.

Cross-publication synthesis should continue alongside application. Material findings from either track should reconcile affected research questions, traceability, doctrine, patterns, practical artifacts, reference architectures, and failure modes through explicit review.

The project should continue to avoid multiplying governance documents. Future refinement should simplify or strengthen the two review surfaces based on application evidence rather than add parallel gates, registries, or scorecards.

The project optimizes for durable clarity, traceability, and practical usefulness rather than rapid expansion of repository volume.
