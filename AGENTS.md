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

It is an operational protocol for repository work. It is not part of the normative UA specification and does not create a second source of doctrine, terminology, conformance, or architectural authority.

Use this file to determine:

- which documents to read before making a change;
- where a new contribution belongs;
- which source has authority when documents appear to conflict;
- how to preserve terminology, provenance, and historical accuracy;
- how to finish a session without introducing conceptual or structural drift.

This file must not be used to override [`SPECIFICATION.md`](SPECIFICATION.md), an explicit document status, the relevant module index, or a canonical definition in [`00-doctrine/glossary.md`](00-doctrine/glossary.md).

## 2. Repository mission

Uncertainty Architecture is an open doctrine and pattern language for building and operating software in which part of the system's behavior is delegated to non-deterministic model judgment while the surrounding system remains deterministic, inspectable, and governable.

The repository exists to evolve an open engineering specification for Thinking Systems at the AI-code boundary.

UA is:

- a shared architectural language;
- a doctrine for reasoning about deterministic boundaries and probabilistic judgment;
- a pattern system for containment, evaluation, escalation, fallback, and correction;
- a control-oriented approach to operating model-mediated software;
- a tool-neutral specification intended to evolve through research and implementation evidence.

UA is not:

- an SDK or universal agent framework;
- a prompt-template collection;
- a vendor-specific architecture;
- a single evaluation method;
- a compliance certification;
- a claim that model uncertainty can be eliminated.

Repository work should strengthen conceptual integrity, practical engineering usefulness, traceability, and long-term maintainability of the specification.

## 3. Mental model for AI contributors

Think like a systems architect working on an evolving engineering specification, not like a framework developer optimizing one implementation.

Prefer:

- system boundaries over isolated components;
- responsibilities over job titles;
- invariants over implementation preferences;
- reusable architectural distinctions over project-specific vocabulary;
- evidence and explicit reasoning over confident generalization;
- cross-references over duplicated definitions;
- refinement of existing concepts over unnecessary expansion;
- control-loop completeness over local technical sophistication.

Do not assume that a technically impressive implementation is architecturally sufficient. A prompt, evaluator, guardrail, agent, workflow engine, or telemetry system may implement one control capability without closing the system-level loop.

When reviewing a proposed control structure, identify at least:

1. where Model Judgment occurs;
2. which deterministic boundaries and invariants constrain it;
3. what evidence makes relevant behavior or outcomes observable;
4. who or what interprets that evidence;
5. who or what has authority to change system behavior;
6. which corrective actions are actually available;
7. how fallback, escalation, containment, rollback, or shutdown works;
8. how the decision and its assumptions remain traceable.

## 4. Authority and conflict resolution

When repository documents appear to conflict, do not resolve the conflict by recency, popularity, file location, external visibility, or confidence of wording.

Use this order of interpretation:

1. [`SPECIFICATION.md`](SPECIFICATION.md) for specification scope, normative language, status vocabulary, conformance, and change control.
2. The explicit status and normative language of the documents involved.
3. The relevant module README for the purpose and boundary of that module.
4. [`00-doctrine/glossary.md`](00-doctrine/glossary.md) for current canonical meanings of terms it defines.
5. Accepted doctrine and other current specification content for the architectural meaning of concepts.
6. [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) for metadata and controlled tagging conventions.
7. Research, history, talks, external references, and examples for evidence, provenance, interpretation, and evolution, not automatic requirements.
8. This file for agent behavior and repository workflow only.

Additional rules:

- Explicit document status takes precedence over directory name.
- `Normative` content takes precedence over conflicting `draft-normative`, `informative`, `reference`, `research`, or `historical` material.
- `Draft normative` content must not be presented as stable or accepted merely because it is newer.
- Maturity fields such as `active`, `stable`, or `superseded` do not replace status.
- A recent commit, article, citation, discussion, talk, implementation, benchmark, or external framework does not become UA doctrine by implication.
- When two current normative or draft-normative sources genuinely conflict, report the contradiction instead of silently choosing one.

## 5. Repository invariants

