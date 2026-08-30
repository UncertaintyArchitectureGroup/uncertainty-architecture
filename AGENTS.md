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

## 1. Purpose and authority

This file defines how language models, coding agents, automated reviewers, and other AI-assisted contributors should work inside the Uncertainty Architecture repository.

It is **operational guidance**, not normative UA specification content. It must not override:

1. [`SPECIFICATION.md`](SPECIFICATION.md);
2. explicit document status and normative language;
3. the relevant module boundary;
4. canonical definitions in [`00-doctrine/glossary.md`](00-doctrine/glossary.md);
5. the owning doctrine or pattern.

Use this file to determine what to read, where a change belongs, how much process is justified, how to preserve ownership and provenance, and how to finish a repository-changing session.

Do not use it as a second glossary, a second specification, or a source of new governance requirements.

When documents conflict, prefer, in order:

1. `SPECIFICATION.md` for scope, status, conformance, and change control;
2. explicit status and normative language;
3. the relevant module README;
4. the glossary for terms it defines;
5. current doctrine for architectural meaning;
6. the owning project or delivery pattern;
7. the relevant AI Control Plane capability document;
8. `DOCUMENT-METADATA.md` for metadata and controlled tags;
9. research, history, talks, implementations, templates, and examples for evidence and context;
10. this file for repository workflow only.

Report genuine contradictions instead of silently choosing one side.

### Session bootstrap and instruction discovery

At the start of every repository task, and again before a repository-changing action when the state may have changed:

1. inspect the repository root and use targeted tree or repository search to discover applicable `AGENTS.md` files and the task-relevant subtree; resolve the default branch, relevant ref, and task-specific branch, issue, pull request, review, and CI state where applicable;
2. read this root `AGENTS.md` in full and discover any nested `AGENTS.md` files whose directory scope intersects the task;
3. treat a nested `AGENTS.md` as a scoped supplement to this file, not as a replacement for it, and read and apply it according to the scope stated by that file; read [`content/research/AGENTS.md`](content/research/AGENTS.md) in full when the task edits files under `content/research/` or makes research-content, provenance, research-state, or publication-edition decisions. Infrastructure that only renders, validates, transports, or packages research artifacts does not activate the long-form research-drafting protocol unless it also changes research content or state;
4. identify the applicable task-specific reading path, owning sources, and relevant repository contracts before proposing or making changes;
5. treat the current repository state as authoritative for repository facts; previous chats, summaries, pasted excerpts, and cached snapshots are supporting context only;
6. report unavailable access or conflicting instructions instead of silently substituting assumptions; and
7. distinguish verified current state, proposed changes, locally prepared changes, and remotely applied changes whenever reporting work state or completion.

Inspecting the repository tree is not the same as reading every file. Do not claim a complete repository review unless the complete relevant content was actually read.

## 2. Repository mission and SMB default

UA is an open doctrine and pattern language for engineering and operating **Thinking Systems**: software systems in which one or more **Consequential Runtime Responsibilities** depend partly on probabilistic Model Judgment rather than being fully specified through explicitly encoded logic in advance. Contributors MUST keep category identification separate from control adequacy: missing Constraints, evidence, decision rights, or corrective mechanisms make a Thinking System inadequately controlled; they do not make it cease to be a Thinking System.

**Consequential Runtime Responsibility** is a classification concept based on the material causal relevance of the responsibility itself, independent of whether it is implemented deterministically or through Model Judgment. Thinking-System classification asks whether at least one such responsibility depends partly on probabilistic Model Judgment. Contributors MUST NOT use **consequential** as a synonym for high-risk, harmful, autonomous, regulated, or production-ready behavior; severity, likelihood, residual exposure, control strength, and release decisions are evaluated separately.

UA is not an SDK, universal agent framework, vendor architecture, prompt collection, evaluation method, compliance certification, or replacement for product discovery, Agile, DevOps, QA, security, change management, or incident response.

Unless a document explicitly requires otherwise, contributors MUST assume a small or medium-sized organization with limited specialist capacity.

The default SMB path is:

```text
Existing organizational sources
→ one living project-level review
→ one living delivery-level review per bounded scope
→ linked runtime evidence, decisions, and actions
```

Default rules:

- link existing organizational sources instead of copying them;
- keep one canonical Project Constraint Architecture at project level;
- keep one canonical Constraint Realization Map at delivery level;
- use existing architecture records, issue trackers, CI, evaluation stores, observability, and incident systems where they already have an owner and lifecycle;
- allow one person to carry several responsibility bundles while keeping decision authority explicit;
- add roles, files, registers, services, committees, or gates only when an independent owner, lifecycle, authority, access boundary, retention need, or audit requirement makes them necessary.

A founder may hold organizational and project authority. A technical lead may carry architecture and delivery responsibilities. An on-call engineer may perform a runtime Controller function.

Combining responsibilities does not collapse decisions. Organizational boundaries, project authorization, delivery release, and runtime action remain distinguishable even when one person participates in all four.

Do not import enterprise-governance structure by default. UA does not require a governance department, mandatory specialist titles, a standing committee, a separate Constraint Register, a separate risk register, a RACI, one file per gate, or one service per capability family.

Increase depth only when consequence, authority, exposure, irreversibility, uncertainty, feedback latency, realization difficulty, Human Authority load, operating capacity, or control economics justify it.

## 3. The two-axis architecture

Every material framework change must be located on two independent axes:

1. **decision level** — where the decision is owned;
2. **capability family and function** — how the decision is made operational.

The four decision levels are not capability layers. The four capability families are not organizational levels, mandatory products, or a fixed execution sequence.

### 3.1 Four decision levels in practical SMB terms

