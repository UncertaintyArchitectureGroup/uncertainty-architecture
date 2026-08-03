---
title: Uncertainty Architecture Open Engineering Specification Article Blueprint
artifact_type: research-note
status: research
maturity: draft
module: research
topics:
  - thinking-systems
  - control-loop
  - constraints
  - sdlc
  - repository-architecture
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/thinking-systems
  - ua/topic/control-loop
  - ua/topic/constraints
  - ua/topic/sdlc
  - ua/topic/repository-architecture
created: 2026-07-31
updated: 2026-08-03
language: en
license: CC-BY-4.0
draft: true
---

# Uncertainty Architecture: An Open Engineering Specification for Thinking Systems

**Proposed subtitle:** From project viability to delivery realization, runtime evidence, and reauthorization

> **Blueprint status:** This document is a drafting-ready editorial contract proposed for Phase 1 acceptance. It is a non-normative research note, not article prose and not a specification source. Every final claim must defer to the current repository specification, glossary, doctrine, patterns, AI Control Plane, reference architectures, failure modes, and explicit maturity state.

## 1. Editorial decision

The article will present one connected argument:

```text
Thinking Systems change the controlled object
→ model quality and observability are not sufficient for control
→ bounded operation requires four control-capability families
→ decisions are owned at four connected lifecycle levels
→ authoritative Constraints flow downward by reference while realization becomes concrete
→ runtime evidence returns to the decision level whose basis it invalidates
→ one project review and one delivery review provide the default SMB operating surface
→ one Constraint trace demonstrates the complete path
→ platforms may implement capabilities without inheriting organizational authority by default
→ the open specification is coherent enough to test but not mature enough to declare complete
```

The four decision levels are the article's conceptual center. The four capability families explain how decisions at every level become operational. The two models remain orthogonal and must not be presented as competing lifecycles, a one-to-one matrix, or a mandatory physical stack.

The article will use eight sections. Earlier proposals for ten sections are consolidated to remove repeated explanations of control theory, inheritance, artifacts, openness, maturity, and the platform boundary.

## 2. Central thesis and claim boundary

### Stable thesis paragraph

Thinking Systems change the object being engineered because consequential runtime behavior may be produced through probabilistic Model Judgment rather than fully enumerated deterministic logic. Evaluation, observability, policies, human approval, and agent orchestration are useful but remain incomplete when they are not connected to approved Constraints, concrete Constraint Realizations, decision authority, corrective action, and reassessment. Uncertainty Architecture provides an open, tool-neutral specification for connecting those responsibilities across organizational, project, delivery, and runtime decision levels while preserving a lightweight default operating path for small and medium-sized teams.

### Defensible claim

UA provides a coherent draft specification spine for reasoning about and operating model-mediated systems from project authorization through delivery release and runtime reassessment.

### Claims the article must not make

The article must not claim that UA is:

- an accepted industry standard;
- a complete scientific theory;
- independently validated across multiple teams or domains;
- a universal governance or compliance framework;
- a replacement for Agile, DevOps, QA, security, incident response, legal review, or organizational policy;
- a mandatory four-service AI Control Plane;
- a universal risk score, maturity ladder, threshold method, or role model;
- a finished product or SDK;
- supported by a complete repository-level project-to-runtime worked application that does not yet exist.

## 3. Audience, tone, and reader promise

### Primary readers

- software and enterprise architects placing Model Judgment inside production systems;
- engineering, delivery, product, and project leaders deciding whether an AI path is viable beyond a prototype;
- AI platform and agent-framework builders implementing control capabilities;
- security, risk, legal, compliance, and governance practitioners connecting authoritative sources to technical operation;
- practitioners and researchers able to test the specification through application evidence.

### Tone

- architectural rather than promotional;
- direct and skeptical of hype without attacking adjacent disciplines or products;
- precise about authority, evidence, failure, and maturity;
- practical for SMB teams without assuming enterprise governance structure;
- open to contradiction and revision.

### Reader promise

By the end, the reader should understand:

1. why consequential Model Judgment changes the controlled object;
2. the difference between measurement, a closed feedback loop, and a complete bounded UA control architecture;
3. the four capability families and their boundaries;
4. the four decision levels and the question owned by each;
5. how Project Constraint Architecture, delivery Constraint Realization Map, runtime evidence, and reassessment connect;
6. why project authorization, DoR, DoD, Release Gate, runtime correction, and project reauthorization are different decisions;
7. how a small team can operate the model without creating parallel governance bureaucracy;
8. what platforms may implement and what authority they do not obtain automatically;
9. what exists in the repository and what remains unvalidated.

## 4. Final article structure

### 4.1 The Missing Engineering Connection

**Purpose**  
Establish the practical gap before introducing UA terminology.

