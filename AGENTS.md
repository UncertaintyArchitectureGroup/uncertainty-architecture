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

## 1. Purpose and boundary

This file defines how language models, coding agents, automated reviewers, and other AI-assisted contributors should work inside the Uncertainty Architecture repository.

It is **operational guidance**, not normative UA specification content. It must not override:

1. [`SPECIFICATION.md`](SPECIFICATION.md);
2. explicit document status and normative language;
3. the relevant module boundary;
4. canonical definitions in [`00-doctrine/glossary.md`](00-doctrine/glossary.md);
5. the owning doctrine or pattern.

Use this file to determine what to read, where a change belongs, how to preserve ownership and provenance, and how to finish a repository-changing session.

Do not use this file as a second glossary or specification entry point.

## 2. Repository mission

UA is an open doctrine and pattern language for building and operating **Thinking Systems**: software in which part of runtime behavior depends on probabilistic Model Judgment while consequential deterministic responsibilities remain explicit and governable.

UA is not an SDK, universal agent framework, vendor architecture, prompt collection, evaluation method, compliance certification, or replacement for product discovery, Agile, DevOps, QA, security, change management, or incident response.

Current terminology and conceptual claims belong to the glossary and doctrine, not to this protocol.

## 3. Required mental models

Before changing framework material, identify two independent dimensions.

### 3.1 Decision level

Use [`00-doctrine/nested-control-lifecycle.md`](00-doctrine/nested-control-lifecycle.md) to identify whether the decision belongs to:

1. organizational control context;
2. project control architecture and viability;
3. delivery-level Thinking System Review;
4. runtime control and reauthorization.

### 3.2 Capability family and function

Use [`00-doctrine/control-loop-anatomy.md`](00-doctrine/control-loop-anatomy.md) to identify whether the change concerns:

- Constraints and their realizations;
- Sensors and evidence;
- Controllers and decision authority;
- Actuators and corrective action.

The Constraints family is intentionally composite: the Constraint is the authoritative boundary object, while the Constraint Realization is the operational mechanism. Do not collapse them.

Do not collapse decision levels into capability layers. Do not treat directory numbering as an execution order or physical topology.

## 4. Authority and conflict resolution

When documents conflict, use this order:

1. [`SPECIFICATION.md`](SPECIFICATION.md) for scope, status, conformance, and change control.
2. Explicit document status and normative language.
3. The relevant module README for module purpose and boundaries.
4. [`00-doctrine/glossary.md`](00-doctrine/glossary.md) for terms it defines.
5. Current doctrine for architectural meaning.
6. The owning project or delivery pattern for its decision surface.
7. The relevant AI Control Plane capability document for capability-specific guidance.
8. [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) for metadata and tags.
9. Research, history, talks, implementations, templates, and examples for evidence and context.
10. This file for repository workflow only.

Additional rules:

- explicit status takes precedence over directory name;
- normative content takes precedence over conflicting lower-status content;
- draft-normative content must not be presented as stable;
- templates mirror patterns and do not create independent protocols;
- named technologies and presentation metaphors do not become requirements by implication;
- report genuine contradictions instead of silently selecting one side.

## 5. Repository invariants