| Practical level | UA decision level | Decision owned | Typical SMB responsibility | Canonical record |
|---|---|---|---|---|
| **Organization** | Organizational control context | Authoritative boundaries, shared capabilities, approved vendors or deployment modes, decision rights, exception authority | Founder, owner, product authority, or existing legal/security/operations responsibility; not necessarily a department | Existing authoritative sources linked by reference; no new UA organization file required by default |
| **Architecture / project** | Project control architecture and viability | Whether the proposed Thinking System has a credible, operable, and economically viable control architecture; authorization, conditions, redesign, deferral, or No-Go | Architect, technical lead, project owner, or another person carrying the architectural decision responsibility | [`Project Control Architecture and Viability Review`](01-patterns/project-control-architecture-and-viability-review.md) |
| **Delivery team** | Delivery-level Thinking System Review | How inherited Constraints are realized, tested, completed, released, and locally reassessed for a bounded scope | The delivery team using existing product, engineering, QA, security, and operational responsibilities | [`Thinking System Review`](01-patterns/thinking-system-review.md) |
| **Runtime** | Runtime operation and reassessment | Whether active operation remains inside the approved boundary and what must be corrected, contained, rolled back, disabled, or escalated | Automated logic, on-call or operational responsibility, Human Authority, or a combination | Runtime evidence and actions linked to active project and delivery versions; no separate runtime register required by default |

“Architect” describes a decision responsibility, not a mandatory job title. The responsible person must be able to make or obtain the project-level architecture and viability decision.

A lower level may refine or narrow a higher-level authorization. It must not silently expand authority, weaken an inherited Hard Constraint, or treat technical configurability as decision authority.

Higher-level decisions and Constraint authority flow downward by reference. Evidence flows upward when it invalidates the basis of a delivery, project, or organizational decision.

### 3.2 Four capability families

Use [`00-doctrine/control-loop-anatomy.md`](00-doctrine/control-loop-anatomy.md) as the canonical architectural source.

| Capability family | Function | Critical distinction |
|---|---|---|
| **Constraints and their realizations** | Define the approved operating boundary and make it operational | A Constraint is the authoritative boundary object; a Constraint Realization is the technical or socio-technical mechanism implementing, enforcing, or influencing it |
| **Sensors and evidence** | Observe behavior, outcomes, conditions, realization state, control health, and Actuator execution | Evidence is not a decision and telemetry alone is not control |
| **Controllers and decision authority** | Compare or interpret evidence relative to references and select or authorize action | A Controller decides or authorizes; it does not become an Actuator merely because one component performs both functions |
| **Actuators and corrective action** | Execute authorized changes to operation or a Constraint Realization | Technical ability to change something does not authorize the change |

One component or person may perform several functions. One function may be distributed. Evidence, authority, and failure responsibilities must still remain distinguishable.

### 3.3 Four-by-four review matrix

The four capability families may appear at every decision level. Use this matrix as a reasoning check, not as a requirement to create sixteen components or sixteen documents.

| Decision level | Constraints and realizations | Sensors and evidence | Controllers and authority | Actuators and action |
|---|---|---|---|---|
| **Organization** | Legal, contractual, security, privacy, procurement, prohibited-use, vendor, geography, and shared-capability boundaries | Cross-project incidents, audits, regulatory or vendor change, portfolio evidence, capability health | Authorized organizational owner or existing decision process selects or authorizes organizational change | Publish or change an authoritative source, approved vendor, shared capability, funding state, exception, or project permission |
| **Architecture / project** | One Project Constraint Architecture derived from organizational sources and project risk | Scenario evidence, feasibility, feedback latency, capacity, control economics, and residual exposure | Project architecture and authorization authority decides to authorize, narrow, condition, research, redesign, defer, escalate, or reject | Issue or update the project baseline; change scope or architecture; allocate capability; start research or redesign; pause or stop project work |
| **Delivery team** | One Constraint Realization Map for the bounded delivery scope | Deterministic tests, evaluations, behavioral evidence, realization health, false blocks, and operational readiness | Delivery and release authority decides within the project baseline | Implement, configure, deploy, block, narrow exposure, fall back, roll back, or request project reauthorization |
| **Runtime** | Active Constraint sources, realization versions, Operating Envelope, permissions, limits, and deployment boundary | Telemetry, outcomes, incidents, violations, bypass, drift, capacity, Human Authority, and Actuator-effect evidence | Runtime software, operational owner, Human Authority, incident process, or a combination selects or authorizes response | Reject, contain, compensate, route to fallback, change configuration within authority, roll back, disable, stop, or escalate |

Ask both questions for every material change:

1. **Who owns this decision and at which level?**
2. **Which capability function defines the boundary, produces evidence, decides, and executes?**

A framework change is incomplete when it answers only one.

## 4. Canonical ownership and invariants

1. One canonical concept should have one authoritative definition.
2. One decision surface should have one owning pattern.
3. Doctrine defines foundational distinctions; lower modules apply rather than redefine them.
4. The glossary owns canonical terminology where an entry exists.
5. The Project Control Architecture and Viability Review owns project viability, Project Constraint Architecture, authorization, inheritance, and reauthorization.
6. The Thinking System Review owns delivery realization, DoR, DoD, Release Gate, and local reassessment.
7. Runtime operation is not a mandatory third governance artifact; runtime evidence and actions should link to active project and delivery versions unless an independent lifecycle requires another record.
8. AI Control Plane documents define logical capability families, not one product topology.
9. Constraint, Constraint Realization, Sensor, Controller, and Actuator must remain distinguishable.
10. A Controller selects or authorizes; an Actuator executes.
11. Hard or soft is a scoped claim about a Constraint and its complete realized path, not an intrinsic property of policy prose.
12. Different guarantee strengths across subjects, paths, or scopes require separate Constraint claims rather than one mixed hard/soft record.
13. A lower-level decision may narrow but must not silently weaken or expand a higher-level authorization or Hard Constraint.
14. Higher-level decisions flow downward by reference; invalidating evidence flows upward.
15. Reference architectures illustrate compositions and do not become mandatory.
16. Failure modes describe reusable mechanisms of loss of control, not isolated undesirable outputs.
17. Research provides evidence and candidates; it is not automatically specification.
18. Historical and raw material preserves original wording and provenance.
19. Navigation, metadata, tags, recency, and publishing infrastructure do not create authority.
20. Repository growth should occur through coherent refinement rather than namespace proliferation.
21. Every notable repository or specification-artifact change must be recorded in [`CHANGELOG.md`](CHANGELOG.md).

