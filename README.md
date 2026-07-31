# Uncertainty Architecture (UA)

## Engineering at the AI–Code Boundary

**Uncertainty Architecture** is an open doctrine and pattern language for building and operating software in which part of runtime behavior is delegated to **non-deterministic Model Judgment**, while consequential deterministic responsibilities, approved Constraints, evidence, decision rights, and corrective mechanisms remain explicit.

UA is designed primarily for small and medium-sized engineering organizations that need practical control without building a large governance bureaucracy.

## Why UA Exists

Traditional software is engineered primarily as explicitly encoded behavior:

```text
y = f(x)
```

A Thinking System delegates part of runtime interpretation, synthesis, planning, or path selection to a probabilistic model:

```text
y ~ P(y | x, context, model configuration)
```

Some consequential behavior is therefore generated during operation rather than fully enumerated in advance. This changes the controlled object itself.

UA complements product discovery, Agile, DevOps, QA, security, change management, and incident response with a project-to-runtime control lifecycle for model-mediated behavior.

Read [`Uncertainty in the Controlled Object`](00-doctrine/uncertainty-in-the-controlled-object.md).

## Two Orthogonal Models

### Where is a decision owned?

The [`Nested Control Lifecycle`](00-doctrine/nested-control-lifecycle.md) distinguishes:

1. organizational control context;
2. project control architecture and viability;
3. delivery-level Thinking System Review;
4. runtime control and reauthorization.

### Which functions make control operational?

The [`Control-Loop Capability Anatomy`](00-doctrine/control-loop-anatomy.md) distinguishes:

1. **Constraints** — approved operating boundaries;
2. **Sensors and evidence** — observation of behavior, outcomes, realization state, and control health;
3. **Controllers and decision authority** — comparison, interpretation, and authorization;
4. **Actuators and corrective action** — execution of authorized change.

The decision levels are not capability layers. The capabilities are not mandatory services.

## Core Control Model

```mermaid
flowchart LR
    R[Authorized intent,<br/>Requirement, and assumptions]
    K[Constraints<br/>approved operating boundaries]
    KR[Constraint Realizations<br/>enforce or influence the boundary]
    P[Thinking System]
    S[Sensors and evidence<br/>behavior · outcomes · conditions<br/>realization and execution state]
    C[Controller and decision authority<br/>compare · interpret · authorize]
    A[Actuators<br/>execute authorized change]

    R --> C
    R --> K
    K --> KR
    K -. defines decision boundary .-> C
    K -. defines action boundary .-> A
    KR -. bounds .-> P
    KR -. gates .-> A
    P --> S
    KR -->|state, violations, and health| S
    A -->|execution state and effects| S
    S --> C
    C -->|authorized action| A
    A --> P
    A -->|authorized realization change| KR
```

A **Constraint** is the approved boundary. A **Constraint Realization** is the mechanism implementing, enforcing, or influencing it. A **Controller** selects or authorizes action. An **Actuator** executes it.

A closed feedback loop can still be unsafe or over-authorized. Constraints bound the space in which the loop may operate; they are not the feedback edge itself.

Canonical definitions live in:

- [`Control-Loop Capability Anatomy`](00-doctrine/control-loop-anatomy.md)
- [`Glossary`](00-doctrine/glossary.md)
- [`AI Control Plane`](02-ai-control-plane/)

## Practical SMB Path

UA uses two living review surfaces with different ownership.

### Project authorization

The [`Project Control Architecture and Viability Review`](01-patterns/project-control-architecture-and-viability-review.md) connects:

- business outcome and AI necessity;
- project boundary and material scenarios;
- one canonical Project Constraint Architecture;
- required realizations, Sensors, Controllers, Actuators, Human Authority, fallback, containment, rollback, compensation, and shutdown;
- evidence feasibility, capacity, and control economics;
- authorization, conditions, bounded research, redesign, deferral, escalation, or No-Go;
- a versioned delivery-inheritance baseline;
- project reauthorization.

Use the [`project review template`](01-patterns/project-control-architecture-and-viability-review-template.md).

### Delivery realization and release

