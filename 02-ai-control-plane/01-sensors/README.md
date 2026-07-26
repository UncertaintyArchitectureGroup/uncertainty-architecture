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

**Role:** Mechanisms that produce evidence about model-mediated behavior, system outcomes, operating conditions, and control performance.

## Purpose

Sensors make relevant change and deviation observable enough for a controller to decide whether intervention is required.

UA does not assume a universal `getBusinessTruth()` function. Evidence may be incomplete, delayed, probabilistic, qualitative, or contested. The engineering problem is to assemble signals that are fit for the decision and explicit about their limits.

## Includes

Possible sensor capabilities include:

- deterministic contract and schema checks;
- representative scenarios and regression sets;
- statistical sampling and outcome metrics;
- model-assisted evaluation with calibration and limitations;
- expert or user review;
- incidents, complaints, overrides, and near misses;
- latency, cost, availability, and tool-execution signals;
- changes in models, prompts, context, data, permissions, or operating conditions;
- audit and traceability records.

## Does not imply

This capability does not imply that:

- one metric is equivalent to business truth;
- a golden set contains one universally ideal answer;
- a fixed sample size is valid across use cases;
- an LLM judge is appropriate as final authority for every decision;
- telemetry alone closes the control loop.

## Design expectations

A mature sensor description should identify:

1. the decision it is intended to support;
2. the behavior, outcome, or condition it observes;
3. its coverage, uncertainty, latency, and known blind spots;
4. how it is calibrated and reviewed;
5. how evidence remains traceable;
6. which controller receives it and what action may follow.

## Relationships

- [`../README.md`](../README.md) defines the AI Control Plane capability model.
- [`../00-actuators/`](../00-actuators/) contains mechanisms capable of changing behavior.
- [`../02-controller/`](../02-controller/) interprets evidence and authorizes corrective action.
- [`../../00-doctrine/glossary.md`](../../00-doctrine/glossary.md) defines sensor, evidence, evaluation, drift, and related terms.