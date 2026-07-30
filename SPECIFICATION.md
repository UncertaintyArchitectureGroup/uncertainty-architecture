---
title: Uncertainty Architecture Specification
artifact_type: specification-index
status: draft-normative
maturity: active
module: repository
topics:
  - thinking-systems
  - uncertainty-boundary
  - control-loop
  - conformance
tags:
  - ua/module/repository
  - ua/type/specification-index
  - ua/status/draft-normative
  - ua/topic/thinking-systems
  - ua/topic/uncertainty-boundary
  - ua/topic/conformance
canonical_for:
  - specification-boundary
  - document-status-model
  - conformance-model
---

# Uncertainty Architecture Specification

**Status:** Draft specification index  
**Version:** 0.x  
**License:** CC BY 4.0

## 1. Purpose

This document defines the normative boundary and document structure of Uncertainty Architecture (UA).

UA is an open specification for designing and governing **Thinking Systems**: software systems whose runtime behavior depends partly on probabilistic model judgment while consequential deterministic boundaries and control responsibilities remain explicit. Earlier UA publications used **Behavioral Software** and **Behavioral Applications** for this category.

UA treats reliability as a system property produced by explicit boundaries, observable behavior, feedback, decision rights, and controlled change rather than by model quality alone.

This file is the canonical entry point for the specification. It does not duplicate the detailed content of the modules it indexes.

## 2. Scope

The UA specification covers:

- the distinction between deterministic control logic and probabilistic judgment;
- functional placement of Model Judgment within a system or workflow;
- architectural boundaries around model-mediated behavior;
- control-loop capabilities for constraining, observing, evaluating, and recalibrating behavior;
- reusable technical and socio-technical patterns;
- recurring failure modes and anti-patterns;
- reference architectures that demonstrate possible compositions of the specification.

The specification does not prescribe:

- a particular model, vendor, framework, orchestration platform, or deployment topology;
- a mandatory pipeline of Input Interpretation, Decision Logic, and Output Mediation;
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

The metadata field `maturity` may describe lifecycle state within a status class, such as `draft`, `active`, `stable`, or `superseded`. It does not replace document status. See [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md).

## 5. Specification structure

### 5.1 Core doctrine

[`00-doctrine/`](00-doctrine/README.md) defines the foundational concepts and distinctions on which the rest of UA depends, including the functional placement taxonomy for Model Judgment.

[`00-doctrine/glossary.md`](00-doctrine/glossary.md) is the canonical vocabulary source for terms it currently defines. The glossary remains draft normative and may be refined through framework review.

Stable doctrine is expected to become normative; unfinished doctrine remains draft normative.

### 5.2 Patterns

[`01-patterns/`](01-patterns/README.md) contains reusable solutions for recurring technical and socio-technical control problems, including explicit boundaries around consequential Judgment Nodes.

Patterns may be normative or draft normative. Examples and compact records attached to a pattern are informative unless stated otherwise.

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

The project uses one canonical namespace for each supporting-material type:

- [`content/research/`](content/research/index.md) — research publications, notes, analyses, synthesis, and research-to-framework traceability;
- [`content/history/`](content/history/README.md) — project history, public evidence, and superseded process or decision records retained for traceability;
- [`content/raw/`](content/raw/README.md) — preserved source snapshots used to create normalized research editions;
- [`content/index.md`](content/index.md) — an informative publishing portal, not a specification or governance source;
- [`ROADMAP.md`](ROADMAP.md) — planned evolution of the project;
- [`CHANGELOG.md`](CHANGELOG.md) — repository-level record of material changes;
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution workflow, review expectations, and current maintainer authority;
- [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) — informative document metadata and controlled tag conventions;
- [`AGENTS.md`](AGENTS.md) — informative repository orientation and editing guidance for language models and automated agents.

The `quartz/` source tree and related Node configuration are publishing infrastructure. They do not define UA concepts, requirements, governance, or conformance.

There is no active root-level research namespace or mandatory RFC namespace. Working research belongs under `content/research/`. Substantial framework proposals use a branch and pull request under [`CONTRIBUTING.md`](CONTRIBUTING.md); a formal RFC namespace may be introduced later only through an explicit project decision.

Content enters the normative specification only through an explicit framework decision and a corresponding status change.

Metadata, tags, publishing placement, recency, external attention, or agent-generated summaries do not change normative authority.

## 7. Conformance

UA conformance is currently defined at the level of explicit architectural reasoning rather than product certification.

A system or design claiming alignment with UA SHOULD be able to identify:

1. where materially consequential Model Judgment occurs;
2. whether each identified Judgment Node performs Input Interpretation, Decision Logic, Output Mediation, or a combination;
3. which inputs and approved context each node receives;
4. which outputs, decisions, paths, or actions each node can change;
5. which authority each node possesses;
6. which deterministic boundaries and invariants constrain it;
7. how relevant behavior and outcomes are observed and evaluated against risk-derived expectations;
8. who or what may authorize corrective action and how escalation, containment, fallback, rollback, or shutdown occurs;
9. how decisions, assumptions, dependencies, and changes remain traceable.

The placement classes are a functional taxonomy, not a mandatory pipeline. A node may combine functions, and a workflow may omit or repeat any class.

A claim of UA alignment MUST NOT imply certification, endorsement, or complete conformance unless the project later establishes a formal conformance program.

## 8. Change control

Normative and draft normative changes SHOULD be:

- scoped to one coherent architectural decision;
- reviewable through a visible change set;
- linked to relevant research, operational evidence, or design rationale;
- explicit about compatibility, supersession, and unresolved uncertainty;
- reflected in the appropriate module index and changelog when material.

Research findings, talks, articles, implementations, and external frameworks do not modify the specification by implication. Adoption requires an explicit normative decision following the current contribution and review workflow.

## 9. Current maturity

UA is in active development. The repository contains a conceptual spine, normalized module entry points, a canonical draft glossary, a Model Judgment placement taxonomy, an initial Judgment Node boundary pattern, a control-plane model, reference material, and failure-mode work, but detailed normative content remains incomplete and may change.

Readers SHOULD follow the explicit status declared by each module or document. Reference architectures and clearly identified examples remain **reference** or **informative**, not mandatory implementation requirements.
