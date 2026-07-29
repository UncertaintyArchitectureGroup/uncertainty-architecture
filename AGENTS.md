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
tags:
  - ua/module/repository
  - ua/type/repository-guide
  - ua/status/informative
  - ua/topic/repository-architecture
  - ua/topic/navigation
  - ua/topic/terminology
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
- how to preserve terminology, provenance, and history;
- how to finish a session without conceptual, structural, or documentation drift.

## 2. Repository mission

UA is an open doctrine and pattern language for building and operating software in which part of the system's behavior is delegated to non-deterministic Model Judgment while the surrounding system remains deterministic, inspectable, and governable.

The repository exists to evolve an open engineering specification for **Thinking Systems** at the AI-code boundary.

UA is:

- a shared architectural language;
- a doctrine for deterministic boundaries and probabilistic judgment;
- a pattern system for containment, evaluation, escalation, fallback, rollback, and correction;
- a control-oriented approach to operating model-mediated software;
- a tool-neutral specification that evolves through research and implementation evidence.

UA is not:

- an SDK or universal agent framework;
- a prompt-template collection;
- a vendor-specific architecture;
- a single evaluation method;
- a compliance certification;
- a claim that uncertainty can be eliminated.

## 3. Mental model for AI contributors

Think like a systems architect working on an evolving engineering specification, not like a framework developer optimizing one implementation.

Prefer:

- system boundaries over isolated components;
- responsibilities over job titles;
- invariants over implementation preferences;
- reusable distinctions over project-specific vocabulary;
- evidence over confident generalization;
- cross-references over duplicated definitions;
- refinement over unnecessary expansion;
- complete control loops over locally impressive tools.

When reviewing a proposed control structure, identify:

1. where Model Judgment occurs;
2. which deterministic boundaries and invariants constrain it;
3. what evidence makes behavior and outcomes observable;
4. who or what interprets that evidence;
5. who or what has authority to change system behavior;
6. which corrective actions are available;
7. how fallback, escalation, containment, rollback, or shutdown works;
8. how assumptions and decisions remain traceable.

## 4. Authority and conflict resolution

When documents appear to conflict, do not resolve the conflict by recency, popularity, file location, external visibility, or confidence of wording.

Use this order:

1. [`SPECIFICATION.md`](SPECIFICATION.md) for specification scope, status vocabulary, conformance, and change control.
2. Explicit document status and normative language.
3. The relevant module README for module purpose and boundaries.
4. [`00-doctrine/glossary.md`](00-doctrine/glossary.md) for current meanings of terms it defines.
5. Current doctrine and other specification content for architectural meaning.
6. [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) for metadata and tags.
7. Research, history, talks, external references, and examples for evidence and context, not automatic requirements.
8. This file for agent behavior and repository workflow only.

Additional rules:

- Explicit status takes precedence over directory name.
- `Normative` content takes precedence over conflicting lower-status material.
- `Draft normative` content must not be presented as stable.
- Maturity does not replace status.
- Research, talks, implementations, citations, or benchmarks do not become doctrine by implication.
- Report genuine contradictions instead of silently choosing one side.

## 5. Repository invariants

1. Every canonical concept should have one authoritative definition.
2. The glossary is the terminology source for terms it defines.
3. Doctrine defines foundational distinctions; lower-level modules must not silently redefine them.
4. Patterns describe reusable responses; they do not create local doctrine.
5. AI Control Plane documents define capabilities, not one mandatory product topology.
6. Reference architectures compose concepts and patterns; they do not become mandatory by example.
7. Failure modes describe reusable mechanisms of loss of control, not unrelated product defects.
8. Research provides evidence and framework candidates; it is not automatically specification.
9. Historical material preserves what was said and when.
10. Raw snapshots remain source evidence and must not be normalized in place.
11. One material type should have one canonical namespace.
12. Navigation and publishing infrastructure must not become a second specification.
13. Metadata, tags, recency, and search ranking do not create authority.
14. Repository growth should occur through coherent refinement, not fragmentation.
15. Every material repository change must remain visible in [`CHANGELOG.md`](CHANGELOG.md).

