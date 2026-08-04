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

## 2. Repository mission and SMB default

UA is an open doctrine and pattern language for engineering and operating **Thinking Systems**: software in which part of runtime behavior depends on probabilistic Model Judgment while consequential deterministic responsibilities remain explicit and governable.

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
11. **Declare** the change in the machine-readable `ua-change-contract` block and ensure its owning paths and companion-update fields match the actual diff.
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
- do not use an exception label as a generic bypass: each exception is category-scoped, maintainer-controlled, visible in the PR, and must be explained.

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
- The `ua-change-contract` block is present exactly once, uses controlled values, and names an owning path that intersects the diff.
- Any maintainer exception label is category-scoped and explained in the PR body.
- PR description matches the actual diff and remaining review state.

### Session report

Summarize:

- what changed;
- which architectural decision was made;
- which decision levels and capability families were affected;
- which files own the resulting meaning;
- which checks were performed;
- what remains unresolved;
- whether the PR is still Draft or ready for review.

## 11. Repository contract checks

The machine-readable repository contract lives at [`.github/policy/repository-contract.json`](.github/policy/repository-contract.json). It protects critical files and sections, the top-level namespace, stable repository links, and compatibility paths. It is a repository-integrity mechanism, not a source of UA architectural meaning.

The metadata and canonical-ownership policy lives at [`.github/policy/metadata-contract.json`](.github/policy/metadata-contract.json). Its owning human-readable convention is [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md).

The diff-aware companion-update policy lives at [`.github/policy/change-coupling-contract.json`](.github/policy/change-coupling-contract.json). It validates the pull request's machine-readable declaration against the actual git diff, including changelog, glossary, roadmap, research traceability, compatibility, deletion, and rename decisions.

Before pushing a repository-policy change or any change that affects protected structure, metadata, canonical ownership, terminology, companion documents, or maintained paths, run:

```bash
python3 .github/scripts/validate_repository_contract.py
python3 .github/tests/repository_contract/test_repository_contract.py
python3 .github/scripts/validate_metadata.py --mode all
python3 .github/tests/metadata_contract/test_metadata.py
python3 .github/scripts/validate_change_coupling.py --base <base-sha> --head <head-sha> --pr-body-file <pr-body-file> --labels <comma-separated-labels>
python3 .github/tests/change_coupling/test_change_coupling.py
```

The change-coupling validator requires a real base/head diff and the pull-request declaration. GitHub Actions supplies the pull-request body, labels, and commit SHAs automatically.

The `ua-change-contract` block must appear exactly once in the PR body. Required fields use controlled values from the policy. `owning_paths` must intersect the actual diff. A notable change requires `CHANGELOG.md`; terminology, roadmap, and research-state decisions must reconcile their owning companion files when applicable. Deleting or renaming maintained material requires an explicit compatibility decision and changelog treatment.

Maintainer exception labels are not a universal override. Each label bypasses only its declared category, repository label permissions determine who may apply it, and the reason must remain visible in the PR body.

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
