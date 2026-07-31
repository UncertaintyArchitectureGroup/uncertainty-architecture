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
  - constraints
tags:
  - ua/module/doctrine
  - ua/type/glossary
  - ua/status/draft-normative
  - ua/topic/thinking-systems
  - ua/topic/uncertainty-boundary
  - ua/topic/ai-control-plane
  - ua/topic/constraints
canonical_for:
  - doctrine-vocabulary
---

# Uncertainty Architecture Glossary

## Status and use

This glossary defines the current canonical meaning of core Uncertainty Architecture terms where an entry exists.

It is **draft normative**. Historical publications retain their original wording when terminology is later renamed, narrowed, or superseded. A term in a talk, article, implementation, or external framework does not automatically acquire the UA meaning defined here.

## System categories

### Thinking System

A software system whose runtime behavior depends partly on probabilistic Model Judgment while consequential deterministic responsibilities, Constraints, decision rights, evidence, and corrective mechanisms remain explicit.

**Thinking Systems** is the current UA category. Earlier UA publications used **Behavioral Software** and **Behavioral Applications**; those names remain historical predecessors.

Agentic systems are a higher-autonomy subset of Thinking Systems rather than the whole category.

### Linear Software

Software whose relevant execution paths and decision rules are explicitly encoded and intended to produce predictable behavior under defined conditions.

Linear Software may still contain operational uncertainty, concurrency, external dependencies, statistical components, and defects. The term distinguishes explicitly encoded control paths from runtime judgment delegated to probabilistic models.

## Boundary and responsibility

### Deterministic Core

The rules, Invariants, permissions, data handling, transaction boundaries, audit requirements, and other responsibilities that must remain explicitly controlled and testable regardless of model behavior.

The Deterministic Core is a responsibility boundary, not necessarily one physical component or service.

### Model Judgment

Interpretation, synthesis, classification, generation, planning, ranking, or action selection performed through a probabilistic model under uncertainty.

Model Judgment may provide useful adaptation and semantic reasoning. It must not be treated as equivalent to a guaranteed business rule.

### Judgment Node

A bounded location in a system or workflow where Model Judgment influences an output, decision, path, or action.

A Judgment Node may perform Input Interpretation, Decision Logic, Output Mediation, or a combination. Its purpose, inputs, authority, applicable Constraints, evidence, failure handling, and ownership should be visible enough to review and operate.

### Input Interpretation

Model Judgment that converts ambiguous, unstructured, incomplete, or context-dependent input into intent, classification, extracted structure, normalized representation, or usable system context.

### Decision Logic

Model Judgment that influences or selects routing, ranking, planning, prioritization, tool choice, action recommendation, or action initiation within an allowed authority boundary.

Decision Logic does not by itself imply autonomous execution or unlimited authority.

### Output Mediation

Model Judgment that creates, adapts, filters, summarizes, explains, or transforms information for a human or downstream system.

Output Mediation may be consequential even when it does not alter underlying data because presentation can change interpretation, trust, disclosure, approval, or subsequent action.

### Uncertainty Boundary

The interface at which deterministic system responsibilities meet Model Judgment.

The boundary may include context assembly, permissions, schemas, policy checks, tool access, validation, evidence collection, fallback, and escalation. It is broader than the model API call.

### Invariant

A condition that must remain true across relevant system states or transitions.

An Invariant should be enforced through deterministic mechanisms when violation would create unacceptable consequences. A probabilistic instruction is not by itself an Invariant.

### Constraint

An approved condition that limits the allowed operating space of a Thinking System.

A Constraint may bound states, transitions, actions, authority, inputs, context, data, tools, outputs, resources, environments, deployment scope, or Human Authority requirements.

A Constraint is an authoritative decision object, not an execution mechanism. It is distinct from the concrete mechanism that implements, enforces, or influences it. That mechanism is a **Constraint Realization**.

A material Constraint should remain traceable to its authoritative source or project-risk rationale, subject, path, scope, claimed strength, realization, assumptions, failure behavior, evidence, and change or override authority.

### Hard Constraint

A scoped Constraint whose complete realized path deterministically prevents or rejects violation within explicitly stated assumptions, subject, path, scope, and enforcement boundaries.

Hard or soft strength is a claim about a Constraint together with its realized path. It is not an intrinsic property of policy prose, a requirement sentence, or an organizational source. The same source condition may be hard in one system path and soft in another.

A probabilistic detector, evaluator, prompt, model policy, or natural-language instruction does not become a Hard Constraint merely because its failure behavior is documented.

### Soft Constraint

A scoped Constraint whose realized path influences probabilistic behavior without guaranteeing that a prohibited state, action, or output remains unreachable.

