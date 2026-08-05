---
title: "Article Blueprint — Uncertainty Architecture: Engineering Thinking Systems That Produce Consequential Judgment"
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
updated: 2026-08-05
language: en
license: CC-BY-4.0
draft: true
---

# Article Blueprint — Uncertainty Architecture: Engineering Thinking Systems That Produce Consequential Judgment

> **Status:** Living editorial design document for the article. This is a non-normative research note, not article prose and not a specification source. It preserves the complete argument, section responsibilities, claim boundaries, figures, transitions, source plan, writing notes, and unresolved editorial decisions. It must evolve after every drafting iteration and must not be compressed into a checklist merely because publication prose exists.

## 1. Editorial decision

The public article uses **Thinking Systems** as the engineering category through which the problem is developed. It does not begin by presenting Uncertainty Architecture as the premise that validates the argument.

The article first:

1. defines Thinking Systems;
2. distinguishes them from agentic applications;
3. explains why consequential probabilistic Model Judgment changes the controlled object;
4. derives the required control capabilities and decision levels;
5. makes the model practical through two living reviews and one continuous Constraint trace;
6. separates platform implementation from organizational and project authority;
7. introduces **Uncertainty Architecture** near the end as the open specification that organizes the derived model.

The connected argument is:

```text
engineering expands around consequential uncertainty it can no longer leave outside its operating model
→ Thinking Systems place probabilistic Model Judgment inside the controlled object
→ Thinking Systems are not synonymous with agentic applications
→ useful runtime variance changes the engineering contract rather than merely making testing harder
→ model quality and observability are necessary but insufficient
→ bounded operation requires four control-capability families
→ different decisions are owned at four connected lifecycle levels
→ authoritative Constraints flow downward by reference while realization becomes concrete
→ runtime evidence returns to the decision level whose basis it invalidates
→ one project review and one delivery review provide a proportional SMB operating surface
→ one illustrative Constraint trace makes the lifecycle concrete
→ platforms may implement capabilities without acquiring organizational or project authority by default
→ Uncertainty Architecture is introduced as the open specification that connects the resulting model
→ the specification is coherent enough to test but not mature enough to declare complete
```

The article uses one unnumbered abstract and eight numbered sections.

Two models remain orthogonal throughout:

- **decision levels** identify where a decision is owned;
- **capability families** identify how boundaries, evidence, decisions, and actions become operational.

The article must not map the four levels one-to-one onto the four families, present either model as a mandatory physical stack, or turn the lifecycle into a one-way waterfall.

The opening may use the evolution from plan-driven engineering through iterative delivery and modern operations as a narrow explanatory lens. It must not claim that one methodology replaced another, reduce any movement to one purpose, or use the comparison as evidence of a universal historical law. Its role is to show how engineering expands when an important location of uncertainty can no longer remain outside the engineering model.

## 2. Two-document drafting model

This article is developed through two living documents with different responsibilities.

### 2.1 Editorial blueprint

This file is the design document for the article. It owns:

- the end-to-end argument;
- detailed section purpose and sequence;
- stable and provisional claims;
- required distinctions, examples, anti-examples, and counterarguments;
- figure contracts;
- transitions and closing claims;
- repository anchors and external-evidence expectations;
- exclusions, maturity boundaries, rejected formulations, and known risks;
- durable reasoning discovered during drafting.

The blueprint is not replaced by prose. Drafting should make it more precise. Detailed section content must not be replaced with one-line reminders after the section has been written.

### 2.2 Target manuscript

The publication-facing manuscript lives at:

```text
content/research/notes/open-engineering-specification-article-draft.md
```

It owns article prose, figures, examples, and the continuous reader experience. Internal drafting rules, contributor instructions, PR workflow, and editorial acceptance checklists do not belong in the article body.

### 2.3 Mandatory iteration loop

Every substantial drafting iteration follows this order:

```text
read the complete blueprint
→ select the next coherent section block
→ read the complete target manuscript
→ inspect terminology, claims, transitions, examples, and figures already established
→ design the new sections as a continuation of the existing argument
→ write and integrate prose, Mermaid diagrams, tables, and examples
→ reread the complete manuscript, not only the new diff
→ repair contradictions, repetition, weak transitions, title drift, figure numbering, and premature framework promotion
→ return to the blueprint
→ update its section design, writing notes, rejected formulations, figures, source needs, and unresolved risks
```

An iteration is incomplete until both documents are reconciled.

### 2.4 Cumulative argument rule

Every new section must be written from:

1. this complete blueprint;
2. every previously accepted article section;
3. terminology and distinctions already introduced;
4. the logical need created by the preceding section;
5. the repository sources that own the relevant meaning.

Later prose must extend the argument rather than restart the framework explanation. When drafting reveals a weakness in an earlier section, revise the earlier manuscript prose and then update this blueprint accordingly.

### 2.5 Diagram rule

Every major argument and every decision level should have an architectural or process representation when a diagram adds information.

Diagrams are part of the reasoning, not decoration. They must:

- make the controlled object, boundary, evidence, authority, action, or reassessment path clearer;
- introduce no doctrine absent from owning repository sources;
- state non-prescriptive boundaries in captions;
- avoid implying mandatory products, services, teams, departments, committees, roles, or execution pipelines;
- remain consistent with all earlier figures;
- be reviewed and renumbered as one visual system after every iteration.

