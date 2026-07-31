---
title: Operational Protocol for AI Contributors
artifact_type: repository-guide
status: informative
maturity: active
module: repository
topics:
  - repository-architecture
  - navigation
  - terminology
  - provenance
  - contribution-workflow
  - thinking-systems
  - control-loop
  - constraints
  - sdlc
  - human-authority
tags:
  - ua/module/repository
  - ua/type/repository-guide
  - ua/status/informative
  - ua/topic/repository-architecture
  - ua/topic/navigation
  - ua/topic/terminology
  - ua/topic/thinking-systems
  - ua/topic/control-loop
  - ua/topic/constraints
canonical_for:
  - ai-agent-repository-guide
---

# Operational Protocol for AI Contributors

## 1. Purpose and scope

This file defines how language models, coding agents, automated reviewers, and other AI-assisted contributors should work inside the Uncertainty Architecture (UA) repository.

It is operational guidance, not part of the normative UA specification. It must not override [`SPECIFICATION.md`](SPECIFICATION.md), explicit document status, a module boundary, or a canonical definition in [`00-doctrine/glossary.md`](00-doctrine/glossary.md).

Use this file to determine:

- what to read before editing;
- where a contribution belongs;
- which source has authority;
- which control level owns a decision;
- which control capability is being defined, implemented, or failed;
- what information and Constraints are inherited between organizational, project, delivery, and runtime work;
- how evidence should trigger local correction or higher-level reassessment;
- how to preserve terminology, provenance, history, and research state;
- how to finish a session without conceptual, structural, constraint, or documentation drift.

## 2. Repository mission

UA is an open doctrine and pattern language for building and operating software in which part of the system's behavior is delegated to non-deterministic Model Judgment while the surrounding system remains deterministic, inspectable, constrained, and governable.

The repository exists to evolve an open engineering specification for **Thinking Systems** at the AI–code boundary.

UA begins from a controlled-object shift: uncertainty does not exist only in product assumptions, requirements, users, infrastructure, or deployment environments. A Thinking System may produce consequential uncertainty inside the operating system through runtime Model Judgment.

UA is:

- a shared architectural language;
- a doctrine for deterministic responsibilities, probabilistic judgment, explicit Constraints, evidence, decision rights, and corrective action;
- a pattern system for project authorization, delivery review, constraint realization, containment, evaluation, escalation, fallback, rollback, correction, and reauthorization;
- a control-oriented approach to model-mediated software across organizational, project, delivery, and runtime levels;
- a tool-neutral specification that evolves through research and implementation evidence.

UA is not:

- an SDK or universal agent framework;
- a prompt-template or guardrail collection;
- a vendor-specific architecture;
- a mandatory four-service topology;
- a single policy, evaluation, or observability method;
- a replacement for product discovery, Agile, DevOps, QA, security, change management, or incident response;
- a compliance certification;
- a claim that uncertainty can be eliminated.

## 3. Two orthogonal models

Before changing framework material, identify both the **decision level** and the **capability function**. Do not collapse them.

### 3.1 Four decision levels

The [`Nested Control Lifecycle`](00-doctrine/nested-control-lifecycle.md) defines where decisions are owned:

1. organizational control context;
2. project control architecture and viability;
3. delivery-level Thinking System Review;
4. runtime control and reauthorization.

### 3.2 Four control capabilities

The [`Control-Loop Capability Anatomy`](00-doctrine/control-loop-anatomy.md) defines which functions make control operational:

1. **Constraints** — define or enforce the allowed operating space;
2. **Sensors and evidence** — make behavior, outcomes, conditions, violations, and control health observable;
3. **Controllers and decision authority** — interpret evidence and authorize decisions;
4. **Actuators and corrective action** — execute authorized changes to behavior or operating conditions.

These capabilities are logical functions, not mandatory components. One tool may perform several functions, and one function may be distributed across code, infrastructure, workflows, and Human Authority.

A tool name does not determine capability classification. Identify the function, guarantee, evidence, authority, and corrective path.

## 4. Four-level UA control context

### 4.1 Organizational control context

This level owns authoritative Constraints, shared capabilities, and decision rights that apply across projects, such as:

- prohibited uses and risk appetite;
- legal, privacy, security, safety, contractual, procurement, residency, and financial Constraints;
- approved vendors, models, deployment modes, geographies, and data classes;
- shared identity, constraint-enforcement, audit, evaluation, observability, incident, fallback, and shutdown capabilities;
- available Human Authority and escalation rights;
- exception and organizational constraint-change authority.

UA does not require one policy, committee, or governance department to own all of this context. Existing organizational sources remain authoritative and should be linked rather than duplicated.

### 4.2 Project control architecture and viability

This level decides whether a proposed Thinking System has a credible, operable, and economically viable control architecture.

The canonical pattern is the [`Project Control Architecture and Viability Review`](01-patterns/project-control-architecture-and-viability-review.md). Its informative working representation is the [`project review template`](01-patterns/project-control-architecture-and-viability-review-template.md).

The project review owns:

