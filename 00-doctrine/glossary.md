---
title: Uncertainty Architecture Glossary
artifact_type: glossary
status: draft-normative
maturity: active
module: doctrine
topics:
  - thinking-systems
  - deterministic-core
  - model-judgment
  - uncertainty-boundary
  - ai-control-plane
  - control-loop
tags:
  - ua/module/doctrine
  - ua/type/glossary
  - ua/status/draft-normative
  - ua/topic/thinking-systems
  - ua/topic/uncertainty-boundary
  - ua/topic/ai-control-plane
canonical_for:
  - doctrine-vocabulary
---

# Uncertainty Architecture Glossary

## Status and use

This glossary defines the current canonical meaning of core Uncertainty Architecture (UA) terms where an entry exists.

The glossary is **draft normative**. Definitions may be refined through research synthesis and framework review. Historical publications retain their original wording even when a term has since been renamed, narrowed, or superseded.

A term appearing in a research source, talk, example, or external framework does not automatically acquire the UA meaning defined here unless the document explicitly uses it in the UA sense.

## System categories

### Thinking System

A software system whose runtime behavior depends partly on probabilistic model judgment while consequential deterministic boundaries, invariants, decision rights, and corrective mechanisms remain explicit.

**Thinking Systems** is the current UA category. Earlier UA publications used **Behavioral Software** and **Behavioral Applications**; those names are historical predecessors, not current synonyms for new framework material.

Agentic systems are a higher-autonomy subset of Thinking Systems rather than the whole category.

### Linear Software

Software whose relevant execution paths and decision rules are explicitly encoded and intended to produce predictable behavior under defined conditions.

Linear Software may still contain operational uncertainty, concurrency, external dependencies, statistical components, or defects. The term distinguishes explicitly encoded control paths from runtime judgment delegated to probabilistic models; it does not claim that classical software is perfectly simple or failure-free.

## Boundary and responsibility

### Deterministic Core

The rules, invariants, permissions, data handling, transaction boundaries, audit requirements, and other responsibilities that must remain explicitly controlled and testable regardless of model behavior.

The Deterministic Core is a responsibility boundary, not necessarily one physical component or service.

### Model Judgment

Interpretation, synthesis, classification, generation, planning, ranking, or action selection performed through a probabilistic model under uncertainty.

Model Judgment may produce useful adaptation and semantic reasoning, but it must not be treated as equivalent to a guaranteed business rule.

### Judgment Node

A bounded location in a system or workflow where Model Judgment influences an output, decision, path, or action.

A Judgment Node should make its inputs, allowed authority, deterministic boundaries, evidence, and failure handling visible enough to review and operate.

### Uncertainty Boundary

The interface at which deterministic system responsibilities meet Model Judgment.

The boundary includes more than an API call. It may include context assembly, permissions, schemas, policy checks, tool access, validation, evidence collection, fallback, and escalation responsibilities.

### Invariant

A condition that must remain true across relevant system states or transitions.

An invariant should be enforced through deterministic mechanisms when violation would create unacceptable consequences. A probabilistic instruction is not by itself an invariant.

### Constraint

A condition intended to limit behavior or reduce the reachable operating space.

A **hard constraint** is enforced deterministically or through a mechanism with explicit failure behavior. A **soft constraint** influences probabilistic behavior but does not guarantee compliance.

## Control-loop vocabulary

### AI Control Plane

The distributed capability model used to constrain, observe, evaluate, and correct model-mediated behavior in a Thinking System.

The AI Control Plane is not necessarily a standalone service, platform, or centralized infrastructure layer. Its responsibilities may be distributed across application code, platform services, evaluation systems, release processes, human workflows, and governance mechanisms.

### Actuator

A mechanism capable of changing, constraining, enabling, disabling, routing, or otherwise shaping system behavior.

Examples may include prompts, context policies, model configuration, permissions, tool access, routing, deterministic gates, rate or execution limits, rollback, or shutdown mechanisms. The exact classification of constraints relative to actuators may be refined, but an actuator must have a real path to affect behavior.

### Sensor

A mechanism that produces evidence about outputs, outcomes, operating conditions, drift, incidents, or control performance.

A sensor does not need to produce a single objective truth value. It must produce information useful enough for a controller to make a bounded decision. Metrics, evaluations, human review, runtime signals, and incident reports may all act as sensors.

### Controller

The decision function that interprets evidence relative to intended outcomes and operating boundaries, then authorizes or selects corrective action.

A controller may be implemented in software, assigned to a human role, or distributed across a socio-technical operating process. Telemetry without decision authority and a mechanism for intervention does not form a functioning controller.

### Open-Loop System

A system that acts without meaningful feedback connected to corrective authority.

Logging alone does not close the loop when evidence cannot change, contain, roll back, escalate, or stop behavior.

### Closed-Loop System

A system in which observations are evaluated against intended operating conditions and can lead to authorized corrective action.

Closed-loop does not imply fully automated control. Human decision authority may be an essential part of the loop.

### Operating Envelope

The approved range of conditions, authority, consequences, resource use, and observed behavior within which a system is considered acceptable to operate under a defined Requirement.

For Model Judgment that performs business logic, the Operating Envelope may include permitted behavioral variation, prohibited regions, business tolerances for relevant outcome distributions, evidence expectations, cost or latency bounds, and required handling when acceptable bounds are exceeded or cannot be established.

The envelope should be derived from context and risk rather than copied as a universal threshold.

## Evidence and change

### Evidence

A recorded signal, observation, evaluation result, incident, outcome, or review artifact used to support a system decision.

Evidence has scope and limitations. A metric, benchmark, anecdote, or model-generated score is not automatically sufficient for every decision.

### Evaluation

A structured process for collecting and interpreting evidence about model-mediated or system-level behavior against defined expectations.

