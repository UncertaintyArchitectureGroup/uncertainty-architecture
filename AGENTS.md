---
title: Operational Protocol for AI Contributors
artifact_type: repository-guide
status: informative
maturity: active
module: repository
topics:
  - repository-architecture
  - contribution-workflow
  - terminology
  - project-authorization
  - delivery-review
  - runtime-control
  - constraints
  - evidence
tags:
  - ua/module/repository
  - ua/type/repository-guide
  - ua/status/informative
  - ua/topic/repository-architecture
  - ua/topic/contribution-workflow
  - ua/topic/terminology
  - ua/topic/project-authorization
  - ua/topic/delivery-review
  - ua/topic/runtime-control
canonical_for:
  - ai-contributor-protocol
---

# Operational Protocol for AI Contributors

## 1. Purpose and authority

This file is the operational protocol for AI contributors working in the Uncertainty Architecture repository. It does not replace the specification, doctrine, glossary, or module ownership rules.

Read [`SPECIFICATION.md`](SPECIFICATION.md), [`00-doctrine/glossary.md`](00-doctrine/glossary.md), [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md), and the owning module before making substantive changes.

The repository is maintainer-led. Vitalii Oborskyi retains final authority over repository scope and merges. Tags, recency, external visibility, generated summaries, or model confidence do not create normative authority.

## 2. Project context

Uncertainty Architecture is an open engineering specification for designing and operating Thinking Systems: software systems in which probabilistic Model Judgment participates in business or operational behavior.

The framework treats governance as control architecture. It distinguishes:

- deterministic software from probabilistic Model Judgment;
- Requirements and Operating Envelopes from implementation mechanisms;
- Constraints from Constraint Realizations;
- Sensors and evidence from Controllers and decision authority;
- Controllers from Actuators and corrective execution;
- organization, project, delivery, and runtime decisions;
- project authorization from delivery release;
- runtime operation from project reauthorization.

The practical default is SMB-first: one living project review, one living delivery review, one Project Constraint Architecture, one delivery Constraint Realization Map, and explicit evidence and authority boundaries without unnecessary governance machinery.

## 3. Normative and evidence boundaries

Normative authority comes from the status model in [`SPECIFICATION.md`](SPECIFICATION.md) and owning module documents. Research, publications, talks, examples, external references, and history may support or challenge the framework but do not change it by implication.

Use the research review process when evidence changes a question state. Record explicit accept, narrow, reject, supersede, or reopen decisions in [`content/research/framework-traceability.md`](content/research/framework-traceability.md) when required.

Do not convert a source metaphor, vendor implementation, role title, threshold, or workflow into a universal requirement without explicit architectural justification.

## 4. Canonical ownership and invariants

Preserve one canonical owner for each concept and decision surface.

Core invariants:

- Thinking System is the current system-category term.
- Model Judgment is probabilistic judgment delegated to a model or model-mediated mechanism.
- A Constraint is an authoritative boundary or condition.
- A Constraint Realization is the operational mechanism that implements or enforces a Constraint.
- Hard or Soft is a scoped claim about a Constraint and its complete realized path.
- A Sensor produces evidence.
- A Controller compares evidence with reference conditions and selects or authorizes action.
- An Actuator executes authorized change.
- Project authorization and delivery release remain separate.
- Runtime reassessment may route evidence upward but does not silently reauthorize a project.
- Metadata, tags, recency, or location do not create authority.

Refine the owning document rather than creating a competing source. When canonical responsibility moves, remove or retire the old active `canonical_for` claim explicitly.

## 5. Repository placement map

- `SPECIFICATION.md` — specification boundary, status model, conformance, and change control.
- `00-doctrine/` — canonical concepts and glossary.
- `01-patterns/` — reusable review and architecture patterns.
- `02-ai-control-plane/` — capability-family guidance.
- `03-reference-architectures/` — informative placement examples.
- `04-failure-modes/` — failure taxonomy and anti-patterns.
- `content/research/` — publications, notes, analyses, review process, and traceability.
- `content/raw/` — preserved source snapshots and provenance.
- `content/history/` — project history and external-recognition records.
- `assets/` — diagrams and visual material.
- `.github/policy/`, `.github/scripts/`, `.github/tests/`, `.github/workflows/` — deterministic repository-integrity controls.

Do not create a new top-level namespace unless no existing canonical location fits and the repository contract is deliberately updated.

## 6. Terminology and Constraint protocol

Use glossary terms exactly where they carry architectural meaning.

Do not collapse:

- Requirement into Constraint;
- Constraint into Constraint Realization;
- Sensor into Controller;
- Controller into Actuator;
- evidence into decision authority;
- DoD into Release Gate;
- runtime reassessment into project reauthorization.

When describing a Hard Constraint, state subject, path, scope, assumptions, and enforcement boundary. If one source condition has different guarantee strengths across subjects, paths, or scopes, split the records.

Use **Thinking Systems** in current framework material. Preserve **Behavioral Software** and **Behavioral Applications** only in explicit historical, publication, quotation, or provenance context.