The article has three primary architectural figures and may contain any number of supporting figures that materially strengthen the deduction.

## 3. Stable thesis and claim boundary

### Stable thesis paragraph

Thinking Systems are software systems whose runtime behavior depends partly on probabilistic Model Judgment while consequential deterministic responsibilities, Constraints, decision rights, evidence, and corrective mechanisms remain explicit. Because useful runtime judgment places consequential uncertainty inside the controlled object, evaluation, observability, policies, human approval, and agent orchestration remain incomplete when disconnected from approved boundaries, concrete realizations, decision authority, corrective action, and reassessment. The article derives the resulting engineering model first and introduces Uncertainty Architecture near the end as an open, tool-neutral specification connecting those responsibilities across organizational, project, delivery, and runtime decision levels.

### Thinking Systems definition

Use the canonical glossary definition:

> A software system whose runtime behavior depends partly on probabilistic Model Judgment while consequential deterministic responsibilities, Constraints, decision rights, evidence, and corrective mechanisms remain explicit.

Preserve the following category boundary:

- agentic systems are a higher-autonomy subset of Thinking Systems, not the entire category;
- a non-agentic feature may be a Thinking System when probabilistic judgment materially affects interpretation, routing, decisions, outputs, or downstream action;
- an application may use agents while remaining largely linear where relevant routes, decisions, and authority are explicitly encoded;
- autonomy and probabilistic Model Judgment are related dimensions, not synonyms;
- a Thinking System remains a mixed deterministic and probabilistic system.

### Defensible public claim

The paper proposes a coherent engineering model for reasoning about and operating Thinking Systems from organizational authority and project viability through delivery release and runtime reassessment, and identifies Uncertainty Architecture as the open draft specification in which that model is being developed.

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

The article must not present the early engineering deduction as proof that UA is uniquely correct. UA is the proposed open specification that organizes the result, not evidence for its own claims.

## 4. Audience, tone, and reader promise

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

1. what a Thinking System is and why the category is not equivalent to agentic software;
2. why consequential Model Judgment changes the controlled object;
3. the difference between measurement, a closed feedback loop, and bounded acceptable operation;
4. the four capability families and their boundaries;
5. the four decision levels and the question owned by each;
6. how organizational authority, Project Constraint Architecture, delivery Constraint Realization Map, runtime evidence, and reassessment connect;
7. why Project Authorization, DoR, DoD, Release Gate, runtime correction, and Project Reauthorization are different decisions;
8. how a small team can use the model without creating parallel governance bureaucracy;
9. what platforms may implement and what authority they do not acquire automatically;
10. what Uncertainty Architecture contributes, what exists in the repository, and what remains unvalidated.

## 5. Article structure

### Unnumbered abstract

**Purpose:** Introduce Thinking Systems, establish the controlled-object shift, summarize the derived engineering problem, and signal that UA will be introduced only after the argument is built.

**Required content:**

- software engineering expands when important uncertainty can no longer remain outside its operating model;
- the canonical Thinking Systems definition;
- explicit distinction from agentic software;
- consequential probabilistic Model Judgment enters the controlled object;
- model quality and observability are insufficient when disconnected from boundaries, authority, corrective action, and reassessment;
- the paper derives control capabilities and decision levels before presenting UA;
- UA appears as an open specification near the conclusion, not as the premise of the paper.

**Exclude:** internal draft status, drafting rules, repository workflow, the complete taxonomy, K-SEND-01 details, named products, market statistics, and promotional calls to action.

**Word budget:** 220–300

---

### 5.1 Engineering Evolves Around Dominant Uncertainty

**Purpose:** Establish the path to Thinking Systems, define the category, distinguish it from agentic software, and expose the missing engineering connection.

**Core claim:** Planning, iterative delivery, and modern operations can be read as cumulative responses to requirement, product-learning, and production-condition uncertainty. Thinking Systems add consequential runtime-judgment uncertainty inside the controlled object. Existing policies, evaluations, traces, approval steps, and orchestration tools do not become a governable system unless connected to authorization, bounded authority, decision ownership, corrective action, and reassessment.

**Required content:**

- Explain the methodology comparison narrowly and cumulatively rather than as replacement history.
- Show how feedback moves closer to runtime as uncertainty becomes harder to contain before implementation.
- Preserve why plan-driven engineering remains rational where uncertainty can be reduced sufficiently in advance and late change is expensive.
- Preserve why iterative delivery does not abandon planning; it shortens the cycle between assumption, delivery, use, and revision.
- Preserve why modern operations extends engineering into runtime because production combinations cannot be reproduced exhaustively before release.
- State explicitly that Thinking Systems retain earlier uncertainty classes while adding consequential uncertainty produced through runtime Model Judgment.
- Introduce the canonical Thinking Systems definition in publication-facing prose.
- Define Model Judgment through interpretation, synthesis, classification, generation, planning, ranking, routing, or action selection under uncertainty.
- Explain that the category describes responsibility structure, not product marketing.
- Distinguish Linear Software, Thinking Systems, agentic Thinking Systems, and agentic but largely linear orchestration.
- State that autonomy and probabilistic judgment are separate dimensions.
- Open or transition into a credible team that has a model, retrieval or tools, traces, evaluations, policy, Human Authority, and a pilot.
- Ask the connected questions those components do not answer:
  - Was Model Judgment necessary?
  - What authority was delegated?
  - Which consequences are prohibited or unacceptable?
  - Which Constraints are authoritative?
  - How are they realized?
  - Which evidence informs which decision?
  - Who may narrow, roll back, disable, redesign, or stop operation?
  - When does runtime evidence invalidate Project Authorization?
  - Does the business case survive the complete control cost?