The following invariants protect the conceptual structure of the repository:

1. Every canonical concept should have one authoritative definition.
2. The glossary is the canonical terminology source for terms it currently defines.
3. Doctrine defines foundational distinctions; lower-level modules must not silently redefine them.
4. Patterns describe reusable responses to recurring problems; they do not create local doctrine.
5. AI Control Plane documents define control capabilities and their relationships; they do not imply one mandatory product topology.
6. Reference architectures compose concepts and patterns; they do not become mandatory by example.
7. Failure modes describe reusable mechanisms of loss of control; they are not collections of unrelated product bugs.
8. Research provides evidence, critique, provenance, and framework candidates; it does not become specification automatically.
9. Historical material preserves what was said and when; it must not be rewritten to appear consistent with current doctrine.
10. Raw source snapshots remain source evidence; they must not be normalized in place.
11. One material type should have one canonical repository namespace.
12. Navigation and publishing infrastructure must not become a second specification.
13. Metadata, tags, recency, and search ranking do not create authority.
14. Repository growth should occur by coherent refinement, not by fragmenting one concept across many partially overlapping files.

## 6. Canonical repository map and placement rules

### 6.1 Public entry points

- [`README.md`](README.md) — public landing page and primary reader navigation. It presents the current project identity and points to canonical sources.
- [`SPECIFICATION.md`](SPECIFICATION.md) — canonical specification boundary, status model, conformance entry point, and change-control rules.
- [`ROADMAP.md`](ROADMAP.md) — current development sequence and planned artifacts.
- [`CHANGELOG.md`](CHANGELOG.md) — repository-level record of material changes.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution workflow, review expectations, and maintainer authority.
- [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) — controlled frontmatter fields and hierarchical tag conventions.
- [`AGENTS.md`](AGENTS.md) — this operational protocol for AI-assisted contributors.

### 6.2 `00-doctrine/`

Purpose: foundational concepts, distinctions, boundaries, and canonical vocabulary on which the rest of UA depends.

Place material here when it defines or materially refines how UA understands:

- Thinking Systems;
- Deterministic Core;
- Model Judgment;
- the Uncertainty Boundary;
- invariants and responsibility boundaries;
- control-oriented first principles;
- core terminology.

Do not place here:

- one-off implementation guidance;
- vendor-specific recipes;
- isolated project examples;
- raw research notes;
- historical records;
- patterns that merely apply existing doctrine.

Any doctrine change must be checked for impact on the glossary, patterns, AI Control Plane, reference architectures, failure modes, module indexes, and changelog.

### 6.3 `01-patterns/`

Purpose: reusable technical and socio-technical responses to recurring control problems.

A pattern should normally make visible:

- context;
- problem;
- forces and trade-offs;
- proposed structure or control response;
- consequences;
- limitations;
- relationship to doctrine and known failure modes.

Do not promote a one-off implementation into a pattern unless the underlying problem and response plausibly generalize.

Patterns must use existing doctrine and glossary terminology. If a pattern appears to require a new foundational concept, resolve that concept in doctrine first.

### 6.4 `02-ai-control-plane/`

Purpose: capabilities required to constrain, observe, evaluate, and correct model-mediated behavior.

Relevant material may address:

- actuators;
- sensors and evidence;
- controllers and decision authority;
- constraints and policy enforcement;
- release and runtime gates;
- escalation and Human Authority;
- containment, fallback, rollback, or shutdown;
- control latency, traceability, and corrective-action paths;
- operating controls distributed across software and human processes.

The AI Control Plane is an architectural capability model. Do not assume it must be one centralized service, product, platform, or team.

When adding a control mechanism, state what behavior it can actually change and which authority can invoke it. Telemetry without a decision path is observation, not control.

### 6.5 `03-reference-architectures/`

Purpose: concrete, non-prescriptive compositions showing how UA concepts and patterns may be applied.

Reference architectures may combine doctrine, patterns, control capabilities, technologies, and operating roles into a worked design.

They must:

