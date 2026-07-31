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

Use this file to determine what to read, where a change belongs, how to preserve ownership and provenance, how much process is justified, and how to finish a repository-changing session.

Do not use this file as a second glossary, a second specification, or a source of new governance requirements.

When documents conflict, use this order:

1. `SPECIFICATION.md` for scope, status, conformance, and change control;
2. explicit document status and normative language;
3. the relevant module README;
4. the glossary for terms it defines;
5. current doctrine for architectural meaning;
6. the owning project or delivery pattern for its decision surface;
7. the relevant AI Control Plane capability document;
8. `DOCUMENT-METADATA.md` for metadata and controlled tags;
9. research, history, talks, implementations, templates, and examples for evidence and context;
10. this file for repository workflow only.

Report genuine contradictions instead of silently selecting one side.

## 2. Repository mission and SMB default

UA is an open doctrine and pattern language for engineering and operating **Thinking Systems**: software in which part of runtime behavior depends on probabilistic Model Judgment while consequential deterministic responsibilities remain explicit and governable.

UA is not an SDK, universal agent framework, vendor architecture, prompt collection, evaluation method, compliance certification, or replacement for product discovery, Agile, DevOps, QA, security, change management, or incident response.

Unless a document explicitly requires otherwise, contributors MUST assume a small or medium-sized organization with limited specialist capacity.

The default SMB operating model is:

1. reuse and link existing organizational sources rather than recreating them;
2. maintain one living project-level decision surface;
3. maintain one living delivery-level decision surface for each bounded delivery scope;
4. connect runtime evidence and actions to the active project, delivery, realization, and deployment versions;
5. add roles, files, registers, services, committees, or gates only when an independent owner, lifecycle, authority, retention need, access boundary, or audit requirement makes them necessary.

The same person may carry several responsibility bundles. A founder may hold organizational and project authority; a technical lead may carry architecture and delivery responsibilities; an on-call engineer may perform a runtime Controller function.

Combining responsibilities does not collapse decisions. The organizational boundary, project authorization, delivery release, and runtime action remain distinguishable even when one person participates in all four.

Do not import enterprise-governance structure by default. UA does not require a governance department, mandatory specialist titles, a standing committee, a separate Constraint Register, a separate risk register, a RACI, one file per gate, or one service per capability family.

Increase process depth only when consequence, authority, exposure, irreversibility, uncertainty, feedback latency, realization difficulty, Human Authority load, operating capacity, or control economics justify it.

## 3. The two-axis architecture

Before changing framework material, locate the change on two independent axes:

1. **decision level** — where the decision is owned;
2. **capability family and function** — how the decision is made operational.

These axes are orthogonal. The four decision levels are not capability layers. The four capability families are not organizational levels, mandatory products, or a fixed execution sequence.

### 3.1 Four decision levels in practical SMB terms

| Practical level | UA decision level | Decision owned | Default SMB responsibility | Canonical record |
|---|---|---|---|---|
| **Organization** | Organizational control context | Authoritative boundaries, shared capabilities, approved vendors or deployment modes, decision rights, exception authority | Founder, owner, product authority, or existing legal/security/operations responsibility; not necessarily a department | Existing authoritative sources linked by reference; no new UA organization file required by default |
| **Architecture / project** | Project control architecture and viability | Whether the proposed Thinking System has a credible, operable, and economically viable control architecture; authorization, conditions, redesign, deferral, or No-Go | Architect, technical lead, project owner, or another person carrying the architectural decision responsibility | [`Project Control Architecture and Viability Review`](01-patterns/project-control-architecture-and-viability-review.md) |
| **Delivery team** | Delivery-level Thinking System Review | How inherited Constraints are realized, tested, completed, released, and locally reassessed for a bounded scope | The delivery team using existing product, engineering, QA, security, and operational responsibilities | [`Thinking System Review`](01-patterns/thinking-system-review.md) |
| **Runtime** | Runtime operation and reassessment | Whether active operation remains inside the approved boundary; what must be corrected, contained, rolled back, disabled, or escalated | Automated logic, on-call or operational responsibility, Human Authority, or a combination | Runtime evidence and actions linked to active project and delivery versions; no separate runtime register required by default |