## 5. Repository placement map

### Public entry points

- [`README.md`](README.md) — public landing page and navigation.
- [`SPECIFICATION.md`](SPECIFICATION.md) — specification boundary and status model.
- [`ROADMAP.md`](ROADMAP.md) — development direction.
- [`CHANGELOG.md`](CHANGELOG.md) — notable repository changes.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution workflow.
- [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) — metadata and controlled tags.
- [`AGENTS.md`](AGENTS.md) — this operational protocol.

### `00-doctrine/`

Owns foundational concepts, distinctions, relationships, and terminology, including Thinking Systems, the controlled-object shift, Nested Control Lifecycle, Control-Loop Capability Anatomy, Constraints, Requirements, Operating Envelopes, Correctness, Bugs, and Human Authority.

Do not place checklists, vendor recipes, isolated examples, raw notes, or one-off project procedures here.

### `01-patterns/`

Owns reusable socio-technical responses:

- [`Project Control Architecture and Viability Review`](01-patterns/project-control-architecture-and-viability-review.md);
- [`Judgment Node Boundary`](01-patterns/judgment-node-boundary.md);
- [`Thinking System Review`](01-patterns/thinking-system-review.md).

### `02-ai-control-plane/`

Owns capability-specific guidance:

- [`00-actuators/`](02-ai-control-plane/00-actuators/);
- [`01-constraints/`](02-ai-control-plane/01-constraints/);
- [`02-sensors/`](02-ai-control-plane/02-sensors/);
- [`03-controller/`](02-ai-control-plane/03-controller/).

The Constraints directory owns the composite Constraint and Constraint Realization family. Directory numbers are navigation only. Named tools remain examples.

### `03-reference-architectures/`

Owns non-prescriptive worked compositions. References must distinguish requirements from illustrative choices and must not introduce local doctrine.

### `04-failure-modes/`

Owns recurring mechanisms by which structural, semantic, operational, economic, or organizational control is lost.

### `content/research/`

Owns research, notes, synthesis, critique, provenance, and research-to-framework traceability. Research informs explicit decisions; it does not update doctrine by implication.

### `content/history/` and `content/raw/`

Preserve chronology, external context, original claims, and source snapshots. Do not normalize raw or historical wording in place.

## 6. Terminology and Constraint protocol

Before introducing, redefining, replacing, deprecating, or narrowing a UA term:

1. read the complete glossary;
2. search current framework material and near-synonyms;
3. identify the owning module, decision level, and capability function;
4. determine whether the distinction is necessary and stable;
5. update the glossary in the same change when canonical meaning changes;
6. update research traceability when a research question is resolved or reopened.

Do not:

- create a second glossary;
- define canonical terms locally in a template or reference architecture;
- use Constraint, Constraint Realization, Invariant, Requirement, policy, guardrail, boundary, and Actuator interchangeably;
- treat an organizational source as a Hard Constraint without a scoped realized path;
- combine deterministic and probabilistic guarantees in one mixed-strength Constraint record;
- invent synonyms for style;
- turn a memorable phrase, slide label, role title, or product category into a canonical term without a durable distinction.

Use **Thinking Systems** in current framework material. Preserve **Behavioral Software** and **Behavioral Applications** in historical titles, quotations, raw sources, and provenance records.

For every material Constraint, answer:

1. What is the authoritative source or project-risk rationale?
2. What subject, path, and scope does it bound?
3. Is the claimed guarantee hard or soft for that subject, path, and scope?
4. What complete Constraint Realization implements, enforces, or influences it?
5. Under which assumptions does the claimed guarantee hold?
6. What happens on violation, bypass, conflict, degradation, uncertainty, or unavailability?
7. What evidence shows activation, coverage, violations, false blocks, friction, and health?
8. Which Controller may select or authorize a change?
9. Which Actuator executes that change?
10. Which changes remain local, require delivery reassessment, require project reauthorization, or require organizational review?

A Hard Constraint must deterministically prevent or reject violation through its complete realized path within stated assumptions, subject, path, scope, and enforcement boundaries.

A prompt, natural-language policy, probabilistic evaluator, classifier, or model preference is not hard by itself.

When one source condition contains different guarantee strengths, split it into separate reviewable Constraint claims.

If these questions cannot be answered, preserve the item as a research candidate, unresolved dependency, or Soft Constraint rather than presenting it as an operable guarantee.

## 7. Capability classification and diagrams

Classify by function in the specific system, not by tool name, team name, role title, or market category.

For evaluation systems, distinguish:

```text
Evaluator and metrics → Sensor
Decision logic selecting block/canary/release → Controller
Deployment, blocking, exposure change, or rollback → Actuator
```

One product may package several functions.

For Mermaid and other architecture diagrams:

- show reference conditions or approved intent reaching the relevant Controller;
- show actual outputs, actions, and downstream outcomes reaching Sensors where material;
- show evidence reaching decision authority;
- show authorized action reaching an Actuator;
- show the Actuator changing operation or a Constraint Realization;
- show realization state and Actuator effects returning as evidence where material;
- use `enforces or influences` and `may gate` in generic diagrams;
- use deterministic language such as `bounds`, `blocks`, or `gates` only when a scoped Hard Constraint and complete realized path justify it;
- do not draw the four capability families as a mandatory vertical execution sequence;
- do not draw the four decision levels as a one-way delivery waterfall without upward reassessment paths.

A closed feedback loop is not automatically a bounded acceptable UA control architecture.

## 8. Task-specific reading paths

### Understanding UA

1. `README.md`
2. `SPECIFICATION.md`
3. `00-doctrine/uncertainty-in-the-controlled-object.md`
4. `00-doctrine/control-loop-anatomy.md`
5. `00-doctrine/nested-control-lifecycle.md`
6. `00-doctrine/glossary.md`
7. project and delivery patterns
8. relevant Control Plane, reference architecture, failure mode, or research source

