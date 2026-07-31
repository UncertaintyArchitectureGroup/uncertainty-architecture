---
title: Open Engineering Specification Article Phase 1 Review
artifact_type: research-note
status: research
maturity: draft
module: research
topics:
  - thinking-systems
  - control-loop
  - open-specification
  - publishing
  - repository-architecture
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/thinking-systems
  - ua/topic/control-loop
  - ua/topic/open-specification
created: 2026-07-31
updated: 2026-07-31
language: en
license: CC-BY-4.0
draft: true
---

# Phase 1 Editorial Review: Open Engineering Specification Article

> **Status:** Active work. Phase 1 is not complete. This note records the remaining architecture, logic, technical, and editorial work required before prose drafting may begin.

## 1. Review outcome

The current blueprint is materially stronger than a simple outline. It already contains the article thesis, audience, maturity boundary, chapter intent, transitions, worked example direction, platform boundary, planned figures, claim-safety notes, and a drafting sequence.

It is not yet ready to serve as the frozen Phase 1 structure.

The main problem is not missing content. It is that the blueprint currently contains more conceptual surfaces than the article can carry without repeating the repository or blurring the distinction between doctrine, lifecycle, artifacts, examples, and specification status.

Phase 1 should therefore end with a controlled reduction and ordering exercise, not with additional conceptual expansion.

## 2. Architectural review

### 2.1 Preserve one article-level center

The article requires one conceptual center:

```text
Thinking Systems change the controlled object
→ control must span four connected levels
→ authorization travels downward
→ evidence travels upward
→ two living artifacts make the lifecycle operable
```

The AI Control Plane explains how control becomes technically and socio-technically possible, but it should support the lifecycle rather than compete with it as a second organizing spine.

### 2.2 Separate three different structures

The final structure must keep these distinct:

1. **The four control levels**
   - organizational context;
   - project control architecture and viability;
   - delivery-level Thinking System Review;
   - runtime control and reauthorization.

2. **The control-loop capability model**
   - actuators;
   - constraints;
   - sensors and evidence;
   - controllers and decision authority.

3. **The two living review artifacts**
   - Project Control Architecture and Viability Review;
   - Thinking System Review.

The four levels describe decision ownership across the lifecycle. The control-loop model describes capabilities required to observe and change behavior. The two artifacts provide lightweight working surfaces. They must not be presented as interchangeable taxonomies.

### 2.3 Keep the article above template-field level

The article should explain why the two artifacts exist, what decisions they preserve, how they link, and how they prevent duplicated governance records. It should not reproduce their field structure. The repository remains the canonical implementation surface.

### 2.4 Keep organizational control as context, not a third UA artifact

UA does not define one mandatory organizational policy, committee, or governance document. Organizational constraints and shared capabilities are inherited from existing sources. The article must not accidentally imply that UA introduces a third living artifact at this level.

### 2.5 Keep runtime control distributed

Runtime control is not one runtime document or one platform component. It is the connected operation of evidence, thresholds, authority, containment, rollback, fallback, escalation, correction, and reauthorization. The article should avoid reducing runtime control to observability or automated evaluation.

## 3. Logic review

### 3.1 Tighten the opening claim

The phrase "The Missing Engineering Layer" is useful, but the article must avoid the historically weak claim that AI engineering has no methodology. Existing evaluation, safety, governance, MLOps, LLMOps, agent orchestration, security, and assurance practices are real.

The defensible claim is:

> Existing practices often remain fragmented across control levels and product boundaries. The missing layer is the connected engineering lifecycle that links project authorization, delivery evidence, runtime correction, and reauthorization.

### 3.2 Clarify why deterministic SDLC is insufficient without attacking it

The article should not claim that deterministic SDLC is obsolete. Traditional engineering remains necessary for deterministic boundaries, state, identity, access, transactions, policy enforcement, logging, rollback, and recovery.

The argument is narrower:

> Traditional SDLC does not by itself define how to authorize, evaluate, release, and continuously correct runtime Model Judgment whose acceptable behavior is bounded rather than exhaustively specified.

### 3.3 Avoid proving control theory twice

The blueprint currently risks explaining control theory once through the controlled-object shift and again through a full actuator–sensor–controller tutorial. The final article should use one concise control-theory bridge:

```text
reference intent
→ observed behavior and outcomes
→ error or deviation evidence
→ decision authority
→ corrective action
```

