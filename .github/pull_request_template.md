## Summary

<!-- What changed, why it belongs in this repository, and the smallest coherent decision represented by this PR. -->

## Repository placement

- **Change class:** <!-- maintenance | repository-policy | research | draft-normative | normative | reference | history | publishing -->
- **Owning path or module:**
- **Decision levels affected:** <!-- organization | project | delivery | runtime | none -->
- **Capability families affected:** <!-- constraints | sensors | controllers | actuators | none -->

## Companion updates

- **Changelog:** <!-- updated | not-required: reason -->
- **Glossary:** <!-- updated | unchanged | not-applicable -->
- **Roadmap:** <!-- updated | unchanged | not-applicable -->
- **Research traceability:** <!-- updated | unchanged | not-applicable -->
- **Compatibility / migration:** <!-- preserved | changed: explain | not-applicable -->

The machine-readable block below is validated against the actual git diff. Keep the human-readable fields and JSON declaration consistent. Use `not-required` only when the change is genuinely outside that companion document's scope. Maintainer exception labels are narrow, visible escapes and do not replace an explanation.

## Validation

- [ ] I read the owning documents and required dependencies from `AGENTS.md`.
- [ ] I checked terminology, links, metadata, compatibility, and duplicate ownership.
- [ ] I ran the relevant local validators or stated which checks were unavailable.
- [ ] I updated `CHANGELOG.md` for a notable change, or explained why no entry is required.
- [ ] The machine-readable change contract matches the actual diff.
- [ ] The PR description matches the actual diff and remaining review state.

## Agent iteration checkpoint

For AI-assisted PR work, update `ua-agent-checkpoint` after every change to the reviewed PR state. The checkpoint is intentionally bound to the exact base SHA, head SHA, PR-description SHA-256 (excluding the checkpoint block itself), and blob SHA of every `AGENTS.md` file applicable to the current diff. Before updating it, re-read those instructions, the full current diff, this PR description, available maintainer corrective feedback, and the end-of-session integrity protocol.

A new commit, base retarget, or PR-description edit makes the prior attestation stale. Updating only the checkpoint block does not change the attested PR-description digest, so the acknowledgement can converge without another code commit or an infinite edit loop.

Dependabot PRs are excluded from this checkpoint because Dependabot cannot maintain the attestation block itself; normal maintainer review and the other repository controls still apply.

## Uncertainty and remaining review

<!-- State assumptions, unresolved questions, unavailable evidence, and whether this PR should remain Draft. -->

<!-- ua-change-contract
{
  "change_class": "select-one",
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
  "reviewed_base_sha": "replace-with-current-40-character-base-sha",
  "reviewed_head_sha": "replace-with-current-40-character-head-sha",
  "reviewed_pr_body_sha256": "replace-with-current-64-character-body-digest",
  "applicable_agents": [
    {
      "path": "AGENTS.md",
      "blob_sha": "replace-with-current-40-character-blob-sha"
    }
  ],
  "diff_recheck": "completed",
  "pr_description_recheck": "completed",
  "corrective_feedback_review": "completed",
  "feedback_disposition": "none",
  "completion_recheck": "completed"
}
-->