1. One canonical concept should have one authoritative definition.
2. One decision surface should have one owning pattern.
3. Doctrine defines foundational distinctions; lower modules apply rather than redefine them.
4. The glossary owns canonical terminology where an entry exists.
5. The Project Control Architecture and Viability Review owns project authorization, project Constraint architecture, inheritance, and reauthorization.
6. The Thinking System Review owns delivery realization, DoR, DoD, Release Gate, and local reassessment.
7. AI Control Plane documents define logical capability families, not one product topology.
8. Constraint, Constraint Realization, Sensor, Controller, and Actuator must remain distinguishable.
9. A Controller selects or authorizes; an Actuator executes.
10. Hard or soft is a scoped claim about a Constraint and its complete realized path, not an intrinsic property of policy prose.
11. Different guarantee strengths across subjects, paths, or scopes require separate Constraint claims rather than one mixed hard/soft record.
12. A lower-level decision may narrow but must not silently weaken or expand a higher-level authorization or Hard Constraint.
13. Higher-level decisions flow downward by reference; invalidating evidence flows upward.
14. Reference architectures illustrate compositions and do not become mandatory.
15. Failure modes describe reusable mechanisms of loss of control, not isolated undesirable outputs.
16. Research provides evidence and candidates; it is not automatically specification.
17. Historical and raw material preserves original wording and provenance.
18. Navigation, metadata, tags, recency, and publishing infrastructure do not create authority.
19. Repository growth should occur through coherent refinement rather than namespace proliferation.
20. Every notable repository or specification-artifact change must be recorded in [`CHANGELOG.md`](CHANGELOG.md).

## 6. Repository map and placement rules

### Public entry points

- [`README.md`](README.md) — public landing page and navigation.
- [`SPECIFICATION.md`](SPECIFICATION.md) — specification boundary and status model.
- [`ROADMAP.md`](ROADMAP.md) — development direction.
- [`CHANGELOG.md`](CHANGELOG.md) — notable repository changes.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution workflow.
- [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) — metadata and controlled tags.
- [`AGENTS.md`](AGENTS.md) — this operational protocol.

### `00-doctrine/`

Owns foundational concepts, distinctions, relationships, and terminology.

Place material here when it defines or materially changes:

- Thinking Systems and the controlled-object shift;
- the Nested Control Lifecycle;
- the Control-Loop Capability Anatomy;
- Deterministic Core, Model Judgment, Uncertainty Boundary, Invariant, Constraint, Constraint Realization, Requirement, Operating Envelope, Correctness, Bug, or Human Authority;
- other control-oriented first principles.

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

The Constraints directory owns the composite Constraint and Constraint Realization family. The directory numbers are navigation only. Named tools remain examples.

### `03-reference-architectures/`

Owns non-prescriptive worked compositions. References must distinguish requirements from illustrative choices and must not introduce local doctrine.

### `04-failure-modes/`

Owns recurring mechanisms by which structural, semantic, operational, economic, or organizational control is lost.

### `content/research/`

Owns research, notes, synthesis, critique, provenance, and research-to-framework traceability. Research informs explicit decisions; it does not update doctrine by implication.

### `content/history/` and `content/raw/`

Preserve chronology, external context, original claims, and source snapshots. Do not normalize raw or historical wording in place.

## 7. Terminology protocol

Before introducing, redefining, replacing, deprecating, or narrowing a UA term:

1. read the complete glossary;
2. search current framework material and near-synonyms;
3. identify the owning module and decision level;
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
- turn a memorable phrase, slide label, or product category into a canonical term without a durable distinction.

Use **Thinking Systems** in current framework material. Preserve **Behavioral Software** and **Behavioral Applications** in historical titles, quotations, raw sources, and provenance records.

## 8. Constraint-specific review protocol

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

If the questions cannot be answered, preserve the item as a research candidate, unresolved dependency, or Soft Constraint rather than presenting it as an operable guarantee.

## 9. Capability classification protocol

Classify by function in the specific system, not by tool name.

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

## 10. Task-specific reading paths

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

Read `SPECIFICATION.md`, relevant doctrine, the complete glossary, both review patterns, the AI Control Plane, affected failure modes, research traceability, roadmap, and changelog.

### Editing project review material

Read the controlled-object doctrine, capability anatomy, lifecycle, project pattern and template, delivery pattern, Constraint capability, relevant failure modes, and traceability.

Confirm that the change concerns project viability, project Constraint architecture, authorization, inheritance, or reauthorization and remains proportional for SMB use.

### Editing delivery review material

Read the project pattern and inheritance rules, delivery pattern and template, Judgment Node Boundary, Constraint capability, glossary, and relevant failure modes.