The four-layer capability model can then be introduced as the UA mapping, without repeating the entire earlier control-theory article.

### 3.4 Make the four-level lifecycle the answer, not another list

Each level should answer four consistent questions:

- What is being decided?
- What evidence is required?
- Who has authority?
- What causes reassessment?

This repeated logic will make the levels comparable and prevent the chapter from becoming four unrelated summaries.

### 3.5 Make inheritance and evidence operational

"Inheritance down / evidence up" must include explicit examples of what crosses each boundary.

Downward examples:

- prohibited authority;
- approved population, geography, data classes, and vendors;
- material risk scenarios;
- deterministic invariants;
- required controls;
- Human Authority capacity;
- control-cost assumptions;
- project authorization limits.

Upward examples:

- observed consequence severity exceeds the project assumption;
- escalation volume exceeds available Human Authority;
- evidence arrives too late to prevent harm;
- control cost destroys project viability;
- a model or provider change alters authority or behavior;
- a delivery change expands population, data, geography, tools, autonomy, or consequence level.

### 3.6 Keep the worked example as one continuous trace

The support-triage example should follow one decision path from project viability through runtime evidence. It should not become a second tutorial or repeat the completed reference architecture.

The example should demonstrate:

```text
business outcome
→ why Model Judgment is needed
→ material consequence scenarios
→ project authorization boundary
→ inherited delivery baseline
→ bounded Judgment Nodes
→ DoR and DoD evidence
→ deployment-specific Release Gate
→ runtime deviation
→ local correction or project reauthorization
```

### 3.7 Move the agent-framework relationship after application

The platform boundary is easier to understand after the reader has seen the lifecycle and worked example. Before that point, the section risks sounding defensive or competitive.

The conclusion should be simple:

> Agent frameworks may implement actuators, constraints, telemetry, evaluation hooks, approval steps, and rollback mechanisms. They do not independently own business authorization, residual-risk acceptance, Human Authority capacity, control economics, or reauthorization across organizational boundaries.

## 4. Technical review

### 4.1 Use current canonical terminology only

Current prose must use **Thinking Systems**, **Model Judgment**, **Judgment Node**, **Deterministic Core**, **Human Authority**, **Requirement**, **Operating Envelope**, **Project Control Architecture and Viability Review**, and **Thinking System Review** according to the glossary.

Historical terms such as **Behavioral Software**, **Linear Software**, and earlier fixed-role labels may be cited only as historical framing, not reused as current specification vocabulary.

### 4.2 Avoid fixed universal thresholds

The final article must not revive historical claims such as mandatory sample sizes, universal accuracy percentages, fixed review cadences, or required specialist job titles. Thresholds, sample sizes, metrics, and review cadence are context- and risk-derived.

### 4.3 Distinguish signals from decisions

A metric, evaluation, drift alert, or human observation is evidence. It becomes control only when connected to decision authority and a corrective mechanism capable of changing, containing, rolling back, escalating, suspending, or stopping behavior.

### 4.4 Keep project authorization, release, and reauthorization separate

These decisions must not collapse into one generic gate:

- **Project authorization** decides whether the complete control architecture is viable and acceptable.
- **Release Gate** decides whether a bounded implementation is acceptable for a stated deployment context.
- **Reauthorization** decides whether new evidence invalidates an earlier project or organizational decision.

### 4.5 Preserve the maturity boundary

The article may state that the repository now has a coherent and inspectable architectural spine, including doctrine, connected project and delivery patterns, control-plane capabilities, worked examples, and failure-mode structure.

It must also state that:

- the specification remains draft and evolving;
- independent implementation evidence is limited;
- thresholds and operating practices are not universally validated;
- UA is not a standard, certification, compliance regime, or finished universal operating model;
- publication is a request for application evidence and criticism, not a declaration of completion.

## 5. Editorial review

### 5.1 Recommended final chapter sequence

The Phase 1 structure should converge on this order:

1. **The Missing Engineering Connection**
2. **The Controlled Object Has Changed**
3. **Control Requires a Closed Decision Loop**
4. **Four Levels of Control**
5. **Authorization Down, Evidence Up**
6. **Two Living Review Artifacts**
7. **One End-to-End Worked Example**
8. **What Agent Platforms Can and Cannot Own**
9. **UA as an Open Engineering Specification**
10. **Current State, Limits, and Review Questions**

