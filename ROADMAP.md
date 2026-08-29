---
title: Uncertainty Architecture Roadmap
artifact_type: roadmap
status: informative
maturity: active
module: repository
topics:
  - repository-architecture
  - navigation
  - constraints
tags:
  - ua/module/repository
  - ua/type/roadmap
  - ua/status/informative
  - ua/topic/repository-architecture
  - ua/topic/navigation
  - ua/topic/constraints
canonical_for:
  - project-roadmap
---

# Uncertainty Architecture Roadmap

Uncertainty Architecture is being developed as a practical open specification for engineering and operating software that delegates part of its behavior to probabilistic Model Judgment.

This roadmap distinguishes completed work, active consolidation, near-term priorities, and later possibilities without speculative dates.

## Status legend

- **Completed** — present and accepted as the current repository baseline.
- **Active** — under development, application, or review.
- **Next** — intended after the active work reaches a stable checkpoint.
- **Later** — useful but not required for the current framework spine.

## Phase 1 — Concept validation

**Status: Completed**

Established:

- the initial UA thesis and publication corpus;
- Deterministic Core and Model Judgment distinctions;
- control-theory framing for AI governance;
- the initial AI Control Plane concept;
- public and expert feedback;
- repository structure and licensing.

## Phase 2 — Framework spine

**Status: Active**

The objective is to consolidate research into a coherent, bounded specification.

### Current baseline

- Research, history, and raw-source namespaces are separated.
- Specification boundary, status model, metadata, glossary, roadmap, changelog, and AI-contributor guidance exist.
- **Thinking Systems** is the current system-category term; category membership is based on whether at least one **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment and is distinct from control completeness or production readiness.
- Requirements, Operating Envelopes, Correctness, Bugs, and diagnostic sources are defined.
- Model Judgment Placement distinguishes Input Interpretation, Decision Logic, and Output Mediation without prescribing a pipeline.
- The Judgment Node Boundary, project review, and delivery review are established.
- Organizational, project, delivery, and runtime decision levels are distinguished.
- Project authorization, delivery release, runtime reassessment, and Architectural Veto remain separate decisions.
- The default SMB path uses one living project review and one living delivery review.
- Four logical capability families are established as the current draft baseline: Constraints and their realizations, Sensors and evidence, Controllers and decision authority, and Actuators and corrective action.
- A closed feedback loop is distinguished from a complete bounded UA control architecture.
- One canonical Project Constraint Architecture and one canonical delivery Constraint Realization Map are established as the default proportional Constraint records.
- Repository-relative links, navigation routes, citation metadata, critical repository structure, compatibility markers, and the top-level namespace have deterministic validation foundations.
- Controlled frontmatter, tag projection, active canonical ownership, and protected glossary entries have deterministic validation foundations; selected terminology drift remains advisory.
- Pull-request declarations, notable-change companion updates, research-state traceability, maintained-path deletion or rename decisions, explicit `agent_assistance` applicability, and repository-policy classification have a diff-aware validation foundation. Change coupling and agent checkpoint share one PR-owned diff definition based on the merge-base of the current target tip and PR head; target-only changes synchronized into a branch are not reclassified as PR-owned changes. PR-owned repository-policy paths force `change_class: repository-policy` rather than trusting a weaker self-declaration. Existing open human-authored PRs created before the applicability field migrate by adding it on their next maintained iteration rather than being silently grandfathered.
- AI-assisted pull-request iterations have a deterministic **checked-state checkpoint** bound to the PR diff-base identity, current target tip, head, tested merge result, PR-description digest, trusted PR-review/inline-review feedback digest, and effective scoped `AGENTS.md` blobs. `agent_assistance: none` is a target-branch CODEOWNER-controlled **head-bound** opt-out rather than a PR-author self-attestation, so a later repository head requires fresh opt-out evidence. High-impact AI-assisted work—including repository-policy work inferred directly from PR-owned policy paths—remains Draft while repository-changing work is active. Leaving Draft requires a fresh checkpoint and a target-branch global CODEOWNER approval bound to the exact head, tested merge SHA, PR-body digest, and checkpoint fingerprint; the approval must exist and remain unedited before Ready. Durable readiness is then verified from the expected job and success step of the protected `.github/workflows/change-coupling.yml` pull-request run attached to the PR head, rather than from a same-named check alone. Failed or premature Ready transitions cannot be legalized retroactively by later checkpoint/comment edits; same-head review feedback may stale the checkpoint without revoking readiness, while a substantive PR-body edit, later head, changed tested-merge state, or new Ready cycle requires fresh authorization. Ordinary top-level PR comments remain semantic feedback rather than immediate PR-head status events; structured CODEOWNER control markers are read during the regular PR-head checkpoint.
- The Research Track now separates active epistemic state from framework promotion: a canonical Research State Register carries material terms, hypotheses, comparison questions, candidate artifacts/processes, provenance records, status, ownership, and next decisions, while `framework-traceability.md` remains the source-to-framework decision ledger.
- Quartz production builds, maintained Mermaid diagrams, workflow syntax and security posture, immutable action and container references, dependency updates, and dependency-risk checks have an executable repository-integrity foundation.