### Editing doctrine or terminology

Read `SPECIFICATION.md`, the complete glossary, relevant doctrine, both review patterns, affected Control Plane capability areas, failure modes, research traceability, roadmap, and changelog.

### Editing project architecture material

Read the controlled-object doctrine, capability anatomy, lifecycle, project pattern and template, delivery pattern, Constraint capability, relevant failure modes, and traceability.

Confirm that the change concerns project viability, Project Constraint Architecture, authorization, inheritance, or reauthorization and remains proportional for SMB use.

### Editing delivery-team material

Read the project pattern and inheritance rules, delivery pattern and template, Judgment Node Boundary, Constraint capability, glossary, and relevant failure modes.

Confirm that one canonical Constraint Realization Map remains the delivery source, each row has one reviewable guarantee strength, and DoR, DoD, Release Gate, and runtime sections reference rather than duplicate it.

### Editing runtime material

Read the active project and delivery ownership rules, capability anatomy, Controller and Actuator guidance, relevant realization, Sensor, incident, fallback, and failure-mode material.

Confirm that runtime logic remains inside delegated authority and routes invalidating evidence to delivery, project, or organizational reassessment.

### Editing the AI Control Plane

Read the capability anatomy, glossary, all affected capability areas, both review patterns, reference architectures, failure modes, source intake, and traceability.

### Editing code, validators, workflows, or publishing infrastructure