- State fragmentation as practitioner observation unless current authoritative evidence supports a broader market claim.
- Explain that observability may describe behavior without authority to act; evaluation may estimate quality without defining an approved boundary; policy may express intent without realization; nominal human approval may lack information, time, power, or capacity; and orchestration may execute a workflow without authorizing it.
- Preserve the anti-substitution argument: evaluation score is not release authorization; prompt is not policy; policy is not a realized control; a human-in-the-loop label is not substantive Human Authority; a rollback button is not evidence that recovery is credible.
- Support factual claims about current industry practice with current primary or authoritative sources. When evidence is unavailable, label the point as practitioner observation.
- Do not claim that no governance, safety, systems, or control practice exists.

**Supporting figures:**

1. engineering responses around dominant uncertainty;
2. category boundary distinguishing Linear Software, Thinking Systems, agentic Thinking Systems, and largely linear agentic orchestration.

**Supporting table:** Location of uncertainty, primary engineering mechanism, and where decisive feedback appears. The table must state that earlier uncertainty classes persist.

**Repository anchors:**

- [`Glossary`](../../../00-doctrine/glossary.md)
- [`Uncertainty in the Controlled Object`](../../../00-doctrine/uncertainty-in-the-controlled-object.md)
- [`Model Judgment Placement`](../../../00-doctrine/model-judgment-placement.md)
- [`Failure Modes and Anti-Patterns`](../../../04-failure-modes/README.md)
- [`Designing Non-Deterministic Systems source intake`](designing-nondeterministic-systems-source-intake.md)

**Transition:** The missing connection exists because the system is often treated as conventional software with an additional AI component rather than as a changed controlled object.

**Closing claims:**

> Previous engineering methods learned to manage uncertainty surrounding software. Thinking Systems require engineering to manage consequential uncertainty produced by the software itself.

> The missing layer is not another AI component. It is the engineering connection between delegated judgment, authorized boundaries, evidence, decision authority, corrective action, and reassessment.

**Working word budget:** 1,000–1,300

---

### 5.2 The Controlled Object Has Changed

**Purpose:** Explain the doctrinal reason the rest of the engineering model changes and derive the connected decision horizons from the controlled-object shift.

**Core claim:** A Thinking System produces part of its consequential uncertainty inside the engineered object because runtime behavior depends partly on probabilistic Model Judgment. Once that happens, organizational, project / architecture, delivery, and runtime decisions become connected manifestations of one control problem.

**Required content:**

- Use determinism as a design-contract distinction, not a claim of perfect physical repeatability:

  ```text
  y = f(x)
  ```

- Describe model-mediated responsibility as selection from plausible outcomes under input, context, model configuration, state, and operating conditions:

  ```text
  y ~ P(y | x, context, model configuration, system state)
  ```

- Explain Model Judgment through interpretation, classification, ranking, planning, generation, routing, or action selection.
- Explain Input Interpretation, Decision Logic, and Output Mediation without presenting them as a mandatory pipeline.
- State that useful variance is the reason the model is present; the objective is bounded operation rather than elimination of all variance.
- Distinguish product and requirement uncertainty, environment and operational uncertainty, and runtime-judgment uncertainty.
- Preserve the mixed-system claim: deterministic responsibilities remain before, between, and after Judgment Nodes.
- Explain why model quality alone cannot define prohibited states, allocate residual-risk authority, restrict reachable actions, execute correction, or determine Project Reauthorization.
- Explain why the changed object creates connected control questions across organizational context, project viability, architecture, delivery realization and release, and runtime reassessment.
- Preserve that levels use different evidence, participants, authority, time horizons, and actions and are not interchangeable.
- State that an operational Controller cannot rewrite an organizational prohibition; a Release Gate cannot expand project authority; Project Authorization cannot claim a Hard Constraint without a complete realized path; and organizational policy is not an operable boundary merely because it is authoritative.
- Introduce the recurring control questions:

  ```text
  What outcome or condition is intended?
  → What operating space is acceptable?
  → What uncertainty or disturbance can move the object outside it?
  → What evidence reveals behavior, outcome, conditions, and control state?
  → Who or what may decide that action is required?
  → Which mechanism can change operation?
  → When does new evidence require reassessment at this or an earlier level?
  ```

- Explain that the transfer from control theory is structural, not a claim that organizations, projects, delivery teams, and runtime services are equivalent to one mathematical Controller or reducible to one scalar error signal.
- State that existing disciplines remain necessary and are connected rather than replaced.

**Primary Figure 1 — Controlled-object shift**

