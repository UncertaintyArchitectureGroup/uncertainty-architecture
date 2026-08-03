---
title: Open Engineering Specification Article Phase 1 Completion Record
artifact_type: research-note
status: research
maturity: draft
module: research
topics:
  - thinking-systems
  - control-loop
  - constraints
  - sdlc
  - repository-architecture
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/thinking-systems
  - ua/topic/control-loop
  - ua/topic/constraints
  - ua/topic/sdlc
  - ua/topic/repository-architecture
created: 2026-07-31
updated: 2026-08-03
language: en
license: CC-BY-4.0
draft: true
---

# Phase 1 Completion Record: Editorial Architecture

> **Current state:** The accepted architecture from PR #32 has been integrated into the branch. Architecture, logic, technical, metadata, and editorial review have produced a drafting-ready editorial contract. Phase 1 remains open only for explicit maintainer review and freeze; article prose has not begun.

## 1. Purpose of Phase 1

Phase 1 converts a large working skeleton into a stable editorial contract for the public synthesis article:

**Uncertainty Architecture: An Open Engineering Specification for Thinking Systems**  
*From project viability to delivery realization, runtime evidence, and reauthorization*

The output is not publishable prose and does not create specification authority. It defines:

- the article's central thesis and claim boundary;
- the final reader journey;
- one unique job for every section;
- the canonical and external source rules;
- the three figures;
- the continuous worked Constraint trace;
- the maturity statement and external validation request;
- the Phase 2 drafting sequence.

## 2. Baseline integrated

The branch includes the current `main` baseline containing:

- the four-family Control-Loop Capability Anatomy;
- Constraint and Constraint Realization as distinct concepts;
- scoped Hard and Soft Constraint claims;
- Project Constraint Architecture and delivery Constraint Realization Map;
- the corrected Nested Control Lifecycle;
- current AI Control Plane, conformance, failure-mode, roadmap, and provenance decisions.

The earlier temporary dependency on PR #32 is resolved.

## 3. Architecture review decision

### Final reader journey

```text
missing engineering connection
→ controlled-object shift
→ model quality versus bounded control
→ four decision levels
→ two living reviews and inheritance
→ one Constraint across the lifecycle
→ platform implementation versus authority
→ current specification state, limits, and validation request
```

### Final section sequence

1. **The Missing Engineering Connection**
2. **The Controlled Object Has Changed**
3. **From Model Quality to Bounded Control**
4. **Four Decision Levels of Uncertainty Architecture**
5. **From Authority to Operation: Two Living Reviews**
6. **One Constraint Across the Full Lifecycle**
7. **What Platforms Can Implement — and What They Cannot Authorize**
8. **Open Specification: Current State, Limits, and Invitation**

### Structural decisions

- The four decision levels remain the conceptual center.
- The four capability families explain how control becomes operational at every level and do not become a second lifecycle.
- The control-theory material remains a distinct section because it establishes the difference between measurement, feedback closure, and bounded acceptable operation before the lifecycle is introduced.
- Inheritance and the two living artifacts are combined into one operating-path section.
- Openness, maturity, limitations, and invitation are combined into one ending.
- The worked narrative traces one Constraint rather than retelling the entire support-triage architecture.

## 4. Logic review record

The revised blueprint removes repeated or competing explanations of:

- deterministic versus model-mediated behavior;
- policies, tools, and evaluations being insufficient in isolation;
- feedback closure versus bounded operation;
- the four decision levels;
- inheritance and evidence routing;
- the two review artifacts;
- the platform boundary;
- repository maturity and openness.

Each section now contains:

- purpose;
- core claim;
- required supporting points;
- canonical source anchors;
- material not to repeat elsewhere;
- transition;
- intended closing claim;
- word budget.

The earlier ten-section plan is reduced to eight sections so the final article reads as one argument rather than adjacent mini-essays.

The final review also separates:

- runtime evidence that invalidates a delivery or project basis;
- a proposed authority change that must enter project and organizational decision paths before implementation.

An autonomous-send request is therefore not presented as runtime evidence.

## 5. Technical and repository review record

### Canonical concepts aligned

- Thinking System and Model Judgment;
- Control-Loop Capability Anatomy;
- Constraint versus Constraint Realization;
- Hard and Soft Constraint as scoped complete-realized-path claims;
- Sensor, Controller, and Actuator functions;
- Human Authority;
- Nested Control Lifecycle;
- Project Constraint Architecture;
- delivery Constraint Realization Map;
- Project Authorization and Project Reauthorization;
- DoR, DoD, and Release Gate;
- runtime operation and reassessment.

### Ownership preserved

- Organization owns authoritative sources, shared capabilities, and decision rights.
- Project owns viability, Project Constraint Architecture, authorization, inheritance, economics, and reauthorization.
- Delivery owns implementation-level Judgment Nodes, Constraint Realization Map, DoR, DoD, Release Gate, and local reassessment.
- Runtime exercises active realizations, produces evidence, and invokes authorized action; it does not automatically reauthorize the project.

### Capability boundaries preserved

- Constraint defines the approved boundary.
- Constraint Realization implements, enforces, or influences it.
- Sensor produces evidence.
- Controller compares or interprets evidence and selects or authorizes action.
- Actuator executes authorized change.
- Evaluator, gate decision, and release execution are not collapsed.
- A closed feedback loop is not represented as a complete bounded UA control architecture.

### Constraint trace aligned