## 6. Canonical repository map and placement rules

### 6.1 Public entry points

- [`README.md`](README.md) — public landing page and reader navigation.
- [`SPECIFICATION.md`](SPECIFICATION.md) — specification boundary, status model, conformance, and change control.
- [`ROADMAP.md`](ROADMAP.md) — development sequence and planned artifacts.
- [`CHANGELOG.md`](CHANGELOG.md) — canonical record of notable repository and specification-artifact changes.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution and review workflow.
- [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) — metadata and controlled tags.
- [`AGENTS.md`](AGENTS.md) — this operational protocol.

### 6.2 `00-doctrine/`

Purpose: foundational concepts, distinctions, boundaries, and canonical vocabulary.

Place material here when it defines or materially refines:

- Thinking Systems;
- Deterministic Core;
- Model Judgment;
- Uncertainty Boundary;
- invariants and responsibility boundaries;
- control-oriented first principles;
- core terminology and conceptual definitions such as Requirement, Bug, or Human Authority.

Do not place here:

- vendor recipes;
- isolated implementation examples;
- raw research notes;
- historical records;
- patterns that only apply existing doctrine.

A doctrine change must be checked against the glossary, patterns, AI Control Plane, reference architectures, failure modes, module indexes, and changelog.

### 6.3 `01-patterns/`

Purpose: reusable technical and socio-technical responses to recurring control problems.

A pattern should make visible:

- context;
- problem;
- forces and trade-offs;
- proposed structure or control response;
- consequences and limitations;
- relationship to doctrine and failure modes.

Do not promote a one-off implementation into a pattern without a reusable problem and response.

### 6.4 `02-ai-control-plane/`

Purpose: capabilities required to constrain, observe, evaluate, and correct model-mediated behavior.

Relevant material includes:

- actuators;
- sensors and evidence;
- controllers and decision authority;
- constraints and policy enforcement;
- release and runtime gates;
- escalation and Human Authority;
- containment, fallback, rollback, and shutdown;
- control latency, traceability, and corrective-action paths;
- operating controls distributed across software and human processes.

Telemetry without decision authority and corrective action is observation, not control.

### 6.5 `03-reference-architectures/`

Purpose: concrete, non-prescriptive compositions showing how UA concepts and patterns may be applied.

Reference architectures may combine:

- doctrine;
- patterns;
- control capabilities;
- technical artifacts;
- technologies;
- roles, responsibilities, and processes.

They must separate specification requirements from illustrative choices and must not introduce local doctrine.

### 6.6 `04-failure-modes/`

Purpose: recurring mechanisms by which Thinking Systems lose structural, semantic, operational, economic, or organizational control.

A failure mode should describe:

- triggering conditions;
- mechanism of failure;
- observable signals;
- consequences;
- affected boundaries or control capabilities;
- containment, mitigation, or recovery options.

An isolated undesirable output is not automatically a reusable failure mode.

### 6.7 `content/research/`

Purpose: research publications, notes, analysis, synthesis, critique, provenance, and research-to-framework traceability.

Research informs explicit framework decisions. It does not update doctrine by implication.

### 6.8 `content/history/`

Purpose: project chronology, public discussions, talks, external references, recognition, and superseded records.

Preserve historical wording and distinguish citation, recommendation, implementation, adoption, certification, and endorsement.

### 6.9 `content/raw/`

Purpose: preserved source snapshots.

Do not paraphrase, modernize, normalize, or overwrite them in place.

### 6.10 Publishing and infrastructure

- `content/index.md` is a publishing portal, not a second specification entry point.
- `quartz/`, Node configuration, and `vercel.json` are publishing infrastructure.
- `assets/` contains diagrams and visual references.

Infrastructure behavior is not a UA requirement unless a specification document says so.

## 7. Canonical terminology

The canonical vocabulary is maintained in [`00-doctrine/glossary.md`](00-doctrine/glossary.md).

