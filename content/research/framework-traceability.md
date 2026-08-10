---
title: Research-to-Framework Traceability
artifact_type: research-traceability
status: research
maturity: active
module: research
topics:
  - provenance
  - thinking-systems
  - constraints
  - repository-architecture
tags:
  - ua/module/research
  - ua/type/research-traceability
  - ua/status/research
  - ua/topic/provenance
  - ua/topic/constraints
created: 2026-07-24
updated: 2026-08-10
license: CC-BY-4.0
---

# Research-to-Framework Traceability

## Purpose

This document records how UA research influences framework components without treating every historical or presentation statement as an approved requirement.

It prevents two opposite errors:

1. building methodology without preserving the reasoning behind it;
2. treating every statement from an article, talk, presentation, or working note as normative.

This matrix is the canonical repository record for material source-to-framework decisions. It is a synthesis aid, not a mandatory ledger for every sentence.

## Status vocabulary

- **Research Finding** — preserved conclusion from research material.
- **Candidate** — potentially suitable for framework translation.
- **Needs Resolution** — terminology, evidence, scope, or contradiction must be resolved.
- **Proposed for Framework Review** — mature enough for a deliberate proposal.
- **Active** — accepted into the current framework boundary, subject to the owning document's status.
- **Superseded** — replaced by a later formulation.
- **Rejected** — considered and intentionally not adopted.

## Candidate framework areas

Traceability entries may point toward Doctrine, Pattern, AI Control Plane capability, Reference Architecture, Artifact, responsibility or process, and Failure Mode.

Lifecycle and operating-model concerns may be represented across these areas rather than maintained as a separate top-level module unless the framework later adopts one explicitly.

## Traceability matrix

