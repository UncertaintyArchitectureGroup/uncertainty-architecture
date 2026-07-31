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
- what information is inherited between project, delivery, and runtime work;
- how to preserve terminology, provenance, history, and research state;
- how to finish a session without conceptual, structural, or documentation drift.

## 2. Repository mission

UA is an open doctrine and pattern language for building and operating software in which part of the system's behavior is delegated to non-deterministic Model Judgment while the surrounding system remains deterministic, inspectable, and governable.

The repository exists to evolve an open engineering specification for **Thinking Systems** at the AI-code boundary.

UA begins from a controlled-object shift: uncertainty does not exist only in product assumptions, requirements, users, infrastructure, or deployment environments. A Thinking System may produce consequential uncertainty inside the operating system through runtime Model Judgment.

UA is:

- a shared architectural language;
- a doctrine for deterministic boundaries and probabilistic judgment;
- a pattern system for project authorization, delivery review, containment, evaluation, escalation, fallback, rollback, correction, and reauthorization;
- a control-oriented approach to model-mediated software across organizational, project, delivery, and runtime levels;
- a tool-neutral specification that evolves through research and implementation evidence.

UA is not:

- an SDK or universal agent framework;
- a prompt-template collection;
- a vendor-specific architecture;
- a single evaluation method;
- a replacement for product discovery, Agile, DevOps, QA, security, change management, or incident response;
- a compliance certification;
- a claim that uncertainty can be eliminated.

## 3. Four-level UA control context

Before analyzing or changing framework material, identify the control level of the question.

### 3.1 Organizational control context

This level owns constraints and shared capabilities that apply across projects, such as:

- prohibited uses and risk appetite;
- legal, privacy, security, safety, contractual, and financial constraints;
- approved vendors, deployment models, geographies, and data classes;
- shared identity, audit, evaluation, observability, incident, and shutdown capabilities;
- available Human Authority and decision rights.

UA does not require one policy, committee, or governance department to own all of this context. Existing organizational sources remain authoritative and should be linked rather than duplicated.

### 3.2 Project control architecture and viability

This level decides whether a proposed Thinking System has a credible, operable, and economically viable control architecture.

The canonical pattern is the [`Project Control Architecture and Viability Review`](01-patterns/project-control-architecture-and-viability-review.md). Its informative working representation is the [`project review template`](01-patterns/project-control-architecture-and-viability-review-template.md).

The project review owns:

- the intended business outcome and AI necessity;
- material risk and consequence scenarios;
- the intended Judgment, autonomy, and authority landscape;
- deterministic invariants and prohibited authority;
- required controls and shared capability dependencies;
- evidence feasibility and feedback latency;
- Human Authority and operational capacity;
- control build and run cost;
- project authorization, limitation, bounded research, redesign, escalation, deferral, or No-Go;
- the baseline inherited by delivery reviews;
- project reauthorization triggers.

### 3.3 Delivery-level review

This level decides whether a bounded whole system, feature, or material change is ready, complete, and acceptable for a stated deployment context.

The canonical pattern is the [`Thinking System Review`](01-patterns/thinking-system-review.md). Its informative working representation is the [`delivery review template`](01-patterns/thinking-system-review-template.md).

The delivery review owns:

- implementation-level Judgment Nodes;
- the applicable Requirement and Operating Envelope;
- the model-mediated Definition of Ready;
- bounded experimentation or implementation;
- the model-mediated Definition of Done;
- the deployment-specific Release Gate;
- local runtime reassessment.

“Delivery level” describes the decision layer, not the size of the work item. A delivery review may cover a bounded whole system, feature, or material change.

### 3.4 Runtime control and reauthorization

This level produces and interprets operational evidence, executes corrective action, and determines whether the evidence remains local or invalidates a higher-level decision.

Runtime evidence may require:

- local delivery correction, containment, rollback, or a new Release Gate;
- project reauthorization because risk, authority, capacity, evidence, or economics changed;
- organizational review because a shared constraint or capability changed.

