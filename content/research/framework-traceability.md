---
title: Research-to-Framework Traceability
artifact_type: research-traceability
status: research
maturity: active
module: research
topics:
  - provenance
  - thinking-systems
  - repository-architecture
tags:
  - ua/module/research
  - ua/type/research-traceability
  - ua/status/research
  - ua/topic/provenance
created: 2026-07-24
updated: 2026-07-31
license: CC-BY-4.0
---

# Research-to-Framework Traceability

## Purpose

This document records how UA research influences framework components without treating every historical statement as an approved requirement.

It prevents two opposite errors:

1. building methodology without preserving the research and reasoning behind it;
2. treating every statement from an article, talk, or working note as if it were already normative.

Traceability is a synthesis aid, not a mandatory ledger for every source or sentence.

This matrix is the canonical repository record for material source-to-framework decisions. Do not create a parallel crystallization ledger elsewhere; detailed argument belongs in supporting analysis, synthesis, or source-intake notes.

## Status vocabulary

- **Research Finding** — a conclusion preserved from research material.
- **Candidate** — potentially suitable for translation into a framework component.
- **Needs Resolution** — terminology, evidence, scope, or contradiction must be resolved first.
- **Proposed for Framework Review** — mature enough for a separate, deliberate normative proposal and visible review.
- **Active** — accepted into the current framework boundary, subject to the status of the owning document.
- **Superseded** — replaced by a later formulation.
- **Rejected** — considered and intentionally not adopted.

## Candidate framework areas

Traceability entries may point toward:

- **Doctrine** — foundational concepts and distinctions;
- **Pattern** — repeatable technical or socio-technical solution;
- **AI Control Plane capability** — reusable sensing, constraint, controller, authority, or corrective-action capability;
- **Reference Architecture** — concrete composition of multiple patterns;
- **Artifact** — canvas, checklist, registry, evidence record, risk map, or other reusable tool;
- **Responsibility or process** — reusable decision right, review, escalation, lifecycle, or operating responsibility;
- **Failure Mode** — recurring mechanism of technical, semantic, operational, economic, or organizational failure.

Lifecycle and operating-model concerns may be represented across these areas rather than maintained as a separate top-level specification module unless the framework later adopts one explicitly.

## Traceability matrix

The historical publication corpus is preserved, while corpus-level synthesis remains in progress. The entries below record explicit source-to-framework decisions already made through reviewed pull requests.

