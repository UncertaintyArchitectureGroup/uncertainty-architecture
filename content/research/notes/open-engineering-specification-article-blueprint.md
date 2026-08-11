---
title: "Article Blueprint — Uncertainty Architecture: Engineering Thinking Systems with Consequential Runtime Responsibilities"
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
updated: 2026-08-11
language: en
license: CC-BY-4.0
draft: true
---

# Article Blueprint — Uncertainty Architecture: Engineering Thinking Systems with Consequential Runtime Responsibilities

> **Status:** Living editorial design document for the article. This is a non-normative research note, not article prose and not a specification source. It preserves the complete argument, section responsibilities, claim boundaries, figures, transitions, source plan, writing notes, and unresolved editorial decisions. It must evolve after every drafting iteration and must not be compressed into a checklist merely because publication prose exists.

## 1. Editorial decision

The public article uses **Thinking Systems** as the engineering category through which the problem is developed. It does not begin by presenting Uncertainty Architecture as the premise that validates the argument.

The article first:

1. defines Thinking Systems;
2. distinguishes them from agentic applications;
3. explains why making a Consequential Runtime Responsibility depend partly on probabilistic Model Judgment changes the controlled object;
4. derives the required control capabilities and decision levels;
5. develops the four decision levels as an operating model with explicit triggers, inputs, decisions, capability obligations, outputs, evidence routes, escalation, and learning;
6. makes the model practical through two living reviews and one continuous Constraint trace;
7. separates platform implementation from organizational and project authority;
8. introduces **Uncertainty Architecture** near the end as the open specification that organizes the derived model.

The connected argument is:

```text
engineering expands around consequential uncertainty it can no longer leave outside its operating model
→ Thinking Systems place probabilistic Model Judgment inside the controlled object
→ Thinking Systems are not synonymous with agentic applications
→ useful runtime variance changes the engineering contract rather than merely making testing harder
→ model quality and observability are necessary but insufficient
→ bounded operation requires four control-capability families
→ governance becomes operational through the active socio-technical control architecture, not through a post-hoc review or document
→ different decisions are owned at four connected lifecycle levels
→ each level must have explicit triggers, inputs, decision rights, evidence needs, downward outputs, and reassessment routes
→ an incomplete cross-level control architecture means the application is not ready for production release at the intended scope
→ authoritative Constraints flow downward by reference while realization becomes concrete
→ runtime and delivery evidence returns to the decision level whose basis it invalidates
→ negative cases feed structured learning back into Sensors, Constraints and realizations, Controllers, Actuators, assumptions, and authorization
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

The four decision levels must be explained as an **operating model through time**, not merely as four static ownership descriptions. Each level must therefore answer a common set of questions:

```text
What activates this level?
→ What inputs and authoritative sources arrive here?
→ Which questions and decisions are owned here?
→ Which Constraints, Sensors, Controllers, and Actuators must exist or be required because of those decisions?
→ What outputs, boundaries, delegated authority, evidence obligations, and artifacts flow downward?
→ What evidence, exceptions, change requests, or invalidated assumptions flow upward?
→ Which decisions can be taken locally and which require reassessment or reauthorization?
→ How do negative cases improve the control architecture over time?
```

This common frame is an editorial rule for Section 5.4. It is not a claim that all four levels use identical processes, teams, cadence, documents, or automation.

The opening may use **plan-driven development**, **iterative delivery**, and **modern operations** as a narrow explanatory lens, with **Waterfall**, **Agile and related approaches**, and **DevOps** named as familiar but non-equivalent examples. The broader engineering categories must remain primary in the prose, Figure 1, and the comparison table. The comparison must not claim that one methodology replaced another, reduce any movement to one purpose, or use the comparison as evidence of a universal historical law. Its role is to show how engineering expands when an important location of uncertainty can no longer remain outside the engineering model.

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

Visual emphasis may be used when it carries architectural meaning. In particular, a distinct red treatment may identify where a Consequential Runtime Responsibility depends partly on probabilistic Model Judgment inside the controlled object, but it must not imply that the entire Thinking System is probabilistic or unsafe.

## 3. Stable thesis and claim boundary

### Stable thesis paragraph

Thinking Systems are software systems in which one or more **Consequential Runtime Responsibilities** depend partly on probabilistic Model Judgment rather than being fully specified through explicitly encoded logic in advance. The category names the changed engineering object; it does not certify that the object is adequately controlled. Because useful runtime judgment places consequential uncertainty inside that object, evaluation, observability, policies, human approval, and agent orchestration remain incomplete when disconnected from approved boundaries, concrete realizations, decision authority, corrective action, and reassessment. For production use, the complete socio-technical control architecture is part of the application rather than a governance layer added after implementation: governance becomes operational only through that architecture, and when it remains incomplete across organizational authority, project and architecture viability, delivery realization and release, and runtime operation and reassessment, the application is not ready for production release at the intended scope. The article derives this engineering model first and introduces Uncertainty Architecture near the end as an open, tool-neutral specification connecting those responsibilities.

### Thinking Systems definition

Use the canonical glossary definition:

> A software system in which one or more **Consequential Runtime Responsibilities** depend partly on probabilistic Model Judgment rather than being fully specified through explicitly encoded logic in advance.

Use **Consequential Runtime Responsibility** as an implementation-neutral classification term: a runtime responsibility is consequential when its output, decision, path, action, or downstream state can materially affect an intended outcome, satisfaction of an applicable Requirement or Constraint, the exercise of delegated authority, resource use, or a person or system downstream. State explicitly that **consequential describes material causal relevance, not implementation mechanism or risk severity**. A Consequential Runtime Responsibility may be fulfilled entirely through explicitly encoded logic or may depend partly on probabilistic Model Judgment; Thinking-System classification changes only in the latter case. Harm, severity, likelihood, reversibility, residual exposure, autonomy, regulation, control strength, and release decisions remain separate. A model invocation with no material influence on any Consequential Runtime Responsibility is not sufficient by itself to establish Thinking-System classification.

Preserve the following category boundary:

- fixed, linear, iterative, adaptive, or dynamically selected orchestration does not determine whether software is Linear Software or a Thinking System;
- a fixed or explicitly orchestrated sequence is a Thinking System when one or more **Consequential Runtime Responsibilities** depend partly on probabilistic Model Judgment;
- category membership and control adequacy are separate: missing Constraints, evidence, decision rights, or corrective mechanisms may make a Thinking System inadequately controlled or not production-ready without changing its category;
- the category may begin in a first simple model-enabled iteration and does not require agents, dynamic routing, multiple models, or high autonomy;
- deterministic code before, between, or after Judgment Nodes does not make delegated Model Judgment deterministic;
- autonomy and delegated authority are additional dimensions separate from both Model Judgment and orchestration topology;
- systems described as agentic may use fixed or dynamic orchestration, while an agent label alone neither establishes nor excludes Thinking-System classification;
- the precise boundary of agentic terminology remains an open research topic and must not be presented as settled doctrine;
- a non-agentic feature may be a Thinking System when probabilistic judgment materially affects interpretation, routing, decisions, outputs, or downstream action;
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
2. why making a Consequential Runtime Responsibility depend partly on probabilistic Model Judgment changes the controlled object;
3. the difference between measurement, a closed feedback loop, and bounded acceptable operation;
4. why governance for a Thinking System becomes operational through an active socio-technical control architecture rather than through a post-hoc review or document;
5. why a Thinking System intended for production use without a complete cross-level control architecture is not ready for production release at the intended scope;
6. the four capability families and their boundaries;
7. the four decision levels and the question owned by each;
8. what activates each decision level, what arrives there, what it decides, what it sends downward, what evidence returns upward, and when reassessment is required;
9. how organizational authority, Project Constraint Architecture, delivery Constraint Realization Map, runtime evidence, and reassessment connect;
10. why Project Authorization, DoR, DoD, Release Gate, runtime correction, and Project Reauthorization are different decisions;
11. how control economics affects the decision to use Model Judgment at all, not only the choice of model;
12. how negative cases should improve Sensors, Constraints and realizations, Controllers, Actuators, assumptions, and authorization rather than becoming isolated incident closure;
13. why a Controller is a decision function that may combine legitimate human authority with automation rather than being synonymous with either a team or an algorithm;
14. how a small team can use the model without creating parallel governance bureaucracy;
15. what platforms may implement and what authority they do not acquire automatically;
16. what Uncertainty Architecture contributes, what exists in the repository, and what remains unvalidated.

## 5. Article structure

### Unnumbered abstract

**Purpose:** Introduce Thinking Systems, establish the controlled-object shift, and summarize the production-release condition without narrating the article's internal reveal sequence.

**Required content:**

- software engineering expands when important uncertainty can no longer remain outside its operating model;
- use **plan-driven development**, **iterative delivery**, and **modern operations** as the primary categories, with **Waterfall**, **Agile and related approaches**, and **DevOps** named as familiar examples;
- the canonical Thinking Systems definition;
- explicit distinction from agentic software;
- a Consequential Runtime Responsibility depends partly on probabilistic Model Judgment inside the controlled object;
- model quality and observability are insufficient when disconnected from boundaries, authority, corrective action, and reassessment;
- for production use of a Thinking System, an incomplete control architecture means the application is not ready for production release at the intended scope even if model and code tests pass locally;
- governance becomes operational through the socio-technical control architecture spanning organizational, project / architecture, delivery, and runtime decision levels, not through a post-hoc review, compliance document, or approval ceremony;
- the paper derives capability families, decision levels, and a proportional operating surface.

**Exclude:** internal draft status, drafting rules, repository workflow, statements narrating when the paper will reveal UA such as “Only after the problem...”, the complete taxonomy, K-SEND-01 details, named products, market statistics, and promotional calls to action.

**Word budget:** 240–330

---

### 5.1 Engineering Evolves Around Dominant Uncertainty

**Purpose:** Establish the path to Thinking Systems, define the category, distinguish it from agentic software, expose the missing engineering connection, and make the production-release condition explicit.

**Core claim:** **Plan-driven development**, **iterative delivery**, and **modern operations** can be read as cumulative responses to requirement, product-learning, and production-condition uncertainty, with Waterfall, Agile and related approaches, and DevOps serving as familiar but non-equivalent examples. Thinking Systems add runtime-judgment uncertainty when Consequential Runtime Responsibilities depend partly on probabilistic Model Judgment inside the controlled object. Existing policies, evaluations, traces, approval steps, and orchestration tools do not become a governable or production-release-ready system unless connected to authorization, bounded authority, decision ownership, corrective action, and reassessment.

**Required content:**

- Explain the methodology comparison narrowly and cumulatively rather than as replacement history.
- Keep the broader engineering responses primary and name Waterfall, Agile and related approaches, and DevOps in parentheses or explanatory prose as familiar examples.
- Do not describe iterative approaches as derivatives of Agile or imply historical equivalence among Waterfall, Agile, and DevOps.
- Show how feedback moves closer to runtime as uncertainty becomes harder to contain before implementation.
- Preserve why plan-driven engineering, including Waterfall, remains rational where uncertainty can be reduced sufficiently in advance and late change is expensive.
- Preserve why iterative delivery, including Agile and related approaches, does not abandon planning; it shortens the cycle between assumption, delivery, use, and revision.
- Preserve why modern operations, commonly associated with DevOps, extends engineering into runtime because production combinations cannot be reproduced exhaustively before release.
- State explicitly that Thinking Systems retain earlier uncertainty classes while adding consequential uncertainty produced through runtime Model Judgment.
- Allow one restrained forward reference at this transition: identify it as the engineering problem Uncertainty Architecture addresses—how to build and operate systems once consequential behavior is partly produced through probabilistic Model Judgment—without introducing UA capability families, decision levels, or framework machinery as premises before they are derived.
- Introduce the canonical Thinking Systems definition in publication-facing prose and give the operational meaning of **consequential** used by the category test.
- Define Model Judgment through interpretation, synthesis, classification, generation, planning, ranking, routing, or action selection under uncertainty.
- Explain that the category describes responsibility structure, not product marketing. Keep the full justification for why a distinct name is needed, and the comparison with broader AI-system labels, in Section 5.2 after the controlled-object shift is introduced.
- Show a simple classification boundary: ask whether any **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment. Route **No** to Linear Software and **Yes** to Thinking System. Show orchestration topology, autonomy, and delegated authority as independent dimensions that affect architecture, risk, and control demand but do not decide category membership.
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
- State explicitly that these gaps are not governance debt that can be closed after release: for production use of a Thinking System, the application is not ready for production release at the intended scope without the complete control architecture across the four decision levels.
- Present this release-readiness consequence as a visually distinct publication-facing callout so the reader can identify it as a central engineering thesis without repeating the argument elsewhere.
- State that governance becomes operational through the socio-technical stack that makes the system bounded, observable, correctable, and reauthorizable, rather than through a policy document or post-release review.
- Support factual claims about current industry practice with current primary or authoritative sources. When evidence is unavailable, label the point as practitioner observation.
- Do not claim that no governance, safety, systems, or control practice exists.

**Supporting figures:**

1. engineering responses around dominant uncertainty, with nodes labeled **Plan-driven engineering (Waterfall)**, **Iterative delivery (Agile and related approaches)**, **Modern operations (DevOps)**, and **Thinking-System engineering**; the Figure 1 caption may identify the final transition as the problem space addressed by Uncertainty Architecture, but must not use UA as the premise from which the earlier engineering argument is derived;
2. classification boundary showing the single category question—whether any **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment—while orchestration topology, autonomy, and delegated authority remain visibly independent dimensions.

**Supporting table:** Location of uncertainty, primary engineering mechanism, and where decisive feedback appears. The first column must use the broader categories first: plan-driven development (including Waterfall), iterative delivery (including Agile and related approaches), modern operations (commonly associated with DevOps), and **Thinking-System engineering — problem space addressed by Uncertainty Architecture**. The table must state that earlier uncertainty classes persist and describe UA response as bounded control architecture rather than as the category definition itself.

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

> A Thinking System intended for production use is not ready for production release at the intended scope without that complete control architecture.

**Working word budget:** 1,100–1,450

---

### 5.2 The Controlled Object Has Changed

**Purpose:** Explain the doctrinal reason the rest of the engineering model changes and derive the connected decision horizons from the controlled-object shift.

**Core claim:** A Thinking System produces part of its consequential uncertainty inside the engineered object because runtime behavior depends partly on probabilistic Model Judgment. Once that happens, organizational, project / architecture, delivery, and runtime decisions become connected manifestations of one control problem.

**Required content:**

- Explain that **Thinking System** names the changed engineering object, not a maturity stage, architecture style, synonym for an agentic system, or replacement for the broader term **AI system**.
- Explain why the broader category is insufficient for this paper: ISO/IEC TR 29119-11 defines an AI-based system by the presence of at least one AI component, while the UA boundary asks whether **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment.
- Include a compact publication-facing comparison that keeps neighboring labels distinct rather than joining them as synonyms: at minimum separate ISO/IEC **AI-based system**, NIST **AI system**, **LLM application**, **agentic system**, and **autonomous system**. Present the table as an analytical comparison, not universal definitions of those neighboring labels.
- State that the category can begin in the first simple model-enabled iteration when an LLM or other probabilistic model performs one or more **Consequential Runtime Responsibilities**, even inside a predefined workflow.
- Use a project-planning example with a fixed sequence such as brief interpretation, requirement generation, planning, risk identification, and work-item drafting to show that deterministic orchestration does not remove delegated Model Judgment.
- Explain that later tools, memory, dynamic routing, multiple models, cooperating agents, or greater autonomy increase complexity and control demand but do not create the category.
- Explain why the object needs a distinct name: in Linear Software, relevant **Consequential Runtime Responsibility** is authored before runtime through explicit code, rules, or state transitions; in a Thinking System, part of the mapping from situation to consequential behavior is completed during runtime through Model Judgment.
- State explicitly that UA treats the whole Thinking System—not the model invocation—as the controlled object.
- Keep category identity separate from control adequacy: Constraints, evidence, decision authority, corrective mechanisms, and cross-level control architecture determine governability and production readiness rather than whether the object belongs to the category.
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
- Replace the dense one-paragraph summary of those horizons with four short publication-facing paragraphs using bold labels for **Organizational control context**, **Project / architecture control and viability**, **Delivery realization and release**, and **Runtime operation and reassessment**.
- Keep project viability and control-architecture design in the same project / architecture paragraph because they belong to one decision horizon; do not create a fifth level or a separate architecture horizon.
- Use that labeled passage as a forward bridge to the later sections rather than as a complete treatment of the levels.
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

Use two vertical top-to-bottom responsibility diagrams placed side by side. The comparison must read as two parallel columns, not as two horizontal execution pipelines and not as one mandatory topology. Because disconnected Mermaid subgraphs may otherwise stack vertically, use an invisible alignment link between the columns to force the side-by-side GitHub rendering.

```text
Left — Primarily explicitly encoded runtime behavior
external, requirement, delivery, and operational uncertainty
→ explicitly encoded decision and action responsibilities
→ observed outputs, actions, and outcomes

