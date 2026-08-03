---
title: Failure Modes and Anti-Patterns
artifact_type: failure-mode-index
status: draft-normative
maturity: active
module: failure-modes
topics:
  - drift
  - constraints
  - containment
  - evidence
  - controller
  - human-authority
tags:
  - ua/module/failure-modes
  - ua/type/failure-mode-index
  - ua/status/draft-normative
  - ua/topic/drift
  - ua/topic/constraints
  - ua/topic/containment
  - ua/topic/evidence
  - ua/topic/controller
canonical_for:
  - failure-modes-module
---

# Failure Modes and Anti-Patterns

**Status:** Draft normative taxonomy; examples are informative  
**Role:** Recurring mechanisms through which control is lost or becomes ineffective in Thinking Systems

## Purpose

Thinking Systems can fail through deterministic defects, probabilistic behavior, invalid Requirements, missing or ineffective Constraints, weak evidence, delayed feedback, unclear authority, unavailable Actuators, inadequate capacity, and controls that exist on paper but cannot change operation.

This module classifies reusable mechanisms rather than every undesirable output or incident.

## Boundaries

This module does not provide:

- an exhaustive incident catalogue;
- one universal severity model;
- a guarantee that one control eliminates a failure mode;
- mandatory implementation technology;
- post-mortems as normative requirements.

Mitigation normally combines approved Constraints, credible Constraint Realizations, Sensors, Controllers, Actuators, Human Authority, and operating procedures proportional to context and consequence.

## Initial taxonomy

### 1. Structural failure

The system violates a technical contract required by surrounding deterministic software.

Examples include malformed output, incorrect types, invalid states, context overflow, repetition, non-termination, or data that cannot be safely parsed or executed.

Typical responses include structural Constraints realized through schemas, types, grammars, deterministic validation, bounded retries, execution limits, evidence, and fallback.

Structural validity does not establish semantic correctness, authorized action, or an acceptable business outcome.

### 2. Semantic or outcome failure

The output is technically valid but wrong, unsafe, misleading, or unsuitable for the Requirement.

Examples include unsupported claims, policy drift, unjustified refusal, business-intent violation, data disclosure, or structurally valid but harmful action proposals.

Possible responses include Soft Constraints, approved context and authority boundaries, semantic and outcome Sensors, Human Authority, escalation, and Controller-authorized corrective action. No semantic guardrail should be assumed complete by default.

### 3. Constraint-definition failure

#### Missing Constraint

A material state, action, authority, data, resource, environment, deployment, or Human Authority boundary is never approved or made explicit.

#### Soft-as-hard substitution

A prompt, rubric, natural-language policy, probabilistic evaluator, classifier, or model preference is represented as a deterministic guarantee.

#### Invalid Hard Constraint claim

A Constraint is called hard even though its complete realized path does not deterministically prevent or reject violation within stated assumptions, subject, path, scope, and enforcement boundaries.

#### Mixed-strength Constraint record

One record combines different subjects, paths, or scopes whose realized guarantees are not the same, then labels the whole record `Hard`, `Soft`, or `Hard/Soft`.

This obscures which outcome is actually unreachable, which part only influences behavior, which evidence applies, and which authority may change the boundary. The result can overstate a guarantee or make verification and incident diagnosis impossible.

The response is to split the condition into separately scoped Constraint claims, each with its own realization, assumptions, evidence, and reassessment trigger.

#### Constraint–realization collapse

The approved boundary, implementation mechanism, active configuration, evidence, decision authority, and change action are treated as one undifferentiated object.

This hides which part failed and which authority may change it.

#### Conflicting or unsatisfiable Constraints

Constraints cannot be satisfied simultaneously, create inconsistent decisions, or leave no valid behavior or fallback.

### 4. Constraint Realization failure

#### Declared but unrealized

A boundary exists in policy or review material, but no credible realization, failure behavior, evidence, or owner exists.

#### Realization bypass

An alternate code path, endpoint, tool, permission, context source, deployment, or operator action avoids the intended mechanism.

#### Fail-open by accident

Operation continues after a realization dependency becomes unavailable without an explicit authorized decision.

#### Stale or mismatched realization

The active schema, permission, policy, prompt, model, context source, deployment, or configuration does not correspond to the approved Constraint and project baseline.

#### Realization unavailable or too slow

The mechanism exists but cannot respond within required latency, availability, scale, or consequence window.

#### Realization evidence failure

Activation, version, violations, bypass attempts, overrides, false blocks, degradation, and coverage cannot be observed or do not reach an authorized Controller.

#### Realization friction or capacity failure

False blocks, latency, review load, fallback volume, or cost make the design unusable or invalidate project viability.

### 5. Sensor and evidence failure

Examples include:

- the metric does not observe the material consequence;
- evidence covers only favorable or non-representative cases;
- violation occurs outside the observation boundary;
- evidence arrives after harm propagates;
- model-assisted evaluation is uncalibrated or shares the controlled model's blind spot;
- realization-version, control-health, dependency-change, or Actuator-execution evidence is missing;
- dashboards have no decision owner;
- aggregation hides critical subpopulation or correlated failure.