`K-SEND-01` is one scoped **Human Authority** Constraint. Its complete realization uses deterministic authority controls, a separate human-operated send path, evidence, and authorized Actuators. The class is not recorded as a local hybrid taxonomy.

### Repository-state correction

The old blueprint incorrectly listed a complete project-to-runtime worked application as already present. The revised blueprint states the actual boundary:

- the repository contains one illustrative delivery-level support-triage review;
- a complete two-level project-and-delivery worked application remains roadmap work;
- the article's K-SEND-01 lifecycle narrative is an editorial synthesis, not evidence that the repository application already exists.

### Metadata and provenance

- frontmatter uses controlled topics and tags from `DOCUMENT-METADATA.md`;
- the article notes remain `status: research`, `maturity: draft`, and `draft: true` for publishing visibility;
- the research index uses the verified PDF boundary and does not claim an available or reviewed editable PPTX.

### External evidence boundary

Canonical repository sources define UA. They cannot, by themselves, prove factual claims about current standards, laws, platform capabilities, or market practice.

Phase 2 must:

- verify current external claims against primary or authoritative sources;
- verify named product capabilities against first-party documentation;
- date comparative claims where material;
- distinguish source-supported facts from practitioner observations and UA proposals.

## 6. Editorial review record

The original blueprint contained extensive draft-like prose, repeated headlines, multiple competing figure plans, and unresolved chapter questions.

The revised contract:

- retains one stable thesis paragraph;
- separates article structure from optional distribution framing;
- uses exactly three primary figures;
- keeps claim-safety rules in one section;
- distinguishes canonical UA sources from external factual evidence;
- defines one Phase 2 drafting sequence;
- removes instructions that attempted to draft the same final passage in several places;
- uses a target length of 4,300–5,200 words with section ranges totaling approximately 4,300–5,150 words.

## 7. Figure decision

### Figure 1 — Controlled-object shift

Shows why consequential runtime Model Judgment changes the engineered object.

### Figure 2 — Two orthogonal UA models

Shows:

- the four decision levels with downward inheritance and upward reassessment;
- the four capability families applying at every level;
- no one-to-one mapping, mandatory stack, or one-way waterfall.

### Figure 3 — K-SEND-01 Constraint trace

Shows:

```text
organizational source
→ scoped Project Constraint
→ delivery Constraint Realization
→ runtime evidence
→ delivery reassessment or project reauthorization

separate proposed authority expansion
→ project reauthorization and organizational review
```

The presentation's brain/nerves/skeleton/muscles stack is not used as the canonical article architecture diagram.

## 8. Worked narrative decision

The article will trace one Human Authority Constraint whose complete realization uses authority controls:

> The model-mediated path may create a draft but must not send customer communication without Human Authority.

The trace includes:

- organizational prohibition and decision rights;
- Project Constraint `K-SEND-01` with source, subject, path, scope, class, strength, realization, assumptions, failure behavior, evidence, and change authority;
- delivery realization through a no-send service identity, deterministic authorization gate, human-operated send path, auditable trace, fail-closed behavior, and tests;
- distinct DoR, DoD, and Release Gate decisions;
- local realization defect routed to delivery;
- capacity and economics failure routed to project reauthorization;
- a separate autonomous-send request routed to project reauthorization and organizational review.

This single trace replaces the earlier broad retelling of three Judgment Nodes and many controls.

## 9. Phase 1 exit checklist

- [x] PR #32 is merged into `main`.
- [x] Current `main` is integrated into the article branch through a merge commit.
- [x] One stable thesis paragraph exists.
- [x] The final section sequence is fixed.
- [x] Every section has a unique logical function.
- [x] The four decision levels are technically correct and central.
- [x] The four capability families are technically correct and orthogonal to the levels.
- [x] Constraint and Constraint Realization remain distinct.
- [x] Project authorization, DoR, DoD, Release Gate, runtime correction, and project reauthorization are not conflated.
- [x] Runtime evidence and proposed authority changes are not conflated.
- [x] Project Constraint Architecture and delivery Constraint Realization Map are the canonical Constraint artifacts.
- [x] Inheritance down and evidence up are demonstrated concretely.
- [x] The two living reviews are accurately scoped and not presented as universally sufficient.
- [x] The worked example has one fixed Constraint narrative and source boundary.
- [x] The platform boundary is precise and non-defensive.
- [x] Canonical terminology is aligned with the current glossary and doctrine.
- [x] Metadata uses controlled values.
- [x] Maturity, openness, validation, and repository-state claims are restrained.
- [x] Current external factual claims have an explicit Phase 2 verification rule.
- [x] Three figure briefs are agreed and introduce no new doctrine.
- [x] Word allocation and Phase 2 sequence are explicit and arithmetically consistent.
- [x] No unresolved architecture, logic, technical, metadata, or editorial blocker remains in the blueprint.
- [ ] Maintainer review explicitly freezes the editorial contract for drafting.

## 10. Phase 2 boundary

Phase 2 must be a separate branch and pull request after Phase 1 is accepted and PR #31 is merged.

Phase 2 will draft the article in four connected blocks:

1. problem and controlled-object doctrine;
2. bounded control and decision levels;
3. two reviews and the K-SEND-01 lifecycle trace;
4. platform boundary, current state, limits, openness, and invitation.

Each block must continue to defer to canonical repository sources. Article prose must not create new normative concepts by repetition, silently update repository maturity, treat historical publications as current definitions, or use internal UA material as evidence for current external facts.
