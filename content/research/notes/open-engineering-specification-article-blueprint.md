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

# Article Blueprint — Uncertainty Architecture: An Open Engineering Specification for Thinking Systems

**Proposed subtitle:** From project viability to delivery realization, runtime evidence, and reauthorization

> **Status:** Proposed Phase 1 editorial contract. This is a non-normative research note, not article prose and not a specification source. Current UA definitions remain owned by the specification, glossary, doctrine, patterns, AI Control Plane, reference architectures, failure modes, and roadmap. Current external factual claims require current primary or authoritative evidence during Phase 2.

## 1. Editorial decision

The article will make one connected argument:

```text
Thinking Systems change the controlled object
→ model quality and observability alone are insufficient for control
→ bounded operation requires four control-capability families
→ decisions are owned at four connected lifecycle levels
→ authoritative Constraints flow downward by reference while realization becomes concrete
→ runtime evidence returns to the decision level whose basis it invalidates
→ one project review and one delivery review provide the default SMB operating surface
→ one illustrative Constraint trace makes the lifecycle concrete
→ platforms may implement capabilities without acquiring organizational or project authority by default
→ the open specification is coherent enough to test but not mature enough to declare complete
```

The article uses one unnumbered abstract and eight numbered sections.

Two models remain orthogonal throughout:

- **decision levels** identify where a decision is owned;
- **capability families** identify how boundaries, evidence, decisions, and actions become operational.

The article must not map the four levels one-to-one onto the four families, present either model as a mandatory physical stack, or turn the lifecycle into a one-way waterfall.

## 2. Stable thesis and claim boundary

### Stable thesis paragraph

Thinking Systems change the object being engineered because consequential runtime behavior may be produced through probabilistic Model Judgment rather than fully enumerated deterministic logic. Evaluation, observability, policies, human approval, and agent orchestration are useful but remain incomplete when they are not connected to approved Constraints, concrete Constraint Realizations, decision authority, corrective action, and reassessment. Uncertainty Architecture provides an open, tool-neutral specification for connecting those responsibilities across organizational, project, delivery, and runtime decision levels while preserving a lightweight default operating path for small and medium-sized teams.

### Defensible public claim

UA provides a coherent draft specification spine for reasoning about and operating model-mediated systems from project authorization through delivery release and runtime reassessment.

### Claims the article must not make

The article must not describe UA as:

- an accepted industry standard;
- a complete scientific theory;
- independently validated across multiple teams or domains;
- a universal governance or compliance framework;
- a replacement for Agile, DevOps, QA, security, change management, incident response, legal review, or organizational policy;
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
- direct and skeptical of hype without dismissing adjacent disciplines or products;
- precise about evidence, authority, failure, and maturity;
- practical for SMB teams without assuming enterprise governance structure;
- open to contradiction and revision.

### Reader promise

The reader should leave able to explain:

1. why consequential Model Judgment changes the controlled object;
2. the difference between measurement, a closed feedback loop, and a complete bounded UA control architecture;
3. the four capability families and their boundaries;
4. the four decision levels and the question owned by each;
5. how Project Constraint Architecture, delivery Constraint Realization Map, runtime evidence, and reassessment connect;
6. why project authorization, DoR, DoD, Release Gate, runtime correction, and project reauthorization are different decisions;
7. how a small team can use the model without creating parallel governance bureaucracy;
8. what platforms may implement and what authority they do not acquire automatically;
9. what exists in the repository and what remains unvalidated.

## 4. Article structure

### Unnumbered abstract

**Purpose:** State the complete argument and maturity boundary without teaching the framework in miniature.

**Required content:**

- Thinking Systems place consequential probabilistic Model Judgment inside the controlled object.
- Model quality, evaluation, observability, policy, and human approval remain incomplete when disconnected from approved boundaries, decision authority, corrective action, and reassessment.
- UA connects four capability families across four decision levels.
- The default SMB operating surface uses one project review and one delivery review rather than a new governance bureaucracy.
- The specification is coherent enough for external application and criticism but lacks sufficient independent evidence for a maturity claim.

