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
source_format: pptx
preserved_format: pdf-export
preserved_file: "content/raw/Designing Non-Deterministic Systems: Maintaining Engineering Rigor in the AI Era.pdf"
updated: 2026-07-31
license: CC-BY-4.0
---

# Designing Non-Deterministic Systems Source Intake

## Purpose

This note records the presentation deck used as a synthesis source for Uncertainty Architecture so that the Research Track distinguishes source evidence, preserved repository material, and explicit framework decisions.

## Source state

The maintainer-supplied original PPTX is the working source used for slide-level review and framework extraction.

The original PPTX is not currently preserved as a repository file. The repository preserves a PDF export under [`content/raw/`](../../raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf). The PDF provides an archival snapshot; it is not a substitute for the original PPTX when slide order, speaker notes, editable content, or presentation-specific detail matters.

Future work may preserve the original PPTX in `content/raw/` when the file and its licensing and attribution state are ready for repository storage. Until then, this intake note is the canonical repository record of the source relationship.

The deck has not been converted into a complete reviewable Markdown transcript or normalized repository edition. Slide content remains research evidence and does not become normative merely because it has been reviewed or preserved.

## Why the source matters

The deck consolidates UA concepts for a practitioner audience, including:

- the shift from deterministic software assumptions to Thinking Systems;
- non-zero runtime variance and probabilistic operating space;
- the claim that LLMs change the engineering object itself rather than acting as an ordinary API integration;
- the AI–code uncertainty boundary;
- control-theory framing for model-mediated systems;
- Actuators, Constraints, Sensors, Controllers, evidence, and corrective action;
- functional locations where Model Judgment creates value;
- lifecycle and operating-model implications;
- system-level risks that extend beyond model quality;
- architectural veto, cost boundaries, and the limits of building at the edge of research-grade uncertainty;
- the relationship between Requirements, approved business tolerances, Correctness, and Bugs.

Because a presentation compresses arguments and may omit qualifications used in longer publications, its claims must be translated through explicit framework review rather than copied directly.

## Slides 1–6 framework-transfer state

The maintainer-defined slides 1–6 transfer scope has been reviewed against the original PPTX and translated into:

- [`00-doctrine/requirements-correctness-and-bugs.md`](../../../00-doctrine/requirements-correctness-and-bugs.md) — mixed Requirements, Operating Envelopes, Correctness, Bugs, and diagnostic sources;
- [`00-doctrine/model-judgment-placement.md`](../../../00-doctrine/model-judgment-placement.md) — Input Interpretation, Decision Logic, and Output Mediation as a functional taxonomy;
- [`01-patterns/judgment-node-boundary.md`](../../../01-patterns/judgment-node-boundary.md) — explicit boundaries around consequential Judgment Nodes;
- [`01-patterns/thinking-system-review.md`](../../../01-patterns/thinking-system-review.md) — one delivery-level review flow with model-mediated DoR and DoD extensions, a distinct Release Gate, responsibility bundles, inherited project Constraints, concrete realization, and reassessment;
- [`01-patterns/thinking-system-review-template.md`](../../../01-patterns/thinking-system-review-template.md) — one living SMB delivery artifact;
- [`03-reference-architectures/judgment-placement-examples.md`](../../../03-reference-architectures/judgment-placement-examples.md) — isolated and composite placement reference architectures;
- [`content/research/framework-traceability.md`](../framework-traceability.md) — current source-to-framework decisions and resolved presentation shorthand.

The slides 1–6 transfer is complete at the current draft-framework level. Later application evidence may still refine the resulting doctrine, patterns, and template.

## Slide 12 framework-transfer state

Slide 12 presents a four-layer control stack:

- **L4 Controller** — brain / judgment;
- **L3 Sensors** — nerves / measurement;
- **L2 Constraints** — skeleton / structure;
- **L1 Actuators** — muscles / execution.

The slide also maps named software examples to those layers, including Prompt Registry, semantic kill switches, HITL gateways, policy changes, Golden Sets, evaluation gates, drift metrics, semantic monitors, JSON Schema, Pydantic, typed interfaces, LangChain, APIs, data pipelines, and tool orchestration.

### Accepted framework decision

UA adopts the slide's durable distinction among four logical capability functions:

1. **Constraints** define or enforce the allowed operating space.
2. **Sensors and evidence** make behavior, outcomes, operating conditions, violations, and control health observable.
3. **Controllers and decision authority** interpret evidence and authorize decisions.
4. **Actuators and corrective action** execute authorized changes to behavior or operating conditions.

This decision is represented in:

- [`00-doctrine/control-loop-anatomy.md`](../../../00-doctrine/control-loop-anatomy.md);
- [`00-doctrine/glossary.md`](../../../00-doctrine/glossary.md);
- [`00-doctrine/nested-control-lifecycle.md`](../../../00-doctrine/nested-control-lifecycle.md);
- [`02-ai-control-plane/`](../../../02-ai-control-plane/);
- [`02-ai-control-plane/01-constraints/`](../../../02-ai-control-plane/01-constraints/);
- project and delivery review patterns and templates;
- reference-architecture expectations;
- the failure-mode taxonomy.

### Narrowing and rejected literal interpretation

UA does **not** adopt slide 12 as:

- a mandatory four-service or four-product topology;
- a required vertical execution order;
- a universal mapping of named tools to one layer;
- a claim that each tool supplies a complete capability by itself.

The current interpretation is functional:

- a Prompt Registry may provide traceability, soft-Constraint configuration, or Actuator inputs; it is not automatically a Controller;
- a semantic monitor or evaluation gate may act as a Sensor;
- JSON Schema, Pydantic, typed interfaces, and grammars may realize structural Constraints but do not establish semantic correctness;
- a HITL gateway may realize a Human Authority Constraint, Controller interface, evidence capture, or several functions together;
- a kill switch may be an Actuator, but not a functioning control loop without authority and operability;
- LangChain, APIs, data pipelines, and orchestration frameworks may host execution or several capability functions but are not Actuators merely by product category.

One component may realize several capability functions, and one capability may be distributed across technical and human mechanisms. Classification follows system function, guarantee, evidence, decision authority, and corrective path.

### Relationship to the four decision levels

The four capabilities are orthogonal to the four UA decision levels.

- The **Nested Control Lifecycle** identifies where decisions are owned: organizational, project, delivery, and runtime.
- The **Control-Loop Capability Anatomy** identifies which functions make those decisions operational: Constraints, Sensors, Controllers, and Actuators.

The presentation metaphor remains a useful explanatory device, but it is not the canonical architecture diagram or conformance topology.

## Additional framework extraction beyond slides 1–6 and 12

A later review pass used the original PPTX—not the repository PDF export—to examine the opening thesis, mathematical framing, process-shift material, architectural-veto section, role implications, and closing feedback-loop model.

This pass informed:

- [`00-doctrine/uncertainty-in-the-controlled-object.md`](../../../00-doctrine/uncertainty-in-the-controlled-object.md);
- [`00-doctrine/nested-control-lifecycle.md`](../../../00-doctrine/nested-control-lifecycle.md);
- [`01-patterns/project-control-architecture-and-viability-review.md`](../../../01-patterns/project-control-architecture-and-viability-review.md);
- [`01-patterns/project-control-architecture-and-viability-review-template.md`](../../../01-patterns/project-control-architecture-and-viability-review-template.md).

Together, these documents translate the deck's argument that:

- the model-mediated part of the system moves from an explicitly computed function toward sampling from a conditional distribution;
- uncertainty therefore exists inside the controlled object during runtime judgment;
- Scrum, Agile, DevOps, QA, security, and operations remain necessary but do not automatically define the control contract for probabilistic business judgment;
- project authorization must be distinguished from delivery release;
- project risk must be translated into Constraints and required control capabilities rather than represented only by a generic score;
- authoritative Constraints flow downward while realization becomes more concrete at project, delivery, and runtime levels;
- runtime evidence may require local correction, project reauthorization, or organizational review;
- architectural veto is part of engineering rigor when Constraint realization, evidence, safety, operational capacity, latency, vendor volatility, missing controls, or control cost make the proposed path non-viable.

The framework narrows several presentation formulations:

- UA complements rather than replaces existing delivery and operations disciplines;
- the nested lifecycle is a conceptual distinction, not a mandatory sequence of ceremonies or departments;
- the four-capability anatomy is a functional model, not a mandatory product stack;
- a material release contains a controlled evidence-generating component but remains bound by an approved Requirement, project authorization, and Constraint baseline;
- architectural veto has no universal score, expected-value threshold, or role owner;
- material risk is mapped through scenarios connected to consequences, detectability, feedback latency, reversibility, propagation, Constraints, capabilities, and residual risk;
- expected-value reasoning is optional and cannot override hard prohibitions or unavailable controls;
- one living project review and one living delivery review preserve distinct decision ownership without requiring separate project-gate, Constraint Register, or release-decision records.

This extraction does not mean the entire deck has been normalized or promoted. Unreviewed role, threshold, metric, and topology claims remain research context.

## Interpretation decisions

The transfer preserves the deck's engineering concerns while narrowing presentation shorthand:

- a statistical excursion or undesirable tail event is evidence, not automatically a Bug;
- a Bug is a system-level violation of an approved Requirement;
- the Operating Envelope is part of the complete Requirement, not its synonym;
- deterministic verification remains necessary alongside behavioral evidence;
- sample sizes, confidence methods, metrics, tolerances, and thresholds are context-derived rather than universal;
- Input Interpretation, Decision Logic, and Output Mediation are functional placement classes, not a mandatory pipeline;
- Constraints, Sensors, Controllers, and Actuators are logical capabilities, not mandatory services;
- a soft Constraint does not create a hard guarantee;
- responsibility bundles and Human Authority do not imply mandatory job titles;
- reference architectures remain non-prescriptive;
- project authorization, delivery release, and runtime reauthorization are distinct decisions with separate canonical owners;
- project context and Constraints flow to delivery through a versioned inheritance package rather than duplicated risk, policy, and economic records;
- delivery owns concrete Constraint realization and verification;
- runtime evidence returns to the decision level whose assumption, Constraint, capability, authority, or economic basis it invalidates.

## Remaining follow-up

1. Preserve the original PPTX in `content/raw/` when appropriate and available for repository storage.
2. Create a complete Markdown transcript or normalized repository edition with slide-level provenance only when useful.
3. Continue reviewing later deck sections against the broader publication corpus rather than promoting presentation shorthand in isolation.
4. Record contradictions, superseded claims, and newly extracted entities in the existing research-to-framework traceability matrix.
5. Build a two-level worked application that traces one or more Constraints from organizational source through project derivation, delivery realization, runtime enforcement and evidence, and reauthorization.
6. Use real-team or documented real-system evidence to test whether the capability taxonomy and two review surfaces are proportionate, complete, non-duplicative, operable, and economically useful.
7. Refine risk-tolerance derivation, control economics, Human Authority, incident loops, Constraint conflicts, and failure modes only where application evidence exposes a concrete gap.

Research-state changes should be reconciled under the [`Research Review Process`](../review-process.md) rather than tracked through a parallel presentation ledger.
