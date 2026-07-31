---
title: Metrics Brief
artifact_type: research-note
status: research
maturity: draft
draft: true
module: research
topics:
  - evidence
  - evaluation
  - drift
  - control-economics
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/evidence
  - ua/topic/evaluation
  - ua/topic/drift
  - ua/topic/control-economics
repository_migrated: 2026-07-25
updated: 2026-07-31
source_path: research/metrics_brief.md
license: CC-BY-4.0
---

# Metrics Brief

> **Research status:** Planning brief. This note identifies a remaining research task; it is not completed analysis and does not create a UA metric, threshold, or conformance requirement.

## Purpose

Determine which measurements produce decision-useful evidence for Thinking Systems, which measurements commonly mislead teams, and how evidence should connect to Requirements, authority, and corrective action.

## Current framework state

UA already establishes that:

- metrics are evidence rather than control by themselves;
- evidence must be interpreted relative to an approved Requirement and decision context;
- no universal sample size, confidence method, accuracy target, hallucination threshold, drift threshold, cost limit, or review cadence is implied;
- completion evidence remains distinct from release authorization and residual-risk acceptance.

The remaining research concerns how teams select, combine, calibrate, and interpret signals in specific consequence and autonomy contexts.

## Focus areas

- drift and change detection;
- model-mediated Requirement violations and Deviation Signals;
- business-outcome and downstream-impact signals;
- evidence coverage across ordinary, boundary, adversarial, and failure scenarios;
- cost-versus-reliability trade-offs;
- sampling, uncertainty, and human review;
- evaluator calibration and disagreement;
- anti-metrics, proxy failure, metric gaming, and false confidence;
- feedback latency and the point at which evidence can still support corrective action.

## Intended deliverables

- a taxonomy of evidence and metric purposes rather than one universal metric set;
- known anti-metrics and interpretation pitfalls;
- guidance on connecting signals to Judgment Nodes, Operating Envelopes, controllers, and reassessment triggers;
- worked examples showing why the same metric may support one decision but not another;
- candidate instrumentation and evaluation patterns where recurring structure is demonstrated.

## Relationship to current work

This brief should be informed by completed Thinking System Reviews and operational observations. It should refine the evidence surface without duplicating the full DoR, DoD, or Release Gate owned by [`thinking-system-review.md`](../../../01-patterns/thinking-system-review.md).