**Exclude:** the complete taxonomy, the K-SEND-01 scenario, market statistics, named products, and promotional calls to action.

**Word budget:** 200–250

---

### 4.1 The Missing Engineering Connection

**Purpose:** Establish the practical gap before introducing UA terminology.

**Core claim:** The ecosystem offers many relevant components, but policies, evaluations, traces, approval steps, and orchestration tools do not become a governable system unless they are connected to authorization, bounded authority, decision ownership, corrective action, and reassessment.

**Required content:**

- Open with a credible team that has a model, retrieval or tools, traces, evaluations, policy, human approval, and a pilot.
- Ask the connected questions the components alone do not answer:
  - Was Model Judgment necessary?
  - What authority was delegated?
  - Which consequences are prohibited or unacceptable?
  - Which Constraints are authoritative?
  - How are they realized?
  - Which evidence informs which decision?
  - Who may narrow, roll back, disable, redesign, or stop operation?
  - When does runtime evidence invalidate project authorization?
  - Does the business case survive the complete control cost?
- State the market observation narrowly: practices may remain fragmented by product boundary, decision level, or organizational function.
- Support factual claims about current industry practice with current primary or authoritative sources. When evidence is unavailable, label the point as practitioner observation rather than established market fact.
- Do not claim that no governance, safety, systems, or control practice exists.

**Canonical anchors:**

- [`SPECIFICATION.md`](../../../SPECIFICATION.md)
- [`Uncertainty in the Controlled Object`](../../../00-doctrine/uncertainty-in-the-controlled-object.md)
- [`Failure Modes and Anti-Patterns`](../../../04-failure-modes/README.md)

**Transition:** The connection is missing because AI is still often treated as an additional component inside an otherwise unchanged engineering object.

**Closing claim:**

> The missing layer is not another AI component. It is the engineering connection between delegated judgment, authorized boundaries, evidence, decision authority, and corrective action.

**Word budget:** 400–500

---

### 4.2 The Controlled Object Has Changed

**Purpose:** Explain the doctrinal reason UA exists.

**Core claim:** A Thinking System produces part of its consequential uncertainty inside the engineered object because runtime behavior depends partly on probabilistic Model Judgment.

**Required content:**

- Use determinism as a design-contract distinction, not a claim of perfect repeatability:

  ```text
  y = f(x)
  ```

- Describe model-mediated responsibility as selection from plausible outcomes under input, context, model, configuration, state, and operating conditions:

  ```text
  y ~ P(y | x, context, model configuration, system state)
  ```

- Explain Model Judgment through interpretation, classification, ranking, planning, generation, routing, or action selection.
- State that useful variance is the reason the model is present; the objective is containment rather than elimination of all variance.
- Distinguish product and requirement uncertainty, environment and operational uncertainty, and runtime-judgment uncertainty.
- State that UA complements existing engineering disciplines.

**Figure 1 — Controlled-object shift**

Use a two-panel composition.

```text
Panel A — Primarily explicit runtime behavior
external, requirement, delivery, and operational uncertainty
→ explicitly encoded runtime responsibilities

Panel B — Thinking System
external, requirement, delivery, and operational uncertainty
→ deterministic ingress and responsibilities
→ bounded Model Judgment
→ deterministic output/action mediation
→ observed outputs, actions, and downstream outcomes
```

Around the Model Judgment region, show approved Constraints and realizations, Sensors and evidence, Controller authority, and Actuator paths.

The figure must not imply that:

- traditional software has no uncertainty;
- a Thinking System is wholly probabilistic;
- every realization acts before the model;
- the capability families form a vertical execution sequence.

**Canonical anchors:**

- [`Uncertainty in the Controlled Object`](../../../00-doctrine/uncertainty-in-the-controlled-object.md)
- [`Glossary`](../../../00-doctrine/glossary.md)
- [`Model Judgment Placement`](../../../00-doctrine/model-judgment-placement.md)

**Transition:** Once consequential uncertainty is produced inside the runtime path, quality measurement is necessary but no longer the complete engineering contract.

**Closing claim:**

> The problem is not merely that AI is harder to test. Part of the controlled object's behavior is now produced through runtime judgment.