- the intended business outcome and AI necessity;
- material risk and consequence scenarios;
- the intended Judgment, autonomy, and authority landscape;
- interpretation of organizational Constraints;
- derivation of project-specific Constraints;
- deterministic invariants and prohibited authority;
- required Constraint, Sensor, Controller, Actuator, Human Authority, fallback, containment, rollback, compensation, and shutdown capabilities;
- evidence feasibility and feedback latency;
- Human Authority and operational capacity;
- constraint and control build, run, review, fallback, and incident cost;
- project authorization, limitation, bounded research, redesign, escalation, deferral, or No-Go;
- the versioned authorization and constraint baseline inherited by delivery reviews;
- project reauthorization triggers.

### 4.3 Delivery-level review

This level decides whether a bounded whole system, feature, or material change is ready, complete, and acceptable for a stated deployment context.

The canonical pattern is the [`Thinking System Review`](01-patterns/thinking-system-review.md). Its informative working representation is the [`delivery review template`](01-patterns/thinking-system-review-template.md).

The delivery review owns:

- implementation-level Judgment Nodes;
- the applicable Requirement and Operating Envelope;
- local realization of inherited and delivery-specific Constraints;
- configuration, enforcement point, failure behavior, evidence, and local change authority;
- the model-mediated Definition of Ready;
- bounded experimentation or implementation;
- the model-mediated Definition of Done;
- the deployment-specific Release Gate;
- local runtime reassessment.

“Delivery level” describes the decision layer, not the size of the work item. A delivery review may cover a bounded whole system, feature, or material change.

### 4.4 Runtime control and reauthorization

This level exercises constraint enforcement, produces and interprets operational evidence, executes authorized corrective action, and determines whether evidence remains local or invalidates a higher-level decision.

Runtime may:

- enforce active Constraints and preserve their versions;
- observe behavior, outcomes, violations, bypass attempts, degradation, false blocks, fallback load, and control health;
- route evidence to a Controller with decision authority;
- invoke available Actuators within delegated authority;
- trigger local delivery correction, containment, rollback, or a new Release Gate;
- require project reauthorization because risk, Constraint feasibility, authority, capacity, evidence, or economics changed;
- require organizational review because an authoritative Constraint, decision right, or shared capability changed.

Do not force every runtime issue upward. Do not keep project-invalidating evidence trapped inside one delivery review.

### 4.5 Canonical ownership and inheritance rule

Use this ownership model:

```text
Organizational sources
→ Project Control Architecture and Viability Review
→ Thinking System Review
→ Runtime enforcement, evidence, and corrective action
```

Information should flow downward by reference:

- organizational Constraints, capabilities, and decision rights constrain the project;
- the project review interprets those sources, derives project Constraints, and creates a versioned authorization and inheritance package;
- delivery reviews link the project version and record concrete constraint realization;
- runtime records link active constraint, delivery, project, and organizational source versions.

Evidence should flow upward when it invalidates a decision basis:

- local implementation, configuration, enforcement, or evidence issue → delivery reassessment;
- project risk, Constraint feasibility, authority, capacity, evidence, or economic assumption changed → project reauthorization;
- authoritative Constraint, policy, decision right, or shared capability changed → organizational review.

Do not duplicate the complete project risk map, constraint architecture, control economics, or organizational policy in every delivery record. Do not allow a delivery review to silently expand authority, autonomy, population, data, domain, geography, deployment, tool access, or consequence level. Do not allow local implementation to weaken an inherited hard Constraint.

## 5. Mental model for AI contributors

Think like a systems architect working on an evolving engineering specification, not like a framework developer optimizing one implementation.

Prefer:

- control level and decision ownership before document creation;
- capability function before tool classification;
- system boundaries over isolated components;
- responsibilities over job titles;
- authoritative Constraint sources over copied policy prose;
- invariants over implementation preferences;
- scenario-to-constraint-and-control reasoning over aggregate risk scores;
- reusable distinctions over project-specific vocabulary;
- evidence over confident generalization;
- inheritance and cross-references over duplicated records;
- refinement over unnecessary expansion;
- complete control loops over locally impressive tools.

When reviewing a proposed control structure, identify:

1. which of the four decision levels owns the question;
2. where Model Judgment occurs or is expected to occur;
3. which decisions, actions, outputs, resources, states, data, tools, or parties it can affect;
4. which authoritative and locally derived Constraints apply;
5. what subject and scope each material Constraint bounds;
6. whether each material Constraint is hard or soft;
7. where and how each material Constraint is realized or enforced;
8. what happens when enforcement is unavailable, uncertain, bypassed, conflicting, or violated;
9. what evidence makes behavior, outcomes, constraint state, and control health observable;
10. who or what interprets that evidence;
11. which decision authority may change behavior or a Constraint;
12. which Constraint changes are local and which require delivery reassessment, project reauthorization, or organizational review;
13. which Actuators and corrective actions are available;
14. how fallback, escalation, containment, rollback, compensation, or shutdown works;
15. which assumptions and decisions are inherited from a higher level;
16. which evidence would require reassessment at a higher level;
17. whether the complete control system is technically, operationally, and economically viable.

## 6. Authority and conflict resolution

When documents appear to conflict, do not resolve the conflict by recency, popularity, file location, external visibility, or confidence of wording.

Use this order:

