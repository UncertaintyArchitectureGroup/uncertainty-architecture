# Uncertainty Architecture Roadmap

Uncertainty Architecture is being developed as a practical open specification for engineering and operating software that delegates part of its behavior to probabilistic model judgment.

This roadmap is the canonical detailed view of project direction. It distinguishes completed work, active work, near-term priorities, and later possibilities without attaching speculative dates.

## Status legend

- **Completed** — present in the repository and accepted as the current project baseline
- **Active** — currently being developed or consolidated
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
- final repository consistency pass completed across canonical routes, status boundaries, module sub-documents, and research-source traceability;
- initial canonical draft glossary established, including Thinking Systems, Deterministic Core, Model Judgment, Uncertainty Boundary, AI Control Plane, control-loop capabilities, and delivery vocabulary;
- early AI delivery lifecycle material reclassified from doctrine into a research note with illustrative thresholds and roles explicitly bounded;
- child AI Control Plane documents aligned with the distributed capability model and stripped of universal sample sizes, thresholds, role titles, and fixed review cadences;
- controlled document metadata and hierarchical `ua/...` tag conventions established in `DOCUMENT-METADATA.md`;
- tool-neutral repository guidance for language models and coding agents established in `AGENTS.md`;
- missing repository records added for the available on-device/cloud article and presentation sources that remain pending preservation or normalization.

### Active and next milestones

- [ ] Complete a cross-publication research synthesis.
- [ ] Identify stable concepts, later refinements, contradictions, and superseded claims.
- [ ] Refine the canonical glossary where synthesis changes scope or meaning.
- [ ] Produce a concise framework-spine proposal.
- [ ] Clarify normative boundaries across Doctrine, Patterns, AI Control Plane, Operating Model, Reference Architectures, Failure Modes, and practical artifacts.
- [ ] Translate accepted framework decisions into module-level normative or draft-normative documents.

## Phase 3 — Patterns and Failure Modes

**Status: Next**

The objective is to turn the framework spine into reusable engineering guidance.

Planned outcomes:

- boundary patterns between deterministic control and model judgment;
- containment, validation, retry, fallback, and escalation patterns;
- drift and verification patterns;
- Human-in-the-Loop and Human-on-the-Loop patterns;
- failure-mode taxonomy grounded in operational examples;
- explicit anti-patterns and conditions where AI should not be used.

## Phase 4 — Operating Model and Practical Artifacts

**Status: Next**

The objective is to make UA usable by small and medium-sized engineering teams without requiring a large governance organization.

Planned outcomes:

- lightweight responsibility and decision model;
- release, incident, change, and learning loops;
- control-loop design guidance;
- risk and tolerance mapping;
- control-economics guidance;
- an SMB-facing artifact for estimating required controls and their operational cost;
- worked examples and adoption guidance.

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

The immediate priority is cross-publication research synthesis and extraction of the framework spine. Once that spine is explicit, the project should derive one practical SMB-facing control-loop and risk-mapping artifact from it.

The project optimizes for durable clarity, traceability, and practical usefulness rather than rapid expansion of repository volume.