Before introducing, redefining, replacing, deprecating, or narrowing a UA term:

1. read the glossary;
2. search for existing uses and near-synonyms;
3. identify the owning module;
4. determine whether the distinction is necessary and stable;
5. update the glossary in the same change when canonical meaning changes.

Do not:

- create a second glossary;
- define canonical terms locally inside patterns or reference architectures;
- invent synonyms for style;
- add vendor vocabulary, temporary labels, section headings, or one-off phrases;
- treat memorable phrases as canonical without a durable architectural distinction.

### 7.1 Terminology migration

Use **Thinking Systems** in current framework material.

Preserve **Behavioral Software** and **Behavioral Applications** in historical titles, quotations, preserved source bodies, raw snapshots, and provenance records.

When current documentation first connects old and new language, it may use:

> **Thinking Systems** (previously described as **Behavioral Software** or **Behavioral Applications**)

Agentic systems are a higher-autonomy subset of Thinking Systems, not a synonym for the whole category.

## 8. Editing rules

### 8.1 Preserve concept ownership

- One concept, one canonical definition, one owning module.
- Prefer links over duplicated explanations.
- Refine the owning document instead of creating a competing source.
- Do not reconcile inconsistency by adding another overlapping document.

### 8.2 Separate specification from evidence and examples

- Research is evidence and analysis; doctrine is explicit synthesis.
- Reference architectures demonstrate compositions; they do not establish mandatory topology.
- Example thresholds are not universal requirements.
- Role names are not automatically mandatory job titles.
- Talks, articles, benchmarks, citations, and implementations do not update the specification by implication.

### 8.3 Classify socio-technical framework content explicitly

When extracting material from talks, research, examples, or source publications, classify each candidate before placing it in the specification.

Use these classes:

- **Concept or definition** — a foundational distinction or canonical meaning; normally belongs in `00-doctrine/` and may require a glossary entry.
- **Artifact** — a maintained object used to express intent, evidence, policy, state, or control, such as a Prompt Registry, Golden Scenario set, release manifest, risk map, escalation matrix, or decision record.
- **Role or responsibility bundle** — decision rights, ownership, competence, and authority required to operate part of the control loop. Prefer responsibilities over mandatory job titles.
- **Process or ritual** — a repeatable sequence through which evidence is reviewed and corrective action is authorized, such as drift review, release review, incident learning, or escalation.
- **Technical reference artifact** — an illustrative schema, interface, manifest, data model, evaluator contract, repository layout, or implementation example.
- **Pattern** — a reusable arrangement of artifacts, responsibilities, processes, and technical mechanisms that addresses a recurring control problem.
- **Failure mode** — a reusable mechanism by which control is lost or becomes ineffective.
- **Reference architecture** — a context-specific composition of several of the above.

Do not create a new top-level repository namespace for these classes merely because the classification exists. Place each item in the module that owns its architectural meaning, and use indexes or cross-references to expose the complete socio-technical stack.

### 8.4 Avoid false precision

Do not introduce universal numerical thresholds for quality, hallucination, drift, latency, cost, autonomy, confidence, Golden Scenario count, or review frequency without a context- and risk-derived basis.

### 8.5 Preserve uncertainty

When evidence conflicts or a concept remains incomplete:

- state the uncertainty;
- preserve relevant alternatives;
- identify the unresolved decision;
- avoid language stronger than the evidence supports.

### 8.6 Keep links, metadata, and change records coherent

- Use repository-relative links.
- Link to canonical module indexes rather than duplicating document lists.
- Planned artifacts belong in `ROADMAP.md` until created.
- Follow `DOCUMENT-METADATA.md`.
- Preserve provenance when moving or superseding content.
- Update `CHANGELOG.md` in the same branch and pull request for every notable repository or specification-artifact change.
- Do not postpone a changelog entry to a later cleanup session.

## 9. Task-specific reading paths

### 9.1 Understanding UA

