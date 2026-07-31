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

**Role:** Mechanisms that execute an authorized change in system behavior or operating conditions.

## Purpose

Actuators provide the path from a Controller decision to a real change in the Thinking System, its environment, its deployment boundary, its Constraint Realizations, or its socio-technical operating process.

They may operate before, during, or after model invocation. An Actuator is defined by its ability to materially affect operation, not by whether it is implemented as an API, workflow engine, feature flag, prompt change, service, deployment step, or human action.

## Includes

Possible Actuator capabilities include:

- changing prompt, instruction, model, policy, context, routing, or tool configuration;
- installing, tightening, relaxing, replacing, or removing a Constraint Realization within delegated authority;
- narrowing deployment scope, population, geography, data, authority, or exposure;
- requiring Human Authority or switching to a manual path;
- enabling or disabling a feature, tool, model, or workflow;
- applying fallback or degraded mode;
- rolling back a model, prompt, policy, configuration, tool, realization, or release;
- containing or isolating a failing path;
- correcting downstream state or compensating affected parties;
- pausing or shutting down operation.

## Constraint boundary

Constraints, Constraint Realizations, and Actuators have different functions.

- A **Constraint** defines the approved operating boundary.
- A **Constraint Realization** implements, enforces, or influences that boundary for a defined scope.
- An **Actuator** executes an authorized change in operation.

An Actuator may change a Constraint Realization. A Constraint Realization may reject or block an attempted action. The same component may perform both implementation and actuation functions, but the functions should remain explicit.

Examples:

- approved tool access is an authority Constraint;
- a tool allowlist is one Constraint Realization;
- a configuration deployment removing a tool from the allowlist is an Actuator action;
- required output structure is a structural Constraint;
- a schema validator is a Constraint Realization;
- activating a new schema version is an Actuator action;
- a feature flag is an Actuator when it enables or disables a path;
- the policy determining who may use the path is a Constraint source or Requirement condition.

## Controller boundary

A Controller selects or authorizes an action. An Actuator executes it.

One service or human workflow may contain both functions, but the distinction should remain visible so decision rights, execution rights, latency, failure behavior, and evidence can be reviewed independently.

## Does not imply

This capability does not imply that:

- every prompt must live outside application code;
- every Actuator belongs in one centralized layer;
- every API call or workflow step is a control Actuator;
- one guardrail can contain every failure mode;
- a soft instruction creates a Hard Constraint;
- changing model parameters alone provides system-level control;
- technical configurability creates authority to change project or organizational boundaries.

## Design expectations

A mature Actuator description should identify:

1. the operation or Constraint Realization it can change;
2. which Controller or decision right may invoke it;
3. the authorized scope of the change;
4. which higher-level boundaries it must not alter;
5. how version and configuration remain traceable;
6. how failure, unavailability, misuse, or partial execution is handled;
7. which Sensors provide execution and effect evidence;
8. whether confirmation, rollback, compensation, or escalation is required.

## Relationships

- [`../README.md`](../README.md) defines the AI Control Plane capability model.
- [`../01-constraints/`](../01-constraints/) defines Constraints and Constraint Realizations.
- [`../02-sensors/`](../02-sensors/) provides evidence about behavior, execution, and effects.
- [`../03-controller/`](../03-controller/) provides the decision function selecting or authorizing action.
- [`../../00-doctrine/control-loop-anatomy.md`](../../00-doctrine/control-loop-anatomy.md) defines capability relationships.
- [`../../00-doctrine/glossary.md`](../../00-doctrine/glossary.md) owns canonical terminology.
