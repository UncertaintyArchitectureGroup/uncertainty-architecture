---
title: Operational Protocol for AI Contributors
artifact_type: repository-guide
status: informative
maturity: active
module: repository
topics:
  - repository-architecture
  - navigation
  - provenance
  - contribution-workflow
tags:
  - ua/module/repository
  - ua/type/repository-guide
  - ua/status/informative
  - ua/topic/repository-architecture
  - ua/topic/navigation
  - ua/topic/provenance
canonical_for:
  - ai-agent-repository-guide
---

# Operational Protocol for AI Contributors

## 1. Purpose and authority

This file is the repository-wide **router and control protocol for AI-assisted contributors**. It tells an agent how to discover instructions, find the canonical owner of a change, choose the required reading path, handle maintainer corrections, and complete checked repository work.

Do not use it as a second glossary, a second specification, or a source of new governance requirements.

Canonical UA meaning belongs in the owning specification documents. Ordinary contribution mechanics belong in [`CONTRIBUTING.md`](CONTRIBUTING.md). Exact schemas and deterministic enforcement belong in the pull-request template, `.github/policy/`, `.github/scripts/`, `.github/tests/`, and GitHub Actions.

Determine authority by **concern**, not by one global document ranking:

- [`SPECIFICATION.md`](SPECIFICATION.md) owns the specification boundary, status model, conformance model, and change-control boundary.
- A document's explicit status and normative language determine whether its statements can carry normative force.
- A module README owns module scope, placement, and navigation; it does not override a canonical term or another document's declared decision surface.
- [`00-doctrine/glossary.md`](00-doctrine/glossary.md) owns canonical vocabulary where an entry exists.
- Doctrine, patterns, capability documents, repository processes, and publishing documents own the meaning or workflow explicitly assigned to them by `canonical_for`, the specification index, or their declared scope.
- [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) owns metadata and controlled tag vocabulary; machine policy validates an observable subset.
- Research, history, raw sources, references, templates, and examples own evidence, provenance, or illustration within their status; they do not update framework meaning by implication.

If two active sources claim the same concern or produce incompatible instructions within the same scope, report the contradiction instead of silently selecting one. Contribution workflow uses scoped ownership: `CONTRIBUTING.md` governs ordinary contributor procedure, while this file supplements it and takes precedence only for AI-specific behavior.

Treat current GitHub repository state as authoritative for repository facts. Prior chats, summaries, pasted excerpts, and cached snapshots are supporting context only.

## 2. Session bootstrap and instruction scope

At the start of every repository task, and again before repository-changing work when state may have changed:

1. resolve repository access, default branch, current target tip, task-relevant ref, and repository tree;
2. discover root and nested `AGENTS.md` files by tree or search rather than assumption;
3. read this root `AGENTS.md` in full;
4. read every nested `AGENTS.md` whose directory scope intersects the task; nested guidance supplements rather than replaces this file;
5. for issue or pull-request work, inspect current title/body, base/head refs, commits, complete PR-owned diff, reviews, unresolved threads, checks, workflow results, mergeability, and Draft/review state where available;
6. identify the task-specific reading path, canonical owner, relevant dependencies, and applicable repository contracts before proposing or editing;
7. distinguish verified current state, proposed work, locally prepared work, remotely applied work, and passing CI when reporting status.

Read [`content/research/AGENTS.md`](content/research/AGENTS.md) in full when work edits `content/research/` or materially changes research content, provenance, research state, or publication-edition decisions. Infrastructure that only renders, validates, transports, or packages research artifacts does not activate the long-form research-drafting protocol unless it also changes research content or state.

Inspecting a tree is not the same as reading a repository. Do not claim complete review of content you did not actually read.

State the inspected ref and material access limitations before editing only when they affect correctness or scope; otherwise include them in the completion report rather than adding a routine preamble to every response.

## 3. Task-specific reading paths

Read the complete sources needed for the task, but do not load unrelated repository content merely because it exists.

