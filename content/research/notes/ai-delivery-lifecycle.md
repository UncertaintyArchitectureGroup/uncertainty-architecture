---
title: AI Delivery Lifecycle Working Note
artifact_type: research-note
status: research
maturity: draft
draft: true
module: research
topics:
  - sdlc
  - evaluation
  - drift
  - control-loop
  - human-authority
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/sdlc
  - ua/topic/evaluation
  - ua/topic/drift
created: 2026-01-26
updated: 2026-07-31
migrated_from: ../../../00-doctrine/LLM_Delivery_SDLC.md
license: CC-BY-4.0
---

# AI Delivery Lifecycle Working Note

> **Research status:** This document preserves an early lifecycle sketch for engineering model-mediated behavior. It was moved out of `00-doctrine/` because it is a working process hypothesis, not canonical doctrine or a mandatory UA lifecycle. Numerical thresholds, role names, sequence, and cadence must be derived from context and risk before any part is promoted into normative guidance.

## Research question

How should a delivery process change when part of the system's runtime behavior is produced through probabilistic Model Judgment rather than only explicitly coded paths?

The sketch below proposes one possible loop from exploration to evidence-based release and production feedback. It is intended to expose control responsibilities, not prescribe one universal SDLC.

## Illustrative lifecycle

```mermaid
graph TD
    subgraph DISCOVERY ["PHASE 1: DISCOVERY"]
        direction TB
        Idea((Idea))
        Explore[Explore model behavior and assumptions]
        InitialReview[Review useful and harmful cases]
    end

    subgraph ENGINEERING ["PHASE 2: ENGINEERING"]
        direction TB
        Cases[Create representative scenarios]
        Boundaries[Define schemas, invariants, permissions, and fallback]
        Version[Version relevant prompts, policies, models, and configuration]
    end

    subgraph EVALUATION ["PHASE 3: EVALUATION"]
        direction TB
        RunEvidence[Collect automated and human evidence]
        Gate{Release decision}
    end

    subgraph PRODUCTION ["PHASE 4: PRODUCTION"]
        direction TB
        Deploy[Deploy within an operating envelope]
        Observe[Observe outcomes, incidents, drift, and operating conditions]
    end

    Idea --> Explore
    Explore --> InitialReview
    InitialReview --> Cases
    Cases --> Boundaries
    Boundaries --> Version
    Version --> RunEvidence
    RunEvidence --> Gate
    Gate -- Insufficient evidence or unacceptable risk --> Explore
    Gate -- Authorized release --> Deploy
    Deploy --> Observe
    Observe -. Deviation or changed conditions .-> Explore
```

## Phase 1: Discovery

### Goal

Learn whether the proposed use of Model Judgment creates enough value to justify further engineering and control cost.

### Possible activities

- explore model behavior across ordinary and adversarial cases;
- identify assumptions about users, context, data, tools, and operating conditions;
- record useful variance as well as unacceptable behavior;
- identify where deterministic responsibilities must remain intact;
- decide whether the use case should proceed at all.

### Exit question

Is there enough evidence of potential value, and a credible path to bounding the important risks, to justify engineering work?

A favorable demonstration is not by itself sufficient evidence.

## Phase 2: Engineering

### Goal

Convert an exploratory model interaction into a reviewable system design.

### Possible artifacts

- representative scenarios, including edge cases and failure cases;
- explicit invariants and permissions;
- schemas and deterministic validation where appropriate;
- bounded tool access and execution authority;
- fallback, escalation, rollback, and shutdown paths;
- versioned prompts, policies, context assembly, models, and evaluation configuration;
- ownership and traceability for behavior-affecting changes.

Representative scenarios should be selected for risk coverage and learning value. UA does not prescribe a universal sample size or one ideal-output format.

## Phase 3: Evaluation and release decision

### Goal

Collect evidence proportional to the consequences, uncertainty, autonomy, reversibility, and operating context of the change.

