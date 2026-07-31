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

**Role:** Mechanisms that produce evidence about model-mediated behavior, system outcomes, operating conditions, constraint state, and control performance.

## Purpose

Sensors make relevant change and deviation observable enough for a Controller to decide whether intervention is required.

UA does not assume a universal `getBusinessTruth()` function. Evidence may be incomplete, delayed, probabilistic, qualitative, or contested. The engineering problem is to assemble signals that are fit for the decision and explicit about their limits.

Sensors also provide evidence about Constraints themselves: whether enforcement is active, which violations or bypass attempts occurred, whether false blocks or operational friction are material, and whether the constraint mechanism is degraded or unavailable.

## Includes

Possible sensor capabilities include:

- deterministic contract and schema checks;
- constraint-enforcement health and violation evidence;
- representative scenarios and regression sets;
- statistical sampling and outcome metrics;
- model-assisted evaluation with calibration and limitations;
- expert or user review;
- incidents, complaints, overrides, and near misses;
- latency, cost, availability, capacity, and tool-execution signals;
- changes in models, prompts, context, data, permissions, constraints, or operating conditions;
- audit and traceability records.

## Does not imply

This capability does not imply that:

- one metric is equivalent to business truth;
- a golden set contains one universally ideal answer;
- a fixed sample size is valid across use cases;
- an LLM judge is appropriate as final authority for every decision;
- a constraint violation signal is automatically a complete diagnosis;
- telemetry alone closes the control loop.

## Design expectations

A mature sensor description should identify:

1. the decision it is intended to support;
2. the behavior, outcome, constraint, or condition it observes;
3. its coverage, uncertainty, latency, and known blind spots;
4. how it is calibrated and reviewed;
5. how evidence remains traceable;
6. which Controller receives it and what action may follow;
7. which higher-level assumption may be invalidated by the evidence.

## Relationships

- [`../README.md`](../README.md) defines the AI Control Plane capability model.
- [`../00-actuators/`](../00-actuators/) contains mechanisms capable of changing behavior.
- [`../01-constraints/`](../01-constraints/) defines the allowed operating space and its enforcement.
- [`../03-controller/`](../03-controller/) interprets evidence and authorizes corrective action.
- [`../../00-doctrine/control-loop-anatomy.md`](../../00-doctrine/control-loop-anatomy.md) defines the capability relationships.
- [`../../00-doctrine/glossary.md`](../../00-doctrine/glossary.md) defines Sensor, Evidence, Evaluation, Drift, and related terms.
