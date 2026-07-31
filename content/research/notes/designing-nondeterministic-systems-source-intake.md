---
title: Designing Non-Deterministic Systems Source Intake
artifact_type: research-note
status: research
maturity: active
module: research
topics:
  - provenance
  - thinking-systems
  - control-loop
  - constraints
  - sdlc
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/provenance
  - ua/topic/thinking-systems
  - ua/topic/control-loop
  - ua/topic/constraints
source_title: Designing Non-Deterministic Systems — Maintaining Engineering Rigor in the AI Era
source_format: pdf-export
preserved_format: pdf
preserved_file: "content/raw/Designing Non-Deterministic Systems: Maintaining Engineering Rigor in the AI Era.pdf"
updated: 2026-07-31
license: CC-BY-4.0
---

# Designing Non-Deterministic Systems Source Intake

## Purpose

This note records the presentation deck used as a synthesis source for Uncertainty Architecture so that the Research Track distinguishes source evidence, preserved repository material, and explicit framework decisions.

## Source state

The source currently available for repository review is a maintainer-supplied PDF export. The repository preserves a PDF snapshot under [`content/raw/`](../../raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf).

An editable PPTX is not currently preserved or independently verified in the repository. Claims about speaker notes, hidden slides, editable object structure, or PPTX-only content therefore remain outside the verified source boundary until the original file is deliberately preserved and reviewed.

The deck has not been converted into a complete reviewable Markdown transcript or normalized repository edition. Slide content remains research evidence and does not become normative merely because it has been reviewed or preserved.

## Why the source matters

The deck consolidates UA concepts for a practitioner audience, including:

- the shift from deterministic software assumptions to Thinking Systems;
- non-zero runtime variance and probabilistic operating space;
- the claim that LLMs change the engineering object rather than acting as an ordinary API integration;
- the AI–code uncertainty boundary;
- control-theory framing for model-mediated systems;
- Actuators, Constraints, Sensors, Controllers, evidence, and corrective action;
- functional locations where Model Judgment creates value;
- lifecycle and operating-model implications;
- system-level risks beyond model quality;
- architectural veto, cost boundaries, and research-grade uncertainty;
- the relationship among Requirements, tolerances, Correctness, and Bugs.

Because a presentation compresses arguments and may omit qualifications used in longer publications, its claims must be translated through explicit framework review rather than copied directly.

## Slides 1–6 framework-transfer state

The current framework translation of the opening material is represented in:

- [`00-doctrine/requirements-correctness-and-bugs.md`](../../../00-doctrine/requirements-correctness-and-bugs.md);
- [`00-doctrine/model-judgment-placement.md`](../../../00-doctrine/model-judgment-placement.md);
- [`01-patterns/judgment-node-boundary.md`](../../../01-patterns/judgment-node-boundary.md);
- [`01-patterns/thinking-system-review.md`](../../../01-patterns/thinking-system-review.md);
- [`01-patterns/thinking-system-review-template.md`](../../../01-patterns/thinking-system-review-template.md);
- [`03-reference-architectures/judgment-placement-examples.md`](../../../03-reference-architectures/judgment-placement-examples.md);
- [`content/research/framework-traceability.md`](../framework-traceability.md).

The transfer is complete at the current draft-framework level. Application evidence may still refine the resulting doctrine, patterns, and templates.

## Slide 12 framework-transfer state

Slide 12, **Anatomy of the AI Controller**, presents a four-layer teaching stack:

- **L4 Controller** — brain / judgment;
- **L3 Sensors** — nerves / measurement;
- **L2 Constraints** — skeleton / structure;
- **L1 Actuators** — muscles / execution.

It maps named examples to those layers:

- Prompt Registry, semantic kill switches, HITL gateways, and runtime policy changes;
- Golden Sets, Eval Gates, drift metrics, and semantic monitors;
- JSON Schema, Pydantic validators, and typed interfaces;
- LangChain, APIs, data pipelines, and tool orchestration.