Prompts, natural-language policies, rubrics, examples, model preferences, and probabilistic classifiers may provide Soft Constraint realizations. They must not be represented as deterministic guarantees.

When one source condition has different guarantee strengths across subjects, paths, or scopes, record separate Constraint claims rather than one mixed hard/soft row.

### Constraint Realization

The concrete technical or socio-technical mechanism through which a Constraint is implemented, configured, enforced or influenced, evidenced, and operated for a defined scope.

Examples may include typed interfaces, schemas, permission gates, policy engines, tool allowlists, state machines, data isolation, resource limits, deployment boundaries, deterministic blocks, or mandatory Human Authority.

A Constraint Realization is not automatically effective merely because the mechanism exists. Active version, coverage, failure behavior, evidence, and decision authority remain relevant.

## Control-loop vocabulary

### Nested Control Lifecycle

The connected organizational, project, delivery, and runtime decision structure through which authoritative Constraints, capabilities, and decision rights flow downward by reference, while evidence flows upward when it invalidates the basis of an earlier decision.

The Nested Control Lifecycle distinguishes project authorization from delivery release and routes runtime evidence to local correction, project reauthorization, or organizational review. It is a decision model, not a mandatory hierarchy, committee, or ceremony sequence.

### Control-Loop Capability Anatomy

The logical model consisting of four capability families:

1. Constraints and their realizations define and operationalize approved boundaries.
2. Sensors and evidence observe behavior, outcomes, conditions, and control state.
3. Controllers and decision authority compare, interpret, select, and authorize.
4. Actuators and corrective action execute authorized change.

The Constraints family is intentionally composite: the Constraint is the authoritative boundary object, while the Constraint Realization provides the operational mechanism. The anatomy does not prescribe four physical services or one deployment topology.

A closed feedback loop is formed by evidence reaching a Controller and authorized Actuator action affecting the controlled process. Constraints bound the space in which that loop may operate; they are not the feedback edge itself.

### AI Control Plane

The distributed capability model used to define and realize boundaries, observe, evaluate, decide, and correct model-mediated behavior in a Thinking System.

Its responsibilities may be distributed across application code, platform services, evaluation systems, release processes, human workflows, and organizational mechanisms. It is not necessarily a standalone product or centralized infrastructure layer.

### Actuator

A mechanism that executes an authorized change in system behavior or operating conditions.

Examples may include changing prompts, models, context, routing, permissions, tools, deployment scope, fallback state, rollback state, Constraint Realization, containment, compensation, or shutdown state.

An API call, workflow step, framework, deployment operation, or human action is an Actuator only when it provides a real path from an authorized decision to changed operation.

### Sensor

A mechanism that produces evidence about outputs, outcomes, operating conditions, drift, incidents, Constraint Realization state, violations, Actuator execution, or control performance.

A Sensor need not produce one objective truth value. It must produce information useful enough for a bounded decision while making uncertainty, coverage, latency, and blind spots visible.

An evaluator normally performs a Sensor function. A gate that interprets evaluation evidence and selects `block`, `canary`, or `release` performs a Controller function.

### Controller

The decision function that compares or interprets evidence relative to approved Requirements, Constraints, and operating assumptions, then selects or authorizes corrective action.

A Controller may be implemented in software, assigned to a human, or distributed across a socio-technical process. It must distinguish changes within delegated authority from changes requiring delivery reassessment, project reauthorization, or organizational review.

A Controller decides or authorizes. An Actuator executes.

### Open-Loop System

A system that acts without meaningful feedback connected to corrective authority and an effective intervention path.

Logging alone does not close the loop when evidence cannot change, contain, roll back, escalate, or stop behavior.

### Closed-Loop System

A system in which observations are evaluated against intended operating conditions and can lead to authorized action that affects the controlled process.

Closed-loop does not imply fully automated control or safe operation. A loop may be closed while operating outside an approved boundary or with inadequate Constraints.

### Operating Envelope

The approved range of conditions, authority, consequences, resource use, and observed behavior within which a system is considered acceptable to operate under a defined Requirement.

The Operating Envelope is part of a Requirement, not a synonym for the complete Requirement.

## Evidence and change

### Evidence

A recorded signal, observation, evaluation result, incident, outcome, configuration state, or review artifact used to support a system decision.

Evidence has scope and limitations. A metric, benchmark, anecdote, or model-generated score is not automatically sufficient for every decision.

### Evaluation

A structured process for collecting and interpreting evidence about model-mediated or system-level behavior against defined expectations.

Evaluation normally supplies a Sensor capability. It becomes part of control only when evidence reaches decision authority and an effective Actuator path.