Do not force every runtime issue upward. Do not keep project-invalidating evidence trapped inside one feature review.

### 3.5 Canonical ownership and inheritance rule

Use this ownership model:

```text
Organizational sources
→ Project Control Architecture and Viability Review
→ Thinking System Review
→ Runtime evidence and corrective action
```

Information should flow downward by reference:

- organizational constraints and shared capabilities constrain the project;
- the project review creates a versioned authorization and inheritance package;
- delivery reviews link the project version and refine local details;
- runtime records link the delivery and project decisions they operate under.

Evidence should flow upward when it invalidates an assumption:

- local implementation or evidence issue → delivery reassessment;
- project risk, authority, capacity, or economic assumption changed → project reauthorization;
- shared policy or capability changed → organizational review.

Do not duplicate the complete project risk map, control economics, or organizational policy in every delivery record. Do not allow a delivery review to silently expand project authority, autonomy, population, data, domain, geography, tool access, or consequence level.

## 4. Mental model for AI contributors

Think like a systems architect working on an evolving engineering specification, not like a framework developer optimizing one implementation.

Prefer:

- control level and decision ownership before document creation;
- system boundaries over isolated components;
- responsibilities over job titles;
- invariants over implementation preferences;
- scenario-to-control reasoning over aggregate risk scores;
- reusable distinctions over project-specific vocabulary;
- evidence over confident generalization;
- inheritance and cross-references over duplicated records;
- refinement over unnecessary expansion;
- complete control loops over locally impressive tools.

When reviewing a proposed control structure, identify:

1. which of the four control levels owns the question;
2. where Model Judgment occurs or is expected to occur;
3. which decisions, actions, outputs, resources, or parties it can affect;
4. which deterministic boundaries and invariants constrain it;
5. what evidence makes behavior and outcomes observable;
6. who or what interprets that evidence;
7. who or what has authority to change system behavior;
8. which corrective actions are available;
9. how fallback, escalation, containment, rollback, compensation, or shutdown works;
10. which assumptions and decisions are inherited from a higher level;
11. which evidence would require reassessment at a higher level;
12. whether the complete control system is operationally and economically viable.

## 5. Authority and conflict resolution

When documents appear to conflict, do not resolve the conflict by recency, popularity, file location, external visibility, or confidence of wording.

Use this order:

1. [`SPECIFICATION.md`](SPECIFICATION.md) for specification scope, status vocabulary, conformance, and change control.
2. Explicit document status and normative language.
3. The relevant module README for module purpose and boundaries.
4. [`00-doctrine/glossary.md`](00-doctrine/glossary.md) for current meanings of terms it defines.
5. Current doctrine and other specification content for architectural meaning.
6. The owning pattern for its decision surface: project review or delivery review.
7. [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) for metadata and tags.
8. Research, history, talks, external references, templates, and examples for evidence and context, not automatic requirements.
9. This file for agent behavior and repository workflow only.

Additional rules:

- Explicit status takes precedence over directory name.
- `Normative` content takes precedence over conflicting lower-status material.
- `Draft normative` content must not be presented as stable.
- Maturity does not replace status.
- Templates mirror patterns and do not create independent protocols.
- Research, talks, implementations, citations, or benchmarks do not become doctrine by implication.
- Report genuine contradictions instead of silently choosing one side.

## 6. Repository invariants