| Task | Required path after bootstrap |
|---|---|
| Understand UA | `README.md` → `SPECIFICATION.md` → controlled-object doctrine → capability anatomy → nested lifecycle → glossary → project/delivery patterns → relevant modules |
| Edit doctrine or terminology | `SPECIFICATION.md` → complete glossary → owning doctrine → both review patterns → affected capability/failure-mode material → traceability → roadmap/changelog |
| Edit project architecture material | controlled-object doctrine → capability anatomy → lifecycle → project pattern/template → delivery pattern → relevant Constraint/failure-mode/traceability material |
| Edit delivery-team material | project inheritance rules → delivery pattern/template → Judgment Node Boundary → relevant Constraint/glossary/failure-mode material |
| Edit runtime material | active project/delivery ownership rules → capability anatomy → relevant Controller/Actuator/Sensor/realization/fallback/incident material |
| Edit AI Control Plane | capability anatomy → glossary → affected capability areas → both review patterns → relevant references/failure modes/source intake/traceability |
| Research or publication content | scoped research `AGENTS.md` → `content/research/index.md` → `review-process.md` → relevant Research State Register entries → traceability → owning research artifacts |
| Metadata or controlled tags | `DOCUMENT-METADATA.md` → `.github/policy/metadata-contract.json` → validator/tests/workflow → affected maintained documents |
| Repository policy or contribution flow | `CONTRIBUTING.md` → human-readable owner of the changed rule → relevant `.github/policy/*` → validators/tests/workflows → roadmap/changelog |
| Quartz, PDF, platform rendition, or build code | `CONTRIBUTING.md` → package/config/build entry points → relevant `quartz/*.md` → owning scripts/tests/workflows; activate research protocol only if research meaning/state changes |

When a task crosses rows, combine the paths without re-reading unrelated material.

## 4. Canonical ownership and invariants

Use this map to route work. Do not copy the mapped semantic content back into this file.

| Concern | Canonical owner or starting point |
|---|---|
| Specification boundary and status | [`SPECIFICATION.md`](SPECIFICATION.md) |
| Canonical terminology | [`00-doctrine/glossary.md`](00-doctrine/glossary.md) |
| Controlled-object shift and Thinking-System category | [`00-doctrine/uncertainty-in-the-controlled-object.md`](00-doctrine/uncertainty-in-the-controlled-object.md) and glossary |
| Decision levels, inheritance, reassessment | [`00-doctrine/nested-control-lifecycle.md`](00-doctrine/nested-control-lifecycle.md) |
| Constraints, Sensors, Controllers, Actuators, bounded control | [`00-doctrine/control-loop-anatomy.md`](00-doctrine/control-loop-anatomy.md) |
| Project viability, Project Constraint Architecture, authorization, reauthorization | [`01-patterns/project-control-architecture-and-viability-review.md`](01-patterns/project-control-architecture-and-viability-review.md) |
| Delivery realization, DoR, DoD, Release Gate, local reassessment | [`01-patterns/thinking-system-review.md`](01-patterns/thinking-system-review.md) |
| Capability-specific realization guidance | [`02-ai-control-plane/README.md`](02-ai-control-plane/README.md) and affected capability area |
| Worked compositions | [`03-reference-architectures/README.md`](03-reference-architectures/README.md) |
| Reusable loss-of-control mechanisms | [`04-failure-modes/README.md`](04-failure-modes/README.md) |
| Research state, synthesis, evidence, provenance | [`content/research/index.md`](content/research/index.md) and scoped research guidance |
| Historical chronology and original source wording | [`content/history/README.md`](content/history/README.md) and [`content/raw/README.md`](content/raw/README.md) |
| Metadata and controlled tags | [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) |
| Ordinary contributor workflow | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Repository-policy enforcement | [`.github/policy/repository-contract.json`](.github/policy/repository-contract.json) plus sibling policy contracts, validators/tests, PR template, and workflows |
| Quartz publishing / PDF / platform renditions | `quartz/` documentation, scripts, tests, and relevant workflows |

Repository-wide invariants:

- One canonical concept or decision surface should have one authoritative owner. Refine the owner instead of creating a competing source.
- Search current terminology, paths, contracts, validators, tests, and overlapping implementations before adding a term, document, abstraction, workflow, or namespace.
- Do not redefine glossary or doctrine concepts locally in templates, examples, reference architectures, agent guidance, or Project instructions.
- Research provides evidence and candidates; it does not update specification meaning by implication. Promote research only through an explicit framework decision and required traceability updates.
- Preserve attributed, raw, historical, and published source wording unless the owning provenance process explicitly authorizes transformation.
- Metadata, tags, recency, navigation, publishing surfaces, and external attention do not create authority.
- A lower-level artifact or implementation must not silently expand higher-level authority or weaken an inherited boundary; read the owning lifecycle or pattern when this distinction matters.
- Prefer the smallest coherent, reviewable change and preserve UA's SMB-first proportionality default. Before adding roles, files, registers, services, committees, gates, or process, read the applicable proportionality owner and justify the added structure against actual consequence, authority, evidence, capacity, or lifecycle needs.
- Every notable repository or specification-artifact change must be recorded in [`CHANGELOG.md`](CHANGELOG.md).
- Never claim a file, test, commit, workflow, review, or PR state without verifying it.