1. [`SPECIFICATION.md`](SPECIFICATION.md) for specification scope, status vocabulary, conformance, and change control.
2. Explicit document status and normative language.
3. The relevant module README for module purpose and boundaries.
4. [`00-doctrine/glossary.md`](00-doctrine/glossary.md) for current meanings of terms it defines.
5. Current doctrine, including [`control-loop-anatomy.md`](00-doctrine/control-loop-anatomy.md) and [`nested-control-lifecycle.md`](00-doctrine/nested-control-lifecycle.md), for architectural meaning.
6. The owning pattern for its decision surface: project review or delivery review.
7. The relevant AI Control Plane capability area for capability-specific meaning.
8. [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) for metadata and tags.
9. Research, history, talks, external references, templates, implementations, and examples for evidence and context, not automatic requirements.
10. This file for agent behavior and repository workflow only.

Additional rules:

- Explicit status takes precedence over directory name.
- `Normative` content takes precedence over conflicting lower-status material.
- `Draft normative` content must not be presented as stable.
- Maturity does not replace status.
- Templates mirror patterns and do not create independent protocols.
- A technology catalog is informative and does not prescribe a vendor or tool.
- Research, talks, implementations, citations, or benchmarks do not become doctrine by implication.
- Report genuine contradictions instead of silently choosing one side.

## 7. Repository invariants

1. Every canonical concept should have one authoritative definition.
2. The glossary is the terminology source for terms it defines.
3. Doctrine defines foundational distinctions; lower-level modules must not silently redefine them.
4. The Control-Loop Capability Anatomy owns the relationship among Constraints, Sensors, Controllers, and Actuators.
5. Constraints are a first-class capability, not merely examples inside Actuators.
6. An Actuator may change a Constraint within delegated authority; technical configurability does not create authority.
7. Patterns describe reusable responses; they do not create local doctrine.
8. The project review owns project viability, constraint architecture, authorization, inheritance, and reauthorization; the delivery review owns concrete realization, DoR, DoD, release, and local reassessment.
9. A lower-level review may narrow but must not silently weaken or expand a higher-level authorization or hard Constraint.
10. AI Control Plane documents define logical capabilities, not one mandatory product topology.
11. A component may realize several capability functions; classification follows function, guarantee, evidence, authority, and corrective path.
12. Reference architectures compose concepts and patterns; they do not become mandatory by example.
13. Failure modes describe reusable mechanisms of loss of control, not unrelated product defects.
14. Research provides evidence and framework candidates; it is not automatically specification.
15. Historical material preserves what was said and when.
16. Raw snapshots remain source evidence and must not be normalized in place.
17. One material type should have one canonical namespace.
18. Navigation and publishing infrastructure must not become a second specification.
19. Metadata, tags, recency, and search ranking do not create authority.
20. Repository growth should occur through coherent refinement, not fragmentation.
21. Higher-level decisions and Constraints should be inherited by reference rather than copied into every lower-level artifact.
22. Lower-level evidence must trigger higher-level reassessment when it invalidates a higher-level assumption, Constraint, capability, authority, or economic decision.
23. Every notable repository or specification-artifact change must remain visible in [`CHANGELOG.md`](CHANGELOG.md).

## 8. Canonical repository map and placement rules

### 8.1 Public entry points

- [`README.md`](README.md) — public landing page and reader navigation.
- [`SPECIFICATION.md`](SPECIFICATION.md) — specification boundary, status model, conformance, and change control.
- [`ROADMAP.md`](ROADMAP.md) — development sequence and planned artifacts.
- [`CHANGELOG.md`](CHANGELOG.md) — canonical record of notable repository and specification-artifact changes.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution and review workflow.
- [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) — metadata and controlled tags.
- [`AGENTS.md`](AGENTS.md) — this operational protocol.

### 8.2 `00-doctrine/`

Purpose: foundational concepts, distinctions, boundaries, and canonical vocabulary.

Place material here when it defines or materially refines:

- Thinking Systems and the controlled-object shift;
- organizational, project, delivery, and runtime decision levels;
- Constraints, Sensors, Controllers, and Actuators as logical capability classes;
- the relationship between capability anatomy and the Nested Control Lifecycle;
- Deterministic Core, Model Judgment, and Uncertainty Boundary;
- Invariants, Constraint, Constraint Realization, Requirement, Operating Envelope, Correctness, Bug, and Human Authority;
- control-oriented first principles.

Do not place here:

- detailed project or delivery review checklists;
- vendor recipes or product comparisons;
- isolated implementation examples;
- raw research notes;
- historical records;
- patterns that only apply existing doctrine.

A doctrine change must be checked against the glossary, project and delivery patterns, AI Control Plane, reference architectures, failure modes, module indexes, research traceability, roadmap, and changelog.

### 8.3 `01-patterns/`

Purpose: reusable technical and socio-technical responses to recurring control problems.

The module owns three connected boundaries:

- [`Project Control Architecture and Viability Review`](01-patterns/project-control-architecture-and-viability-review.md) — project risk, constraint architecture, capability feasibility, capacity, economics, authorization, inheritance, and reauthorization;
- [`Judgment Node Boundary`](01-patterns/judgment-node-boundary.md) — constrained, observable, operable boundaries around consequential Model Judgment;
- [`Thinking System Review`](01-patterns/thinking-system-review.md) — delivery-level constraint realization, DoR, bounded experiment, DoD, Release Gate, and local reassessment.

