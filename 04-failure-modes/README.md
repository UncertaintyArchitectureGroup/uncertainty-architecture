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
**Role:** Recurring mechanisms through which control is lost in Thinking Systems

## Purpose

This module documents recurring ways in which systems containing model-mediated judgment lose structural, semantic, operational, economic, or organizational control.

Traditional software failures often arise from explicit logical defects. Thinking Systems also fail through probabilistic drift, boundary breaches, missing or ineffective Constraints, weak evidence, delayed feedback, unclear authority, and controls that exist on paper but cannot change runtime behavior.

## Defines

This module defines or develops a taxonomy of:

- structural and syntactic failures;
- semantic and outcome failures;
- constraint definition, realization, enforcement, and authority failures;
- runtime and feedback-loop failures;
- architectural boundary failures;
- governance and decision-authority failures;
- control-capacity and economic failures;
- anti-patterns that treat probabilistic behavior as deterministic code.

## Does not define

This module does not provide:

- an exhaustive catalogue of every possible incident;
- one universal severity model;
- a guarantee that a single Constraint or control eliminates a failure mode;
- mandatory implementation technology;
- post-mortems as normative requirements.

Individual examples are illustrative. Mitigation normally requires a combination of Constraints, Sensors, Controllers, Actuators, Human Authority, and operating procedures proportional to the system's consequences and context.

## Key concepts

- syntactic entropy;
- semantic entropy;
- probabilistic drift;
- missing, soft, stale, bypassed, conflicting, or unavailable Constraint;
- boundary breach;
- open-loop deployment;
- evidence failure;
- Controller or authority failure;
- Actuator or corrective-path failure;
- containment and recovery failure;
- control-capacity and economic non-viability.

## Relationships

- [`00-doctrine/control-loop-anatomy.md`](../00-doctrine/control-loop-anatomy.md) defines the four capability classes used to diagnose loss of control.
- [`00-doctrine/nested-control-lifecycle.md`](../00-doctrine/nested-control-lifecycle.md) defines the decision level to which invalidating evidence should return.
- [`01-patterns/`](../01-patterns/) contains reusable responses to recurring failure mechanisms.
- [`02-ai-control-plane/01-constraints/`](../02-ai-control-plane/01-constraints/) defines constraint source, realization, failure behavior, evidence, and authority.
- [`02-ai-control-plane/`](../02-ai-control-plane/) provides the capabilities used to bound, detect, interpret, and correct deviations.
- [`03-reference-architectures/`](../03-reference-architectures/) demonstrates how failure handling may be composed in concrete systems.
- [`SPECIFICATION.md`](../SPECIFICATION.md) defines the status and normative boundary of this taxonomy.

## Initial taxonomy

### 1. Syntactic entropy — the structure breaks

The model output violates a technical contract required by the surrounding system.

Illustrative examples:

- malformed structured output;
- incorrect field or value types;
- repetition or non-terminating behavior;
- context overflow or truncation;
- outputs that cannot be parsed, validated, or safely executed.

Typical controls include structural Constraints such as schemas, types, grammars, validation, bounded retries, deterministic parsing, execution limits, evidence about validation failures, and explicit fallback paths.

A schema prevents only violations it can express. Structural validity does not establish semantic correctness, authorized action, or acceptable business outcome.

### 2. Semantic entropy — the meaning breaks

The output is technically valid but functionally wrong, unsafe, misleading, or unsuitable for the operating context.

Illustrative examples:

- unsupported or false claims;
- tone or policy drift;
- unjustified refusal or over-restriction;
- ignored instructions or negative constraints;
- valid-looking actions that violate business intent;
- output inside a structural schema but outside the approved Requirement.

Typical controls include soft behavioral Constraints, context and authority boundaries, evaluations, golden scenarios, runtime outcome signals, policy checks, Human Authority, escalation, and Controller-authorized changes. No single semantic guardrail should be assumed complete.

### 3. Constraint failures — the operating boundary fails

#### Missing Constraint

A material state, action, authority, data, resource, environment, or Human Authority boundary is never defined.

The system may appear controlled locally while a consequential reachable path remains unrestricted.

#### Soft-as-hard substitution

A prompt, rubric, natural-language policy, or model preference is represented as if it guaranteed compliance with a hard invariant.

The system has influence but not enforcement.

#### Declared but unenforced Constraint

The project or delivery artifact records a boundary, but no credible realization, enforcement point, failure behavior, evidence, or owner exists.

This commonly occurs when policies are copied into review documents without being connected to architecture.

#### Constraint bypass

An alternate code path, tool, permission, endpoint, context source, deployment, or operator action avoids the intended enforcement mechanism.

Bypass may be deliberate, accidental, introduced by integration, or created by a later configuration change.

#### Fail-open by accident

The system continues operation after a schema service, policy engine, permission check, Human Authority path, or other enforcement dependency becomes unavailable, although no authorized fail-open decision exists.

#### Stale or mismatched Constraint

The active schema, policy, permission, prompt, model, context source, release, or deployment configuration does not correspond to the approved Requirement or inherited project version.

The system may be enforcing a boundary, but not the authorized boundary.

#### Conflicting or unsatisfiable Constraints

Two or more Constraints cannot be satisfied simultaneously, produce inconsistent decisions, or create a path in which no valid behavior or fallback remains.

The result may be hidden fallback, repeated retries, manual work accumulation, or silent relaxation.

#### Unauthorized Constraint change

A runtime Controller, operator, deployment process, framework, or vendor configuration changes a project or organizational boundary outside delegated authority.

Technical configurability is mistaken for decision authority.

#### Constraint enforcement unavailable or too slow

