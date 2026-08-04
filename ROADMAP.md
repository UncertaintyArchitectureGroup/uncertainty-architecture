---
title: Uncertainty Architecture Roadmap
artifact_type: roadmap
status: informative
maturity: active
module: repository
topics:
  - repository-architecture
  - navigation
  - constraints
tags:
  - ua/module/repository
  - ua/type/roadmap
  - ua/status/informative
  - ua/topic/repository-architecture
  - ua/topic/navigation
  - ua/topic/constraints
canonical_for:
  - project-roadmap
---

# Uncertainty Architecture Roadmap

Uncertainty Architecture is being developed as a practical open specification for engineering and operating software that delegates part of its behavior to probabilistic Model Judgment.

This roadmap distinguishes completed work, active consolidation, near-term priorities, and later possibilities without speculative dates.

## Status legend

- **Completed** — present and accepted as the current repository baseline.
- **Active** — under development, application, or review.
- **Next** — intended after the active work reaches a stable checkpoint.
- **Later** — useful but not required for the current framework spine.

## Phase 1 — Concept validation

**Status: Completed**

Established:

- the initial UA thesis and publication corpus;
- Deterministic Core and Model Judgment distinctions;
- control-theory framing for AI governance;
- the initial AI Control Plane concept;
- public and expert feedback;
- repository structure and licensing.

## Phase 2 — Framework spine

**Status: Active**

The objective is to consolidate research into a coherent, bounded specification.

### Current baseline

- Research, history, and raw-source namespaces are separated.
- Specification boundary, status model, metadata, glossary, roadmap, changelog, and AI-contributor guidance exist.
- **Thinking Systems** is the current system-category term.
- Requirements, Operating Envelopes, Correctness, Bugs, and diagnostic sources are defined.
- Model Judgment Placement distinguishes Input Interpretation, Decision Logic, and Output Mediation without prescribing a pipeline.
- The Judgment Node Boundary, project review, and delivery review are established.
- Organizational, project, delivery, and runtime decision levels are distinguished.
- Project authorization, delivery release, runtime reassessment, and Architectural Veto remain separate decisions.
- The default SMB path uses one living project review and one living delivery review.
- Four logical capability families are established as the current draft baseline: Constraints and their realizations, Sensors and evidence, Controllers and decision authority, and Actuators and corrective action.
- A closed feedback loop is distinguished from a complete bounded UA control architecture.
- One canonical Project Constraint Architecture and one canonical delivery Constraint Realization Map are established as the default proportional Constraint records.
- Repository-relative links, navigation routes, citation metadata, critical repository structure, compatibility markers, and the top-level namespace have deterministic validation foundations.
- Controlled frontmatter, tag projection, active canonical ownership, and protected glossary entries have deterministic validation foundations; selected terminology drift remains advisory.
- Pull-request declarations, notable-change companion updates, research-state traceability, and maintained-path deletion or rename decisions have a diff-aware validation foundation.
- Quartz production builds, maintained Mermaid diagrams, workflow syntax and security posture, immutable action and container references, dependency updates, and dependency-risk checks have an executable repository-integrity foundation.

### Four-family capability baseline

The accepted current draft baseline:

- establishes a composite Constraints family containing the authoritative Constraint and its operational Constraint Realization;
- places that family alongside Sensors and evidence, Controllers and decision authority, and Actuators and corrective action;
- distinguishes a closed feedback loop from a complete bounded UA control architecture;
- distinguishes Constraint from Constraint Realization;
- defines hard or soft as a scoped claim about a Constraint and its complete realized path;
- requires separate records when one source condition has different guarantee strengths across subjects, paths, or scopes;
- classifies tools by function rather than product name;
- separates evaluation evidence, gate decision logic, and release execution into Sensor, Controller, and Actuator functions;
- introduces one canonical Project Constraint Architecture and one canonical delivery Constraint Realization Map;
- preserves legacy Sensor and Controller deep links through informative compatibility notices;
- records the PDF presentation source and rejects unverified PPTX-only provenance claims;
- aligns doctrine, patterns, Control Plane, references, failure modes, conformance, navigation, and research traceability around one model.

The repository integration is complete. The relevant framework documents remain draft-normative and still require worked application, real-team use, operational evidence, and further terminology validation before a broader maturity claim.

### Exit work for this phase

- [x] Complete architectural and logical consistency review of the capability-family model.
- [x] Confirm one Project Constraint Architecture and one delivery Constraint Realization Map as the default proportional record structure.
- [x] Integrate the four-family capability model across current repository doctrine, patterns, Control Plane, references, failure modes, conformance, navigation, and traceability.
- [x] Complete automated internal-link, navigation-route, anchor, and citation validation.
- [x] Establish a machine-readable repository contract protecting critical files, landing-page functions, compatibility paths, and the top-level namespace, with independent regression fixtures.
- [x] Establish controlled frontmatter, tag-projection, active canonical-ownership, protected-glossary, and terminology-warning validation.
- [x] Establish diff-aware changelog, glossary, roadmap, traceability, deletion, rename, and machine-readable pull-request coupling.
- [x] Complete automated Mermaid rendering and Quartz production-build validation.
- [x] Establish workflow linting, security analysis, immutable action/container policy, dependency update automation, and bounded dependency-risk checks.
- [ ] Build a two-level worked application tracing Constraints from organizational source through project architecture, delivery realization, runtime evidence, and reauthorization.
- [ ] Apply both reviews to a real team or documented real system boundary.
- [ ] Complete cross-publication synthesis and resolve remaining terminology conflicts.
- [ ] Validate the capability-family model against operational and incident evidence.