1. Every canonical concept should have one authoritative definition.
2. The glossary is the terminology source for terms it defines.
3. Doctrine defines foundational distinctions; lower-level modules must not silently redefine them.
4. Patterns describe reusable responses; they do not create local doctrine.
5. The project review owns project viability, authorization, inheritance, and reauthorization; the delivery review owns DoR, DoD, release, and local reassessment.
6. AI Control Plane documents define capabilities, not one mandatory product topology.
7. Reference architectures compose concepts and patterns; they do not become mandatory by example.
8. Failure modes describe reusable mechanisms of loss of control, not unrelated product defects.
9. Research provides evidence and framework candidates; it is not automatically specification.
10. Historical material preserves what was said and when.
11. Raw snapshots remain source evidence and must not be normalized in place.
12. One material type should have one canonical namespace.
13. Navigation and publishing infrastructure must not become a second specification.
14. Metadata, tags, recency, and search ranking do not create authority.
15. Repository growth should occur through coherent refinement, not fragmentation.
16. Higher-level decisions should be inherited by reference rather than copied into every lower-level artifact.
17. Lower-level evidence must trigger higher-level reassessment when it invalidates a higher-level assumption.
18. Every material repository change must remain visible in [`CHANGELOG.md`](CHANGELOG.md).

## 7. Canonical repository map and placement rules

### 7.1 Public entry points

- [`README.md`](README.md) — public landing page and reader navigation.
- [`SPECIFICATION.md`](SPECIFICATION.md) — specification boundary, status model, conformance, and change control.
- [`ROADMAP.md`](ROADMAP.md) — development sequence and planned artifacts.
- [`CHANGELOG.md`](CHANGELOG.md) — canonical record of notable repository and specification-artifact changes.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution and review workflow.
- [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) — metadata and controlled tags.
- [`AGENTS.md`](AGENTS.md) — this operational protocol.

### 7.2 `00-doctrine/`

Purpose: foundational concepts, distinctions, boundaries, and canonical vocabulary.

Place material here when it defines or materially refines:

- Thinking Systems;
- the controlled-object shift;
- the distinction between organizational, project, delivery, and runtime control levels;
- Deterministic Core;
- Model Judgment;
- Uncertainty Boundary;
- invariants and responsibility boundaries;
- control-oriented first principles;
- core terminology and conceptual definitions such as Requirement, Bug, or Human Authority.

Do not place here:

- detailed project or delivery review checklists;
- vendor recipes;
- isolated implementation examples;
- raw research notes;
- historical records;
- patterns that only apply existing doctrine.

A doctrine change must be checked against the glossary, project and delivery patterns, AI Control Plane, reference architectures, failure modes, module indexes, research traceability, roadmap, and changelog.

### 7.3 `01-patterns/`

Purpose: reusable technical and socio-technical responses to recurring control problems.

The module currently owns two connected review surfaces:

- [`Project Control Architecture and Viability Review`](01-patterns/project-control-architecture-and-viability-review.md) — project risk, control architecture, capacity, economics, authorization, inheritance, and reauthorization;
- [`Thinking System Review`](01-patterns/thinking-system-review.md) — delivery-level DoR, bounded experiment, DoD, Release Gate, and local reassessment.

A pattern should make visible:

- context;
- problem;
- forces and trade-offs;
- proposed structure or control response;
- artifacts, responsibilities, economics, and decision rights where relevant;
- consequences and limitations;
- relationship to doctrine and failure modes.

Do not promote a one-off implementation into a pattern without a reusable problem and response.

Do not duplicate project-level and delivery-level ownership merely because both patterns discuss risk, evidence, authority, controls, or reassessment.

### 7.4 `02-ai-control-plane/`

Purpose: capabilities required to constrain, observe, evaluate, and correct model-mediated behavior.

Relevant material includes:

- actuators;
- sensors and evidence;
- controllers and decision authority;
- constraints and policy enforcement;
- project, release, and runtime gates;
- escalation and Human Authority;
- containment, fallback, rollback, compensation, and shutdown;
- control latency, traceability, and corrective-action paths;
- operating controls distributed across software and human processes.

Telemetry without decision authority and corrective action is observation, not control.

### 7.5 `03-reference-architectures/`

Purpose: concrete, non-prescriptive compositions showing how UA concepts and patterns may be applied.

Reference architectures may combine:

- doctrine;
- project and delivery patterns;
- control capabilities;
- technical artifacts;
- technologies;
- roles, responsibilities, economics, and processes.

A two-level worked application should show project baseline inheritance and runtime reauthorization without creating duplicate canonical records.