- identify which parts are required by current specification content and which are illustrative;
- avoid presenting one topology, vendor, model, or organizational structure as universal;
- link to the doctrine and patterns they apply;
- make assumptions, risk context, and unresolved limitations visible.

A concept discovered through a reference architecture does not become canonical until it is reconciled with the owning module and glossary.

### 6.6 `04-failure-modes/`

Purpose: recurring mechanisms by which Thinking Systems lose structural, semantic, operational, economic, or organizational control.

A failure mode should normally describe:

- triggering conditions;
- mechanism of failure;
- observable signals;
- consequences;
- affected boundaries or control capabilities;
- containment, mitigation, or recovery options;
- unresolved uncertainty where applicable.

Do not describe an isolated product defect as a UA failure mode unless it exposes a reusable system mechanism.

### 6.7 `content/research/`

Purpose: research publications, notes, analysis, synthesis, critique, provenance, and research-to-framework traceability.

Research may inform the specification, but research content is not automatically normative.

When working with research:

- distinguish source preservation from interpretation;
- preserve attribution and publication provenance;
- separate evidence from framework conclusions;
- record contradictory evidence and limitations;
- use explicit framework decisions to move ideas into normative modules.

Start with [`content/research/index.md`](content/research/index.md) and use [`content/research/framework-traceability.md`](content/research/framework-traceability.md) for decision-oriented mapping where relevant.

### 6.8 `content/history/`

Purpose: project chronology, public discussions, talks, external references, recognition, and superseded records retained for traceability.

Historical material must remain historically accurate.

Do not:

- silently modernize terminology in historical titles or source bodies;
- turn invitations, views, reactions, reposts, recommendations, or advisory relationships into technical validation;
- describe an implementation, citation, or discussion as adoption or certification without evidence supporting that exact claim.

Use clarification, annotation, or supersession notes instead of rewriting the past.

### 6.9 `content/raw/`

Purpose: preserved source snapshots used for normalized research editions and provenance.

Raw material is source evidence, not current doctrine.

Do not paraphrase, normalize, modernize, or overwrite raw snapshots in place.

### 6.10 Publishing and repository infrastructure

- `content/index.md` is a publishing portal for the Quartz site, not a second specification entry point.
- `quartz/`, `quartz.config.ts`, `quartz.layout.ts`, Node package files, and `vercel.json` are publishing infrastructure.
- `assets/` contains diagrams and visual references.

Infrastructure behavior is not a UA requirement unless a specification document explicitly makes it one.

Keep publishing-only changes separate from methodology changes when practical.

## 7. Canonical terminology

The canonical vocabulary of UA is maintained in [`00-doctrine/glossary.md`](00-doctrine/glossary.md).

Before introducing, redefining, replacing, deprecating, or materially narrowing a UA-specific term:

1. read the glossary;
2. search the repository for existing uses and near-synonyms;
3. identify which module owns the underlying concept;
4. determine whether the distinction is necessary and stable;
5. update the glossary in the same change when the canonical meaning changes.

Do not:

- create a second glossary inside this file or another document;
- define a canonical term locally inside a pattern or reference architecture;
- invent a synonym merely to improve style;
- add ordinary software-engineering vocabulary, vendor terminology, temporary labels, section headings, or one-off phrases to the glossary;
- treat a memorable phrase as a canonical concept without a durable architectural distinction.

A new glossary term should normally represent a concept that is necessary to understand or apply UA across more than one isolated document.

### 7.1 Terminology migration

Use **Thinking Systems** as the current UA category for software systems whose runtime behavior depends partly on probabilistic model judgment while consequential deterministic boundaries, invariants, decision rights, and corrective mechanisms remain explicit.

Earlier UA publications used **Behavioral Software** and **Behavioral Applications**.

Rules:

- Use `Thinking Systems` in new doctrine, patterns, AI Control Plane documents, reference architectures, failure modes, specification text, and current repository guidance.
- Preserve `Behavioral Software` and `Behavioral Applications` in historical titles, quotations, preserved publication bodies, raw snapshots, and provenance records.
- Do not silently rewrite historical material solely to modernize terminology.
- When current documentation needs to connect old and new language, the first relevant reference may use:

> **Thinking Systems** (previously described as **Behavioral Software** or **Behavioral Applications**)

Subsequent current discussion should use **Thinking Systems**.

Agentic systems are a higher-autonomy subset of Thinking Systems, not a synonym for the whole category.

## 8. Editing rules

### 8.1 Preserve ownership of concepts

- One concept should have one canonical definition and one owning module.
- Prefer repository-relative links to duplicated explanations.
- If an existing document owns the concept, refine or cross-reference it instead of creating a competing source.
- Do not solve inconsistency by adding another document that restates both sides.

### 8.2 Separate normative content from evidence and examples

- Research is evidence and analysis; doctrine is explicit synthesis.
- A reference architecture demonstrates one composition; it does not establish a mandatory topology.
- An example threshold is not a universal requirement.
- A role name is not automatically a required job title.
- A talk, article, benchmark, external citation, or implementation does not update the specification by implication.

### 8.3 Avoid false precision

Do not introduce universal numerical thresholds for quality, hallucination, drift, latency, cost, autonomy, confidence, Golden Scenario count, or review frequency without an explicit context- and risk-derived basis.

When numbers are illustrative, label them as examples and state the conditions under which they may differ.

### 8.4 Preserve uncertainty and disagreement

Do not convert unresolved research questions into settled doctrine.

When evidence conflicts or a concept remains incomplete:

- state the uncertainty;
- preserve relevant alternatives;
- identify the decision that remains open;
- avoid language stronger than the available evidence supports.

### 8.5 Keep internal links and metadata coherent

- Use repository-relative links for internal files.
- Link to the canonical index of a directory rather than copying its full document list into many places.
- Do not link to nonexistent planned files; planned artifacts belong in `ROADMAP.md` until created.
- Follow [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md).
- Do not infer authority from tags alone.
- When moving or superseding content, preserve provenance and update inbound navigation.

## 9. Task-specific reading paths

### 9.1 Understanding UA

1. Read [`README.md`](README.md).
2. Read [`SPECIFICATION.md`](SPECIFICATION.md).
3. Read [`00-doctrine/README.md`](00-doctrine/README.md).
4. Read [`00-doctrine/glossary.md`](00-doctrine/glossary.md).
5. Read the module relevant to the question.
6. Use research and history when provenance, evidence, critique, or evolution matters.

### 9.2 Editing doctrine or terminology

1. Read `SPECIFICATION.md`.
2. Read the relevant doctrine documents and module index.
3. Read the complete glossary.
4. Search the repository for all uses and near-synonyms of affected terms.
5. Identify downstream dependencies in patterns, AI Control Plane, reference architectures, and failure modes.
6. Update the glossary, indexes, links, and changelog when material.
7. State compatibility, supersession, and unresolved uncertainty.

### 9.3 Proposing or changing a pattern

1. Read the doctrine and glossary terms the pattern relies on.
2. Search `01-patterns/` for overlapping patterns.
3. Review relevant failure modes.
4. Identify which control-loop elements the pattern provides and which remain external.
5. Distinguish reusable structure from implementation examples.
6. Check whether the proposal actually requires a doctrine change first.

### 9.4 Editing the AI Control Plane

1. Read the relevant doctrine and glossary entries.
2. Identify actuator, sensor, controller, authority, evidence, and feedback path.
3. State what behavior can be changed, contained, or stopped.
4. Review reference architectures for downstream effects.
5. Review failure modes that the control capability is intended to address.
6. Check whether the change affects conformance reasoning in `SPECIFICATION.md`.

### 9.5 Editing a reference architecture

1. Read the relevant doctrine, patterns, and AI Control Plane documents.
2. State context, assumptions, risk, autonomy, reversibility, and operating constraints.
3. Separate required specification content from illustrative design choices.
4. Avoid vendor lock-in unless vendor specificity is the point of the reference.
5. Check that no local terminology or doctrine is being introduced implicitly.

### 9.6 Editing a failure mode