Use a two-panel comparison of responsibility structure, not one mandatory execution path.

```text
Panel A — Primarily explicitly encoded runtime behavior
external, requirement, delivery, and operational uncertainty
→ explicitly encoded decision and action responsibilities
→ observed outputs, actions, and outcomes

Panel B — Thinking System boundary
external, requirement, delivery, and operational uncertainty
→ deterministic responsibilities before, between, and after Judgment Nodes
↔ one or more bounded Judgment Nodes
   placed as Input Interpretation, Decision Logic,
   Output Mediation, or a combination
→ observed outputs, actions, and downstream outcomes
```

Show approved Constraints and their realizations, Sensors and evidence, Controller authority, and Actuator paths across the relevant system boundary and around material Judgment Nodes.

The figure must not imply that:

- traditional software has no uncertainty;
- a Thinking System is wholly probabilistic;
- every system has one Judgment Node;
- Judgment placement follows one fixed order;
- every realization acts before a model call;
- capability families form a vertical execution sequence.

**Supporting figures:**

- functional placement of Model Judgment;
- connected locations of requirement, operational, and runtime-judgment uncertainty;
- one controlled object viewed across four decision horizons.

**Repository anchors:**

- [`Uncertainty in the Controlled Object`](../../../00-doctrine/uncertainty-in-the-controlled-object.md)
- [`Glossary`](../../../00-doctrine/glossary.md)
- [`Model Judgment Placement`](../../../00-doctrine/model-judgment-placement.md)
- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)

**Transition:** Once consequential uncertainty is produced inside execution, measurement is necessary but no longer the complete engineering contract.

**Closing claim:**

> The problem is not merely that AI is harder to test. Part of the controlled object's behavior is now produced through runtime judgment, and every decision that controls that object must account for the change.

**Working word budget:** 900–1,200

---

### 5.3 From Model Quality to Bounded Control

**Purpose:** Introduce the accepted Control-Loop Capability Anatomy and distinguish measurement, feedback closure, and bounded acceptable operation.

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

- Explain why a loop may remain closed while unsafe, over-authorized, too slow, operationally fragile, or economically unacceptable.
- Introduce the four logical capability families without presenting UA as the premise:
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
- Avoid UA-first formulations such as “UA asks” in this section; the capability anatomy must follow from the problem itself.

**Figures:**

- supporting figure — closed feedback loop;
- supporting figure — complete bounded control architecture showing the four capability families as logical functions, not services, layers, or one execution order.

**Repository anchors:**

- [`Control-Loop Capability Anatomy`](../../../00-doctrine/control-loop-anatomy.md)
- [`AI Control Plane`](../../../02-ai-control-plane/README.md)
- [`Constraint Capability Family`](../../../02-ai-control-plane/01-constraints/README.md)
- [`Constraint Realization Catalog`](../../../02-ai-control-plane/01-constraints/constraint-realization-catalog.md)
- [`Actuator Capabilities`](../../../02-ai-control-plane/00-actuators/README.md)
- [`Sensor and Evidence Capabilities`](../../../02-ai-control-plane/02-sensors/README.md)
- [`Controller and Decision Authority`](../../../02-ai-control-plane/03-controller/README.md)

**Transition:** Capability functions explain what bounded control requires, but not where project, release, runtime, and organizational decisions are owned.

**Closing claims:**

> A closed loop can still be unacceptable when it operates outside an approved, credibly realized, observable, and correctable boundary.

> Capability without legitimate decision ownership is not a complete control architecture.

**Working word budget:** 750–950

---

### 5.4 Four Decision Levels for Thinking Systems

**Purpose:** Present the connected organizational, project / architecture, delivery, and runtime horizons as the conceptual center of the paper.

**Core claim:** Different control decisions require different evidence, authority, time horizons, and corrective actions. They must remain connected without collapsing into one gate, platform, committee, or governance process.

**Primary Figure 2 — Two orthogonal models**

Show two adjacent views:

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

**Required argument:**

- Link existing legal, contractual, security, privacy, safety, procurement, vendor, geography, prohibited-use, incident, and decision-right sources.
- Identify which existing functions legitimately influence the Thinking System and which decisions each owns.
- Depending on the system, these may include product, engineering, architecture, operations, security, privacy, legal, compliance, procurement, finance, customer support, domain specialists, and executive authority.
- Define material dependencies, evidence needs, exception rights, response obligations, and escalation paths before they are needed.
- Do not imply that every function participates in every project or runtime decision.
- Do not create a mandatory UA organizational artifact, committee, or governance department.
- Preserve SMB proportionality: several responsibilities may be carried by the same people while decisions remain explicit.
- Organizational sources do not become Hard Constraints merely because they are authoritative; realization and scoped guarantee still matter.

**Supporting figure — Organizational influence architecture:** Show relevant functions converging into explicit decision rights and dependencies around the Thinking System, with evidence returning to those responsibilities.

#### Project control architecture and viability

**Question owned:** Does a credible, operable, and economically viable control architecture exist for this proposed Thinking System within a defined boundary?

**Required argument:**

