---
title: Requirements, Correctness, and Bugs in Thinking Systems
artifact_type: doctrine
status: draft-normative
maturity: active
module: doctrine
topics:
  - thinking-systems
  - requirements
  - operating-envelope
  - correctness
  - defects
  - model-judgment
tags:
  - ua/module/doctrine
  - ua/type/doctrine
  - ua/status/draft-normative
  - ua/topic/thinking-systems
  - ua/topic/model-judgment
canonical_for:
  - requirement-model
  - correctness-model
  - bug-model
source_basis:
  - "../content/raw/Designing Non-Deterministic Systems: Maintaining Engineering Rigor in the AI Era.pdf"
---

# Requirements, Correctness, and Bugs in Thinking Systems

## Status

This document is **draft normative**. It defines a candidate doctrine for requirements, correctness, and bugs when probabilistic Model Judgment performs part of the business logic of a Thinking System.

The presentation *Designing Non-Deterministic Systems: Maintaining Engineering Rigor in the AI Era* is a synthesis source for this formulation. The source remains historical research evidence; this document is the explicit framework decision that translates the relevant idea into current UA terminology.

## 1. Core relationship

A **Requirement** defines the approved operating contract of a system.

**Correctness** is the condition in which observed system behavior satisfies that contract.

A **Bug** is a violation of an approved Requirement caused or permitted by the implemented system.

This relationship applies to both Linear Software and Thinking Systems. What changes is how the Requirement can be specified and how compliance must be evaluated.

## 2. Requirements in Linear Software

For explicitly encoded deterministic behavior, a Requirement may prescribe one expected output, transition, or rule for defined inputs and conditions.

Correctness can often be evaluated by comparing the observed result directly with that expected result.

A violation is typically reproducible as a deterministic deviation from the specified behavior.

## 3. Requirements in Thinking Systems

When an LLM or another probabilistic model performs interpretation, classification, generation, planning, ranking, or action selection that contributes to business logic, one exact acceptable output cannot always be specified in advance.

A Requirement for Model Judgment therefore SHOULD define the approved **Operating Envelope** within which behavioral variation is acceptable for the intended business context.

Depending on the system and consequence level, the operating contract may include:

- intended outcomes;
- invariants that must never be delegated to probabilistic judgment alone;
- permitted behavioral variation;
- prohibited behaviors or regions;
- authority and action boundaries;
- business tolerances for relevant outcome distributions;
- evidence and evaluation expectations;
- required handling when behavior is uncertain or outside approved bounds;
- fallback, escalation, containment, rollback, or shutdown obligations.

The envelope MUST be derived from context and risk. A numerical threshold, sample size, evaluation score, or review cadence is not universal merely because it appears in an example or source.

## 4. Correctness under probabilistic business logic

Thinking Systems do not eliminate the concept of correctness. They change how correctness must be specified and demonstrated.

For a stochastic component that performs business logic, correctness cannot normally be reduced to whether one sampled output matches one predetermined answer.

Correctness is instead evaluated from evidence that the implemented system:

1. preserves required invariants;
2. keeps relevant behavior and outcomes within the approved Operating Envelope;
3. detects material deviations with sufficient evidence for the decision context;
4. executes the required control response when acceptable bounds are exceeded or cannot be established.

This makes correctness a system property. It depends on the model-mediated behavior together with deterministic boundaries, sensors, controllers, decision rights, and corrective mechanisms.

## 5. Canonical definition of Bug

> **A Bug is a violation of an approved Requirement caused or permitted by the implemented system.**

In Linear Software, this commonly appears as an incorrect deterministic result or transition.

In a Thinking System, a Bug may appear when:

- observed model-mediated behavior materially exceeds an approved business tolerance;
- the behavior or outcome leaves the approved Operating Envelope;
- an invariant is violated;
- a prohibited action is allowed;
- a required boundary, sensor, controller, or corrective mechanism is absent or ineffective;
- the system fails to contain, escalate, fall back, roll back, or stop as required.

For an LLM that performs business logic, a statistically evidenced excursion beyond an approved business tolerance is therefore a Bug **when that tolerance is part of the approved Requirement and the implemented system causes or permits the violation**.

This preserves the presentation's essential point without treating every rare or undesirable model output as a defect.

## 6. Event, evidence, and diagnosis must remain distinct

An individual undesirable output or out-of-envelope observation is first an event and may generate a **Deviation Signal**.

It is not automatically sufficient to diagnose a Bug because:

- the event may fall within an explicitly accepted residual-risk region;
- the available sample may be too weak to establish a material tolerance breach;
- the Requirement or Operating Envelope may be incomplete, ambiguous, or invalid;
- the event may have been correctly detected and handled by the required containment path;
- the observed symptom may arise from an external condition outside the system's stated responsibility.

Diagnosis SHOULD determine whether the system violated its approved operating contract and why.

Relevant classifications may include:

- deterministic implementation defect;
- statistically material tolerance breach;
- missing or invalid Requirement;
- missing boundary or constraint;
- inadequate sensor or evaluation design;
- controller or decision-authority failure;
- containment or recovery failure;
- accepted distribution tail handled as designed;
- invalid assumption about the operating context.

The **Bug** is the Requirement violation. A statistical excursion, evaluation result, incident, or user report is evidence used to establish that violation and its cause.

## 7. Consequences for engineering practice

Because Bug is derived from Requirement, changes to the requirement model propagate through the delivery system:

```text
Requirement model
      ↓
Correctness model
      ↓
Bug and incident classification
      ↓
Evaluation and testing strategy
      ↓
Definition of Done and release evidence
      ↓
Runtime observation and corrective action
```

Traditional pass/fail tests remain appropriate for deterministic rules and invariants.

Model-mediated business logic additionally requires evidence about behavioral distributions, consequential scenarios, boundaries, and control performance. Passing an evaluation suite does not by itself prove universal correctness; it supports a bounded release or operating decision.

## 8. Relationship to other UA concepts

- [`glossary.md`](glossary.md) contains the canonical concise definitions of Requirement, Operating Envelope, Correctness, Bug, and Deviation Signal.
- [`../02-ai-control-plane/`](../02-ai-control-plane/) defines the capabilities used to observe deviations and authorize corrective action.
- [`../01-patterns/`](../01-patterns/) may define reusable structures for specifying and evaluating operating envelopes.
- [`../04-failure-modes/`](../04-failure-modes/) distinguishes recurring mechanisms of control loss from individual defect instances.
- [`../content/research/notes/designing-nondeterministic-systems-source-intake.md`](../content/research/notes/designing-nondeterministic-systems-source-intake.md) records the presentation source and its normalization state.

## 9. Open questions

The following remain subject to further framework review:

- whether UA needs a separate canonical term for a statistically established tolerance breach;
- how requirement evidence should be represented across different risk and autonomy levels;
- how accepted residual risk should be documented without normalizing avoidable defects;
- how conformance claims should distinguish design adequacy from observed production performance.