1. Identify the reusable mechanism, not only the observed symptom.
2. Link the failure to affected boundaries, evidence, authority, or corrective mechanisms.
3. Review existing failure modes for overlap.
4. Distinguish deterministic defects, expected distribution tails, missing controls, inadequate sensors, controller failures, and invalid assumptions.
5. State mitigations without pretending they guarantee elimination of the failure.

### 9.7 Working with research

1. Start with `content/research/index.md`.
2. Distinguish source, normalized edition, analysis, synthesis, and framework candidate.
3. Preserve attribution and source meaning.
4. Record evidence quality, scope, limitations, and contradictions.
5. Use `content/research/framework-traceability.md` when mapping findings into repository decisions.
6. Do not promote a claim into doctrine without an explicit normative change.

### 9.8 Working with history or external recognition

1. Start with `content/history/README.md`.
2. Distinguish publication, discussion, citation, recommendation, advisory relationship, invited talk, implementation, adoption, certification, and endorsement.
3. Use evidence that supports the exact claim being recorded.
4. Preserve criticism and alternative interpretations where material.
5. Keep current terminology explanations outside preserved historical source bodies.

### 9.9 Working with the publishing site

1. Treat `content/index.md` as a publishing portal, not the canonical repository landing page.
2. Do not move specification authority into Quartz configuration or generated navigation.
3. Do not alter methodology merely to simplify site structure.
4. Keep publishing changes separate from specification changes when practical.

## 10. Contribution workflow for AI-assisted changes

For repository-changing work, follow this sequence:

1. **Understand the request** — restate the architectural purpose and identify whether the change is normative, informative, reference, research, historical, or infrastructure.
2. **Locate ownership** — identify the module and existing document that owns the concept.
3. **Read dependencies** — follow the relevant task-specific reading path.
4. **Search before creating** — check for existing terms, patterns, documents, and overlapping claims.
5. **Assess authority** — verify status, maturity, module boundaries, and normative language.
6. **Make the smallest coherent change** — prefer one reviewable architectural decision over broad unrelated cleanup.
7. **Cross-reference** — link related doctrine, patterns, control capabilities, evidence, failure modes, and history where useful.
8. **Check terminology** — compare all UA-specific wording with the glossary.
9. **Check repository integrity** — verify metadata, navigation, provenance, and status boundaries.
10. **Report uncertainty** — disclose contradictions, assumptions, evidence gaps, and decisions that remain unresolved.
11. **Finish the session protocol** — complete the checklist in the next section before declaring the work done.

Substantial framework changes should be made on a branch and reviewed through a pull request under [`CONTRIBUTING.md`](CONTRIBUTING.md).

## 11. End-of-session repository integrity protocol

Before completing any session that changes repository content, perform all of the following checks.

### 11.1 Placement review

- Is each changed file in the correct canonical module or supporting namespace?
- Does the change have one clear architectural purpose?
- Could an existing canonical document have been refined instead of adding a new file?
- Was a new top-level namespace introduced without a repository-level decision?

### 11.2 Authority and status review

- Does the declared status match the actual language and role of the document?
- Is draft material clearly represented as draft?
- Did any informative, reference, research, historical, or infrastructure material accidentally create a normative claim?
- Does the change conflict with `SPECIFICATION.md` or a module boundary?

### 11.3 Terminology and glossary review

Review [`00-doctrine/glossary.md`](00-doctrine/glossary.md) before finishing.

Check whether the session:

- introduced a new UA-specific concept;
- changed the meaning, scope, or ownership of an existing term;
- deprecated, replaced, or renamed a term;
- created an alias or historical terminology relationship;
- used a term inconsistently with the glossary;
- exposed a missing distinction necessary to understand or apply the specification.

If any condition applies, update the glossary in the same change and review downstream uses.

Do not update the glossary merely because a phrase is new, memorable, convenient, vendor-specific, temporary, or used in only one isolated passage.

If no glossary change is required, report:

> Glossary reviewed — no canonical terminology change required.

### 11.4 Cross-reference and navigation review

- Do related doctrine, patterns, AI Control Plane documents, reference architectures, and failure modes need links or updates?
- Do module indexes need to include or supersede the changed artifact?
- Do all internal links resolve to existing paths?
- Were inbound links preserved after moving content?
- Did the change create a duplicate canonical route?