**Core claim**  
The ecosystem has many responsible components, but policies, evaluations, traces, approval steps, and orchestration tools do not become a governable system unless they are connected to authorization, bounded authority, decision ownership, corrective action, and reassessment.

**Required points**

- Open with a credible team that has a model, retrieval or tools, traces, evaluations, policy, human approval, and a pilot.
- Show the connected questions the team still cannot answer:
  - Was Model Judgment necessary?
  - What authority was delegated?
  - Which consequences are prohibited or unacceptable?
  - Which Constraints are authoritative?
  - How are those Constraints realized?
  - Which evidence informs which decision?
  - Who may narrow, roll back, disable, redesign, or stop operation?
  - When does runtime evidence invalidate project authorization?
  - Does the business case survive the complete control cost?
- State the market claim narrowly: practices may remain fragmented by product boundary, decision level, or organizational function.
- Support any factual claim about current industry practice with current primary or authoritative sources during Phase 2. When evidence is unavailable, frame the point explicitly as a practitioner observation rather than an established market fact.
- Do not claim that no governance, safety, systems, or control practice exists.

**Canonical source anchors**

- [`SPECIFICATION.md`](../../../SPECIFICATION.md)
- [`00-doctrine/uncertainty-in-the-controlled-object.md`](../../../00-doctrine/uncertainty-in-the-controlled-object.md)
- [`04-failure-modes/README.md`](../../../04-failure-modes/README.md)

**Must not repeat elsewhere**  
The full inventory of disconnected point solutions and the general industry-gap argument.

**Transition**  
The gap exists because teams are still treating AI as an additional component inside an unchanged engineering object.

**Intended closing claim**

> The missing layer is not another AI component. It is the engineering connection between delegated judgment, authorized boundaries, evidence, decision authority, and corrective action.

**Word budget:** 400–500

---

### 4.2 The Controlled Object Has Changed

**Purpose**  
Explain the doctrinal reason UA exists.

**Core claim**  
A Thinking System produces part of its consequential uncertainty inside the engineered object because runtime behavior depends partly on probabilistic Model Judgment.

**Required points**

- Use deterministic software as a design-contract distinction, not a claim of perfect repeatability:

  ```text
  y = f(x)
  ```

- Introduce model-mediated responsibility as behavior selected from plausible outcomes under input, context, model, configuration, state, and operating conditions:

  ```text
  y ~ P(y | x, context, model configuration, system state)
  ```

- Explain Model Judgment through interpretation, classification, ranking, planning, generation, routing, or action selection.
- State that useful variance is the reason the model is present; the objective is containment rather than elimination of all variance.
- Distinguish:
  - product and requirement uncertainty;
  - environment and operational uncertainty;
  - runtime-judgment uncertainty.
- State that UA complements product discovery, Agile, DevOps, QA, security, change management, resilience, and incident response.
- Avoid claiming that identical model calls must always produce different outputs.

**Canonical source anchors**

- [`00-doctrine/uncertainty-in-the-controlled-object.md`](../../../00-doctrine/uncertainty-in-the-controlled-object.md)
- [`00-doctrine/glossary.md`](../../../00-doctrine/glossary.md)
- [`00-doctrine/model-judgment-placement.md`](../../../00-doctrine/model-judgment-placement.md)

**Figure 1 — Controlled-object shift**

Required visual message:

```text
External and delivery uncertainty
        ↓
Explicit deterministic responsibilities
        ↓
Model Judgment inside the runtime path
        ↓
Multiple plausible behaviors
        ↓
Deterministic responsibilities, Constraints and realizations,
evidence, decision authority, and corrective action
```

The figure must not imply that traditional software has no uncertainty or that a Thinking System is wholly probabilistic.

**Must not repeat elsewhere**  
The full deterministic-versus-model-mediated explanation.

**Transition**  
Once the system itself produces consequential uncertainty, quality measurement is necessary but no longer the complete engineering contract.

**Intended closing claim**

> The problem is not merely that AI is harder to test. Part of the controlled object's behavior is now produced through runtime judgment.

**Word budget:** 450–550

---

### 4.3 From Model Quality to Bounded Control

**Purpose**  
Introduce the accepted Control-Loop Capability Anatomy and distinguish feedback closure from bounded acceptable operation.

**Core claim**  
A measured system is not necessarily controlled, and a closed feedback loop is not necessarily operating inside an approved boundary.

**Required points**

- Use the canonical closed-feedback path:

  ```text
  Thinking System
  → Sensors and evidence
  → Controller and decision authority
  → Actuators and corrective action
  → changed Thinking System operation
  ```

