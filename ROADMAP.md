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
- empty `scripts/` and `templates/` scaffolds removed.

### Active and next milestones

- [ ] Complete a final repository consistency pass covering links, document statuses, canonical entry points, and orphaned placeholders.
- [ ] Complete a cross-publication research synthesis.
- [ ] Identify stable concepts, later refinements, contradictions, and superseded claims.
- [ ] Define the relationship between Thinking Systems and higher-autonomy agentic systems in the canonical glossary.
- [ ] Produce a concise framework-spine proposal.
- [ ] Clarify normative boundaries across Doctrine, Patterns, AI Control Plane, Operating Model, Reference Architectures, Failure Modes, and practical artifacts.
- [ ] Consolidate canonical definitions in a repository glossary.

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
- example prompt, policy, and evaluation registries;
- reference control-plane implementations;
- executable examples and architecture demonstrations;
- reusable templates generated from stable specification components.

No universal SDK or platform is currently planned.

## Current priority

The immediate priority is to complete the final repository consistency pass. After that, the project should complete the research synthesis, establish the framework spine, and derive one practical SMB-facing control-loop and risk-mapping artifact from that spine.

The project optimizes for durable clarity, traceability, and practical usefulness rather than rapid expansion of repository volume.