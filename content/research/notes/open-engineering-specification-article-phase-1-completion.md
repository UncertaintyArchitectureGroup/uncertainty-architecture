---
title: Open Engineering Specification Article Phase 1 Completion Candidate Record
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

# Phase 1 Completion Candidate Record: Editorial Architecture

> **Current state:** The accepted architecture from PR #32 has been integrated into the branch. Architecture, logic, technical, metadata, repository, and editorial review have produced a drafting-ready editorial contract. Phase 1 remains open until explicit maintainer review and freeze; article prose has not begun.

## 1. Purpose

Phase 1 converts a large working skeleton into a stable editorial contract for the public synthesis article:

**Uncertainty Architecture: An Open Engineering Specification for Thinking Systems**  
*From project viability to delivery realization, runtime evidence, and reauthorization*

The output is not publishable prose and does not create specification authority. It defines:

- the article's central thesis and claim boundary;
- one unnumbered abstract and eight numbered sections;
- one unique logical job for every section;
- the canonical and external source rules;
- the three figures;
- the continuous illustrative Constraint trace;
- the maturity statement and external validation request;
- the Phase 2 repository path and drafting sequence.

## 2. Baseline integrated

The branch includes the current `main` baseline containing:

- the four-family Control-Loop Capability Anatomy;
- Constraint and Constraint Realization as distinct concepts;
- scoped Hard and Soft Constraint claims;
- Project Constraint Architecture and delivery Constraint Realization Map;
- the corrected Nested Control Lifecycle;
- current AI Control Plane, conformance, failure-mode, roadmap, and provenance decisions.

The earlier temporary dependency on PR #32 is resolved. The branch is ahead of and not behind `main`.

## 3. Architecture review decision

### Final reader journey

```text
missing engineering connection
→ controlled-object shift
→ model quality versus bounded control
→ four decision levels
→ two living reviews and inheritance
→ one illustrative Constraint across the lifecycle
→ platform implementation versus acquired authority
→ current specification state, limits, and validation request
```

### Final structure

Unnumbered abstract, followed by:

1. **The Missing Engineering Connection**
2. **The Controlled Object Has Changed**
3. **From Model Quality to Bounded Control**
4. **Four Decision Levels of Uncertainty Architecture**
5. **From Authority to Operation: Two Living Reviews**
6. **One Constraint Across the Full Lifecycle**
7. **What Platforms Can Implement — and What Authority They Do Not Acquire by Default**
8. **Open Specification: Current State, Limits, and Invitation**

### Structural decisions

- The four decision levels remain the conceptual center.
- The four capability families explain how control becomes operational at every level and do not become a second lifecycle.
- The control-theory material remains distinct because it establishes the difference between measurement, feedback closure, and bounded acceptable operation before the lifecycle is introduced.
- Inheritance and the two living artifacts are combined into one operating-path section.
- Openness, maturity, limitations, and invitation are combined into one ending.
- The worked narrative illustrates one Constraint rather than retelling the entire support-triage architecture or claiming real-world application evidence.
- The platform section allows bounded delegated Controller authority while rejecting automatic transfer of organizational or project authority.

## 4. Logic and editorial review record

The revised blueprint removes repeated or competing explanations of:

- deterministic versus model-mediated behavior;
- policies, tools, and evaluations being insufficient in isolation;
- feedback closure versus bounded operation;
- the four decision levels;
- inheritance and evidence routing;
- the two review artifacts;
- the platform boundary;
- repository maturity and openness.

The unnumbered abstract has a separate purpose and budget. Each numbered section contains:

- purpose;
- core claim;
- required supporting points;
- canonical source anchors;
- material not to repeat elsewhere;
- intended closing claim;
- word budget.

Each non-final numbered section contains a necessary transition. The final section closes the argument rather than creating another transition.

The final review also separates:

- runtime evidence that invalidates a delivery, project, or organizational basis;
- a proposed authority change that must enter the owning decision process before implementation;
- illustrative synthesis from independent application evidence.

## 5. Technical review record

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

`K-SEND-01` is one scoped **Human Authority** Constraint. Its complete realization uses deterministic authority controls, a separate human-operated send path, evidence, and authorized Actuators.

The Hard claim is bounded by:

- subject;
- every reachable model-mediated send path in the reviewed scope;
- stated assumptions;
- fail-closed behavior;
- alternate-path and bypass verification;
- active realization evidence.

DoD now requires coverage of every reachable send path in the reviewed scope and explicit proof that no alternate path bypasses the realization. “Every reviewed path” is not treated as sufficient evidence by itself.

