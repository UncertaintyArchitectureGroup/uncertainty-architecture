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

It is intentionally **not** a second specification, glossary, contributor manual, or copy of validator internals. Canonical UA meaning belongs in the owning specification documents. Ordinary contribution mechanics belong in [`CONTRIBUTING.md`](CONTRIBUTING.md). Deterministic enforcement belongs in `.github/policy/`, `.github/scripts/`, `.github/tests/`, the pull-request template, and GitHub Actions.

This file is informative operational guidance and must not override, in descending order:

1. [`SPECIFICATION.md`](SPECIFICATION.md) for specification scope, status, conformance, and change control;
2. explicit document status and normative language;
3. the relevant module README;
4. [`00-doctrine/glossary.md`](00-doctrine/glossary.md) for terms it defines;
5. current doctrine for architectural meaning;
6. the owning project or delivery pattern;
7. the relevant AI Control Plane capability document;
8. [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) for metadata conventions;
9. research, history, raw sources, references, templates, and examples for evidence and context;
10. [`CONTRIBUTING.md`](CONTRIBUTING.md) for ordinary contribution workflow;
11. this file for AI-specific repository workflow.

Report genuine contradictions instead of silently choosing one side. Treat current GitHub repository state as authoritative for repository facts; prior chats, summaries, pasted excerpts, and cached snapshots are supporting context only.

## 2. Session bootstrap and instruction scope

At the start of every repository task, and again before repository-changing work when state may have changed:

1. resolve repository access, default branch, current target tip, task-relevant ref, and repository tree;
2. discover root and nested `AGENTS.md` files by tree/search rather than assumption;
3. read this root `AGENTS.md` in full;
4. read every nested `AGENTS.md` whose directory scope intersects the task; nested guidance supplements rather than replaces this file;
5. for issue or pull-request work, inspect current title/body, base/head refs, commits, full PR-owned diff, reviews, unresolved threads, checks, workflow results, mergeability, and Draft/review state where available;
6. identify the task-specific reading path, canonical owning source, relevant dependencies, and applicable repository contracts before proposing or editing;
7. distinguish verified current state, proposed work, locally prepared work, remotely applied work, and passing CI when reporting status.

Read [`content/research/AGENTS.md`](content/research/AGENTS.md) in full when work edits `content/research/` or materially changes research content, provenance, research state, or publication-edition decisions. Infrastructure that only renders, validates, transports, or packages research artifacts does not activate the long-form research-drafting protocol unless it also changes research content or state.

Inspecting a tree is not the same as reading a repository. Do not claim complete review of content you did not actually read.

Before substantive analysis or editing, briefly report the ref/commit inspected, applicable `AGENTS.md` files, task state, owning sources, and any access limitation.

## 3. Canonical ownership map

Use this map to **route** work. Do not copy the mapped content back into this file.

| Concern | Canonical owner or starting point |
|---|---|
| Specification boundary and status | [`SPECIFICATION.md`](SPECIFICATION.md) |
| Canonical terminology | [`00-doctrine/glossary.md`](00-doctrine/glossary.md) |
| Controlled-object shift and Thinking-System category | [`00-doctrine/uncertainty-in-the-controlled-object.md`](00-doctrine/uncertainty-in-the-controlled-object.md) and glossary |
| Decision levels, inheritance, and reassessment | [`00-doctrine/nested-control-lifecycle.md`](00-doctrine/nested-control-lifecycle.md) |
| Constraints, Sensors, Controllers, Actuators, and bounded control | [`00-doctrine/control-loop-anatomy.md`](00-doctrine/control-loop-anatomy.md) |
| Project viability, Project Constraint Architecture, authorization, reauthorization | [`01-patterns/project-control-architecture-and-viability-review.md`](01-patterns/project-control-architecture-and-viability-review.md) |
| Delivery realization, DoR, DoD, Release Gate, local reassessment | [`01-patterns/thinking-system-review.md`](01-patterns/thinking-system-review.md) |
| Capability-specific realization guidance | [`02-ai-control-plane/`](02-ai-control-plane/) |
| Worked compositions | [`03-reference-architectures/`](03-reference-architectures/) |
| Reusable loss-of-control mechanisms | [`04-failure-modes/`](04-failure-modes/) |
| Research state, synthesis, evidence, provenance | [`content/research/`](content/research/) and its scoped `AGENTS.md` |
| Historical chronology and original source wording | [`content/history/`](content/history/) and [`content/raw/`](content/raw/) |
| Metadata and controlled tags | [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) |
| Ordinary contributor workflow | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Repository-policy enforcement | [`.github/policy/`](.github/policy/), validators/tests, PR template, and workflows |
| Quartz publishing / PDF / platform renditions | `quartz/` documentation, scripts, tests, and relevant workflows |