**Word budget:** 450–550

---

### 4.3 From Model Quality to Bounded Control

**Purpose:** Introduce the accepted Control-Loop Capability Anatomy and distinguish feedback closure from bounded acceptable operation.

**Core claim:** A measured system is not necessarily controlled, and a closed feedback loop is not necessarily operating inside an approved boundary.

**Required content:**

- Use the canonical feedback path:

  ```text
  Thinking System
  → Sensors and evidence
  → Controller and decision authority
  → Actuators and corrective action
  → changed Thinking System operation
  ```

- Explain why the loop may remain closed while unsafe, over-authorized, or economically unacceptable.
- Introduce the four logical capability families:
  1. **Constraints and their realizations** define and operationalize approved boundaries.
  2. **Sensors and evidence** observe behavior, outcomes, conditions, realization state, Actuator execution, and control health.
  3. **Controllers and decision authority** compare or interpret evidence relative to approved Requirements, Constraints, and assumptions, then select or authorize action.
  4. **Actuators and corrective action** execute authorized changes to operation or a Constraint Realization.
- Preserve the functional distinctions:
  - Constraint is the authoritative boundary object.
  - Constraint Realization implements, enforces, or influences it.
  - Constraint Realization is not a fifth family.
  - Controller decides or authorizes; Actuator executes.
  - evaluator and metrics normally perform Sensor functions;
  - logic selecting `block`, `canary`, or `release` performs a Controller function;
  - deployment, blocking, exposure change, or rollback performs an Actuator function.
- Explain scoped Hard and Soft claims:
  - a Hard Constraint's complete realized path deterministically prevents or rejects violation within stated assumptions, subject, path, scope, and enforcement boundaries;
  - prompts, natural-language policies, probabilistic evaluators, and model preferences are not hard by themselves;
  - different guarantee strengths require separate Constraint records.
- Use short anti-examples: telemetry without authority is observation; a Controller without an effective Actuator cannot correct; a declared policy without realization is not an operable boundary; nominal human review is not substantive Human Authority.

**Canonical anchors:**

- [`Control-Loop Capability Anatomy`](../../../00-doctrine/control-loop-anatomy.md)
- [`AI Control Plane`](../../../02-ai-control-plane/README.md)
- [`Constraint Capability Family`](../../../02-ai-control-plane/01-constraints/README.md)
- [`Constraint Realization Catalog`](../../../02-ai-control-plane/01-constraints/constraint-realization-catalog.md)
- [`Actuator Capabilities`](../../../02-ai-control-plane/00-actuators/README.md)
- [`Sensor and Evidence Capabilities`](../../../02-ai-control-plane/02-sensors/README.md)
- [`Controller and Decision Authority`](../../../02-ai-control-plane/03-controller/README.md)

**Transition:** The capability anatomy explains how control works, but not where project, release, runtime, and organizational decisions are owned.

**Closing claim:**

> A closed loop can still be unacceptable. UA asks whether that loop operates inside an approved, credibly realized, observable, and correctable boundary.

**Word budget:** 550–600

---

### 4.4 Four Decision Levels of Uncertainty Architecture

**Purpose:** Present the Nested Control Lifecycle as the conceptual center.

**Core claim:** Different control decisions require different evidence, authority, time horizons, and corrective actions; they must remain connected without collapsing into one gate or governance process.

**Figure 2 — Two orthogonal UA models**

Show two adjacent views.

```text
Decision ownership
Organization
→ Project / architecture
→ Delivery team
→ Runtime operation and reassessment
↖ evidence returns to the decision basis it invalidates

Capability functions at every level
Constraints and realizations
Sensors and evidence
Controllers and decision authority
Actuators and corrective action
```

The figure must show downward inheritance and upward reassessment and must not imply one-to-one mapping, four mandatory services, or a one-way waterfall.

#### Organizational control context

**Question owned:** Within which authoritative boundaries, shared capabilities, and decision rights may projects operate?

- Link existing legal, contractual, security, privacy, safety, procurement, vendor, geography, prohibited-use, incident, and decision-right sources.
- Do not create a mandatory UA organizational artifact or governance department.
- Organizational sources do not become Hard Constraints merely because they are authoritative; realization and scoped guarantee still matter.

