---
title: Thinking System Review Template
artifact_type: pattern
status: informative
maturity: active
module: patterns
topics:
  - thinking-systems
  - model-judgment
  - evidence
  - sdlc
  - human-authority
tags:
  - ua/module/patterns
  - ua/type/pattern
  - ua/status/informative
  - ua/topic/thinking-systems
  - ua/topic/model-judgment
  - ua/topic/evidence
  - ua/topic/sdlc
canonical_for:
  - thinking-system-review-template
related:
  - thinking-system-review.md
  - judgment-node-boundary.md
  - ../00-doctrine/requirements-correctness-and-bugs.md
  - ../02-ai-control-plane/README.md
source_basis:
  - "../content/raw/Designing Non-Deterministic Systems: Maintaining Engineering Rigor in the AI Era.pdf"
---

# Thinking System Review Template

## How to use this template

This is the default working artifact for the draft-normative [`Thinking System Review`](thinking-system-review.md) pattern.

Use one copy for one system, feature, or material change. Keep it as a living document through framing, implementation or experimentation, completion, release, and operation.

After a release decision:

1. preserve an immutable or versioned snapshot;
2. link the deployed system, model, prompt, policy, tool, and configuration versions where material;
3. create a new version when a reassessment trigger occurs;
4. preserve the relationship to the previous decision.

Mark an item `N/A` with a reason when it does not apply. Do not silently delete review areas because they appear inconvenient.

---

## 1. Review identity

- **System or feature:**
- **Review version:**
- **Previous review or decision:**
- **Review status:** Draft / Ready review / In implementation / In experiment / Done review / Release review / Operating / Reassessment
- **Date opened:**
- **Last updated:**
- **Implementation responsibility:**
- **Evaluation responsibility:**
- **Operational responsibility:**
- **Release decision authority:**

### Relevant versions and references

- **Requirement or feature record:**
- **Architecture or design record:**
- **Repository and revision:**
- **Model and version:**
- **Prompt or instruction version:**
- **Policy or configuration version:**
- **Tools and external services:**
- **Evaluation evidence location:**
- **Operational dashboard or logs:**

---

## 2. Intended outcome and scope

- **User or business outcome:**
- **Why Model Judgment is used:**
- **In scope:**
- **Out of scope:**
- **Affected users, systems, or parties:**
- **Current lifecycle context:** Bounded experiment / Prototype / Limited deployment / Production change
- **Key assumptions:**
- **Known unknowns:**

### System boundary

Describe the complete system responsibility, not only the model call.

- **Inputs:**
- **Outputs, decisions, paths, or actions:**
- **Upstream dependencies:**
- **Downstream dependencies:**
- **External dependencies:**

---

## 3. Mixed-system responsibilities

### 3.1 Deterministic responsibilities

- **Rules:**
- **Invariants:**
- **Schemas and interface contracts:**
- **Authentication and permissions:**
- **Exact constraints:**
- **Transactions, audit, or data-handling obligations:**

### 3.2 Model-mediated responsibilities

- **Expected judgment:**
- **Acceptable variation:**
- **Model-mediated decisions, paths, actions, or outputs:**
- **Unacceptable outcomes:**

### 3.3 Boundary and control responsibilities

- **Context assembly and provenance:**
- **Authority boundary:**
- **Deterministic validation:**
- **Sensors and evidence:**
- **Controller or decision authority:**
- **Fallback:**
- **Containment:**
- **Escalation:**
- **Rollback, disable, or shutdown:**

---

## 4. Judgment Nodes

Repeat this section for each consequential Judgment Node. Use the minimal fields by default and complete optional fields where authority, downstream impact, reversibility, or failure consequences justify them.

### Judgment Node 1

- **Name:**
- **Purpose:**
- **Placement:** Input Interpretation / Decision Logic / Output Mediation / Combination
- **Inputs and approved context:**
- **Allowed authority:**
- **Hard constraints:**
- **Unacceptable outcomes:**
- **Evidence and telemetry:**
- **Fallback or escalation:**
- **Operational owner:**