For material framework changes, locate the work on both canonical axes—**decision level** and **capability family/function**—by reading the Nested Control Lifecycle and Control-Loop Capability Anatomy. Do not maintain a duplicate four-by-four framework model here.

## 4. Repository-wide agent invariants

Apply these rules across tasks; obtain semantic detail from the owning sources above.

- One canonical concept or decision surface should have one authoritative owner. Refine the owner instead of creating a competing source.
- Search current terminology, paths, contracts, validators, tests, and overlapping implementations before adding a new term, document, abstraction, workflow, or namespace.
- Do not redefine glossary or doctrine concepts locally in templates, examples, reference architectures, agent guidance, or Project instructions.
- Research provides evidence and candidates; it does not update specification meaning by implication. Promote research only through an explicit framework decision and required traceability updates.
- Preserve attributed, raw, historical, and published source wording unless the owning provenance process explicitly authorizes transformation.
- Metadata, tags, recency, navigation, publishing surfaces, and external attention do not create authority.
- A lower-level artifact or implementation must not silently expand higher-level authority or weaken an inherited boundary; read the owning lifecycle/pattern when this distinction matters.
- Prefer the smallest coherent, reviewable change. Avoid unnecessary roles, files, registers, services, committees, gates, or duplicate protocols.
- Preserve repository-relative links, explicit status/maturity, and compatibility decisions for maintained path renames or deletions.
- Every notable repository or specification-artifact change must update [`CHANGELOG.md`](CHANGELOG.md).
- Do not weaken a contract or validator merely to make a failing check green. Determine whether the change is wrong, the contract is stale, or an explicit compatibility decision is required.
- Never claim a file, test, commit, workflow, review, or PR state without verifying it.

## 5. Task-specific reading paths

Read only the complete sources needed for the task; a targeted path is better than loading the entire repository.

| Task | Required path after bootstrap |
|---|---|
| Understand UA | `README.md` → `SPECIFICATION.md` → controlled-object doctrine → capability anatomy → nested lifecycle → glossary → project/delivery patterns → relevant modules |
| Edit doctrine or terminology | `SPECIFICATION.md` → complete glossary → owning doctrine → both review patterns → affected capability/failure-mode material → traceability → roadmap/changelog |
| Edit project architecture material | controlled-object doctrine → capability anatomy → lifecycle → project pattern/template → delivery pattern → relevant Constraint/failure-mode/traceability material |
| Edit delivery-team material | project inheritance rules → delivery pattern/template → Judgment Node Boundary → relevant Constraint/glossary/failure-mode material |
| Edit runtime material | active project/delivery ownership rules → capability anatomy → relevant Controller/Actuator/Sensor/realization/fallback/incident material |
| Edit AI Control Plane | capability anatomy → glossary → all affected capability areas → both review patterns → relevant references/failure modes/source intake/traceability |
| Research or publication content | scoped research `AGENTS.md` → `content/research/index.md` → `review-process.md` → relevant Research State Register entries → traceability → owning research artifacts |
| Repository policy, metadata, contribution flow | `CONTRIBUTING.md` → relevant `.github/policy/*` → validators/tests/workflows → metadata convention if affected → roadmap/changelog |
| Quartz, PDF, platform rendition, or build code | `CONTRIBUTING.md` → package/config/build entry points → relevant `quartz/*.md` → owning scripts/tests/workflows; activate research protocol only if research meaning/state changes |

When a task crosses rows, combine the paths without re-reading unrelated material.

## 6. Editing and review workflow

For repository-changing work:

1. reconstruct the current state and identify the requested outcome;
2. identify the canonical owner and applicable scoped instructions;
3. read the required dependencies and search for overlapping rules/implementations;
4. classify the change and determine required changelog, glossary, roadmap, traceability, metadata, and compatibility updates;
5. create a focused branch and make the smallest coherent change;
6. update the owner first, then required companion/enforcement surfaces; do not create parallel meaning;
7. review the complete PR-owned diff for semantic drift, duplicate ownership, stale links, metadata, compatibility, and unintended scope;
8. complete the machine-readable `ua-change-contract` so it matches the actual PR-owned diff;
9. run applicable repository-contract, metadata, navigation, change-coupling, agent-control, build, and task-specific regression checks;
10. reconcile the PR description, current feedback, checks, and Draft/readiness state before reporting completion.

