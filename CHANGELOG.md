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

- Added diff-aware pull-request validation that checks the machine-readable `ua-change-contract` against the actual git diff, enforces changelog and companion-document coupling, requires explicit compatibility decisions for maintained-file deletion or rename, and supports narrow maintainer exception labels with focused regression fixtures.
- Added a machine-readable metadata contract, dependency-free frontmatter and canonical-ownership validator, protected-glossary and terminology checks, focused GitHub Actions jobs, and mutation-based regression fixtures for controlled metadata, tag projection, active `canonical_for` uniqueness, and selected terminology drift.
- Added a machine-readable repository contract, dependency-free validator, mutation-based regression fixtures, focused GitHub Actions checks, structured pull-request template, and `CODEOWNERS` map to protect critical files, landing-page functions, compatibility paths, stable repository links, and the top-level namespace without freezing ordinary prose evolution.
- Added a root [`CITATION.cff`](CITATION.cff) so GitHub and compatible citation tools can expose machine-readable repository citation metadata for Vitalii Oborskyi and Sam Walker, and extended CI to validate that metadata against CFF schema 1.2.0.
- Added a GitHub Actions CI workflow that validates the declared navigation coverage and destinations and uses a SHA-pinned `lychee` action in offline mode to check repository-relative links, directory indexes, Markdown heading fragments, and explicit HTML compatibility anchors across maintained Markdown without making external-network availability part of repository integrity.
- Added a non-normative drafting-ready editorial contract and Phase 1 completion-candidate record for the planned public synthesis article, *Uncertainty Architecture: An Open Engineering Specification for Thinking Systems*. The proposed structure uses one unnumbered abstract, eight numbered sections, three figures, and one illustrative continuous Constraint trace; article prose has not begun and maintainer freeze remains pending.
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

- Aligned `DOCUMENT-METADATA.md`, `AGENTS.md`, `CONTRIBUTING.md`, and `ROADMAP.md` with automated metadata validation; classified the external-recognition evidence ledger with controlled frontmatter; and corrected two project-pattern references that mislabeled runtime reassessment as runtime reauthorization.
- Updated `AGENTS.md`, `CONTRIBUTING.md`, and `ROADMAP.md` to document the repository-contract protocol, local validation commands, contract-change discipline, and the current tooling baseline; converted the two license-file references in `LICENSING.md` into repository-relative Markdown links.
- Established a consistent navigation system across the root, specification, doctrine, patterns, AI Control Plane, reference-architecture, failure-mode, and research entry pages; linked the four decision levels and four capability families to their owning locations; added owner/back links to the two practical templates and the Judgment Placement references; aligned the runtime lifecycle heading to **Runtime operation and reassessment** while preserving the previous deep-link anchor; and corrected stale PDF/PPTX provenance and runtime terminology in research and raw-source indexes.
- Recorded the merged four-family capability architecture as the current draft roadmap baseline while retaining worked-application, real-team, tooling, operational-evidence, and terminology validation as open maturity work.
- Corrected the root README so the runtime decision level is described as operation and reassessment rather than runtime reauthorization.
- Established four logical capability families orthogonal to the four organizational-to-runtime decision levels: **Constraints and their realizations**, **Sensors and evidence**, **Controllers and decision authority**, and **Actuators and corrective action**.
- Clarified that the Constraints family is intentionally composite: the Constraint is the authoritative boundary object, while the Constraint Realization is the operational mechanism; realization is not a fifth capability family.
- Corrected canonical control diagrams so reference conditions reach the Controller, Controllers select or authorize action, Actuators execute change, and generic realization arrows do not imply deterministic enforcement for every Soft Constraint.
- Completed a repository-wide diagram consistency pass: taxonomy, lifecycle, Requirement-decomposition, diagnosis, review-flow, boundary, and complete-control diagrams now state or preserve their scope and do not imply omitted capability paths are absent.
- Completed a second repository consistency pass by connecting actual Judgment Node outputs, actions, and outcomes to Sensors; standardizing Hard Constraint claims around subject, path, and scope; using **Human Authority** consistently as the Constraint class; and naming the Project Constraint Architecture and delivery Constraint Realization Map as the two canonical lifecycle artifacts.
- Corrected reference diagrams so Constraint Realizations act on accepted context, Judgment, gates, and delivery boundaries rather than unrealistically bounding external inputs or allowing Actuators to modify consumers directly.
- Aligned the Requirement/Correctness/Bug and Model Judgment Placement doctrine with the four capability families and the verified PDF source boundary.
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
- Updated the Nested Control Lifecycle so the project owns one Project Constraint Architecture, delivery owns one Constraint Realization Map, and lower levels inherit higher-level decisions by reference.
- Updated the roadmap to reflect the reviewed four-family consolidation and its remaining validation work.
- Corrected presentation provenance: the verified repository-review source is the maintainer-supplied PDF export; an editable PPTX is not preserved or independently verified.
- Preserved the slide 12 brain/nerves/skeleton/muscles model as an explanatory metaphor while rejecting it as mandatory topology, execution order, or literal product taxonomy.
- Adopted **Thinking Systems** as the current system-category term while preserving **Behavioral Software** and **Behavioral Applications** in historical sources and provenance records.
- Clarified that UA complements rather than replaces Agile, DevOps, QA, security, change management, and incident response.
- Established separate canonical ownership for project authorization, delivery readiness/completion/release, and runtime reassessment.
- Replaced universal sample sizes, fixed thresholds, mandatory review cadences, and mandatory specialist titles with context-derived guidance.
- Clarified that Golden Scenarios support regression and change detection rather than universal ground truth.
- Clarified that telemetry or evaluation becomes control only when connected to reference conditions, decision authority, and an effective Actuator path.

### Fixed

- Restored the root README attribution, contributor, advisor, maturity, evidence, contribution, repository-citation, and full dual-license guidance that was unintentionally dropped during landing-page simplification.