Reference architectures must separate specification requirements from illustrative choices and must not introduce local doctrine.

### 7.6 `04-failure-modes/`

Purpose: recurring mechanisms by which Thinking Systems lose structural, semantic, operational, economic, or organizational control.

A failure mode should describe:

- triggering conditions;
- mechanism of failure;
- observable signals;
- consequences;
- affected boundaries or control capabilities;
- affected control level;
- containment, mitigation, recovery, or reauthorization options.

An isolated undesirable output is not automatically a reusable failure mode.

### 7.7 `content/research/`

Purpose: research publications, notes, analysis, synthesis, critique, provenance, and research-to-framework traceability.

Research informs explicit framework decisions. It does not update doctrine or patterns by implication.

### 7.8 `content/history/`

Purpose: project chronology, public discussions, talks, external references, recognition, and superseded records.

Preserve historical wording and distinguish citation, recommendation, implementation, adoption, certification, and endorsement.

### 7.9 `content/raw/`

Purpose: preserved source snapshots.

Do not paraphrase, modernize, normalize, or overwrite them in place.

### 7.10 Publishing and infrastructure

- `content/index.md` is a publishing portal, not a second specification entry point.
- `quartz/`, Node configuration, and `vercel.json` are publishing infrastructure.
- `assets/` contains diagrams and visual references.

Infrastructure behavior is not a UA requirement unless a specification document says so.

## 8. Canonical terminology

The canonical vocabulary is maintained in [`00-doctrine/glossary.md`](00-doctrine/glossary.md).

Before introducing, redefining, replacing, deprecating, or narrowing a UA term:

1. read the glossary;
2. search for existing uses and near-synonyms;
3. identify the owning module and control level;
4. determine whether the distinction is necessary and stable;
5. update the glossary in the same change when canonical meaning changes.

Do not:

- create a second glossary;
- define canonical terms locally inside patterns, templates, or reference architectures;
- invent synonyms for style;
- add vendor vocabulary, temporary labels, section headings, or one-off phrases;
- treat memorable phrases or pattern names as glossary terms without a durable architectural distinction.

### 8.1 Terminology migration

Use **Thinking Systems** in current framework material.

Preserve **Behavioral Software** and **Behavioral Applications** in historical titles, quotations, preserved source bodies, raw snapshots, and provenance records.

When current documentation first connects old and new language, it may use:

> **Thinking Systems** (previously described as **Behavioral Software** or **Behavioral Applications**)

Agentic systems are a higher-autonomy subset of Thinking Systems, not a synonym for the whole category.

## 9. Editing rules

### 9.1 Preserve concept and decision ownership

- One concept, one canonical definition, one owning module.
- One decision surface, one owning pattern.
- Prefer links and inherited versions over duplicated explanations and records.
- Refine the owning document instead of creating a competing source.
- Do not reconcile inconsistency by adding another overlapping document.

### 9.2 Preserve review-level boundaries

Project review and delivery review intentionally overlap in vocabulary but not in decision ownership.

Project-level material may include high-level Judgment landscape, risk scenarios, required controls, evidence feasibility, capacity, economics, and project authorization.

Delivery-level material may include detailed Judgment Nodes, Requirement and Operating Envelope, DoR, implementation or experiment evidence, DoD, release scope, residual risk, and local reassessment.

When a delivery review needs project context, link the project version and identify inherited fields. Do not copy the complete project review.

When delivery or runtime evidence invalidates the project baseline, update or reauthorize the project review. Do not hide the contradiction in a local exception.

### 9.3 Separate specification from evidence and examples

- Research is evidence and analysis; doctrine is explicit synthesis.
- Reference architectures demonstrate compositions; they do not establish mandatory topology.
- Templates implement patterns; they do not create independent conformance paths.
- Example thresholds are not universal requirements.
- Role names are not automatically mandatory job titles.
- Talks, articles, benchmarks, citations, and implementations do not update the specification by implication.

### 9.4 Classify socio-technical framework content explicitly