“Architect” describes a decision responsibility, not a mandatory job title. The relevant person must be able to make or obtain the project-level architecture and viability decision.

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

One component or person may perform several functions. One function may be distributed. The evidence, authority, and failure responsibilities must still remain distinguishable.

### 3.3 The four-by-four review matrix

The four capability families may appear at every decision level. Contributors should use this matrix as a reasoning check, not as a requirement to create sixteen components or sixteen documents.

| Decision level | Constraints and realizations | Sensors and evidence | Controllers and authority | Actuators and action |
|---|---|---|---|---|
| **Organization** | Legal, contractual, security, privacy, procurement, prohibited-use, vendor, geography, and shared-capability boundaries | Cross-project incidents, audits, regulatory or vendor change, portfolio evidence, capability health | Authorized organizational owner or existing decision process | Change an authoritative source, approved vendor, shared capability, funding, exception, or project permission |
| **Architecture / project** | One Project Constraint Architecture derived from organizational sources and project risk | Scenario evidence, feasibility, feedback latency, capacity, control economics, and residual exposure | Project architecture and authorization authority | Authorize, narrow, condition, redirect to research, redesign, defer, escalate, or reject the AI path |
| **Delivery team** | One Constraint Realization Map for the bounded delivery scope | Deterministic tests, evaluations, behavioral evidence, realization health, false blocks, and operational readiness | Delivery and release decision authority inside the project baseline | Implement, configure, deploy, block, narrow exposure, fall back, roll back, or request project reauthorization |
| **Runtime** | Active Constraint sources, realization versions, Operating Envelope, permissions, limits, and deployment boundary | Telemetry, outcomes, incidents, violations, bypass, drift, capacity, Human Authority, and Actuator-effect evidence | Runtime software, operational owner, Human Authority, incident process, or a combination | Reject, contain, compensate, route to fallback, change configuration within authority, roll back, disable, stop, or escalate |

Ask both questions for every material change:

1. **Who owns this decision and at which level?**
2. **Which capability function defines the boundary, produces evidence, decides, and executes?**

A framework change is incomplete when it answers only one of these questions.

## 4. Canonical ownership and repository invariants

1. One canonical concept should have one authoritative definition.
2. One decision surface should have one owning pattern.
3. Doctrine defines foundational distinctions; lower modules apply rather than redefine them.
4. The glossary owns canonical terminology where an entry exists.
5. The Project Control Architecture and Viability Review owns project viability, project Constraint architecture, authorization, inheritance, and reauthorization.
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

## 5. Repository map and placement rules

### Public entry points

- [`README.md`](README.md) — public landing page and navigation.
- [`SPECIFICATION.md`](SPECIFICATION.md) — specification boundary and status model.
- [`ROADMAP.md`](ROADMAP.md) — development direction.
- [`CHANGELOG.md`](CHANGELOG.md) — notable repository changes.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution workflow.
- [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) — metadata and controlled tags.
- [`AGENTS.md`](AGENTS.md) — this operational protocol.

### `00-doctrine/`

Owns foundational concepts, distinctions, relationships, and terminology, including Thinking Systems, the controlled-object shift, the Nested Control Lifecycle, the Control-Loop Capability Anatomy, Constraints, Requirements, Operating Envelopes, Correctness, Bugs, and Human Authority.

Do not place checklists, vendor recipes, isolated examples, raw notes, or one-off project procedures here.

### `01-patterns/`

Owns reusable socio-technical responses:

- [`Project Control Architecture and Viability Review`](01-patterns/project-control-architecture-and-viability-review.md);
- [`Judgment Node Boundary`](01-patterns/judgment-node-boundary.md);
- [`Thinking System Review`](01-patterns/thinking-system-review.md).

Patterns should expose context, problem, forces, response, evidence, decision rights, economics where material, consequences, and limitations.

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

## 6. Terminology and Constraint review

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

When a change creates or modifies a material Constraint, answer:

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

## 7. Capability classification and diagram rules

Classify by function in the specific system, not by tool name, team name, or market category.

Check:

- what approved boundary exists;
- which realization implements or influences it;
- which evidence is produced;
- which function compares or interprets that evidence;
- which decision right exists;
- which mechanism executes change;
- what happens when each part fails.