Right — Controlled Thinking System — UA target structure
external, requirement, delivery, and operational uncertainty
→ deterministic responsibilities made explicit before, between, and after Judgment Nodes
↔ one or more bounded Judgment Nodes
   placed as Input Interpretation, Decision Logic,
   Output Mediation, or a combination
→ observed outputs, actions, and downstream outcomes
```

Carry the visual distinction inside the Thinking System column itself. Do not add a separate callout node that competes with the two-column comparison or changes the apparent topology.

Use restrained red treatment on the blocks whose responsibility changes because Model Judgment is present: the deterministic responsibility before judgment, the Judgment Node itself, and deterministic validation, authority, and execution after judgment. The external-input and final-output blocks and the Thinking System boundary itself should remain neutral. Red must identify the structural change, not imply that the whole Thinking System is probabilistic, unsafe, or erroneous. The right-hand control structure is an engineering target for controlled production use, not part of the category-membership test.

The figure must not imply that:

- traditional software has no uncertainty;
- a Thinking System is wholly probabilistic;
- every system has one Judgment Node;
- Judgment placement follows one fixed order;
- every realization acts before a model call;
- capability families form a vertical execution sequence;
- red denotes an error state rather than the structural addition being explained.

**Supporting figures:**

- functional placement of Model Judgment, with **Model Judgment** above and **Input Interpretation**, **Decision Logic**, and **Output Mediation** aligned horizontally beneath it;
- connected locations of requirement, operational, and runtime-judgment uncertainty;
- one controlled object viewed across four decision horizons, rendered as one centered vertical decision-horizon spine in the canonical order Organization → Project / Architecture → Delivery → Runtime. A single Runtime evidence node sits beneath Runtime. Direct dotted return routes lead from that evidence to Delivery, Project / Architecture, or Organization, with the invalidated decision basis written on the route itself. Reassessment criteria are routing conditions, not standalone architectural components or a separate subsystem.

The Model Judgment placement figure is a taxonomy, not a sequence. It must not connect the three placement categories laterally in a way that implies a mandatory pipeline.

For the four-horizon figure, keep each horizon block focused on the decision it owns rather than listing every responsibility. Downward edges should show authority and Constraints becoming more concrete. The caption must state that the figure shows decision ownership and reassessment routing, not a four-stage delivery workflow.

**Repository anchors:**

- [`Uncertainty in the Controlled Object`](../../../00-doctrine/uncertainty-in-the-controlled-object.md)
- [`Glossary`](../../../00-doctrine/glossary.md)
- [`Model Judgment Placement`](../../../00-doctrine/model-judgment-placement.md)
- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)

**Transition:** Once consequential uncertainty is produced inside execution, measurement is necessary but no longer the complete engineering contract.

**Closing claim:**

> The problem is not merely that AI is harder to test. Part of the controlled object's behavior is now produced through runtime judgment, and every decision that controls that object must account for the change.

**Working word budget:** 950–1,300

---

### 5.3 From Model Quality to Bounded Control

**Purpose:** Introduce the accepted Control-Loop Capability Anatomy, distinguish measurement, feedback closure, and bounded acceptable operation, and explain how governance becomes operational through the complete socio-technical control architecture.

**Core claim:** A measured system is not necessarily controlled, a closed feedback loop is not necessarily operating inside an approved boundary, and a Thinking System intended for production use is not ready for production release at the intended scope without a complete cross-level control architecture.

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
- Introduce the four logical capability families in the publication-facing pedagogical order **Actuators → Constraints and realizations → Sensors → Controllers**. State explicitly that this is a reading traversal of the closed control loop, not a mandatory execution order or physical stack:
  1. **Actuators and corrective action** execute authorized changes to operation or a Constraint Realization.
  2. **Constraints and their realizations** define and operationalize approved boundaries around those changes and the operating space.
  3. **Sensors and evidence** observe behavior, outcomes, conditions, realization state, Actuator execution, and control health.
  4. **Controllers and decision authority** compare or interpret evidence relative to approved Requirements, Constraints, and assumptions, then select or authorize the next action.
- Close the four-family explanation by making the loop explicit: Controller authorizes Actuator; Actuator changes operation or realization; Constraints bound legitimate change; Sensors expose resulting state and effects; evidence returns to Controller.
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
  - where an organizationally or project-level prohibited state can feasibly be made unreachable through deterministic enforcement, prefer deterministic realization over probabilistic influence;
  - when deterministic prevention is not feasible, do not label the boundary Hard merely because the intent is important; record the remaining uncertainty and evidence obligations explicitly;
  - prompts, natural-language policies, probabilistic evaluators, and model preferences are not hard by themselves;
  - different guarantee strengths require separate Constraint records.
- Use short anti-examples: telemetry without authority is observation; a Controller without an effective Actuator cannot correct; a declared policy without realization is not an operable boundary; nominal human review is not substantive Human Authority.
- Define **Controller** as a decision function rather than as a team, person, dashboard, or algorithm. At organizational, project, and delivery levels the Controller is commonly socio-technical: legitimate human decision authority combined with automated evidence collection, invariant checks, routing, decision support, and bounded automated decisions where delegation permits them. At runtime the proportion of automation may be greater, but automation does not create authority that was never delegated.
- State that automation should remove repetitive sensing, checking, routing, evidence aggregation, and safe bounded response wherever feasible without obscuring responsibility or silently expanding decision rights.
- State explicitly that AI governance is not a fifth capability family, a post-hoc checkpoint, or a document layered over the implementation.
- Explain that governance becomes operational through the complete socio-technical control architecture formed by the capability families across organizational, project / architecture, delivery, and runtime decision levels.
- State the release-readiness condition: until credible boundaries, evidence, authority, effective Actuators, Human Authority and fallback where needed, and reassessment paths exist, the application may be demonstrable or testable but is not ready for production release at the intended scope.
- Avoid UA-first formulations such as “UA asks” in this section; the capability anatomy must follow from the problem itself.

**Figures:**

- supporting figure — closed feedback loop;
- supporting figure — complete bounded control architecture showing the four capability families as logical functions, not services, layers, or one execution order. The figure may show the true relationship topology even though the prose introduces the families in Actuator-first pedagogical order.

**Repository anchors:**

- [`Control-Loop Capability Anatomy`](../../../00-doctrine/control-loop-anatomy.md)
- [`AI Control Plane`](../../../02-ai-control-plane/README.md)
- [`Constraint Capability Family`](../../../02-ai-control-plane/01-constraints/README.md)
- [`Constraint Realization Catalog`](../../../02-ai-control-plane/01-constraints/constraint-realization-catalog.md)
- [`Actuator Capabilities`](../../../02-ai-control-plane/00-actuators/README.md)
- [`Sensor and Evidence Capabilities`](../../../02-ai-control-plane/02-sensors/README.md)
- [`Controller and Decision Authority`](../../../02-ai-control-plane/03-controller/README.md)

**Transition:** Capability functions explain what bounded control requires, but not where project, release, runtime, and organizational decisions are owned or how those decision horizons interact through time.

**Closing claims:**

> A closed loop can still be unacceptable when it operates outside an approved, credibly realized, observable, and correctable boundary.

> Capability without legitimate decision ownership is not a complete control architecture.

> Governance becomes operational through the active socio-technical control architecture; without it, readiness for production release at the intended scope is incomplete.

**Working word budget:** 950–1,150

---

### 5.4 Four Decision Levels for Thinking Systems — the operating map

**Purpose:** Present the connected organizational, project / architecture, delivery, and runtime horizons as the conceptual and operational center of the paper. The section must explain not only where decisions are owned, but how each level becomes active, what enters it, what it decides, which control capabilities its decisions require, what it sends downward, what evidence returns upward, and how negative cases trigger reassessment and learning.

**Core claim:** Different control decisions require different evidence, authority, time horizons, automation, and corrective actions. Together, the four levels describe how one Thinking System is authorized, made viable, realized, released, operated, corrected, and reauthorized. They are not four documents or four meetings; they are connected decision horizons in one socio-technical control system.

#### Common operating-frame rule for all four levels

Each level subsection must use the same publication-facing logic while preserving level-specific meaning:

1. **Activation triggers** — what event, proposal, evidence, or change causes this level to act.
2. **Inputs and authoritative basis** — what information, Constraints, assumptions, dependencies, prior decisions, and evidence arrive here.
3. **Questions and decisions owned** — what this level may legitimately decide and what it may not decide.
4. **Capability obligations** — what Constraints, Sensors, Controllers, Actuators, Human Authority, fallback, and automation must exist or be required because of the decisions owned here.
5. **Outputs and artifacts** — what authorization, boundaries, delegated decision rights, evidence obligations, realization requirements, records, and versioned artifacts flow downward or become active.
6. **Evidence and change received** — what lower-level evidence, incidents, changed assumptions, capacity or economic findings, and authority-expansion requests return here.
7. **Local action versus escalation** — what may be repaired, narrowed, accepted, or rejected locally and what requires reassessment or reauthorization at another level.
8. **Learning and stabilization** — how negative cases improve the relevant Sensors, Constraints and realizations, Controllers, Actuators, assumptions, and decision rules rather than closing as isolated incidents.

The manuscript should make this common rhythm visible without mechanically repeating eight labels in every paragraph. A compact table may summarize the frame after the four detailed subsections if it improves navigation.

**Required framing before the level subsections:**

- State that the four levels are not four governance documents, four mandatory teams, or four approval meetings.
- Explain that they are the decision-ownership horizons through which governance becomes operational.
- State that production release at the intended scope requires the relevant capability functions and decisions to be connected across all four levels.
- Preserve the distinction that combining responsibilities in one person does not collapse the decisions.
- Explain that the same organization may implement Controllers at different levels using different mixtures of people and automation.
- Reuse the bold-labeled forward bridge from Section 5.2 as orientation, but do not repeat its full prose. The detailed treatment here is the canonical explanation of the four levels.

**Primary Figure 2 — Two orthogonal models**

Show two adjacent views. The **decision-ownership side must reproduce the four-horizon supporting figure from Section 5.2 verbatim**, not paraphrase it: use the same four horizon questions, the same Runtime evidence node, the same downward labels, and the same three direct reassessment routes with the same invalidated-decision-basis wording. This makes the earlier four-horizon figure a literal submodel of the orthogonal-model figure rather than a second competing representation.

```text
Decision ownership — verbatim reuse of the four-horizon model
Organization — What may be authorized?
→ Project / Architecture — Is the controlled system viable and authorizable?
→ Delivery — Is this bounded realization complete and releasable?
→ Runtime — Does active operation remain inside the authorized boundary?
→ Runtime evidence — behavior · outcomes · control state · changed assumptions