Read `README.md`, `SPECIFICATION.md`, `00-doctrine/README.md`, the complete glossary, and then the relevant module.

### 9.2 Editing doctrine or terminology

1. Read `SPECIFICATION.md`.
2. Read relevant doctrine and its module index.
3. Read the complete glossary.
4. Search all uses and near-synonyms.
5. Identify downstream impact.
6. Update glossary, indexes, links, and changelog in the same change.
7. State compatibility, supersession, and unresolved uncertainty.

### 9.3 Proposing or changing a pattern

Read relevant doctrine, glossary terms, overlapping patterns, and failure modes. Identify which control-loop capabilities the pattern provides and which remain external.

### 9.4 Editing the AI Control Plane

Identify actuator, sensor, controller, authority, evidence, feedback path, and the behavior that can actually be changed, contained, or stopped.

### 9.5 Editing a reference architecture

Read relevant doctrine, patterns, and Control Plane documents. State context, assumptions, risk, autonomy, reversibility, and operating constraints. Separate required content from illustrative design choices.

### 9.6 Editing a failure mode

Identify the reusable mechanism, not only the symptom. Distinguish deterministic defects, expected distribution tails, missing controls, inadequate sensors, controller failures, and invalid assumptions.

### 9.7 Working with research or source extraction

Start with `content/research/index.md`. Distinguish source, normalized edition, analysis, synthesis, and framework candidate. Preserve evidence quality, scope, limitations, and contradictions.

For each extracted entity:

1. state the source and original claim;
2. classify it as concept, artifact, role/responsibility, process, technical reference artifact, pattern, failure mode, or reference architecture;
3. identify the owning module;
4. decide whether it is normative, draft normative, informative, reference, research, or historical;
5. check glossary impact;
6. identify dependencies and cross-references;
7. update the changelog when the repository changes.

### 9.8 Working with history

Start with `content/history/README.md`. Preserve source meaning and distinguish visibility from validation, adoption, certification, or endorsement.

## 10. Contribution workflow for AI-assisted changes

For repository-changing work:

1. **Understand** — identify the architectural purpose and document class.
2. **Locate ownership** — identify the module and existing owning document.
3. **Read dependencies** — follow the relevant reading path.
4. **Search before creating** — check terms, patterns, documents, and overlapping claims.
5. **Classify the entity** — concept, artifact, responsibility, process, technical reference artifact, pattern, failure mode, or reference architecture.
6. **Assess authority** — verify status, maturity, module boundaries, and normative language.
7. **Make the smallest coherent change** — prefer one reviewable decision.
8. **Cross-reference** — connect doctrine, patterns, control capabilities, evidence, failure modes, and history.
9. **Check terminology** — compare UA-specific wording with the glossary.
10. **Update the changelog** — record every notable repository or specification-artifact change under `[Unreleased]` in the same branch and pull request.
11. **Check repository integrity** — verify metadata, navigation, provenance, and status boundaries.
12. **Report uncertainty** — disclose contradictions, assumptions, evidence gaps, and unresolved decisions.
13. **Finish the session protocol** — complete the checks below.

Substantial framework changes should use a branch and pull request under [`CONTRIBUTING.md`](CONTRIBUTING.md).

## 11. End-of-session repository integrity protocol

Before completing any session that changes repository content, perform all checks.

### 11.1 Placement review

- Is each file in the correct module or namespace?
- Does the change have one clear architectural purpose?
- Could an existing canonical document have been refined?
- Was a new namespace introduced without a repository decision?

### 11.2 Authority and status review

- Does status match the document's actual role and language?
- Is draft material clearly marked?
- Did lower-status material accidentally create a normative claim?
- Does the change conflict with `SPECIFICATION.md` or a module boundary?

### 11.3 Terminology and glossary review

Review the glossary before finishing.

Update it in the same change when the session:

- introduces a canonical UA concept;
- changes a term's meaning, scope, or ownership;
- deprecates, replaces, or renames a term;
- creates an alias or historical relationship;
- exposes a missing distinction necessary to apply the specification.

