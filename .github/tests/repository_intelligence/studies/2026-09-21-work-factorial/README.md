# Work factorial study, 21 September 2026

Status: execution inputs prepared; 0/12 scored sessions dispatched. The input
archive must be published on this PR branch before dispatch. See
[PROTOCOL.md](PROTOCOL.md) for the decision rules and limitations, and
[PROGRESS.md](PROGRESS.md) for the durable slot ledger.

This is a new execution of the three tasks and four conditions from the
maintainer-approved September 18 clean preparation. It does not resume or
replace old workers. The previous six reported answers are not imported.
The two previously committed studies remain unchanged.

On September 21 the maintainer approved using native Work agents with
instructional access restrictions and explicitly required publication of each
completed test in PR #125. This revises the earlier preparation's requirement
for externally enforced exclusive tool access before any execution. The
synthetic canary probe found direct shell access available; it did not find
actual experimental contamination. No OS isolation is claimed.

Inputs, exact messages, original preparation, native outputs, source manifest,
reader and pre-run checks are retained in `frozen-inputs.zip`. Each session's
first answer and complete reader journal will be published in a separate
`evidence/WFxx.zip` before another slot is launched in its place. Answers are
also published as plain text. Missing, failed or interrupted attempts remain
in the ledger. Git history preserves each publication; no selective reruns.

Only the source snapshot at `989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3` is used
by tested agents. Publication changes to this PR do not change their sources.

The tasks are organizer-authored convenience scenarios, not independently
sampled maintainer work. A separate fresh scorer will assess shuffled answers
without condition labels. Quality, measured payload and operations are
descriptive evidence; actual backend identity, all platform context, total
tokens, latency and billing are not attestable here.