#### Project control architecture and viability

**Question owned:** Does a credible, operable, and economically viable control architecture exist for this proposed Thinking System within a defined boundary?

The project review owns outcome and AI necessity, project boundary, material scenarios, Project Constraint Architecture, required capabilities and assumptions, evidence feasibility, Human Authority, capacity, control economics, authorization, inheritance, and project reauthorization.

A successful prototype is not project authorization. Architectural Veto is a valid engineering outcome.

#### Delivery-level Thinking System Review

**Question owned:** Is a bounded system, feature, or material change ready, complete, and acceptable for a specific deployment context under project authorization?

The delivery review owns implementation-level Judgment Nodes, the delivery Requirement and Operating Envelope, one Constraint Realization Map, DoR, implementation or bounded experiment, DoD, Release Gate, and local reassessment.

Distinguish:

- DoR establishes readiness and the authority basis for bounded work;
- DoD establishes implementation and evidence completeness;
- Release Gate accepts, limits, conditions, escalates, or rejects a deployment.

Delivery may narrow but must not expand project authority or weaken an inherited Hard Constraint.

#### Runtime operation and reassessment

**Question owned:** Does active operation remain within the approved Requirement, Constraint baseline, authority, capacity, and economics, with required realizations active and healthy, and what action follows when it does not?

Runtime exercises deployed realizations and produces evidence about behavior, outcomes, realization state, violations, bypass, degradation, Actuator execution, Human Authority, fallback capacity, and project or organizational assumptions.

Evidence routes by the decision basis invalidated:

```text
local implementation, realization, configuration, or evidence issue
→ delivery reassessment

project risk, authority, feasibility, evidence, capacity, or economics changed
→ project reauthorization

authoritative source, decision right, or shared capability changed
→ organizational review
```

**Canonical anchors:**

- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
- [`Project Control Architecture and Viability Review`](../../../01-patterns/project-control-architecture-and-viability-review.md)
- [`Thinking System Review`](../../../01-patterns/thinking-system-review.md)

**Transition:** The lifecycle becomes practical only when authoritative decisions are inherited rather than recopied and when runtime evidence can be traced back to the decision it challenges.

**Closing claim:**

> Lower levels may refine and narrow a higher-level decision. They may not silently expand its authority or normalize evidence that invalidates it.

**Word budget:** 950–1,150

---

### 4.5 From Authority to Operation: Two Living Reviews

**Purpose:** Explain inheritance, realization, evidence routing, and the default SMB operating surface without reproducing the templates.

**Core claim:** UA reduces duplication by preserving one project Constraint artifact and one delivery realization artifact, linked to existing organizational sources and runtime evidence.

**Canonical path:**

```text
existing organizational sources, shared capabilities, and decision rights
→ one living Project Control Architecture and Viability Review
→ one versioned Project Constraint Architecture and authorization
→ one living Thinking System Review per bounded delivery scope
→ one canonical Constraint Realization Map
→ deployment-specific Release Gate
→ active runtime versions, evidence, decisions, and actions
→ delivery reassessment, project reauthorization, or organizational review
```

**Required content:**

- Constraint authority flows downward by reference; policy prose is not copied as if it were a complete technical control.
- Project-level Constraints are interpreted or derived, scoped, connected to required realization, assumptions, evidence, authority, economics, inheritance, and reauthorization.
- Delivery makes realization concrete through active mechanisms, configuration, verification, failure behavior, evidence, change authority, and release scope.
- Runtime preserves material source, project, delivery, realization, model, prompt, policy, tool, and deployment versions.
- Judgment Nodes, DoR, DoD, Release Gate, and runtime sections reference the same Constraint Realization Map rather than creating parallel records.
- Additional registers, RACIs, gate files, financial models, or committees remain optional when independent ownership, lifecycle, access, retention, regulation, or audit needs justify them.
- Two living reviews are the default proportional path, not a universal sufficiency claim.
- One person may carry several responsibility bundles without collapsing the decisions.

**Canonical anchors:**

- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
- [`Project Review Template`](../../../01-patterns/project-control-architecture-and-viability-review-template.md)
- [`Thinking System Review Template`](../../../01-patterns/thinking-system-review-template.md)
- [`Judgment Node Boundary`](../../../01-patterns/judgment-node-boundary.md)

**Transition:** An illustrative Constraint trace can make the consequences concrete without pretending that the repository already contains evidence for a complete two-level application.

**Closing claim:**

> The goal is not to document everything repeatedly. It is to preserve the chain from authoritative source to scoped Constraint, concrete realization, runtime evidence, and corrective decision.

**Word budget:** 400–500

---

### 4.6 One Constraint Across the Full Lifecycle

**Purpose:** Illustrate one continuous project-to-runtime decision path without claiming that the repository already contains a completed two-level worked application.

**Evidence boundary:** The narrative is an editorial synthesis using the project pattern, Constraint capability, and the illustrative delivery review for support triage. It illustrates specification behavior; it is not independent application evidence.

**Scenario:** A company wants a Thinking System to interpret English-language Product A support tickets, recommend routing, and draft grounded replies for trained support agents.

**Constraint statement:**

> The model-mediated support path may create a draft but must not invoke or execute outbound customer communication. Sending remains reserved to an authorized human-operated path after review.

#### Organizational source

- Autonomous customer communication is prohibited for the initial use case.
- Outbound communication remains reserved to Human Authority.
- Existing identity, authorization, audit, incident, and shutdown capabilities are authoritative dependencies.
- An organizational exception would be required before autonomous sending could be considered.

#### Project Constraint Architecture

```text
Constraint ID: K-SEND-01
Intent: preserve human authority over outbound customer communication
Source/rationale: organizational prohibited-use and customer-commitment boundary
Subject: outbound customer-communication send authority
Path: every model-mediated tool, API, workflow, and alternate path that could reach a send action
Scope: English-language Product A support within the authorized initial population
Class: Human Authority
Claimed strength: Hard, within stated assumptions
Required realization: model-path identity has no send permission; only an authorized human-operated path may send after review
Assumptions: credentials remain isolated; all reachable send paths are known; no alternate endpoint bypasses the boundary; active permission state is verified
Failure behavior: fail closed; preserve draft; route to manual handling; disable the feature when authorization state is unknown
Evidence: negative permission tests, denied-send events, active permission/configuration versions, approved human-send attribution, alternate-path and bypass tests
Change authority: delivery may repair or roll back inside the baseline; autonomous sending requires project reauthorization and organizational review
```

The project may authorize bounded delivery only when the complete realization, evidence, Human Authority capacity, fallback, and control economics are credible.

#### Delivery Constraint Realization Map

Map `K-SEND-01` to:

- a service identity with no outbound-send permission;
- a deterministic authorization boundary covering every reachable send path in scope;
- a draft queue visible to trained support agents;
- an authorized human-operated send path separated from Model Judgment;
- auditable linkage among draft, reviewer decision, and send event;
- fail-closed behavior when permission or approval state is unavailable;
- negative-authority, alternate-path, bypass, and configuration-drift tests;
- runtime evidence and rollback/disable Actuators.

Every Judgment Node references `K-SEND-01`; node cards do not redefine it.

#### DoR, DoD, and Release Gate

- **DoR:** inherited Constraint and scope, Judgment Nodes, complete realization design, assumptions, evidence, Human Authority, fallback, and bounded experiment are explicit.
- **DoD:** every reachable send path in the reviewed scope is covered; no alternate path bypasses the realization; unavailable behavior and bypass are tested; evidence and Actuators are operational.
- **Release Gate:** active realization versions, reviewer capacity, deployment population, residual risk, and rollback/disable readiness are acceptable for limited release.

#### Runtime evidence and change routing

1. **Local realization defect** — a configuration mismatch is detected before an unauthorized send path becomes reachable. Delivery fails closed, repairs the realization, verifies the complete path, and passes a new Release Gate.
2. **Project assumption invalidated** — review volume and latency make the control perimeter economically non-viable at planned scale. `K-SEND-01` remains valid, but project capacity and economics do not. Project reauthorization narrows, redesigns, defers, or rejects the path.
3. **Separate authority-change request** — the business requests autonomous sending. This is not runtime evidence or delivery tuning. It requires project reauthorization and organizational review before any new realization is designed.

