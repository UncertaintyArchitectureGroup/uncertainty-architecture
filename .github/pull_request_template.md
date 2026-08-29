## Summary

<!-- What changed, why it belongs in this repository, and the smallest coherent decision represented by this PR. -->

## Repository placement

- **Change class:** <!-- maintenance | repository-policy | research | draft-normative | normative | reference | history | publishing -->
- **Agent assistance:** <!-- used | none -->
- **Owning path or module:**
- **Decision levels affected:** <!-- organization | project | delivery | runtime | none -->
- **Capability families affected:** <!-- constraints | sensors | controllers | actuators | none -->

## Companion updates

- **Changelog:** <!-- updated | not-required: reason -->
- **Glossary:** <!-- updated | unchanged | not-applicable -->
- **Roadmap:** <!-- updated | unchanged | not-applicable -->
- **Research traceability:** <!-- updated | unchanged | not-applicable -->
- **Compatibility / migration:** <!-- preserved | changed: explain | not-applicable -->

The machine-readable block below is validated against the PR-owned git diff. Keep the human-readable fields and JSON declaration consistent. Repository-policy paths force `change_class: repository-policy`; a weaker self-declaration cannot disable repository-policy controls.

Every human-authored PR declares whether AI/agent assistance was materially used. `agent_assistance: none` is a maintainer-controlled, **head-bound** opt-out rather than a self-attested bypass. Before it can disable the checkpoint, a target-branch global CODEOWNER must add this structured PR Conversation comment for the exact current head:

```text
<!-- ua-agent-assistance-none
{
  "agent_assistance":"none",
  "head_sha":"replace-with-current-40-character-head-sha"
}
-->
```

A later repository head invalidates that opt-out. Dependabot remains exempt when its generated body predates the declaration field. Use `not-required` only when the change is genuinely outside that companion document's scope. Maintainer exception labels are narrow, visible escapes and do not replace an explanation.

## Validation

- [ ] I read the owning documents and required dependencies.
- [ ] I checked terminology, links, metadata, compatibility, and duplicate ownership.
- [ ] I ran the relevant local validators or stated which checks were unavailable.
- [ ] I updated `CHANGELOG.md` for a notable change, or explained why no entry is required.
- [ ] The machine-readable change contract matches the PR-owned diff.
- [ ] The PR description matches the actual diff and remaining review state.

## Agent iteration checkpoint

This section applies when `agent_assistance` is `used`. AI-assisted repository-policy changes are detected from PR-owned policy paths even if the declared `change_class` is weaker; `repository-policy`, `draft-normative`, and `normative` work remains **Draft** while repository-changing work is active.

The `ua-agent-checkpoint` is bound to the PR diff-base SHA, current target-branch tip, PR head, GitHub tested merge result, PR-description SHA-256 (excluding the checkpoint block itself), deterministic trusted PR-review feedback SHA-256, and the exact effective `AGENTS.md` blobs applicable to **PR-owned** changed paths. Both the checkpoint and the change-coupling contract derive PR-owned paths from the merge-base of the current target tip and PR head, so target-only changes already synchronized into the branch do not become false PR scope. Rename scope preserves both old and new paths; copy detection is not claimed by this contract.

Before refreshing the checkpoint, re-read the effective instructions, the PR-owned full diff, this PR description, external maintainer corrective signals available in the active agent conversation, current trusted GitHub review/inline-review feedback, relevant top-level PR Conversation feedback, and the end-of-session integrity protocol. Trusted review submissions/edits/dismissals and inline review comments invalidate the deterministic feedback watermark. Ordinary top-level PR comments remain a semantic feedback surface rather than a PR-head status-check trigger because GitHub emits `issue_comment` workflows on the default-branch ref/SHA.

### Ready-for-review authorization

Ready is a two-stage control rather than a bare GitHub state change. First obtain a fresh checkpoint for the current head. Then a target-branch global CODEOWNER must add a structured approval comment bound to the exact current head, tested merge state, PR-body digest, and canonical SHA-256 fingerprint of the current `ua-agent-checkpoint` JSON:

```text
<!-- ua-agent-ready-approval
{
  "head_sha":"replace-with-current-40-character-head-sha",
  "merge_sha":"replace-with-current-40-character-tested-merge-sha",
  "pr_body_sha256":"replace-with-current-64-character-body-digest",
  "checkpoint_sha256":"replace-with-current-64-character-canonical-checkpoint-digest"
}
-->
```

Only after that approval may the PR be marked `ready_for_review`. The approval comment must already exist and must not have been edited after the Ready transition. The `ready_for_review` workflow run must itself pass the fresh checked-state validation; only then does the separate **Agent protocol / readiness authorization** job succeed.

Durable readiness is accepted only when GitHub proves that successful job came from the protected `.github/workflows/change-coupling.yml` pull-request run for the current PR head, with the expected readiness job and success step. The check is read from the PR **head SHA**; the structured approval separately binds the tested merge SHA and PR-body digest. A same-named success from another workflow does not satisfy the control.

Review or inline-review feedback on the same successfully authorized head may stale the checkpoint without revoking readiness because it does not change the approved PR-body digest. A substantive PR-description edit, a later repository commit, a changed tested-merge state, a new Ready cycle after returning to Draft, removal/edit of the approval marker, or changed approved PR-body digest requires fresh readiness evidence. Updating only the checkpoint block does not change the attested PR-description digest, so ordinary checkpoint acknowledgement can still converge without an infinite edit loop.

Existing open human-authored PRs created before `agent_assistance` was introduced must add it on their next maintained iteration. That migration is an explicit compatibility change, not silent backward compatibility.

## Uncertainty and remaining review

<!-- State assumptions, unresolved questions, unavailable evidence, and whether this PR should remain Draft. -->

<!-- ua-change-contract
{
  "change_class": "select-one",
  "agent_assistance": "select-one",
  "owning_paths": [],
  "decision_levels": [],
  "capability_families": [],
  "terminology_impact": "select-one",
  "research_state": "select-one",
  "compatibility": "select-one",
  "changelog": "select-one",
  "glossary": "select-one",
  "roadmap": "select-one",
  "traceability": "select-one"
}
-->

<!-- ua-agent-checkpoint
{
  "checkpoint_version": 1,
  "reviewed_base_sha": "replace-with-40-character-pr-diff-base-sha",
  "reviewed_base_tip_sha": "replace-with-current-40-character-target-tip-sha",
  "reviewed_head_sha": "replace-with-current-40-character-head-sha",
  "reviewed_merge_sha": "replace-with-current-40-character-tested-merge-sha",
  "reviewed_pr_body_sha256": "replace-with-current-64-character-body-digest",
  "reviewed_feedback_sha256": "replace-with-current-64-character-feedback-digest",
  "applicable_agents": [
    {
      "path": "AGENTS.md",
      "blob_sha": "replace-with-current-40-character-effective-blob-sha"
    }
  ],
  "diff_recheck": "completed",
  "pr_description_recheck": "completed",
  "corrective_feedback_review": "completed",
  "feedback_disposition": "none",
  "completion_recheck": "completed"
}
-->
