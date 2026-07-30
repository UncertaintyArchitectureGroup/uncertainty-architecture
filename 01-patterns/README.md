---
title: Interface and Control Patterns
artifact_type: pattern-index
status: draft-normative
maturity: active
module: patterns
topics:
  - model-judgment
  - uncertainty-boundary
  - containment
  - fallback
  - escalation
tags:
  - ua/module/patterns
  - ua/type/pattern-index
  - ua/status/draft-normative
  - ua/topic/model-judgment
  - ua/topic/uncertainty-boundary
  - ua/topic/containment
  - ua/topic/fallback
  - ua/topic/escalation
canonical_for:
  - patterns-module
---

# Interface and Control Patterns

**Status:** Draft normative  
**Role:** Reusable architectural responses for recurring control problems

## Purpose

This module contains reusable patterns for engineering the boundary between deterministic software responsibilities and probabilistic Model Judgment in Thinking Systems.

Patterns turn UA doctrine into reviewable design choices. They describe where uncertainty may enter a workflow, how it is bounded, what evidence is produced, and how failure is contained or escalated.

## Defines

This module defines or develops patterns for:

- separating Judgment Nodes from deterministic control logic;
- making a Judgment Node's purpose, inputs, authority, constraints, evidence, failure handling, and ownership explicit;
- preserving hard invariants around probabilistic behavior;
- expressing soft constraints without confusing them with guarantees;
- validating, gating, retrying, containing, or escalating model outputs;
- maintaining traceability across model-mediated decisions;
- creating procedural interfaces between code, models, tools, and Human Authority.

## Does not define

This module does not prescribe:

- one universal workflow or orchestration framework;
- a fixed implementation technology;
- a separate registry or document for every Judgment Node;
- identical controls for systems with different consequences and operating contexts;
- reference architectures as mandatory deployment topologies;
- universal numerical thresholds for acceptable behavior.

## Pattern expectations

A mature UA pattern should make the following explicit:

1. the recurring problem and operating context;
2. the uncertainty or failure mechanism being addressed;
3. the deterministic responsibilities that must remain intact;
4. the proposed control structure;
5. the evidence or signals needed to operate it;
6. escalation, fallback, or recovery behavior;
7. important trade-offs and known limits.

Examples attached to a pattern are informative unless explicitly classified otherwise. Pattern records and templates should be proportional to authority, downstream impact, reversibility, and failure consequences.

## Key concepts

- Judgment Node;
- Model Judgment placement;
- deterministic boundary;
- authority boundary;
- hard invariant;
- soft constraint;
- procedural interface;
- validation gate;
- fallback and escalation;
- containment of non-determinism.

## Documents

- [`judgment-node-boundary.md`](judgment-node-boundary.md) — draft-normative pattern for making consequential Model Judgment explicit, bounded, observable, and operable through a minimal or extended boundary.

The Judgment Node Boundary pattern includes a compact SMB-facing card directly in the document. The repository does not maintain a separate `judgment-node-record.md` artifact.

Individual patterns should use the metadata and status conventions in [`DOCUMENT-METADATA.md`](../DOCUMENT-METADATA.md).

## Relationships

- [`00-doctrine/`](../00-doctrine/) provides the foundational distinctions used by the patterns, including the [`Model Judgment Placement`](../00-doctrine/model-judgment-placement.md) taxonomy.
- [`02-ai-control-plane/`](../02-ai-control-plane/) provides the control capabilities through which patterns are operated.
- [`03-reference-architectures/`](../03-reference-architectures/) demonstrates possible combinations of patterns.
- [`04-failure-modes/`](../04-failure-modes/) provides the failure mechanisms that patterns should mitigate.
- [`SPECIFICATION.md`](../SPECIFICATION.md) defines the status and normative boundary of this module.
