---
title: Constraint Realization Catalog
artifact_type: control-capability
status: informative
maturity: active
module: control-plane
topics:
  - constraints
  - ai-control-plane
  - containment
  - evidence
  - human-authority
tags:
  - ua/module/control-plane
  - ua/type/control-capability
  - ua/status/informative
  - ua/topic/constraints
  - ua/topic/ai-control-plane
  - ua/topic/containment
related:
  - README.md
  - ../../00-doctrine/control-loop-anatomy.md
---

# Constraint Realization Catalog

**Status:** Informative  
**Role:** Implementation-oriented examples of how constraints may be realized, evidenced, changed, and failed

## Purpose

This catalog helps teams translate an approved constraint into a concrete technical or socio-technical realization.

It is not a mandatory technology list. Named products and libraries are examples only. A tool belongs to a capability category because of the function it performs in a particular control loop, not because of its market label.

Use the catalog through this reasoning chain:

```text
constraint intent
→ subject, path, and scope
→ hard or soft claim
→ realization and enforcement point
→ failure behavior
→ evidence
→ change and override authority
→ reassessment trigger
```

## 1. Structural and interface realization

### Typical purposes

- require machine-readable output;
- limit allowed fields, values, and nesting;
- prevent unsafe or unsupported tool arguments;
- preserve compatibility between Model Judgment and deterministic code;
- reject output that cannot enter the downstream system safely.

### Illustrative mechanisms

- JSON Schema;
- OpenAPI schemas;
- Protocol Buffers and typed RPC contracts;
- Pydantic, Zod, dataclasses, or typed DTO validation;
- XML Schema;
- enum and range validation;
- deterministic parsers;
- constrained decoding;
- context-free grammars;
- regular-language or finite-state output constraints;
- database constraints and typed persistence boundaries.

### Evidence

- contract-test results;
- validation failure and repair rates;
- parser and serialization errors;
- rejected tool calls;
- schema-version compatibility;
- bypass or unvalidated-path detection;
- latency and cost of validation or repair.

### Important limit

A valid structure can still contain incorrect, harmful, unsupported, or unauthorized meaning. Structural constraints normally require semantic sensors, authority checks, and failure handling around them.

## 2. Authority and action realization

### Typical purposes

- prevent Model Judgment from creating its own authority;
- restrict the tools, functions, records, or state transitions it may affect;
- separate recommendation from execution;
- require deterministic or human approval for consequential actions;
- make least privilege enforceable.

### Illustrative mechanisms

- RBAC and ABAC;
- capability-based security and scoped tokens;
- OAuth scopes and short-lived credentials;
- service-account separation;
- tool and function allowlists;
- per-tool argument validation;
- deterministic authority gates;
- approval-before-execution workflows;
- write/read permission separation;
- transaction and state-transition guards;
- policy engines such as Open Policy Agent or Cedar;
- API gateway authorization policies;
- sandboxed execution accounts;
- dual control and separation of duties.

### Evidence

- permission and negative-authority tests;
- denied-action logs;
- unauthorized tool-call attempts;
- approval and override records;
- credential scope and expiry evidence;
- audit logs connecting recommendation, authorization, and execution;
- incidents involving privilege expansion or bypass.

### Important limit

Tool availability is not the same as authorized tool use. A framework exposing a tool to an agent does not establish who may authorize the action or which consequences are acceptable.

## 3. State and transaction realization

### Typical purposes

- preserve business invariants;
- prevent partial or inconsistent side effects;
- ensure that critical transitions happen only after validation and approval;
- make rollback or compensation possible;
- prevent repeated or non-terminating execution.

### Illustrative mechanisms

- explicit state machines;
- preconditions and postconditions;
- database transactions;
- idempotency keys;
- optimistic or pessimistic concurrency control;
- saga and compensation patterns;
- command validation;
- write-ahead logs and immutable decision records;
- bounded workflow steps;
- maximum plan, retry, or loop depth;
- stop states and terminal conditions.

### Evidence

- invariant and state-transition tests;
- duplicate-action and idempotency evidence;
- partial-failure simulations;
- compensation and rollback tests;
- transaction audit records;
- loop-depth and termination telemetry;
- recovery time and unresolved-state evidence.

### Important limit

A model may propose a state transition. Deterministic transaction logic should remain responsible for enforcing critical state and consistency rules.

## 4. Data and context realization

### Typical purposes

- prevent unauthorized data use or disclosure;
- restrict context to approved and relevant sources;
- preserve source provenance;
- reduce prompt-injection and context-contamination exposure;
- enforce residency, retention, and classification boundaries.

