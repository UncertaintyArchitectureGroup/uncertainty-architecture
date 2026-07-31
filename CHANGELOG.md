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
- Added draft-normative doctrine defining Requirements, Operating Envelopes, Correctness, Bugs, and their conceptual relationship to Definition of Ready, Definition of Done, and Release Gates when probabilistic Model Judgment performs part of system behavior.
- Added conceptual diagrams for mixed Requirements, evidence-based diagnosis, and the relationship between defect source and a system-level Bug.
- Added draft-normative Model Judgment placement doctrine defining Input Interpretation, Decision Logic, and Output Mediation as functional classes rather than a mandatory pipeline.
- Added the draft-normative Judgment Node Boundary pattern with proportional minimal and extended modes, an embedded SMB-facing node card, placement-specific review prompts, and deterministic-containment guidance.
- Added the draft-normative Thinking System Review pattern as one lightweight SMB-facing delivery flow connecting inherited project constraints, outcome framing, Judgment Nodes, Requirements and Operating Envelopes, full model-mediated DoR and DoD extensions, release decisions, responsibility bundles, and runtime reassessment.
- Added an informative Thinking System Review template that keeps the inherited project baseline, working contract, evidence, residual risk, deployment scope, release decision, and version history in one living delivery artifact rather than separate governance records.
- Added `03-reference-architectures/judgment-placement-examples.md` with four non-prescriptive architectures for Input Interpretation, Decision Logic, Output Mediation, and a composite Thinking System.
- Added a completed illustrative Thinking System Review for human-supervised support triage and grounded reply drafting, including three bounded Judgment Nodes, a staged experiment, full DoR and DoD decisions, residual risk, a human-supervised Release Gate, runtime control, and framework-application observations.
- Added `00-doctrine/uncertainty-in-the-controlled-object.md` defining the controlled-object shift, useful variance, distinct locations of uncertainty, nested control levels, project authorization versus delivery release, runtime evidence, and architectural veto.
- Added two doctrine diagrams for the location of uncertainty across engineering disciplines and the nested organizational, project, delivery, and runtime control lifecycle.
- Added the draft-normative Project Control Architecture and Viability Review pattern connecting business outcome, material risk scenarios, intended Model Judgment and authority, required control capabilities, evidence feasibility, Human Authority, operational capacity, control economics, project authorization, delivery inheritance, and reauthorization.
- Added an informative Project Control Architecture and Viability Review template that keeps the project decision, residual risk, control economics, inherited delivery baseline, and decision history in one living artifact without a separate Project Launch Gate record.
- Expanded the canonical draft glossary with current UA terminology and explicit historical-term boundaries.

### Changed