| Research finding or source claim | Source or synthesis | Framework area | Status | Current framework decision |
|---|---|---|---|---|
| Model-mediated runtime behavior has non-zero variance, so system design must distinguish deterministic responsibilities, model-mediated responsibilities, and the boundaries and controls between them. | Original *Designing Non-Deterministic Systems* PPTX, slides 1–6 transfer scope, refined through framework review | Doctrine | Active | Thinking Systems are mixed systems; deterministic obligations remain explicit while Model Judgment is bounded and evaluated through system-level Requirements. |
| Correctness cannot always be represented by one exact output, and requirements must define acceptable operating space. | Original PPTX, requirement and tolerance material, refined through framework review | Doctrine and glossary | Active | A Requirement is the approved operating contract; the Operating Envelope is one part of it; Correctness is satisfaction of the Requirement. |
| A stochastic defect should be reasoned about through business tolerances and observed behavior rather than code-path failure alone. | Original PPTX bug material, refined through framework review | Doctrine and glossary | Active | A Bug is a system-level Requirement violation. A tail event, metric change, or Deviation Signal is evidence until diagnosis establishes the violation and its source. |
| Model Judgment creates value in input interpretation, dynamic decision logic, and contextual output. | Original PPTX architectural-space material, refined into current terminology | Doctrine | Active | Input Interpretation, Decision Logic, and Output Mediation are functional placement classes, not a mandatory three-stage pipeline. |
| Consequential Model Judgment requires an explicit boundary around purpose, context, authority, deterministic constraints, evidence, failure handling, and ownership. | Presentation control framing plus framework synthesis | Pattern | Active | The Judgment Node Boundary pattern provides proportional minimal and extended boundary modes without requiring a separate node registry. |
| Readiness, resource cost, completion evidence, and release authorization must change together when Model Judgment affects consequential behavior. | Original PPTX development-contract material, narrowed through framework review | Pattern and artifact | Active | The Thinking System Review owns full model-mediated DoR and DoD extensions, keeps the delivery Release Gate distinct, uses responsibility bundles rather than job titles, and records the decision in one living template. |
| Placement classes should be demonstrable in isolated and composite systems without becoming a required topology. | Placement doctrine plus slides 1–6 transfer synthesis | Reference Architecture | Active | `03-reference-architectures/judgment-placement-examples.md` shows four non-prescriptive compositions and links back to canonical doctrine and patterns. |
| A model-mediated responsibility samples from a space of plausible outcomes; uncertainty is therefore produced inside the system being controlled rather than existing only in requirements, users, or infrastructure. | *Beyond Embeddings* chapters 1–2 plus the original PPTX opening and mathematical-fact sections | Doctrine | Active | [`00-doctrine/uncertainty-in-the-controlled-object.md`](../../00-doctrine/uncertainty-in-the-controlled-object.md) defines the controlled-object shift and explains why UA requires an additional control lifecycle. |
| Product uncertainty, operational uncertainty, and runtime-judgment uncertainty require related but different feedback and control responses. | Cross-source synthesis of the AI delivery lifecycle note, original PPTX process-shift material, and current UA doctrine | Doctrine | Active | UA complements plan-driven analysis, iterative delivery, Agile, DevOps, QA, security, and incident response; it does not replace them. Its distinctive concern is consequential uncertainty produced through runtime Model Judgment. |
| Delivery-level work cannot answer whether a whole Thinking System project has a credible control architecture or viable risk-control economics. | *Beyond Embeddings* control-tax, drift-planning, and no-go argument; AI Delivery Lifecycle discovery question; worked-review application | Doctrine, pattern, and artifact | Active | Project authorization is distinct from delivery release. [`01-patterns/project-control-architecture-and-viability-review.md`](../../01-patterns/project-control-architecture-and-viability-review.md) operationalizes material risk scenarios, intended Judgment and authority, required controls, evidence feasibility, Human Authority, operational capacity, control economics, authorization, inheritance, and reauthorization through one project-level review and template. |
| Some AI paths should not be built when critical violations cannot be detected or contained, required Human Authority is unavailable, or the control perimeter destroys the business case. | *Beyond Embeddings* chapters 1–2 and original PPTX architectural-veto material | Doctrine, pattern, and artifact | Active | Architectural veto is a valid project-review outcome. The project pattern separates hard prohibitions and unavailable controls from optional expected-value reasoning; no universal score, formula, role owner, or veto threshold is adopted. |
| Project risk should be represented through material scenarios connected to controls rather than compressed into one universal score. | *Beyond Embeddings* risk-control coupling, presentation risk-space framing, and framework synthesis | Pattern and artifact | Active | The project review maps affected obligations, mechanisms, authority, consequence, detectability, feedback latency, reversibility, propagation, required controls, Human Authority, and residual risk. Local scales are allowed but cannot replace scenario and decision rationale. |
| Human review is a control only when people have sufficient competence, context, time, capacity, independence, and intervention authority. | *Beyond Embeddings* containment discussion, support-triage worked review, and framework synthesis | Pattern and responsibility | Active | The project review tests Human Authority and operational capacity before authorization; the delivery review verifies that the local implementation remains consistent with that inherited capacity assumption. |
| The cost of the primary model call understates the cost of controlling a Thinking System. | *Beyond Embeddings* Control Tax and expected-net-value argument, plus delivery-review resource findings | Pattern and artifact | Active | The project review includes one-time control cost, recurring control and operating cost, residual exposure, benefit assumptions, sensitivity, non-AI alternatives, and hard vetoes. The optional expected-value formula is a decision aid rather than a conformance requirement. |
| Project decisions and delivery decisions require separate records but should not duplicate the same reasoning. | Controlled-object doctrine, AI Delivery Lifecycle note, repository artifact-minimization rule, and framework synthesis | Pattern and artifact | Active | One living project review produces a versioned inheritance package; one living delivery review links that version and refines local Judgment Nodes, Requirements, evidence, and release scope. Separate Project Launch Gate and Release Decision Record files are not required. |
| Production evidence can invalidate delivery assumptions or the project-level control architecture. | Thinking System Review reassessment, worked support-triage review, AI Delivery Lifecycle production-feedback section, and framework synthesis | Doctrine, pattern, and process | Active | UA distinguishes local delivery reassessment, project reauthorization, and organizational review. The level follows the assumption invalidated by evidence. A material model-mediated release is bounded evidence-generating operation, not uncontrolled experimentation. |

## Conflict and evolution register

This section records cross-source issues that required an explicit resolution rather than silent editorial normalization.

