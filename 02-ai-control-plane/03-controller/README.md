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

**Role:** Interpret evidence relative to intended operating conditions and authorize or select corrective action.

## Purpose

The Controller closes the feedback loop by connecting Sensors to Actuators and authorized constraint changes through explicit decision rights.

A Controller may be implemented in software, assigned to a human role, or distributed across a socio-technical operating process. It should not be assumed to be another LLM, one centralized service, one workflow engine, or one management committee.

## Includes

Controller responsibilities may include:

- interpreting evidence and uncertainty;
- comparing observed behavior with the approved Requirement, Operating Envelope, constraints, and assumptions;
- deciding whether a constraint is active, effective, infeasible, degraded, or creating unacceptable friction;
- authorizing release, limitation, rollback, containment, compensation, or shutdown;
- deciding when evidence is insufficient;
- escalating cases to an authority with greater context or permission;
- changing evaluation, prompts, policies, models, tools, permissions, constraints, or workflows within delegated authority;
- preserving the rationale and traceability of material decisions.

## Constraint authority

A Controller must distinguish:

- constraints it may adjust during ordinary operation;
- constraints that require a delivery reassessment;
- project-level constraints that require project reauthorization;
- organizational constraints that require organizational review or an authorized exception.

A runtime Controller must not silently relax a hard project or organizational boundary merely because the technical mechanism is configurable.

## Does not imply

This capability does not imply that:

- one job title is mandatory;
- every decision should be automated;
- reviews must occur on one universal cadence;
- a fixed accuracy threshold is valid across contexts;
- collecting telemetry creates authority to intervene;
- a Prompt Registry, dashboard, kill-switch endpoint, or Human-in-the-Loop screen is a Controller by itself;
- human involvement is effective when the human lacks information, time, competence, independence, capacity, or real decision power.

## Responsibility model

A real implementation should assign responsibility for:

1. the intended outcomes and approved Requirement;
2. the applicable constraints and their authoritative sources;
3. evidence interpretation and calibration;
4. release and change authority;
5. incident, escalation, containment, and reauthorization decisions;
6. actuator ownership and execution;
7. traceability, learning, and reassessment.

Responsibilities may be bundled into existing roles. Titles such as Prompt Steward, Evaluation Owner, or AI Reliability Engineer are examples from earlier UA work, not mandatory organizational requirements.

## Control cadence

Control cadence should follow feedback latency, consequence, autonomy, reversibility, propagation, constraint failure behavior, and rate of operating change. Some decisions may be made per action, per release, after an incident, or through periodic review. UA does not prescribe a universal weekly ritual.

## Relationships

- [`../README.md`](../README.md) defines the AI Control Plane capability model.
- [`../00-actuators/`](../00-actuators/) provides mechanisms capable of changing behavior.
- [`../01-constraints/`](../01-constraints/) defines and realizes the allowed operating space.
- [`../02-sensors/`](../02-sensors/) provides evidence about behavior, constraints, and operating conditions.
- [`../../00-doctrine/control-loop-anatomy.md`](../../00-doctrine/control-loop-anatomy.md) defines the capability relationships.
- [`../../00-doctrine/glossary.md`](../../00-doctrine/glossary.md) defines Controller, Escalation, Human Authority, Release Gate, Rollback, and related terms.