1. read [`CONTRIBUTING.md`](CONTRIBUTING.md#code-contributions) and [`quartz/README.md`](quartz/README.md) when Quartz, publishing, site generation, or their tests are affected;
2. identify whether each changed path is Quartz-derived core, UA-owned integration, repository policy, a regression fixture, or generated output;
3. read the owning behavioral contract, relevant implementation, tests, package command, workflow, and machine-readable repository protection before editing;
4. prefer configuration or an existing UA-owned extension surface over modifying Quartz-derived core when it can satisfy the requirement without duplicating behavior;
5. document intent and non-obvious invariants rather than narrating syntax, and keep security, atomicity, provenance, compatibility, threshold, and fail-closed rationale adjacent to the code that relies on it;
6. add or update regression coverage for every externally observable behavior or defect fix, including relevant failure and preservation paths;
7. run the incremental code-quality validator, the applicable Quartz and publication tests, the production build, and any affected repository-policy suites documented in `quartz/README.md`; and
8. update the owning descriptive contract, machine-readable protection, and regression fixture together when a protected code or workflow invariant changes deliberately.

### Working with research

Start with [`content/research/index.md`](content/research/index.md), [`content/research/review-process.md`](content/research/review-process.md), and [`content/research/framework-traceability.md`](content/research/framework-traceability.md).

Record explicit accept, narrow, reject, supersede, or reopen decisions. Research does not update doctrine by implication.

## 9. Editing workflow

For repository-changing work:

1. **Understand** the architectural purpose and document class.
2. **Locate** the change on both axes: decision level and capability family/function.
3. **Identify** the owning doctrine, pattern, or module.
4. **Read** required dependencies.
5. **Search** terms, paths, near-synonyms, overlapping records, and old terminology.
6. **Classify** the entity and evidence source.
7. **Assess** status, authority, inheritance, scope, guarantee strength, and SMB proportionality.
8. **Make** the smallest coherent change on a branch.
9. **Cross-reference** affected doctrine, patterns, capabilities, failure modes, and research.
10. **Update** glossary, roadmap, changelog, or traceability where genuinely required.
11. **Declare** the change in the machine-readable `ua-change-contract` block and ensure its owning paths and companion-update fields match the PR-owned diff.
12. **Audit** terminology, links, diagrams, metadata, compatibility, mixed-strength records, duplicate artifacts, and deletion or rename consequences.
13. **Run** the applicable repository, metadata, navigation, and change-coupling validators and regression suites.
14. **Report** uncertainty, assumptions, unresolved decisions, exception use, and unavailable automated checks.
15. **Complete** the end-of-session protocol.

Additional rules:

- refine the owning document instead of creating a competing source;
- use repository-relative links;
- preserve explicit status and maturity;
- separate specification requirements from examples and vendor choices;
- avoid universal thresholds, sample sizes, risk scores, role titles, or cadences without context-derived evidence;
- preserve unresolved alternatives where evidence is incomplete;
- treat path renames and deletions as compatibility decisions, not cosmetic cleanup;
- use a Draft pull request for substantial framework changes until review criteria are satisfied;
- AI-assisted repository-policy work is identified from the actual PR-owned repository-policy surface, including `.github/`, `AGENTS.md`, `CONTRIBUTING.md`, and `DOCUMENT-METADATA.md`, as well as the declared `change_class`; a weaker declaration MUST NOT disable repository-policy controls;
- changes touching a maintained Markdown artifact whose current-target or candidate frontmatter status is `draft-normative` or `normative` are high-impact even if the PR attempts to downgrade that status in the same change; a weaker `change_class` MUST NOT disable the Draft/readiness controls;
- AI-assisted `repository-policy`, `draft-normative`, and `normative` pull requests, including those classified as high-impact from actual paths or document status, MUST remain Draft while repository-changing work is active; leaving Draft requires the CODEOWNER-controlled readiness protocol below, and any later repository head, target tip, tested-merge state, or approved PR-body state requires a fresh authorization cycle;
- `agent_assistance: none` is a maintainer-controlled, head-bound opt-out, not a self-attested bypass; except for Dependabot compatibility, a target-branch global CODEOWNER who still has current `write`, `maintain`, or `admin` repository permission and a trusted GitHub author association must explicitly authorize the opt-out for the current repository head through the structured `ua-agent-assistance-none` marker below;
- do not use an exception label as a generic bypass: each exception is category-scoped, maintainer-controlled, visible in the PR, and must be explained.

### Corrective feedback and control improvement

Treat the active maintainer conversation as a feedback surface. The contributor MUST monitor the interaction for **corrective feedback signals** indicating that its interpretation, decision, implementation, or workflow deviated from the maintainer's intended behavior.

Corrective signals are semantic, not phrase-matched. Examples include the maintainer explaining that the opposite behavior was intended, that the requested outcome was misunderstood, that an expected workflow or verification step was skipped, that the wrong source of truth was used, that scope was expanded or narrowed incorrectly, or that the maintainer expected the work to be approached in a materially different way.

For every material corrective signal:

1. reconcile it with the current repository state, the authority order in this file, explicit task authorization, and applicable repository contracts;
2. correct the current work when the signal is valid within those boundaries, or report the conflict or required decision when it is not;
3. diagnose the likely cause of the deviation rather than treating the corrected output as sufficient;
4. determine whether the cause is local to the current task or reasonably likely to recur; and
5. evaluate whether a durable control improvement is warranted.

Related corrective signals may be accumulated across several iterations of the active work when that makes the underlying failure pattern clearer. Do not manufacture a durable rule from every isolated preference, wording choice, or conversational clarification.

When a durable candidate exists, route it to the narrowest appropriate owner:

1. execution-environment bootstrap, project context, or tool routing → Project Instructions or the equivalent project-level agent configuration;
2. behavior genuinely reusable across projects or repositories → reusable/custom-agent instructions;
3. repository-wide contributor behavior → this root `AGENTS.md`;
4. subtree-specific contributor behavior → the applicable nested `AGENTS.md`;
5. project meaning, terminology, ownership, research state, publishing contract, or another canonical rule → the relevant canonical repository artifact rather than agent guidance;
6. an objectively enforceable invariant → an existing or new test, validator, policy contract, pull-request check, template, or GitHub workflow.

Prefer one canonical descriptive owner. A rule may also have a separate enforcement owner when deterministic automation verifies an observable subset. Prefer improving an existing owner or validator over creating a parallel instruction, document, workflow, or abstraction.

Before writing a **feedback-derived** change to persistent agent guidance, the contributor MUST present the candidate to the maintainer and explain:

- which corrective signal or recurring deviation exposed the candidate;
- why the problem is reasonably likely to recur or materially worth preventing;
- which control surface should own the improvement;
- the exact proposed behavioral or scope change;
- what failure mode or friction the change is expected to reduce; and
- whether deterministic enforcement is appropriate.

Apply that feedback-derived persistent-guidance improvement only after the maintainer approves the described candidate. The approval applies to the candidate that was explained; material expansion requires renewed approval.

This approval step is part of the feedback-learning loop, not a general governance requirement for editing agent guidance. When the maintainer directly requests an `AGENTS.md`, Project Instruction, or other agent-guidance change as the task itself, normal task authorization applies and no additional feedback-learning approval is required merely because the target is persistent guidance.

Do not:

- turn every one-off preference into permanent process;
- place canonical UA meaning in Project instructions, reusable agent definitions, or contributor workflow files;
- duplicate one rule across several instruction surfaces without identifying its canonical owner;
- encode subjective editorial judgment as brittle automation;
- create a new workflow when an existing validator, contract, or test can coherently own the check; or
- claim that an external Project, custom agent, repository file, check, or workflow was updated when only a recommendation was produced.

For every material durable candidate considered during the task, the session report MUST state the corrective signal or failure pattern, whether it was classified as local or durable, the proposed canonical owner, the expected improvement, automation feasibility, whether maintainer approval was required and obtained, and whether the candidate was applied, proposed, rejected, or deferred.

### Deterministic agent iteration checkpoint

This section is the canonical human-readable owner of the repository's deterministic AI-agent checked-state protocol. Machine-readable policy, validators, pull-request template fields, and GitHub Actions enforce observable parts of this protocol; they do not redefine it.

Every human-authored pull request MUST declare `agent_assistance` in its `ua-change-contract` as either `used` or `none`. The declaration makes applicability explicit but does not let the PR author disable the control loop unilaterally. Except for Dependabot compatibility, `agent_assistance: none` becomes effective only after a **target-branch global CODEOWNER with current `write`, `maintain`, or `admin` repository permission and trusted GitHub author association** adds this structured top-level PR Conversation comment bound to the exact current repository head:

```text
<!-- ua-agent-assistance-none
{
  "agent_assistance":"none",
  "head_sha":"<current-head-sha>"
}
-->
```

The authority source begins with the global `* @user` ownership declared by the current target branch's `.github/CODEOWNERS`, not a CODEOWNERS file modified by the pull request, and is narrowed by the user's current repository permission and trusted GitHub association. A stale CODEOWNERS entry after loss of write authority is insufficient. A later repository head invalidates an earlier `agent_assistance: none` approval. Existing open human-authored PRs created before `agent_assistance` was introduced are a deliberate compatibility migration: they MUST add the field on their next maintained iteration rather than being silently grandfathered.

When `agent_assistance` is `used`, the contributor MUST maintain exactly one `ua-agent-checkpoint` block. A valid checkpoint attests that the contributor re-ran the review loop against the checked PR state and is bound to:

- the PR diff-base SHA recorded by GitHub;
- the current target-branch tip SHA;
- the current PR head SHA;
- GitHub's tested merge-result SHA;
- `reviewed_pr_body_sha256`, computed from the current PR description with the checkpoint block itself removed;
- `reviewed_feedback_sha256`, computed from trusted PR review and inline-review feedback; and
- the exact blob SHA of every applicable root or nested `AGENTS.md` file in the tested merge state.

Applicable instruction scope and change-coupling scope MUST use the same definition of **PR-owned changed paths**. Compute both from the merge-base of the current target tip and PR head through the PR head. Preserve both sides of detected renames. Copy detection is not part of this contract. This prevents target-only changes already synchronized into the feature branch from becoming false PR scope in either the agent checkpoint or companion-update validator. Resolve applicable `AGENTS.md` files against the tested merge result; when the PR deletes scoped guidance, retain the governing version from the current target branch for review.

High-impact classification MUST NOT rely solely on PR-body self-declaration. Repository-policy scope is derived from the protected repository-policy surface, and maintained Markdown is treated as high-impact when either the governing current-target version or the candidate version has `status: draft-normative` or `status: normative`. Reading both sides prevents a status downgrade in the same PR from disabling the control.

Trusted GitHub maintainer feedback is an observable supplement to the external conversation feedback surface. The deterministic `reviewed_feedback_sha256` watermark includes submitted/edited/dismissed reviews and inline review comments authored with GitHub `OWNER`, `MEMBER`, or `COLLABORATOR` association, excluding bots. Those event types are attached to the PR head lifecycle and therefore can invalidate the PR-head checkpoint. Ordinary top-level PR Conversation comments remain part of the semantic feedback surface but are deliberately excluded from the feedback watermark and `issue_comment` workflow trigger because GitHub emits those workflows on the default-branch ref/SHA. The structured CODEOWNER control markers are nevertheless read from the PR Conversation during ordinary PR-head checkpoint events.

Before refreshing a checkpoint, the contributor MUST re-read the effective applicable `AGENTS.md` files, the complete PR-owned diff, the current PR description, available external corrective feedback, current trusted PR review/inline-review feedback, relevant top-level PR Conversation feedback, and this end-of-session protocol. It MUST then classify any material corrective signal as local or durable, route justified durable candidates to the proper owner, and update the checkpoint disposition truthfully.

#### Ready-for-review authorization

For AI-assisted repository-policy work inferred from PR-owned policy paths, for changes to maintained Markdown with current-target or candidate `draft-normative` / `normative` status, and for declared `repository-policy`, `draft-normative`, and `normative` changes, the PR MUST remain Draft while repository-changing work is active. Ready is a two-stage control and a bare `ready_for_review` event is not proof of maintainer authorization.

First establish a fresh checkpoint for the current head. Then a currently authorized target-branch global CODEOWNER MUST add a structured approval comment bound to that exact head, tested merge state, approved PR-description digest, and canonical SHA-256 fingerprint of the current `ua-agent-checkpoint` JSON:

```text
<!-- ua-agent-ready-approval
{
  "head_sha":"<current-head-sha>",
  "merge_sha":"<current-tested-merge-sha>",
  "pr_body_sha256":"<current-pr-body-sha256>",
  "checkpoint_sha256":"<canonical-checkpoint-sha256>"
}
-->
```

Only after that evidence exists may the AI contributor initiate `ready_for_review`, and only after explicit maintainer instruction to do so. The approval comment MUST already exist and MUST NOT have been edited after the Ready transition. The `ready_for_review` workflow run MUST itself pass the checked-state validation against the same head, merge state, PR-body digest, and checkpoint fingerprint. Only then may the separate **Agent protocol / readiness authorization** job succeed.

Durable readiness evidence is read from the PR **head SHA**, because GitHub Actions check-runs for pull requests are attached to the head SHA even when the workflow checks out `refs/pull/<n>/merge`. The evidence MUST come from the protected `.github/workflows/change-coupling.yml` pull-request run for that PR and head, with the expected `Agent protocol / readiness authorization` job and successful `Record successful head-bound readiness authorization` step. A same-named check from another workflow, another PR/head, or a different job implementation does not satisfy this control. Check-run pagination MUST be exhausted rather than assuming the evidence remains within the first 100 check-runs. The structured CODEOWNER marker separately binds the tested merge SHA and PR-body digest.

A failed or premature Ready transition MUST NOT be legalized retroactively by creating or editing an older comment after Ready. On later PR events, non-Draft state is valid only when the current head, tested merge, and PR-body digest still match the CODEOWNER approval and the verified readiness workflow evidence exists for the current Ready cycle. Review or inline-review feedback on that same authorized head may make the checkpoint stale without revoking readiness because it does not change the approved PR-body digest. A substantive PR-description edit, later repository commit/head, changed current target tip, changed tested-merge state, return to Draft followed by a new Ready cycle, or removal/edit of the matching approval requires fresh readiness authorization. Updating only the checkpoint block does not change `reviewed_pr_body_sha256` and therefore does not require a new Ready approval.

#### Trusted-base enforcement and target advance

The candidate `Change coupling` workflow provides fast PR-head evidence, regression tests, and checked-state validation, but it is not the sole trust boundary for repository-policy changes because a pull request may modify that workflow, its validators, or its contracts.

After this trusted-base guard is present on the target branch, the separate **Agent protocol / trusted-base guard** is the independent enforcement owner for non-self-modifiable classification and target-advance freshness. `.github/workflows/agent-policy-guard.yml` runs target-branch code through `pull_request_target`, checks out only the target/default branch, treats candidate files and PR text strictly as untrusted API data, and MUST NOT check out or execute candidate-branch code. It may use `statuses: write` only to publish the guard result on the PR head; candidate PR workflows remain read-only for these control surfaces.

The trusted-base guard derives repository-policy scope and `draft-normative` / `normative` document status from target-owned policy plus candidate data, validates the current target tip, head, tested merge, PR-body and review-feedback checkpoint identities, applies current CODEOWNER authority checks, and refuses to let a candidate shrink the target branch's protection set for its own review. On every push to the target `main` branch it re-evaluates all open PRs targeting `main` and refreshes **Agent protocol / trusted-base guard** status on each PR head. Therefore a base-tip or tested-merge change can invalidate a previously fresh checkpoint even when the PR head did not receive a `synchronize` event.

`ua-exception/pr-contract` is only a narrow escape for the malformed or missing `ua-change-contract` declaration. It does **not** bypass the agent checkpoint, Draft/readiness inference, current-target freshness, or trusted-base guard. When that exception is present, agent controls fail safe with `agent_assistance: used` defaults until the declaration is restored.

The initial PR that introduces the trusted-base workflow cannot be protected by that new `pull_request_target` workflow before the workflow exists on the target branch. That bootstrap limitation MUST be explicit and requires maintainer review of the bootstrap PR itself; after merge, subsequent PRs are subject to the target-owned guard. Do not represent candidate-branch unit tests of the guard as equivalent to an already-active target-branch guard.

The checkpoint and authorization surfaces reduce self-attested bypasses, but GitHub cannot cryptographically distinguish a human action from an AI action performed through the same authenticated GitHub principal. Do not claim stronger identity separation than the available GitHub evidence supports.

The checkpoint is intentionally a **checked-state** control, not proof that the model understood the prose. Deterministic validation can prove identities, scope derivation, state freshness, feedback-watermark freshness, CODEOWNER control evidence, current-head readiness/Draft state, and completed declarations. Semantic understanding, classification of external or ordinary top-level conversational corrective signals, and the quality of a durable-improvement proposal remain Model Judgment subject to maintainer review.

The existing `Change coupling` workflow listens to PR changes, trusted reviews, and trusted inline-review-comment events. Untrusted review/comment actors do not enter the checkpoint job, and workflow concurrency is partitioned by event type and actor so an untrusted event cannot cancel an active repository-state checkpoint. Top-level `issue_comment` events remain outside this deterministic PR-head workflow. The workflow uses read-only Issues access to read structured CODEOWNER authorization comments and read-only Checks access to verify durable readiness evidence; it does not grant PR-controlled code a write token for these control surfaces.

Checkpoint regression tests and repository-contract protection are part of this control surface. The repository contract MUST protect registration of `repository-contract-agent-checkpoint.json` itself and the trusted-base workflow/script wiring; mutation coverage MUST fail if either enforcement path is silently removed.

Run at minimum:

```bash
python3 .github/tests/agent_checkpoint/test_agent_checkpoint.py
python3 .github/tests/agent_checkpoint/test_feedback_context.py
python3 .github/tests/agent_checkpoint/test_trusted_base_guard.py
python3 .github/tests/agent_checkpoint/test_checkpoint_repository_contract.py
```

The live GitHub Actions run remains authoritative for PR-state, tested-merge, current-target CODEOWNER evidence, readiness workflow provenance, and trusted PR-review feedback because those inputs do not exist in an ordinary local checkout. Once the trusted-base workflow exists on `main`, its head status is additionally authoritative for target-owned classification and base-advance freshness.

## 10. End-of-session integrity protocol

### Architecture and ownership

- Every material change is located on both axes.
- Organization, architecture/project, delivery-team, and runtime decisions remain distinct.
- One canonical owner remains for each concept and decision surface.
- Project authorization and delivery release remain distinct.
- Runtime action remains inside delegated authority.
- No unnecessary namespace, role, service, register, committee, gate, or duplicate protocol was introduced.

### Terminology and capability logic

- Glossary terms are used consistently.
- Constraint and Constraint Realization are not collapsed.
- The Constraints family does not imply that a Constraint object is itself an execution mechanism.
- Controller and Actuator responsibilities are not collapsed.
- Hard and Soft claims are scoped to complete realized paths.
- Mixed-strength Constraint records are split.
- Controlled-process outputs, actions, and downstream outcomes reach Sensors where material.
- Closed-loop feedback is not confused with bounded acceptable operation.
- Generic diagrams do not imply deterministic enforcement for every Soft Constraint Realization.

### SMB proportionality

- Existing organizational records are linked rather than copied.
- One canonical Project Constraint Architecture remains at project level.
- One canonical Constraint Realization Map remains at delivery level.
- Other sections reference rather than restate those records.
- The same person may hold several responsibilities without erasing decision boundaries.
- Added process is justified by a real owner, lifecycle, consequence, authority, evidence, access, retention, or audit need.

### Repository integrity

- Relative links resolve or unavailable automated validation is stated.
- Renamed or deleted maintained paths have an explicit compatibility decision.
- Mermaid diagrams are syntactically and semantically reviewed or unavailable automated rendering is stated.
- Metadata and status are coherent.
- Active `canonical_for` claims remain unique unless an explicit exception exists.
- Protected glossary entries remain present and unique.
- Research provenance does not claim unavailable source formats or unverified review actions.
- `CHANGELOG.md` is updated for notable changes.
- Glossary, roadmap, and research traceability declarations match the actual companion-file diff.
- The `ua-change-contract` block is present exactly once, uses controlled values, declares `agent_assistance`, and names an owning path that intersects the PR-owned diff, unless the narrow PR-contract exception is explicitly applied; that exception does not disable agent controls.
- PR-owned repository-policy paths require `change_class: repository-policy`; the protected policy surface includes `.github/`, `AGENTS.md`, `CONTRIBUTING.md`, and `DOCUMENT-METADATA.md`.
- A changed maintained Markdown artifact whose target or candidate status is `draft-normative` or `normative` remains high-impact even when its candidate frontmatter or PR declaration attempts to downgrade it.
- `agent_assistance: none` is accepted only with target-branch global CODEOWNER evidence bound to the current head from a user who retains current `write`, `maintain`, or `admin` permission and trusted association, except for the explicit Dependabot compatibility path.
- When `agent_assistance` is `used`, the `ua-agent-checkpoint` is current for the checked PR state, trusted PR-review feedback, and applicable instruction blobs.
- AI-assisted high-impact work remains Draft during repository-changing iterations; a non-Draft current head requires matching CODEOWNER `ua-agent-ready-approval` evidence for the current head, tested merge and PR-body digest plus verified `Agent protocol / readiness authorization` provenance.
- Both change coupling and agent checkpoint reason over the same PR-owned `merge-base(current target tip, head) → head` diff.
- When the trusted-base guard is installed on the target branch, its PR-head status reflects current target-owned classification and is refreshed after target-branch advances; candidate workflow success does not replace that independent status.
- Any maintainer exception label is category-scoped and explained in the PR body, and a shared exception is applied consistently without expanding its category.
- PR description matches the actual diff and remaining review state.

### Session report

Summarize:

- the repository ref and applicable `AGENTS.md` files inspected;
- what changed;
- which architectural decision was made;
- which decision levels and capability families were affected;
- which files own the resulting meaning;
- which checks were performed;
- which corrective feedback signals were evaluated for durable control improvement, how each candidate was routed, and whether any required feedback-derived guidance approval was obtained;
- the `agent_assistance` declaration and any head-bound CODEOWNER opt-out evidence, checkpoint disposition, current Draft/readiness authorization state, and trusted-base guard availability/status where a pull request exists;
- what remains unresolved;
- whether the PR is still Draft or has completed the maintainer-authorized readiness protocol.

## 11. Repository contract checks

The machine-readable repository contract lives at [`.github/policy/repository-contract.json`](.github/policy/repository-contract.json). It protects critical files and sections, the top-level namespace, stable repository links, and compatibility paths. It is a repository-integrity mechanism, not a source of UA architectural meaning.

The metadata and canonical-ownership policy lives at [`.github/policy/metadata-contract.json`](.github/policy/metadata-contract.json). Its owning human-readable convention is [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md).

The diff-aware companion-update policy lives at [`.github/policy/change-coupling-contract.json`](.github/policy/change-coupling-contract.json). It validates the pull request's machine-readable declaration against the PR-owned diff derived from the merge-base of the **current target-branch tip** and PR head through the PR head, including changelog, glossary, roadmap, research traceability, compatibility, deletion, rename decisions, explicit `agent_assistance`, repository-policy classification derived from the protected policy surface, and high-impact status derived from both current-target and candidate maintained Markdown.

The deterministic AI-agent checkpoint policy lives at [`.github/policy/agent-checkpoint-contract.json`](.github/policy/agent-checkpoint-contract.json). Its canonical descriptive owner is the `Deterministic agent iteration checkpoint` section above. [`.github/scripts/validate_agent_checkpoint.py`](.github/scripts/validate_agent_checkpoint.py) validates the candidate checked-state attestation; [`.github/scripts/fetch_agent_checkpoint_context.py`](.github/scripts/fetch_agent_checkpoint_context.py) collects live PR, target-branch, Draft/readiness, tested-merge, current CODEOWNER authority, readiness workflow provenance, paginated check history, and trusted PR-review context.

The independent trusted-base policy lives in the current target branch: [`.github/workflows/agent-policy-guard.yml`](.github/workflows/agent-policy-guard.yml) invokes [`.github/scripts/validate_agent_policy_guard.py`](.github/scripts/validate_agent_policy_guard.py) through `pull_request_target` and `push` to `main`, never executes candidate code, and publishes **Agent protocol / trusted-base guard** on the PR head. [`.github/policy/repository-contract-agent-checkpoint.json`](.github/policy/repository-contract-agent-checkpoint.json) protects stable observable wiring and contract values for both control paths, including extension registration, without freezing private validator function names.

Before pushing a repository-policy change or any change that affects protected structure, metadata, canonical ownership, terminology, companion documents, or maintained paths, run:

```bash
python3 .github/scripts/validate_code_quality.py --base <current-target-tip-sha> --head <head-sha>
python3 .github/tests/code_quality/test_code_quality.py
npm test
npm run build
python3 .github/scripts/validate_repository_contract.py
python3 .github/tests/repository_contract/test_repository_contract.py
python3 .github/scripts/validate_metadata.py --mode all
python3 .github/tests/metadata_contract/test_metadata.py
python3 .github/scripts/validate_change_coupling.py --base <current-target-tip-sha> --head <head-sha> --pr-body-file <pr-body-file> --labels <comma-separated-labels>
python3 .github/tests/change_coupling/test_change_coupling.py
python3 .github/tests/agent_checkpoint/test_agent_checkpoint.py
python3 .github/tests/agent_checkpoint/test_feedback_context.py
python3 .github/tests/agent_checkpoint/test_trusted_base_guard.py
python3 .github/tests/agent_checkpoint/test_checkpoint_repository_contract.py
```

The change-coupling validator requires the current target tip, the PR head, and the pull-request declaration. GitHub Actions resolves the current target tip and supplies the pull-request body, labels, actor, and head SHA automatically. Do not substitute the historical PR `base.sha` when determining PR-owned scope after the target branch has advanced.

The `ua-change-contract` block must normally appear exactly once in the PR body. Required fields use controlled values from the policy. `owning_paths` must intersect the PR-owned diff. A notable change requires `CHANGELOG.md`; terminology, roadmap, and research-state decisions must reconcile their owning companion files when applicable. Deleting or renaming maintained material requires an explicit compatibility decision and changelog treatment.

`ua-exception/pr-contract` bypasses only the missing or malformed change-contract declaration. The agent checkpoint and trusted-base guard continue with safe agent-assisted defaults, so the exception cannot be used to suppress high-impact classification, checkpoint freshness, or Draft/readiness controls.

Maintainer exception labels are not a universal override. Each label bypasses only its declared category, repository label permissions determine who may apply it, and the reason must remain visible in the PR body. When more than one validator depends on the same prerequisite, a declared exception for that prerequisite must be reconciled consistently without silently broadening it.

The validators and self-tests use only the Python standard library and resolve the repository root from their own location.

Metadata errors are blocking. Advisory warnings identify title/H1 drift, unusually large tag sets, or selected superseded terminology and do not fail CI by default. Do not suppress a genuine warning by broadening an exception; determine whether the text is current terminology, an explicit historical reference, or a real defect.

Do not mechanically normalize preserved publication bodies, raw sources, or legacy historical material. Their provenance and publishing metadata may follow a different schema.

When a legitimate repository change adds, removes, renames, or deliberately changes a protected path, section, link, marker, metadata value, glossary entry, canonical responsibility, or change-coupling rule:

1. update the owning document first;
2. update the relevant machine-readable contract in the same pull request;
3. add or modify a regression fixture showing the old failure and the intended new baseline;
4. when `canonical_for` responsibility moves, retire or remove the old active claim explicitly;
5. explain the compatibility and ownership decision in the pull-request description;
6. update `CHANGELOG.md`, and `ROADMAP.md` when the repository-tooling baseline changes;
7. ensure the final `ua-change-contract` declaration matches the complete diff.

Do not weaken or bypass a contract merely to make a failing check green. Determine whether the repository change is wrong, the contract is stale, or an explicit compatibility decision is required.