For evaluation systems, distinguish:

```text
Evaluator and metrics → Sensor
Decision logic selecting block/canary/release → Controller
Deployment, blocking, exposure change, or rollback → Actuator
```

One product may package several functions.

For Mermaid and other architecture diagrams:

- show reference conditions or approved intent reaching the relevant Controller;
- show evidence reaching decision authority;
- show authorized action reaching an Actuator;
- show the Actuator changing operation or a Constraint Realization;
- show realization state and Actuator effects returning as evidence where material;
- use `enforces or influences` and `may gate` in generic diagrams;
- use deterministic language such as `bounds`, `blocks`, or `gates` only when a scoped Hard Constraint and complete realized path justify it;
- do not draw the four capability families as a mandatory vertical execution sequence;
- do not draw the four decision levels as a one-way delivery waterfall without upward reassessment paths.

A closed feedback loop is not automatically a bounded acceptable UA control architecture.

## 8. SMB artifact and process rules

Use the smallest set of records that preserves the decisions:

```text
Existing organizational sources
→ one living Project Control Architecture and Viability Review
→ one living Thinking System Review per bounded delivery scope
→ linked runtime evidence, decisions, and actions
```

Default rules:

- link organizational sources instead of copying them;
- maintain one canonical Project Constraint Architecture at project level;
- maintain one canonical Constraint Realization Map at delivery level;
- make Judgment Nodes, DoR, DoD, Release Gate, and runtime sections reference Constraint IDs rather than repeat definitions;
- use existing issue trackers, architecture records, CI, evaluation stores, observability, and incident systems where they already have an owner and lifecycle;
- preserve versioned snapshots only at material decisions or changes;
- allow the same person to fill several responsibility bundles while keeping decision authority explicit;
- add a separate file, register, service, committee, or role only when the existing two decision surfaces and linked evidence cannot preserve ownership, lifecycle, access, retention, or traceability.

Templates are informative working representations. They must not create stricter requirements than their owning patterns.

## 9. Task-specific reading paths

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

Classify each candidate as concept, artifact, responsibility, process, technical reference, pattern, failure mode, or reference architecture. Record explicit accept, narrow, reject, supersede, or reopen decisions.

## 10. Editing and contribution workflow

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
11. **Audit** terminology, links, diagrams, metadata, compatibility, mixed-strength records, and duplicate artifacts.
12. **Report** uncertainty, assumptions, unresolved decisions, and unavailable automated checks.
13. **Complete** the end-of-session protocol.

Additional editing rules:

- refine the owning document instead of creating a competing source;
- use repository-relative links;
- preserve explicit status and maturity;
- separate specification requirements from examples and vendor choices;
- avoid universal thresholds, sample sizes, risk scores, role titles, or cadences without context-derived evidence;
- preserve unresolved alternatives where evidence is incomplete;
- treat path renames as compatibility decisions, not cosmetic cleanup;
- use a Draft pull request for substantial framework changes until review criteria are satisfied.

## 11. End-of-session integrity protocol

Before completing a repository-changing session, verify:

### Architecture and ownership

- Every material change is located on both axes.
- Organizational, project architecture, delivery team, and runtime decisions remain distinct.
- Each file is in the correct module.
- One canonical owner remains for each concept and decision surface.
- No unnecessary namespace, role, service, register, committee, gate, or duplicate protocol was introduced.
- Project authorization and delivery release remain distinct.
- Runtime action remains inside delegated authority.

### Terminology and capability logic

- Glossary terms are used consistently.
- Constraint and Constraint Realization are not collapsed.
- The Constraints family does not imply that a Constraint object is itself an execution mechanism.
- Controller and Actuator responsibilities are not collapsed.
- Hard and Soft claims are scoped to complete realized paths.
- Mixed-strength Constraint records are split.
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
- Renamed paths have an explicit compatibility decision.
- Mermaid diagrams are syntactically and semantically reviewed or unavailable automated rendering is stated.
- Metadata and status are coherent.
- Research provenance does not claim unavailable source formats or unverified review actions.
- `CHANGELOG.md` is updated for notable changes.
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