### Repository-state boundary

The repository contains one illustrative delivery-level support-triage review. It does not yet contain a complete two-level project-and-delivery worked application.

The article's K-SEND-01 lifecycle narrative is an editorial synthesis that illustrates specification behavior. It is not evidence that the complete lifecycle has been independently applied.

### Metadata and provenance

- frontmatter uses controlled topics and tags from `DOCUMENT-METADATA.md`;
- the article notes remain `status: research`, `maturity: draft`, and `draft: true`;
- the blueprint H1 identifies the artifact as an article blueprint rather than presenting itself as completed article prose;
- the research index uses the verified PDF boundary and does not claim an available or reviewed editable PPTX.

### External evidence boundary

Canonical repository sources define UA. They cannot, by themselves, prove factual claims about current standards, laws, platform capabilities, or market practice.

Phase 2 must:

- verify current external claims against primary or authoritative sources;
- verify named product capabilities against first-party documentation;
- date comparative claims where material;
- distinguish source-supported facts from practitioner observations and UA proposals.

## 6. Figure decision

### Figure 1 — Controlled-object shift

Uses a two-panel view:

- primarily explicit runtime behavior;
- a Thinking System with bounded Model Judgment inside the controlled object.

It shows deterministic ingress and output/action responsibilities, Constraints and realizations around the Judgment region, observed outputs and outcomes, decision authority, and corrective paths without turning the four capability families into a mandatory pipeline.

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

The figure is labeled as an illustrative editorial synthesis. The presentation's brain/nerves/skeleton/muscles stack is not used as the canonical article architecture diagram.

## 7. Publication and repository decision

### Target length

The target remains 4,300–5,200 English words. The section ranges total 4,300–5,150 words.

### Draft location

Phase 2 article prose begins in a separate branch and pull request under:

```text
content/research/notes/open-engineering-specification-article-draft.md
```

The draft remains non-normative research material and must not be placed in the root README, doctrine, patterns, or another specification-owning file.

### Publication location

After editorial acceptance and public release, the normalized canonical repository edition belongs under:

```text
content/research/publications/uncertainty-architecture-open-engineering-specification.md
```

The research publications index and relevant history record must be updated. Medium and LinkedIn editions remain distribution copies linking back to the repository edition.

## 8. Phase 1 exit checklist

- [x] PR #32 is merged into `main`.
- [x] Current `main` is integrated into the article branch through a merge commit.
- [x] One stable thesis paragraph exists.
- [x] The unnumbered abstract and final section sequence are fixed.
- [x] Every numbered section has a unique logical function.
- [x] Every non-final numbered section has a necessary transition.
- [x] The four decision levels are technically correct and central.
- [x] The four capability families are technically correct and orthogonal to the levels.
- [x] Constraint and Constraint Realization remain distinct.
- [x] Project authorization, DoR, DoD, Release Gate, runtime correction, and project reauthorization are not conflated.
- [x] Runtime evidence and proposed authority changes are not conflated.
- [x] Project Constraint Architecture and delivery Constraint Realization Map are the canonical Constraint artifacts.
- [x] Inheritance down and evidence up are illustrated concretely.
- [x] The two living reviews are accurately scoped and not presented as universally sufficient.
- [x] The worked narrative has one fixed illustrative Constraint and source boundary.
- [x] The platform boundary allows delegated Controller authority without automatically transferring project or organizational authority.
- [x] Canonical terminology is aligned with the current glossary and doctrine.
- [x] Metadata uses controlled values.
- [x] Maturity, openness, validation, and repository-state claims are restrained.
- [x] Current external factual claims have an explicit Phase 2 verification rule.
- [x] Three figure briefs have distinct jobs and introduce no new doctrine.
- [x] Word allocation, source plan, repository path, and Phase 2 sequence are explicit.
- [x] No known architecture, logic, technical, metadata, repository, or editorial blocker remains in the blueprint.
- [ ] Maintainer review explicitly freezes the editorial contract for drafting.

## 9. Phase 2 boundary

Phase 2 must be a separate branch and pull request after Phase 1 is accepted and PR #31 is merged.

Draft in four connected blocks:

1. abstract, problem, and controlled-object doctrine;
2. bounded control and decision levels;
3. two reviews and the K-SEND-01 lifecycle trace;
4. platform boundary, current state, limits, openness, and invitation.

Each block must continue to defer to canonical repository sources. Article prose must not create new normative concepts by repetition, silently update repository maturity, treat historical publications as current definitions, present illustrative synthesis as application evidence, or use internal UA material as evidence for current external facts.
