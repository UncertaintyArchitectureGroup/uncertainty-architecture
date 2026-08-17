---
title: "Thinking Systems: From Model Judgment to Bounded Control"
artifact_type: research-note
status: research
maturity: draft
module: research
topics:
  - thinking-systems
  - model-judgment
  - control-loop
  - constraints
  - human-authority
  - project-authorization
  - runtime-control
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/thinking-systems
  - ua/topic/model-judgment
  - ua/topic/control-loop
  - ua/topic/human-authority
created: 2026-08-17
updated: 2026-08-17
language: en
license: CC-BY-4.0
draft: true
authors:
  - "Vitalii Oborskyi"
publication_stage: adaptation-draft
derived_from:
  - open-engineering-specification-article-draft.md
  - open-engineering-specification-article-blueprint.md
related:
  - ../index.md
  - ../../../00-doctrine/glossary.md
  - ../../../00-doctrine/uncertainty-in-the-controlled-object.md
  - ../../../00-doctrine/control-loop-anatomy.md
  - ../../../00-doctrine/nested-control-lifecycle.md
---

# Thinking Systems: From Model Judgment to Bounded Control

> **Publication note.** This is a shorter standalone adaptation of the larger living working paper, [*Uncertainty Architecture: Engineering Thinking Systems with Consequential Runtime Responsibilities*](open-engineering-specification-article-draft.md). It intentionally stops after the core category, controlled-object, bounded-control, and decision-horizon argument. The longer paper remains under development. This adaptation is being prepared now so external criticism can shape the next research phase rather than arrive only after the full manuscript has been completed.

Software engineering repeatedly expands when an important source of uncertainty can no longer remain outside the engineering model.

Plan-driven development tries to reduce requirement and design uncertainty before implementation. Iterative delivery shortens the distance between assumptions and product feedback. Modern operations extends engineering into production because runtime conditions cannot be reproduced exhaustively before release.

AI adds another shift.

The uncertainty is no longer only around the software. Part of the consequential behavior may now be formed inside the software at runtime through probabilistic Model Judgment.

That changes the engineering object.

## A narrower category than “AI software”

This article uses **Thinking System** in a specific engineering sense:

> A software system in which one or more **Consequential Runtime Responsibilities** depend partly on probabilistic Model Judgment rather than being fully specified through explicitly encoded logic in advance.

A runtime responsibility is **consequential** here when its output, decision, path, action, or downstream state can materially affect an intended outcome, an applicable Requirement or Constraint, delegated authority, resource use, or another person or system downstream.

Consequential does not mean dangerous, regulated, autonomous, or high-risk. It describes material causal relevance. Severity, likelihood, reversibility, residual exposure, autonomy, and production readiness are separate questions.

The category also does not depend on whether the application is marketed as “agentic.” A fixed workflow can already be a Thinking System if one consequential responsibility inside it depends partly on probabilistic Model Judgment. A dynamically orchestrated system can remain outside the category when all consequential responsibilities are still explicitly encoded.

The classification question is simply:

```text
Does any Consequential Runtime Responsibility
partly depend on probabilistic Model Judgment?

No  → Linear Software for this category test
Yes → Thinking System
```

Orchestration topology, autonomy, and delegated authority still matter enormously. They affect architecture, consequence, and control demand. They just do not define the category.

The word **Thinking** is functional, not anthropomorphic. It makes no claim about consciousness, sentience, or human-like cognition. It gives us a short name for a changed responsibility structure in software.

## The controlled object is not the model call

One reason AI systems are easy to reason about badly is that the model invocation attracts most of the attention.

We measure model quality. We tune prompts. We compare models. We add evaluations, guardrails, traces, and human review. Each can be useful. But the model call is usually not the thing that produces the business consequence by itself.

Consider a bounded customer-support resolution system. It may retrieve account and order context, interpret a request, apply policy, recommend a remedy, draft consequential communication, decide whether an action can proceed, call a transaction API, or route the case to Human Authority.

The controlled object is the whole software system within its declared boundary: deterministic code, probabilistic Judgment Nodes, data, configuration, identity and authorization, retrieval, tools, dependencies, deployment state, and the interfaces through which the system can create downstream effects.

The important structural change is that one or more consequential responsibilities inside that mixed system are no longer fully authored in advance.

Traditional software can be idealized as an explicitly authored relationship:

```text
situation + operating conditions
→ explicitly encoded consequential decision mechanism
→ consequential output / action / state
```

A Thinking System may instead contain a mixed responsibility structure:

```text
situation + operating conditions
→ explicitly encoded responsibilities
→ probabilistic Model Judgment at one or more Judgment Nodes
→ explicitly encoded responsibilities
→ consequential output / action / state
```

