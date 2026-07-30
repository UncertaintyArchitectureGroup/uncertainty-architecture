---
title: Core Doctrine
artifact_type: doctrine
status: draft-normative
maturity: active
module: doctrine
topics:
  - thinking-systems
  - deterministic-core
  - model-judgment
  - uncertainty-boundary
  - containment
tags:
  - ua/module/doctrine
  - ua/type/doctrine
  - ua/status/draft-normative
  - ua/topic/thinking-systems
  - ua/topic/deterministic-core
  - ua/topic/model-judgment
  - ua/topic/uncertainty-boundary
canonical_for:
  - doctrine-module
---

# Core Doctrine

**Status:** Draft normative  
**Role:** Foundational vocabulary and architectural distinctions

## Purpose

This module defines the conceptual foundation used throughout Uncertainty Architecture (UA). It establishes how to reason about **Thinking Systems**: software systems whose runtime behavior depends partly on probabilistic model judgment while consequential boundaries, responsibilities, and corrective mechanisms remain explicit.

The doctrine provides the shared mental model needed to discuss uncertainty without treating model behavior as either ordinary deterministic code or uncontrollable magic.

## Defines

This module defines or develops the foundational distinctions behind:

- Thinking Systems;
- deterministic control logic and Model Judgment;
- the boundary between probabilistic behavior and deterministic system responsibilities;
- open-loop and closed-loop operating conditions;
- uncertainty containment rather than uncertainty elimination;
- the limits of metrics without decision authority and corrective action;
- the architectural importance of interfaces, invariants, feedback, and Human Authority;
- requirements, correctness, and bug classification when probabilistic Model Judgment performs business logic.

## Does not define

This module does not prescribe:

- a specific model, vendor, framework, or implementation stack;
- a complete runtime control-plane design;
- one universal set of controls or evaluation thresholds;
- a mandatory organizational structure;
- a certification or conformance program.

## Key concepts

- **Thinking System** — a software system in which part of the runtime path or decision process is produced through model-mediated judgment while consequential deterministic responsibilities remain explicit.
- **Deterministic Core** — rules, invariants, permissions, data handling, and other responsibilities that must remain explicitly controlled.
- **Model Judgment** — interpretation, synthesis, classification, generation, planning, or action selection under uncertainty.
- **Uncertainty Boundary** — the interface at which deterministic responsibilities meet probabilistic judgment.
- **Containment** — limiting where uncertainty may propagate and defining what happens when behavior leaves acceptable bounds.
- **Requirement** — the approved operating contract against which correctness and bugs are evaluated.
- **Operating Envelope** — the context- and risk-derived region within which behavioral variation remains acceptable.

The canonical wording for terms currently defined by UA is maintained in the [project glossary](glossary.md). Undefined or unresolved terms remain draft framework questions rather than implied requirements.

## Documents

- [`glossary.md`](glossary.md) — canonical draft-normative vocabulary for current UA terms.
- [`requirements-correctness-and-bugs.md`](requirements-correctness-and-bugs.md) — draft-normative relationship between requirements, operating envelopes, correctness, and bugs in Linear Software and Thinking Systems.

Process hypotheses, lifecycle sketches, and historical terminology belong in the Research Track unless deliberately adopted into doctrine.

## Relationships

- [`01-patterns/`](../01-patterns/) translates doctrine into reusable architectural responses.
- [`02-ai-control-plane/`](../02-ai-control-plane/) defines the capabilities used to constrain, observe, and correct model-mediated behavior.
- [`03-reference-architectures/`](../03-reference-architectures/) demonstrates possible compositions of the doctrine and patterns.
- [`04-failure-modes/`](../04-failure-modes/) records recurring mechanisms through which these distinctions are violated or lost.
- [`SPECIFICATION.md`](../SPECIFICATION.md) defines the status and normative boundary of this module.