### Illustrative mechanisms

- tenant and row-level security;
- context-source allowlists;
- retrieval filters by identity, data class, product, geography, or time;
- signed or versioned source manifests;
- provenance metadata and source identifiers;
- deterministic redaction and DLP;
- PII detection with deterministic blocking where required;
- region-pinned storage and inference;
- network segmentation and egress controls;
- untrusted-content isolation;
- retrieval result validation;
- data-retention and deletion policies;
- encrypted storage and transport;
- context-budget and relevance rules.

### Evidence

- source and context lineage;
- cross-tenant and unauthorized-access tests;
- redaction and disclosure tests;
- retrieval allowlist violations;
- prompt-injection and contaminated-context scenarios;
- region and residency audits;
- source freshness and version evidence;
- privacy, security, or disclosure incidents.

### Important limit

Retrieval does not automatically make context trustworthy, current, relevant, or authorized. Context selection is part of the control boundary.

## 5. Resource and exposure realization

### Typical purposes

- limit economic and operational loss;
- contain runaway agent loops or tool use;
- preserve response-time obligations;
- bound experiment and rollout exposure;
- prevent one request or tenant from exhausting shared capacity.

### Illustrative mechanisms

- token and inference budgets;
- cost ceilings;
- rate and concurrency limits;
- timeouts and deadlines;
- maximum iterations, retries, recursion, and plan depth;
- tool-call quotas;
- circuit breakers;
- queue and backpressure controls;
- tenant-specific limits;
- canary and phased rollout;
- feature flags;
- population, geography, language, or product limits;
- bounded experiment duration and sample exposure;
- manual-review capacity caps;
- degraded mode when capacity is unavailable.

### Evidence

- token, tool, model, and infrastructure cost;
- p50/p95/p99 latency;
- rate-limit and timeout events;
- loop and retry distributions;
- queue and review backlog;
- fallback load and capacity;
- affected population and rollout state;
- cost or latency evidence that invalidates project economics.

### Important limit

A resource limit can protect the system while also destroying usability or ROI. Operational friction and false blocks are evidence relevant to project reauthorization, not merely tuning noise.

## 6. Environment and dependency realization

### Typical purposes

- constrain approved models, vendors, versions, and deployment modes;
- isolate untrusted execution;
- preserve evidence when external dependencies change;
- prevent unauthorized network or tool access;
- maintain a known operating configuration.

### Illustrative mechanisms

- pinned model and provider deployments;
- model and prompt version registries;
- deployment allowlists;
- provider-region restrictions;
- sandboxing, containers, and process isolation;
- read-only file systems;
- network egress allowlists;
- domain and endpoint restrictions;
- dependency health checks;
- signed configuration and release manifests;
- feature compatibility gates;
- fallback providers or deterministic paths;
- automatic disable on unapproved dependency change.

### Evidence

- active model, prompt, policy, tool, and configuration versions;
- provider and dependency change events;
- sandbox and network policy tests;
- dependency availability and degradation;
- fallback independence tests;
- incident reconstruction evidence;
- unapproved configuration drift.

### Important limit

A vendor-side model update can change behavior without an application-code change. Version and dependency evidence should therefore connect to delivery and project decisions.

## 7. Human Authority realization

### Typical purposes

- reserve consequential decisions for Human Authority;
- provide judgment when deterministic or automated control is insufficient;
- create escalation for ambiguous or high-consequence cases;
- prevent automated systems from normalizing exceptions.

### Illustrative mechanisms

- approval queues;
- Human-in-the-Loop gateways;
- dual approval;
- escalation matrices;
- incident command and shutdown authority;
- review interfaces that expose sources, uncertainty, and consequences;
- review-volume limits;
- time-bounded emergency override;
- independent review for conflicts of interest;
- mandatory reauthorization after defined changes.

### Evidence

- review volume and peak load;
- response time;
- accept, edit, reject, and override decisions;
- reviewer disagreement and calibration;
- alert fatigue and backlog;
- skipped or bypassed approval;
- competence and coverage gaps;
- cases in which Human Authority could not act before harm propagated.

### Important limit

A button labeled “Approve” does not create Human Authority. The person must have adequate evidence, context, competence, time, capacity, independence, and power to block or change the path.

## 8. Soft behavioral realization

### Typical purposes

- shape tone, reasoning approach, output priorities, or default behavior;
- express policies too semantic to encode fully as deterministic rules;
- reduce undesired behavior before hard validation and review;
- provide task and domain context.