- Simplified the repository contribution and research workflow for maintainer-led development while preserving deliberate review for normative, high-impact, automated, and externally contributed changes.
- Reframed research review artifacts as proportional tools rather than mandatory components of every research update.
- Redesigned the root README as a specification landing page with direct navigation to the controlled-object doctrine, project review and template, delivery review and template, research, discussions, independent references, talks, the glossary, metadata conventions, and the agent guide.
- Expanded the root README rationale to explain that Thinking Systems produce part of their uncertainty inside the controlled object and that UA complements Agile, DevOps, QA, security, and incident response with an additional organizational-to-runtime control lifecycle.
- Replaced the earlier delivery-only SMB path with a connected project-to-runtime path: project viability and authorization, versioned delivery inheritance, delivery DoR and DoD, deployment-specific release, and local or project reassessment.
- Established separate canonical ownership for project and delivery decisions: the project review owns risk, required controls, capacity, economics, authorization, inheritance, and reauthorization; the Thinking System Review owns implementation-level Judgment Nodes, DoR, DoD, release, and local reassessment.
- Added versioned project-baseline inheritance to the Thinking System Review and its template, including explicit outcomes when a delivery change requires project reauthorization or organizational review.
- Expanded `AGENTS.md` so AI contributors identify the organizational, project, delivery, or runtime control level; preserve canonical decision ownership; inherit higher-level context by reference; and escalate lower-level evidence when it invalidates a higher-level assumption.
- Normalized the entry-point structure and status declarations of the five primary specification modules.
- Adopted **Thinking Systems** as the current UA system-category term. **Behavioral Software** and **Behavioral Applications** are retained only as explicitly identified historical terminology in archived sources and provenance records.
- Consolidated supporting material into one canonical namespace per type: `content/research/`, `content/history/`, and `content/raw/`.
- Replaced the obsolete RFC-oriented `content/index.md` with an informative publishing portal that links back to the canonical repository sources.
- Replaced the research status `Proposed for RFC` with `Proposed for Framework Review` because the repository has no active mandatory RFC process.
- Clarified that Quartz and related Node files are publishing infrastructure rather than normative UA content.
- Removed the stale private Quartz deployment base URL rather than replacing it with an unverified public domain.
- Reclassified the early AI delivery lifecycle from doctrine to a research note and marked its sequence, role names, sample sizes, and thresholds as illustrative rather than universal.
- Split the lifecycle research question into organizational context, project authorization, delivery-level review, and runtime reauthorization while retaining the earlier four-phase lifecycle as an illustrative research model.
- Reworked child AI Control Plane documents so actuators, sensors, controllers, metrics, golden scenarios, evaluations, prompt interfaces, and responsibility bundles align with the distributed capability model in the module index.
- Replaced universal claims such as fixed sample sizes, fixed accuracy gates, mandatory weekly reviews, and mandatory specialist job titles with context- and risk-derived guidance.
- Clarified that golden scenarios are regression and change-detection anchors rather than universal ground truth.
- Clarified that telemetry or evaluation becomes control only when connected to decision authority and a mechanism that can change, contain, roll back, escalate, or stop behavior.
- Added controlled metadata to the specification, glossary, module entry points, Control Plane sub-documents, and actively maintained research indexes.
- Updated contribution guidance to require consistent metadata for new maintained conceptual documents and to direct agent-assisted work through `AGENTS.md`.
- Expanded `AGENTS.md` into an operational protocol that requires same-PR changelog updates and explicit classification of source-derived concepts, artifacts, responsibilities, processes, patterns, failure modes, and reference architectures.
- Clarified the proportional research-review process with a concise source-extraction and framework-crystallization step, canonical ownership rules, executable-clarity guidance, and reuse of the existing traceability matrix rather than a second ledger.
- Refined the canonical definitions of Requirement, Operating Envelope, Correctness, Bug, and Deviation Signal so statistical excursions remain evidence while a Bug is defined by violation of the approved operating contract.
- Refactored the Requirements, Correctness, and Bugs doctrine around mixed deterministic, model-mediated, and boundary responsibilities; added three diagnostic sources of a system-level Bug; and moved detailed readiness, completion, release, lifecycle, evidence-package, and responsibility guidance out of doctrine.
- Expanded UA conformance to identify each consequential Judgment Node's placement, inputs and approved context, affected behavior, authority, deterministic constraints, evidence, corrective paths, and traceability.
- Extended UA conformance with project-level reasoning for outcome, non-AI alternatives, risk scenarios, required controls, evidence feasibility, substantive Human Authority, operational capacity, control economics, project authorization, delivery inheritance, and reauthorization without requiring one template, score, or committee.
- Connected Judgment Node boundaries to the distributed AI Control Plane capability model without treating the boundary record itself as a complete control loop.
- Extended the Patterns module and UA conformance model to recognize equivalent lightweight project and delivery review records without requiring a separate Operating Model module.
- Established `01-patterns/thinking-system-review.md` as the canonical owner of the full model-mediated Definition of Ready, Definition of Done, distinct Release Gate, delivery responsibility bundles, and local reassessment flow; the template remains its informative working representation.
- Updated the reference-architecture index, root reader path, specification maturity, and roadmap to include placement-focused examples and mark the slides 1–6 framework transfer complete at the current draft level.
- Updated the presentation source-intake and framework-traceability records to distinguish the original maintainer-supplied PPTX used for slide-level review from the preserved PDF export and to record active source-to-framework decisions.
- Recorded an additional bounded PPTX extraction for the controlled-object, process-shift, feedback, and architectural-veto material without promoting the entire presentation or its illustrative thresholds and role claims.
- Advanced the roadmap from defining the project-level pattern to testing project-to-delivery inheritance through one two-level worked application and then real-team validation.
- Added a research-state reconciliation trigger to `AGENTS.md`, `CONTRIBUTING.md`, and the Research Review Process so source-derived framework work and worked applications update affected research questions and traceability without creating a parallel worklog.
- Synchronized the Research Track and Research Notes indexes with the completed presentation transfers and clarified that cross-publication synthesis and worked applications proceed as an iterative feedback loop.
- Updated the Research Track direction and traceability matrix to record the project review and template as active framework components rather than future candidates.
- Normalized the metadata and current scope of the control-theory, metrics, and reference-implementation briefs; reconciled the AI delivery lifecycle note with framework decisions adopted through the project and delivery reviews.
- Updated the research templates to use the current entity-classification and canonical-owner model instead of treating Lifecycle or Operating Model as automatic repository destinations.
- Clarified presentation provenance across the raw-source archive, source-intake record, and doctrine source metadata: the original PPTX is the slide-level working source, while the repository PDF is an archival export.
- Expanded the reference-architecture index and roadmap to expose the first completed worked delivery review while keeping its synthesized evidence separate from production validation.

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