For material framework changes, locate the work on both canonical axes—**decision level** and **capability family/function**—by reading the Nested Control Lifecycle and Control-Loop Capability Anatomy. This file does not maintain a duplicate four-by-four framework model.

## 5. Repository placement map

Use the existing namespace whose owner matches the material:

- root entry points — public navigation, specification boundary, roadmap, changelog, metadata, contribution process, and this AI routing protocol;
- `00-doctrine/` — foundational distinctions and canonical architecture meaning;
- `01-patterns/` — reusable socio-technical responses and review patterns;
- `02-ai-control-plane/` — capability-specific realization guidance;
- `03-reference-architectures/` — non-prescriptive worked compositions;
- `04-failure-modes/` — reusable loss-of-control mechanisms;
- `content/research/` — research state, evidence, synthesis, critique, and provenance;
- `content/history/` and `content/raw/` — chronology and preserved source wording;
- `assets/` — maintained visual assets;
- `quartz/` and related build configuration — publishing implementation;
- `.github/` — deterministic repository policy and CI enforcement.

Do not create a parallel namespace or new canonical record when an existing owner can be refined.

## 6. Terminology and AI-control protocol

Before introducing, redefining, replacing, deprecating, or narrowing a UA term, read the complete glossary, search current framework material and near-synonyms, identify the declared owner of the affected meaning, and reconcile glossary and research traceability when the canonical meaning or research disposition changes.

Use terminology from the current glossary and meaning from the declared owning doctrine, pattern, or capability document. Preserve historical, quoted, raw, and attributed wording under the applicable provenance rules instead of normalizing it in place.

For Constraint, Constraint Realization, Hard/Soft strength, Sensor, Controller, Actuator, Human Authority, diagrams, and bounded-control semantics, read [`00-doctrine/control-loop-anatomy.md`](00-doctrine/control-loop-anatomy.md) and the affected owning pattern or capability material. For project/delivery inheritance, authorization, release, and reassessment semantics, read [`00-doctrine/nested-control-lifecycle.md`](00-doctrine/nested-control-lifecycle.md) and the owning project or delivery pattern.

### Corrective feedback and control improvement

Treat the active maintainer conversation and trusted GitHub review surfaces as feedback signals. When the maintainer corrects an interpretation, source-of-truth choice, scope, implementation, or verification step:

1. apply the valid correction or report the authority conflict that prevents it;
2. diagnose why the deviation occurred;
3. classify the cause as local or reasonably likely to recur;
4. route a durable candidate to the narrowest correct owner: Project/bootstrap configuration, reusable agent guidance, root or nested `AGENTS.md`, a canonical UA/publishing artifact, or an existing deterministic control;
5. prefer one descriptive owner, with automation only for an observable subset.

Do not turn every preference into permanent guidance, duplicate one rule across several instruction surfaces, encode subjective editorial judgment as brittle CI, or create a new workflow when an existing control can coherently own the check.

Before applying a **feedback-derived** persistent-guidance change, present the candidate to the maintainer with the triggering failure pattern, recurrence rationale, proposed owner, exact scope change, expected benefit, and automation feasibility. Apply it only after approval of that candidate. This extra approval is not required when editing agent guidance is itself the maintainer's explicit task.

The completion report must record every material durable candidate considered, its owner, automation feasibility, approval/disposition, and whether it was applied, proposed, rejected, or deferred.

### Deterministic agent iteration checkpoint

This section owns behavioral invariants; [`CONTRIBUTING.md`](CONTRIBUTING.md) owns ordinary contributor procedure and step-by-step PR mechanics. Exact marker schemas and field layouts belong to the PR template and machine contracts, not this always-loaded router.

Every human-authored PR declares `agent_assistance` as `used` or `none`. The `ua-agent-assistance-none` path is a maintainer-controlled, head-bound opt-out, not self-attestation. When assistance is used, maintain one current checkpoint bound to the PR-owned changed paths, current target/head/tested-merge state, PR-body digest, `reviewed_feedback_sha256`, and effective root/nested instruction blobs.

