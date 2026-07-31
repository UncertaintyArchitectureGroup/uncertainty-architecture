---
title: Controller and Decision Authority
artifact_type: control-capability
status: draft-normative
maturity: active
module: control-plane
topics:
  - controller
  - constraints
  - human-authority
  - escalation
  - rollback
  - control-loop
tags:
  - ua/module/control-plane
  - ua/type/control-capability
  - ua/status/draft-normative
  - ua/topic/controller
  - ua/topic/constraints
  - ua/topic/human-authority
  - ua/topic/escalation
  - ua/topic/rollback
---

# Controller and Decision Authority

**Role:** Compare or interpret evidence relative to intended operating conditions, then select or authorize corrective action.

## Purpose

The Controller connects Sensors and evidence to authorized decisions. The Actuator executes those decisions.

A Controller may be implemented in software, assigned to a human, or distributed across a socio-technical operating process. It should not be assumed to be another LLM, one centralized service, one workflow engine, or one management committee.

## Includes

Controller responsibilities may include:

- receiving the approved Requirement, Operating Envelope, Constraints, assumptions, and other reference conditions;
- interpreting evidence and its uncertainty;
- comparing observed behavior with intended operating conditions;
- deciding whether a Constraint Realization is active, effective, infeasible, degraded, bypassed, or creating unacceptable friction;
- selecting or authorizing release, limitation, rollback, containment, compensation, or shutdown;
- selecting or authorizing changes to evaluations, prompts, policies, models, tools, permissions, Constraint Realizations, or workflows within delegated authority;
- deciding when evidence is insufficient;
- escalating cases to an authority with greater context or permission;
- preserving the rationale and traceability of material decisions.

The Controller does not perform execution merely because the same service, workflow, or person contains both decision and execution functions. Analysis should still identify the decision right and the Actuator path separately.

## Constraint authority

A Controller must distinguish:

- Constraint Realization changes it may authorize during ordinary operation;
- changes requiring delivery reassessment;
- project-level Constraint or authorization changes requiring project reauthorization;
- organizational Constraint changes requiring organizational review or an authorized exception.

A runtime Controller must not silently authorize relaxation of a Hard Constraint or higher-level boundary merely because the technical mechanism is configurable.

Technical configurability does not create decision authority.

## Reference signal and evidence

A Controller requires both:

1. **reference conditions** — the Requirement, Constraints, operating assumptions, decision boundary, and accepted residual risk;
2. **evidence** — observed behavior, outcomes, realization state, Actuator execution, incidents, operating conditions, and control health.

Evidence without reference conditions cannot determine whether deviation is material. Reference conditions without evidence cannot support runtime control.

## Does not imply

This capability does not imply that:

- one job title is mandatory;
- every decision should be automated;
- reviews must occur on one universal cadence;
- a fixed threshold is valid across contexts;
- collecting telemetry creates authority to intervene;
- a Prompt Registry, dashboard, evaluation service, kill-switch endpoint, or HITL screen is a Controller by itself;
- human involvement is effective when the person lacks information, time, competence, independence, capacity, or real decision power.

## Evaluator, gate, and action boundary

```text
Evaluation runner and metrics
→ Sensor and evidence

Logic selecting block / canary / release
→ Controller function

Deployment, exposure change, rollback, or block execution
→ Actuator function
```

One product may package all three functions. The package name does not remove their different authority and failure responsibilities.

## Responsibility model

A real implementation should assign responsibility for:

1. approved outcomes and Requirements;
2. applicable Constraints and their sources;
3. evidence interpretation and calibration;
4. release and change authority;
5. incident, escalation, containment, and reauthorization decisions;
6. Actuator ownership and execution;
7. traceability, learning, and reassessment.

Responsibilities may be bundled into existing roles. UA does not prescribe mandatory job titles.

## Control cadence

Control cadence should follow feedback latency, consequence, autonomy, reversibility, propagation, Constraint failure behavior, and rate of operating change. Decisions may occur per action, per release, after an incident, or through periodic review. UA does not prescribe one universal ritual.

## Relationships

- [`../README.md`](../README.md) defines the AI Control Plane capability model.
- [`../00-actuators/`](../00-actuators/) defines execution of authorized change.
- [`../01-constraints/`](../01-constraints/) defines Constraints and Constraint Realization.
- [`../02-sensors/`](../02-sensors/) defines evidence capabilities.
- [`../../00-doctrine/control-loop-anatomy.md`](../../00-doctrine/control-loop-anatomy.md) defines capability relationships.
- [`../../00-doctrine/glossary.md`](../../00-doctrine/glossary.md) owns canonical terminology.