Do not update the glossary merely because a phrase is new or memorable.

When unchanged, report:

> Glossary reviewed — no canonical terminology change required.

### 11.4 Changelog review

Review [`CHANGELOG.md`](CHANGELOG.md) before finishing.

- Every notable repository or specification-artifact change must be recorded under `[Unreleased]` in the same branch and pull request.
- Use `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, or `Security` as appropriate.
- Describe the repository-level effect, not a low-level file-edit narrative.
- Do not duplicate talks, publications, community discussions, or external recognition that belong in `content/history/`.
- Do not postpone the entry to a later session.

When no changelog entry is appropriate because the change is purely mechanical or non-notable, explicitly report:

> Changelog reviewed — no notable repository or specification-artifact change required.

### 11.5 Cross-reference and navigation review

- Do related modules need links or updates?
- Do module indexes need to include or supersede the artifact?
- Do internal links resolve?
- Was provenance preserved after moving content?
- Was a duplicate canonical route introduced?

### 11.6 Provenance and historical review

- Were titles, quotations, dates, attribution, and source bodies preserved?
- Were historical terms left intact where required?
- Were research conclusions separated from source evidence?
- Were recognition and visibility kept separate from validation and adoption?

### 11.7 Change-control review

- Is the change one coherent architectural decision?
- Are compatibility, supersession, and unresolved uncertainty explicit?
- Was `CHANGELOG.md` updated when the change was notable?
- Does `ROADMAP.md` need an update because sequence or scope changed?
- Are changed files and rationale summarized clearly?

## 12. Quality checklist

- [ ] Correct status and maturity.
- [ ] Correct module and placement.
- [ ] Extracted entities were explicitly classified.
- [ ] Current terminology outside historical material.
- [ ] Glossary reviewed and updated when required.
- [ ] Changelog reviewed and updated when required.
- [ ] No canonical concept redefined locally.
- [ ] Examples are not universal requirements.
- [ ] Responsibilities are not confused with mandatory titles.
- [ ] Research, history, and reference material remain within their authority boundaries.
- [ ] Controls include a real intervention path, not telemetry alone.
- [ ] Metadata and tags agree with the content.
- [ ] Internal links resolve.
- [ ] No duplicate canonical entry point or namespace.
- [ ] Moved or superseded material remains traceable.
- [ ] Module indexes and cross-references reviewed.
- [ ] Roadmap impact reviewed.
- [ ] Unresolved assumptions and evidence gaps disclosed.

## 13. Repository anti-patterns

### Duplicate doctrine

Creating a second explanation of a canonical concept. Refine the owning document and link to it.

### Local terminology

Inventing a new name inside a pattern or reference architecture for an existing concept. Use the glossary or propose an explicit glossary change.

### Accidental promotion

Writing research or examples as if they were normative. Preserve status and make promotion explicit.

### Architecture by accumulation

Adding files to reconcile inconsistency. Resolve ownership, status, and terminology instead.

### Tool-as-control fallacy

Treating a schema, evaluator, dashboard, guardrail, model, or workflow engine as a complete control system without authority and corrective action.

### Universal thresholds

Copying illustrative numbers into requirements without risk- and context-derived justification.

### Historical normalization

Rewriting old publications to match current terminology. Preserve the original and annotate separately.

### Namespace proliferation

Creating `new`, `v2`, `final`, `latest`, or parallel canonical paths without an explicit decision.

### Changelog omission

Making a notable repository or specification-artifact change without updating `CHANGELOG.md` in the same branch and pull request.

Preferred response: add a concise entry under `[Unreleased]` that describes the repository-level effect.

## 14. Scope of this file

`AGENTS.md` is the tool-neutral operational protocol for AI-assisted contributors.

Tool-specific adapters such as `CLAUDE.md` or `.cursorrules` should point here and contain only the minimal tool-specific delta.

This file should evolve when repository structure, authority rules, terminology workflow, change-record policy, or contribution practice changes. It must not become a parallel specification of UA itself.