- Before substantial implementation begins, describe at least one credible complete control loop for each material scenario.
- This does not require final production configuration but requires more than a list of future controls.
- Identify outcome and AI necessity, project boundary, material scenarios, Requirement and Operating Envelope, reachable consequences, Project Constraint Architecture, intended realizations, evidence feasibility, Controller authority, Actuators, Human Authority, fallback, expected feedback latency, assumptions, failure behavior, capacity, and reauthorization conditions.
- Include the full control perimeter cost in project viability from the beginning.
- Include evaluation, observability, semantic review, Human Authority capacity, fallback, incident response, model/vendor dependencies, control maintenance, and operational friction.
- Distinguish bounded research authorization from production authorization.
- A successful prototype is not Project Authorization.
- Preserve Architectural Veto as a valid engineering result.
- Produce one versioned Project Constraint Architecture and authorization baseline.

**Supporting figure — Project control architecture and viability:** Show intended outcome → material scenarios → Project Constraint Architecture → credible loop → Human Authority/fallback and economics → authorization, narrowing, research, redesign, deferral, or No-Go.

#### Designing the control architecture

**Required argument:**

- Translate material business and operational risks into a realizable control structure.
- Identify where Model Judgment is placed, what authority and consequences are reachable from each Judgment Node, which deterministic responsibilities must surround it, and which scenarios could produce unacceptable outcomes.
- Derive the required Constraints, candidate Constraint Realizations, Sensors, Controller decisions, Actuator paths, Human Authority, fallback, containment, recovery, and reassessment mechanisms.
- Distinguish machine-checkable or syntactic evidence from semantic or probabilistic evidence without creating new capability families.
- Machine-checkable evidence may verify schema, type, structure, permissions, tool arguments, state transitions, resource limits, and other deterministic conditions.
- Semantic evidence may estimate grounding, relevance, harmfulness, intent alignment, factual support, policy meaning, or downstream business acceptability.
- Semantic evidence must expose coverage, uncertainty, latency, and blind spots rather than being treated as an oracle.
- Treat Human Authority as part of the architecture where required, including information, decision right, time, expected volume, expertise, fatigue, escalation rights, unavailability, and overload.
- Drive the design from the risks, authority, and consequences of the system rather than a generic control-component checklist.

#### Delivery-level Thinking System Review

**Question owned:** Is a bounded system, feature, or material change ready, complete, and acceptable for a specific deployment context under Project Authorization?

**Required argument:**

- Delivery owns implementation-level Judgment Nodes, delivery Requirement and Operating Envelope, one canonical Constraint Realization Map, DoR, implementation or bounded experiment, DoD, Release Gate, and local reassessment.
- Delivery readiness includes team capability, not only code completion.
- The team as a whole must understand deterministic responsibility versus Model Judgment, Constraint realization, behavioral evidence, drift, delegated authority, runtime correction, and escalation.
- The delivery responsibility must cover architecture, implementation, deterministic verification, semantic evaluation, release decisions, observability, runtime operation, Human Authority, and escalation.
- The team must understand drift across model, prompt, context, retrieval, tools, data, evaluators, configuration, and population.
- Establish two-way translation:
  - business risk and authority → scoped scenarios, Constraints, evidence requirements, decision basis, and Actuators;
  - technical drift or degradation → changed business exposure, capacity, authority, and project viability.
- This translation is part of system design and operation, not a reporting exercise after implementation.
- Distinguish:
  - DoR establishes readiness and the authority basis for bounded work;
  - DoD establishes implementation and evidence completeness;
  - Release Gate accepts, limits, conditions, escalates, or rejects a deployment.
- Delivery may narrow but must not expand project authority or weaken an inherited Hard Constraint.

**Supporting figure — Delivery translation loop:** Business intent/risk/authority → engineering translation → implementation → technical evidence → business interpretation → reassessment.

#### Runtime operation and reassessment

**Question owned:** Does active operation remain within the approved Requirement, Constraint baseline, authority, capacity, and economics, with required realizations active and healthy, and what action follows when it does not?

**Required argument:**

- Monitor the complete socio-technical controlled system, not only the model.
- Evidence may include model behavior, downstream outcomes, active model and prompt versions, context and retrieval state, tool use, authorization failures, realization activation and bypass, syntactic and semantic evidence, drift, complaints, overrides, Human Authority capacity, fallback load, cost, latency, incidents, Actuator execution, and whether corrective action produced the intended state.
- Connect every material signal to an interpretation boundary, expected decision latency, responsible Controller, available Actuator, and escalation or reassessment route.
- Runtime Controllers may decide only within delegated authority.
- Runtime Actuators may reject, contain, compensate, route to fallback, narrow exposure, roll back, disable, or stop operation.
- Distinguish restoration from redesign:
  - local action may restore a previously authorized state;
  - persistent drift, changed business exposure, unsustainable Human Authority load, loss of Sensor validity, or broken control economics may require delivery reassessment or Project Reauthorization.
- Route evidence by the basis invalidated:

  ```text
  local implementation, realization, configuration, or evidence issue
  → delivery reassessment

  project risk, authority, feasibility, evidence, capacity, or economics changed
  → Project Reauthorization

  authoritative source, decision right, or shared capability changed
  → organizational review
  ```

