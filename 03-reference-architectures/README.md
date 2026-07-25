# Reference Architectures

**Status:** Reference  
**Role:** Concrete, non-prescriptive compositions of UA concepts and patterns

## Purpose

This module contains concrete architectures that demonstrate how Uncertainty Architecture may be applied in real systems.

Reference architectures make abstract responsibilities visible: where model judgment occurs, which deterministic boundaries surround it, how evidence is collected, who or what controls change, and how failure is contained.

## Defines

This module provides:

- worked architectural compositions;
- examples of deterministic and probabilistic responsibility boundaries;
- possible distributions of AI Control Plane capabilities;
- implementation-oriented demonstrations of UA patterns;
- explicit assumptions, trade-offs, and unresolved design choices where available.

## Does not define

This module does not prescribe:

- a mandatory system topology;
- one preferred vendor, framework, or orchestration platform;
- universal controls for every risk class or operating context;
- conformance merely through copying an example;
- any reference implementation as the UA standard itself.

## Reference expectations

A mature reference architecture should identify:

1. the operating context and intended outcomes;
2. where probabilistic judgment occurs;
3. the deterministic boundaries and invariants;
4. relevant actuators, sensors, and controllers;
5. decision authority and human involvement;
6. failure, escalation, rollback, and containment paths;
7. known assumptions, limits, and trade-offs.

## Current scope

Indranet is one implementation-oriented expression of UA concepts. It is a reference, not the specification itself, and its design choices are not automatically normative.

## Relationships

- [`00-doctrine/`](../00-doctrine/) provides the conceptual foundation.
- [`01-patterns/`](../01-patterns/) provides reusable architectural building blocks.
- [`02-ai-control-plane/`](../02-ai-control-plane/) provides the control capability model used in compositions.
- [`04-failure-modes/`](../04-failure-modes/) provides failure mechanisms that references should address explicitly.
- [`SPECIFICATION.md`](../SPECIFICATION.md) defines why reference architectures remain outside the mandatory topology of the specification.