When extracting material from talks, research, examples, or source publications, classify each candidate before placing it in the specification.

Use these classes:

- **Concept or definition** — a foundational distinction or canonical meaning; normally belongs in `00-doctrine/` and may require a glossary entry.
- **Artifact** — a maintained object used to express intent, evidence, policy, state, or control, such as a project review, Prompt Registry, Golden Scenario set, release manifest, risk map, escalation matrix, or decision record.
- **Role or responsibility bundle** — decision rights, ownership, competence, and authority required to operate part of the control loop. Prefer responsibilities over mandatory job titles.
- **Process or ritual** — a repeatable sequence through which evidence is reviewed and corrective action is authorized, such as project authorization, drift review, release review, incident learning, or escalation.
- **Technical reference artifact** — an illustrative schema, interface, manifest, data model, evaluator contract, repository layout, or implementation example.
- **Pattern** — a reusable arrangement of artifacts, responsibilities, processes, economics, and technical mechanisms that addresses a recurring control problem.
- **Failure mode** — a reusable mechanism by which control is lost or becomes ineffective.
- **Reference architecture** — a context-specific composition of several of the above.

Do not create a new top-level repository namespace for these classes merely because the classification exists. Place each item in the module that owns its architectural meaning, and use indexes or cross-references to expose the complete socio-technical stack.

### 9.5 Avoid false precision

Do not introduce universal numerical thresholds for quality, hallucination, drift, latency, cost, autonomy, confidence, Golden Scenario count, review frequency, risk, or expected value without a context- and consequence-derived basis.

Do not allow one aggregate risk score or expected-value number to override a hard prohibition, unacceptable consequence, missing control, or non-substantive Human Authority.

### 9.6 Preserve uncertainty

When evidence conflicts or a concept remains incomplete:

- state the uncertainty;
- preserve relevant alternatives;
- identify the unresolved decision and owning control level;
- avoid language stronger than the evidence supports.

### 9.7 Keep links, metadata, inheritance, and change records coherent

- Use repository-relative links.
- Link to canonical module indexes and owning patterns rather than duplicating document lists.
- Planned artifacts belong in `ROADMAP.md` until created.
- Follow `DOCUMENT-METADATA.md`.
- Preserve provenance when moving or superseding content.
- Preserve project and delivery decision versions when runtime evidence changes the current state.
- Update `CHANGELOG.md` in the same branch and pull request for every notable repository or specification-artifact change.
- Do not postpone a changelog entry to a later cleanup session.

## 10. Task-specific reading paths

### 10.1 Understanding UA

Read in this order:

1. `README.md`;
2. `SPECIFICATION.md`;
3. `00-doctrine/uncertainty-in-the-controlled-object.md`;
4. `00-doctrine/README.md`;
5. the complete glossary;
6. `01-patterns/project-control-architecture-and-viability-review.md`;
7. `01-patterns/thinking-system-review.md`;
8. the relevant Control Plane, reference architecture, failure mode, or research source.

### 10.2 Editing doctrine or terminology

1. Read `SPECIFICATION.md`.
2. Read relevant doctrine and its module index.
3. Read the complete glossary.
4. Search all uses and near-synonyms.
5. Identify downstream impact across all four control levels.
6. Update glossary, indexes, links, research traceability, roadmap, and changelog when affected.
7. State compatibility, supersession, and unresolved uncertainty.

### 10.3 Proposing or changing the project review

Read:

- `00-doctrine/uncertainty-in-the-controlled-object.md`;
- `01-patterns/project-control-architecture-and-viability-review.md`;
- its template;
- `01-patterns/thinking-system-review.md`;
- `02-ai-control-plane/README.md`;
- relevant research traceability and failure modes.

Check that the change:

- concerns project viability, authorization, inheritance, or reauthorization;
- does not duplicate full DoR, DoD, or the delivery Release Gate;
- connects risk scenarios to control capabilities, evidence, authority, corrective action, capacity, and economics;
- preserves No-Go and non-AI alternatives;
- remains proportional for SMB use.

