---
title: Reference Implementations Brief
artifact_type: research-note
status: research
maturity: draft
draft: true
module: research
topics:
  - thinking-systems
  - containment
  - evidence
  - control-loop
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/thinking-systems
  - ua/topic/containment
  - ua/topic/evidence
  - ua/topic/control-loop
repository_migrated: 2026-07-25
updated: 2026-07-31
source_path: research/reference-implementations_brief.md
license: CC-BY-4.0
---

# Reference Implementations Brief

> **Research status:** Planning brief. This note identifies a possible implementation-evidence task; it is not a completed survey and does not establish implementation guidance.

## Purpose

Study production systems, worked applications, and implementation experiments that separate deterministic control from probabilistic judgment and can test current UA doctrine and patterns.

## Current framework state

UA now contains:

- a Model Judgment placement taxonomy;
- a Judgment Node Boundary pattern;
- a Thinking System Review and practical template;
- four placement-focused reference architectures.

Those artifacts describe what should be made explicit, but they do not yet establish which implementation choices work well across real operating contexts. The next useful evidence is therefore not another generic architecture diagram, but worked application and implementation evidence mapped back to the current framework.

## Focus areas

- production Thinking System architectures;
- deterministic containment strategies around Model Judgment;
- workflow orchestration and authority boundaries;
- evidence collection, controller decisions, and corrective-action paths;
- fallback, rollback, degraded mode, escalation, and shutdown;
- change traceability across models, prompts, policies, tools, context, and data;
- failure modes observed in practice;
- control effort and operating cost relative to business value.

## Intended deliverables

- worked Thinking System Reviews using real or realistically bounded systems;
- implementation-oriented architecture records with explicit assumptions and trade-offs;
- recurring technical and socio-technical patterns supported by evidence;
- failure-mode observations and missing-control findings;
- feedback on whether the current SMB template is sufficiently clear and lightweight;
- candidate reference implementations only after stable recurring needs are demonstrated.

## Relationship to current work

Implementation evidence should be compared with the canonical doctrine and patterns rather than treated as a source of local doctrine. Reference architectures remain non-prescriptive, and a particular framework, orchestration product, vendor, or repository layout must not become the UA standard by example.
