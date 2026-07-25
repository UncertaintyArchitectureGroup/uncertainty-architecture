# Interface and Control Patterns

**Status:** Draft normative  
**Role:** Reusable architectural responses for recurring control problems

## Purpose

This module contains reusable patterns for engineering the boundary between deterministic software responsibilities and probabilistic model judgment in Thinking Systems.

Patterns turn UA doctrine into reviewable design choices. They describe where uncertainty may enter a workflow, how it is bounded, what evidence is produced, and how failure is contained or escalated.

## Defines

This module defines or develops patterns for:

- separating judgment nodes from deterministic control logic;
- preserving hard invariants around probabilistic behavior;
- expressing soft constraints without confusing them with guarantees;
- validating, gating, retrying, containing, or escalating model outputs;
- maintaining traceability across model-mediated decisions;
- creating procedural interfaces between code, models, tools, and human authority.

## Does not define

This module does not prescribe:

- one universal workflow or orchestration framework;
- a fixed implementation technology;
- identical controls for systems with different consequences and operating contexts;
- reference architectures as mandatory deployment topologies;
- universal numerical thresholds for acceptable behavior.

## Pattern expectations

A mature UA pattern should make the following explicit:

1. the recurring problem and operating context;
2. the uncertainty or failure mechanism being addressed;
3. the deterministic responsibilities that must remain intact;
4. the proposed control structure;
5. the evidence or signals needed to operate it;
6. escalation, fallback, or recovery behavior;
7. important trade-offs and known limits.

Examples attached to a pattern are informative unless explicitly classified otherwise.

## Key concepts

- judgment node;
- deterministic boundary;
- hard invariant;
- soft constraint;
- procedural interface;
- validation gate;
- fallback and escalation;
- containment of non-determinism.

## Relationships

- [`00-doctrine/`](../00-doctrine/) provides the foundational distinctions used by the patterns.
- [`02-ai-control-plane/`](../02-ai-control-plane/) provides the control capabilities through which patterns are operated.
- [`03-reference-architectures/`](../03-reference-architectures/) demonstrates possible combinations of patterns.
- [`04-failure-modes/`](../04-failure-modes/) provides the failure mechanisms that patterns should mitigate.
- [`SPECIFICATION.md`](../SPECIFICATION.md) defines the status and normative boundary of this module.