### 10.4 Proposing or changing a delivery pattern

Read relevant doctrine, the project review and inheritance rules, glossary terms, overlapping patterns, and failure modes. Identify which project constraints are inherited and which implementation details the delivery pattern owns.

### 10.5 Editing the AI Control Plane

Identify actuator, sensor, controller, authority, evidence, feedback path, affected control level, and the behavior that can actually be changed, contained, compensated, or stopped.

### 10.6 Editing a reference architecture

Read relevant doctrine, project and delivery patterns, and Control Plane documents. State context, assumptions, risk, autonomy, reversibility, operating constraints, project baseline, delivery scope, and reauthorization path. Separate required content from illustrative design choices.

### 10.7 Editing a failure mode

Identify the reusable mechanism, not only the symptom. Distinguish deterministic defects, expected distribution tails, missing controls, inadequate sensors, controller failures, invalid assumptions, control-capacity failure, economic non-viability, and the control level where the failure becomes material.

### 10.8 Working with research or source extraction

Start with [`content/research/index.md`](content/research/index.md). Use [`content/research/review-process.md`](content/research/review-process.md) for the detailed proportional workflow and [`content/research/framework-traceability.md`](content/research/framework-traceability.md) as the single canonical record for material source-to-framework decisions.

Distinguish source, normalized edition, analysis, synthesis, framework candidate, and worked-application evidence. Preserve evidence quality, scope, limitations, contradictions, and control-level implications.

For each extracted entity:

1. state the source and original claim;
2. classify it as concept, artifact, role/responsibility, process, technical reference artifact, pattern, failure mode, or reference architecture;
3. identify the owning module and control level;
4. decide whether it is normative, draft normative, informative, reference, research, or historical;
5. check glossary impact;
6. identify dependencies, inheritance, reauthorization, and cross-references;
7. update the changelog when the repository changes.

#### Research reconciliation trigger

After a source-derived framework change, worked application, incident, or operational observation, check whether the work:

- registers or materially reinterprets a source;
- resolves, narrows, rejects, supersedes, or reopens a research question;
- promotes a candidate into doctrine, a pattern, a control capability, a failure mode, an artifact, or a reference architecture;
- changes the relationship between existing research and the current framework;
- changes which control level owns a decision or how information is inherited between levels.

When any trigger applies, review the owning research note or source-intake record, `framework-traceability.md`, affected open questions or maturity, and the research index when direction or navigation changed. Update only records whose state actually changed. Do not create a second ledger or use research as a session log.

### 10.9 Working with history

Start with `content/history/README.md`. Preserve source meaning and distinguish visibility from validation, adoption, certification, or endorsement.

## 11. Contribution workflow for AI-assisted changes

For repository-changing work:

1. **Understand** — identify the architectural purpose and document class.
2. **Identify the control level** — organizational, project, delivery, runtime, or a deliberate connection between them.
3. **Locate ownership** — identify the module, owning doctrine or pattern, and existing authoritative record.
4. **Read dependencies** — follow the relevant reading path.
5. **Search before creating** — check terms, patterns, documents, review surfaces, and overlapping claims.
6. **Classify the entity** — concept, artifact, responsibility, process, technical reference artifact, pattern, failure mode, or reference architecture.
7. **Assess authority** — verify status, maturity, module boundaries, normative language, and decision rights.
8. **Check inheritance** — identify what is linked from a higher level and what evidence may require upward reassessment.
9. **Make the smallest coherent change** — prefer one reviewable decision.
10. **Cross-reference** — connect doctrine, project and delivery patterns, control capabilities, evidence, failure modes, and history.
11. **Check terminology** — compare UA-specific wording with the glossary.
12. **Update the changelog** — record every notable repository or specification-artifact change under `[Unreleased]` in the same branch and pull request.
13. **Reconcile research state when triggered** — update only the affected intake, note, analysis, traceability, or research navigation.
14. **Check repository integrity** — verify metadata, navigation, provenance, status boundaries, ownership, and inheritance.
15. **Report uncertainty** — disclose contradictions, assumptions, evidence gaps, and unresolved decisions.
16. **Finish the session protocol** — complete the checks below.