### 11.5 Provenance and historical review

- Were quotations, titles, source bodies, dates, and attribution preserved?
- Was historical language left intact where required?
- Were visibility, recognition, invitations, or advisory relationships kept separate from validation, adoption, certification, or endorsement?
- Were research conclusions kept separate from source evidence?

### 11.6 Change-control review

- Is the change scoped to one coherent architectural decision?
- Are compatibility, supersession, and unresolved uncertainty explicit?
- Does `CHANGELOG.md` need an entry because the change is material?
- Does `ROADMAP.md` need an update because sequencing or planned scope changed?
- Are the files changed and the rationale summarized clearly for reviewers?

## 12. Quality checklist

Before proposing or approving a repository change, verify:

- [ ] The target document has the correct status and maturity.
- [ ] The change belongs in the selected module.
- [ ] Current terminology is used outside historical material.
- [ ] The glossary was reviewed and updated when required.
- [ ] No existing canonical concept was redefined locally.
- [ ] Examples are not written as universal requirements.
- [ ] Responsibilities are not confused with mandatory job titles.
- [ ] Research, history, and reference material remain outside the normative boundary unless explicitly promoted.
- [ ] Controls include a real path to affect behavior, not telemetry alone.
- [ ] The change does not imply that one tool or metric closes a system-level control loop.
- [ ] Metadata fields and tags agree with the content.
- [ ] Internal links resolve to existing files.
- [ ] No duplicate canonical entry point or namespace was introduced.
- [ ] Moved or superseded material remains traceable.
- [ ] Relevant module indexes and cross-references were reviewed.
- [ ] Changelog and roadmap impact were considered.
- [ ] Unresolved contradictions, assumptions, and evidence gaps are disclosed.

## 13. Repository anti-patterns

Avoid the following patterns of contribution:

### Duplicate doctrine

Creating a second explanation of a canonical concept because the existing one is inconvenient, incomplete, or located elsewhere.

Preferred response: refine the owning document and link to it.

### Local terminology

Inventing a new name inside a pattern, reference architecture, or article for a concept already represented in the glossary.

Preferred response: use the canonical term or propose an explicit glossary change.

### Accidental promotion

Writing research findings, examples, or reference designs in language that makes them appear normative.

Preferred response: preserve their status and create an explicit specification change when promotion is intended.

### Architecture by accumulation

Adding more files to reconcile inconsistency instead of resolving ownership, status, or terminology.

Preferred response: identify the canonical source and consolidate or supersede deliberately.

### Tool-as-control fallacy

Treating an evaluator, guardrail, schema, dashboard, model, or workflow engine as a complete control system without authority and corrective action.

Preferred response: describe the capability it provides and the missing parts of the loop.

### Universal thresholds

Copying illustrative numbers into requirements without deriving them from consequences, uncertainty, autonomy, reversibility, evidence quality, and context.

Preferred response: describe how thresholds should be selected and label examples clearly.

### Historical normalization

Rewriting old publications or records to match current terminology and doctrine.

Preferred response: preserve the original and add current interpretation separately.

### Namespace proliferation

Creating `new`, `v2`, `final`, `latest`, temporary top-level directories, or parallel canonical paths without an explicit repository decision.

Preferred response: use status, version control, supersession notes, and the existing taxonomy.

### Publishing-driven authority

Allowing site navigation, generated pages, tags, or search behavior to redefine repository authority.

Preferred response: keep the canonical boundary in `SPECIFICATION.md` and module indexes.

## 14. Scope of this file

`AGENTS.md` is the repository's tool-neutral operational protocol for AI-assisted contributors.

Tool-specific files such as `CLAUDE.md`, `.cursorrules`, or similar adapters should not duplicate this document. If a tool-specific adapter is required, it should point here and contain only the minimal tool-specific delta.

This file should evolve when repository structure, authority rules, terminology workflow, or contribution practice changes. It must not evolve into a parallel specification of UA itself.