Runtime evidence → Delivery: implementation / realization / evidence issue
Runtime evidence → Project / Architecture: risk / authority / feasibility / capacity / economics invalidated
Runtime evidence → Organization: authoritative source / decision right / shared capability changed

Capability functions at every level — visually distinct control dimension
Actuators and corrective action
Constraints and realizations
Sensors and evidence
Controllers and decision authority
```

Use one restrained green semantic class for the capability-family side so the additional control-theory dimension is immediately distinguishable from the reused decision-horizon model. The green treatment identifies the orthogonal capability model, not a maturity state, safety claim, or execution sequence. The capability-family ordering is a reading aid consistent with Section 5.3; it must not be rendered as a directional pipeline. Use a neutral undirected structural rail or equivalent grouping to show that the four capability families form one control-capability model without implying causal sequence. The figure must show that all four capability families may appear at every decision horizon and must not imply one-to-one mapping, four mandatory services, or a one-way waterfall.

#### Organizational authorization and control context

**Primary question owned:** Should this business capability be implemented as a Thinking System at all, and if so, within what organizational authority, non-negotiable boundaries, shared capabilities, evidence obligations, and decision rights may a project proceed?

The manuscript may preserve the shorter orientation question **“What may be authorized?”** in figures. The detailed subsection must make clear that organizational control begins before project authorization and includes the option to prefer a deterministic solution, prohibit the proposed use, constrain it, or allow only bounded research.

**Activation triggers:**

- a new business capability, process problem, customer need, or product opportunity for which Model Judgment is proposed;
- a proposal to replace or augment a deterministic path with probabilistic Model Judgment;
- a proposed expansion of autonomy, delegated authority, deployment population, geography, data access, tool access, or downstream action capability;
- a new or changed legal, contractual, privacy, security, safety, procurement, vendor, geography, prohibited-use, incident, or shared-capability source;
- a Project Reauthorization request that cannot be resolved inside existing organizational authority;
- repeated delivery or runtime evidence showing that an organizational assumption, shared capability, decision right, or business rationale may no longer be valid.

**Inputs and authoritative basis:**

- business outcome sought and the value expected from the capability;
- available deterministic or less judgment-dependent alternatives where known;
- existing policies, contracts, legal obligations, security/privacy boundaries, procurement rules, customer commitments, geography and deployment restrictions, prohibited uses, incident obligations, and vendor constraints;
- existing shared organizational capabilities such as identity, authorization, audit, secrets management, logging, incident response, rollback/shutdown, data governance, model/vendor approval, and Human Authority capacity;
- existing exception authority and decision-right structures;
- evidence from prior related systems or prior incidents where material;
- project, delivery, or runtime evidence when the level is reactivated after initial authorization.

**Questions and decisions owned:**

- Is Model Judgment necessary for the intended outcome, or can the business capability be delivered credibly through deterministic software or a narrower deterministic path?
- What incremental value is expected from introducing probabilistic judgment, and which new uncertainty, control cost, authority, and consequences does that choice create?
- Is the use category acceptable to the organization at all?
- Which outcomes, actions, data uses, geographies, populations, vendors, or authority expansions are prohibited, conditionally allowed, or explicitly reserved to Human Authority?
- Which existing organizational sources are authoritative for this system and which take precedence when they conflict?
- Which organizational functions legitimately own decisions that may be affected by system behavior—for example product, engineering, architecture, operations, security, privacy, legal, compliance, procurement, finance, customer support, domain specialists, or executive authority?
- Which decisions may be delegated to Project, Delivery, or Runtime Controllers, and which remain reserved at organizational level?
- Which exceptions may be granted, by whom, using what evidence, for what scope and duration?
- Which shared capabilities are mandatory dependencies before Project Authorization can be credible?
- Which material evidence must lower levels be able to produce so organizational decision owners can know when a boundary or assumption they own is threatened or invalidated?
- Is the expected business value large enough to justify exploring a Thinking-System path once the likely control perimeter is considered, even though detailed control economics will be determined at Project / Architecture level?

**Capability obligations created by organizational authority:**

The organization does not merely name participating departments. If an organizational function has legitimate authority over a boundary or outcome, the downstream architecture must provide that decision owner with an operable control relationship.

For every material organizational boundary or reserved decision right, the article should establish the chain:

```text
authoritative source or organizational decision
→ scoped project Constraint or explicit project assumption
→ required Constraint Realization properties
→ Sensor / evidence obligation
→ Controller / decision owner and expected decision latency
→ available Actuator, escalation, exception, or reauthorization path
```

This does **not** mean Organization designs every technical Sensor or realization. It means Organization creates evidence and decision obligations that Project / Architecture must make realizable.

Where a prohibited state can feasibly be made unreachable through deterministic enforcement, Project / Architecture should prefer deterministic realization rather than probabilistic influence. An organizational statement is not a Hard Constraint merely because its source is authoritative. If deterministic prevention cannot be credibly realized for the relevant path, the system must not hide that uncertainty behind a Hard label.

**Controller composition at Organization level:**

- The organizational Controller is the legitimate decision function, not a committee by definition.
- It may be one accountable person, several existing functions, or an existing governance/management process.
- Human authority will usually dominate consequential organizational decisions, but sensing and decision support should be automated wherever useful: source/version tracking, policy checks, evidence aggregation, threshold detection, notification, routing, dependency-health signals, and preparation of exception or reauthorization context.
- Automation may help apply explicit delegated rules, but it must not invent authority, change a prohibited-use boundary, or silently accept residual risk outside delegation.

**Outputs and artifacts flowing downward:**

The level should produce or make explicit, by reference where possible:

- the organizational authorization status: prohibited, deterministic solution preferred/required, bounded research allowed, or eligible for Project / Architecture authorization;
- authoritative source references and the organizational assumptions relevant to the use case;
- prohibited or conditionally allowed outcomes, actions, authority, data use, populations, geographies, vendors, or deployment modes;
- reserved Human Authority and exception authority;
- delegated decision rights for Project, Delivery, and Runtime;
- mandatory shared-capability dependencies;
- organizational evidence obligations and escalation expectations;
- conditions that require return to organizational review.

Do **not** require a new standalone “UA Organization Document.” Existing sources and decision records should be linked rather than copied. In an SMB, several responsibility bundles may be held by the same people. These outputs may be represented inside the Project Control Architecture and Viability Review as linked authority, source, dependency, evidence, and escalation fields when that preserves clarity and ownership.

**Evidence and change received from lower levels:**

- Project finding that a required control cannot be realized credibly under the current organizational boundary;
- Project finding that control economics, latency, Human Authority capacity, vendor constraints, or shared-capability cost destroy the expected business case;
- requests to expand authority, autonomy, geography, data access, vendor choice, deployment mode, or reachable downstream actions;
- repeated or material runtime violations of an organizationally owned boundary;
- evidence that a shared organizational capability is unavailable, degraded, bypassable, or insufficient;
- evidence that the legal, contractual, customer, security, privacy, or business assumptions used for authorization changed;
- evidence that lower levels cannot produce the information required for the organizational decision owner to act credibly.

**Local action versus escalation:**

Organization may prohibit, authorize, condition, narrow, suspend, change a shared capability, redefine delegated authority, approve or reject an exception, or require Project Reauthorization. Runtime and Delivery may trigger organizational review; they do not perform it automatically. A lower-level workaround cannot normalize an organizationally prohibited state.

**Learning and stabilization:**

Negative cases affecting organizational decisions must not end with “incident closed.” They should ask whether:

- the authoritative source was ambiguous or inaccessible;
- decision rights were unclear;
- required evidence was missing, late, or too aggregated;
- a shared capability failed or was incorrectly assumed;
- an exception path encouraged authority drift;
- organizational Constraints were too broad, too vague, internally conflicting, or impossible to realize at the claimed strength;
- the original business case underestimated the control perimeter.

The resulting change may improve source clarity, delegated authority, evidence obligations, shared capabilities, exception handling, project-entry criteria, or the decision to use a Thinking System for similar cases.

**Supporting figure — Organizational control process across the lifecycle:** Replace the current department-centric influence map with a process-oriented figure showing:

```text
business capability / proposed Thinking-System use
+ authoritative organizational sources
+ shared capabilities and decision rights
+ project/runtime evidence or authority-change request
→ Organizational Controller / legitimate decision owners
→ decision:
   deterministic path / prohibit / bounded research / authorize within conditions