Use a Draft pull request for AI-assisted repository-policy, `draft-normative`, or `normative` work while repository-changing iterations remain active. High-impact classification is derived from protected paths and maintained-document status, not only from the PR author's declaration.

Exceptions are category-scoped maintainer controls, not generic bypasses. Explain any exception visibly and do not broaden it beyond the category defined by policy.

### Corrective feedback and control improvement

Treat the active maintainer conversation and trusted GitHub review surfaces as feedback signals. When the maintainer corrects an interpretation, expected behavior, source-of-truth choice, scope, implementation, or verification step:

1. apply the valid correction to the current task or report the authority conflict that prevents it;
2. diagnose why the deviation occurred;
3. classify the cause as local or reasonably likely to recur;
4. for a durable candidate, route it to the narrowest correct owner:
   - Project/bootstrap/tool-routing behavior → Project Instructions or equivalent project configuration;
   - genuinely cross-project agent behavior → reusable/custom-agent guidance;
   - repository-wide contributor behavior → this root `AGENTS.md`;
   - subtree-only behavior → the applicable nested `AGENTS.md`;
   - UA meaning, terminology, ownership, research state, or publishing contract → the canonical repository artifact;
   - objectively enforceable invariant → an existing or appropriately scoped test, validator, policy contract, PR check, template, or workflow;
5. prefer one canonical descriptive owner, with deterministic automation only for an observable subset.

Do not turn every preference into permanent guidance, duplicate one rule across several instruction surfaces, encode subjective editorial judgment as brittle CI, or create a new workflow when an existing control can coherently own the check.

Before applying a **feedback-derived** persistent-guidance change, present the candidate to the maintainer with the triggering failure pattern, recurrence rationale, proposed owner, exact behavior/scope change, expected benefit, and automation feasibility. Apply it only after approval of that candidate. This extra approval is not required when editing agent guidance is itself the maintainer's explicit task.

The session report must record every material durable candidate considered, its owner, automation feasibility, approval/disposition, and whether it was applied, proposed, rejected, or deferred.

### Deterministic agent iteration checkpoint

This section is the canonical human-readable owner of the AI-assisted checked-state protocol. Exact field schemas and observable enforcement are owned by [`.github/policy/agent-checkpoint-contract.json`](.github/policy/agent-checkpoint-contract.json), [`.github/policy/change-coupling-contract.json`](.github/policy/change-coupling-contract.json), the PR template, validators/tests, and protected workflows. Keep this section behavioral; do not copy validator implementation detail back into it.

Every human-authored PR declares `agent_assistance` as `used` or `none` in `ua-change-contract`.

`agent_assistance: none` is a maintainer-controlled, head-bound opt-out, not self-attestation. Except for Dependabot compatibility, it is effective only after a target-branch global CODEOWNER who still has current `write`, `maintain`, or `admin` permission and trusted GitHub association adds the structured top-level PR comment for the exact head:

```text
<!-- ua-agent-assistance-none
{"agent_assistance":"none","head_sha":"<current-head-sha>"}
-->
```

A later head invalidates that opt-out.

When `agent_assistance: used`, maintain exactly one `ua-agent-checkpoint` block using the PR template. A valid checkpoint is bound to the PR diff-base identity, current target tip, current head, tested merge result, `reviewed_pr_body_sha256`, `reviewed_feedback_sha256`, and exact effective root/nested `AGENTS.md` blob SHAs.

Instruction applicability and change coupling use the same **PR-owned changed paths**: `merge-base(current target tip, head) → head`, preserving both sides of detected renames. Resolve effective instructions in the tested merge state; if scoped guidance is deleted by the PR, retain the governing target version for the review.

Before refreshing a checkpoint, re-read the effective applicable `AGENTS.md` files, complete PR-owned diff, current PR description, available external maintainer corrective feedback, trusted review/inline-review feedback, relevant top-level PR Conversation feedback, and this completion protocol. Classify durable feedback truthfully before updating checkpoint disposition.

High-impact AI-assisted work remains Draft while repository-changing work is active. Repository-policy scope and protected `draft-normative` / `normative` status are derived from target/candidate state and cannot be disabled by a weaker PR declaration or same-PR status downgrade.

Leaving Draft is maintainer-controlled. First establish a fresh checkpoint. Then a currently authorized target-branch global CODEOWNER must add approval bound to the current head, tested merge, approved PR-body digest, and canonical checkpoint fingerprint:

```text
<!-- ua-agent-ready-approval
{
  "head_sha":"<current-head-sha>",
  "merge_sha":"<current-tested-merge-sha>",
  "pr_body_sha256":"<current-pr-body-sha256>",
  "checkpoint_sha256":"<canonical-checkpoint-sha256>"
}
-->
```