- Explain why the feedback loop may remain closed while unsafe, over-authorized, or economically unacceptable.
- Introduce the four logical capability families:
  1. **Constraints and their realizations** define and operationalize approved boundaries.
  2. **Sensors and evidence** observe behavior, outcomes, operating conditions, realization state, Actuator execution, and control health.
  3. **Controllers and decision authority** compare or interpret evidence relative to approved Requirements, Constraints, and assumptions, then select or authorize action.
  4. **Actuators and corrective action** execute authorized changes to operation or a Constraint Realization.
- Preserve these distinctions:
  - Constraint is an authoritative decision object.
  - Constraint Realization is the technical or socio-technical mechanism implementing, enforcing, or influencing it.
  - Constraint Realization is not a fifth family.
  - Controller decides or authorizes; Actuator executes.
  - evaluator and metrics normally perform Sensor functions;
  - logic selecting `block`, `canary`, or `release` performs a Controller function;
  - deployment, blocking, exposure change, or rollback performs an Actuator function.
- Explain scoped Hard and Soft claims:
  - a Hard Constraint's complete realized path deterministically prevents or rejects violation within stated assumptions, subject, path, scope, and enforcement boundaries;
  - prompts, natural-language policies, probabilistic evaluators, and model preferences are not hard by themselves;
  - different guarantee strengths require separate Constraint records.
- Use short anti-examples:
  - telemetry without a Controller is observation;
  - a Controller without an effective Actuator cannot correct;
  - policy without credible realization is not an operable boundary;
  - a nominal human approval step is not substantive Human Authority;
  - a kill-switch endpoint without authority, evidence, and operability is not a complete control system.

**Canonical source anchors**

- [`00-doctrine/control-loop-anatomy.md`](../../../00-doctrine/control-loop-anatomy.md)
- [`02-ai-control-plane/README.md`](../../../02-ai-control-plane/README.md)
- [`02-ai-control-plane/01-constraints/README.md`](../../../02-ai-control-plane/01-constraints/README.md)
- [`02-ai-control-plane/01-constraints/constraint-realization-catalog.md`](../../../02-ai-control-plane/01-constraints/constraint-realization-catalog.md)

**Must not repeat elsewhere**  
Detailed capability definitions and the closed-loop-versus-bounded-operation distinction.

**Transition**  
The capability anatomy explains how control works, but not where project, release, runtime, and organizational decisions are owned.

**Intended closing claim**

> A closed loop can still be unacceptable. UA asks whether that loop operates inside an approved, credibly realized, observable, and correctable boundary.

**Word budget:** 550–600

---

### 4.4 Four Decision Levels of Uncertainty Architecture

**Purpose**  
Present the Nested Control Lifecycle as the article's conceptual center.

**Core claim**  
Different control decisions require different evidence, authority, time horizons, and corrective actions; they must remain connected without collapsing into one gate or governance process.

**Figure 2 — Two orthogonal UA models**

The figure must show two adjacent, explicitly orthogonal views.

**Decision ownership view:**

```text
Organizational control context
        ↓ authoritative sources, shared capabilities, decision rights
Project control architecture and viability
        ↓ versioned Project Constraint Architecture and authorization
Delivery-level Thinking System Review
        ↓ concrete Constraint Realization Map and deployment-specific release decision
Runtime operation and reassessment
        ↑ local evidence / project invalidation / organizational invalidation
```

**Capability view, applying at every level:**

```text
Constraints and their realizations
Sensors and evidence
Controllers and decision authority
Actuators and corrective action
```

The figure must not imply a one-to-one mapping between four levels and four families, four mandatory services, or a one-way waterfall.

#### Organizational control context

**Question owned:** Within which authoritative boundaries, shared capabilities, and decision rights may projects operate?

**Required points**

- Link existing legal, contractual, security, privacy, safety, procurement, vendor, geography, prohibited-use, incident, and decision-right sources.
- Do not create a mandatory UA organizational artifact or governance department.
- Shared capabilities may include identity, authorization, audit, evaluation, incident response, Human Authority, rollback, containment, compensation, and shutdown.
- Organizational sources do not become Hard Constraints merely because they are authoritative; the realized path and scoped guarantee still matter.

#### Project control architecture and viability

**Question owned:** Does a credible, operable, and economically viable control architecture exist for this proposed Thinking System within a defined boundary?

**Required points**

- The [`Project Control Architecture and Viability Review`](../../../01-patterns/project-control-architecture-and-viability-review.md) owns:
  - outcome and AI necessity;
  - project boundary and intended Judgment landscape;
  - material scenarios and consequences;
  - organizational Constraint interpretation and project-specific Constraints;
  - one canonical **Project Constraint Architecture**;
  - required realization capabilities and assumptions;
  - required Sensors, Controllers, Actuators, Human Authority, fallback, containment, compensation, rollback, and shutdown;
  - evidence feasibility and latency;
  - operating capacity and control economics;
  - authorization, conditions, bounded research, redesign, deferral, escalation, or No-Go;
  - delivery inheritance and project reauthorization triggers.