### Possible evidence

- deterministic contract checks;
- scenario-based evaluations;
- statistical sampling;
- qualitative expert review;
- adversarial or boundary testing;
- model-assisted evaluation with calibration and limits made explicit;
- latency, cost, reliability, and operational-readiness evidence;
- rollback and incident-response exercises.

### Release gate

The release decision should identify:

1. which evidence is required;
2. who or what has authority to approve or block release;
3. which deviations are tolerable;
4. which conditions require limitation, escalation, or rejection;
5. what recovery mechanisms are available.

UA does not prescribe a universal accuracy percentage, service-level threshold, or fixed evidence count. Thresholds should be derived from the use case and the cost of error.

## Phase 4: Production feedback

### Goal

Operate the system inside an explicit envelope and maintain a path from observation to corrective action.

### Possible activities

- monitor technical behavior and business outcomes;
- review incidents, complaints, overrides, and near misses;
- detect changes in models, prompts, context, data, tools, user behavior, or environment;
- reassess evidence when operating conditions change;
- authorize configuration changes, containment, rollback, or shutdown;
- feed production learning back into scenarios, boundaries, and design assumptions.

Production telemetry does not close the loop unless evidence is connected to decision authority and a mechanism capable of changing or stopping behavior.

## Roles and responsibilities

Early versions of this sketch used titles such as **Prompt Steward**, **Eval Owner**, and **Reliability Engineer**. These remain useful examples of responsibility bundles, not mandatory job titles.

A real implementation should assign responsibility for:

- behavior-affecting configuration;
- evaluation design and calibration;
- deterministic boundaries and infrastructure;
- release authority;
- runtime observation and incident handling;
- escalation and human judgment;
- traceability and controlled change.

One person or existing team may hold several responsibilities in a small organization.

## Open questions

- Which evidence types are useful for different consequence and autonomy classes?
- How should release and reassessment cadence scale with feedback latency and operating change?
- When does the cost of control make the proposed automation structurally unattractive?
- Which incident and learning-loop refinements are needed beyond the current review pattern?
- Which lifecycle distinctions remain useful across very different delivery organizations and product types?

## Framework translation status

Several questions from the original sketch have now been translated into current draft framework components:

| Earlier lifecycle question | Current framework decision |
|---|---|
| Where should lifecycle responsibilities live? | Reusable delivery responsibilities are expressed through the [`Thinking System Review`](../../../01-patterns/thinking-system-review.md) pattern rather than embedded in doctrine or placed in a new top-level Operating Model module. |
| Which lightweight artifacts can SMB teams maintain? | One living [`Thinking System Review Template`](../../../01-patterns/thinking-system-review-template.md) contains Judgment Node cards, DoR, DoD, residual risk, deployment scope, release decision, and reassessment history. |
| How should readiness, completion, and release differ? | Full model-mediated DoR and DoD extensions have one canonical owner in the review pattern, while the Release Gate remains a distinct residual-risk decision. |
| Are specialist AI role titles mandatory? | Implementation, evaluation, operation, and release decision authority are responsibility bundles, not mandatory job titles. |
| Does every change require separate governance records? | The default SMB path uses versioned snapshots of one review artifact rather than separate readiness, completion, role, node-registry, and release records. |

These translations do not make the four-phase diagram a mandatory lifecycle. The remaining open questions concern evidence proportionality, control economics, incident learning, reassessment cadence, and compatibility across delivery contexts.

## Framework relationship

This note may continue to inform future work on:

- evaluation and evidence patterns;
- change and incident loops;
- risk and tolerance mapping;
- control-economics guidance;
- SMB-facing application examples;
- failure modes revealed through practical use.

It does not activate those elements as normative requirements. Research-state changes should be reconciled through [`content/research/review-process.md`](../review-process.md) and the existing traceability matrix rather than a parallel lifecycle ledger.