→ outputs downward:
   authoritative boundaries
   delegated decision rights
   shared-capability obligations
   evidence obligations
   organizational reassessment triggers
→ Project / Architecture

Project viability or authority request ───────→ Organization
Runtime evidence invalidating organizational basis ─→ Organization
```

The caption must state that the figure represents a decision horizon and evidence relationship, not a required department structure or sequential stage gate.

#### Project / architecture control and viability

**Primary question owned:** Does a credible, operable, and economically viable control architecture exist for this proposed Thinking System within the organizationally authorized boundary?

This is the level at which “AI is allowed in principle” becomes a concrete system authorization decision. A successful prototype is not Project Authorization.

**Activation triggers:**

- organizational eligibility or bounded research authorization for a proposed use;
- a material new use of Model Judgment inside an existing project;
- a new Judgment Node, changed authority path, model/tool/retrieval architecture, vendor, deployment mode, or material population expansion;
- delivery or runtime evidence that invalidates project risk, authority, feasibility, evidence, Human Authority capacity, control latency, shared-capability assumptions, or economics;
- a proposed authority expansion that remains within organizational policy but exceeds current Project Authorization.

**Inputs and authoritative basis:**

- intended business outcome and evidence that Model Judgment adds necessary or material value;
- organizational authorization, authoritative source references, prohibited states, reserved decisions, shared-capability dependencies, evidence obligations, and reassessment triggers;
- proposed system boundary, user population, data, models, tools, dependencies, downstream effects, and reachable authority;
- material scenarios, expected operating conditions, business assumptions, cost assumptions, and available Human Authority;
- relevant prior evidence, incidents, platform limitations, and known failure modes.

**Questions and decisions owned:**

- Is Model Judgment genuinely required for the intended outcome, or should the design use a deterministic or narrower judgment-dependent path?
- Where is Model Judgment placed and which Consequential Runtime Responsibilities depend on it?
- What authority and downstream consequences are reachable from each Judgment Node?
- Which material scenarios could move the system outside acceptable operation?
- What Requirement and Operating Envelope define success and acceptable operation?
- Which organizational boundaries become scoped project Constraints?
- Which complete Constraint Realization paths are credible, and at what guarantee strength?
- What evidence can detect loss of acceptable operation early enough for the consequence?
- Who or what owns each project-level decision and which authority can be delegated downward?
- Which Actuator can change operation when evidence requires action?
- Where is substantive Human Authority required, and is the required information, expertise, time, volume, and fallback capacity realistic?
- What happens when Sensors, realizations, models, tools, or Human Authority are unavailable or degraded?
- Can at least one credible complete control loop be described for every material scenario?
- Does the full control perimeter preserve technical, operational, and economic viability?
- Which assumptions or evidence changes require Project Reauthorization?

**Capability obligations:**

Project / Architecture translates risks and organizational decisions into a realizable control architecture. For each material scenario it must derive or identify:

- scoped Constraints and intended guarantee strength;
- candidate Constraint Realizations and complete paths;
- Sensors and evidence, including coverage, uncertainty, latency, and blind spots;
- Controller decisions, authority, and escalation boundaries;
- effective Actuator paths;
- Human Authority, fallback, containment, recovery, and fail-safe behavior where required;
- versioning, traceability, and assumptions needed to know what was actually authorized;
- evidence obligations needed by organizational decision owners.

**Control economics and viability:**

The business case must include the control perimeter rather than treating it as post-launch overhead. Include evaluation, observability, semantic review, Human Authority capacity, fallback, incident response, model and vendor dependencies, control maintenance, evidence retention, operational friction, latency, and expected correction cost.

The article must make the decision logic explicit:

```text
expected business value from Model Judgment
− model / platform / data cost
− control perimeter cost
− Human Authority and fallback cost
− expected operational friction and failure handling
→ viable enough to authorize, narrow, research, redesign, defer, or reject
```

This need not be a universal numerical formula. The point is architectural: if adequate control destroys the economics, the correct engineering outcome may be deterministic redesign, narrower scope, research, deferral, or No-Go.

**Controller composition at Project / Architecture level:**

The project Controller is commonly socio-technical. Architecture, product, engineering, risk/security/domain owners, finance or operations may contribute evidence and authority according to the decision. Automated tooling should gather model/evaluator evidence, verify invariants, compare versions, estimate capacity/cost, detect missing dependencies, and route deviations. Human decision owners remain accountable for decisions that require legitimate business, architectural, residual-risk, or authority judgment.

**Outputs and artifacts flowing downward:**

- Project Authorization status and authorized scope;
- one versioned **Project Constraint Architecture**;
- explicit Judgment Nodes and system/control boundary;
- Requirement and Operating Envelope;
- material scenarios and assumptions;
- required Constraint Realization properties and claimed strength;
- required Sensors/evidence and expected decision latency;
- Controller ownership and delegated authority;
- required Actuator paths;
- Human Authority, fallback, containment, and recovery requirements;
- required shared capabilities and dependencies;
- control economics baseline;
- reauthorization triggers;
- conditions under which Delivery may narrow, repair, or experiment without returning to Project.

The canonical living artifact is the **Project Control Architecture and Viability Review**, which owns the Project Constraint Architecture and authorization baseline. Additional financial, risk, or architecture records are optional when existing organizational practice requires them.

**Evidence and change received from Delivery / Runtime:**

- inability to realize a required Hard Constraint or evidence path;
- evidence coverage weaker than assumed;
- new reachable tool/action/data paths;
- drift or incidents that change scenario likelihood or consequence;
- Human Authority overload or unavailability;
- fallback saturation;
- control latency incompatible with the consequence;
- material model/vendor/platform changes;
- changed capacity or unit economics;
- repeated local defects indicating the architecture rather than one implementation is wrong;
- requested authority or scope expansion.

**Local action versus escalation:**

Project may authorize, narrow, condition, redesign, require more research, defer, or issue No-Go. Project may change its architecture within organizational authority. If the proposed change requires a new organizational boundary, reserved decision right, vendor/deployment permission, or shared capability outside existing authorization, Project must escalate to Organization.

**Learning and stabilization:**

Negative cases should test whether the project model of the controlled object was wrong: missing scenario, incorrect assumption, insufficient Constraint, non-credible Hard claim, poor Sensor coverage, wrong Controller authority, ineffective Actuator, unrealistic Human Authority capacity, or invalid economics. Repeated delivery/runtime workarounds are evidence that Project Authorization may need revision rather than more local tuning.

**Supporting figure — Project control architecture and viability:** Show:

```text
organizational authorization + intended outcome
→ need for Model Judgment / deterministic alternative check
→ material scenarios and reachable consequences
→ Project Constraint Architecture
→ credible complete control loops
→ Human Authority / fallback / recovery
+ control economics and capacity
→ authorize / narrow / bounded research / redesign / defer / No-Go