### Golden Scenario

A curated case representing an important expected behavior, boundary condition, failure mode, or decision context.

Golden Scenarios anchor regression and change detection. They are not universal ground truth and need not prescribe one ideal output.

### Drift

A material change in model-mediated behavior, system outcomes, operating conditions, Constraint sources or realizations, or the relationship between evidence and expectations over time.

Drift may arise without application-code changes and may be semantic, logical, statistical, operational, organizational, or constraint-related.

### Deviation Signal

Evidence indicating that observed behavior, outcomes, Constraints, or operating conditions may have moved outside an intended Operating Envelope or expectation.

A Deviation Signal may be uncertain and require interpretation. It is not a guaranteed diagnosis or automatically a Bug.

### Release Gate

A decision point at which an authorized decision-maker determines whether realized Constraints, available evidence, residual risk, and operational capacity are acceptable for a specific deployment context.

A Release Gate is distinct from Definition of Done. DoD establishes implementation and evidence completeness; the Release Gate accepts, limits, conditions, escalates, or rejects release.

### Escalation

The transfer of a decision, incident, or uncertain case to an authority with greater context, competence, or permission to act.

Escalation requires a real recipient, decision right, expected response path, and available action.

### Containment

Limiting where uncertainty or failure may propagate and defining how the system behaves when it leaves acceptable bounds.

Containment may include bounded authority, isolation, fallback, rate limits, degraded modes, rollback, human review, or shutdown.

### Fallback

A predefined alternative behavior used when the preferred model-mediated path cannot be accepted or completed.

A Fallback may be deterministic, human-operated, degraded, or intentionally unavailable. Repeating the same uncertain action is not automatically a Fallback.

### Rollback

Restoring a previously accepted model, prompt, policy, Constraint Realization, workflow, configuration, deployment, or system state after a harmful or uncertain change.

Rollback depends on versioning, traceability, compatibility, and authority to execute it.

### Human Authority

A human decision right that can materially approve, reject, change, contain, escalate, or stop system behavior.

A nominal human-in-the-loop step without adequate information, competence, time, capacity, independence, or intervention power is not effective Human Authority.

## Requirement, diagnosis, and decision vocabulary

### Requirement

The approved operating contract for a system, feature, or change.

A Requirement may include intended outcomes, deterministic and model-mediated obligations, Invariants, authority boundaries, Constraints, acceptable operating conditions, resource boundaries, evidence expectations, and failure handling. The Operating Envelope is one part of this contract.

### Correctness

The condition in which observed system behavior satisfies the approved Requirement.

Correctness is a system property. Different obligations may require deterministic verification, evidence across model-mediated variation, or both.

### Deterministic Defect

A defect in explicitly encoded logic, configuration, interface, state handling, permission enforcement, Constraint Realization, or another deterministic responsibility.

A Deterministic Defect may cause model-mediated or non-model behavior to violate the Requirement.

### Behavioral Deviation

An observed model-mediated behavior or distribution change that differs from an expectation or accepted baseline.

A Behavioral Deviation is evidence. It becomes a Bug only when it violates the approved Requirement.

### Bug

A system-level violation of an approved Requirement.

A Bug may originate in deterministic code, Model Judgment, context, data, configuration, a Constraint or its realization, evidence, authority, an external dependency, or interaction among them. A single surprising output or tail event is not automatically a Bug without the relevant Requirement and diagnosis.

### Accepted Residual Behavior

Known behavior, uncertainty, or exposure explicitly accepted by an authorized decision within a stated scope, period, Requirement, Constraint baseline, and residual-risk decision.

Acceptance does not make the behavior correct outside that boundary and must be reassessed when its assumptions change.

### Project Authorization

The project-level decision that a proposed Thinking System has a sufficiently credible and viable Constraint and control architecture to proceed within a defined boundary.

Possible outcomes include bounded research, constrained authorization, redesign, deferral, escalation, or No-Go.

### Project Reauthorization

A new project-level decision required when evidence invalidates a material project assumption about risk, authority, Constraint feasibility, evidence, capacity, control economics, deployment scope, or residual exposure.

### Architectural Veto

A decision not to build or continue an AI path because required Constraints, evidence, authority, corrective mechanisms, operational capacity, or economics cannot credibly support the proposed consequences and scope.

No universal score or role title is required for Architectural Veto.

### Definition of Ready

The delivery-level decision that a bounded system, feature, or material change is sufficiently framed to begin implementation or a bounded experiment within inherited project authorization.

### Definition of Done

The delivery-level decision that implementation and required evidence are sufficiently complete for a separate Release Gate decision.

DoD does not itself authorize deployment.
