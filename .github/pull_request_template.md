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

The machine-readable block below is validated against the actual git diff. Keep the human-readable fields and JSON declaration consistent. Every human-authored PR declares whether AI/agent assistance was materially used. `agent_assistance: none` does not activate the agent checkpoint. Use `not-required` only when the change is genuinely outside that companion document's scope. Maintainer exception labels are narrow, visible escapes and do not replace an explanation.

## Validation

- [ ] I read the owning documents and required dependencies.
- [ ] I checked terminology, links, metadata, compatibility, and duplicate ownership.
- [ ] I ran the relevant local validators or stated which checks were unavailable.
- [ ] I updated `CHANGELOG.md` for a notable change, or explained why no entry is required.
- [ ] The machine-readable change contract matches the actual diff.
- [ ] The PR description matches the actual diff and remaining review state.

## Agent iteration checkpoint

This section applies only when `agent_assistance` is `used`. AI-assisted `repository-policy`, `draft-normative`, and `normative` pull requests remain **Draft** while repository-changing work is active. After the current head has a fresh checkpoint, an explicitly maintainer-authorized `ready_for_review` transition records that head as ready. Review, inline-review-comment, label, or checkpoint-only PR-description events on that same head may require a fresh checkpoint without revoking readiness. Any later repository commit/head change requires returning the PR to Draft before that new repository-changing iteration can pass the checkpoint.

The `ua-agent-checkpoint` is bound to the PR diff-base SHA, current target-branch tip, PR head, GitHub tested merge result, PR-description SHA-256 (excluding the checkpoint block itself), deterministic trusted PR-review feedback SHA-256, and the exact effective `AGENTS.md` blobs applicable to **PR-owned** changed paths. PR-owned paths are computed from the merge-base of the current target tip and PR head, so target-only changes already synchronized into the branch do not become false agent scope.

Before refreshing the checkpoint, re-read the effective instructions, the PR-owned full diff, this PR description, external maintainer corrective signals available in the active agent conversation, current trusted GitHub review/inline-review feedback, and the end-of-session integrity protocol. Trusted review submissions/edits/dismissals and inline review comments invalidate the deterministic feedback watermark. Top-level PR conversation comments remain a semantic feedback surface but are deliberately not represented as a PR-head status-check trigger because GitHub emits `issue_comment` workflows on the default-branch ref/SHA; they must be reconsidered at the next checkpoint. Updating only the checkpoint block does not change the attested PR-description digest, so the acknowledgement can converge without another code commit or an infinite edit loop.

Dependabot is treated as `agent_assistance: none` when its generated PR body predates this declaration field. Existing open human-authored PRs created before this field was introduced must add `agent_assistance` on their next maintained iteration; that migration is an explicit compatibility change, not silent backward compatibility.

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