Evaluations may be deterministic, statistical, model-assisted, human, or combined. Evaluation is a sensor capability; it does not become control until connected to decision authority and corrective action.

### Golden Scenario

A curated case representing an important expected behavior, boundary condition, failure mode, or decision context.

Golden scenarios are anchors for regression and change detection. They are not universal ground truth and need not take the form of one ideal output.

### Drift

A material change in model-mediated behavior, system outcomes, operating conditions, or the relationship between evidence and expectations over time.

Drift may arise without code changes and may be semantic, logical, statistical, operational, or organizational.

### Deviation Signal

Evidence indicating that observed behavior or outcomes may have moved outside an intended operating envelope or expectation.

A deviation signal may be uncertain and require interpretation; it should not be confused with a guaranteed diagnosis or with a Bug by itself.

### Release Gate

A decision point at which authorized decision-makers use defined evidence, completion status, residual risk, and operating context to allow, block, limit, phase, or condition a release or configuration change.

A Release Gate is distinct from Definition of Done. DoD establishes whether the change has the required implementation, evidence, operability, and recovery support; the Release Gate determines whether the available evidence and residual risk are accepted for a specific deployment context.

Thresholds and evidence requirements should be proportional to consequences, reversibility, uncertainty, exposure, and context.

### Escalation

The transfer of a decision, incident, or uncertain case to an authority with greater context, competence, or permission to act.

Escalation requires a real recipient, decision right, and expected response path. Merely notifying someone is not necessarily escalation.

### Containment

Limiting where uncertainty or failure may propagate and defining how the system behaves when it leaves acceptable bounds.

Containment may include bounded authority, isolation, fallback, rate limits, degraded modes, rollback, human review, or shutdown.

### Fallback

A predefined alternative behavior used when the preferred model-mediated path cannot be accepted or completed safely.

A fallback may be deterministic, human-operated, degraded, or unavailable by design. Repeating the same uncertain action is not automatically a fallback.

### Rollback

Restoring a previously accepted configuration, model, prompt, policy, workflow, or system state after a harmful or uncertain change.

Rollback capability depends on versioning, traceability, compatibility, and authority to execute it.

### Human Authority

A human decision right that can materially approve, reject, change, contain, escalate, or stop system behavior.

A nominal human-in-the-loop step without adequate information, time, competence, or power is not effective Human Authority.

## Delivery vocabulary

### Requirement

The approved operating contract of a system, expressed through intended outcomes, invariants, boundaries, acceptable operating conditions, evidence expectations, resource constraints, and required failure handling.

For Model Judgment that performs business logic, a Requirement should avoid pretending that one exact output can always be specified. It should distinguish hard constraints from probabilistic expectations and define the context- and risk-derived Operating Envelope within which behavioral variation remains acceptable.

### Correctness

The condition in which observed system behavior satisfies the approved Requirement.

For Linear Software, correctness may often be established by comparing a deterministic result with a specified result. For a Thinking System, correctness may require evidence that relevant behavior remains within the approved Operating Envelope, preserves invariants, respects material resource constraints, and triggers required control responses when acceptable bounds are exceeded or cannot be established.

### Definition of Ready (DoR)

The entry gate at which work involving Model Judgment is judged sufficiently framed to begin implementation or controlled experimentation.

A DoR should make the operating contract and the plan for establishing compliance explicit in proportion to risk and autonomy. Relevant conditions may include intended outcomes, the location and authority of Model Judgment, invariants and prohibited actions, the initial Operating Envelope and business tolerances, consequential scenarios, evidence strategy, rationale for sample adequacy, cost or resource envelopes, ownership, decision authority, failure handling, and unresolved assumptions.

DoR is not proof of correctness. It may permit controlled experimentation when final tolerances are not yet known, provided exploratory hypotheses are distinguished from approved production requirements and the evidence path for refining them is explicit.

### Definition of Done (DoD)

The completion gate at which a change involving Model Judgment is judged to have sufficient implementation, evidence, operability, traceability, and recovery support for a defined release context.

A DoD may require deterministic tests for rules and invariants, evaluation evidence against the approved Operating Envelope, visible scope and limitations of the evidence, consequential-scenario coverage, resource-bound evidence, observability, tested fallback and corrective paths, residual-risk records, and operational ownership.

DoD is not equivalent to one successful run, a universal sample size, or release authorization. Passing an evaluation supports a bounded completion claim; it does not prove universal correctness or eliminate the need for runtime control.

### Bug

A violation of an approved Requirement caused or permitted by the implemented system.

In Linear Software, a Bug commonly appears as an incorrect deterministic result or transition. In a Thinking System, it may appear when model-mediated behavior materially exceeds an approved business tolerance, leaves the approved Operating Envelope, violates an invariant, permits a prohibited action, exceeds a material resource boundary, or when a required boundary, sensor, controller, containment path, or corrective mechanism is absent or ineffective.

For an LLM that performs business logic, a statistically evidenced excursion beyond an approved business tolerance is a Bug when that tolerance is part of the approved Requirement and the implemented system causes or permits the violation.

An individual undesirable output or Deviation Signal is not automatically a Bug. Diagnosis must distinguish a Requirement violation from an accepted distribution tail handled as designed, insufficient evidence, an invalid Requirement, an external condition outside system responsibility, or another unresolved cause.

See [`requirements-correctness-and-bugs.md`](requirements-correctness-and-bugs.md) for the full doctrine and classification model.

## Terminology evolution

When current documentation discusses an older UA source, the first relevant reference may use:

> **Thinking Systems** (previously described as **Behavioral Software** or **Behavioral Applications**)

Subsequent current discussion should use **Thinking Systems**. Historical titles, quotations, and preserved source bodies must retain their original language.