| Research finding or source claim | Source or synthesis | Framework area | Status | Current framework decision |
|---|---|---|---|---|
| Model-mediated runtime behavior has non-zero variance, so design must distinguish deterministic responsibilities, Model Judgment, and the boundaries and controls between them. | *Designing Non-Deterministic Systems* PDF, opening material, refined through framework review | Doctrine | Active | Thinking Systems are mixed systems; deterministic obligations remain explicit while Model Judgment is bounded and evaluated through system-level Requirements. |
| Correctness cannot always be represented by one exact output, and Requirements must define acceptable operating space. | Presentation requirement and tolerance material | Doctrine and glossary | Active | A Requirement is the approved operating contract; the Operating Envelope is one part of it; Correctness is satisfaction of the Requirement. |
| A stochastic defect should be reasoned about through business tolerances and observed behavior rather than code-path failure alone. | Presentation bug material | Doctrine and glossary | Active | A Bug is a system-level Requirement violation. A tail event, metric change, or Deviation Signal remains evidence until diagnosis establishes the violation and its source. |
| Model Judgment creates value in input interpretation, dynamic decision logic, and contextual output. | Presentation architectural-space material | Doctrine | Active | Input Interpretation, Decision Logic, and Output Mediation are functional placement classes, not a mandatory pipeline. |
| Model Judgment that performs or materially influences a Consequential Runtime Responsibility requires an explicit boundary around purpose, context, authority, Constraints, evidence, failure handling, and ownership. | Presentation control framing plus framework synthesis | Pattern | Active | The Judgment Node Boundary provides proportional minimal and extended modes without requiring a separate node registry. |
| Readiness, resource cost, implementation evidence, and release authorization change when Model Judgment affects consequential behavior. | Presentation development-contract material | Pattern and artifact | Active | The Thinking System Review owns delivery-level DoR, one canonical Constraint Realization Map, DoD, Release Gate, runtime evidence, and reassessment in one living artifact. |
| Placement classes should be demonstrable in isolated and composite systems without becoming a required topology. | Placement doctrine plus presentation synthesis | Reference Architecture | Active | `03-reference-architectures/judgment-placement-examples.md` provides non-prescriptive compositions linked to canonical doctrine and patterns. |
| A control architecture can be explained through Actuators, Constraints, Sensors, and Controller. | Presentation slide 12 reviewed against existing control-plane and control-theory material | Doctrine, AI Control Plane, patterns, failure modes, and repository structure | Active | [`00-doctrine/control-loop-anatomy.md`](../../00-doctrine/control-loop-anatomy.md) defines four logical capability families: Constraints and their realizations, Sensors and evidence, Controllers and decision authority, and Actuators and corrective action. The model is functional, not a mandatory physical stack. |
| Constraints require a distinct architectural category rather than remaining an unresolved subset of Actuators. | Slide 12 plus review of project, delivery, runtime, policy, schema, authority, and resource boundaries | Doctrine, glossary, and AI Control Plane | Active | The Constraints family is intentionally composite. Constraints are authoritative approved boundaries; Constraint Realizations implement, enforce, or influence them. Actuators execute authorized changes and may modify realizations within delegated authority. Constraint Realization is not a fifth capability family. |
| The slide's claim that removing any layer opens the loop is useful shorthand but not literally correct for Constraints. | Slide 12 metaphor reviewed against feedback-control semantics | Doctrine and research narrowing | Active | Sensing, decision, and effective actuation form the feedback path. Constraints define the space in which a loop operates. A loop may remain closed while unsafe or over-authorized when Constraints or credible realizations are missing. |
| Named tools can illustrate capabilities but do not define the taxonomy. | Slide 12 software mapping plus framework review | Doctrine and informative technical reference | Active | Prompt registries, schemas, HITL gateways, policy engines, evaluators, APIs, kill switches, and agent frameworks are classified by function, guarantee, evidence, authority, and corrective path. Literal product-to-layer mapping is rejected. |
| Eval Gate is not one indivisible Sensor function. | Slides 12 and 14 interpreted through the capability model | AI Control Plane | Active | Evaluation runner and metrics perform Sensor functions; logic selecting block/canary/release performs a Controller function; deployment, block, exposure change, or rollback execution performs an Actuator function. One product may package all three. |
| Constraints flow downward and become more concrete while runtime evidence flows upward. | Slide 12 structure metaphor combined with Nested Control Lifecycle and project/delivery inheritance | Doctrine, patterns, and artifacts | Active | Organizational Constraint sources are interpreted and extended at project level, realized and verified at delivery level, exercised at runtime, and reassessed at the decision level whose basis is invalidated. Constraint authority is inherited by reference; realization becomes concrete. |
| Hard and Soft Constraint language requires explicit scope and a complete realized path. | Cross-source synthesis of prompts, schemas, evaluators, permissions, and deterministic boundaries | Doctrine, glossary, AI Control Plane, patterns, and artifacts | Active | Hard or soft is a scoped claim about a Constraint and its complete realized path, not a property of policy prose. A Hard Constraint deterministically prevents or rejects violation within stated assumptions, subject, path, scope, and enforcement boundary. Different guarantee strengths require separate records. |
| Statistical quality, cost, latency, and capacity thresholds do not automatically become Hard Constraints. | Presentation tolerance and release-gate material combined with project/delivery review analysis | Doctrine, patterns, artifacts, and reference architecture | Active | Measured tolerances remain part of the Requirement and Operating Envelope unless a separate scoped realization deterministically enforces a specific boundary. The support-triage example separates hard per-request limits from aggregate cost and p95 latency evidence. |
| A model-mediated responsibility samples from a space of plausible outcomes; uncertainty is therefore produced inside the controlled system. | *Beyond Embeddings* plus the presentation opening and mathematical framing | Doctrine | Active | [`00-doctrine/uncertainty-in-the-controlled-object.md`](../../00-doctrine/uncertainty-in-the-controlled-object.md) defines the controlled-object shift and need for an additional control lifecycle. |
| Product uncertainty, operational uncertainty, and runtime-judgment uncertainty require related but different responses. | AI delivery lifecycle note, presentation process-shift material, and current doctrine | Doctrine | Active | UA complements product discovery, iterative delivery, Agile, DevOps, QA, security, and incident response; it does not replace them. |
| Feature delivery cannot answer whether a whole Thinking System project has a credible and viable control architecture. | *Beyond Embeddings*, lifecycle questions, and worked-review application | Doctrine, pattern, and artifact | Active | Project authorization is distinct from delivery release. The project review owns risk scenarios, Constraint architecture, capabilities, evidence, Human Authority, capacity, economics, authorization, inheritance, and reauthorization. |
| Some AI paths should not be built when critical violations cannot be bounded, detected, or contained, required authority is unavailable, or the control perimeter destroys the business case. | *Beyond Embeddings* and presentation architectural-veto material | Doctrine and pattern | Active | Architectural Veto and `AI path rejected / No-Go` are valid outcomes. No universal score or expected-value threshold is adopted. |
| Project risk should be translated into Constraints and control requirements rather than compressed into one score. | Cross-source synthesis | Pattern and artifact | Active | The project review uses scenario-based mapping across obligations, authority, consequence, detectability, latency, reversibility, propagation, required Constraints and capabilities, and residual decision effect. |
| Human review is control only when the reviewer has evidence, competence, time, capacity, independence, and real authority. | Control-theory operating-model argument and project/delivery synthesis | Pattern and process | Active | Project and delivery reviews test Human Authority and capacity explicitly. A nominal HITL gateway is insufficient. |
| The primary model-call cost is not the cost of controlling the system. | *Beyond Embeddings* control-tax argument and project viability synthesis | Pattern and artifact | Active | Control economics includes Constraint design and operation, evaluation, human review, false blocks, fallback load, latency, incident response, reassessment, and residual exposure. |
| Delivery reviews should inherit project Constraints rather than rediscover project-wide risk and economics for every change. | Nested lifecycle plus project/delivery synthesis | Pattern and artifact | Active | The project review produces a versioned authorization and Constraint baseline. The delivery review records one concrete realization map and references it from DoR, DoD, Release Gate, and runtime sections. |
| Production evidence can invalidate a local delivery decision or the project-level architecture. | Thinking System Review reassessment, worked support-triage review, and lifecycle production feedback | Doctrine and process | Active | UA distinguishes local delivery reassessment, project reauthorization, and organizational review according to the assumption, Constraint, capability, authority, or economic basis invalidated. |