- A successful prototype is not project authorization.
- Architectural Veto is a valid engineering outcome.

#### Delivery-level Thinking System Review

**Question owned:** Is a bounded system, feature, or material change ready, complete, and acceptable for a specific deployment context under the project authorization?

**Required points**

- The [`Thinking System Review`](../../../01-patterns/thinking-system-review.md) owns:
  - implementation-level Judgment Nodes;
  - the delivery Requirement and Operating Envelope;
  - one canonical **Constraint Realization Map** linked to the project baseline;
  - Definition of Ready;
  - bounded experiment or implementation;
  - Definition of Done;
  - deployment-specific Release Gate;
  - local runtime reassessment.
- Distinguish:
  - DoR establishes readiness and the authority basis for beginning bounded work;
  - DoD establishes implementation and evidence completeness;
  - Release Gate accepts, limits, conditions, escalates, or rejects a deployment.
- Delivery may narrow but must not expand project authority or weaken an inherited Hard Constraint.

#### Runtime operation and reassessment

**Question owned:** Does active operation remain within the approved Requirement, Constraint baseline, authority, capacity, and economics, with required realizations active and healthy, and what action follows when it does not?

**Required points**

- Runtime exercises deployed realizations and produces evidence about:
  - behavior and downstream outcomes;
  - realization state, violations, bypass, conflict, degradation, and unavailability;
  - false blocks and friction;
  - Actuator execution and resulting state;
  - Human Authority and fallback capacity;
  - project and organizational assumptions.
- Evidence reaches an authorized Controller; Actuators execute correction, narrowing, fallback, containment, compensation, rollback, suspension, or shutdown.
- Runtime operation does not require a mandatory third governance register.
- Route evidence by the decision basis invalidated:

  ```text
  local implementation, realization, configuration, or evidence issue
  → delivery reassessment

  project risk, authority, feasibility, evidence, capacity, or economics changed
  → project reauthorization

  authoritative source, decision right, or shared capability changed
  → organizational review
  ```

**Must not repeat elsewhere**  
Full ownership definitions for the four levels.

**Transition**  
The lifecycle becomes practical only when authoritative decisions are inherited rather than recopied and when concrete runtime evidence can be traced back to the decision it challenges.

**Intended closing claim**

> Lower levels may refine and narrow a higher-level decision. They may not silently expand its authority or normalize evidence that invalidates it.

**Word budget:** 950–1,150

---

### 4.5 From Authority to Operation: Two Living Reviews

**Purpose**  
Explain inheritance, realization, evidence routing, and the default SMB operating surface without reproducing templates.

**Core claim**  
UA reduces duplication by preserving one project Constraint artifact and one delivery realization artifact, linked to existing organizational sources and runtime evidence.

**Canonical path**

```text
Existing organizational sources, shared capabilities, and decision rights
→ one living Project Control Architecture and Viability Review
→ one versioned Project Constraint Architecture and authorization
→ one living Thinking System Review per bounded delivery scope
→ one canonical Constraint Realization Map
→ deployment-specific Release Gate
→ active runtime versions, evidence, decisions, and actions
→ delivery reassessment, project reauthorization, or organizational review
```

**Required points**

- Constraint authority flows downward by reference; policy prose is not copied as if it were a complete technical control.
- At project level, Constraints are interpreted or derived, scoped, assigned required realization and assumptions, connected to evidence, authority, economics, inheritance, and reauthorization.
- At delivery level, realization becomes concrete through active mechanisms, configuration, verification, failure behavior, evidence, change authority, and release scope.
- At runtime, active source, project, delivery, realization, model, prompt, policy, tool, and deployment versions remain traceable where material.
- Judgment Node cards reference delivery Constraint IDs instead of redefining Constraints locally.
- DoR, DoD, Release Gate, and runtime sections reference the same Constraint Realization Map rather than creating parallel records.
- Additional risk registers, Constraint Registers, RACIs, gate files, financial models, or responsibility matrices are optional when independent ownership, lifecycle, access, retention, regulation, or audit needs justify them.
- Two living reviews are the default proportional path, not a claim that they are sufficient for every organization or consequence level.
- One person may hold several responsibility bundles without collapsing the decisions.

**Canonical source anchors**

- [`00-doctrine/nested-control-lifecycle.md`](../../../00-doctrine/nested-control-lifecycle.md)
- [`01-patterns/project-control-architecture-and-viability-review-template.md`](../../../01-patterns/project-control-architecture-and-viability-review-template.md)
- [`01-patterns/thinking-system-review-template.md`](../../../01-patterns/thinking-system-review-template.md)
- [`01-patterns/judgment-node-boundary.md`](../../../01-patterns/judgment-node-boundary.md)