Delivery/runtime invalidating evidence → Project Reauthorization
Project need for wider authority → Organizational review
```

#### Designing the control architecture

This remains inside the Project / Architecture decision horizon and must not be presented as a fifth level.

**Required argument:**

- Translate material business and operational risks into a realizable control structure.
- Identify where Model Judgment is placed, what authority and consequences are reachable from each Judgment Node, which deterministic responsibilities must surround it, and which scenarios could produce unacceptable outcomes.
- Derive the required Constraints, candidate Constraint Realizations, Sensors, Controller decisions, Actuator paths, Human Authority, fallback, containment, recovery, and reassessment mechanisms.
- Distinguish machine-checkable or syntactic evidence from semantic or probabilistic evidence without creating new capability families.
- Machine-checkable evidence may verify schema, type, structure, permissions, tool arguments, state transitions, resource limits, and other deterministic conditions.
- Semantic evidence may estimate grounding, relevance, harmfulness, intent alignment, factual support, policy meaning, or downstream business acceptability.
- Semantic evidence must expose coverage, uncertainty, latency, and blind spots rather than being treated as an oracle.
- Treat Human Authority as part of the architecture where required, including information, decision right, time, expected volume, expertise, fatigue, escalation rights, unavailability, and overload.
- Prefer deterministic realization for prohibited states where technically feasible and do not upgrade a Soft guarantee to Hard because the business intent is important.
- Drive the design from the risks, authority, and consequences of the system rather than a generic control-component checklist.

#### Delivery realization and release

**Primary question owned:** Is this bounded realization complete, evidence-bearing, operationally supportable, and acceptable for a specific deployment context under Project Authorization?

**Activation triggers:**

- Project Authorization of a bounded implementation or experiment;
- a new feature, Judgment Node, model/prompt/context/retrieval/tool change, Constraint Realization change, evaluator change, or material configuration change;
- a new deployment population or environment inside existing Project Authorization;
- local runtime defect, realization degradation, or evidence issue that Delivery is authorized to repair;
- Project Reauthorization that changes the delivery baseline.

**Inputs and authoritative basis:**

- Project Authorization and current Project Constraint Architecture;
- inherited Constraints, assumptions, Judgment Nodes, evidence obligations, shared-capability dependencies, delegated authority, reauthorization triggers, and control economics baseline;
- implementation scope and deployment context;
- relevant historical defects, incidents, runtime evidence, and known failure modes.

**Questions and decisions owned:**

- Is the bounded work ready to begin under known authority and evidence conditions?
- Are all Judgment Nodes and deterministic responsibilities in scope explicit?
- Does every inherited and local Constraint have a concrete realization path or an explicit unresolved gap?
- Are claimed Hard paths complete and bypass-tested for the reviewed scope?
- Are Sensors/evaluators/telemetry operational, versioned, and sufficient for the decisions they feed?
- Are Controller decision boundaries and delegated authority explicit?
- Are Actuators, fallback, rollback, containment, and Human Authority paths operational and tested?
- Are failure/unavailable/degraded states explicit?
- Is implementation and evidence complete for the reviewed scope?
- Is release acceptable for the specific population, environment, model/configuration versions, residual exposure, capacity, and economics?
- Does any new evidence invalidate Project Authorization rather than only a local realization?

**Capability obligations:**

Delivery makes the project control architecture concrete. It must implement, configure, verify, and operate the required realizations, Sensors, bounded Controllers, Actuators, Human Authority interfaces, fallback, version records, and evidence paths. It must also ensure that material evidence can travel upward in a form usable by Project and Organization decision owners.

**Controller composition at Delivery level:**

Delivery Controllers combine explicit human release/engineering authority with automation. Automation should handle repeatable invariant checks, build/test/evaluation execution, evidence aggregation, traceability, drift/version detection, policy-as-code checks, blocked-action verification, release-condition checks, routing, and safe bounded actions. Human decision owners retain decisions that require contextual acceptance, architecture judgment, residual-risk acceptance, or authority change.

**Outputs and artifacts:**

- one living **Thinking System Review** for the bounded delivery scope;
- one canonical **Constraint Realization Map** referenced by Judgment Nodes, DoR, DoD, Release Gate, and runtime operation;
- Definition of Ready decision and evidence;
- implementation and bounded experiments inside delegated authority;
- Definition of Done decision and evidence completeness;
- deployment-specific Release Gate decision;
- active model, prompt, context/retrieval, tool, policy, evaluator, realization, and deployment versions where material;
- runtime Sensor/Actuator configuration and expected decision latency;
- known gaps and reauthorization/escalation triggers.

**Evidence and change received from Runtime:**

- local implementation or configuration defects;
- realization unavailable/degraded/bypassed signals;
- evaluator or telemetry gaps;
- drift or version mismatch;
- denied-action or failed-Actuator evidence;
- Human Authority overload;
- fallback saturation;
- incidents and complaints;
- unexpected cost/latency/capacity behavior;
- repeated local corrections indicating a project-level assumption is invalid.

**Local action versus escalation:**

Delivery may repair, reconfigure, roll back, narrow exposure, disable, or re-release within delegated authority. It may not silently expand project authority, weaken an inherited Hard Constraint, change an organizational prohibition, or normalize evidence that project viability has failed. Such evidence routes to Project Reauthorization or Organization according to the decision basis affected.

**Learning and stabilization:**

Every material negative case should ask which part of the delivery control architecture failed or was insufficient:

- missing or late Sensor;
- ambiguous or incomplete Constraint;
- incorrect, degraded, or bypassable Constraint Realization;
- Controller rule/authority/latency problem;
- ineffective or unavailable Actuator;
- weak Human Authority path;
- missing deterministic validation around Model Judgment;
- inadequate test/evaluation coverage;
- untracked version or configuration drift.

The fix should improve the weakest control element and the evidence that verifies it, not default to prompt tuning because the model produced the visible symptom.

**Supporting figure — Delivery translation and release loop:** Extend the current translation figure so it shows:

```text
Project Authorization + Constraints + evidence obligations
→ delivery translation and realization
→ implementation / evaluation / verification
→ DoR / DoD / Release Gate decisions
→ runtime deployment and evidence
→ local repair / rollback / narrow / re-release
   OR Project Reauthorization when the authorization basis is invalidated
```

Preserve the existing two-way business ↔ engineering translation claim inside this process.

#### Runtime operation, correction, and reassessment

**Primary question owned:** Does active operation remain inside the authorized Requirement, Constraint baseline, authority, capacity, and economics with required realizations active and healthy, and what response is authorized when it does not?

**Activation trigger:** Runtime is continuously active while the Thinking System operates. Specific Controller decisions are triggered by Sensor evidence, violations, drift, incidents, degraded control state, capacity/economic thresholds, authority failures, or scheduled reassessment conditions.

**Inputs and authoritative basis:**

- active authorized Project and Delivery baselines;
- deployment scope and active versions;
- delegated runtime authority;
- active Constraints and Constraint Realizations;
- Sensor/evidence definitions and interpretation boundaries;
- Controller rules and Human Authority responsibilities;
- available Actuators, fallback, containment, rollback, disable, and stop paths;
- expected decision latency and escalation routing.

**Questions and decisions owned:**

- Is the active controlled system operating inside the authorized boundary?
- Are required realizations active, healthy, and non-bypassed?
- Are model behavior, downstream outcomes, cost, latency, capacity, Human Authority, fallback, and control health inside acceptable conditions?
- Is the current evidence sufficient to make the runtime decision, or is Sensor validity itself degraded?
- Which local corrective action is authorized now?
- Did the Actuator actually produce the intended state?
- Has operation returned to a known authorized state, or has the basis of Project or organizational authorization been invalidated?
- What must be escalated, to whom, and with what evidence?

**Capability obligations:**

Runtime must operate the complete feedback path:

```text
active Thinking System / realizations
→ Sensors and evidence
→ Runtime Controller within delegated authority
→ Actuator / Human Authority / fallback
→ changed operation
→ Sensor verification of the resulting state
```

Monitoring must cover the socio-technical controlled system rather than only model output. Evidence may include model behavior, downstream outcomes, model/prompt/context/retrieval/tool versions, authorization failures, realization activation and bypass, evaluator results, drift, complaints, overrides, Human Authority capacity, fallback load, cost, latency, incidents, Actuator execution, and post-action verification.

**Controller composition at Runtime:**

Runtime should automate the control path as far as the consequence, evidence quality, and delegated authority permit. Deterministic checks, rate/permission boundaries, circuit breakers, routing, rollback, exposure narrowing, fallback selection, and well-defined invariant responses should not require humans merely for ceremony. Human Authority is required where interpretation, accountability, residual-risk acceptance, or reserved authority cannot be credibly automated. Automated runtime control remains bounded by delegated authority and may not reauthorize the project.

**Outputs and records:**

- active evidence and control-health state;
- runtime decisions and decision basis where material;
- Actuator execution and verification evidence;
- incidents, overrides, Human Authority decisions, fallback use, denied actions, and relevant outcomes;
- active version/configuration traceability;
- routed evidence packages for Delivery, Project, or Organization when the relevant basis is invalidated.

These are operational records, not necessarily a new standalone UA document.

**Evidence routing by invalidated decision basis:**

```text
local implementation, realization, configuration, or evidence issue
→ Delivery reassessment

project risk, authority, feasibility, evidence, Human Authority capacity, control latency, or economics changed
→ Project Reauthorization

authoritative source, decision right, prohibited-use boundary, approved vendor/deployment mode, or shared capability changed
→ Organizational review