**Figure 3 — K-SEND-01 Constraint trace**

```text
organizational prohibition and reserved Human Authority
→ Project Constraint K-SEND-01
→ delivery Constraint Realization Map
→ runtime evidence
   ├─ local defect → delivery reassessment
   └─ capacity/economics invalidated → project reauthorization

separate proposed authority expansion
→ project reauthorization + organizational review
```

Label the figure as an illustrative editorial synthesis, not application evidence.

**Canonical anchors:**

- [`Project Control Architecture and Viability Review`](../../../01-patterns/project-control-architecture-and-viability-review.md)
- [`Thinking System Review`](../../../01-patterns/thinking-system-review.md)
- [`Worked Support-Triage Review`](../../../03-reference-architectures/worked-thinking-system-review-support-triage.md)
- [`Constraint Realization Catalog`](../../../02-ai-control-plane/01-constraints/constraint-realization-catalog.md)

**Transition:** The example separates the decision architecture from the tools that may implement it, making the platform boundary precise.

**Closing claim:**

> Evidence and proposed authority changes must route according to the decision basis they invalidate or seek to change, not merely according to where they first appear.

**Word budget:** 600–700

---

### 4.7 What Platforms Can Implement — and What Authority They Do Not Acquire by Default

**Purpose:** Address productization without dismissing agent, governance, observability, or AI-native delivery platforms.

**Core claim:** A platform may implement several UA capabilities and records and may exercise explicitly delegated Controller authority, but it does not acquire organizational or project decision authority merely by hosting them.

**Required content:**

- Classify platform functions by what they do in the specific system, not by market category.
- A platform may host or implement Constraint Realizations, Sensors and evidence, bounded automated Controller logic, human decision interfaces, Actuators, version records, and decision records.
- A platform does not independently determine whether Model Judgment is necessary, which source is authoritative, what consequences or authority are acceptable, who may accept residual risk, whether Human Authority is substantive, whether the control perimeter preserves viability, or when project or organizational authorization must change.
- A platform may execute delegated authority. It does not create that authority.
- Avoid the categorical claim that platforms “cannot solve governance.” State the narrower ownership and delegation boundary.
- Verify named-platform claims against current first-party documentation. Prefer functional, vendor-neutral framing when a named comparison is unnecessary.

**Canonical anchors:**

- [`Control-Loop Capability Anatomy`](../../../00-doctrine/control-loop-anatomy.md)
- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
- [`AI Control Plane`](../../../02-ai-control-plane/README.md)
- [`Specification`](../../../SPECIFICATION.md)

**Transition:** This separation is why UA is developed as an open specification rather than one privileged implementation.

**Closing claim:**

> A platform can make control capabilities easier to implement and may exercise delegated decision logic. It does not, by default, authorize the project or define the organizational boundary in which that implementation is legitimate.

**Word budget:** 350–400

---

### 4.8 Open Specification: Current State, Limits, and Invitation

**Purpose:** End with an accurate repository state and a serious request for validation rather than a product-style call to action.

**Core claim:** UA has a coherent, inspectable draft specification spine, but independent application evidence remains insufficient for a maturity claim.

**What exists:**

- controlled-object doctrine and canonical glossary;
- Control-Loop Capability Anatomy and Nested Control Lifecycle;
- Requirement, Correctness, Bug, and Model Judgment Placement doctrine;
- Judgment Node Boundary;
- project and delivery reviews with informative templates;
- Constraint capability and realization catalog;
- Sensors, Controllers, and Actuators guidance;
- placement-focused reference architectures;
- one illustrative delivery-level support-triage review;
- failure-mode taxonomy;
- research provenance and framework traceability.

**What does not yet exist or remains unproven:**