Instruction applicability and change coupling use the same **PR-owned changed paths**: `merge-base(current target tip, head) → head`, preserving both sides of detected renames. Before refreshing a checkpoint, re-read the applicable instructions, complete PR-owned diff, current PR description, material external maintainer corrections, trusted GitHub review/inline feedback, relevant top-level PR conversation, and this completion protocol.

AI-assisted repository-policy and protected `draft-normative` or `normative` work remains Draft while repository-changing work is active. Leaving Draft requires a fresh checkpoint, a current-authority `ua-agent-ready-approval`, explicit maintainer instruction, and successful **Agent protocol / readiness authorization** evidence for the same checked state. Later head, target, tested-merge, substantive body, or Ready-cycle changes require fresh authorization.

The separate **Agent protocol / trusted-base guard** is the target-owned boundary for candidate-modifiable policy. Candidate workflow success does not replace that status. Exception labels remain category-scoped and do not bypass checkpoint, high-impact, freshness, Draft/readiness, or trusted-base controls outside their declared category.

These controls attest checked repository state, not semantic understanding or cryptographic separation of a human from an AI acting through the same GitHub principal. Do not claim stronger guarantees than the evidence provides.

## 7. Editing workflow

Follow [`CONTRIBUTING.md`](CONTRIBUTING.md) for ordinary branching, PR, companion-update, validation-command, and readiness mechanics. This file adds the AI-specific requirements:

1. reconstruct current state and identify the requested outcome, applicable instructions, and canonical owner;
2. read the required dependencies and search for competing meaning or enforcement before editing;
3. make the smallest coherent change in the owner first, then update genuinely required companion or enforcement surfaces;
4. keep high-impact AI-assisted work Draft while repository-changing iterations remain active;
5. keep `ua-change-contract`, checkpoint disposition, PR description, and actual PR-owned diff synchronized;
6. re-read the full final diff and material feedback before claiming completion;
7. report verified state, unavailable checks, unresolved risks, and remaining maintainer actions without overstating success.

Maintainer exception labels are not a universal override. Each exception is category-scoped, must be visibly explained, and must not be broadened beyond the policy category it owns.

Do not weaken or bypass a contract merely to make a failing check green. Determine whether the repository change is wrong, the contract is stale, or an explicit compatibility decision is required.

## 8. End-of-session integrity protocol

Before reporting a repository-changing task complete:

1. re-read the effective instructions, final PR-owned diff, current PR description, material maintainer/GitHub feedback, and relevant owning sources;
2. confirm one canonical owner remains for every changed concept or workflow and that this file has not become a semantic, process, or schema mirror of those owners;
3. confirm required metadata, links, changelog, roadmap, glossary, traceability, compatibility, and task-specific companion updates match the actual diff;
4. confirm tests, validators, live CI, reviews, and PR state are reported accurately, including unavailable checks;
5. confirm `ua-change-contract`, `agent_assistance`, checkpoint disposition, Draft/readiness authorization, and trusted-base status match current PR state;
6. report unresolved risks, assumptions, exceptions, durable-improvement disposition, and decisions still requiring maintainer action.

Metadata errors are blocking.

The completion report must include the ref/commit inspected, applicable `AGENTS.md` files, verified state and work performed, changed/owning files, tests and CI, reviews and PR state, corrective-feedback improvement disposition, checkpoint/readiness/trusted-base state, unresolved risks, and whether work is complete, still Draft, or ready for review.

## 9. Repository contract checks

The machine-readable repository contract lives at [`.github/policy/repository-contract.json`](.github/policy/repository-contract.json). The metadata policy lives at [`.github/policy/metadata-contract.json`](.github/policy/metadata-contract.json). Agent-checkpoint, change-coupling, and trusted-base contracts live beside them. These files protect observable repository invariants; they do not own UA architectural meaning or ordinary contributor prose.

Use the validation commands and procedures owned by [`CONTRIBUTING.md`](CONTRIBUTING.md), adding navigation, link, Mermaid, build, publication, research-register, supply-chain, or other task-specific checks when the changed surface requires them. Live GitHub Actions remains authoritative for current PR state, tested merge state, target-owned guard status, CODEOWNER evidence, and trusted GitHub review context.

When a legitimate policy change alters a protected path, marker, value, or control invariant, update the human-readable owner first, then the relevant machine-readable contract and regression fixture in the same PR. Reorganizing prose does not itself justify weakening enforcement.