## Phase 3 — Patterns and failure modes

**Status: Active**

### Current outcomes

- Judgment Node Boundary with compact and extended use;
- project review connecting scenarios, Constraint architecture, capabilities, evidence, capacity, economics, authorization, inheritance, and reauthorization;
- delivery review connecting one realization map, DoR, implementation or experiment, DoD, Release Gate, operation, and reassessment;
- scenario-based risk reasoning without mandatory aggregate scores;
- failure taxonomy covering Constraint definition, realization, Sensor, Controller, Actuator, feedback, Human Authority, capacity, and economic failures;
- placement-focused reference architectures;
- one illustrative delivery review.

### Next outcomes

- two-level worked project-and-delivery application;
- containment, fallback, compensation, retry, escalation, and rollback patterns;
- drift, dependency-change, and verification patterns;
- Human-in-the-Loop and Human-on-the-Loop patterns;
- incident-based failure-mode examples;
- deeper guidance for deriving Constraints and tolerances from consequence, authority, detectability, reversibility, propagation, and capacity;
- additional worked domains.

## Phase 4 — Operating model and practical artifacts

**Status: Active**

The objective is practical use by SMB teams without a large governance organization.

### Current operating model

- one project review owns project viability, Project Constraint Architecture, authorization, inheritance, and reauthorization;
- one delivery review owns one Constraint Realization Map, DoR, DoD, Release Gate, and local reassessment;
- higher-level context is linked by version rather than copied;
- Judgment Node cards reference delivery Constraint IDs rather than redefining them;
- separate registers, gate records, responsibility matrices, or governance-board protocols are optional only when independent ownership or lifecycle requires them;
- versioned snapshots preserve decision history.

### Next outcomes

- real-team usability and time-to-complete evidence;
- decision-quality and duplication analysis;
- control-economics guidance using ranges and sensitivity rather than false precision;
- adoption guidance based on application evidence;
- refinements to incident, exception, and learning loops where concrete use exposes gaps.

A new top-level Operating Model module is not planned at this stage.

## Phase 5 — Optional tooling and reference implementations

**Status: Later**

### Current repository-integrity foundation

- deterministic navigation coverage and route validation;
- offline repository-relative link and anchor validation;
- machine-readable citation validation;
- a machine-readable repository contract for critical paths, sections, links, compatibility markers, and the top-level namespace;
- controlled frontmatter and tag-projection validation for the declared maintained-document baseline;
- active `canonical_for` uniqueness with superseded claims excluded;
- protected glossary-entry presence and uniqueness checks;
- non-blocking warnings for selected terminology drift, title/H1 drift, and unusually large tag sets;
- diff-aware changelog, glossary, roadmap, research-traceability, deletion, rename, compatibility, and pull-request declaration validation;
- Quartz production builds and rendering of maintained Mermaid blocks;
- actionlint and zizmor checks for GitHub Actions workflows;
- full-SHA action references, version comments, and sha256 container digests enforced by a machine-readable contract;
- weekly Dependabot updates for npm and GitHub Actions;
- bounded npm audit enforcement and GitHub Dependency Review integration, with Dependency Graph enablement remaining a repository-setting prerequisite;
- independent mutation fixtures proving that protected structural, metadata, change-coupling, and supply-chain regressions fail predictably;
- explicit repository ownership through `CODEOWNERS` and structured pull-request input through the default template.

### Later tooling

- checks for stale canonical paths and relationships;
- stronger dependency-review enforcement after repository Dependency Graph enablement;
- example Constraint, realization, prompt, policy, evaluation, and release manifests;
- executable realization examples;
- reference control-plane implementations;
- template generation from stable specification components.

Tooling must serve the specification rather than redefine it. No universal SDK, platform, policy engine, or agent framework is planned.

## Current priority

The immediate priority is to stabilize and test this path:

```text
Controlled-object doctrine
→ Control-Loop Capability Anatomy
→ Project Constraint Architecture and authorization
→ Delivery Constraint Realization and release
→ Runtime evidence and corrective action
→ Local reassessment, project reauthorization, or organizational review
```

The next worked application should show:

- authoritative organizational sources and decision rights;
- project scenarios, Constraints, capability requirements, evidence, capacity, economics, and authorization;
- one versioned inheritance package;
- one or more delivery realization maps;
- runtime realization state, behavior, violations, false blocks, Sensor evidence, Controller decisions, and Actuator execution;
- evidence that remains local versus evidence requiring higher-level reassessment;
- how duplication and parallel registries are avoided.

The project optimizes for durable clarity, traceability, and practical usefulness rather than repository volume.
