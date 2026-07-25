# Uncertainty Architecture Specification

**Status:** Draft specification index  
**Version:** 0.x  
**License:** CC BY 4.0

## 1. Purpose

This document defines the normative boundary and document structure of Uncertainty Architecture (UA).

UA is an open specification for designing and governing software systems whose runtime behavior depends partly on probabilistic models. It treats reliability as a system property produced by explicit boundaries, observable behavior, feedback, decision rights, and controlled change rather than by model quality alone.

This file is the canonical entry point for the specification. It does not duplicate the detailed content of the modules it indexes.

## 2. Scope

The UA specification covers:

- the distinction between deterministic control logic and probabilistic judgment;
- architectural boundaries around model-mediated behavior;
- control-loop capabilities for constraining, observing, evaluating, and recalibrating behavior;
- reusable technical and socio-technical patterns;
- recurring failure modes and anti-patterns;
- reference architectures that demonstrate possible compositions of the specification.

The specification does not prescribe:

- a particular model, vendor, framework, orchestration platform, or deployment topology;
- universal numerical thresholds for quality, risk, latency, cost, or autonomy;
- mandatory job titles or a single organizational structure;
- identical controls for every AI system;
- any reference implementation as the standard itself.

Controls and evidence should be proportional to consequences, uncertainty, autonomy, reversibility, and operating context.

## 3. Normative language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL**, when written in uppercase, indicate the strength of a requirement.

Examples, explanations, and rationale are informative unless explicitly stated otherwise.

## 4. Document status model

Every specification document SHOULD declare one of the following statuses:

- **Normative** — accepted specification content defining requirements, concepts, interfaces, responsibilities, or conformance expectations.
- **Draft normative** — proposed specification content under active development. It may change and MUST NOT be represented as stable.
- **Informative** — explanation, rationale, guidance, or example that supports the specification without creating requirements.
- **Reference** — a concrete architecture or implementation demonstrating one possible application of UA. It is not the standard itself.
- **Research** — source material, analysis, or synthesis that may inform future specification changes but is not automatically normative.
- **Historical** — superseded or archival material retained for traceability.

A directory name does not by itself determine status. The explicit status in the document or its module index takes precedence.

## 5. Specification structure

### 5.1 Core doctrine

[`00-doctrine/`](00-doctrine/README.md) defines the foundational concepts and distinctions on which the rest of UA depends.

Stable doctrine is expected to become normative; unfinished doctrine remains draft normative.

### 5.2 Patterns

[`01-patterns/`](01-patterns/README.md) contains reusable solutions for recurring technical and socio-technical control problems.

Patterns may be normative or draft normative. Examples attached to a pattern are informative unless stated otherwise.

### 5.3 AI Control Plane

[`02-ai-control-plane/`](02-ai-control-plane/README.md) defines the capabilities required to constrain, observe, evaluate, and adjust model-mediated behavior.

The control plane is an architectural capability model, not necessarily a standalone product or infrastructure layer. Implementations MAY distribute its responsibilities across application code, platform services, human workflows, and governance processes.

### 5.4 Reference architectures

[`03-reference-architectures/`](03-reference-architectures/README.md) contains concrete compositions showing how UA concepts and patterns may be applied.

Reference architectures MUST NOT be treated as mandatory implementation topologies unless a separate normative document explicitly adopts a requirement they illustrate.

### 5.5 Failure modes

[`04-failure-modes/`](04-failure-modes/README.md) records recurring mechanisms by which AI-integrated systems lose structural, semantic, operational, or organizational control.

A taxonomy may be normative; individual examples and post-mortems are normally informative.

## 6. Supporting material outside the specification

The following repository areas support the project but are not automatically part of the normative specification:

- [`content/research/`](content/research/index.md) — publications, analyses, synthesis, and research-to-framework traceability;
- `content/history/` — project history and archival records;
- `research/` — working research material pending consolidation or explicit classification;
- `rfcs/` — formal proposals when the project chooses to use an RFC process;
- [`ROADMAP.md`](ROADMAP.md) — planned evolution of the project;
- [`CHANGELOG.md`](CHANGELOG.md) — repository-level record of material changes;
- [`GOVERNANCE.md`](GOVERNANCE.md) — decision authority and project governance;
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution workflow.

Content enters the normative specification only through an explicit project decision and a corresponding status change.

## 7. Conformance

UA conformance is currently defined at the level of explicit architectural reasoning rather than product certification.

A system or design claiming alignment with UA SHOULD be able to identify:

1. where probabilistic judgment occurs;
2. which deterministic boundaries and invariants constrain it;
3. how relevant behavior and outcomes are observed;
4. how evidence is evaluated against risk-derived expectations;
5. who or what may change system behavior;
6. how escalation, containment, rollback, or shutdown occurs;
7. how decisions, assumptions, and changes remain traceable.

A claim of UA alignment MUST NOT imply certification, endorsement, or complete conformance unless the project later establishes a formal conformance program.

## 8. Change control

Normative and draft normative changes SHOULD be:

- scoped to one coherent architectural decision;
- reviewable through a visible change set;
- linked to relevant research, operational evidence, or design rationale;
- explicit about compatibility, supersession, and unresolved uncertainty;
- reflected in the appropriate module index and changelog when material.

Research findings, talks, articles, implementations, and external frameworks do not modify the specification by implication. Adoption requires an explicit normative decision under project governance.

## 9. Current maturity

UA is in active development. The repository already contains a conceptual spine, patterns, a control-plane model, reference material, and failure-mode work, but these areas are not yet uniformly classified or complete.

Until module-level status declarations are normalized, readers SHOULD treat existing specification modules as **draft normative**, except for reference architectures and clearly identified examples, which are **reference** or **informative**.