Telemetry volume does not compensate for decision-irrelevant evidence.

### 6. Controller and authority failure

Examples include:

- no one owns evidence interpretation or decision;
- reference conditions are missing or ambiguous;
- decision authority is unclear, unavailable, or too slow;
- a Controller authorizes a change outside delegated authority;
- Human Authority lacks information, competence, time, independence, capacity, or intervention power;
- escalation has no real recipient or response path;
- project-invalidating evidence is normalized as a local exception;
- organizational issues remain trapped inside one project.

A workflow, approval screen, dashboard, Prompt Registry, or committee is not a Controller merely because it exists.

### 7. Actuator and execution failure

Examples include:

- a kill switch is unavailable, untested, or has no authorized operator;
- rollback cannot restore compatible state;
- fallback repeats the same uncertain path or shares the failing dependency;
- a Controller can decide but no Actuator can execute the decision;
- containment does not stop downstream effects;
- compensation is unavailable after harm;
- execution is too slow for the consequence window;
- partial execution leaves inconsistent state;
- an Actuator changes a Constraint Realization outside authorized scope.

A button, API, workflow, or human action becomes an Actuator only when it provides a real path from an authorized decision to changed operation.

### 8. Feedback and connection failure

#### Open-loop operation

Behavior is released without meaningful evidence connected to decision authority and effective actuation.

#### Closed-loop but unbounded operation

Sensors, Controller, and Actuators form a feedback path, but approved Constraints or credible realizations are missing. The loop may remain closed while unsafe, over-authorized, or economically unacceptable.

#### Disconnected capability path

Examples include:

- evidence with no Controller;
- Controller with no effective Actuator;
- realization with no health evidence;
- Actuator execution with no evidence of effect;
- runtime evidence disconnected from active project and delivery versions;
- undefined reassessment triggers;
- feedback latency exceeding propagation speed;
- locally valid loops forming an uncontrolled end-to-end system.

A collection of tools does not become a control architecture by accumulation.

### 9. Process and governance anti-patterns

- **Vibe-check release** — deployment based on a few favorable outputs rather than decision-relevant evidence.
- **Constraint-as-prompt fallacy** — probabilistic instruction presented as deterministic enforcement.
- **Declared-but-unrealized governance** — rule without realization, evidence, failure behavior, or authority.
- **Mixed-strength record** — different guarantee strengths collapsed into one Constraint row.
- **Tool-name taxonomy** — classifying products by marketing category rather than function.
- **Telemetry without authority** — observation without a decision owner or Actuator path.
- **Runtime authority overreach** — local authorization or execution changing a higher-level boundary.
- **Human-in-the-loop theatre** — nominal human involvement without substantive authority and capacity.
- **Constraint accumulation** — overlapping checks without conflict, latency, ownership, or cost analysis.
- **Exception normalization** — repeated bypass until the exception becomes the operating system.
- **Duplicate-control records** — the same Constraint redefined inconsistently across project, delivery, release, and runtime artifacts.

### 10. Economic and capacity failure

The architecture may be technically possible but not sustainably operable.

Examples include:

- Human Authority cannot absorb real volume;
- fallback capacity collapses during incidents;
- realization and evaluation maintenance cost grows faster than value;
- false blocks erase promised efficiency;
- required latency violates product need;
- incident and compensation burden invalidates economics;
- vendor volatility forces revalidation beyond available capacity;
- authorization assumes capabilities the organization does not possess.

When these findings invalidate project assumptions, the response is project reauthorization, narrowing, redesign, or No-Go rather than indefinite local workaround.

## Failure-mode document expectations

A mature failure-mode document should identify:

- affected decision level;
- failed Constraint, realization, Sensor, Controller, Actuator, Human Authority, or connection;
- triggering conditions and mechanism;
- observable signals and evidence limits;
- consequences and propagation;
- containment, recovery, and compensation;
- delivery reassessment, project reauthorization, or organizational review triggers;
- capacity and economic effects where material.

## Relationships

- [`00-doctrine/control-loop-anatomy.md`](../00-doctrine/control-loop-anatomy.md) defines capability relationships.
- [`00-doctrine/nested-control-lifecycle.md`](../00-doctrine/nested-control-lifecycle.md) defines decision ownership and reassessment.
- [`01-patterns/`](../01-patterns/) contains reusable responses.
- [`02-ai-control-plane/01-constraints/`](../02-ai-control-plane/01-constraints/) defines Constraints and Constraint Realization.
- [`02-ai-control-plane/`](../02-ai-control-plane/) develops the four capability families.
- [`03-reference-architectures/`](../03-reference-architectures/) demonstrates possible compositions.
- [`SPECIFICATION.md`](../SPECIFICATION.md) defines status and conformance.
