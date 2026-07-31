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
updated: 2026-07-31
license: CC-BY-4.0
---

# Research-to-Framework Traceability

## Purpose

This document records how UA research influences framework components without treating every historical statement as an approved requirement.

It prevents two opposite errors:

1. building methodology without preserving the research and reasoning behind it;
2. treating every statement from an article, talk, presentation, or working note as if it were already normative.

Traceability is a synthesis aid, not a mandatory ledger for every source or sentence. This matrix is the canonical repository record for material source-to-framework decisions.

## Status vocabulary

- **Research Finding** — a conclusion preserved from research material.
- **Candidate** — potentially suitable for translation into a framework component.
- **Needs Resolution** — terminology, evidence, scope, or contradiction must be resolved first.
- **Proposed for Framework Review** — mature enough for a deliberate normative proposal and visible review.
- **Active** — accepted into the current framework boundary, subject to the status of the owning document.
- **Superseded** — replaced by a later formulation.
- **Rejected** — considered and intentionally not adopted.

## Candidate framework areas

Traceability entries may point toward Doctrine, Pattern, AI Control Plane capability, Reference Architecture, Artifact, responsibility or process, and Failure Mode.

Lifecycle and operating-model concerns may be represented across these areas rather than maintained as a separate top-level specification module unless the framework later adopts one explicitly.

## Traceability matrix