A pattern should make visible:

- context and recurring problem;
- failure mechanism;
- relevant Constraints and deterministic responsibilities;
- Constraint, Sensor, Controller, and Actuator functions;
- artifacts, responsibilities, economics, and decision rights;
- evidence, failure handling, and reassessment;
- consequences, limitations, and non-prescription.

Do not promote a one-off implementation into a pattern without a reusable problem and response. Do not duplicate project-level and delivery-level ownership merely because both discuss Constraints, evidence, authority, controls, or reassessment.

### 8.4 `02-ai-control-plane/`

Purpose: capabilities required to bound, observe, decide, and correct model-mediated behavior.

Canonical capability areas:

- [`00-actuators/`](02-ai-control-plane/00-actuators/) — mechanisms that execute authorized change;
- [`01-constraints/`](02-ai-control-plane/01-constraints/) — conditions and enforcement mechanisms that bound the reachable operating space;
- [`02-sensors/`](02-ai-control-plane/02-sensors/) — evidence about behavior, outcomes, constraints, drift, and control health;
- [`03-controller/`](02-ai-control-plane/03-controller/) — interpretation, decision authority, constraint-change authority, and corrective decisions.

The informative [`constraint-realization-catalog.md`](02-ai-control-plane/01-constraints/constraint-realization-catalog.md) may name schemas, types, policy engines, permissions, sandboxes, budgets, HITL mechanisms, and other examples. Named tools do not become requirements.

Telemetry without decision authority and corrective action is observation, not control. A declared Constraint without realization, failure behavior, evidence, and authority is not an operable boundary.

### 8.5 `03-reference-architectures/`

Purpose: concrete, non-prescriptive compositions showing how UA concepts and patterns may be applied.

Reference architectures may combine doctrine, project and delivery patterns, Constraints, Sensors, Controllers, Actuators, technical artifacts, technologies, roles, economics, and processes.

A reference should classify functions rather than products and distinguish specification requirements from illustrative choices. A two-level worked application should show constraint inheritance, delivery realization, runtime evidence, and reauthorization without creating duplicate canonical records.

### 8.6 `04-failure-modes/`

Purpose: recurring mechanisms by which Thinking Systems lose structural, semantic, operational, economic, or organizational control.

A failure mode should describe:

- triggering conditions and mechanism;
- affected decision level;
- failed or missing Constraint, Sensor, Controller, Actuator, authority, or connection;
- observable signals and evidence limits;
- consequences and propagation;
- containment, mitigation, recovery, delivery reassessment, project reauthorization, or organizational review;
- capacity and economic effects where material.

An isolated undesirable output is not automatically a reusable failure mode.

### 8.7 `content/research/`

Purpose: research publications, notes, analysis, synthesis, critique, provenance, and research-to-framework traceability.

Research informs explicit framework decisions. It does not update doctrine or patterns by implication.

### 8.8 `content/history/`

Purpose: project chronology, public discussions, talks, external references, recognition, and superseded records.

Preserve historical wording and distinguish citation, recommendation, implementation, adoption, certification, and endorsement.

### 8.9 `content/raw/`

Purpose: preserved source snapshots.

Do not paraphrase, modernize, normalize, or overwrite them in place.

### 8.10 Publishing and infrastructure

- `content/index.md` is a publishing portal, not a second specification entry point.
- `quartz/`, Node configuration, and `vercel.json` are publishing infrastructure.
- `assets/` contains diagrams and visual references.

Infrastructure behavior is not a UA requirement unless a specification document says so.

## 9. Canonical terminology

The canonical vocabulary is maintained in [`00-doctrine/glossary.md`](00-doctrine/glossary.md).

Before introducing, redefining, replacing, deprecating, or narrowing a UA term:

1. read the glossary;
2. search for existing uses and near-synonyms;
3. identify the owning module and decision level;
4. determine whether the distinction is necessary and stable;
5. update the glossary in the same change when canonical meaning changes.

Do not:

- create a second glossary;
- define canonical terms locally inside patterns, templates, or reference architectures;
- use Constraint, Invariant, Requirement, boundary, guardrail, policy, and Actuator interchangeably;
- invent synonyms for style;
- add vendor vocabulary, temporary labels, section headings, or one-off phrases as canonical terms;
- treat memorable phrases or product categories as glossary concepts without a durable architectural distinction.

### 9.1 Terminology migration

Use **Thinking Systems** in current framework material.

Preserve **Behavioral Software** and **Behavioral Applications** in historical titles, quotations, preserved source bodies, raw snapshots, and provenance records.

When current documentation first connects old and new language, it may use:

> **Thinking Systems** (previously described as **Behavioral Software** or **Behavioral Applications**)

Agentic systems are a higher-autonomy subset of Thinking Systems, not a synonym for the whole category.

## 10. Editing rules

### 10.1 Preserve concept and decision ownership

- One concept, one canonical definition, one owning module.
- One decision surface, one owning pattern.
- Prefer links and inherited versions over duplicated explanations and records.
- Refine the owning document instead of creating a competing source.
- Do not reconcile inconsistency by adding another overlapping document.