**Must not repeat elsewhere**  
The complete inheritance and two-artifact explanation.

**Transition**  
A single Constraint trace can demonstrate whether this structure changes real decisions rather than merely reorganizing terminology.

**Intended closing claim**

> The goal is not to document everything repeatedly. It is to preserve the chain from authoritative source to scoped Constraint, concrete realization, runtime evidence, and corrective decision.

**Word budget:** 400–500

---

### 4.6 One Constraint Across the Full Lifecycle

**Purpose**  
Provide one continuous project-to-runtime narrative without claiming that the repository already contains a completed two-level worked application.

**Source boundary**  
The narrative is an editorial synthesis using the project pattern, Constraint capability, and the existing illustrative delivery review for support triage. The final article must state that the repository currently contains a delivery-level worked example, while a complete two-level worked application remains roadmap work.

**Scenario**  
A company wants a Thinking System to interpret English-language Product A support tickets, recommend routing, and draft grounded replies for trained support agents.

**Constraint selected for the trace**

> The model-mediated path may create a draft but must not send customer communication without Human Authority.

#### Organizational source

- Autonomous customer communication is prohibited for the initial use case.
- Human Authority is required before outbound communication.
- Existing identity, authorization, audit, incident, and shutdown capabilities are authoritative dependencies.
- An organizational exception would be required to permit autonomous sending.

#### Project Constraint Architecture

Use one illustrative record:

```text
Constraint ID: K-SEND-01
Intent: prevent model-mediated autonomous customer communication
Source/rationale: organizational prohibited-use and customer-commitment boundary
Subject: outbound send action
Path: every model-mediated tool, API, workflow, and alternate execution path
Scope: English-language Product A support within the authorized initial population
Class: Human Authority
Claimed strength: Hard, within stated assumptions
Required realization: model-path identity has no send permission; only a human-operated approved path may send after review
Assumptions: credentials remain isolated; no alternate endpoint bypasses the gate; active permission state is verified
Failure behavior: fail closed; preserve draft; route to manual handling; disable feature when authorization state is unknown
Evidence: negative permission tests, denied-send events, active permission/configuration versions, approved human-send attribution, bypass tests
Change authority: delivery may repair or roll back inside the baseline; autonomous sending requires project reauthorization and organizational review
```

The project may authorize bounded delivery only if this realization, evidence, Human Authority capacity, fallback, and control economics are credible.

#### Delivery Constraint Realization Map

The delivery review maps `K-SEND-01` to:

- a service identity with no outbound-send permission;
- a deterministic authorization gate covering all send paths;
- a draft queue visible to trained support agents;
- a human-operated send action separated from Model Judgment;
- auditable linkage among draft, reviewer decision, and send event;
- fail-closed behavior when permission or approval state is unavailable;
- negative-authority, bypass, and configuration-drift tests;
- runtime evidence and local rollback/disable Actuators.

Each Judgment Node references `K-SEND-01`. The node cards do not rewrite the Constraint.

#### DoR, DoD, and Release Gate

- **DoR:** inherited Constraint and scope, Judgment Nodes, complete realization design, assumptions, evidence, Human Authority, fallback, and bounded experiment are explicit.
- **DoD:** the realization is implemented; every reviewed send path is covered; bypass and unavailable behavior are tested; evidence and Actuators are operational.
- **Release Gate:** active realization versions, reviewer capacity, deployment population, residual risk, and rollback/disable readiness are acceptable for the limited release.

#### Runtime evidence and change routing

Use two runtime evidence outcomes and one separate authority-change request:

1. **Local realization defect**  
   A configuration mismatch is detected before any unauthorized send path becomes reachable. Delivery fails closed, corrects the configuration, verifies the complete path, and passes a new Release Gate.

2. **Project assumption invalidated**  
   Human review volume and latency make the control perimeter economically non-viable at planned scale. `K-SEND-01` remains valid, but project capacity and economics no longer do. The result is project reauthorization: narrow eligible cases, population, or volume; redesign the workflow; or reject the AI path.

3. **Authority expansion requested**  
   The business requests autonomous sending. This is not runtime evidence or a delivery tuning change. It changes project authority and conflicts with the organizational source. It requires project reauthorization and organizational review before any new realization may be designed.

**Figure 3 — Constraint trace**

```text
Organizational prohibition and Human Authority requirement
        ↓
Project K-SEND-01
subject + path + scope + Hard claim + assumptions
        ↓
Delivery Constraint Realization Map
no-send identity + deterministic gate + human send path + evidence
        ↓
Runtime operation and evidence
        ├─ local defect → delivery reassessment
        └─ capacity/economics invalidated → project reauthorization

Separate proposed authority expansion
        └─ autonomous sending → project reauthorization + organizational review
```

