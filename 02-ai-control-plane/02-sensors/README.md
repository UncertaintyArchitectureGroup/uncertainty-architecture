---
title: Sensor and Evidence Capabilities
artifact_type: control-capability
status: draft-normative
maturity: active
module: control-plane
topics:
  - sensors
  - evidence
  - evaluation
  - drift
  - constraints
  - ai-control-plane
tags:
  - ua/module/control-plane
  - ua/type/control-capability
  - ua/status/draft-normative
  - ua/topic/sensors
  - ua/topic/evidence
  - ua/topic/evaluation
  - ua/topic/drift
---

# Sensor and Evidence Capabilities

**Role:** Mechanisms that produce evidence about model-mediated behavior, system outcomes, operating conditions, Constraint Realization state, Actuator execution, and control performance.

## Purpose

Sensors make relevant behavior and change observable enough for a Controller to decide whether intervention is required.

UA does not assume a universal `getBusinessTruth()` function. Evidence may be incomplete, delayed, probabilistic, qualitative, or contested. The engineering problem is to assemble signals fit for the bounded decision and explicit about their limits.

Sensors also provide evidence about control mechanisms themselves:

- whether a Constraint Realization is active;
- which violations, bypass attempts, or overrides occurred;
- whether false blocks or operational friction are material;
- whether enforcement is degraded or unavailable;
- whether an Actuator executed and produced the intended state change.

## Includes

Possible Sensor capabilities include:

- deterministic contract, permission, state, and schema checks;
- Constraint Realization health and violation evidence;
- representative scenarios, Golden Scenarios, and regression sets;
- statistical sampling and outcome metrics;
- model-assisted evaluation with calibration and limitations;
- expert, operator, or user review;
- incidents, complaints, overrides, and near misses;
- latency, cost, availability, capacity, fallback-load, and tool-execution signals;
- changes in models, prompts, context, data, permissions, Constraint sources or realizations, dependencies, and operating conditions;
- Actuator execution and resulting-state evidence;
- audit and traceability records.

## Evaluator, gate, and action boundary

An evaluation system may package several capability functions. Preserve them analytically:

```text
Evaluation runner, metrics, and evidence
→ Sensor function

Logic comparing evidence with a threshold or policy
and selecting block / canary / release
→ Controller function

Deployment, exposure change, block, or rollback execution
→ Actuator function
```

Calling the package an `Eval Gate` does not make all of it a Sensor.

## Does not imply

This capability does not imply that:

- one metric is equivalent to business truth;
- a Golden Scenario set contains one universally ideal answer;
- a fixed sample size is valid across use cases;
- an LLM judge is appropriate as final authority for every decision;
- a violation signal is automatically a complete diagnosis;
- telemetry alone closes the control loop;
- evidence alone creates authority to intervene;
- a probabilistic detector creates a Hard Constraint.

## Design expectations

A mature Sensor description should identify:

1. the decision it is intended to support;
2. the behavior, outcome, realization, action, or condition it observes;
3. its coverage, uncertainty, latency, and known blind spots;
4. how it is calibrated and reviewed;
5. how evidence remains traceable to active versions and scope;
6. which Controller receives it;
7. which action or escalation may follow;
8. which project or organizational assumption may be invalidated.

## Relationships

- [`../README.md`](../README.md) defines the AI Control Plane capability model.
- [`../00-actuators/`](../00-actuators/) defines mechanisms executing authorized change.
- [`../01-constraints/`](../01-constraints/) defines approved Constraints and their realizations.
- [`../03-controller/`](../03-controller/) interprets evidence and selects or authorizes action.
- [`../../00-doctrine/control-loop-anatomy.md`](../../00-doctrine/control-loop-anatomy.md) defines the capability relationships.
- [`../../00-doctrine/glossary.md`](../../00-doctrine/glossary.md) owns canonical terminology.