Only after that evidence exists, and only after explicit maintainer instruction, may the AI contributor initiate Ready. The protected `ready_for_review` run must validate the same state and the separate **Agent protocol / readiness authorization** evidence must come from the expected job/step of `.github/workflows/change-coupling.yml` on the PR head. A failed or premature Ready transition cannot be legalized retroactively by later comment edits.

A later head, target tip, tested merge, substantive PR-body change, or new Ready cycle requires fresh authorization. Same-head trusted review feedback may stale the checkpoint without by itself revoking an already valid readiness cycle.

The separate **Agent protocol / trusted-base guard** is the target-owned enforcement boundary for candidate-modifiable repository policy. Its `pull_request_target` path executes only trusted target code, treats candidate content as untrusted data, and re-evaluates open PRs when `main` advances. Candidate workflow success is not a substitute for this target-owned status. `ua-exception/pr-contract` bypasses only malformed/missing change-contract validation; it does not bypass checkpoint, high-impact, freshness, Draft/readiness, or trusted-base controls.

These controls attest checked repository state, not semantic understanding or cryptographic separation of a human from an AI acting through the same GitHub principal. Do not claim stronger guarantees than the evidence provides.

## 7. Validation and repository contracts

For repository-policy work, inspect the relevant contracts and run at minimum:

```bash
python3 .github/scripts/validate_repository_contract.py
python3 .github/tests/repository_contract/test_repository_contract.py
python3 .github/scripts/validate_metadata.py --mode all
python3 .github/tests/metadata_contract/test_metadata.py
python3 .github/scripts/validate_change_coupling.py --base <current-target-tip-sha> --head <head-sha> --pr-body-file <pr-body-file> --labels <comma-separated-labels>
python3 .github/tests/change_coupling/test_change_coupling.py
python3 .github/tests/agent_checkpoint/test_agent_checkpoint.py
python3 .github/tests/agent_checkpoint/test_feedback_context.py
python3 .github/tests/agent_checkpoint/test_trusted_base_guard.py
python3 .github/tests/agent_checkpoint/test_checkpoint_repository_contract.py
```

Add navigation, link, Mermaid, build, publication, research-register, supply-chain, or other task-specific checks when the changed surface requires them. The live GitHub Actions state remains authoritative for inputs that do not exist in an ordinary checkout, including current PR state, tested-merge state, target-owned guard status, CODEOWNER authorization evidence, and trusted GitHub review context.

Machine-readable owners:

- [`.github/policy/repository-contract.json`](.github/policy/repository-contract.json) — critical repository structure and compatibility;
- [`.github/policy/metadata-contract.json`](.github/policy/metadata-contract.json) — metadata and canonical ownership;
- [`.github/policy/change-coupling-contract.json`](.github/policy/change-coupling-contract.json) — PR declaration and companion-file coupling;
- [`.github/policy/agent-checkpoint-contract.json`](.github/policy/agent-checkpoint-contract.json) — checked-state checkpoint fields and controlled values;
- [`.github/policy/repository-contract-agent-checkpoint.json`](.github/policy/repository-contract-agent-checkpoint.json) — protected agent-control wiring.

When a legitimate policy change alters a protected path, marker, value, or control invariant, update the human-readable owner first, then the machine-readable contract and regression fixture in the same PR. Do not modify enforcement merely because this guide was reorganized.

## 8. End-of-session integrity protocol

Before reporting a repository-changing task complete:

1. re-read the effective instructions, final PR-owned diff, current PR description, material maintainer/GitHub feedback, and relevant owning sources;
2. confirm one canonical owner remains for every changed concept or workflow and that this file has not become a semantic mirror of those owners;
3. confirm required metadata, links, changelog, roadmap, glossary, traceability, compatibility, and task-specific companion updates match the actual diff;
4. confirm tests/validators and live CI are reported accurately, including unavailable checks;
5. confirm `ua-change-contract`, `agent_assistance`, current checkpoint disposition, Draft/readiness authorization, and trusted-base status match current PR state;
6. report unresolved risks, assumptions, exceptions, and decisions still requiring maintainer action.

The completion report must include:

- ref and commit inspected;
- applicable `AGENTS.md` files;
- verified state and work performed;
- changed and owning files;
- tests, validators, CI, review, and PR state;
- corrective feedback evaluated for durable improvement, proposed owner, automation feasibility, approval/disposition;
- `agent_assistance` / checkpoint / readiness / trusted-base state where a PR exists;
- unresolved risks or unavailable checks;
- whether the work is complete, still Draft, or ready for review.