**Canonical source anchors**

- [`01-patterns/project-control-architecture-and-viability-review.md`](../../../01-patterns/project-control-architecture-and-viability-review.md)
- [`01-patterns/thinking-system-review.md`](../../../01-patterns/thinking-system-review.md)
- [`03-reference-architectures/worked-thinking-system-review-support-triage.md`](../../../03-reference-architectures/worked-thinking-system-review-support-triage.md)
- [`02-ai-control-plane/01-constraints/constraint-realization-catalog.md`](../../../02-ai-control-plane/01-constraints/constraint-realization-catalog.md)

**Must not repeat elsewhere**  
Detailed support-triage scenario content and the full K-SEND-01 trace.

**Transition**  
The example separates the architecture from the tools that may implement it, which makes the platform boundary precise.

**Intended closing claim**

> Evidence and proposed authority changes must route according to the decision basis they invalidate or seek to change, not merely according to where they first appear.

**Word budget:** 600–700

---

### 4.7 What Platforms Can Implement — and What They Cannot Authorize

**Purpose**  
Address productization without dismissing agent, governance, observability, or AI-native delivery platforms.

**Core claim**  
A platform may implement several UA capabilities and records, but it does not receive organizational or project decision authority merely by hosting them.

**Required points**

- Classify platform functions by what they do in the specific system, not by market category.
- Platforms may host or implement:
  - Constraint Realizations such as permissions, schemas, state gates, policy engines, data boundaries, budgets, approval paths, and deployment limits;
  - Sensors and evidence such as traces, evaluations, incidents, realization state, and Actuator-effect evidence;
  - bounded automated Controller logic and human decision interfaces;
  - Actuators such as block, route, narrow exposure, change configuration, fall back, roll back, disable, compensate, or stop;
  - version and decision records.
- A platform does not independently determine:
  - whether Model Judgment is necessary;
  - which organizational source is authoritative;
  - what consequences and authority are acceptable;
  - who may accept residual risk;
  - whether Human Authority is substantive and sufficiently staffed;
  - whether the control perimeter preserves project viability;
  - when project or organizational authorization must change.
- A platform may execute delegated authority. It does not create that authority.
- Avoid categorical claims that platforms “cannot solve governance.” State the narrower ownership boundary.
- Verify claims about any named platform against current first-party documentation during Phase 2. When the article does not need a named product, keep the argument functional and vendor-neutral.

**Canonical source anchors**

- [`02-ai-control-plane/README.md`](../../../02-ai-control-plane/README.md)
- [`AGENTS.md`](../../../AGENTS.md)
- [`SPECIFICATION.md`](../../../SPECIFICATION.md)

**Must not repeat elsewhere**  
The platform-versus-authority boundary.

**Transition**  
This separation is why UA is developed as an open specification rather than as one privileged implementation.

**Intended closing claim**

> A platform can make control capabilities easier to implement. It cannot, by default, authorize the project or define the organizational boundary in which that implementation is legitimate.

**Word budget:** 350–400

---

### 4.8 Open Specification: Current State, Limits, and Invitation

**Purpose**  
End with an accurate repository state and a serious request for validation rather than a product-style CTA.

**Core claim**  
UA has a coherent, inspectable draft specification spine, but independent application evidence remains insufficient for a maturity claim.

**What exists in the repository**

- controlled-object doctrine and canonical glossary;
- Control-Loop Capability Anatomy;
- Nested Control Lifecycle;
- Requirement, Correctness, Bug, and Model Judgment Placement doctrine;
- Judgment Node Boundary;
- Project Control Architecture and Viability Review with an informative template;
- Thinking System Review with an informative template;
- Constraint capability and informative realization catalog;
- Sensors, Controllers, and Actuators capability guidance;
- placement-focused reference architectures;
- one illustrative delivery-level support-triage review;
- failure-mode taxonomy;
- research provenance and framework traceability.

**What does not yet exist or remain proven**

- a completed repository-level two-level project-and-delivery worked application;
- independent real-team use across multiple organizations;
- evidence that two living reviews are sufficient in every context;
- validated time-to-complete, usability, and decision-quality evidence;
- mature control-cost and Human Authority capacity methods;
- validated incident and drift patterns across domains;
- universal threshold derivation;
- proof that teams can apply UA correctly without author involvement;
- evidence that current terminology and boundaries will survive sustained external use unchanged.

**Why open**

- enable independent critique and contradictory evidence;
- compare application across domains and implementations;
- prevent a vendor, consultancy, platform, or author from owning the complete language of control;
- preserve visible evolution of decisions and terminology;
- allow many products and organizations to implement the specification.