### Four-family capability baseline

The accepted current draft baseline:

- establishes a composite Constraints family containing the authoritative Constraint and its operational Constraint Realization;
- places that family alongside Sensors and evidence, Controllers and decision authority, and Actuators and corrective action;
- distinguishes a closed feedback loop from a complete bounded UA control architecture;
- distinguishes Constraint from Constraint Realization;
- defines hard or soft as a scoped claim about a Constraint and its complete realized path;
- requires separate records when one source condition has different guarantee strengths across subjects, paths, or scopes;
- classifies tools by function rather than product name;
- separates evaluation evidence, gate decision logic, and release execution into Sensor, Controller, and Actuator functions;
- introduces one canonical Project Constraint Architecture and one canonical delivery Constraint Realization Map;
- preserves legacy Sensor and Controller deep links through informative compatibility notices;
- records the PDF presentation source and rejects unverified PPTX-only provenance claims;
- aligns doctrine, patterns, Control Plane, references, failure modes, conformance, navigation, and research traceability around one model.

The repository integration is complete. The relevant framework documents remain draft-normative and still require worked application, real-team use, operational evidence, and further terminology validation before a broader maturity claim.

### Exit work for this phase

- [x] Complete architectural and logical consistency review of the capability-family model.
- [x] Confirm one Project Constraint Architecture and one delivery Constraint Realization Map as the default proportional record structure.
- [x] Integrate the four-family capability model across current repository doctrine, patterns, Control Plane, references, failure modes, conformance, navigation, and traceability.
- [x] Complete automated internal-link, navigation-route, anchor, and citation validation.
- [x] Establish a machine-readable repository contract protecting critical files, landing-page functions, compatibility paths, and the top-level namespace, with independent regression fixtures.
- [x] Establish controlled frontmatter, tag-projection, active canonical-ownership, protected-glossary, and terminology-warning validation.
- [x] Establish diff-aware changelog, glossary, roadmap, traceability, deletion, rename, and machine-readable pull-request coupling.
- [x] Establish a deterministic AI-agent checked-state checkpoint with diff-derived repository-policy classification, target-branch CODEOWNER-controlled and head-bound applicability opt-out, one PR-owned diff model shared with change coupling, tested-merge instruction resolution, PR-description and trusted PR-review/inline-review feedback watermarks, state-bound CODEOWNER readiness approval across head/merge/body/checkpoint, verified readiness workflow/job/step provenance on the PR head, retroactive-comment-edit rejection, coherent PR-contract exception handling, explicit migration for pre-existing open PRs, and mutation/regression protection of the control surface including its repository-contract registration.
- [x] Establish a cross-document Research State Register with stable material-item IDs, provenance boundaries, epistemic status, ownership, next decisions, deterministic CI validation, and regression fixtures.
- [x] Complete automated Mermaid rendering and Quartz production-build validation.
- [x] Establish workflow linting, security analysis, immutable action/container policy, dependency update automation, and bounded dependency-risk checks.
- [ ] Build a two-level worked application tracing Constraints from organizational source through project architecture, delivery realization, runtime evidence, and reauthorization.
- [ ] Apply both reviews to a real team or documented real system boundary.
- [ ] Complete cross-publication synthesis and resolve remaining terminology conflicts.
- [ ] Validate the capability-family model against operational and incident evidence.

## Phase 3 — Patterns and failure modes

**Status: Active**

### Current outcomes

- Judgment Node Boundary with compact and extended use;
- project review connecting scenarios, Constraint architecture, capabilities, evidence, capacity, economics, authorization, inheritance, and reauthorization;
- delivery review connecting one realization map, DoR, implementation or experiment, DoD, Release Gate, operation, and reassessment;
- scenario-based risk reasoning without mandatory aggregate scores;
- failure taxonomy covering Constraint definition, realization, Sensor, Controller, Actuator, feedback, Human Authority, capacity, and economic failures;
- placement-focused reference architectures;
- one illustrative delivery review.

### Next outcomes

- two-level worked project-and-delivery application;
- containment, fallback, compensation, retry, escalation, and rollback patterns;
- drift, dependency-change, and verification patterns;
- Human-in-the-Loop and Human-on-the-Loop patterns;
- incident-based failure-mode examples;
- deeper guidance for deriving Constraints and tolerances from consequence, authority, detectability, reversibility, propagation, and capacity;
- additional worked domains.

## Phase 4 — Operating model and practical artifacts

**Status: Active**

The objective is practical use by SMB teams without a large governance organization.

### Current operating model