| Research finding or source claim | Source or synthesis | Framework area | Status | Current framework decision |
|---|---|---|---|---|
| Model-mediated runtime behavior has non-zero variance, so system design must distinguish deterministic responsibilities, model-mediated responsibilities, and the boundaries and controls between them. | Original *Designing Non-Deterministic Systems* PPTX, slides 1–6 transfer scope, refined through framework review | Doctrine | Active | Thinking Systems are mixed systems; deterministic obligations remain explicit while Model Judgment is bounded and evaluated through system-level Requirements. |
| Correctness cannot always be represented by one exact output, and Requirements must define acceptable operating space. | Original PPTX requirement and tolerance material | Doctrine and glossary | Active | A Requirement is the approved operating contract; the Operating Envelope is one part of it; Correctness is satisfaction of the Requirement. |
| A stochastic defect should be reasoned about through business tolerances and observed behavior rather than code-path failure alone. | Original PPTX bug material | Doctrine and glossary | Active | A Bug is a system-level Requirement violation. A tail event, metric change, or Deviation Signal is evidence until diagnosis establishes the violation and its source. |
| Model Judgment creates value in input interpretation, dynamic decision logic, and contextual output. | Original PPTX architectural-space material | Doctrine | Active | Input Interpretation, Decision Logic, and Output Mediation are functional placement classes, not a mandatory three-stage pipeline. |
| Consequential Model Judgment requires an explicit boundary around purpose, context, authority, deterministic Constraints, evidence, failure handling, and ownership. | Presentation control framing plus framework synthesis | Pattern | Active | The Judgment Node Boundary provides proportional minimal and extended modes including applicable Constraint source, realization, evidence, fallback, and change authority without requiring a separate node registry. |
| Readiness, resource cost, completion evidence, and release authorization must change together when Model Judgment affects consequential behavior. | Original PPTX development-contract material | Pattern and artifact | Active | The Thinking System Review owns delivery-level DoR, concrete Constraint realization, DoD, Release Gate, runtime enforcement, and reassessment in one living template. |
| Placement classes should be demonstrable in isolated and composite systems without becoming a required topology. | Placement doctrine plus slides 1–6 synthesis | Reference Architecture | Active | `03-reference-architectures/judgment-placement-examples.md` shows four non-prescriptive compositions and links back to canonical doctrine and patterns. |
| A control system can be explained through Actuators, Constraints, Sensors, and Controller. | Original *Designing Non-Deterministic Systems* PPTX, slide 12, reviewed against existing AI Control Plane and control-theory material | Doctrine, AI Control Plane, patterns, failure modes, and repository structure | Active | [`00-doctrine/control-loop-anatomy.md`](../../00-doctrine/control-loop-anatomy.md) defines four logical capability classes: Constraints bound the operating space; Sensors produce evidence; Controllers interpret and authorize; Actuators execute authorized change. The model is functional, not a mandatory physical stack. |
| Constraints need a distinct architectural category rather than remaining an unresolved subset of Actuators. | Slide 12 plus review of project, delivery, runtime, policy, schema, authority, and resource boundaries | Doctrine, glossary, and AI Control Plane | Active | Constraints are first-class capabilities with source, subject, scope, hard or soft strength, realization, failure behavior, evidence, and change authority. Actuators may modify Constraints but do not subsume them. |
| Named tools can illustrate control capabilities but do not define the taxonomy. | Slide 12 software mapping plus framework review | Doctrine and informative technical reference | Active | Prompt registries, semantic monitors, schemas, HITL gateways, kill switches, APIs, policy engines, and agent frameworks are classified by function, guarantee, evidence, authority, and corrective path. Literal product-to-layer mapping was rejected. |
| Constraints flow downward and become more concrete while runtime evidence flows upward. | Slide 12 structure metaphor combined with Nested Control Lifecycle, project/delivery inheritance, and control-theory synthesis | Doctrine, patterns, and artifacts | Active | Organizational Constraint sources are interpreted and extended at project level, realized and verified at delivery level, enforced and evidenced at runtime, and reassessed at the decision level whose basis is invalidated. |
| A model-mediated responsibility samples from a space of plausible outcomes; uncertainty is therefore produced inside the controlled system rather than existing only in requirements, users, or infrastructure. | *Beyond Embeddings* chapters 1–2 plus the original PPTX opening and mathematical framing | Doctrine | Active | [`00-doctrine/uncertainty-in-the-controlled-object.md`](../../00-doctrine/uncertainty-in-the-controlled-object.md) defines the controlled-object shift and the need for an additional control lifecycle. |
| Product uncertainty, operational uncertainty, and runtime-judgment uncertainty require related but different feedback and control responses. | AI delivery lifecycle note, original PPTX process-shift material, and current doctrine | Doctrine | Active | UA complements plan-driven analysis, iterative delivery, Agile, DevOps, QA, security, and incident response; it does not replace them. |
| Feature or change delivery cannot answer whether a whole Thinking System project has a credible control architecture or viable risk-control economics. | *Beyond Embeddings* control-tax, drift-planning, and No-Go argument; AI Delivery Lifecycle discovery question; worked-review application | Doctrine, pattern, and artifact | Active | Project authorization is distinct from delivery release. The project review operationalizes risk scenarios, Constraint architecture, intended authority, required capabilities, evidence, Human Authority, capacity, economics, authorization, inheritance, and reauthorization. |
| Some AI paths should not be built when critical violations cannot be constrained, detected, or contained, required Human Authority is unavailable, or the control perimeter destroys the business case. | *Beyond Embeddings* chapters 1–2 and original PPTX architectural-veto material | Doctrine and pattern | Active | Architectural veto and `AI path rejected / No-Go` are valid outcomes. No universal expected-value formula, risk score, or veto threshold is adopted; hard prohibitions cannot be averaged away. |
| Project risk should be translated into Constraints and control requirements rather than compressed into one score. | Cross-source synthesis of *Beyond Embeddings*, control-theory material, and project-level lifecycle questions | Pattern and artifact | Active | The project review uses scenario-based mapping across affected obligations, authority, consequence, detectability, feedback latency, reversibility, propagation, required Constraints and capabilities, and residual decision effect. |
| Human review is only a control when the reviewer has evidence, competence, time, capacity, independence, and real authority to reject or intervene. | Control-theory operating-model argument, lifecycle note, worked support review, and project-level synthesis | Pattern and process | Active | The project and delivery reviews test Human Authority and capacity explicitly. A nominal HITL gateway is insufficient when intervention is ceremonial or operationally impossible. |
| The cost of the primary model call is not the cost of controlling the system. | *Beyond Embeddings* control-tax argument and project viability synthesis | Pattern and artifact | Active | Control economics includes Constraint design and operation, evaluation, human review, false blocks, fallback load, latency, incident response, reassessment, and residual exposure. Expected-value formulas remain optional decision aids. |
| Delivery reviews should inherit project Constraints rather than rediscover project-wide risk and economics for every change. | Nested-lifecycle doctrine plus project/delivery synthesis | Pattern and artifact | Active | The project review produces a versioned authorization and Constraint inheritance package. The delivery review records concrete realization and may narrow but must not silently expand authority or weaken inherited hard Constraints. |
| Production evidence can invalidate a local delivery decision or the project-level Constraint and control architecture. | Thinking System Review reassessment, worked support-triage review, AI Delivery Lifecycle production-feedback section | Doctrine and process | Active | UA distinguishes local delivery reassessment, project reauthorization, and organizational review according to the assumption, Constraint, capability, authority, or economic basis invalidated. |

## Conflict and evolution register