proposed authority expansion
→ Project Reauthorization
→ Organizational review where the organizational boundary must change
```

**Local action versus escalation:**

Runtime may reject, contain, compensate, route to fallback, narrow exposure, roll back, disable, or stop within delegated authority. These actions may restore a previously authorized state. They do not authorize redesign, new authority, or a new business boundary. Persistent or repeated local recovery is evidence for reassessment when the underlying basis remains invalid.

**Learning and stabilization:**

Runtime negative cases are not only operational noise. Their analysis should improve the control system at the correct level. The review asks whether the case exposed:

- a missing Sensor or blind spot;
- a weak or mis-scoped Constraint;
- a degraded/bypassable realization;
- a Controller threshold, authority, or decision-latency problem;
- an ineffective Actuator;
- a Human Authority capacity problem;
- a project scenario or assumption that was wrong;
- an organizational boundary or shared capability that needs revision.

Repeated cases should become less frequent, earlier detectable, less consequential, cheaper to correct, or structurally impossible where deterministic prevention is feasible.

**Supporting figures:**

- runtime control and reassessment;
- evidence and change routing.

#### Cross-level operating discipline — measurement, learning, automation, and stabilization

This subsection is required after the four level descriptions. Its purpose is to state the practices that apply across the whole Nested Control Lifecycle without creating a fifth decision level.

**1. Measure for decisions, not for dashboards.**

Do not use “measure everything” literally. Every **material control claim and decision basis** should be observable enough for the Controller that owns it to decide within the consequence-relevant time horizon. Evidence should have a known consumer, decision boundary, expected latency, coverage, uncertainty, and blind spots. Telemetry with no decision path remains observation.

**2. Every material negative case gets an owning level.**

A negative case may be a violation, near miss, denied action, bad output, downstream harm, failed realization, Sensor blind spot, Actuator failure, Human Authority overload, fallback saturation, capacity/economic break, or evidence that an authorization assumption is false. It should route to the level that owns the affected decision basis rather than to the team that happened to observe it first.

**3. Analyze control failure, not only model failure.**

For each material negative case ask:

```text
Did the Sensor fail to observe or observe in time?
Did the Constraint fail to express the required boundary?
Did the Constraint Realization fail, degrade, or permit bypass?
Did the Controller have the wrong rule, evidence, authority, or latency?
Did the Actuator fail to execute or verify correction?
Did Human Authority lack information, time, capacity, or power?
Was the project scenario, assumption, or economics wrong?
Was the organizational source, decision right, or shared capability wrong or changed?
```

The visible model output is only one possible failure location.

**4. Improve the weakest control element and its evidence.**

Corrective learning may improve Sensors, Constraints, realizations, Controller logic, Actuators, Human Authority, fallback, assumptions, tests/evaluators, organizational sources, delegated authority, or project economics. The system should not treat repeated prompt adjustment as the default response to every negative case.

**5. Prefer deterministic prevention for prohibited states where feasible.**

When a prohibited state can credibly be made unreachable at an identity, permission, type, transaction, resource, tool, or execution boundary, prefer that deterministic enforcement and verify the full path. Do not claim Hard control where only probabilistic influence exists.

**6. Automate the control loop without automating authority into existence.**

Across all levels, automate repetitive sensing, evidence collection, invariant checking, routing, version comparison, alerting, decision support, and safe bounded Actuation where possible. Higher-level Controllers may remain predominantly human because the decisions involve business authority, ambiguity, residual exposure, or exceptions. Runtime Controllers may be predominantly automated. In every case, authority must be explicitly delegated before automation exercises it.

**7. Stabilization means reducing uncontrolled recurrence.**

The objective is not zero variance from Model Judgment. The objective is progressive reduction of uncontrolled or poorly understood failure modes. Over time, important negative cases should become one or more of:

- structurally prevented;
- detected earlier;
- routed to the correct Controller faster;
- corrected by a more reliable Actuator;
- cheaper to recover from;
- less consequential because exposure or authority is narrower;
- better represented in project scenarios and evidence obligations;
- reflected in revised organizational or project authorization where required.

**Supporting figure — Cross-level learning and stabilization loop:** Show negative case/evidence → owning decision level → diagnose Sensor/Constraint/Realization/Controller/Actuator/assumption weakness → change within authority or reauthorize upward → improved control architecture → runtime verification. The figure must not imply that every case escalates to Organization.

**Repository anchors for Section 5.4:**

- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
- [`Project Control Architecture and Viability Review`](../../../01-patterns/project-control-architecture-and-viability-review.md)
- [`Thinking System Review`](../../../01-patterns/thinking-system-review.md)
- [`Judgment Node Boundary`](../../../01-patterns/judgment-node-boundary.md)
- [`Control-Loop Capability Anatomy`](../../../00-doctrine/control-loop-anatomy.md)
- [`AI Control Plane`](../../../02-ai-control-plane/README.md)
- [`Failure Modes and Anti-Patterns`](../../../04-failure-modes/README.md)

**Transition:** Once each decision horizon is described as a living control process, the practical problem becomes preserving that chain without creating four parallel governance bureaucracies. The next section therefore reduces the operating model to a proportional artifact surface rather than introducing another conceptual layer.

**Closing claims:**

> Lower levels may refine and narrow a higher-level decision. They may not silently expand its authority or normalize evidence that invalidates it.

> A decision owner that receives no fit-for-purpose evidence is authority on paper, not an operational Controller.

> Negative cases should improve the control architecture at the level that owns the failed decision basis, not disappear into local incident closure.

**Working word budget:** 3,200–4,300 before final compression. Do not optimize this section back to the previous 1,800–2,300-word target until the operating model is fully expressed and reviewed.

---

### 5.5 From Authority to Operation: Two Living Reviews

**Purpose:** Explain how the detailed four-level operating model can remain practical without reproducing one process document per level. This section owns the proportional artifact surface, not the conceptual definition of the levels.

**Core claim:** The decisions are richer than the documents required to carry them. For many SMB contexts the model can preserve one living project review and one living delivery review, linked to existing organizational sources and runtime evidence, without collapsing decision ownership.

**Canonical path:**

```text
existing organizational sources, shared capabilities, delegated decision rights, and evidence obligations
→ one living Project Control Architecture and Viability Review
→ one versioned Project Constraint Architecture and authorization
→ one living Thinking System Review per bounded delivery scope
→ one canonical Constraint Realization Map
→ deployment-specific Release Gate
→ active runtime versions, evidence, decisions, and actions
→ delivery reassessment, Project Reauthorization, or organizational review
→ learning updates the owning decision basis and control elements
```

**Required content:**

- Artifacts follow decisions; they do not create authority merely by existing.
- Constraint authority flows downward by reference; policy prose is not copied as if it were a complete technical control.
- Project-level Constraints are interpreted or derived, scoped, and connected to required realization, assumptions, evidence, authority, economics, inheritance, and reauthorization.
- Delivery makes realization concrete through active mechanisms, configuration, verification, failure behavior, evidence, change authority, and release scope.
- Runtime preserves material source, project, delivery, realization, model, prompt, policy, tool, and deployment versions.
- Judgment Nodes, DoR, DoD, Release Gate, and runtime sections reference the same Constraint Realization Map rather than creating parallel records.
- Organizational outputs such as authoritative source references, delegated rights, evidence obligations, shared-capability dependencies, and reassessment triggers may be carried by reference inside the Project Review rather than requiring a separate UA organization document.
- Runtime evidence, decisions, and actions are operational records rather than a mandatory third living review.
- Additional registers, RACIs, gate files, financial models, or committees remain optional when independent ownership, lifecycle, access, retention, regulation, or audit needs justify them.
- Two living reviews are the proportional default, not a universal sufficiency claim.
- One person may carry several responsibility bundles without collapsing the decisions.
- The article should distinguish **decision process**, **canonical artifacts**, and **implementation tooling** so that readers do not confuse the four decision levels with four forms or four software services.

**Required figure:** Show existing organizational sources and decision rights above the two living reviews, the Project Constraint Architecture and Constraint Realization Map as the two canonical Constraint artifacts, deployment-specific release below, active runtime evidence beneath it, and return routes to delivery, project, or organization according to the basis invalidated. Include a small learning loop showing that repeated negative cases can modify the relevant control element or authorization basis.

**Repository anchors:**

- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
- [`Project Review Template`](../../../01-patterns/project-control-architecture-and-viability-review-template.md)
- [`Thinking System Review Template`](../../../01-patterns/thinking-system-review-template.md)
- [`Judgment Node Boundary`](../../../01-patterns/judgment-node-boundary.md)

**Transition:** An illustrative Constraint trace can make the consequences concrete without pretending that the repository already contains independent evidence for a complete two-level application.

**Closing claim:**

> The goal is not to document everything repeatedly. It is to preserve the chain from authoritative source to scoped Constraint, concrete realization, runtime evidence, corrective decision, and learning.

**Working word budget:** 650–850

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
- The organizational decision also creates evidence obligations: lower levels must be able to show that model-mediated identities cannot send, that denied-send attempts are visible, that the human-operated send path remains distinct, and that any request for autonomous sending returns for reauthorization.
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

1. **Local realization defect** — a configuration mismatch is detected before an unauthorized send path becomes reachable. Delivery fails closed, repairs the realization, verifies the complete path, and passes a new Release Gate. The case also checks whether Sensor coverage or realization verification should improve so the same defect is detected earlier.
2. **Project assumption invalidated** — review volume and latency make the control perimeter economically non-viable at planned scale. `K-SEND-01` remains valid, but project capacity and economics do not. Project Reauthorization narrows, redesigns, defers, or rejects the path.
3. **Organizational evidence obligation triggered** — repeated denied-send attempts reveal an unexpected alternate integration path. The runtime system blocks the action, Delivery contains the local path, and Project reassesses whether the architecture covers all reachable send paths. Organization is informed if the evidence changes an organizationally owned assumption or shared capability rather than merely the implementation.
4. **Separate authority-change request** — the business requests autonomous sending. This is not runtime evidence or delivery tuning. It requires Project Reauthorization and organizational review before any new realization is designed.

**Primary Figure 3 — K-SEND-01 Constraint trace**

```text
organizational prohibition + reserved Human Authority + evidence obligation
→ Project Constraint K-SEND-01
→ delivery Constraint Realization Map
→ runtime evidence
   ├─ local defect → delivery reassessment + control improvement
   ├─ capacity/economics invalidated → Project Reauthorization
   └─ organizational basis invalidated → organizational review

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

**Working word budget:** 750–950

---

### 5.7 What Platforms Can Implement — and What Authority They Do Not Acquire by Default

**Purpose:** Address productization without dismissing agent, governance, observability, or AI-native delivery platforms.

**Core claim:** A platform may implement multiple control capabilities and may exercise explicitly delegated Controller authority, but hosting or automating those capabilities does not create organizational or project authority.

**Required content:**

- Classify platform functions by what they do in the specific system, not by market category.
- A platform may host or implement Constraint Realizations, Sensors and evidence, bounded automated Controller logic, human decision interfaces, Actuators, version records, and decision records.
- A platform may automate evidence collection, invariant checks, routing, decision support, and bounded Actuation across several levels where authority has been explicitly delegated.
- A platform does not independently determine whether Model Judgment is necessary, which source is authoritative, what consequences or authority are acceptable, who may accept residual risk, whether Human Authority is substantive, whether the control perimeter preserves viability, or when Project or organizational authorization must change.
- A platform may execute delegated authority. It does not create that authority.
- Avoid the categorical claim that platforms “cannot solve governance.” State the narrower ownership and delegation boundary.
- Verify named-platform claims against current first-party documentation. Prefer functional, vendor-neutral framing when a named comparison is unnecessary.