Substantial framework changes should use a branch and pull request under [`CONTRIBUTING.md`](CONTRIBUTING.md).

## 12. End-of-session repository integrity protocol

Before completing any session that changes repository content, perform all checks.

### 12.1 Placement and control-level review

- Is each file in the correct module or namespace?
- Is the owning control level explicit?
- Does the change have one clear architectural purpose?
- Could an existing canonical document have been refined?
- Was a new namespace introduced without a repository decision?

### 12.2 Authority and status review

- Does status match the document's actual role and language?
- Is draft material clearly marked?
- Did lower-status material accidentally create a normative claim?
- Does the change conflict with `SPECIFICATION.md`, doctrine, a module boundary, or an owning pattern?
- Did a template accidentally become a second protocol?

### 12.3 Review ownership and inheritance review

- Is project viability or authorization owned by the project review?
- Are DoR, DoD, release, and local reassessment owned by the delivery review?
- Are organizational sources linked rather than copied?
- Does the delivery artifact identify the inherited project version?
- Did a lower-level change silently expand higher-level authority or scope?
- Are upward reassessment triggers explicit when evidence invalidates a higher-level assumption?

### 12.4 Terminology and glossary review

Review the glossary before finishing.

Update it in the same change when the session:

- introduces a canonical UA concept;
- changes a term's meaning, scope, or ownership;
- deprecates, replaces, or renames a term;
- creates an alias or historical relationship;
- exposes a missing distinction necessary to apply the specification.

Do not update the glossary merely because a phrase, pattern name, or section heading is new.

When unchanged, report:

> Glossary reviewed — no canonical terminology change required.

### 12.5 Changelog review

Review [`CHANGELOG.md`](CHANGELOG.md) before finishing.