- A proposed authority expansion is not runtime tuning and requires Project Reauthorization and, where necessary, organizational review.

**Supporting figures:**

- runtime control and reassessment;
- evidence and change routing.

**Repository anchors:**

- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
- [`Project Control Architecture and Viability Review`](../../../01-patterns/project-control-architecture-and-viability-review.md)
- [`Thinking System Review`](../../../01-patterns/thinking-system-review.md)
- [`Judgment Node Boundary`](../../../01-patterns/judgment-node-boundary.md)

**Transition:** Once decision ownership is separated, the practical problem becomes preserving the chain without creating four parallel governance processes.

**Closing claim:**

> Lower levels may refine and narrow a higher-level decision. They may not silently expand its authority or normalize evidence that invalidates it.

**Working word budget:** 1,700–2,200

---

### 5.5 From Authority to Operation: Two Living Reviews

**Purpose:** Explain inheritance, realization, evidence routing, and the default SMB operating surface without reproducing the templates.

**Core claim:** The model can remain proportional by preserving one project Constraint artifact and one delivery realization artifact, linked to existing organizational sources and runtime evidence.

**Canonical path:**

```text
existing organizational sources, shared capabilities, and decision rights
→ one living Project Control Architecture and Viability Review
→ one versioned Project Constraint Architecture and authorization
→ one living Thinking System Review per bounded delivery scope
→ one canonical Constraint Realization Map
→ deployment-specific Release Gate
→ active runtime versions, evidence, decisions, and actions
→ delivery reassessment, Project Reauthorization, or organizational review
```

**Required content:**

- Constraint authority flows downward by reference; policy prose is not copied as if it were a complete technical control.
- Project-level Constraints are interpreted or derived, scoped, and connected to required realization, assumptions, evidence, authority, economics, inheritance, and reauthorization.
- Delivery makes realization concrete through active mechanisms, configuration, verification, failure behavior, evidence, change authority, and release scope.
- Runtime preserves material source, project, delivery, realization, model, prompt, policy, tool, and deployment versions.
- Judgment Nodes, DoR, DoD, Release Gate, and runtime sections reference the same Constraint Realization Map rather than creating parallel records.
- Additional registers, RACIs, gate files, financial models, or committees remain optional when independent ownership, lifecycle, access, retention, regulation, or audit needs justify them.
- Two living reviews are the proportional default, not a universal sufficiency claim.
- One person may carry several responsibility bundles without collapsing the decisions.

**Required figure:** Show existing organizational sources above the two living reviews, the Project Constraint Architecture and Constraint Realization Map as the two canonical Constraint artifacts, deployment-specific release below, and runtime evidence returning upward to delivery, project, or organization.

**Repository anchors:**

- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
- [`Project Review Template`](../../../01-patterns/project-control-architecture-and-viability-review-template.md)
- [`Thinking System Review Template`](../../../01-patterns/thinking-system-review-template.md)
- [`Judgment Node Boundary`](../../../01-patterns/judgment-node-boundary.md)

**Transition:** An illustrative Constraint trace can make the consequences concrete without pretending that the repository already contains independent evidence for a complete two-level application.

**Closing claim:**

> The goal is not to document everything repeatedly. It is to preserve the chain from authoritative source to scoped Constraint, concrete realization, runtime evidence, and corrective decision.

**Working word budget:** 500–700

---

### 5.6 One Constraint Across the Full Lifecycle

**Purpose:** Illustrate one continuous project-to-runtime decision path without claiming that the repository already contains a completed two-level worked application.

**Evidence boundary:** The narrative is an editorial synthesis using the project pattern, Constraint capability, and illustrative delivery review for support triage. It illustrates specification behavior; it is not independent application evidence.

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
Change authority: delivery may repair or roll back inside the baseline; autonomous sending requires Project Reauthorization and organizational review
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
2. **Project assumption invalidated** — review volume and latency make the control perimeter economically non-viable at planned scale. `K-SEND-01` remains valid, but project capacity and economics do not. Project Reauthorization narrows, redesigns, defers, or rejects the path.
3. **Separate authority-change request** — the business requests autonomous sending. This is not runtime evidence or delivery tuning. It requires Project Reauthorization and organizational review before any new realization is designed.

**Primary Figure 3 — K-SEND-01 Constraint trace**

```text
organizational prohibition and reserved Human Authority
→ Project Constraint K-SEND-01
→ delivery Constraint Realization Map
→ runtime evidence
   ├─ local defect → delivery reassessment
   └─ capacity/economics invalidated → Project Reauthorization

separate proposed authority expansion
→ Project Reauthorization + organizational review
```

Label the figure as an illustrative editorial synthesis, not application evidence.

**Repository anchors:**

- [`Project Control Architecture and Viability Review`](../../../01-patterns/project-control-architecture-and-viability-review.md)
- [`Thinking System Review`](../../../01-patterns/thinking-system-review.md)
- [`Worked Support-Triage Review`](../../../03-reference-architectures/worked-thinking-system-review-support-triage.md)
- [`Constraint Realization Catalog`](../../../02-ai-control-plane/01-constraints/constraint-realization-catalog.md)

**Transition:** The example separates the decision architecture from the products that may implement parts of it, making the platform boundary precise.