**Licensing**

- documentation and specification material: CC BY 4.0;
- code and future reference implementations: Apache 2.0.

**Validation request**

Ask readers for:

- documented worked applications;
- anonymized project and delivery reviews;
- contradictory cases;
- issue reports against unclear terminology or ownership;
- proposals that simplify the review surface;
- examples of platform mappings;
- evidence of realization, Human Authority, capacity, cost, or reassessment failures;
- operational failure modes discovered in real systems.

Ask concrete questions:

- Which decision level remains ambiguous?
- Where do Constraint source, subject, path, scope, strength, realization, or authority remain unclear?
- Which evidence cannot be routed honestly through the proposed model?
- When are two living reviews insufficient?
- Does the default path reduce duplication in practice?
- Which system classes break the lifecycle or capability anatomy?
- Which controls make the project non-viable?
- Can a team apply the specification without the author in the room?

**Intended closing claim**

> Uncertainty Architecture is coherent enough to be tested, not mature enough to be protected from criticism. The next step is external application, contradictory evidence, and revision.

**Word budget:** 400–500

## 5. Figure plan

Use exactly three primary figures.

### Figure 1 — Controlled-object shift

Shows the changed engineering object without claiming that deterministic software has no uncertainty or that a Thinking System is wholly probabilistic.

### Figure 2 — Two orthogonal UA models

Shows:

- four decision levels with downward inheritance and upward reassessment;
- four capability families applying at every level;
- explicit non-equivalence between levels and families;
- no mandatory physical stack or one-way waterfall.

This is the article's central figure.

### Figure 3 — K-SEND-01 Constraint trace

Shows one authoritative source becoming a scoped Project Constraint, a concrete delivery realization, runtime evidence, and correctly separated reassessment and authority-change routes.

Do not use the earlier presentation brain/nerves/skeleton/muscles stack as the canonical article figure. It may be mentioned as source history only when useful.

## 6. Terminology and claim-safety rules

### Required current terms

- Thinking System;
- Model Judgment;
- Judgment Node;
- Constraint;
- Constraint Realization;
- Hard Constraint and Soft Constraint as scoped realized-path claims;
- Sensor;
- Controller;
- Actuator;
- Human Authority;
- Project Constraint Architecture;
- Constraint Realization Map;
- Nested Control Lifecycle;
- Project Authorization and Project Reauthorization;
- Definition of Ready, Definition of Done, and Release Gate.

### Historical or contextual terms only

- Behavioral Software;
- Behavioral Applications;
- mandatory Prompt Steward, Eval Owner, AI Reliability Engineer, or other fixed role titles;
- universal maturity ladders, sample sizes, thresholds, or review cadences;
- Operating Model as one monolithic Controller;
- three-part Actuator/Sensor/Controller taxonomy where Constraints were unresolved.

### Technical and evidence safety rules

- Do not call a prompt, natural-language policy, probabilistic evaluator, classifier, or model preference a Hard Constraint by itself.
- Do not call a schema or permission check a Constraint without distinguishing the authoritative Constraint from its realization.
- Do not describe Actuators as defining policy or authorizing their own changes.
- Do not collapse evaluator, gate decision, and release execution into one function.
- Do not equate a closed feedback loop with acceptable bounded operation.
- Do not imply that every realization acts before the model call or that the four families form a vertical pipeline.
- Do not imply that runtime “reauthorizes” a project automatically; runtime evidence triggers the owning decision process.
- Do not classify every deviation as a Bug; diagnosis depends on the approved Requirement.
- Do not describe aggregate quality, cost, latency, or capacity tolerances as Hard Constraints unless a separate scoped realization deterministically enforces the boundary.
- Do not use internal UA documents as evidence for claims about current external standards, products, laws, or market practice. Verify those claims against current primary or authoritative external sources during Phase 2.

## 7. Publication framing

### Primary title

**Uncertainty Architecture: An Open Engineering Specification for Thinking Systems**

### Subtitle

**From project viability to delivery realization, runtime evidence, and reauthorization**

### Optional distribution headline

**We Have Been Governing AI at the Wrong Level**

The distribution headline belongs in LinkedIn or another wrapper, not in the canonical repository article title.

### Target length

**4,300–5,200 English words.**

Approximate allocation:

| Section | Words |
|---|---:|
| Abstract and opening | 200–250 |
| Missing Engineering Connection | 400–500 |
| Controlled Object | 450–550 |
| Bounded Control | 550–600 |
| Four Decision Levels | 950–1,150 |
| Two Living Reviews | 400–500 |
| One Constraint Trace | 600–700 |
| Platform Boundary | 350–400 |
| State, Limits, Invitation | 400–500 |