### 10.2 Preserve project, delivery, and runtime boundaries

Project review and delivery review intentionally overlap in vocabulary but not in decision ownership.

Project-level material may include organizational Constraint interpretation, project-specific constraint architecture, Judgment landscape, risk scenarios, required capabilities, evidence feasibility, capacity, economics, authorization, inheritance, and reauthorization.

Delivery-level material may include inherited constraint references, local realization, configuration, enforcement, Judgment Nodes, Requirement and Operating Envelope, DoR, implementation or experiment evidence, DoD, release scope, residual risk, and local reassessment.

Runtime material may include active versions, enforcement state, violations, bypass attempts, control health, Controller decisions, Actuator execution, and evidence routing.

When a delivery review needs project context, link the project version and identify inherited fields. Do not copy the complete project review.

When delivery or runtime evidence invalidates the project baseline, update or reauthorize the project review. Do not hide the contradiction in a local exception.

### 10.3 Apply the Constraint test

When creating or reviewing a Constraint, answer:

1. What is the authoritative source or project-risk rationale?
2. What behavior, state, authority, data, context, tool, output, resource, environment, deployment, or human decision does it bound?
3. What is its scope?
4. Is it hard or soft?
5. Where is it realized or enforced?
6. What does it guarantee, and what does it not guarantee?
7. What happens when enforcement is unavailable, uncertain, bypassed, conflicting, or violated?
8. What evidence shows activation, violations, degradation, false blocks, and operational friction?
9. Who may propose, approve, execute, override, or disable a change?
10. Which Actuator can implement the authorized change?
11. Which Controller owns the decision?
12. Which change remains local, which requires delivery reassessment, which requires project reauthorization, and which requires organizational review?

If these questions cannot be answered, preserve the item as a research candidate, unresolved dependency, or soft influence rather than presenting it as an operable hard boundary.

### 10.4 Separate capability from topology and tool

- Do not assume one service per capability.
- Do not classify a tool by product category alone.
- Identify the capability function performed in the specific system.
- State when one component realizes several functions.
- State when one function is distributed across technical and human mechanisms.
- Preserve the difference between a constraint declaration, its realization, its evidence, the Controller decision, and the Actuator action.

### 10.5 Separate specification from evidence and examples

- Research is evidence and analysis; doctrine is explicit synthesis.
- Reference architectures demonstrate compositions; they do not establish mandatory topology.
- Templates implement patterns; they do not create independent conformance paths.
- Named technologies are examples, not requirements.
- Example thresholds are not universal requirements.
- Role names are not automatically mandatory job titles.
- Talks, articles, benchmarks, citations, and implementations do not update the specification by implication.

### 10.6 Classify socio-technical framework content explicitly

Use these classes:

- **Concept or definition** — foundational distinction or canonical meaning; normally doctrine and possibly glossary.
- **Artifact** — maintained object expressing intent, evidence, policy, state, or control.
- **Role or responsibility bundle** — decision rights, ownership, competence, and authority.
- **Process or ritual** — repeatable sequence through which evidence is reviewed and corrective action is authorized.
- **Technical reference artifact** — illustrative schema, interface, manifest, data model, evaluator contract, policy example, repository layout, or implementation example.
- **Pattern** — reusable arrangement of artifacts, responsibilities, processes, economics, and technical mechanisms.
- **Failure mode** — reusable mechanism by which control is lost or becomes ineffective.
- **Reference architecture** — context-specific composition of several of the above.

Do not create a new top-level repository namespace for these classes merely because the classification exists. Place each item in the module that owns its architectural meaning.

### 10.7 Avoid false precision

Do not introduce universal numerical thresholds for quality, hallucination, drift, latency, cost, autonomy, confidence, Golden Scenario count, review frequency, risk, expected value, or Constraint effectiveness without a context- and consequence-derived basis.

Do not allow one aggregate risk score or expected-value number to override a hard prohibition, unacceptable consequence, missing Constraint, unavailable control, or non-substantive Human Authority.

### 10.8 Preserve uncertainty

When evidence conflicts or a concept remains incomplete:

- state the uncertainty;
- preserve relevant alternatives;
- identify the unresolved decision and owning level;
- avoid language stronger than the evidence supports.

### 10.9 Keep links, metadata, inheritance, and change records coherent

- Use repository-relative links.
- Link to canonical module indexes and owning patterns rather than duplicating document lists.
- Planned artifacts belong in `ROADMAP.md` until created.
- Follow `DOCUMENT-METADATA.md`.
- Preserve provenance when moving or superseding content.
- Preserve project, delivery, and active constraint versions when runtime evidence changes the current state.
- Update `CHANGELOG.md` in the same branch and pull request for every notable repository or specification-artifact change.

## 11. Task-specific reading paths

### 11.1 Understanding UA

Read in this order:

1. `README.md`;
2. `SPECIFICATION.md`;
3. `00-doctrine/uncertainty-in-the-controlled-object.md`;
4. `00-doctrine/control-loop-anatomy.md`;
5. `00-doctrine/nested-control-lifecycle.md`;
6. `00-doctrine/README.md`;
7. the complete glossary;
8. `01-patterns/project-control-architecture-and-viability-review.md`;
9. `01-patterns/thinking-system-review.md`;
10. the relevant AI Control Plane, reference architecture, failure mode, or research source.

