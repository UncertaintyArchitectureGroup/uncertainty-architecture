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
- the SMB Thinking System Review established as the canonical owner of the full model-mediated DoR, DoD, Release Gate, responsibility bundles, and reassessment flow for a feature or material change;
- one informative Thinking System Review template added as the default living SMB working artifact;
- four placement-focused reference architectures added for Input Interpretation, Decision Logic, Output Mediation, and one composite Thinking System;
- slides 1–6 source-to-framework traceability updated to distinguish the original PPTX used for review from the preserved PDF export and to record active framework decisions;
- research-state reconciliation added to the agent and research workflows so framework changes and worked applications update affected questions and traceability without creating a parallel worklog;
- one completed illustrative Thinking System Review added for human-supervised support triage and grounded reply drafting, exercising the full feature-level review surface without presenting synthesized evidence as production validation;
- the controlled-object shift established as doctrine: Thinking Systems produce part of their runtime uncertainty internally through Model Judgment;
- product uncertainty, operational uncertainty, and runtime-judgment uncertainty distinguished without positioning UA as a replacement for Agile, DevOps, QA, security, or incident response;
- organizational context, project control architecture and viability, feature/change delivery, and runtime reauthorization established as connected control levels;
- project authorization distinguished from feature release, and architectural veto recognized as a valid engineering outcome.

### Active and next milestones

- [ ] Define a lightweight project-level control-architecture and viability pattern.
- [ ] Define how project constraints, shared controls, and reauthorization triggers are inherited by feature-level Thinking System Reviews.
- [ ] Complete a cross-publication research synthesis.
- [ ] Identify stable concepts, later refinements, contradictions, and superseded claims.
- [ ] Refine the canonical glossary where synthesis changes scope or meaning.
- [ ] Consolidate the framework spine across Doctrine, Patterns, AI Control Plane, Reference Architectures, Failure Modes, and practical artifacts.
- [ ] Translate additional accepted framework decisions into module-level normative or draft-normative documents.
- [ ] Validate compatibility and terminology through real-team applications and additional worked domains.

## Phase 3 — Patterns and Failure Modes

**Status: Active**

The objective is to turn the framework spine into reusable engineering guidance.

### Completed or active outcomes

- Judgment Node Boundary pattern for consequential Model Judgment;
- minimal and extended boundary modes proportional to authority and consequences;
- compact Judgment Node card embedded in the pattern rather than maintained as a separate registry;
- Thinking System Review pattern connecting Requirements, Judgment Nodes, readiness, completion, release, and runtime reassessment for a feature or material change;
- explicit separation of completion evidence from residual-risk acceptance;
- placement reference architectures that isolate each functional class and show one non-prescriptive composite system;
- a fully populated support-triage worked review showing three Judgment Nodes, bounded experimentation, complete DoR and DoD decisions, residual risk, a human-supervised release decision, runtime control, and reassessment triggers;
- doctrine that places the feature/change loop inside a broader project-to-runtime control lifecycle.

### Next outcomes

- project control architecture and viability review pattern;
- risk-scenario mapping tied to authority, consequence, detectability, reversibility, propagation, and required control capabilities;
- project authorization, limitation, redesign, research-only, escalation, and no-go outcomes;
- project reauthorization triggers for material changes in autonomy, authority, data, population, domain, operational capacity, or control economics;
- containment, validation, retry, fallback, and escalation patterns;
- drift and verification patterns;
- Human-in-the-Loop and Human-on-the-Loop patterns;
- failure-mode taxonomy grounded in operational examples;
- explicit anti-patterns and conditions where AI should not be used;
- additional worked domains and at least one real-team application that test whether the current framework remains usable outside the reference scenario.

## Phase 4 — Operating Model and Practical Artifacts

**Status: Active**

The objective is to make UA usable by small and medium-sized engineering teams without requiring a large governance organization.

### Completed or active outcomes

- one lightweight Thinking System Review flow for feature/change framing, implementation or bounded experimentation, completion, release, and reassessment;
- one living practical template containing Judgment Node cards, full model-mediated DoR and DoD extensions, residual risk, deployment scope, release decision, and reassessment history;
- four responsibility bundles — implementation, evaluation, operation, and release decision authority — defined as responsibilities rather than mandatory job titles;
- versioned or immutable review snapshots used for traceability without requiring a separate Release Decision Record;
- explicit default that the SMB feature path does not require a Judgment Node registry, governance board protocol, readiness record, completion package, or responsibility matrix;
- minimal reference architectures that show how the review surface changes by placement without duplicating the complete checklists;
- one completed illustrative SMB review demonstrating that multiple Judgment Nodes and release decisions can remain in one artifact without a separate operating-model module or registry;
- a conceptual four-level lifecycle connecting organizational context, project authorization, feature delivery, and runtime reauthorization.

### Next outcomes

- one SMB-facing Project Control Architecture and Viability Review artifact;
- risk and tolerance mapping;
- control-economics guidance covering build cost, run cost, human-review capacity, latency, evaluation maintenance, incident handling, and expected residual exposure;
- a project authorization decision that can approve, limit, condition, redirect to research, redesign, escalate, or reject the AI path;
- one two-level worked example showing how a project baseline is inherited by a feature-level Thinking System Review and how runtime evidence can trigger reauthorization;
- additional completed Thinking System Review examples across different domains and consequence levels;
- a real-team application that can reveal usability, ownership, evidence, and control-cost gaps not visible in a synthesized example;
- adoption guidance based on practical application feedback;
- incident, change, and learning-loop refinements where the current review patterns prove insufficient.

A new top-level Operating Model module is not planned at this stage. Project and feature responsibilities may remain patterns and practical artifacts until several stable independent components justify a structural change.

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

The current draft now distinguishes two control decisions that were previously compressed into one delivery lifecycle:

1. **Project authorization:** whether a proposed Thinking System has a credible, operable, and economically viable control architecture.
2. **Feature/change release:** whether one implementation or material change has sufficient evidence and acceptable residual risk for a specific deployment context.

The immediate framework priority is a project-level pattern that turns this distinction into a lightweight SMB process without inventing a universal risk score, mandatory committee, or duplicate governance records.

The expected sequence is:

```text
Controlled-object doctrine
→ Project Control Architecture and Viability Review pattern
→ One project-level working template
→ Two-level worked application
→ Real-team validation and refinement
```

The project-level pattern should expose the minimum reasoning needed to map material risk scenarios, intended Model Judgment and authority, deterministic invariants, required control capabilities, Human Authority, evidence feasibility, operational capacity, control cost, residual risk, project authorization, and reauthorization triggers.

Cross-publication synthesis should continue alongside this work. Material findings from either track should reconcile the affected research questions, traceability, doctrine, patterns, practical artifacts, reference architectures, or failure modes through explicit review.

The project should continue to avoid multiplying governance documents. The next artifacts should demonstrate inheritance between project and feature levels rather than duplicate the same risk, authority, or control information in multiple records.

The project optimizes for durable clarity, traceability, and practical usefulness rather than rapid expansion of repository volume.