- Every notable repository or specification-artifact change must be recorded under `[Unreleased]` in the same branch and pull request.
- Use `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, or `Security` as appropriate.
- Describe the repository-level effect, not a low-level file-edit narrative.
- Do not duplicate talks, publications, community discussions, or external recognition that belong in `content/history/`.
- Do not postpone the entry to a later session.

When no changelog entry is appropriate because the change is purely mechanical or non-notable, explicitly report:

> Changelog reviewed — no notable repository or specification-artifact change required.

### 12.6 Cross-reference and navigation review

- Do related modules need links or updates?
- Do module indexes need to include or supersede the artifact?
- Does the root README expose new primary reader paths?
- Do internal links resolve?
- Was provenance preserved after moving content?
- Was a duplicate canonical route introduced?

### 12.7 Provenance and historical review

- Were titles, quotations, dates, attribution, and source bodies preserved?
- Were historical terms left intact where required?
- Were research conclusions separated from source evidence?
- Were recognition and visibility kept separate from validation and adoption?

### 12.8 Research-state review

When the research reconciliation trigger applies:

- Was the owning source-intake, analysis, synthesis, or working note reviewed?
- Were resolved, narrowed, rejected, superseded, reopened, and remaining questions stated accurately?
- Was `framework-traceability.md` updated when an auditable source-to-framework decision changed?
- Was research navigation updated only when direction or state materially changed?
- Was duplicate logging avoided?

When no research state changed, do not add a research record merely to document that the session happened.

### 12.9 Change-control review

- Is the change one coherent architectural decision?
- Are compatibility, supersession, and unresolved uncertainty explicit?
- Was `CHANGELOG.md` updated when the change was notable?
- Does `ROADMAP.md` need an update because sequence or scope changed?
- Are changed files and rationale summarized clearly?

## 13. Quality checklist

- [ ] Correct status and maturity.
- [ ] Correct module, placement, and control level.
- [ ] Extracted entities were explicitly classified.
- [ ] Current terminology outside historical material.
- [ ] Glossary reviewed and updated when required.
- [ ] Changelog reviewed and updated when required.
- [ ] Research state reconciled when triggered.
- [ ] No canonical concept redefined locally.
- [ ] Project and delivery decision ownership remain separate.
- [ ] Higher-level context is inherited by reference rather than copied.
- [ ] Upward reassessment is explicit when lower-level evidence invalidates a higher-level assumption.
- [ ] Examples and templates are not universal requirements.
- [ ] Responsibilities are not confused with mandatory titles.
- [ ] Research, history, and reference material remain within their authority boundaries.
- [ ] Controls include a real intervention path, not telemetry alone.
- [ ] Human Authority is substantive where claimed.
- [ ] Risk scores and expected value do not override hard prohibitions or missing controls.
- [ ] Metadata and tags agree with the content.
- [ ] Internal links resolve.
- [ ] Root and module navigation expose new primary artifacts.
- [ ] No duplicate canonical entry point or namespace.
- [ ] Moved or superseded material remains traceable.
- [ ] Module indexes and cross-references reviewed.
- [ ] Roadmap impact reviewed.
- [ ] Unresolved assumptions and evidence gaps disclosed.

## 14. Repository anti-patterns

### Control-level collapse

Treating organizational constraints, project authorization, delivery release, and runtime response as one generic governance decision.

Preferred response: identify the owning level, inherit higher-level constraints, and escalate evidence only when it invalidates a higher-level assumption.

### Duplicate doctrine

Creating a second explanation of a canonical concept. Refine the owning document and link to it.

### Duplicate project and delivery records

Copying the project risk map, control economics, or organizational policy into every delivery review, or embedding full DoR and DoD checklists in the project review.

Preferred response: preserve separate ownership and pass a versioned inheritance package by reference.

### Silent scope expansion

Allowing one feature, tool integration, or release to expand project authority, autonomy, population, data, domain, geography, or consequence without project reauthorization.

Preferred response: record the reauthorization trigger and return the decision to the project review.

### Local terminology

Inventing a new name inside a pattern or reference architecture for an existing concept. Use the glossary or propose an explicit glossary change.

### Accidental promotion

Writing research, templates, or examples as if they were normative. Preserve status and make promotion explicit.

### Architecture by accumulation

Adding files to reconcile inconsistency. Resolve ownership, status, terminology, and inheritance instead.

### Tool-as-control fallacy

Treating a schema, evaluator, dashboard, guardrail, model, or workflow engine as a complete control system without authority and corrective action.

### Ceremonial Human Authority

Claiming Human-in-the-Loop or Human-on-the-Loop control when people lack time, context, competence, independence, capacity, or real intervention power.

### Universal thresholds and scores

Copying illustrative numbers into requirements or compressing risk into one score without consequence- and context-derived justification.

### Expected-value override

Using a positive ROI estimate to average away a hard prohibition, unacceptable consequence, unavailable control, or unmanageable feedback latency.

### Historical normalization

Rewriting old publications to match current terminology. Preserve the original and annotate separately.

### Namespace proliferation

Creating `new`, `v2`, `final`, `latest`, or parallel canonical paths without an explicit decision.

### Changelog omission

Making a notable repository or specification-artifact change without updating `CHANGELOG.md` in the same branch and pull request.

Preferred response: add a concise entry under `[Unreleased]` that describes the repository-level effect.

### Research log duplication

Recording routine sessions or pull-request history as research without a change in evidence, question state, interpretation, or framework destination.

Preferred response: update only the owning research record when a meaningful state transition occurs.

## 15. Scope of this file

`AGENTS.md` is the tool-neutral operational protocol for AI-assisted contributors.

Tool-specific adapters such as `CLAUDE.md` or `.cursorrules` should point here and contain only the minimal tool-specific delta.

This file should evolve when repository structure, authority rules, terminology workflow, control-level ownership, inheritance, change-record policy, research reconciliation, or contribution practice changes. It must not become a parallel specification of UA itself.