### 11.2 Editing doctrine or terminology

1. Read `SPECIFICATION.md`.
2. Read relevant doctrine and its module index.
3. Read the complete glossary.
4. Search all uses and near-synonyms.
5. Identify downstream impact across all four decision levels and four capabilities.
6. Update glossary, indexes, links, research traceability, roadmap, and changelog when affected.
7. State compatibility, supersession, and unresolved uncertainty.

### 11.3 Editing the Control-Loop Capability Anatomy

Read:

- `00-doctrine/control-loop-anatomy.md`;
- `00-doctrine/nested-control-lifecycle.md`;
- `00-doctrine/glossary.md`;
- `02-ai-control-plane/README.md` and all four capability areas;
- project and delivery patterns and templates;
- reference architectures;
- failure modes;
- source-intake and framework traceability for the motivating research.

Check that the change:

- preserves Constraints, Sensors, Controllers, and Actuators as logical functions;
- does not create a mandatory physical stack;
- does not classify tools by name;
- preserves decision-level ownership;
- updates all affected diagrams and navigation.

### 11.4 Editing Constraints

Read:

- `00-doctrine/control-loop-anatomy.md`;
- the Constraint and related glossary entries;
- `02-ai-control-plane/01-constraints/README.md`;
- the realization catalog when implementation examples matter;
- project and delivery review patterns and templates;
- relevant reference architectures and failure modes.

Apply the complete Constraint test in section 10.3. Distinguish the approved Constraint from the mechanism, Sensor, Controller, and Actuator around it.

### 11.5 Proposing or changing the project review

Read:

- `00-doctrine/uncertainty-in-the-controlled-object.md`;
- `00-doctrine/control-loop-anatomy.md`;
- `00-doctrine/nested-control-lifecycle.md`;
- `01-patterns/project-control-architecture-and-viability-review.md` and template;
- `01-patterns/thinking-system-review.md`;
- `02-ai-control-plane/README.md` and `01-constraints/`;
- relevant research traceability and failure modes.

Check that the change concerns project viability, constraint architecture, authorization, inheritance, or reauthorization; does not duplicate full DoR, DoD, or Release Gate; connects risk scenarios to all four capabilities, Human Authority, capacity, and economics; preserves No-Go and non-AI alternatives; and remains proportional for SMB use.

### 11.6 Proposing or changing a delivery pattern

Read relevant doctrine, the project review and inheritance rules, the Constraint capability, glossary terms, overlapping patterns, and failure modes. Identify which project Constraints are inherited, which local details the delivery pattern owns, and which evidence may force project reauthorization.

### 11.7 Editing the AI Control Plane

Identify:

- the capability function being changed;
- Constraint source, subject, scope, strength, realization, failure behavior, evidence, and authority where relevant;
- Sensor decision-usefulness and latency;
- Controller decision right and escalation boundary;
- Actuator effect and failure behavior;
- affected decision level;
- the behavior that can actually be changed, contained, compensated, or stopped.

### 11.8 Editing a reference architecture

Read relevant doctrine, project and delivery patterns, and AI Control Plane documents. State context, assumptions, risk, autonomy, reversibility, organizational and project Constraints, delivery realization, Sensors, Controller, Actuators, project baseline, release scope, economics, and reauthorization path. Separate required content from illustrative design choices.

### 11.9 Editing a failure mode

Identify the reusable mechanism, not only the symptom. Distinguish deterministic defects, model-mediated violations, missing or failed Constraints, Sensor failures, Controller failures, Actuator failures, invalid assumptions, control-capacity failure, economic non-viability, and the decision level where the failure becomes material.

### 11.10 Working with research or source extraction

Start with [`content/research/index.md`](content/research/index.md). Use [`content/research/review-process.md`](content/research/review-process.md) and [`content/research/framework-traceability.md`](content/research/framework-traceability.md).

For each extracted entity:

1. state the source and original claim;
2. classify it as concept, artifact, role/responsibility, process, technical reference artifact, pattern, failure mode, or reference architecture;
3. identify the owning module, decision level, and capability function;
4. decide whether it is normative, draft normative, informative, reference, research, or historical;
5. check glossary impact;
6. identify dependencies, inheritance, constraint realization, reauthorization, and cross-references;
7. update the changelog when the repository changes.

#### Research reconciliation trigger

After a source-derived framework change, worked application, incident, or operational observation, check whether the work:

- registers or materially reinterprets a source;
- resolves, narrows, rejects, supersedes, or reopens a research question;
- promotes a candidate into doctrine, a pattern, a capability, a failure mode, an artifact, or a reference architecture;
- changes the relationship between existing research and the current framework;
- changes which decision level owns a decision or how Constraints and information are inherited and realized.

When any trigger applies, review the owning research note or source-intake record, `framework-traceability.md`, affected open questions or maturity, and research navigation when direction changed. Update only records whose state actually changed.

### 11.11 Working with history

Start with `content/history/README.md`. Preserve source meaning and distinguish visibility from validation, adoption, certification, or endorsement.

## 12. Contribution workflow for AI-assisted changes

For repository-changing work:

1. **Understand** — identify the architectural purpose and document class.
2. **Identify the decision level** — organizational, project, delivery, runtime, or a deliberate connection between them.
3. **Identify the capability function** — Constraint, Sensor, Controller, Actuator, or another explicit concept.
4. **Locate ownership** — identify the module, owning doctrine or pattern, and existing authoritative record.
5. **Read dependencies** — follow the relevant reading path.
6. **Search before creating** — check terms, patterns, documents, capability areas, review surfaces, and overlapping claims.
7. **Classify the entity** — concept, artifact, responsibility, process, technical reference artifact, pattern, failure mode, or reference architecture.
8. **Assess authority** — verify status, maturity, module boundaries, normative language, and decision rights.
9. **Check Constraint semantics** — source, scope, strength, realization, failure, evidence, and change authority.
10. **Check inheritance** — identify what is linked from a higher level and what evidence may require upward reassessment.
11. **Make the smallest coherent change** — prefer one reviewable architectural decision.
12. **Cross-reference** — connect doctrine, project and delivery patterns, capabilities, evidence, failure modes, and history.
13. **Check terminology** — compare UA-specific wording with the glossary.
14. **Update the changelog** — record every notable repository or specification-artifact change under `[Unreleased]` in the same branch and pull request.
15. **Reconcile research state when triggered** — update only affected intake, note, analysis, traceability, or navigation.
16. **Check repository integrity** — verify metadata, navigation, provenance, status boundaries, ownership, capabilities, inheritance, and links.
17. **Report uncertainty** — disclose contradictions, assumptions, evidence gaps, and unresolved decisions.
18. **Finish the session protocol** — complete the checks below.

Substantial framework changes should use a branch and pull request under [`CONTRIBUTING.md`](CONTRIBUTING.md).

## 13. End-of-session repository integrity protocol

### 13.1 Placement, level, and capability review

- Is each file in the correct module or namespace?
- Is the owning decision level explicit?
- Is the capability function explicit?
- Does the change have one clear architectural purpose?
- Could an existing canonical document have been refined?
- Was a new namespace introduced without a repository decision?
- Was a logical capability accidentally presented as a physical service?

### 13.2 Authority and status review

- Does status match the document's actual role and language?
- Is draft material clearly marked?
- Did lower-status material accidentally create a normative claim?
- Does the change conflict with `SPECIFICATION.md`, doctrine, a module boundary, or an owning pattern?
- Did a template, reference, technology catalog, or source presentation become a second protocol?

### 13.3 Constraint review

- Is the authoritative source or project rationale explicit?
- Are subject, scope, and hard or soft strength explicit?
- Is realization or enforcement separated from the Constraint itself?
- Is failure, bypass, conflict, and unavailability behavior explicit?
- Is evidence about activation, violations, degradation, and friction available?
- Are Controller and change, override, or exception authority explicit?
- Is an Actuator available for authorized corrective change?
- Does a lower-level component silently relax a higher-level boundary?
- Are delivery, project, and organizational reassessment triggers explicit?

### 13.4 Review ownership and inheritance review

- Is project viability, constraint architecture, or authorization owned by the project review?
- Are concrete realization, DoR, DoD, release, and local reassessment owned by the delivery review?
- Are organizational sources linked rather than copied?
- Does the delivery artifact identify the inherited project and constraint versions?
- Did a lower-level change silently expand authority or scope or weaken a hard Constraint?
- Are upward reassessment triggers explicit when evidence invalidates a higher-level basis?

### 13.5 Terminology and glossary review

Review the glossary before finishing.

Update it in the same change when the session:

- introduces a canonical UA concept;
- changes a term's meaning, scope, or ownership;
- changes the relationship among Constraint, Sensor, Controller, and Actuator;
- deprecates, replaces, or renames a term;
- creates an alias or historical relationship;
- exposes a missing distinction necessary to apply the specification.

Do not update the glossary merely because a phrase, tool name, pattern name, or section heading is new.

When unchanged, report:

> Glossary reviewed — no canonical terminology change required.

### 13.6 Changelog review

Review [`CHANGELOG.md`](CHANGELOG.md) before finishing.