The slide concludes that execution, limits, measurement, and judgment must form one loop and uses the shorthand: `REMOVE ONE LAYER AND THE CONTROL LOOP OPENS`.

### Accepted framework decision

UA adopts the durable distinction among four logical capability functions:

1. **Constraints** define approved operating boundaries.
2. **Sensors and evidence** make behavior, outcomes, operating conditions, realization state, Actuator execution, and control health observable.
3. **Controllers and decision authority** compare or interpret evidence and select or authorize action.
4. **Actuators and corrective action** execute authorized changes to operation.

The decision is represented in:

- [`00-doctrine/control-loop-anatomy.md`](../../../00-doctrine/control-loop-anatomy.md);
- [`00-doctrine/glossary.md`](../../../00-doctrine/glossary.md);
- [`00-doctrine/nested-control-lifecycle.md`](../../../00-doctrine/nested-control-lifecycle.md);
- [`02-ai-control-plane/`](../../../02-ai-control-plane/);
- [`02-ai-control-plane/01-constraints/`](../../../02-ai-control-plane/01-constraints/);
- project and delivery review patterns and templates;
- reference-architecture expectations;
- the failure-mode taxonomy.

### Narrowing and rejected literal interpretations

UA does **not** adopt slide 12 as:

- a mandatory four-service or four-product topology;
- a required vertical execution order;
- a universal mapping of named tools to one layer;
- a claim that each named tool supplies a complete capability;
- a literal control-theory claim that removing Constraints opens the feedback edge.

The current interpretation distinguishes a closed feedback loop from a complete bounded UA control architecture:

```text
Closed feedback loop
= controlled process → Sensor → Controller → Actuator → controlled process

Complete UA control architecture
= closed feedback loop
+ approved Requirement
+ explicit Constraints and realizations
+ bounded decision authority
+ realization and execution evidence
+ reassessment path
```

Removing effective sensing, decision, or actuation can leave the system open-loop or unable to correct. Removing explicit Constraints may leave the loop closed while allowing unsafe, unauthorized, or economically unacceptable operation.

### Function-based interpretation of the named examples

- A **Prompt Registry** may provide configuration, traceability, evidence, or Actuator inputs. It is not automatically a Controller.
- A **semantic monitor** normally performs a Sensor function.
- **Golden Scenarios**, an evaluation runner, and metrics produce Sensor evidence.
- Threshold or policy logic selecting `block`, `canary`, or `release` performs a Controller function.
- Deployment, exposure change, block execution, or rollback performs an Actuator function.
- JSON Schema, Pydantic, typed interfaces, and grammars may realize structural Constraints but do not establish semantic correctness.
- A HITL gateway may realize an approval Constraint, a Controller interface, evidence capture, an Actuator path, or several functions together.
- A kill-switch endpoint normally performs an Actuator function and does not form a complete control loop without authority, evidence, and operability.
- LangChain, APIs, data pipelines, and orchestration frameworks may host execution or several capability functions but are not Actuators merely by product category.

Classification follows the function, guarantee, evidence, decision authority, and corrective path in the specific system.

### Constraint versus Constraint Realization

The slide visually groups schemas and validators under Constraints. UA narrows this relationship:

- a **Constraint** is the approved boundary;
- a **Constraint Realization** is the mechanism implementing, enforcing, or influencing it;
- a realization may block an attempted action;
- a Sensor provides evidence about realization state and effects;
- a Controller authorizes change;
- an Actuator executes the change.

### Hard and soft interpretation

A Hard Constraint deterministically prevents or rejects violation within stated assumptions, scope, and enforcement boundaries.

A probabilistic detector, evaluator, prompt, model policy, or natural-language instruction does not become hard merely because its failure behavior is documented. A composite control may use probabilistic sensing and deterministic downstream enforcement, but the claimed guarantee must follow the complete realized path and its assumptions.