| Topic | Earlier or presentation formulation | Current UA formulation | Current status | Resolution |
|---|---|---|---|---|
| Primary system category | Behavioral Software / Behavioral Applications | Thinking Systems | Active | Use Thinking Systems in current framework documents; preserve legacy wording in historical sources and provenance records. |
| Bug under stochastic business logic | A bug is a statistical excursion beyond approved business tolerances | A Bug is a violation of an approved Requirement; a statistically evidenced tolerance excursion may establish that violation when the tolerance is part of the Requirement | Active | Event, evidence, diagnosis, accepted residual behavior, and system responsibility remain separate. |
| Requirement versus tolerance envelope | Requirement is the safe probabilistic operating area | The Operating Envelope is part of a broader Requirement | Active | Preserve intended outcome, deterministic obligations, authority, evidence expectations, resource constraints, and failure handling outside the envelope concept. |
| Statistical quality contract | Large-sample runs, fixed metrics, and confidence intervals prove readiness or completion | Evidence method and adequacy are derived from the Requirement and decision context | Active | No universal sample size, metric, confidence method, or threshold is adopted. Deterministic and behavioral evidence coexist. |
| Three connected AI planes | Intent UX → Cognitive Logic → Contextual Output | Input Interpretation, Decision Logic, and Output Mediation as optional, repeatable, combinable functions | Active | Treat the deck composition as illustrative rather than a mandatory pipeline. |
| Specialized role framing | PM, architect, QA, or other specialist titles own parts of the loop | Project and delivery responsibility bundles identify required decision rights without mandatory titles | Active | Small teams may combine responsibilities; project authorization and delivery release authority remain explicit. |
| Operational records | Separate readiness, completion, risk, role, financial, project-gate, and release artifacts | One living project review plus one living delivery review, each with versioned snapshots and distinct ownership | Active | Organizational sources and supporting evidence are linked. Project context flows downward through an inheritance package; lower-level evidence flows upward only when it invalidates a higher-level assumption. |
| UA relative to delivery methods | The AI shift may be read as requiring a replacement for Scrum, Agile, DevOps, or the existing SDLC | UA adds a control lifecycle for model-mediated behavior and integrates with existing product, delivery, operations, quality, security, and incident practices | Active | Distinguish the control problem by where uncertainty is produced. Do not present UA as a universal successor methodology. |
| One AI lifecycle | Discovery → engineering → evaluation → production as one illustrative loop | Organizational context → project authorization → delivery-level review → runtime control and reauthorization as nested levels | Active | Retain the early four-phase lifecycle as research. Use separate project and delivery patterns and route runtime evidence to the level whose assumption changed. |
| Risk representation | A digital risk space or aggregate score may appear to be the central risk artifact | Material risk scenarios connected to controls, evidence, authority, capacity, economics, and decision effects | Active | Teams may use defined local scales, but no combined score can replace hard prohibitions, scenario detail, control feasibility, or decision rationale. |
| Every release is an experiment | Production release may be described as experimentation because the real user distribution cannot be reproduced | Every material model-mediated release contains a controlled evidence-generating component while remaining bound by an approved Requirement, project authorization, deployment scope, and corrective path | Active | Avoid language that excuses uncontrolled experimentation or weakens production obligations. |

## Remaining topics for synthesis and application

Topics still expected to require further review include:

- the relationship between Thinking Systems and agentic systems at different autonomy levels;
- Model Control Plane terminology versus Model Context Protocol acronym conflict;
- AI Control Plane as capability model versus possible platform implementations;
- actuators versus constraints as separate control categories;
- automated controller logic versus the socio-technical controller;
- usability of the project review and inheritance package in a two-level worked application and real team;
- practical completeness of material risk scenarios without governance overload or false precision;
- derivation of tolerances from authority, consequence, detectability, reversibility, propagation, exposure, and operational capacity;
- deeper control-economics methods, uncertainty ranges, sensitivity analysis, and maintenance-cost estimation;
- evidence for deciding whether Human Authority is substantive rather than ceremonial;
- boundaries between local delivery reassessment, project reauthorization, and organizational review in real incidents;
- failure-mode taxonomy and the evidence needed to distinguish drift, defects, attacks, invalid Requirements, control-capacity failure, and economic non-viability;
- simplification opportunities revealed by two-level and real-team application.

## Update rule

A research change may add findings and conflicts supported by a single source, multiple sources, a research note, or an explicit synthesis.

Entries should remain concise and decision-oriented. Detailed argument belongs in supporting analysis or synthesis documents.

Repository-wide terminology or methodology changes require separate deliberate framework review. A traceability entry alone does not activate a normative requirement.

Metadata and tags follow [`DOCUMENT-METADATA.md`](../../DOCUMENT-METADATA.md).