- Every notable repository or specification-artifact change must be recorded under `[Unreleased]` in the same branch and pull request.
- Use `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, or `Security` as appropriate.
- Describe the repository-level effect, not a low-level file-edit narrative.
- Do not postpone the entry to a later cleanup session.

When no changelog entry is appropriate, explicitly report:

> Changelog reviewed — no notable repository or specification-artifact change required.

### 13.7 Cross-reference and navigation review

- Do related modules need links or updates?
- Do module indexes need to include or supersede the artifact?
- Does the root README expose new primary reader paths?
- Do internal links resolve, including moved capability directories?
- Was provenance preserved after moving content?
- Was a duplicate canonical route introduced?

### 13.8 Provenance and research review

- Were titles, quotations, dates, attribution, and source bodies preserved?
- Were historical terms left intact where required?
- Were research conclusions separated from source evidence?
- Was a presentation metaphor or product mapping translated rather than copied into doctrine?
- Were affected source-intake and framework-traceability records updated?
- Was duplicate research logging avoided?

### 13.9 Change-control review

- Is the change one coherent architectural decision?
- Are compatibility, path migrations, supersession, and unresolved uncertainty explicit?
- Was `CHANGELOG.md` updated?
- Does `ROADMAP.md` reflect changed sequence or capability maturity?
- Are changed files and rationale summarized clearly?

## 14. Quality checklist

- [ ] Correct status, maturity, module, and decision level.
- [ ] Capability function is explicit and not confused with topology.
- [ ] Current terminology outside historical material.
- [ ] Glossary reviewed and updated when required.
- [ ] Changelog reviewed and updated when required.
- [ ] Research state reconciled when triggered.
- [ ] No canonical concept redefined locally.
- [ ] Project and delivery decision ownership remain separate.
- [ ] Higher-level Constraints and context are inherited by reference.
- [ ] Constraint source, scope, strength, realization, failure, evidence, and authority are explicit.
- [ ] Soft Constraints are not represented as hard guarantees.
- [ ] Lower-level configuration does not silently relax higher-level authorization.
- [ ] Sensors support a real decision.
- [ ] Controller authority and escalation are substantive.
- [ ] Actuators provide a real corrective path.
- [ ] Upward reassessment is explicit when evidence invalidates a higher-level basis.
- [ ] Examples and templates are not universal requirements.
- [ ] Named technologies remain informative.
- [ ] Responsibilities are not confused with mandatory titles.
- [ ] Human Authority is substantive where claimed.
- [ ] Risk scores and expected value do not override hard prohibitions, missing Constraints, or unavailable controls.
- [ ] Metadata and tags agree with content.
- [ ] Internal links resolve, including renamed capability directories.
- [ ] Root and module navigation expose primary artifacts.
- [ ] No duplicate canonical entry point or namespace.
- [ ] Moved or superseded material remains traceable.
- [ ] Roadmap impact reviewed.
- [ ] Unresolved assumptions and evidence gaps disclosed.

## 15. Repository anti-patterns

### Control-level collapse

Treating organizational Constraints, project authorization, delivery realization and release, and runtime response as one generic governance decision.

Preferred response: identify the owning level, inherit higher-level Constraints, and escalate evidence only when it invalidates a higher-level basis.

### Capability/topology collapse

Treating Constraints, Sensors, Controllers, and Actuators as four mandatory products or services.

Preferred response: identify logical functions and allow implementations to distribute or combine them explicitly.

### Tool-name taxonomy

Calling a Prompt Registry a Controller, a schema the complete Constraint layer, a dashboard a control system, or an orchestration framework an Actuator without identifying the function, guarantee, evidence, authority, and corrective path.

### Constraint-as-prompt fallacy

Treating a probabilistic instruction as deterministic enforcement of a hard invariant.

### Declared-but-unenforced Constraint

Recording a boundary without a credible realization, failure behavior, evidence, owner, or change authority.

### Runtime policy overreach

Allowing a runtime component or operator to relax a project or organizational Constraint outside delegated authority.

### Constraint drift

Changing schemas, policies, permissions, prompts, models, tools, data, context, or deployment without preserving the relationship to the approved Requirement and inherited versions.

### Duplicate doctrine

Creating a second explanation of a canonical concept. Refine the owning document and link to it.

### Duplicate project and delivery records

Copying the project risk map, constraint architecture, control economics, or organizational policy into every delivery review, or embedding full DoR and DoD checklists in the project review.

### Silent scope expansion

Allowing one feature, tool integration, or release to expand project authority, autonomy, population, data, domain, geography, deployment, or consequence without project reauthorization.

### Accidental promotion

Writing research, presentations, templates, tool catalogs, or examples as if they were normative.

### Architecture by accumulation

Adding files, guardrails, or tools to reconcile inconsistency without resolving ownership, status, terminology, constraints, and capability connections.

### Tool-as-control fallacy

Treating a schema, evaluator, dashboard, guardrail, model, policy engine, kill switch, or workflow engine as a complete control system without source, evidence, authority, and corrective connection.

### Ceremonial Human Authority

Claiming Human-in-the-Loop or Human-on-the-Loop control when people lack time, context, competence, independence, capacity, or real intervention power.

### Universal thresholds and scores

Copying illustrative numbers into requirements or compressing risk into one score without consequence- and context-derived justification.

### Expected-value override

Using a positive ROI estimate to average away a hard prohibition, unacceptable consequence, missing Constraint, unavailable control, or unmanageable feedback latency.

### Namespace proliferation

Creating `new`, `v2`, `final`, `latest`, or parallel canonical paths without an explicit decision.

### Changelog omission

Making a notable repository or specification-artifact change without updating `CHANGELOG.md` in the same branch and pull request.

### Research log duplication

Recording routine sessions or pull-request history as research without a change in evidence, question state, interpretation, or framework destination.

## 16. Scope of this file

`AGENTS.md` is the tool-neutral operational protocol for AI-assisted contributors.

Tool-specific adapters such as `CLAUDE.md` or `.cursorrules` should point here and contain only the minimal tool-specific delta.

This file should evolve when repository structure, authority rules, terminology workflow, capability anatomy, constraint semantics, decision-level ownership, inheritance, change-record policy, research reconciliation, or contribution practice changes. It must not become a parallel specification of UA itself.