| Topic | Earlier or presentation formulation | Current UA formulation | Current status | Resolution |
|---|---|---|---|---|
| Primary system category | Behavioral Software / Behavioral Applications | Thinking Systems | Active | Use Thinking Systems in current framework documents; preserve legacy wording in historical sources and provenance records. |
| Bug under stochastic business logic | A bug is a statistical excursion beyond approved business tolerances | A Bug is a violation of an approved Requirement | Active | Event, evidence, diagnosis, accepted residual behavior, and system responsibility remain separate. |
| Requirement versus tolerance envelope | Requirement is the safe probabilistic operating area | The Operating Envelope is part of a broader Requirement | Active | Preserve intended outcome, deterministic obligations, authority, Constraints, evidence expectations, resource limits, and failure handling outside the envelope concept. |
| Statistical quality contract | Large-sample runs, fixed metrics, and confidence intervals prove readiness or completion | Evidence method and adequacy are derived from the Requirement and decision context | Active | No universal sample size, metric, confidence method, or threshold is adopted. |
| Three connected AI planes | Intent UX → Cognitive Logic → Contextual Output | Input Interpretation, Decision Logic, and Output Mediation as optional, repeatable, combinable functions | Active | Treat the deck composition as illustrative rather than a mandatory pipeline. |
| Three-part control model in early repository wording | Actuators, Sensors, and Controller; Constraints partly grouped under Actuators | Constraints, Sensors, Controllers, and Actuators as four logical capabilities | Active | Constraints now have a separate canonical category and capability area. Actuators execute authorized change and may modify Constraints within delegated authority. |
| Slide 12 four-layer metaphor | Brain / nerves / skeleton / muscles as stacked layers | Four logical capabilities with non-prescriptive topology | Active | Preserve the metaphor as explanatory source context; use the Control-Loop Capability Anatomy as the canonical relation model. |
| Slide 12 software mapping | Named tools assigned directly to layers | Function-based classification | Active | A tool may realize several capabilities or only part of one. Classification follows function, guarantee, evidence, authority, and corrective path. |
| Specialized role framing | PM, architect, QA, or other specialist titles own parts of the loop | Explicit responsibility bundles and decision authority | Active | Small teams may combine responsibilities; the framework does not require job titles. |
| Delivery operational records | Separate readiness, completion, Constraint, risk, role, and release artifacts | One living Thinking System Review plus linked evidence and versioned snapshots | Active | Additional records are optional only where independent ownership or lifecycle requires them. |
| Project operational records | Separate risk register, Constraint Register, control catalog, financial model, gate record, and responsibility matrix | One living Project Control Architecture and Viability Review linking authoritative sources and evidence | Active | The default SMB path uses one project artifact and decision history; supporting systems remain linked rather than duplicated. |
| UA relative to delivery methods | The AI shift may be read as requiring replacement of Scrum, Agile, DevOps, or the SDLC | UA adds a control lifecycle for model-mediated behavior | Active | Distinguish the control problem by where uncertainty is produced. Do not present UA as a universal successor methodology. |
| One AI lifecycle | Discovery → engineering → evaluation → production as one illustrative loop | Organizational context → project authorization → delivery realization and release → runtime control and reauthorization | Active | Retain the early lifecycle as research. Use the nested distinction to separate project viability, delivery release, local correction, and reauthorization. |
| Every release is an experiment | Production release described as experimentation because the full user distribution cannot be reproduced | Material model-mediated release contains a controlled evidence-generating component while remaining bound by an approved Requirement and Constraint baseline | Active | Avoid language that excuses uncontrolled experimentation or weakens production obligations. |

## Remaining topics for synthesis and validation

- the relationship between Thinking Systems and agentic systems at different autonomy levels;
- Model Control Plane terminology versus Model Context Protocol acronym conflict;
- AI Control Plane capability model versus possible platform implementations;
- automated Controller logic versus the socio-technical Controller;
- interactions, conflicts, and precedence among multiple Constraints;
- practical proportionality of project Constraint architecture for different SMB consequence levels;
- evidence needed to demonstrate Constraint effectiveness without overstating guarantees;
- methods for estimating control cost and residual exposure without false precision;
- validation of Constraint inheritance and realization through a two-level worked application;
- local reassessment versus project reauthorization in real incidents and material changes;
- organizational control context as authoritative inputs and shared capabilities without creating a large governance layer;
- failure-mode and incident evidence distinguishing drift, defects, attacks, invalid Requirements, Constraint failure, control-capacity failure, and economic non-viability;
- real-team usability and decision quality.

## Update rule

Entries should remain concise and decision-oriented. Detailed argument belongs in supporting analysis or synthesis documents.

Repository-wide terminology or methodology changes require separate deliberate framework review. A traceability entry alone does not activate a normative requirement.

Metadata and tags follow [`DOCUMENT-METADATA.md`](../../DOCUMENT-METADATA.md).