The [`Thinking System Review`](01-patterns/thinking-system-review.md) applies the project boundary to one bounded system, feature, or material change through:

- implementation-level Judgment Nodes;
- the delivery Requirement and Operating Envelope;
- one canonical Constraint Realization Map;
- Definition of Ready;
- implementation or bounded experiment;
- Definition of Done;
- deployment-specific Release Gate;
- runtime evidence and reassessment.

Use the [`delivery review template`](01-patterns/thinking-system-review-template.md).

A successful demo is not project authorization. DoD is not release authorization. A Release Gate does not expand the project boundary. `No-Go` remains a valid engineering result.

## Constraint Engineering

Constraints may address structure, authority, states, data, context, resources, exposure, environment, dependencies, Human Authority, and probabilistic behavioral influence.

A **Hard Constraint** deterministically prevents or rejects violation within stated assumptions, scope, and enforcement boundaries.

A prompt, natural-language policy, probabilistic evaluator, classifier, or model policy is not hard by itself.

See:

- [`Constraint Capabilities`](02-ai-control-plane/01-constraints/)
- [`Constraint Realization Catalog`](02-ai-control-plane/01-constraints/constraint-realization-catalog.md)

Named technologies are examples, not requirements.

## Start Here

1. [`SPECIFICATION.md`](SPECIFICATION.md)
2. [`00-doctrine/uncertainty-in-the-controlled-object.md`](00-doctrine/uncertainty-in-the-controlled-object.md)
3. [`00-doctrine/control-loop-anatomy.md`](00-doctrine/control-loop-anatomy.md)
4. [`00-doctrine/nested-control-lifecycle.md`](00-doctrine/nested-control-lifecycle.md)
5. [`00-doctrine/glossary.md`](00-doctrine/glossary.md)
6. [`01-patterns/project-control-architecture-and-viability-review.md`](01-patterns/project-control-architecture-and-viability-review.md)
7. [`01-patterns/thinking-system-review.md`](01-patterns/thinking-system-review.md)
8. [`02-ai-control-plane/`](02-ai-control-plane/)
9. [`03-reference-architectures/`](03-reference-architectures/)
10. [`04-failure-modes/`](04-failure-modes/)

## Repository Structure

- [`00-doctrine/`](00-doctrine/) — foundational concepts and terminology.
- [`01-patterns/`](01-patterns/) — project review, Judgment Node Boundary, delivery review, and reusable patterns.
- [`02-ai-control-plane/`](02-ai-control-plane/) — distributed capabilities:
  - [`00-actuators/`](02-ai-control-plane/00-actuators/)
  - [`01-constraints/`](02-ai-control-plane/01-constraints/)
  - [`02-sensors/`](02-ai-control-plane/02-sensors/)
  - [`03-controller/`](02-ai-control-plane/03-controller/)
- [`03-reference-architectures/`](03-reference-architectures/) — non-prescriptive applications.
- [`04-failure-modes/`](04-failure-modes/) — recurring loss-of-control mechanisms.
- [`content/research/`](content/research/) — research and framework traceability.
- [`content/history/`](content/history/) — chronology and preserved public context.
- [`content/raw/`](content/raw/) — source snapshots.

The AI Control Plane directory numbering is navigation only. It does not define an execution order or physical stack.

## What UA Is — and Is Not

UA is a shared architectural language, a project-to-runtime control lifecycle, a set of technical and socio-technical patterns, and an evolving tool-neutral specification.

UA is not an SDK, universal agent framework, prompt collection, single guardrail product, mandatory four-service topology, replacement SDLC, governance department, compliance certification, or claim that uncertainty can be eliminated.

## Status and contribution

The repository is an evolving open specification. Documents declare their own status and maturity. See [`SPECIFICATION.md`](SPECIFICATION.md).

For contribution guidance:

- [`CONTRIBUTING.md`](CONTRIBUTING.md)
- [`AGENTS.md`](AGENTS.md)
- [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md)
- [`content/research/review-process.md`](content/research/review-process.md)

Documentation is licensed under CC BY 4.0. Code, where present, is licensed under Apache 2.0.