- one project review owns project viability, Project Constraint Architecture, authorization, inheritance, and reauthorization;
- one delivery review owns one Constraint Realization Map, DoR, DoD, Release Gate, and local reassessment;
- higher-level context is linked by version rather than copied;
- Judgment Node cards reference delivery Constraint IDs rather than redefining them;
- separate registers, gate records, responsibility matrices, or governance-board protocols are optional only when independent ownership or lifecycle requires them;
- versioned snapshots preserve decision history.

### Next outcomes

- real-team usability and time-to-complete evidence;
- decision-quality and duplication analysis;
- control-economics guidance using ranges and sensitivity rather than false precision;
- adoption guidance based on application evidence;
- refinements to incident, exception, and learning loops where concrete use exposes gaps.

A new top-level Operating Model module is not planned at this stage.

## Phase 5 — Optional tooling and reference implementations

**Status: Later**

### Current repository-integrity foundation

- deterministic navigation coverage and route validation;
- offline repository-relative link and anchor validation;
- machine-readable citation validation;
- a machine-readable repository contract for critical paths, sections, links, compatibility markers, and the top-level namespace;
- controlled frontmatter and tag-projection validation for the declared maintained-document baseline;
- active `canonical_for` uniqueness with superseded claims excluded;
- protected glossary-entry presence and uniqueness checks;
- non-blocking warnings for selected terminology drift, title/H1 drift, and unusually large tag sets;
- diff-aware changelog, glossary, roadmap, research-traceability, deletion, rename, compatibility, pull-request declaration, repository-policy classification, and `agent_assistance` validation over a shared PR-owned current-target merge-base diff;
- a checked-state AI-agent iteration checkpoint that rejects stale attestations, resolves effective root/nested `AGENTS.md` from the tested merge state, incorporates trusted review/inline-review feedback on the PR lifecycle, requires head-bound CODEOWNER evidence before a human-only `none` opt-out, and enforces Draft/readiness through CODEOWNER approval bound to head + tested merge + PR-body digest + checkpoint fingerprint followed by verified readiness workflow/job/step provenance on the PR head; retroactive edits to pre-Ready comments do not authorize Ready, and repository-contract registration is mutation-protected rather than self-tested only by direct extension loading;
- deterministic validation of stable Research State Register IDs, controlled item classes/statuses/origins, repository paths, and indexed provenance records for external review/dialogue inputs;
- Quartz production builds and rendering of maintained Mermaid blocks;
- deployment-independent Quartz-to-PDF rendering from canonical Markdown, with draft-only temporary builds, strict provenance manifests, coherent PDF/manifest rollback, visual verification, and explicit standalone-article versus long-form working-paper outputs;
- reproducible Medium and LinkedIn rendition packages generated from one committed content edition, with reviewed publication assets, platform-safe copy packages, alt text, canonical-link guidance, SEO metadata, launch-post validation, and provenance/readiness manifests;
- actionlint and zizmor checks for GitHub Actions workflows;
- full-SHA action references, version comments, and sha256 container digests enforced by a machine-readable contract;
- weekly Dependabot updates for npm and GitHub Actions;
- bounded npm audit enforcement and GitHub Dependency Review integration, with Dependency Graph enablement remaining a repository-setting prerequisite;
- independent mutation fixtures proving that protected structural, metadata, research-register, change-coupling, agent-checkpoint, and supply-chain regressions fail predictably;
- explicit repository ownership through `CODEOWNERS` and structured pull-request input through the default template.

### Later tooling

- diff-aware enforcement that material research-state transitions update either the Research State Register, framework traceability, or both according to the declared effect;
- checks for stale canonical paths and relationships;
- make `Agent protocol / checked-state checkpoint` and, where appropriate, `Agent protocol / readiness authorization` required merge checks through a repository ruleset or equivalent branch protection, and require current-base integration before merge so a stale or missing checkpoint cannot be bypassed by ordinary merge flow;
- stronger dependency-review enforcement after repository Dependency Graph enablement;
- example Constraint, realization, prompt, policy, evaluation, and release manifests;
- executable realization examples;
- reference control-plane implementations;
- template generation from stable specification components.

Tooling must serve the specification rather than redefine it. No universal SDK, platform, policy engine, or agent framework is planned.

## Current priority

The immediate priority is to stabilize and test this path:

```text
Controlled-object doctrine
→ Control-Loop Capability Anatomy
→ Project Constraint Architecture and authorization
→ Delivery Constraint Realization and release
→ Runtime evidence and corrective action
→ Local reassessment, project reauthorization, or organizational review
```

The next worked application should show:

- authoritative organizational sources and decision rights;
- project scenarios, Constraints, capability requirements, evidence, capacity, economics, and authorization;
- one versioned inheritance package;
- one or more delivery realization maps;
- runtime realization state, behavior, violations, false blocks, Sensor evidence, Controller decisions, and Actuator execution;
- evidence that remains local versus evidence requiring higher-level reassessment;
- how duplication and parallel registries are avoided.

The project optimizes for durable clarity, traceability, and practical usefulness rather than repository volume.
