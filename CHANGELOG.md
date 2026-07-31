---
title: Uncertainty Architecture Changelog
artifact_type: changelog
status: informative
maturity: active
module: repository
topics:
  - provenance
  - repository-architecture
  - constraints
tags:
  - ua/module/repository
  - ua/type/changelog
  - ua/status/informative
  - ua/topic/provenance
  - ua/topic/repository-architecture
  - ua/topic/constraints
canonical_for:
  - change-record
---

# Changelog

All notable changes to the **Uncertainty Architecture repository and specification artifacts** are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/). Version numbers are assigned only through an explicit release decision.

Publications, talks, community discussions, and independent references belong under [`content/history/`](content/history/) rather than this release-oriented record.

## [Unreleased]

### Added

- Added draft-normative [`Control-Loop Capability Anatomy`](00-doctrine/control-loop-anatomy.md), distinguishing a closed feedback loop from a complete bounded UA control architecture.
- Added the composite [`Constraint Capability Family`](02-ai-control-plane/01-constraints/) and an informative [`Constraint Realization Catalog`](02-ai-control-plane/01-constraints/constraint-realization-catalog.md).
- Added canonical definitions for **Constraint**, **Hard Constraint**, **Soft Constraint**, and **Constraint Realization**.
- Added one canonical **Project Constraint Architecture** to the project review and one canonical **Constraint Realization Map** to the delivery review.
- Added compatibility notices at the legacy [`01-sensors/`](02-ai-control-plane/01-sensors/) and [`02-controller/`](02-ai-control-plane/02-controller/) paths so published deep links remain usable after capability-directory renumbering.
- Added constraint-specific failure modes, including Constraint–realization collapse, invalid Hard Constraint claims, mixed-strength Constraint records, realization bypass, closed-loop but unbounded operation, and duplicate control records.
- Added source-to-framework traceability for slide 12 of *Designing Non-Deterministic Systems* and its accepted, narrowed, and rejected interpretations.
- Established the Research Track under `content/research/`, preserved source snapshots under `content/raw/`, and separated project history under `content/history/`.
- Added `SPECIFICATION.md`, `ROADMAP.md`, `DOCUMENT-METADATA.md`, and `AGENTS.md` as canonical repository-level navigation and process artifacts.
- Added draft-normative doctrine for the controlled-object shift, Nested Control Lifecycle, Requirements, Operating Envelopes, Correctness, Bugs, and Model Judgment Placement.
- Added project-level and delivery-level review patterns and informative living templates.
- Added the Judgment Node Boundary pattern and placement-focused reference architectures.
- Added an illustrative completed Thinking System Review for support triage.

### Changed