The mechanism exists but cannot respond within the required latency, scale, availability, or consequence window.

A theoretically correct boundary is operationally ineffective.

#### Constraint evidence failure

Activation state, violations, bypass attempts, overrides, false blocks, and degradation are not observable or do not reach a Controller able to act.

The organization assumes the boundary works because no evidence contradicts it.

#### Constraint-friction or capacity failure

False blocks, latency, review demand, fallback volume, or operating cost make the constrained system unusable or invalidate the project business case.

This is not merely a tuning issue when it changes the project-level viability assumption.

### 4. Sensor and evidence failures — the system cannot see

Illustrative mechanisms include:

- the metric does not observe the material consequence;
- evidence covers only favorable or non-representative scenarios;
- a violation occurs outside the logging boundary;
- evidence arrives after harm has propagated;
- model-assisted evaluation is uncalibrated or shares the same blind spot as the controlled model;
- control-health, constraint-version, or dependency-change evidence is missing;
- a dashboard displays signals that no decision process reviews;
- evidence is aggregated until critical subpopulation or correlated failures disappear.

Telemetry quantity does not compensate for decision-irrelevant evidence.

### 5. Controller and authority failures — the system cannot decide

Illustrative mechanisms include:

- no one owns interpretation or action;
- decision authority is unclear or unavailable;
- the Controller lacks the context needed to distinguish expected variance from a Requirement violation;
- automated Controller logic changes a higher-level boundary outside its mandate;
- Human Authority lacks time, competence, independence, capacity, or intervention power;
- escalation has no real recipient or response expectation;
- project-invalidating evidence is normalized as a local exception;
- organizational issues are trapped inside one project.

A workflow step, approval screen, dashboard, Prompt Registry, or committee is not a Controller merely because it appears in the process.

### 6. Actuator and corrective-path failures — the system cannot change

Illustrative mechanisms include:

- the named kill switch is unavailable, untested, or has no authorized operator;
- rollback cannot restore compatible state;
- fallback repeats the same uncertain path or depends on the same failing provider;
- the Controller can decide but cannot change permissions, routing, deployment, or model behavior;
- containment does not stop downstream side effects;
- compensation or remediation is impossible after harm;
- the Actuator executes too slowly for the consequence window;
- a partial Actuator failure leaves inconsistent state.

A button or API becomes an Actuator only when it provides a real and operable path from authorized decision to changed behavior.

### 7. Open-loop and feedback failures — the capabilities do not connect

Illustrative mechanisms include:

- evidence has no decision owner;
- the Controller has no Actuator;
- a Constraint has no Sensor or control-health evidence;
- an Actuator changes behavior without evidence of effect;
- runtime evidence is disconnected from the project and delivery versions under which the system operates;
- reauthorization triggers are undefined;
- feedback latency exceeds the rate of propagation;
- several locally valid loops create an uncontrolled end-to-end system.

A collection of tools does not become a control loop by accumulation.

### 8. Process and governance anti-patterns — the socio-technical system breaks

Illustrative examples:

- **Vibe-check release:** deployment based on a few favorable examples rather than risk- and Constraint-derived evidence;
- **Hidden behavior configuration:** prompts, policies, constraints, permissions, or model settings embedded without ownership or traceability;
- **Open-loop deployment:** operation without meaningful feedback or a mechanism for corrective action;
- **Perfect-prompt fallacy:** attempting to eliminate uncertainty through prompting instead of engineering hard boundaries, evidence, and recovery;
- **Constraint-as-prompt fallacy:** treating probabilistic instruction as deterministic enforcement;
- **Declared-but-unenforced governance:** recording a rule without realization, failure behavior, evidence, or authority;
- **Tool-name taxonomy:** classifying products as Controllers, Sensors, Constraints, or Actuators without identifying their actual functions;
- **Telemetry without authority:** collecting metrics without assigning who may intervene or change the system;
- **Runtime policy overreach:** allowing operational tuning to change project or organizational authorization;
- **Human-in-the-loop theatre:** nominal approval steps without adequate context, time, competence, independence, capacity, or real decision power;
- **Constraint accumulation:** adding overlapping guardrails and checks without resolving conflict, latency, ownership, and cost;
- **Exception normalization:** repeatedly bypassing the approved boundary until the exception becomes the actual system.

### 9. Economic and control-capacity failure — the control system is not viable

The system may be technically controllable but not sustainably operable.

Illustrative mechanisms include:

- Human Authority cannot absorb real volume;
- fallback capacity collapses during incidents;
- evaluation and constraint maintenance cost grows faster than value;
- false blocks erase the promised efficiency;
- required control latency violates the product need;
- incident and remediation burden invalidates the business case;
- vendor or model volatility forces continuous revalidation beyond available capacity;
- project authorization assumed capabilities that the organization does not actually possess.

When these findings invalidate project assumptions, the correct response is project reauthorization, narrowing, redesign, or No-Go rather than indefinite local workaround.

## Documents

Future failure-mode documents should identify whether they define a taxonomy entry, provide an informative incident example, or preserve a historical post-mortem. They should follow [`DOCUMENT-METADATA.md`](../DOCUMENT-METADATA.md).

A mature failure-mode document should identify:

- the affected lifecycle level;
- the failed Constraint, Sensor, Controller, Actuator, authority, or connection;
- observable signals and evidence limits;
- local containment and recovery;
- delivery reassessment, project reauthorization, or organizational review triggers;
- economic and capacity effects where material.

## Contribution

Operational failure reports and post-mortems are valuable inputs to this module. Contributions should distinguish observed evidence from interpretation, identify operating context and consequences, preserve active versions and constraint sources, and avoid presenting a single incident as a universal rule.