- a complete repository-level two-level project-and-delivery worked application;
- independent real-team use across multiple organizations;
- evidence that two living reviews are sufficient in every context;
- validated usability, time-to-complete, and decision-quality evidence;
- mature control-cost and Human Authority capacity methods;
- validated incident and drift patterns across domains;
- universal threshold derivation;
- proof that teams can apply UA correctly without author involvement;
- evidence that current terminology and boundaries will survive sustained external use unchanged.

**Why open:** enable independent critique and contradictory evidence, compare application across domains, prevent vendor or author capture of the control language, preserve visible evolution, and support many implementations.

**Licensing:** documentation and specification material use CC BY 4.0; code and reference implementations use Apache 2.0 where present.

**Validation request:** ask for documented applications, anonymized reviews, contradictory cases, terminology issues, simplification proposals, platform mappings, control-cost evidence, Human Authority failures, and operational failure modes.

**Canonical anchors:**

- [`README.md`](../../../README.md)
- [`SPECIFICATION.md`](../../../SPECIFICATION.md)
- [`ROADMAP.md`](../../../ROADMAP.md)
- [`CONTRIBUTING.md`](../../../CONTRIBUTING.md)
- [`Research Track`](../index.md)

**Closing claim:**

> Uncertainty Architecture is coherent enough to be tested, not mature enough to be protected from criticism. The next step is external application, contradictory evidence, and revision.

**Word budget:** 400–500

## 5. Figure contract

Use exactly three primary figures:

1. **Controlled-object shift** — two-panel explicit-behavior versus bounded Model Judgment view.
2. **Two orthogonal UA models** — decision levels with downward inheritance and upward reassessment beside capability families applying at every level.
3. **K-SEND-01 Constraint trace** — illustrative source-to-runtime path with delivery reassessment, project reauthorization, and separate authority expansion.

Do not use the presentation's brain/nerves/skeleton/muscles stack as the canonical article architecture diagram. It may be mentioned as source history only.

## 6. Terminology and claim-safety rules

Use current terms: Thinking System, Model Judgment, Judgment Node, Constraint, Constraint Realization, Hard Constraint, Soft Constraint, Sensor, Controller, Actuator, Human Authority, Project Constraint Architecture, Constraint Realization Map, Nested Control Lifecycle, Project Authorization, Project Reauthorization, DoR, DoD, and Release Gate.

Treat Behavioral Software, Behavioral Applications, fixed specialist role titles, universal maturity ladders, universal thresholds, and the old three-part Actuator/Sensor/Controller model as historical or contextual only.

Do not:

- call a prompt, natural-language policy, probabilistic evaluator, classifier, or model preference a Hard Constraint by itself;
- call a schema or permission check a Constraint without distinguishing the authoritative Constraint from its realization;
- describe Actuators as defining policy or authorizing their own changes;
- collapse evaluator, gate decision, and release execution;
- equate closed feedback with acceptable bounded operation;
- imply runtime reauthorizes a project automatically;
- classify every deviation as a Bug;
- describe aggregate quality, cost, latency, or capacity tolerances as Hard Constraints without deterministic enforcement;
- present the illustrative K-SEND-01 trace as independent application evidence;
- use internal UA documents as evidence for current external standards, laws, products, or market practice.

## 7. Source plan for Phase 2

### Canonical UA sources