- Established four logical capability families orthogonal to the four organizational-to-runtime decision levels: **Constraints and their realizations**, **Sensors and evidence**, **Controllers and decision authority**, and **Actuators and corrective action**.
- Clarified that the Constraints family is intentionally composite: the Constraint is the authoritative boundary object, while the Constraint Realization is the operational mechanism; realization is not a fifth capability family.
- Corrected canonical control diagrams so reference conditions reach the Controller, Controllers select or authorize action, Actuators execute change, and generic realization arrows do not imply deterministic enforcement for every Soft Constraint.
- Clarified that Constraints define the space in which a feedback loop operates; they are not the feedback edge that closes the loop.
- Separated an approved Constraint from its concrete Constraint Realization throughout doctrine, glossary, patterns, Control Plane documents, references, failure modes, and conformance.
- Tightened the Hard Constraint definition: the complete realized path must deterministically prevent or reject violation within stated assumptions, subject, path, scope, and enforcement boundaries.
- Clarified that hard or soft is a scoped claim about a Constraint and its complete realized path, not an intrinsic property of policy prose, a Requirement sentence, or an organizational source.
- Required separate Constraint records when one source condition has different guarantee strengths across subjects, paths, or scopes.
- Clarified that measured distribution, quality, cost, latency, and capacity tolerances remain part of the Requirement and Operating Envelope unless a separate realization deterministically enforces a specific boundary.
- Updated the worked support-triage review so deterministic per-request execution and exposure limits remain Hard Constraints while aggregate cost and p95 latency remain measured Release Gate and reauthorization evidence.
- Clarified that a prompt, natural-language policy, probabilistic evaluator, classifier, or model policy is not a Hard Constraint by itself.
- Decomposed evaluation gates by function: evaluator and metrics are Sensors; block/canary/release selection is a Controller function; deployment, blocking, exposure change, and rollback are Actuator functions.
- Reworked Controller guidance so decision authority and execution authority remain distinct even when one component performs both.
- Reworked Sensor guidance to include Constraint Realization state, violation evidence, false blocks, control health, and Actuator execution evidence.
- Reworked Actuator guidance so Actuators change operation or Constraint Realizations within delegated authority rather than directly owning policy decisions.
- Simplified the project and delivery patterns and templates to avoid repeating the same Constraint definition across scenarios, Judgment Nodes, DoR, DoD, Release Gate, and runtime sections.
- Updated the Judgment Node Boundary card to reference delivery Constraint IDs instead of redefining Constraints locally.
- Updated reference architectures so diagrams distinguish Constraints, realizations, Sensors, Controllers, and Actuators.
- Updated the failure taxonomy to distinguish open-loop operation from closed-loop but unbounded operation.
- Simplified the root README into a landing page that links to canonical doctrine instead of acting as a second specification.
- Reworked `AGENTS.md` around an explicit SMB-first operating model, practical organization–architecture/project–delivery-team–runtime ownership, and a four-decision-level by four-capability-family review matrix while preserving role flexibility and rejecting unnecessary enterprise-governance artifacts.
- Updated `SPECIFICATION.md` conformance to require accurate scoped Hard/Soft claims, explicit realization assumptions, reference conditions, decision authority, execution paths, and reassessment.
- Updated the Nested Control Lifecycle so project and delivery each maintain one canonical Constraint record for their decision surface and lower levels inherit higher-level decisions by reference.
- Updated the roadmap to reflect the reviewed four-family consolidation and its remaining validation work.
- Corrected presentation provenance: the verified repository-review source is the maintainer-supplied PDF export; an editable PPTX is not preserved or independently verified.
- Preserved the slide 12 brain/nerves/skeleton/muscles model as an explanatory metaphor while rejecting it as mandatory topology, execution order, or literal product taxonomy.
- Adopted **Thinking Systems** as the current system-category term while preserving **Behavioral Software** and **Behavioral Applications** in historical sources and provenance records.
- Clarified that UA complements rather than replaces Agile, DevOps, QA, security, change management, and incident response.
- Established separate canonical ownership for project authorization, delivery readiness/completion/release, and runtime reassessment.
- Replaced universal sample sizes, fixed thresholds, mandatory review cadences, and mandatory specialist titles with context-derived guidance.
- Clarified that Golden Scenarios support regression and change detection rather than universal ground truth.
- Clarified that telemetry or evaluation becomes control only when connected to reference conditions, decision authority, and an effective Actuator path.

### Moved and compatibility

- Organized the AI Control Plane under:
  - [`00-actuators/`](02-ai-control-plane/00-actuators/)
  - [`01-constraints/`](02-ai-control-plane/01-constraints/)
  - [`02-sensors/`](02-ai-control-plane/02-sensors/)
  - [`03-controller/`](02-ai-control-plane/03-controller/)
- Retained informative compatibility notices at the previous Sensor and Controller paths rather than treating the renumbering as a silent breaking change.
- Consolidated supporting material into `content/research/`, `content/history/`, and `content/raw/`.
- Archived the superseded RFC-oriented governance material under history.

### Removed

- Removed duplicate or inactive supporting namespaces after preserving material in canonical research, history, or raw-source locations.
- Removed empty scaffolds and stale references to nonexistent governance or publishing resources.
- Removed universal or presentation-derived claims that lacked a context- and consequence-based foundation.

## [0.1.0] - 2025-12-09

### Added

- Initial repository initialization.
- Core documentation structure (`README.md`, `LICENSE`, `CONTRIBUTING.md`).
- Initial Uncertainty Architecture concepts and Actuator/Sensor/Controller model.