## 7. Architecture and diagram protocol

Classify each change on two axes:

1. decision level: organization, project, delivery, or runtime;
2. capability family or function: Constraints, Sensors, Controllers, or Actuators.

Do not draw the four capability families as a mandatory vertical execution sequence. Do not draw the four decision levels as a one-way waterfall without reassessment paths.

For Mermaid and other architecture diagrams:

- show reference conditions or approved intent reaching the relevant Controller;
- show actual outputs, actions, and downstream outcomes reaching Sensors where material;
- show evidence reaching decision authority;
- show authorized action reaching an Actuator;
- show the Actuator changing operation or a Constraint Realization;
- show realization state and Actuator effects returning as evidence where material;
- use `enforces or influences` and `may gate` in generic diagrams;
- use deterministic language only when a scoped Hard Constraint and complete realized path justify it.

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

### Editing delivery-team material

Read the project pattern and inheritance rules, delivery pattern and template, Judgment Node Boundary, Constraint capability, glossary, and relevant failure modes.

### Editing runtime material

Read the active project and delivery ownership rules, capability anatomy, Controller and Actuator guidance, relevant realization, Sensor, incident, fallback, and failure-mode material.

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
8. **Determine coupling** from the intended diff: changelog, glossary, roadmap, research traceability, compatibility, and canonical ownership.
9. **Make** the smallest coherent change on a branch.
10. **Cross-reference** affected doctrine, patterns, capabilities, failure modes, and research.
11. **Update** required companion files in the same pull request.
12. **Complete** the human-readable PR fields and machine-readable `ua-change-contract` block.
13. **Audit** terminology, links, diagrams, metadata, compatibility, mixed-strength records, duplicate artifacts, and declared owning paths.
14. **Run** repository, metadata, navigation, and diff-aware coupling validators.
15. **Report** uncertainty, assumptions, unresolved decisions, exception labels, and unavailable automated checks.
16. **Complete** the end-of-session protocol.

Additional rules:

- refine the owning document instead of creating a competing source;
- use repository-relative links;
- preserve explicit status and maturity;
- separate specification requirements from examples and vendor choices;
- avoid universal thresholds, sample sizes, risk scores, role titles, or cadences without context-derived evidence;
- preserve unresolved alternatives where evidence is incomplete;
- treat path renames as compatibility decisions, not cosmetic cleanup;
- use a Draft pull request for substantial framework changes until review criteria are satisfied.

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
- Controller and Actuator responsibilities are not collapsed.
- Hard and Soft claims are scoped to complete realized paths.
- Controlled-process outputs, actions, and downstream outcomes reach Sensors where material.
- Closed-loop feedback is not confused with bounded acceptable operation.

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
- Glossary, roadmap, and traceability declarations match the actual companion-file diff.
- The `ua-change-contract` block is valid, controlled, and intersects the actual owning paths.
- Any maintainer exception label is category-specific and explained in the PR body.
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

The diff-aware change-coupling policy lives at [`.github/policy/change-coupling-contract.json`](.github/policy/change-coupling-contract.json). It validates the pull-request declaration against the actual diff and enforces required companion updates, research-state traceability, and compatibility decisions.

Before pushing a repository-policy change or any change that affects protected structure, metadata, canonical ownership, terminology, or companion-update coupling, run:

```bash
python3 .github/scripts/validate_repository_contract.py
python3 .github/tests/repository_contract/test_repository_contract.py
python3 .github/scripts/validate_metadata.py --mode all
python3 .github/tests/metadata_contract/test_metadata.py
python3 .github/scripts/validate_change_coupling.py \
  --base origin/main \
  --head HEAD \
  --pr-body-file /path/to/pr-body.md
python3 .github/tests/change_coupling/test_change_coupling.py
```

The validators and self-tests use only the Python standard library and resolve the repository root from their own location.

Metadata errors are blocking. Advisory warnings identify title/H1 drift, unusually large tag sets, or selected superseded terminology and do not fail CI by default.

Diff-aware coupling errors are blocking. Exception labels bypass only their declared category and require maintainer authority plus an explicit PR explanation. Do not apply a broad or unrelated exception merely to make a failing check green.

When a legitimate repository change adds, removes, renames, or deliberately changes a protected path, section, link, marker, metadata value, glossary entry, canonical responsibility, or change-coupling rule:

1. update the owning document first;
2. update the relevant machine-readable contract in the same pull request;
3. add or modify a regression fixture showing the old failure and the intended new baseline;
4. when `canonical_for` responsibility moves, retire or remove the old active claim explicitly;
5. explain the compatibility and ownership decision in the pull-request description;
6. update `CHANGELOG.md`, and `ROADMAP.md` when the repository-tooling baseline changes;
7. ensure the machine-readable PR contract matches the final diff.

Do not weaken or bypass a contract merely to make a failing check green. Determine whether the repository change is wrong, the contract is stale, or an explicit compatibility decision is required.