## Conflict and evolution register

| Topic | Earlier or presentation formulation | Current UA formulation | Status | Resolution |
|---|---|---|---|---|
| Primary system category | Behavioral Software / Behavioral Applications | Thinking Systems | Active | Use Thinking Systems in current framework documents; preserve legacy wording in historical sources and provenance records. |
| Thinking System category versus control adequacy | Category definition bundled Model Judgment with already-explicit Constraints, evidence, decision rights, and corrective mechanisms | Category begins when at least one **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment; control completeness is evaluated separately | Active | This is a semantic compatibility change: inadequately controlled or pre-production applications may now satisfy category membership. UA controls address how that changed object becomes bounded, observable, correctable, governable, and production-ready. |
| Agentic label and orchestration topology | Agentic systems described as a higher-autonomy subset while largely linear agentic orchestration could be read as Linear Software | Fixed or dynamic topology does not determine the Linear Software / Thinking System distinction; Model Judgment may appear in either topology, while Thinking-System classification depends on whether at least one **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment | Narrowed | A predefined project-planning or other workflow is a Thinking System when at least one **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment. Autonomy, delegated authority, and the precise boundary of agentic terminology remain open. |
| Bug under stochastic business logic | A bug is a statistical excursion beyond approved business tolerances | A Bug is a violation of an approved Requirement | Active | Event, evidence, diagnosis, accepted residual behavior, and responsibility remain separate. |
| Requirement versus tolerance envelope | Requirement is the safe probabilistic operating area | Operating Envelope is part of a broader Requirement | Active | Preserve intended outcome, deterministic obligations, authority, Constraints, evidence, resources, and failure handling outside the envelope concept. |
| Statistical quality contract | Large-sample runs and confidence intervals prove readiness or completion | Evidence method and adequacy follow the Requirement and decision context | Active | No universal sample size, metric, confidence method, or threshold is adopted. Measured tolerances do not automatically become Hard Constraints. |
| Three connected AI planes | Intent UX → Cognitive Logic → Contextual Output | Input Interpretation, Decision Logic, and Output Mediation as optional, repeatable functions | Active | Treat the deck composition as illustrative rather than mandatory. |
| Three-part control model | Actuators, Sensors, and Controller; Constraints partly grouped under Actuators | Four capability families, with Constraints and their realizations as one composite family | Active | Constraint, Constraint Realization, Sensor, Controller, and Actuator remain distinct even though the first two form one family. |
| Slide 12 four-layer metaphor | Brain / nerves / skeleton / muscles as stacked layers | Four logical capability families with non-prescriptive topology | Active | Preserve the metaphor as source context; use Control-Loop Capability Anatomy as the canonical relationship model. |
| `Remove one layer and the loop opens` | Every layer presented as part of loop closure | Feedback closure distinguished from bounded control architecture | Active | Constraints define the loop's operating space; missing Constraints or realizations can leave a loop closed but unacceptable. |
| Slide 12 software mapping | Named tools assigned directly to layers | Function-based classification | Active | One tool may perform several functions or only part of one. |
| Constraint versus mechanism | Schemas and validators presented directly as Constraints | Constraint separated from Constraint Realization | Active | The approved boundary, mechanism, runtime state, evidence, decision, and change action remain distinguishable. |
| Hard versus Soft strength | Constraint or policy text labeled hard or soft in isolation | Scoped claim about the Constraint and complete realized path | Active | Different strengths across subject, path, or scope require separate records; mixed hard/soft rows are rejected. |
| Specialized role framing | PM, architect, QA, or specialist titles own parts of the loop | Responsibility bundles and decision authority | Active | Small teams may combine responsibilities; UA does not require job titles. |
| Delivery operational records | Separate readiness, completion, Constraint, risk, role, and release artifacts | One living Thinking System Review with one canonical realization map and linked evidence | Active | Additional records are optional only when independent ownership or lifecycle requires them. |
| Project operational records | Separate risk register, Constraint Register, control catalog, financial model, gate record, and responsibility matrix | One living Project Control Architecture and Viability Review | Active | The default SMB path uses one project artifact and linked evidence. |
| UA relative to delivery methods | AI shift may be read as replacing Scrum, Agile, DevOps, or SDLC | UA adds a control lifecycle for model-mediated behavior | Active | Distinguish the control problem by where uncertainty is produced. |
| One AI lifecycle | Discovery → engineering → evaluation → production | Organizational context → project authorization → delivery realization and release → runtime control and reassessment | Active | Preserve early lifecycle material as research; use the nested decision model in current framework content. |
| Every release is an experiment | Production release described as experimentation | Material release contains a controlled evidence-generating component within an approved Requirement and Constraint baseline | Active | Avoid language that excuses uncontrolled experimentation or weakens production obligations. |

## Remaining topics for synthesis and validation

- autonomy, delegated authority, and agentic terminology across fixed and dynamic Thinking-System workflows;
- Model Control Plane terminology versus Model Context Protocol acronym conflict;
- AI Control Plane capability-family model versus platform implementations;
- automated Controller logic versus socio-technical Controller;
- interactions, precedence, and conflicts among multiple Constraints;
- proportionality of project Constraint architecture for different SMB consequence levels;
- evidence needed to demonstrate realization effectiveness without overstating guarantees;
- methods for estimating control cost and residual exposure without false precision;
- validation through a two-level worked application;
- local reassessment versus project reauthorization in real incidents;
- organizational control context without creating a large governance layer;
- real-team usability and decision quality.

## Update rule

Entries should remain concise and decision-oriented. Detailed argument belongs in supporting analysis or synthesis documents.

Repository-wide terminology or methodology changes require deliberate framework review. A traceability entry alone does not activate a normative requirement.

Metadata and tags follow [`DOCUMENT-METADATA.md`](../../DOCUMENT-METADATA.md).