### Relationship to the four decision levels

The four capabilities are orthogonal to the four UA decision levels.

- The **Nested Control Lifecycle** identifies where decisions are owned: organizational, project, delivery, and runtime.
- The **Control-Loop Capability Anatomy** identifies which functions make those decisions operational: Constraints, Sensors, Controllers, and Actuators.

The presentation stack remains a useful teaching metaphor. It is not the canonical architecture diagram or conformance topology.

## Additional framework extraction

The PDF was also reviewed for its opening thesis, mathematical framing, process-shift material, architectural-veto section, role implications, and closing feedback-loop model.

This informed:

- [`00-doctrine/uncertainty-in-the-controlled-object.md`](../../../00-doctrine/uncertainty-in-the-controlled-object.md);
- [`00-doctrine/nested-control-lifecycle.md`](../../../00-doctrine/nested-control-lifecycle.md);
- [`01-patterns/project-control-architecture-and-viability-review.md`](../../../01-patterns/project-control-architecture-and-viability-review.md);
- [`01-patterns/project-control-architecture-and-viability-review-template.md`](../../../01-patterns/project-control-architecture-and-viability-review-template.md).

The framework translates the deck's argument that:

- a model-mediated responsibility samples from a space of plausible outcomes;
- uncertainty is therefore produced inside the controlled object during runtime judgment;
- existing product, delivery, QA, security, and operations disciplines remain necessary but do not automatically define the control contract for probabilistic business judgment;
- project authorization must be distinguished from delivery release;
- project risk must be translated into Constraints and required control capabilities rather than only a generic score;
- Constraint authority flows downward while realization becomes more concrete;
- runtime evidence may require local correction, project reauthorization, or organizational review;
- architectural veto is part of engineering rigor when realization, evidence, authority, capacity, latency, vendor dependence, or control cost make the path non-viable.

## Interpretation decisions

The transfer preserves the deck's engineering concerns while narrowing presentation shorthand:

- a statistical excursion or undesirable tail event is evidence, not automatically a Bug;
- a Bug is a system-level violation of an approved Requirement;
- the Operating Envelope is part of the Requirement, not its synonym;
- deterministic verification remains necessary alongside behavioral evidence;
- sample sizes, confidence methods, metrics, tolerances, and thresholds are context-derived;
- Input Interpretation, Decision Logic, and Output Mediation are functional placement classes, not a mandatory pipeline;
- Constraints, Sensors, Controllers, and Actuators are logical capabilities, not mandatory services;
- Constraint and Constraint Realization remain distinct;
- a Soft Constraint does not create a hard guarantee;
- responsibility bundles and Human Authority do not imply mandatory job titles;
- project authorization, delivery release, and runtime reassessment remain separate decisions;
- delivery records one canonical Constraint Realization Map rather than repeating the same Constraint definition at every phase;
- runtime evidence returns to the decision level whose assumption, Constraint, capability, authority, or economic basis it invalidates.

## Remaining follow-up

1. Preserve and verify the editable PPTX only when the original file and its licensing state are ready for repository storage.
2. Create a complete Markdown transcript or normalized edition only when slide-level provenance would provide clear value.
3. Continue reviewing the deck against the broader publication corpus rather than promoting presentation shorthand in isolation.
4. Record contradictions, superseded claims, and newly extracted entities in the existing research-to-framework traceability matrix.
5. Build a two-level worked application tracing Constraints from source through project derivation, delivery realization, runtime operation, evidence, and reauthorization.
6. Use real-team or documented real-system evidence to test whether the capability taxonomy and two review surfaces are proportionate, complete, operable, and economically useful.
7. Refine Constraint conflicts, precedence, control economics, Human Authority, incident loops, and failure modes only where application evidence exposes a concrete gap.

Research-state changes should be reconciled under the [`Research Review Process`](../review-process.md) rather than tracked through a parallel presentation ledger.