The system does not become wholly probabilistic. Deterministic responsibilities remain before, between, and after Model Judgment. But the engineering contract changes because part of a consequential responsibility is now resolved at runtime rather than exhaustively specified through code beforehand.

That is why “the model passed the evals” cannot be the complete release argument.

## Measurement is necessary. It is not control.

Thinking Systems need better measurement than conventional software in several places: offline evaluations, traces, runtime outcomes, drift signals, cost, latency, incidents, control-health evidence, and often semantic or probabilistic evaluators.

But measurement answers only part of the question.

It tells us what happened, how often, under which conditions, and with what confidence.

Control requires additional relationships:

- relative to which approved boundary is the evidence interpreted?
- who or what has legitimate authority to decide that action is required?
- which mechanism can actually change operation?
- what evidence confirms that the corrective action worked?
- when does new evidence invalidate the decision that authorized the current system in the first place?

A dashboard with perfect telemetry can still describe an uncontrolled system.

A policy can be authoritative but not operationally realized.

A human approval button can exist without the reviewer having the information, competence, time, capacity, or real authority to change the outcome.

A rollback capability can exist without evidence that it restores the system to a known authorized state.

A closed feedback loop can exist and still be unacceptable if it operates outside the wrong boundary, reacts too slowly, depends on a failed Sensor, or exercises authority that was never legitimately delegated.

## Four capability functions

A bounded control architecture needs four kinds of function. These are logical capability families, not mandatory services, teams, products, or runtime layers.

**Constraints and their realizations** define the approved operating boundary and make it concrete. A Constraint is the authoritative boundary object. A Constraint Realization is the technical or socio-technical mechanism that implements, enforces, or influences it.

**Sensors and evidence** expose behavior, outcomes, conditions, realization state, control health, and the result of corrective actions. Evidence is useful only relative to a decision that consumes it.

**Controllers and decision authority** compare or interpret evidence relative to approved Requirements, Constraints, and assumptions, then select or authorize the next action. A Controller is a decision function. It may be human, automated, or socio-technical, but automation does not create authority that was never delegated.

**Actuators and corrective action** execute authorized changes: reject, route, narrow exposure, roll back, disable, compensate, switch fallback, or change an approved realization within delegated authority.

The relationships form a loop:

```text
Thinking System / active realization
→ Sensors and evidence
→ Controller and legitimate decision authority
→ Actuator / corrective action
→ changed system operation
→ new evidence
```

Constraints bound the legitimate operating space around that loop.

A product marketed as a “guardrail” may implement several of these functions. An evaluation platform may provide Sensors and some Controller automation. An orchestration runtime may implement Actuation, state, local decision logic, and Human Authority workflow primitives. The useful distinction is functional, not commercial.

The harder question is how those functions connect to authority and decisions over time.

## Four decision horizons over the same system

The same Thinking System is controlled through decisions that belong to different horizons.

They should not be collapsed into one generic “AI governance gate.”

### Organization — what may be authorized?

The organizational horizon owns authoritative boundaries, reserved decisions, shared capabilities, admissibility, exception authority, and the business or institutional basis within which a project may proceed.

It may determine that certain data, vendors, deployment modes, populations, geographies, actions, or classes of decision are prohibited or reserved to Human Authority.

An organizational policy is not automatically a technical control. Its consequences must eventually become realizable requirements, evidence obligations, decision rights, and corrective paths.

### Project / Architecture — is the controlled system viable and authorizable?

This horizon asks whether Model Judgment is actually justified for the intended outcome and whether a credible complete bounded control architecture can be built within the organizational boundary.

A project should be allowed to conclude that the right answer is deterministic software, a manual process, a narrower model-assisted path, bounded research, redesign, deferral, or No-Go.

The business case must include not only model and platform cost, but also the control perimeter: evaluation, Human Authority, fallback, observability, incident response, control maintenance, latency, false blocks, and the cost of reassessment.

A design that is technically possible but economically irrational is still a bad architecture decision.

### Delivery — is this bounded realization releasable?

Delivery translates the authorized design into a specific implementation and deployment scope.

The question is not whether “the AI feature works.” It is whether the inherited Constraints have credible realizations, the required evidence exists, claimed deterministic paths are actually complete and bypass-tested, Human Authority and fallback are operational, and rollback or containment can be executed inside delegated authority.

Delivery may repair, reconfigure, narrow, roll back, or re-release within its authorization. It may not silently expand project authority or normalize evidence that the project architecture is no longer viable.

### Runtime — does active operation remain inside the authorized boundary?

Runtime continuously produces evidence about the active system: behavior, outcomes, versions, authorization failures, realization health, evaluator health, Human Authority load, fallback load, cost, latency, incidents, and the result of Actuator execution.