**Closing claim:**

> Evidence and proposed authority changes must route according to the decision basis they invalidate or seek to change, not merely according to where they first appear.

**Working word budget:** 650–850

---

### 5.7 What Platforms Can Implement — and What Authority They Do Not Acquire by Default

**Purpose:** Address productization without dismissing agent, governance, observability, or AI-native delivery platforms.

**Core claim:** A platform may implement multiple control capabilities and may exercise explicitly delegated Controller authority, but hosting or automating those capabilities does not create organizational or project authority.

**Required content:**

- Classify platform functions by what they do in the specific system, not by market category.
- A platform may host or implement Constraint Realizations, Sensors and evidence, bounded automated Controller logic, human decision interfaces, Actuators, version records, and decision records.
- A platform does not independently determine whether Model Judgment is necessary, which source is authoritative, what consequences or authority are acceptable, who may accept residual risk, whether Human Authority is substantive, whether the control perimeter preserves viability, or when Project or organizational authorization must change.
- A platform may execute delegated authority. It does not create that authority.
- Avoid the categorical claim that platforms “cannot solve governance.” State the narrower ownership and delegation boundary.
- Verify named-platform claims against current first-party documentation. Prefer functional, vendor-neutral framing when a named comparison is unnecessary.

**Required figure:** Show implementable platform functions inside delegated authority and organizational/project decisions outside the platform's default mandate.

**Repository anchors:**

- [`Control-Loop Capability Anatomy`](../../../00-doctrine/control-loop-anatomy.md)
- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
- [`AI Control Plane`](../../../02-ai-control-plane/README.md)
- [`Specification`](../../../SPECIFICATION.md)

**Transition:** The ownership boundary explains why the resulting model is developed as an open specification rather than one privileged implementation.

**Closing claim:**

> A platform can make control capabilities easier to implement and may exercise delegated decision logic. It does not, by default, authorize the project or define the organizational boundary in which that implementation is legitimate.

**Working word budget:** 400–550

---

### 5.8 From Thinking Systems to Uncertainty Architecture

**Purpose:** Introduce UA only after the engineering model has been derived, then state repository scope, current maturity, limits, and invitation.

**Core claim:** Uncertainty Architecture is the open draft specification that organizes the derived responsibilities for Thinking Systems; it is coherent enough to inspect and test but lacks sufficient independent application evidence for a maturity claim.

**Required content:**

- Explicitly connect the preceding deduction to UA without implying that the deduction proves UA uniquely correct.
- Explain the name: architecture for locating, bounding, observing, deciding about, correcting, and reassessing consequential uncertainty across a socio-technical system.
- Present the four capability families, four decision levels, two living reviews, and Constraint trace as the current specification spine.
- Explain tool neutrality and the separation between capability and authority.

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

**Why open:** Enable independent critique and contradictory evidence, compare application across domains, prevent vendor or author capture of the control language, preserve visible evolution, and support many implementations.

**Licensing:** Documentation and specification material use CC BY 4.0; code and reference implementations use Apache 2.0 where present.

**Validation request:** Ask for documented applications, anonymized reviews, contradictory cases, terminology issues, simplification proposals, platform mappings, control-cost evidence, Human Authority failures, and operational failure modes.

**Required final figure:** A compact map from Thinking System problem → bounded control capabilities → connected decision levels → living reviews and evidence routing → Uncertainty Architecture open specification. It may synthesize earlier figures but must introduce no new doctrine.

**Repository anchors:**

- [`README.md`](../../../README.md)
- [`SPECIFICATION.md`](../../../SPECIFICATION.md)
- [`ROADMAP.md`](../../../ROADMAP.md)
- [`CONTRIBUTING.md`](../../../CONTRIBUTING.md)
- [`Research Track`](../index.md)

**Closing claim:**

> Uncertainty Architecture is coherent enough to be tested, not mature enough to be protected from criticism. The next step is external application, contradictory evidence, and revision.

**Working word budget:** 550–750

## 6. Figure contract

The three primary architectural figures are:

1. **Controlled-object shift** — two-panel comparison of responsibility structure, showing one or more possible Judgment Node placements without prescribing a pipeline.
2. **Two orthogonal models** — decision levels with downward inheritance and upward reassessment beside capability families applying at every level.
3. **K-SEND-01 Constraint trace** — illustrative source-to-runtime path with delivery reassessment, Project Reauthorization, and separate authority expansion.

Supporting figures currently expected:

- engineering responses around dominant uncertainty;
- Thinking Systems category boundary;
- Model Judgment placement;
- connected uncertainty locations;
- one controlled object across four decision horizons;
- closed feedback loop;
- complete bounded control architecture;
- organizational influence architecture;
- project control architecture and viability;
- delivery translation loop;
- runtime control and reassessment;
- evidence and change routing;
- two living reviews operating surface;
- platform capability and authority boundary;
- final Thinking Systems-to-UA synthesis.

Supporting figures are not capped. They must materially strengthen comprehension, introduce no new doctrine, remain consistent with owning repository sources, carry explicit non-prescriptive captions, and remain subordinate to the primary figures.

Do not use the presentation's brain/nerves/skeleton/muscles stack as the canonical article architecture diagram. It may be mentioned as source history only.