Optional extensions:

- **Consequentiality and downstream impact:**
- **Model, prompt, policy, tool, and configuration dependencies:**
- **Acceptable variation:**
- **Output contract:**
- **Failure conditions and Deviation Signals:**
- **Containment:**
- **Rollback or shutdown:**
- **Change authority:**

### Additional Judgment Nodes

Copy the card above as needed. Do not create a separate registry unless independent ownership or lifecycle management genuinely requires one.

---

## 5. Requirement and Operating Envelope

### 5.1 Approved Requirement

- **Intended outcome:**
- **Deterministic obligations:**
- **Model-mediated obligations:**
- **Authority boundaries:**
- **Evidence expectations:**
- **Required failure handling:**

### 5.2 Operating Envelope

- **Intended operating conditions:**
- **Acceptable behavioral range:**
- **Prohibited outcomes or regions:**
- **Business tolerances:**
- **Resource envelope:** Token / inference / compute / latency / concurrency / tool or service cost
- **Exposure and deployment limits:**
- **Human supervision requirements:**
- **Known assumptions:**

### 5.3 Control-loop design

- **Sensors:**
- **Constraints and actuators:**
- **Controller or decision authority:**
- **Corrective actions:**
- **Feedback latency or review timing:**

---

## 6. Definition of Ready

For each item, mark `[x]`, `[ ]`, or `N/A`, and link evidence or explain open conditions.

### 6.1 Outcome and scope

- [ ] Intended user or business outcome is defined.
- [ ] System boundary is defined.
- [ ] In-scope and out-of-scope behavior is identified.
- [ ] Experiment, prototype, limited deployment, and production Requirement are distinguished where relevant.

**Evidence or notes:**

### 6.2 Judgment placement

- [ ] Consequential Judgment Nodes are identified.
- [ ] Each node's placement class is recorded.
- [ ] Affected decisions, actions, paths, or outputs are identified.
- [ ] Model-mediated responsibilities are separated from deterministic responsibilities.

**Evidence or notes:**

### 6.3 Authority

- [ ] Permitted authority is defined.
- [ ] Prohibited decisions and actions are defined.
- [ ] Human Authority or approval points are identified where required.
- [ ] Deterministic execution boundary is defined.

**Evidence or notes:**

### 6.4 Requirements and Operating Envelope

- [ ] Deterministic invariants are identified.
- [ ] Acceptable behavioral variation is described.
- [ ] Unacceptable outcomes are described.
- [ ] Material tolerances or thresholds are defined where feasible and justified.
- [ ] Resource envelope is defined where material.
- [ ] Required failure handling is specified.

**Evidence or notes:**

### 6.5 Evidence strategy

- [ ] Relevant scenarios are identified.
- [ ] Consequential and adversarial scenarios are included where appropriate.
- [ ] Evaluation approach is defined.
- [ ] Evidence sources and limitations are understood.
- [ ] Success and failure criteria are defined.
- [ ] Known unknowns are recorded.

**Evidence or notes:**

### 6.6 Control strategy

- [ ] Necessary sensors are identified.
- [ ] Necessary constraints and actuators are identified.
- [ ] Fallback, containment, or escalation is defined.
- [ ] Observability expectations are defined.
- [ ] Rollback or shutdown feasibility is considered.

**Evidence or notes:**

### 6.7 Ownership

- [ ] Implementation responsibility is assigned.
- [ ] Evaluation responsibility is assigned.
- [ ] Operational responsibility is assigned.
- [ ] Release decision authority is explicit.

**Evidence or notes:**

### 6.8 Feasibility

- [ ] Expected cost and latency are understood sufficiently for the decision.
- [ ] Required data, environments, and tools are available.
- [ ] Legal, security, privacy, and compliance dependencies are identified.
- [ ] Unresolved risks are closed or explicitly accepted for a bounded experiment.