Confirm that one canonical Constraint Realization Map remains the delivery source, that each row has one reviewable guarantee strength, and that DoR, DoD, Release Gate, and runtime sections reference rather than duplicate it.

### Editing the AI Control Plane

Read the capability anatomy, glossary, all affected capability areas, both review patterns, reference architectures, failure modes, source intake, and traceability.

### Working with research

Start with [`content/research/index.md`](content/research/index.md), [`content/research/review-process.md`](content/research/review-process.md), and [`content/research/framework-traceability.md`](content/research/framework-traceability.md).

Classify each candidate as concept, artifact, responsibility, process, technical reference, pattern, failure mode, or reference architecture. Record explicit accept, narrow, reject, supersede, or reopen decisions.

## 11. Editing rules

- Prefer the smallest coherent architectural decision.
- Refine the owning document instead of creating a competing source.
- Use repository-relative links.
- Preserve explicit status and maturity.
- Keep templates informative and aligned with their patterns.
- Link higher-level decisions and evidence rather than copying them.
- Separate specification requirements from examples and vendor choices.
- Avoid universal thresholds, sample sizes, risk scores, role titles, or cadences without context-derived evidence.
- Preserve uncertainty and unresolved alternatives where evidence is incomplete.
- Update module indexes, navigation, roadmap, changelog, and traceability only when their state genuinely changes.
- Treat path renames as compatibility decisions, not cosmetic cleanup.

## 12. Contribution workflow

For repository-changing work:

1. **Understand** the architectural purpose and document class.
2. **Identify** decision level and capability family/function.
3. **Locate** the owning doctrine, pattern, or module.
4. **Read** required dependencies.
5. **Search** terms, paths, near-synonyms, and overlapping records.
6. **Classify** the entity and evidence source.
7. **Assess** status, authority, inheritance, scope, and guarantee strength.
8. **Make** the smallest coherent change on a branch.
9. **Cross-reference** affected doctrine, patterns, capabilities, failure modes, and research.
10. **Update** glossary, roadmap, changelog, or traceability where required.
11. **Audit** terminology, links, diagrams, metadata, compatibility, and mixed-strength records.
12. **Report** uncertainty, assumptions, and unresolved decisions.
13. **Complete** the end-of-session protocol.

Substantial framework changes should use a Draft pull request until review criteria are satisfied.

## 13. End-of-session integrity protocol

Before completing a repository-changing session, verify:

### Placement and ownership

- Each file is in the correct module.
- One canonical owner remains for each concept and decision surface.
- No unnecessary namespace or duplicate protocol was introduced.
- Project and delivery ownership remain distinct.

### Terminology and architecture

- Glossary terms are used consistently.
- Constraint and Constraint Realization are not collapsed.
- The Constraints capability family does not imply that a Constraint object is itself an execution mechanism.
- Controller and Actuator responsibilities are not collapsed.
- Hard and Soft Constraint claims are scoped to complete realized paths.
- Mixed-strength Constraint records are split.
- Capability diagrams include reference conditions, evidence, decision authority, and execution paths.
- Closed-loop feedback is not confused with bounded safe operation.

### Proportionality

- Project and delivery artifacts remain usable by SMB teams.
- One canonical Project Constraint Architecture remains at project level.
- One canonical Constraint Realization Map remains at delivery level.
- Other sections reference rather than restate those records.

### Repository integrity

- Relative links resolve.
- Renamed paths have an explicit compatibility decision.
- Mermaid diagrams are syntactically and semantically reviewed.
- Generic diagrams do not imply deterministic enforcement for every Soft Constraint Realization.
- Metadata and status are coherent.
- Research provenance does not claim unavailable source formats or unverified review actions.
- `CHANGELOG.md` is updated for notable changes.
- PR description matches the actual diff and remaining review state.

### Session report

Summarize:

- what changed;
- which architectural decision was made;
- which files own the new meaning;
- which checks were performed;
- what remains unresolved;
- whether the PR is still Draft or ready for review.