## 7. Terminology and claim-safety rules

Use current terms: Thinking System, Linear Software, Model Judgment, Judgment Node, Constraint, Constraint Realization, Hard Constraint, Soft Constraint, Sensor, Controller, Actuator, Human Authority, Project Constraint Architecture, Constraint Realization Map, Nested Control Lifecycle, Project Authorization, Project Reauthorization, DoR, DoD, and Release Gate.

Treat Behavioral Software, Behavioral Applications, fixed specialist role titles, universal maturity ladders, universal thresholds, and the old three-part Actuator/Sensor/Controller model as historical or contextual only.

Do not:

- equate Thinking Systems with all agentic applications;
- imply that all agentic software is necessarily a Thinking System under the canonical definition;
- imply that a non-agentic application cannot be a Thinking System;
- call a prompt, natural-language policy, probabilistic evaluator, classifier, or model preference a Hard Constraint by itself;
- call a schema, permission check, or other realization a Constraint without distinguishing the authoritative Constraint from its realization;
- describe Actuators as defining policy or authorizing their own changes;
- collapse evaluator, gate decision, and release execution;
- equate closed feedback with acceptable bounded operation;
- imply runtime reauthorizes a project automatically;
- classify every deviation as a Bug;
- describe aggregate quality, cost, latency, or capacity tolerances as Hard Constraints without deterministic enforcement;
- present the illustrative K-SEND-01 trace as independent application evidence;
- use internal UA documents as evidence for current external standards, laws, products, or market practice;
- introduce UA as the premise that validates the early engineering argument.

## 8. Repository source plan

### Authority-bearing framework sources

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
14. [`Sensor and Evidence Capabilities`](../../../02-ai-control-plane/02-sensors/README.md)
15. [`Controller and Decision Authority`](../../../02-ai-control-plane/03-controller/README.md)

Status and ownership still apply within this set. The paper may derive an explanatory sequence, but it must not override the specification, glossary, or owning source.

### Supporting repository sources

- [`Constraint Realization Catalog`](../../../02-ai-control-plane/01-constraints/constraint-realization-catalog.md) — informative implementation examples.
- [`Worked Support-Triage Review`](../../../03-reference-architectures/worked-thinking-system-review-support-triage.md) — illustrative delivery-level reference.
- [`Failure Modes and Anti-Patterns`](../../../04-failure-modes/README.md) — reusable loss-of-control mechanisms according to document status.
- [`ROADMAP.md`](../../../ROADMAP.md) — current project state and open validation work.

Historical articles, talks, presentation material, and research may provide provenance and evidence. They must not override authority-bearing framework sources.

### External evidence

Current factual claims about standards, laws, platform capabilities, market practice, or the state of AI governance must be checked against current primary or authoritative sources. Named platform capabilities must be checked against first-party documentation. Comparative claims should be narrow, dated, and should not imply exhaustive market coverage.

## 9. Publication framing

### Working title

**Uncertainty Architecture: Engineering Thinking Systems That Produce Consequential Judgment**

The title begins with **Uncertainty Architecture** for attribution and discoverability, while the article body delays full framework introduction until the engineering model has been derived.

### Target length

The working manuscript may exceed the earlier 4,300–5,200-word target while the argument is still being constructed. Preserve the argument during section drafting; perform one integrated reduction pass only after all eight sections exist.

Expected working range: **6,500–8,500 English words**, subject to final editorial compression.

### Target and publication paths

Working article:

```text
content/research/notes/open-engineering-specification-article-draft.md
```

Published repository edition:

```text
content/research/publications/uncertainty-architecture-thinking-systems.md
```

Medium and LinkedIn editions are distribution copies and should link back to the repository edition.

## 10. Iteration acceptance criteria

Every article-writing PR must satisfy all of the following:

- [ ] The complete blueprint was read before selecting the next section block.
- [ ] The complete target article was read before drafting.
- [ ] New prose continues the existing argument and terminology.
- [ ] Previously written sections were revised where the new block exposed repetition, contradiction, weak transitions, or premature framing.
- [ ] Every major new argument has an appropriate figure or an explicit reason why prose is clearer.
- [ ] All figures were reviewed as one visual sequence and renumbered consistently.
- [ ] The complete target article was reread after integration.
- [ ] This blueprint was updated after the target article review.
- [ ] Section purposes, required content, transitions, claims, examples, and known risks remain detailed rather than compressed.
- [ ] UA is not introduced as the premise of the early engineering argument.
- [ ] Thinking Systems remain distinct from agentic software.
- [ ] Decision levels and capability families remain orthogonal.
- [ ] Constraint and Constraint Realization remain distinct.
- [ ] Project Authorization, DoR, DoD, Release Gate, runtime correction, and Project Reauthorization remain separate.
- [ ] Project Constraint Architecture and Constraint Realization Map remain the two canonical Constraint artifacts.
- [ ] Runtime evidence and proposed authority changes are not conflated.
- [ ] Platform implementation and decision authority remain separate.
- [ ] Illustrative material is not presented as independent validation.
- [ ] Source authority, external-evidence rules, maturity boundaries, and publication framing remain accurate.