Runtime Controllers may act within delegated authority. They can reject, contain, compensate, narrow, fall back, roll back, disable, or stop when those actions have been authorized.

But runtime cannot reauthorize the project merely because software is technically capable of changing configuration.

The crucial routing rule is:

```text
local realization / configuration / evidence defect
→ Delivery reassessment

project risk / feasibility / Human Authority / capacity / economics invalidated
→ Project / Architecture reassessment

authoritative organizational basis or reserved decision changed
→ Organizational review
```

Evidence should return to the decision whose basis it invalidates.

That is the difference between feedback and bureaucracy: the path exists because a specific decision owner needs evidence to decide, not because every event must climb an approval hierarchy.

## What production readiness means here

The central thesis is deliberately stronger than “use evals” or “add governance.”

> A Thinking System is not ready for production at the intended scope while any material control responsibility remains unowned, unrealized, insufficiently evidenced for its decision, or without a credible corrective or reassessment path.

“Complete” does not mean maximal. A low-consequence internal assistant may need a very lightweight explicit control surface. A system that can communicate consequential decisions directly, change business state, exercise delegated authority, or create difficult-to-reverse effects may need much more.

The complete map is useful diagnostically: inspect the whole problem first, then deliberately keep only the depth justified by the actual authority, consequence, reversibility, uncertainty, feedback latency, Human Authority burden, and economics.

One model call is not necessarily a simple control problem. One hundred services are not necessarily a difficult one. The reachable consequences matter more than the UI count.

## Why publish this before the larger paper is finished?

The longer working paper continues beyond this argument into proportional implementation, substitution against existing engineering methods and platforms, the relationship between UA and adjacent systems/safety/runtime-assurance approaches, and a broader validation agenda.

I could finish all of that first and ask for feedback later.

I think that would be the wrong order.

The useful questions now are whether the category boundary is meaningful, whether the whole-system controlled-object framing survives real architectures, whether the four capability functions are a useful partition, whether the four decision horizons place authority correctly, and where existing engineering methods already solve the same problem more cleanly.

Those answers should shape the remaining work.

There is also a recursive aspect to the research. Increasingly, the paper and the UA repository are being developed through agentic workflows. I am not treating AI as a text generator attached to the side of the work. I am increasingly using explicit sources of authority, bounded tasks, review loops, evidence, versioned repository state, human decision points, and escalation when an agent cannot legitimately resolve an ambiguity.

In other words, I am beginning to use the same architectural ideas to structure the human–agent system through which the framework itself is developed.

That is not validation. A framework cannot prove itself by being used to write about itself. But it does create another working environment in which weak boundaries, unclear authority, bad evidence routing, or false confidence become visible quickly.

The larger [working paper](open-engineering-specification-article-draft.md) and its [editorial blueprint](open-engineering-specification-article-blueprint.md) remain public in the repository. The next sections are intentionally not treated as untouchable conclusions.

## Acknowledgments and provenance

The formulation **“Thinking Systems”** entered this research through my exchange with **Arkadiy Dobkin** following his LinkedIn post [*From Fall to Rise*](https://www.linkedin.com/posts/arkadiydobkin_from-fall-to-rise-activity-7477593508879724544-8-ZL). I am grateful to Arkadiy specifically for that formulation and for the discussion that pushed me to sharpen the problem boundary. This article does **not** claim coinage of the phrase. The specific engineering definition used here—Consequential Runtime Responsibility partly dependent on probabilistic Model Judgment—and the surrounding control model are developed in the Uncertainty Architecture research track.

The work has also benefited from continuing dialogue with the **Taller** team, especially **Christophe Kolb, Maxi Armesto, and Jan**, around the socio-technical architecture surrounding AI systems. Those exchanges have helped pressure-test how authority, human participation, workflow, tooling, and control mechanics fit around the model rather than inside the model alone.

These acknowledgments record intellectual provenance and dialogue. They do not imply co-authorship, endorsement of UA, or agreement with the specific definitions and claims in this article.

## Try to break the map

I do not particularly need readers to agree with Uncertainty Architecture.

I need people to try to break it.

Apply the category test to a real system. Show where it over-classifies or misses an important case. Find a decision that does not fit the four horizons. Show where the four capability functions distort an established safety or systems-engineering method. Point to an existing platform, standard, or internal process that already preserves the same relationships with less conceptual overhead.

Show what can be removed.

Uncertainty Architecture is an open-source project and an open engineering specification under validation. Critique, contradictory cases, issues, pull requests, worked applications, and serious collaboration are welcome.

If an existing approach already solves part of the problem better, the right response is not to protect the framework. It is to make the framework smaller or change it.
