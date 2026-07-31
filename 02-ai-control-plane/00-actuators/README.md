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

Actuators provide the path from a Controller decision to a real change in the Thinking System, its environment, its deployment boundary, or its socio-technical operating process.

They may operate before, during, or after model invocation. An actuator is defined by its ability to materially affect behavior or operating conditions, not by whether it is implemented as an API, workflow engine, feature flag, prompt change, service, or human action.

## Includes

Possible actuator capabilities include:

- changing prompt, instruction, model, policy, context, routing, or tool configuration;
- installing, tightening, relaxing, switching, or removing a constraint within delegated authority;
- narrowing deployment scope, population, geography, data, authority, or exposure;
- requiring Human Authority or switching to a manual path;
- enabling or disabling a feature, tool, model, or workflow;
- applying fallback or degraded mode;
- rolling back a model, prompt, policy, configuration, tool, or release;
- containing or isolating a failing path;
- correcting downstream state or compensating affected parties;
- pausing or shutting down operation.

## Constraint boundary

Actuators and Constraints are separate capability classes.

- A **Constraint** defines or enforces the allowed operating space.
- An **Actuator** executes an authorized change in behavior or operating conditions.

An actuator may modify a constraint. A constraint may block an attempted action. The same component may implement both functions, but the functions should remain explicit.

Examples:

- a tool allowlist is an authority Constraint;
- a configuration change that removes a tool from the allowlist is an Actuator action;
- a schema is a structural Constraint;
- a deployment that activates a new schema version is an Actuator action;
- a feature flag is an Actuator when it enables or disables a path;
- the policy defining who may use that feature is a Constraint.

## Does not imply

This capability does not imply that:

- every prompt must live outside application code;
- every actuator belongs in one centralized layer;
- every API call or workflow step is a control actuator;
- one guardrail can contain every relevant failure mode;
- a soft instruction creates a hard invariant;
- changing model parameters alone provides system-level control;
- technical configurability creates authority to change project or organizational constraints.

## Design expectations

A mature actuator description should identify:

1. which behavior, operating condition, or constraint it can change;
2. which Controller or decision right may invoke it;
3. the scope of the change;
4. which higher-level boundaries it must not alter;
5. how its version and configuration remain traceable;
6. how failure, unavailability, misuse, or partial execution is handled;
7. which Sensors provide evidence about its execution and effect;
8. whether rollback, compensation, or confirmation is required.

## Relationships

- [`../README.md`](../README.md) defines the AI Control Plane capability model.
- [`../01-constraints/`](../01-constraints/) defines the operating boundaries within which actuators operate.
- [`../02-sensors/`](../02-sensors/) provides evidence about behavior, actuator execution, and effects.
- [`../03-controller/`](../03-controller/) provides the decision function that authorizes corrective action.
- [`../../00-doctrine/control-loop-anatomy.md`](../../00-doctrine/control-loop-anatomy.md) defines the capability relationships.
- [`../../00-doctrine/glossary.md`](../../00-doctrine/glossary.md) defines the current canonical vocabulary.