This keeps the article to ten chapters and gives each chapter one job.

### 5.2 Merge overlapping publication sections

"UA as an Open Engineering Specification," "Current State of the Specification," "Why Open," and "Invitation for Review" should not become four full chapters. They should form two closing chapters:

- what kind of artifact UA is and why it is open;
- what exists now, what is missing, and what evidence is requested.

### 5.3 Remove blueprint prose that prewrites the article

Phase 1 should retain:

- chapter purpose;
- required claims;
- exclusions;
- key examples;
- figure intent;
- transition logic;
- maturity constraints;
- acceptance criteria for the chapter.

It should remove or shorten passages that already attempt final rhetoric, repeated closing lines, and multiple alternative formulations. Otherwise Phase 2 becomes editing a hidden first draft rather than writing from an agreed architecture.

### 5.4 Limit figures to three

The article should use three canonical figures:

1. **Controlled-object shift** — deterministic logic versus bounded runtime Model Judgment.
2. **Four-level lifecycle** — organizational context, project authorization, delivery review, runtime evidence and reauthorization.
3. **Inheritance and evidence flow** — authorization and constraints downward, evidence and invalidated assumptions upward, with the two artifacts shown at project and delivery levels.

The worked example may use a compact inline trace, but should not require a fourth large conceptual diagram unless the text proves insufficient.

## 6. Phase 1 completion tasks

Phase 1 is complete only after the blueprint is revised to satisfy all items below.

### A. Structural convergence

- [ ] Freeze the ten-chapter sequence.
- [ ] Make the four-level lifecycle the single conceptual center.
- [ ] Keep the control-loop capability model subordinate to that lifecycle.
- [ ] Merge the four closing publication/status sections into two.
- [ ] Remove duplicated explanations of control theory, maturity, and platform boundaries.

### B. Chapter contracts

For every chapter, define:

- [ ] one purpose;
- [ ] one primary claim;
- [ ] required supporting distinctions;
- [ ] explicit exclusions;
- [ ] transition in;
- [ ] transition out;
- [ ] one completion criterion.

### C. Canonical alignment

- [ ] Recheck all terms against `00-doctrine/glossary.md`.
- [ ] Recheck the controlled-object argument against current doctrine.
- [ ] Recheck level ownership against `00-doctrine/nested-control-lifecycle.md`.
- [ ] Recheck project decisions against the Project Control Architecture and Viability Review.
- [ ] Recheck delivery decisions against the Thinking System Review.
- [ ] Recheck Control Plane claims against `02-ai-control-plane/`.
- [ ] Recheck maturity language against `SPECIFICATION.md`, `ROADMAP.md`, and the current repository state.

### D. Claim safety

- [ ] Replace absolute market-absence claims with fragmentation claims.
- [ ] Remove universal metrics, thresholds, sample sizes, role titles, and cadences.
- [ ] Keep control-theory language precise and avoid pretending that every socio-technical decision maps to a simple linear controller.
- [ ] State where the framework is synthesis, where it is draft normative content, and where evidence remains limited.

### E. Example and figures

- [ ] Reduce the support-triage example to one continuous project-to-runtime trace.
- [ ] Define the exact information shown in each of the three figures.
- [ ] Ensure no figure introduces a second taxonomy or new terminology.

### F. Phase 1 exit review

- [ ] Architecture review passed.
- [ ] Logic review passed.
- [ ] Technical review passed.
- [ ] Editorial review passed.
- [ ] Blueprint explicitly marked as frozen for Phase 2 drafting.
- [ ] Draft PR remains open and draft until the revised blueprint is reviewed.

## 7. Phase 1 exit condition

Phase 1 is not complete because the current blueprint still needs structural convergence, canonical rechecking, duplication removal, and chapter-level acceptance criteria.

Phase 2 may begin only when the blueprint can answer, without contradiction or repetition:

1. What exact problem does the article establish?
2. Why did the controlled object change?
3. Why does that require a connected control lifecycle?
4. What does each of the four levels decide?
5. What is inherited downward and what evidence travels upward?
6. Why are two living artifacts sufficient for the lightweight operating surface?
7. How does one example demonstrate the complete path?
8. What can implementation platforms own, and what remains organizational authority?
9. What kind of specification is UA today?
10. What evidence and criticism are being requested?

Until those answers are frozen, the document remains an active editorial blueprint rather than a drafting-ready article structure.