1. [`SPECIFICATION.md`](../../../SPECIFICATION.md)
2. [`Glossary`](../../../00-doctrine/glossary.md)
3. [`Uncertainty in the Controlled Object`](../../../00-doctrine/uncertainty-in-the-controlled-object.md)
4. [`Control-Loop Capability Anatomy`](../../../00-doctrine/control-loop-anatomy.md)
5. [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
6. [`Requirements, Correctness, and Bugs`](../../../00-doctrine/requirements-correctness-and-bugs.md)
7. [`Model Judgment Placement`](../../../00-doctrine/model-judgment-placement.md)
8. [`Project Control Architecture and Viability Review`](../../../01-patterns/project-control-architecture-and-viability-review.md)
9. [`Thinking System Review`](../../../01-patterns/thinking-system-review.md)
10. [`Judgment Node Boundary`](../../../01-patterns/judgment-node-boundary.md)
11. [`AI Control Plane`](../../../02-ai-control-plane/README.md)
12. [`Actuator Capabilities`](../../../02-ai-control-plane/00-actuators/README.md)
13. [`Constraint Capability Family`](../../../02-ai-control-plane/01-constraints/README.md)
14. [`Constraint Realization Catalog`](../../../02-ai-control-plane/01-constraints/constraint-realization-catalog.md)
15. [`Sensor and Evidence Capabilities`](../../../02-ai-control-plane/02-sensors/README.md)
16. [`Controller and Decision Authority`](../../../02-ai-control-plane/03-controller/README.md)
17. [`Worked Support-Triage Review`](../../../03-reference-architectures/worked-thinking-system-review-support-triage.md)
18. [`Failure Modes and Anti-Patterns`](../../../04-failure-modes/README.md)
19. [`ROADMAP.md`](../../../ROADMAP.md)

Historical articles, talks, and presentation material may provide provenance and explanatory language. They must not override current framework definitions.

### External evidence

Current factual claims about standards, laws, platform capabilities, market practice, or the state of AI governance must be checked against current primary or authoritative sources. Named platform capabilities must be checked against first-party documentation. Comparative claims should be narrow, dated, and should not imply exhaustive market coverage.

## 8. Publication framing and repository path

### Title and length

- **Primary title:** *Uncertainty Architecture: An Open Engineering Specification for Thinking Systems*
- **Subtitle:** *From project viability to delivery realization, runtime evidence, and reauthorization*
- **Target:** 4,300–5,200 English words

| Part | Words |
|---|---:|
| Abstract | 200–250 |
| Missing Engineering Connection | 400–500 |
| Controlled Object | 450–550 |
| Bounded Control | 550–600 |
| Four Decision Levels | 950–1,150 |
| Two Living Reviews | 400–500 |
| One Constraint Trace | 600–700 |
| Platform Boundary | 350–400 |
| State, Limits, Invitation | 400–500 |

The ranges total 4,300–5,150 words.

### Phase 2 draft

Create article prose in a separate branch and pull request at:

```text
content/research/notes/open-engineering-specification-article-draft.md
```

Use `status: research`, `maturity: draft`, and `draft: true`.

### Published repository edition

After editorial acceptance and public release, create or move the normalized repository edition to:

```text
content/research/publications/uncertainty-architecture-open-engineering-specification.md
```

Update the research publications index and the relevant history record. Medium and LinkedIn editions are distribution copies and should link back to the repository edition.

## 9. Phase 2 drafting sequence

Draft four connected blocks:

1. abstract, problem, and controlled-object doctrine;
2. bounded control and decision levels;
3. two reviews and the K-SEND-01 trace;
4. platform boundary, current state, limits, openness, and invitation.

Then perform one integrated pass for terminology, duplication, source support, links, figure placement, decision-level ownership, capability boundaries, Hard/Soft claims, project-versus-delivery authority, evidence-versus-authority changes, illustrative-versus-application evidence, maturity claims, and final word count.

## 10. Phase 1 acceptance criteria

- [x] One stable thesis paragraph exists.
- [x] The abstract and eight numbered sections have distinct functions.
- [x] Every non-final section creates the need for the next.
- [x] Decision levels and capability families remain orthogonal.
- [x] Constraint and Constraint Realization remain distinct.
- [x] Project authorization, DoR, DoD, Release Gate, runtime correction, and project reauthorization remain separate.
- [x] Project Constraint Architecture and Constraint Realization Map remain the two canonical Constraint artifacts.
- [x] The SMB two-review model is proportional and non-universal.
- [x] K-SEND-01 is explicitly illustrative and has a scoped complete-path Hard claim.
- [x] Runtime evidence and proposed authority changes are not conflated.
- [x] The platform boundary allows delegated Controller authority without automatic organizational or project authority.
- [x] Three figures have distinct jobs and introduce no new doctrine.
- [x] Source plan, external-evidence rule, repository paths, word allocation, and drafting sequence are explicit.
- [ ] The maintainer has reviewed and explicitly frozen the editorial contract.

Phase 2 must begin in a separate branch and pull request after PR #31 is accepted and merged.
