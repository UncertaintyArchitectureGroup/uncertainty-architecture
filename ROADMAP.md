---
title: Uncertainty Architecture Roadmap
artifact_type: roadmap
status: informative
maturity: active
module: repository
topics:
  - repository-architecture
  - navigation
tags:
  - ua/module/repository
  - ua/type/roadmap
  - ua/status/informative
  - ua/topic/repository-architecture
  - ua/topic/navigation
canonical_for:
  - project-roadmap
---

# Uncertainty Architecture Roadmap

Uncertainty Architecture is being developed as a practical open specification for engineering and operating software that delegates part of its behavior to probabilistic model judgment.

This roadmap is the canonical detailed view of project direction. It distinguishes completed work, active work, near-term priorities, and later possibilities without attaching speculative dates.

## Status legend

- **Completed** — present in the repository and accepted as the current project baseline
- **Active** — currently being developed, applied, or consolidated
- **Next** — intended after the active work reaches a stable checkpoint
- **Later** — valuable, but not required for the current framework spine

## Phase 1 — Concept Validation

**Status: Completed**

Established the initial thesis and public evidence that AI-enabled systems require explicit engineering at the boundary between deterministic software and probabilistic model judgment.

Completed outcomes:

- initial Uncertainty Architecture publications;
- control-theory framing for AI governance;
- deterministic-core and model-judgment distinction;
- AI Control Plane concept;
- public and expert feedback;
- initial repository structure and licensing model.

## Phase 2 — Framework Spine

**Status: Active**

The objective is to consolidate the existing research into a coherent, bounded specification that explains what UA governs, how its parts relate, and what remains non-normative.

### Completed in this phase

- Research Track structure established under `content/research/`;
- historical raw source snapshots preserved under `content/raw/`;
- five historical publications normalized and archived under `content/research/publications/`;
- provenance and normalization report added;
- research-to-framework traceability scaffold created;
- repository contribution and research workflow simplified for maintainer-led development;
- canonical specification boundary and document-status model established in `SPECIFICATION.md`;
- root README redesigned as the project landing page with direct evidence navigation;
- primary module entry points normalized around a shared structure;
- **Thinking Systems** adopted as the current system-category term, with **Behavioral Software** and **Behavioral Applications** retained only as historical terminology;
- canonical supporting namespaces consolidated under `content/research/`, `content/history/`, and `content/raw/`;
- earlier root research briefs classified as draft research notes;
- the retired RFC governance scaffold archived as historical rather than left as an active process;
- empty repository scaffolds and orphaned `.gitkeep` files removed;
- repository consistency pass completed across canonical routes, status boundaries, module sub-documents, and research-source traceability;
- initial canonical draft glossary established, including Thinking Systems, Deterministic Core, Model Judgment, Uncertainty Boundary, AI Control Plane, control-loop capabilities, and delivery vocabulary;
- early AI delivery lifecycle material reclassified from doctrine into a research note with illustrative thresholds and roles explicitly bounded;
- child AI Control Plane documents aligned with the distributed capability model and stripped of universal sample sizes, thresholds, role titles, and fixed review cadences;
- controlled document metadata and hierarchical `ua/...` tag conventions established in `DOCUMENT-METADATA.md`;
- tool-neutral repository guidance for language models and coding agents established in `AGENTS.md`;
- source-intake records added for the available on-device/cloud article and the *Designing Non-Deterministic Systems* presentation;
- Requirements, Operating Envelopes, Correctness, and Bugs refactored into a mixed-system doctrine with deterministic, model-mediated, and boundary-or-control diagnostic sources;
- Model Judgment Placement established as a functional taxonomy of Input Interpretation, Decision Logic, and Output Mediation;
- Judgment Node Boundary established as the first reusable pattern connecting Model Judgment to authority, deterministic constraints, evidence, fallback, escalation, and ownership;
- the SMB Thinking System Review established as the canonical owner of the full model-mediated DoR, DoD, Release Gate, responsibility bundles, and reassessment flow;
- one informative Thinking System Review template added as the default living SMB working artifact;
- four placement-focused reference architectures added for Input Interpretation, Decision Logic, Output Mediation, and one composite Thinking System;
- slides 1–6 source-to-framework traceability updated to distinguish the original PPTX used for review from the preserved PDF export and to record active framework decisions;
- research-state reconciliation added to the agent and research workflows so framework changes and worked applications update affected questions and traceability without creating a parallel worklog.