**Evidence or notes:**

### 6.9 Readiness decision

Select one:

- [ ] Ready for implementation
- [ ] Ready for bounded experiment
- [ ] Ready with explicit conditions
- [ ] Needs clarification
- [ ] Control cost not justified
- [ ] AI path rejected

- **Decision date:**
- **Decision authority:**
- **Conditions or open questions:**
- **Bounded-experiment limits and stopping conditions, if applicable:**
- **Rationale:**

---

## 7. Implementation or bounded experiment

- **Selected path:** Implementation / Bounded experiment
- **Scope:**
- **Users, data, and environments:**
- **Authority and tool limits:**
- **Duration or exposure limit:**
- **Resource limits:**
- **Stopping or escalation conditions:**
- **Changes made:**
- **Evidence collected:**
- **Requirement, Operating Envelope, or boundary refinements:**
- **Material deviations or incidents:**

---

## 8. Definition of Done

For each item, mark `[x]`, `[ ]`, or `N/A`, and link evidence or explain limitations.

### 8.1 Deterministic implementation evidence

- [ ] Applicable unit tests passed.
- [ ] Applicable integration tests passed.
- [ ] Interface and schema contracts were verified.
- [ ] Deterministic invariants were tested.
- [ ] Authorization and permission controls were tested.
- [ ] Applicable security, privacy, and compliance checks were completed.

**Evidence or notes:**

### 8.2 Behavioral evaluation evidence

- [ ] Required scenario set was executed.
- [ ] Expected behavior was assessed.
- [ ] Unacceptable outcomes were tested.
- [ ] Operating Envelope evidence was collected.
- [ ] Variability across relevant runs was assessed where material.
- [ ] Regressions against the accepted baseline were checked.
- [ ] Material model and configuration versions were recorded.

**Evidence or notes:**

### 8.3 Evidence quality

- [ ] Evaluation datasets and scenarios are documented.
- [ ] Known evidence limitations are recorded.
- [ ] Unsupported extrapolations are avoided.
- [ ] Confidence is proportional to the evidence.
- [ ] Material evidence gaps are explicitly listed.

**Evidence or notes:**

### 8.4 Authority and boundary evidence

- [ ] Authority limits were tested.
- [ ] Prohibited actions were blocked.
- [ ] Tool-use constraints were tested where applicable.
- [ ] Deterministic validation around Judgment Nodes was verified.
- [ ] Human Authority or approval points were tested where applicable.

**Evidence or notes:**

### 8.5 Resource evidence

- [ ] Token, inference, or compute use was assessed where material.
- [ ] Latency was assessed.
- [ ] Concurrency or rate behavior was assessed where material.
- [ ] Tool and external-service cost was assessed.
- [ ] Resource limits and failure behavior were tested.

**Evidence or notes:**

### 8.6 Operational controls

- [ ] Required sensors are operational.
- [ ] Required telemetry is available.
- [ ] Alerts or review triggers are defined.
- [ ] Drift indicators are available where needed.
- [ ] Logs and traceability are sufficient for diagnosis.

**Evidence or notes:**

### 8.7 Failure handling

- [ ] Fallback was tested.
- [ ] Containment was tested.
- [ ] Escalation path was verified.
- [ ] Rollback or disable mechanisms were tested where applicable.
- [ ] Degraded mode is understood.
- [ ] Partial-failure behavior was assessed.

**Evidence or notes:**

### 8.8 Operability and ownership

- [ ] Operational responsibility is assigned.
- [ ] Support and incident expectations are defined.
- [ ] Reassessment triggers are documented.
- [ ] Material residual risks are recorded.
- [ ] Relevant operational documentation is complete.

**Evidence or notes:**

### 8.9 Completion decision

Select one:

- [ ] Complete
- [ ] Complete with recorded limitations
- [ ] Insufficient evidence
- [ ] Controls incomplete
- [ ] Return to implementation
- [ ] Return to bounded experiment

- **Decision date:**
- **Decision responsibility:**
- **Evidence references:**
- **Known limitations:**
- **Material gaps:**
- **Rationale:**

---

## 9. Residual risk

- **Known residual risks:**
- **Expected consequence or impact:**
- **Affected users, systems, or parties:**
- **Current mitigations:**
- **Evidence uncertainty:**
- **Accepted residual behavior handled as designed:**
- **Conditions under which current acceptance is no longer valid:**

---

## 10. Proposed deployment scope

- **Environment:**
- **Version or configuration:**
- **Users or population:**
- **Data scope:**
- **Duration:**
- **Usage, rate, or resource limits:**
- **Tool and action permissions:**
- **Human supervision:**
- **Rollout approach:** Full / Limited / Phased / Canary
- **Conditions:**

---

## 11. Release Gate

DoD establishes completeness. This section records whether the available evidence and residual risk are acceptable for the proposed deployment context.

### 11.1 Evidence reviewed

- **Approved Requirement and Operating Envelope:**
- **DoD outcome:**
- **Deterministic evidence:**
- **Behavioral evaluation evidence:**
- **Authority and boundary evidence:**
- **Control and failure-handling evidence:**
- **Resource evidence:**
- **Known limitations and gaps:**
- **Residual-risk statement:**

### 11.2 Release decision

Select one:

- [ ] Release
- [ ] Limited release
- [ ] Phased or canary release
- [ ] Release with conditions
- [ ] Human-supervised release
- [ ] Block
- [ ] Return to experimentation
- [ ] Roll back
- [ ] Escalate

- **Decision date:**
- **Release decision authority:**
- **Decision rationale:**
- **Conditions:**
- **Monitoring and review expectations:**
- **Rollback, containment, or shutdown trigger:**
- **Decision validity period or reassessment date, if applicable:**

---

## 12. Operation and reassessment

### 12.1 Runtime observation

- **Key runtime evidence:**
- **Deviation Signals:**
- **Review or alert thresholds and rationale:**
- **Named response path:**
- **Corrective actions available:**

### 12.2 Reassessment triggers

Mark applicable triggers and add system-specific triggers.

- [ ] Material model or model-configuration change
- [ ] Prompt or policy change
- [ ] Authority change
- [ ] New tool integration
- [ ] Significant data or context-source change
- [ ] Incident or confirmed Requirement violation
- [ ] Material drift or evidence degradation
- [ ] Expansion of deployment scope or population
- [ ] Material change in resource use, latency, or external dependency
- [ ] New legal, security, privacy, compliance, or business constraint
- [ ] Other:

### 12.3 Reassessment outcome

- [ ] Current decision remains valid
- [ ] New evidence required
- [ ] Deployment scope narrowed
- [ ] Return to implementation
- [ ] Return to bounded experiment
- [ ] Release conditions changed
- [ ] Rollback or containment initiated
- [ ] Escalated
- [ ] Shutdown or AI path rejected

- **Date:**
- **Decision authority:**
- **Rationale:**
- **Link to next review version:**

---

## 13. Version and decision history

| Review version | Date | Trigger | Readiness outcome | Completion outcome | Release or reassessment decision | Decision authority | Snapshot or link |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

---

## Final snapshot check

Before preserving a release or reassessment snapshot:

- [ ] Requirement and Operating Envelope reflect the actual approved contract.
- [ ] Consequential Judgment Nodes and authority boundaries are current.
- [ ] DoR, DoD, and Release Gate outcomes are distinct and recorded.
- [ ] Evidence references resolve and known limitations are visible.
- [ ] Residual risk and deployment scope are explicit.
- [ ] Operational responsibility and corrective paths are real.
- [ ] Reassessment triggers are documented.
- [ ] Relevant versions and dependencies are traceable.