**Required figure:** Show implementable platform functions inside delegated authority and organizational/project decisions outside the platform's default mandate. The figure may show automation spanning Sensors, Controller logic, and Actuators without implying that the platform owns the source of authority.

**Repository anchors:**

- [`Control-Loop Capability Anatomy`](../../../00-doctrine/control-loop-anatomy.md)
- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
- [`AI Control Plane`](../../../02-ai-control-plane/README.md)
- [`Specification`](../../../SPECIFICATION.md)

**Transition:** The ownership boundary explains why the resulting model is developed as an open specification rather than one privileged implementation.

**Closing claim:**

> A platform can make control capabilities easier to implement and may exercise delegated decision logic. It does not, by default, authorize the project or define the organizational boundary in which that implementation is legitimate.

**Working word budget:** 450–600

---

### 5.8 From Thinking Systems to Uncertainty Architecture

**Purpose:** Introduce UA only after the engineering model has been derived, then state repository scope, current maturity, limits, and invitation.

**Core claim:** Uncertainty Architecture is the open draft specification that organizes the derived responsibilities for Thinking Systems; it is coherent enough to inspect and test but lacks sufficient independent application evidence for a maturity claim.

**Required content:**

- Explicitly connect the preceding deduction to UA without implying that the deduction proves UA uniquely correct.
- Explain the name: architecture for locating, bounding, observing, deciding about, correcting, and reassessing consequential uncertainty across a socio-technical system.
- Present the four capability families, four operating decision levels, two living reviews, Constraint trace, and cross-level learning/stabilization loop as the current specification spine.
- Explain tool neutrality and the separation between capability and authority.
- Present the article itself as a publication-facing **working paper / open engineering map under validation**, not as evidence that the specification is mature. “White paper” may be used only if publication context benefits from the term and the maturity caveat remains explicit; avoid vendor-whitepaper tone.

**Intellectual context, antecedents, and novelty boundary:**

- Keep the publication-facing treatment compact rather than turning Section 8 into a literature review.
- State explicitly that UA is a synthesis and recomposition rather than an invention of closed-loop control, systems thinking, socio-technical safety, runtime assurance, ML-systems engineering, software engineering for AI, or AI risk management from first principles.
- State that UA does not claim coinage of the phrase **Thinking Systems**; its claim is the UA-specific engineering definition and boundary assigned to the term.
- Use a compact comparison that gives each major adjacent tradition one clear contribution and one clear boundary relative to UA:
  - **STAMP/STPA** — socio-technical systems safety, safety constraints, hierarchical control, and feedback;
  - **Simplex** — runtime assurance, trusted safety paths, and fallback around complex behavior;
  - **production ML / software engineering for AI** — system-level technical debt, changed engineering practices, testing, maintenance, and lifecycle concerns;
  - **NIST AI RMF** — AI risk management spanning organizational governance and system-specific lifecycle activities.
- Explain why UA remains a distinct proposed entity without claiming exhaustive absence across the literature: the cited sources address important slices of the problem but do not by themselves provide the same combination of Thinking-System category, cross-level authority, delivery realization and release, runtime correction and reassessment, and an explicit operating map for routing evidence and learning across those decisions.
- State the integration claim positively: UA treats the whole Thinking System as the controlled object and connects organizational authorization, project / architecture viability, delivery realization and release, and runtime evidence, correction, reassessment, and learning around that same object.
- Describe the relationship as conceptual continuity, comparison, and recomposition—not equivalence, endorsement, proof that UA is correct, or a claim that UA was derived from any single prior framework.
- Do not claim novelty for Constraints, Sensors, Controllers, Actuators, feedback loops, fallback, socio-technical control, AI risk management, or the observation that AI changes software engineering; do not turn a bounded comparison of cited sources into an exhaustive claim about the entire field.
- Preserve the more detailed provenance and research positioning in `content/research/index.md`; the article should summarize it rather than duplicate it.
- State evidence maturity explicitly: UA is a draft systems-engineering hypothesis/open specification under validation, not a mature empirical standard. Distinguish repository rigor from evidence of framework correctness.
- Name the next validation threshold: worked reference implementations, real project decision/release/reassessment traces, negative-case learning and control-improvement traces, cross-project comparison, and documented revision or falsification when evidence contradicts doctrine.

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
- validated evidence that the proposed negative-case learning loop improves stability across real systems;
- universal threshold derivation;
- proof that teams can apply UA correctly without author involvement;
- evidence that current terminology and boundaries will survive sustained external use unchanged.

**Why open:** Enable independent critique and contradictory evidence, compare application across domains, prevent vendor or author capture of the control language, preserve visible evolution, and support many implementations.

**Licensing:** Documentation and specification material use CC BY 4.0; code and reference implementations use Apache 2.0 where present.

**Validation request:** Ask for documented applications, anonymized reviews, contradictory cases, terminology issues, simplification proposals, platform mappings, control-cost evidence, Human Authority failures, negative-case learning traces, Sensor/Constraint/Controller/Actuator failure examples, and operational failure modes.

**Required final figure:** A compact map:

```text
Thinking-System problem
→ bounded control capabilities
→ four connected operating decision horizons
→ two living reviews + canonical Constraint artifacts + runtime evidence
→ correction / reassessment / reauthorization
→ negative-case learning and stabilization
→ Uncertainty Architecture open specification
```

It may synthesize earlier figures but must introduce no new doctrine.

**Repository anchors:**

- [`README.md`](../../../README.md)
- [`SPECIFICATION.md`](../../../SPECIFICATION.md)
- [`ROADMAP.md`](../../../ROADMAP.md)
- [`CONTRIBUTING.md`](../../../CONTRIBUTING.md)
- [`Research Track`](../index.md)

**Closing claim:**

> Uncertainty Architecture is coherent enough to be tested, not mature enough to be protected from criticism. The next step is external application, contradictory evidence, negative-case learning traces, and revision.

**Working word budget:** 650–850

## 6. Figure contract

The three primary architectural figures are:

1. **Controlled-object shift** — two vertical top-to-bottom responsibility diagrams placed side by side, with restrained red treatment on the changed responsibility blocks in the Thinking System column.
2. **Two orthogonal models** — the decision side reproduces the four-horizon decision model verbatim, including Runtime evidence and the same reassessment routes, while a visually distinct green capability-family side shows Actuators, Constraints and realizations, Sensors and evidence, and Controllers and decision authority as functions that may appear at every horizon. The green ordering is a reading aid, not an execution pipeline or one-to-one mapping. An undirected rail or equivalent structural grouping may connect the capability blocks to show one model without implying causal sequence.
3. **K-SEND-01 Constraint trace** — illustrative source-to-runtime path with delivery reassessment, Project Reauthorization, organizational evidence obligations, negative-case control improvement, and separate authority expansion.

Supporting figures currently expected:

- engineering responses around dominant uncertainty, labeled Plan-driven engineering (Waterfall), Iterative delivery (Agile and related approaches), Modern operations (DevOps), and Thinking-System engineering;
- Thinking Systems category boundary;
- Model Judgment placement, with Model Judgment above and the three placement categories in one horizontal row beneath it;
- connected uncertainty locations;
- one controlled object across four decision horizons, with all four horizon blocks centered in one vertical line, one Runtime evidence node beneath them, and direct return routes to the level whose decision basis is invalidated; reassessment criteria belong on those routes rather than in a separate lane of component-like boxes;
- closed feedback loop;
- complete bounded control architecture;
- **organizational control process across the lifecycle** — business capability + authoritative sources + lower-level evidence → legitimate organizational Controller → deterministic/prohibit/research/authorize decision → boundaries, delegated rights, shared-capability obligations, evidence obligations, and reassessment triggers flowing to Project / Architecture; return routes from Project and Runtime where the organizational basis is challenged;
- project control architecture and viability including AI-necessity/deterministic-alternative check and control economics;
- delivery translation and release loop;
- runtime control and reassessment;
- evidence and change routing;
- **cross-level learning and stabilization loop** — negative case → owning level → diagnose Sensor/Constraint/Realization/Controller/Actuator/assumption weakness → local change or reauthorization → improved control → runtime verification;
- two living reviews operating surface;
- platform capability and authority boundary;
- final Thinking Systems-to-UA synthesis including learning/stabilization.

Supporting figures are not capped. They must materially strengthen comprehension, introduce no new doctrine, remain consistent with owning repository sources, carry explicit non-prescriptive captions, and remain subordinate to the primary figures.

Do not use the presentation's brain/nerves/skeleton/muscles stack as the canonical article architecture diagram. It may be mentioned as source history only.

## 7. Terminology and claim-safety rules

Use current terms: Thinking System, Linear Software, Model Judgment, Judgment Node, Constraint, Constraint Realization, Hard Constraint, Soft Constraint, Sensor, Controller, Actuator, Human Authority, Project Constraint Architecture, Constraint Realization Map, Nested Control Lifecycle, Project Authorization, Project Reauthorization, DoR, DoD, and Release Gate.

Treat Behavioral Software, Behavioral Applications, fixed specialist role titles, universal maturity ladders, universal thresholds, and the old three-part Actuator/Sensor/Controller model as historical or contextual only.

Do not:

- equate Thinking Systems with agentic applications;
- imply that fixed, sequential, or explicitly orchestrated workflows cannot be Thinking Systems when at least one **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment;
- use an agent label, dynamic control flow, autonomy level, or existing control completeness as a substitute for the Thinking System category test;
- imply that a poorly controlled or pre-production system is not a Thinking System merely because Constraints, evidence, decision rights, or corrective mechanisms are incomplete;
- imply that **Thinking** asserts consciousness, sentience, human-like cognition, or an anthropomorphic theory of model behavior;
- imply that the Thinking System category begins only after agentic, multi-agent, dynamic, or high-autonomy capabilities appear;
- imply that a non-agentic application cannot be a Thinking System;
- call a prompt, natural-language policy, probabilistic evaluator, classifier, or model preference a Hard Constraint by itself;
- call a schema, permission check, or other realization a Constraint without distinguishing the authoritative Constraint from its realization;
- describe an organizationally important prohibition as Hard unless the complete scoped realized path actually supports the deterministic claim;
- describe Actuators as defining policy or authorizing their own changes;
- collapse evaluator, gate decision, and release execution;
- equate Controller with a team, a dashboard, or an algorithm; Controller means the decision function and legitimate authority, which may be socio-technical and partially automated;
- imply that automation creates authority that was not delegated;
- equate closed feedback with acceptable bounded operation;
- describe governance as a post-hoc review, policy document, compliance artifact, fifth capability family, or exact synonym for every element of the control architecture;
- imply that governance can become operational without the relevant socio-technical control architecture;
- imply that a Thinking System can be ready for production release at the intended scope while its required cross-level control architecture remains incomplete;
- imply that control-architecture design creates a fifth decision level separate from project / architecture;
- use red visual emphasis in Figure 3 to imply that the entire Thinking System is probabilistic, unsafe, or erroneous;
- imply runtime reauthorizes a project automatically;
- classify every deviation as a Bug;
- describe aggregate quality, cost, latency, or capacity tolerances as Hard Constraints without deterministic enforcement;
- imply that every negative case must escalate to Organization; route by invalidated decision basis;
- imply that every negative case is a model-quality failure; analyze the complete control architecture;
- use “measure everything” as a literal requirement; material evidence must be tied to decision ownership and latency;
- present the illustrative K-SEND-01 trace as independent application evidence;
- use internal UA documents as evidence for current external standards, laws, products, or market practice;
- introduce UA as the premise that validates the early engineering argument;
- claim that UA invented generic control-loop primitives, systems-theoretic safety, runtime assurance, ML-systems engineering, or AI risk management;
- claim that UA coined the phrase **Thinking Systems** itself rather than defining a specific engineering meaning for it;
- present STAMP/STPA, Simplex, NIST AI RMF, or other antecedents as equivalent to UA, as endorsements of UA, or as evidence that UA is uniquely correct.

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

