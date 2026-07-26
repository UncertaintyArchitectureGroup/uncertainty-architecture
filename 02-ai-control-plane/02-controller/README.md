---
title: Controller and Decision Authority
artifact_type: control-capability
status: draft-normative
maturity: active
module: control-plane
topics:
  - controller
  - human-authority
  - escalation
  - rollback
  - control-loop
tags:
  - ua/module/control-plane
  - ua/type/control-capability
  - ua/status/draft-normative
  - ua/topic/controller
  - ua/topic/human-authority
  - ua/topic/escalation
  - ua/topic/rollback
---

# Controller and Decision Authority

**Role:** Interpret evidence relative to intended operating conditions and authorize or select corrective action.

## Purpose

The controller closes the feedback loop by connecting sensors to actuators through explicit decision rights.

A controller may be implemented in software, assigned to a human role, or distributed across a socio-technical operating process. It should not be assumed to be another LLM, one centralized service, or one management committee.

## Includes

Controller responsibilities may include:

- interpreting evidence and uncertainty;
- comparing observed behavior with an intended operating envelope;
- authorizing release, limitation, rollback, containment, or shutdown;
- deciding when evidence is insufficient;
- escalating cases to an authority with greater context or permission;
- changing evaluation, prompts, policies, models, tools, permissions, or workflows;
- preserving the rationale and traceability of material decisions.

## Does not imply

This capability does not imply that:

- one job title is mandatory;
- every decision should be automated;
- reviews must occur on one universal cadence;
- a fixed accuracy threshold is valid across contexts;
- collecting telemetry creates authority to intervene;
- human involvement is effective when the human lacks information, time, competence, or real decision power.

## Responsibility model

A real implementation should assign responsibility for:

1. the intended outcomes and acceptable operating envelope;
2. evidence interpretation and calibration;
3. release and change authority;
4. incident, escalation, and containment decisions;
5. actuator ownership and execution;
6. traceability, learning, and reassessment.

Responsibilities may be bundled into existing roles. Titles such as Prompt Steward, Evaluation Owner, or AI Reliability Engineer are examples from earlier UA work, not mandatory organizational requirements.

## Control cadence

Control cadence should follow feedback latency, consequence, autonomy, reversibility, and rate of operating change. Some decisions may be made per action, per release, after an incident, or through periodic review. UA does not prescribe a universal weekly ritual.

## Relationships

- [`../README.md`](../README.md) defines the AI Control Plane capability model.
- [`../00-actuators/`](../00-actuators/) provides mechanisms capable of changing behavior.
- [`../01-sensors/`](../01-sensors/) provides evidence about behavior and operating conditions.
- [`../../00-doctrine/glossary.md`](../../00-doctrine/glossary.md) defines controller, escalation, human authority, release gate, rollback, and related terms.