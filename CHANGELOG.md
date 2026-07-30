---
title: Uncertainty Architecture Changelog
artifact_type: changelog
status: informative
maturity: active
module: repository
topics:
  - provenance
  - repository-architecture
tags:
  - ua/module/repository
  - ua/type/changelog
  - ua/status/informative
  - ua/topic/provenance
  - ua/topic/repository-architecture
canonical_for:
  - change-record
---

# Changelog

All notable changes to the **Uncertainty Architecture repository and specification artifacts** are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/). Version numbers are assigned only when the project makes an explicit release decision.

Project publications, talks, community discussions, and independent references are documented under [`content/history/`](content/history/) rather than repeated here.

## [Unreleased]

### Added

- Expanded the repository into dedicated areas for doctrine, patterns, the AI Control Plane, reference architectures, and failure modes.
- Established the UA Research Track under `content/research/` with an explicit boundary between historical research and normative framework material.
- Added research publication, analysis, and framework-traceability templates.
- Added a research-to-framework traceability scaffold.
- Preserved five historical source snapshots under `content/raw/`.
- Preserved the PDF export of *Designing Non-Deterministic Systems: Maintaining Engineering Rigor in the AI Era* under `content/raw/` and registered it in the raw-source and research indexes.
- Added normalized repository editions of five historical research publications under `content/research/publications/`.
- Added a normalization report documenting provenance, transformations, quality checks, and unresolved publication metadata.
- Added a canonical project roadmap in `ROADMAP.md`.
- Added a project-history area separating the timeline, public talks, and independent references from release history and normative specification content.
- Added `SPECIFICATION.md` as the canonical specification boundary and document-status index.
- Added a canonical research-notes area under `content/research/notes/`.
- Added `content/raw/README.md` to define the provenance and non-normative boundary of source snapshots.
- Added a historical archive for the superseded January 2026 RFC governance scaffold under `content/history/legacy-rfcs/`.
- Added `DOCUMENT-METADATA.md` with controlled frontmatter fields, document classes, topics, relationship metadata, and hierarchical `ua/...` tags for Obsidian, Quartz, and machine retrieval.
- Added `AGENTS.md` as a tool-neutral repository map and editing guide for language models and coding agents.
- Added source-intake records for the available on-device/cloud article and the *Designing Non-Deterministic Systems* presentation.
- Added draft-normative doctrine defining Requirements, Operating Envelopes, Correctness, Bugs, Definition of Ready, Definition of Done, and Release Gates when probabilistic Model Judgment performs business logic.
- Expanded the canonical draft glossary with current UA terminology and explicit historical-term boundaries.

### Changed

- Simplified the repository contribution and research workflow for maintainer-led development while preserving deliberate review for normative, high-impact, automated, and externally contributed changes.
- Reframed research review artifacts as proportional tools rather than mandatory components of every research update.
- Redesigned the root README as a specification landing page with direct navigation to research, discussions, independent references, talks, the glossary, metadata conventions, and the agent guide.
- Normalized the entry-point structure and status declarations of the five primary specification modules.
- Adopted **Thinking Systems** as the current UA system-category term. **Behavioral Software** and **Behavioral Applications** are retained only as explicitly identified historical terminology in archived sources and provenance records.
- Consolidated supporting material into one canonical namespace per type: `content/research/`, `content/history/`, and `content/raw/`.
- Replaced the obsolete RFC-oriented `content/index.md` with an informative publishing portal that links back to the canonical repository sources.
- Replaced the research status `Proposed for RFC` with `Proposed for Framework Review` because the repository has no active mandatory RFC process.
- Clarified that Quartz and related Node files are publishing infrastructure rather than normative UA content.
- Removed the stale private Quartz deployment base URL rather than replacing it with an unverified public domain.
- Reclassified the early AI delivery lifecycle from doctrine to a research note and marked its sequence, role names, sample sizes, and thresholds as illustrative rather than universal.
- Reworked child AI Control Plane documents so actuators, sensors, controllers, metrics, golden scenarios, evaluations, prompt interfaces, and responsibility bundles align with the distributed capability model in the module index.
- Replaced universal claims such as fixed sample sizes, fixed accuracy gates, mandatory weekly reviews, and mandatory specialist job titles with context- and risk-derived guidance.
- Clarified that golden scenarios are regression and change-detection anchors rather than universal ground truth.
- Clarified that telemetry or evaluation becomes control only when connected to decision authority and a mechanism that can change, contain, roll back, escalate, or stop behavior.
- Added controlled metadata to the specification, glossary, module entry points, Control Plane sub-documents, and actively maintained research indexes.
- Updated contribution guidance to require consistent metadata for new maintained conceptual documents and to direct agent-assisted work through `AGENTS.md`.
- Expanded `AGENTS.md` into an operational protocol that requires same-PR changelog updates and explicit classification of source-derived concepts, artifacts, responsibilities, processes, patterns, failure modes, and reference architectures.
- Refined the canonical definitions of Requirement, Operating Envelope, Correctness, Bug, Definition of Ready, Definition of Done, Release Gate, and Deviation Signal so stochastic evidence supports bounded engineering decisions without being mistaken for universal proof.
- Updated the roadmap so cross-publication synthesis is now the immediate substantive priority.

### Removed

- Removed the duplicate root-level `research/` namespace after migrating its three planning briefs into `content/research/notes/`.
- Removed the active `content/rfcs/` namespace after preserving its governance proposal and template as superseded historical records.
- Removed empty `scripts/` and `templates/` scaffolds that contained no active utilities or reusable project artifacts.
- Removed references to the nonexistent `GOVERNANCE.md` and to inactive root research or RFC namespaces.
- Removed the obsolete `00-doctrine/LLM_Delivery_SDLC.md` path after preserving and reclassifying its substantive content under `content/research/notes/ai-delivery-lifecycle.md`.
- Removed redundant `.gitkeep` files from directories that already contain maintained documents.

## [0.1.0] - 2025-12-09

### Added

- Initial repository initialization.
- Core documentation structure (`README.md`, `LICENSE`, `CONTRIBUTING.md`).
- Definition of Uncertainty Architecture core concepts, Control Plane pattern, and Actuator/Sensor/Controller model.