### Illustrative mechanisms

- system prompts and instruction templates;
- few-shot examples;
- rubrics;
- model policy text;
- refusal and escalation instructions;
- prompt registries and versioning;
- retrieval of approved procedural guidance;
- model tuning or preference optimization;
- critique or repair passes.

### Evidence

- scenario and regression results;
- prompt and model version traces;
- policy adherence evaluation;
- violation, repair, and fallback rates;
- drift after prompt, model, or context changes;
- difference between claimed and demonstrated behavior.

### Important limit

Soft constraints are probabilistic influence. They should not be described as mechanical stops, hard invariants, or guaranteed compliance.

## 9. Compound constraint example: support reply drafting

### Approved constraint intent

> The system may draft a reply but must not send it, must not expose another tenant's data, and must not present unsupported product claims as fact.

### Possible realization

| Capability function | Illustrative realization |
|---|---|
| Authority constraint | Service account has no message-send permission. |
| Data constraint | Tenant isolation and source allowlist are enforced before context assembly. |
| Structural constraint | Draft output follows a typed schema containing text, source references, and uncertainty. |
| Soft constraint | Prompt requires grounded wording and disclosure of missing evidence. |
| Sensor | Claim-to-source evaluation, human reject/edit data, cross-tenant tests, and incident evidence. |
| Human Authority constraint | Support agent approval is required before any send action. |
| Controller | Support lead and release authority interpret evidence and decide changes. |
| Actuator | Disable the feature, roll back model/prompt/policy, narrow population, or switch to a deterministic template. |
| Reauthorization trigger | Autonomous send, new data class, new product, unsupported-claim incident, or review-capacity failure. |

The constraint is implemented through a system of capabilities rather than one guardrail.

## 10. Compound constraint example: bounded agent tool use

### Approved constraint intent

> The agent may inspect an incident and recommend or execute only approved reversible actions inside the current environment.

### Possible realization

- scoped credentials;
- tool allowlist;
- typed tool contracts;
- deterministic preconditions;
- environment and resource limits;
- human approval for non-routine actions;
- immutable action trace;
- post-action outcome sensor;
- bounded retries and plan depth;
- rollback or compensation path;
- feature-level and project-level reauthorization triggers.

A tool orchestration framework can host some of these mechanisms. It does not own the organizational constraint source, project authorization, residual-risk acceptance, or Human Authority by default.

## 11. Review prompts by lifecycle level

### Organizational source

- Which source is authoritative?
- What is prohibited, conditionally allowed, or delegated?
- Which shared enforcement and evidence capabilities exist?
- Who may approve an exception or change?

### Project architecture

- Which material scenario requires this constraint?
- Is the constraint hard or soft?
- Is enforcement technically and operationally feasible?
- Is evidence available within the required latency?
- What is the build, run, review, fallback, and incident cost?
- Which constraint failure would make the project non-viable?

### Delivery realization

- Which inherited version is being implemented?
- Where is the enforcement point?
- How is failure handled?
- How are bypass, degradation, and unavailability tested?
- Which configuration and versions are deployed?
- Who may change or override the mechanism?

### Runtime operation

- Is the constraint active and healthy?
- Which violations, blocks, overrides, and false blocks occurred?
- Can corrective action happen within the required time?
- Did the operating context or dependency change?
- Does the evidence remain local, require project reauthorization, or require organizational review?

## 12. Selection rule

Do not select a technology first and then invent the constraint it supposedly provides.

Start from:

1. the approved Requirement and material consequence;
2. the authority or operating space that must be bounded;
3. the guarantee strength required;
4. the enforcement and failure behavior needed;
5. the evidence and decision latency required;
6. the authority and actuator path;
7. the complete operational and economic cost.

## Relationships

- [`README.md`](README.md) defines the draft-normative Constraint capability.
- [`../../00-doctrine/control-loop-anatomy.md`](../../00-doctrine/control-loop-anatomy.md) defines the capability relationships.
- [`../README.md`](../README.md) defines the AI Control Plane.
- [`../../01-patterns/project-control-architecture-and-viability-review.md`](../../01-patterns/project-control-architecture-and-viability-review.md) derives project constraints from risk and viability.
- [`../../01-patterns/thinking-system-review.md`](../../01-patterns/thinking-system-review.md) realizes and verifies constraints at delivery level.
- [`../../03-reference-architectures/`](../../03-reference-architectures/) shows context-specific compositions.