The ranges total approximately 4,300–5,150 words. The lifecycle is the conceptual center. The Constraint trace is the concrete center. Platform positioning and licensing remain concise.

## 8. Source plan for Phase 2

### Canonical UA sources

Phase 2 drafting must use current canonical repository files rather than historical articles as definitions:

1. [`SPECIFICATION.md`](../../../SPECIFICATION.md)
2. [`00-doctrine/glossary.md`](../../../00-doctrine/glossary.md)
3. [`00-doctrine/uncertainty-in-the-controlled-object.md`](../../../00-doctrine/uncertainty-in-the-controlled-object.md)
4. [`00-doctrine/control-loop-anatomy.md`](../../../00-doctrine/control-loop-anatomy.md)
5. [`00-doctrine/nested-control-lifecycle.md`](../../../00-doctrine/nested-control-lifecycle.md)
6. [`00-doctrine/requirements-correctness-and-bugs.md`](../../../00-doctrine/requirements-correctness-and-bugs.md)
7. [`00-doctrine/model-judgment-placement.md`](../../../00-doctrine/model-judgment-placement.md)
8. [`01-patterns/project-control-architecture-and-viability-review.md`](../../../01-patterns/project-control-architecture-and-viability-review.md)
9. [`01-patterns/thinking-system-review.md`](../../../01-patterns/thinking-system-review.md)
10. [`01-patterns/judgment-node-boundary.md`](../../../01-patterns/judgment-node-boundary.md)
11. [`02-ai-control-plane/README.md`](../../../02-ai-control-plane/README.md)
12. [`02-ai-control-plane/01-constraints/README.md`](../../../02-ai-control-plane/01-constraints/README.md)
13. [`03-reference-architectures/worked-thinking-system-review-support-triage.md`](../../../03-reference-architectures/worked-thinking-system-review-support-triage.md)
14. [`04-failure-modes/README.md`](../../../04-failure-modes/README.md)
15. [`ROADMAP.md`](../../../ROADMAP.md)

Historical articles, talks, and the presentation may provide provenance and explanatory language. They must not override the current framework.

### External evidence

Current factual claims about standards, laws, platform capabilities, market practice, or the state of AI governance must be checked during Phase 2 against current primary or authoritative sources. External sources support public factual claims; they do not become canonical definitions of UA.

Named platform capabilities should be verified against first-party documentation. Comparative claims should be narrow, dated, and avoid implying exhaustive market coverage.

## 9. Phase 2 drafting sequence

Draft in four connected blocks.

### Block A — Problem and doctrine

- abstract and opening;
- Missing Engineering Connection;
- Controlled Object Has Changed.

### Block B — Control architecture

- From Model Quality to Bounded Control;
- Four Decision Levels.

### Block C — Operating path and application

- Two Living Reviews;
- K-SEND-01 Constraint trace.

### Block D — Positioning and validation

- platform boundary;
- current state, limits, openness, and invitation.

After all blocks exist, perform one integrated pass for:

- duplicated claims;
- terminology against the glossary;
- separation of decision levels and capability families;
- Constraint versus Constraint Realization;
- Controller versus Actuator;
- accurate Hard and Soft claims;
- project authorization versus delivery release;
- runtime correction versus project reauthorization;
- runtime evidence versus proposed authority changes;
- unsupported maturity, external-fact, or repository-state claims;
- exact links and figure placement;
- narrative momentum and final word count.

## 10. Phase 1 acceptance criteria

This blueprint is ready for maintainer acceptance when:

- [x] one stable thesis paragraph exists;
- [x] the section sequence is fixed at eight sections;
- [x] every section has one unique logical function;
- [x] the capability anatomy reflects the accepted four-family model;
- [x] Constraints remain distinct from Constraint Realizations;
- [x] the four decision levels remain the article's conceptual center;
- [x] project authorization, delivery DoR, DoD, Release Gate, runtime correction, and project reauthorization remain separate;
- [x] Project Constraint Architecture and delivery Constraint Realization Map are the two canonical Constraint artifacts;
- [x] inheritance down and evidence up are demonstrated concretely;
- [x] the SMB two-review model is accurately scoped and non-universal;
- [x] the worked narrative uses one continuous Constraint trace;
- [x] runtime evidence and proposed authority changes are not conflated;
- [x] the article does not claim that a complete two-level worked application already exists;
- [x] the platform boundary is precise and non-defensive;
- [x] maturity and validation claims match the roadmap;
- [x] external factual claims have an explicit Phase 2 verification rule;
- [x] exactly three figures have distinct jobs;
- [x] Phase 2 source set and drafting sequence are explicit;
- [ ] the maintainer has reviewed and explicitly frozen the editorial contract for drafting.

Phase 2 article prose should be created in a separate branch and pull request after this blueprint is accepted and PR #31 is merged.