Status and ownership still apply within this set. The paper may derive an explanatory sequence and publication-facing operating model, but it must not override the specification, glossary, or owning source. New operating-model formulations discovered in the article remain research until separately reconciled into authority-bearing repository material.

### Supporting repository sources

- [`Constraint Realization Catalog`](../../../02-ai-control-plane/01-constraints/constraint-realization-catalog.md) — informative implementation examples.
- [`Worked Support-Triage Review`](../../../03-reference-architectures/worked-thinking-system-review-support-triage.md) — illustrative delivery-level reference.
- [`Failure Modes and Anti-Patterns`](../../../04-failure-modes/README.md) — reusable loss-of-control mechanisms according to document status.
- [`ROADMAP.md`](../../../ROADMAP.md) — current project state and open validation work.

Historical articles, talks, presentation material, and research may provide provenance and evidence. They must not override authority-bearing framework sources.

### External evidence

Current factual claims about standards, laws, platform capabilities, market practice, or the state of AI governance must be checked against current primary or authoritative sources. Named platform capabilities must be checked against first-party documentation. Comparative claims should be narrow, dated, and should not imply exhaustive market coverage.

Primary antecedent and comparison sources currently expected for Section 5.8:

- Nancy G. Leveson, *Engineering a Safer World* / STAMP: https://mitpress.mit.edu/9780262016629/engineering-a-safer-world/
- Software Engineering Institute, *An Architectural Description of the Simplex Architecture*: https://www.sei.cmu.edu/library/an-architectural-description-of-the-simplex-architecture/
- Sculley et al., *Hidden Technical Debt in Machine Learning Systems*: https://research.google/pubs/hidden-technical-debt-in-machine-learning-systems/
- NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
- ISO/IEC TR 29119-11:2020, *Guidelines on the testing of AI-based systems*: https://www.iso.org/standard/79016.html
- Amershi et al., *Software Engineering for Machine Learning: A Case Study* (ICSE 2019): https://www.microsoft.com/en-us/research/publication/software-engineering-for-machine-learning-a-case-study/
- Martínez-Fernández et al., *Software Engineering for AI-Based Systems: A Survey* (TOSEM 2022): https://doi.org/10.1145/3487043

Use these to establish intellectual context, terminology scope, maturity, and comparison boundaries, not to imply direct derivation, endorsement, or equivalence.

## 9. Publication framing

### Working title

**Uncertainty Architecture: Engineering Thinking Systems with Consequential Runtime Responsibilities**

The title begins with **Uncertainty Architecture** for attribution and discoverability, while the article body delays full framework introduction until the engineering model has been derived.

### Publication identity

Treat the repository edition as an **open engineering working paper / architecture working paper under validation**. This framing fits the article's purpose: define the problem space, propose an operating map and practices, expose assumptions, and invite external review and contradictory cases. “White paper” is acceptable as a distribution label only when the maturity caveat is preserved and the presentation does not imply a vendor product claim, final standard, or validated industry consensus.

### Target length

The working manuscript may exceed the earlier 4,300–5,200-word target while the argument is still being constructed. Preserve the argument during section drafting; perform one integrated reduction pass only after all eight sections exist.

Expected working range after the expanded operating-model section: **8,000–10,500 English words** before final editorial compression.

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
- [ ] Plan-driven development, iterative delivery, and modern operations remain the primary categories, with Waterfall, Agile and related approaches, and DevOps named consistently as familiar examples in the opening prose, Figure 1, and the comparison table.
- [ ] The abstract does not narrate the article's reveal sequence or contain internal editorial commentary.
- [ ] Governance is framed as becoming operational through the active socio-technical control architecture rather than as a post-hoc review, document, or exact synonym for every control element.
- [ ] The consequence of an incomplete cross-level control architecture is explicit, scoped to readiness for production release at the intended scope, and visually emphasized once as a central engineering thesis without duplicating the argument.
- [ ] Figure 3 places two vertical top-to-bottom responsibility diagrams side by side and uses restrained red treatment on the changed Thinking System blocks without implying that the entire system is probabilistic.
- [ ] Figure 4 places Model Judgment above Input Interpretation, Decision Logic, and Output Mediation, with the three placements aligned horizontally and no implied mandatory sequence.
- [ ] Figure 6 keeps Organization, Project / Architecture, Delivery, and Runtime in one centered vertical spine, preserves concise downward inheritance labels, places one Runtime evidence node beneath Runtime, and routes invalidating evidence directly back to the owning decision level with the invalidated basis on the return edge rather than in a separate reassessment subsystem.
- [ ] Figure 9 reproduces Figure 6's decision-horizon model verbatim—including horizon questions, Runtime evidence, downward inheritance labels, and reassessment-route wording—and adds the orthogonal capability-family dimension as a visually distinct green group with undirected structural grouping and no implied one-to-one mapping or execution pipeline.
- [ ] Section 3 introduces the capability families in Actuator → Constraint/Realization → Sensor → Controller pedagogical order and explicitly distinguishes that reading sequence from execution order.
- [ ] Section 3 defines Controller as a decision function that may combine legitimate human authority with automation and states that automation does not create undelegated authority.
- [ ] Hard Constraint discussion prefers deterministic prevention where feasible but does not claim Hard strength when the complete scoped realized path remains probabilistic.
- [ ] The decision-horizon bridge uses short bold-labeled paragraphs and keeps control-architecture design inside the project / architecture level.
- [ ] Section 4 treats all four levels as operating processes through time, not only static ownership descriptions.
- [ ] Each decision level explicitly covers activation triggers, inputs/authority basis, owned decisions, capability obligations, outputs/artifacts, evidence received, local action versus escalation, and learning/stabilization.
- [ ] Organizational control asks whether a Thinking-System solution should exist at all and permits deterministic solution, prohibition, bounded research, conditional authorization, or Project / Architecture entry as distinct outcomes.
- [ ] Organizational decision owners create downstream evidence obligations when they own a material boundary or outcome; the article connects authoritative source → scoped Constraint/assumption → realization requirement → Sensor/evidence → Controller → Actuator/escalation.
- [ ] Organizational control does not become a mandatory new department, committee, or standalone UA document; existing sources and roles may carry the authority.
- [ ] Project / Architecture explicitly re-tests the need for Model Judgment, includes the complete control perimeter in viability, and allows authorize/narrow/research/redesign/defer/No-Go outcomes.
- [ ] Delivery clearly distinguishes inherited Project Authorization, concrete realization, DoR, DoD, Release Gate, local repair, and Project Reauthorization.
- [ ] Runtime distinguishes restoration of an authorized state from redesign or reauthorization and verifies that Actuator execution produced the intended state.
- [ ] The cross-level operating discipline ties material evidence to an owning decision and does not use “measure everything” as a literal telemetry requirement.
- [ ] Every material negative case is analyzed against the complete control architecture—Sensor, Constraint, Constraint Realization, Controller, Actuator, Human Authority, assumptions, and economics—not only model quality.
- [ ] The learning loop routes negative cases to the level whose decision basis they invalidate and does not imply that every case escalates to Organization.
- [ ] Stabilization is framed as reducing uncontrolled recurrence through prevention, earlier detection, faster routing, more reliable correction, narrower exposure, cheaper recovery, or revised authorization rather than eliminating all probabilistic variance.
- [ ] Every major new argument has an appropriate figure or an explicit reason why prose is clearer.
- [ ] Organizational Figure 10 is process-oriented rather than a department influence map and shows both downward obligations and return evidence/reauthorization routes.
- [ ] A supporting cross-level learning/stabilization figure exists if the prose alone does not make negative-case routing and control improvement obvious.
- [ ] All figures were reviewed as one visual sequence and renumbered consistently.
- [ ] The complete target article was reread after integration.
- [ ] This blueprint was updated after the target article review.
- [ ] Section purposes, required content, transitions, claims, examples, and known risks remain detailed rather than compressed.
- [ ] UA is not introduced as the premise of the early engineering argument.
- [ ] Thinking-System category identity is separated from control adequacy; **Consequential Runtime Responsibility** is implementation-neutral, has an operational material-effect test, and is explicitly distinguished from risk severity; Figure 2 classifies by whether such a responsibility depends partly on probabilistic Model Judgment and shows orchestration topology, autonomy, and delegated authority as independent dimensions.
- [ ] **Thinking** is explicitly functional and non-anthropomorphic, with no claim about consciousness or human-like cognition.
- [ ] Section 8 acknowledges established antecedents and intellectual context, distinguishes conceptual continuity from equivalence or direct derivation, and scopes UA's proposed contribution without claiming novelty for generic control-loop or socio-technical safety primitives.
- [ ] The article explains why broader labels such as AI-based system do not provide the narrower consequential-responsibility boundary and does not claim that UA discovered the broader SE-for-AI problem space.
- [ ] Evidence maturity is explicit: repository rigor is not empirical validation, and the next validation threshold is practical application, failure/correction traces, negative-case learning traces, cross-project comparison, and revision under contradictory evidence.
- [ ] Decision levels and capability families remain orthogonal.
- [ ] Constraint and Constraint Realization remain distinct.
- [ ] Project Authorization, DoR, DoD, Release Gate, runtime correction, and Project Reauthorization remain separate.
- [ ] Project Constraint Architecture and Constraint Realization Map remain the two canonical Constraint artifacts.
- [ ] Runtime evidence and proposed authority changes are not conflated.
- [ ] Platform implementation and decision authority remain separate.
- [ ] Illustrative material is not presented as independent validation.
- [ ] Source authority, external-evidence rules, maturity boundaries, and publication framing remain accurate.
