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
updated: 2026-08-04
language: en
license: CC-BY-4.0
draft: true
---

# Article Blueprint — Uncertainty Architecture: An Open Engineering Specification for Thinking Systems

**Proposed subtitle:** From project viability to delivery realization, runtime evidence, and reauthorization

> **Status:** Accepted Phase 1 editorial contract under active Phase 2 application. This is a non-normative research note, not article prose and not a specification source. Final UA claims must follow repository authority: `SPECIFICATION.md` and explicit status, then the glossary and the owning doctrine, pattern, or capability document. Reference architectures, failure modes, roadmap, and research contribute examples, reusable failure mechanisms, project state, or evidence according to their declared status. Current external factual claims require current primary or authoritative evidence during Phase 2.

## 1. Editorial decision

The article will make one connected argument:

```text
engineering expands around consequential uncertainty it can no longer leave outside its operating model
→ Thinking Systems change the controlled object
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

The opening may use the evolution from plan-driven engineering through iterative delivery and modern operations as a narrow explanatory lens. It must not claim that one methodology replaced another, reduce any movement to one purpose, or use the comparison as evidence of a universal historical law. Its role is to show how engineering expands when an important location of uncertainty can no longer remain outside the engineering model.

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

### 4.1 Engineering Evolves Around Dominant Uncertainty

**Purpose:** Establish the practical missing connection before introducing the full UA anatomy, using the changing location of uncertainty as the explanatory path.

**Core claim:** Planning, iterative delivery, and modern operations can be read as cumulative engineering responses to requirement, product-learning, and production-condition uncertainty. Thinking Systems add consequential runtime-judgment uncertainty inside the controlled object. Existing policies, evaluations, traces, approval steps, and orchestration tools do not become a governable system unless they are connected to authorization, bounded authority, decision ownership, corrective action, and reassessment.

**Required content:**

- Explain the methodology comparison narrowly and cumulatively rather than as replacement history.
- Show how feedback moves closer to runtime as uncertainty becomes harder to contain before implementation.
- Open or transition into a credible team that has a model, retrieval or tools, traces, evaluations, policy, human approval, and a pilot.
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
- State fragmentation as practitioner observation unless current authoritative evidence supports a broader market claim.
- Do not claim that no governance, safety, systems, or control practice exists.

**Repository anchors:**

- [`SPECIFICATION.md`](../../../SPECIFICATION.md)
- [`Uncertainty in the Controlled Object`](../../../00-doctrine/uncertainty-in-the-controlled-object.md)
- [`Failure Modes and Anti-Patterns`](../../../04-failure-modes/README.md)
- [`Designing Non-Deterministic Systems source intake`](designing-nondeterministic-systems-source-intake.md)

**Transition:** The connection is missing because AI is often implemented as an additional component while the implications of the changed engineering object remain distributed across separate decisions and practices.

**Closing claim:**

> The missing layer is not another AI component. It is the engineering connection between delegated judgment, authorized boundaries, evidence, decision authority, corrective action, and reassessment.

**Working word budget:** 700–900. The integrated pass may rebalance this section against Section 4.2 while preserving the total article target.

---

### 4.2 The Controlled Object Has Changed

**Purpose:** Explain the doctrinal reason UA exists and derive the connected decision horizons from the controlled-object shift.

**Core claim:** A Thinking System produces part of its consequential uncertainty inside the engineered object because runtime behavior depends partly on probabilistic Model Judgment. Once that happens, organizational, project, architectural, delivery, and runtime decisions become connected manifestations of one control problem.

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
- State that useful variance is the reason the model is present; the objective is bounded operation rather than elimination of all variance.
- Distinguish product and requirement uncertainty, environment and operational uncertainty, and runtime-judgment uncertainty.
- Explain why the changed object creates connected control questions across organizational context, project viability, architecture, delivery realization and release, and runtime reassessment.
- State that UA complements existing engineering disciplines.

**Primary Figure 1 — Controlled-object shift**

Use a two-panel comparison of responsibility structure, not one mandatory execution path. Show explicitly encoded responsibilities in one panel and a mixed Thinking System with deterministic responsibilities before, between, and after one or more Judgment Nodes in the other.

The figure must not imply that traditional software has no uncertainty, a Thinking System is wholly probabilistic, every system has one Judgment Node, Judgment placement follows one fixed order, every realization acts before a model call, or capability families form a vertical execution sequence.

**Supporting figures permitted in the foundation:**

- engineering responses as uncertainty moves toward runtime;
- functional placement of Model Judgment;
- connected locations of requirement, operational, and runtime-judgment uncertainty;
- one controlled object viewed across four decision horizons.

Supporting figures must strengthen the deduction, introduce no new doctrine, carry explicit non-prescriptive captions, and remain subordinate to the three primary architectural figures.

**Repository anchors:**

- [`Uncertainty in the Controlled Object`](../../../00-doctrine/uncertainty-in-the-controlled-object.md)
- [`Glossary`](../../../00-doctrine/glossary.md)
- [`Model Judgment Placement`](../../../00-doctrine/model-judgment-placement.md)
- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)

**Transition:** Once consequential uncertainty is produced inside the runtime path, quality measurement is necessary but no longer the complete engineering contract.

**Closing claim:**

> The problem is not merely that AI is harder to test. Part of the controlled object's behavior is now produced through runtime judgment, and every decision that controls that object must account for the change.

**Working word budget:** 900–1,200. The integrated pass must reduce duplication with Sections 4.3 and 4.4 and preserve the overall target.

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

**Repository anchors:**

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

**Primary Figure 2 — Two orthogonal UA models**

Show decision ownership with downward inheritance and upward reassessment beside capability functions applying at every level. The figure must not imply one-to-one mapping, four mandatory services, or a one-way waterfall.

#### Organizational control context

**Question owned:** Within which authoritative boundaries, shared capabilities, and decision rights may projects operate?

#### Project control architecture and viability

**Question owned:** Does a credible, operable, and economically viable control architecture exist for this proposed Thinking System within a defined boundary?

#### Delivery-level Thinking System Review

**Question owned:** Is a bounded system, feature, or material change ready, complete, and acceptable for a specific deployment context under project authorization?

Distinguish DoR, DoD, and Release Gate. Delivery may narrow but must not expand project authority or weaken an inherited Hard Constraint.

#### Runtime operation and reassessment

**Question owned:** Does active operation remain within the approved Requirement, Constraint baseline, authority, capacity, and economics, with required realizations active and healthy, and what action follows when it does not?

Evidence routes by the decision basis invalidated: local issues to delivery reassessment; project risk, authority, feasibility, evidence, capacity, or economics changes to project reauthorization; authoritative source, decision-right, or shared-capability changes to organizational review.

**Repository anchors:**

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

The two living reviews are the default proportional path, not a universal sufficiency claim.

**Repository anchors:**

- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
- [`Project Review Template`](../../../01-patterns/project-control-architecture-and-viability-review-template.md)
- [`Thinking System Review Template`](../../../01-patterns/thinking-system-review-template.md)
- [`Judgment Node Boundary`](../../../01-patterns/judgment-node-boundary.md)

**Closing claim:**

> The goal is not to document everything repeatedly. It is to preserve the chain from authoritative source to scoped Constraint, concrete realization, runtime evidence, and corrective decision.

**Word budget:** 400–500

---

### 4.6 One Constraint Across the Full Lifecycle

**Purpose:** Illustrate one continuous project-to-runtime decision path without claiming that the repository already contains a completed two-level worked application.

Use the K-SEND-01 support scenario and preserve the distinction among organizational source, Project Constraint Architecture, delivery Constraint Realization Map, DoR, DoD, Release Gate, runtime evidence, delivery reassessment, project reauthorization, and a separate proposed authority expansion.

**Primary Figure 3 — K-SEND-01 Constraint trace**

Label the figure as an illustrative editorial synthesis, not application evidence.

**Repository anchors:**

- [`Project Control Architecture and Viability Review`](../../../01-patterns/project-control-architecture-and-viability-review.md)
- [`Thinking System Review`](../../../01-patterns/thinking-system-review.md)
- [`Worked Support-Triage Review`](../../../03-reference-architectures/worked-thinking-system-review-support-triage.md)
- [`Constraint Realization Catalog`](../../../02-ai-control-plane/01-constraints/constraint-realization-catalog.md)

**Closing claim:**

> Evidence and proposed authority changes must route according to the decision basis they invalidate or seek to change, not merely according to where they first appear.

**Word budget:** 600–700

---

### 4.7 What Platforms Can Implement — and What Authority They Do Not Acquire by Default

**Purpose:** Address productization without dismissing agent, governance, observability, or AI-native delivery platforms.

**Core claim:** A platform may implement several UA capabilities and records and may exercise explicitly delegated Controller authority, but it does not acquire organizational or project decision authority merely by hosting them.

A platform may execute delegated authority. It does not create that authority.

**Repository anchors:**

- [`Control-Loop Capability Anatomy`](../../../00-doctrine/control-loop-anatomy.md)
- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
- [`AI Control Plane`](../../../02-ai-control-plane/README.md)
- [`Specification`](../../../SPECIFICATION.md)

**Closing claim:**

> A platform can make control capabilities easier to implement and may exercise delegated decision logic. It does not, by default, authorize the project or define the organizational boundary in which that implementation is legitimate.

**Word budget:** 350–400

---

### 4.8 Open Specification: Current State, Limits, and Invitation

**Purpose:** End with an accurate repository state and a serious request for validation rather than a product-style call to action.

**Core claim:** UA has a coherent, inspectable draft specification spine, but independent application evidence remains insufficient for a maturity claim.

The section must state what exists, what remains unproven, why the specification is open, the licensing boundary, and the specific external evidence requested.

**Repository anchors:**

- [`README.md`](../../../README.md)
- [`SPECIFICATION.md`](../../../SPECIFICATION.md)
- [`ROADMAP.md`](../../../ROADMAP.md)
- [`CONTRIBUTING.md`](../../../CONTRIBUTING.md)
- [`Research Track`](../index.md)

**Closing claim:**

> Uncertainty Architecture is coherent enough to be tested, not mature enough to be protected from criticism. The next step is external application, contradictory evidence, and revision.

**Word budget:** 400–500

## 5. Figure contract

The article uses three **primary architectural figures**:

1. **Controlled-object shift** — two-panel comparison of responsibility structure, showing one or more possible Judgment Node placements without prescribing a pipeline.
2. **Two orthogonal UA models** — decision levels with downward inheritance and upward reassessment beside capability families applying at every level.
3. **K-SEND-01 Constraint trace** — illustrative source-to-runtime path with delivery reassessment, project reauthorization, and separate authority expansion.

Additional supporting figures, comparison diagrams, tables, and explanatory visualizations are permitted where they materially strengthen understanding. They must introduce no new doctrine, remain consistent with owning repository sources, carry explicit captions describing scope and non-prescriptive boundaries, avoid implying a mandatory topology or replacement history, and remain subordinate to the three primary figures.

Do not use the presentation's brain/nerves/skeleton/muscles stack as the canonical article architecture diagram. It may be mentioned as source history only.

## 6. Terminology and claim-safety rules

Use current terms: Thinking System, Model Judgment, Judgment Node, Constraint, Constraint Realization, Hard Constraint, Soft Constraint, Sensor, Controller, Actuator, Human Authority, Project Constraint Architecture, Constraint Realization Map, Nested Control Lifecycle, Project Authorization, Project Reauthorization, DoR, DoD, and Release Gate.

Treat Behavioral Software, Behavioral Applications, fixed specialist role titles, universal maturity ladders, universal thresholds, and the old three-part Actuator/Sensor/Controller model as historical or contextual only.

Do not call a prompt, natural-language policy, probabilistic evaluator, classifier, or model preference a Hard Constraint by itself; call a realization a Constraint; let an Actuator define or authorize policy; collapse evaluator, gate decision, and release execution; equate closed feedback with acceptable bounded operation; imply runtime reauthorizes a project automatically; classify every deviation as a Bug; present aggregate quality, cost, latency, or capacity tolerances as Hard Constraints without deterministic enforcement; present K-SEND-01 as independent application evidence; or use internal UA documents as evidence for current external standards, laws, products, or market practice.

## 7. Repository source plan for Phase 2

Framework claims follow `SPECIFICATION.md`, the glossary, and the owning doctrine, pattern, or capability document. Supporting sources may provide informative realization examples, reference applications, failure mechanisms, project state, provenance, and research evidence according to status. Historical articles, talks, presentations, and research must not override authority-bearing framework sources.

Current factual claims about standards, laws, platform capabilities, market practice, or the state of AI governance must be checked against current primary or authoritative sources. Named platform capabilities must be checked against first-party documentation. Comparative claims should be narrow, dated, and should not imply exhaustive market coverage.

## 8. Publication framing and repository path

- **Primary title:** *Uncertainty Architecture: An Open Engineering Specification for Thinking Systems*
- **Subtitle:** *From project viability to delivery realization, runtime evidence, and reauthorization*
- **Target:** approximately 4,300–5,500 English words, subject to one integrated reduction pass after all four drafting blocks.

The Phase 2 draft lives at:

```text
content/research/notes/open-engineering-specification-article-draft.md
```

After editorial acceptance and public release, the normalized repository edition will live at:

```text
content/research/publications/uncertainty-architecture-open-engineering-specification.md
```

Medium and LinkedIn editions are distribution copies and should link back to the repository edition.

## 9. Phase 2 drafting sequence

Draft four connected blocks:

1. abstract, engineering uncertainty, the missing connection, and controlled-object doctrine;
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
- [x] Three primary figures have distinct jobs and introduce no new doctrine.
- [x] Supporting figures are permitted under explicit non-normative boundaries.
- [x] Source authority, external-evidence rules, repository paths, word allocation, and drafting sequence are explicit.
- [x] The maintainer has reviewed and explicitly frozen the editorial contract for Phase 2 drafting.