### Active and next milestones

- [ ] Complete a cross-publication research synthesis.
- [ ] Identify stable concepts, later refinements, contradictions, and superseded claims.
- [ ] Refine the canonical glossary where synthesis changes scope or meaning.
- [ ] Consolidate the framework spine across Doctrine, Patterns, AI Control Plane, Reference Architectures, Failure Modes, and practical artifacts.
- [ ] Translate additional accepted framework decisions into module-level normative or draft-normative documents.
- [ ] Validate compatibility and terminology through worked applications of the framework.

## Phase 3 — Patterns and Failure Modes

**Status: Active**

The objective is to turn the framework spine into reusable engineering guidance.

### Completed or active outcomes

- Judgment Node Boundary pattern for consequential Model Judgment;
- minimal and extended boundary modes proportional to authority and consequences;
- compact Judgment Node card embedded in the pattern rather than maintained as a separate registry;
- Thinking System Review pattern connecting Requirements, Judgment Nodes, readiness, completion, release, and runtime reassessment;
- explicit separation of completion evidence from residual-risk acceptance;
- placement reference architectures that isolate each functional class and show one non-prescriptive composite system.

### Next outcomes

- containment, validation, retry, fallback, and escalation patterns;
- drift and verification patterns;
- Human-in-the-Loop and Human-on-the-Loop patterns;
- failure-mode taxonomy grounded in operational examples;
- explicit anti-patterns and conditions where AI should not be used;
- worked domain examples that apply the Thinking System Review and expose missing distinctions.

## Phase 4 — Operating Model and Practical Artifacts

**Status: Active**

The objective is to make UA usable by small and medium-sized engineering teams without requiring a large governance organization.

### Completed or active outcomes

- one lightweight Thinking System Review flow for framing, implementation or bounded experimentation, completion, release, and reassessment;
- one living practical template containing Judgment Node cards, full model-mediated DoR and DoD extensions, residual risk, deployment scope, release decision, and reassessment history;
- four responsibility bundles — implementation, evaluation, operation, and release decision authority — defined as responsibilities rather than mandatory job titles;
- versioned or immutable review snapshots used for traceability without requiring a separate Release Decision Record;
- explicit default that the SMB path does not require a Judgment Node registry, governance board protocol, readiness record, completion package, or responsibility matrix;
- minimal reference architectures that show how the review surface changes by placement without duplicating the complete checklists.

### Next outcomes

- risk and tolerance mapping;
- control-economics guidance;
- an SMB-facing extension for estimating required controls and their operational cost;
- completed Thinking System Review examples across different domains and consequence levels;
- adoption guidance based on practical application feedback;
- incident, change, and learning-loop refinements where the current review pattern proves insufficient.

## Phase 5 — Optional Tooling and Reference Implementations

**Status: Later**

Tooling is optional and must serve the specification rather than redefine it.

Possible outcomes:

- small validation or repository-maintenance utilities;
- metadata and internal-link validation;
- example prompt, policy, and evaluation registries;
- reference control-plane implementations;
- executable examples and architecture demonstrations;
- reusable templates generated from stable specification components.

No universal SDK or platform is currently planned.

## Current priority

The slides 1–6 framework transfer is complete at the current draft level. The immediate practical priority is one completed, realistically bounded Thinking System Review that tests the current template and exposes missing distinctions.

Cross-publication synthesis should proceed alongside that application rather than wait for every framework concept to be finished. Material findings from either track should reconcile the affected research questions, traceability, doctrine, patterns, or practical artifact through explicit review.

Evidence from the worked review should determine whether the next coherent expansion is risk and tolerance mapping, control-cost estimation, failure modes, incident-loop refinement, or template simplification. The project should not multiply governance documents before that evidence exists.

The project optimizes for durable clarity, traceability, and practical usefulness rather than rapid expansion of repository volume.
