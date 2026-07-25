# Core Doctrine

**Status:** Draft normative  
**Role:** Foundational vocabulary and architectural distinctions

## Purpose

This module defines the conceptual foundation used throughout Uncertainty Architecture (UA). It establishes how to reason about **Thinking Systems**: software systems whose runtime behavior depends partly on probabilistic model judgment while consequential boundaries, responsibilities, and corrective mechanisms remain explicit.

The doctrine provides the shared mental model needed to discuss uncertainty without treating model behavior as either ordinary deterministic code or uncontrollable magic.

## Defines

This module defines or develops the foundational distinctions behind:

- Thinking Systems;
- deterministic control logic and model judgment;
- the boundary between probabilistic behavior and deterministic system responsibilities;
- open and non-deterministic operating conditions;
- uncertainty containment rather than uncertainty elimination;
- the limits of metrics without decision authority and corrective action;
- the architectural importance of interfaces, invariants, feedback, and human authority.

## Does not define

This module does not prescribe:

- a specific model, vendor, framework, or implementation stack;
- a complete runtime control-plane design;
- one universal set of controls or evaluation thresholds;
- a mandatory organizational structure;
- a certification or conformance program.

## Key concepts

- **Thinking System** — a software system in which part of the runtime path or decision process is produced through model-mediated judgment.
- **Deterministic Core** — rules, invariants, permissions, data handling, and other responsibilities that must remain explicitly controlled.
- **Model Judgment** — interpretation, synthesis, classification, generation, or action selection under uncertainty.
- **Uncertainty Boundary** — the interface at which deterministic responsibilities meet probabilistic judgment.
- **Containment** — limiting where uncertainty may propagate and defining what happens when behavior leaves acceptable bounds.

Canonical wording will be consolidated in the project glossary. Until then, these descriptions establish the intended conceptual direction rather than final term-level conformance language.

## Relationships

- [`01-patterns/`](../01-patterns/) translates doctrine into reusable architectural responses.
- [`02-ai-control-plane/`](../02-ai-control-plane/) defines the capabilities used to constrain, observe, and correct model-mediated behavior.
- [`03-reference-architectures/`](../03-reference-architectures/) demonstrates possible compositions of the doctrine and patterns.
- [`04-failure-modes/`](../04-failure-modes/) records recurring mechanisms through which these distinctions are violated or lost.
- [`SPECIFICATION.md`](../SPECIFICATION.md) defines the status and normative boundary of this module.
