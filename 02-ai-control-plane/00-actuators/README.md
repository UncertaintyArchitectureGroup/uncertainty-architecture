---
title: Actuator Capabilities
artifact_type: control-capability
status: draft-normative
maturity: active
module: control-plane
topics:
  - actuators
  - constraints
  - containment
  - ai-control-plane
tags:
  - ua/module/control-plane
  - ua/type/control-capability
  - ua/status/draft-normative
  - ua/topic/actuators
  - ua/topic/constraints
  - ua/topic/containment
---

# Actuator Capabilities

**Role:** Mechanisms that can materially shape, constrain, enable, disable, route, or stop model-mediated behavior.

## Purpose

Actuators provide the path from a controller decision to a real change in system behavior.

They may operate before, during, or after model invocation. An actuator is defined by its ability to affect the reachable behavior or operating conditions of the system, not by whether it is implemented as a prompt, service, policy, or human action.

## Includes

Possible actuator capabilities include:

- prompt and instruction configuration;
- context-selection and context-assembly policy;
- model selection and routing;
- permissions and bounded tool access;
- schemas and deterministic validation gates;
- rate, token, time, and execution limits;
- policy enforcement and action authorization;
- fallback, degraded mode, rollback, containment, and shutdown;
- human approval or intervention that can materially change the path.

## Does not imply

This capability does not imply that:

- every prompt must live outside application code;
- every actuator belongs in one centralized layer;
- one guardrail can contain every relevant failure mode;
- a soft instruction creates a hard invariant;
- changing model parameters alone provides system-level control.

The relationship between **actuators** and **constraints** remains an explicit taxonomy question. Some constraints are implemented through actuators; others define the operating boundary within which actuators may operate.

## Design expectations

A mature actuator description should identify:

1. which behavior or authority it can change;
2. which controller or decision right may invoke it;
3. its scope and deterministic guarantees, if any;
4. how its version and configuration remain traceable;
5. how failure, unavailability, or misuse is handled;
6. which sensors provide evidence about its effect.

## Relationships

- [`../README.md`](../README.md) defines the AI Control Plane capability model.
- [`../01-sensors/`](../01-sensors/) provides evidence about behavior and actuator effects.
- [`../02-controller/`](../02-controller/) provides the decision function that authorizes corrective action.
- [`../../00-doctrine/glossary.md`](../../00-doctrine/glossary.md) defines the current canonical vocabulary.