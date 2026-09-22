# Baseline task calibration pilot, September 22

## Purpose and authorization

The maintainer requests design and execution of a pilot in Draft PR #125 to
find tasks sensitive to repository mistakes after the previous score ceiling.
This separate study calibrates tasks, not RI benefit. No previous outcomes are
reused, repaired, regraded or counted as new observations. Production guidance
and the general RI-EVAL acceptance decision remain unchanged.

## Frozen design

Four separately authored synthetic but repository-grounded tasks; two fresh
baseline sessions per task, eight first outcomes total. C1/C2 review mixed
faulty and legitimate changes, C3 produces concrete bounded replacement text
and companion decisions, C4 applies concepts to a novel operational scenario.
An author with no inherited conversation or previous benchmark access writes
prompts, fixtures, reference solutions and itemized criteria from the pinned
ordinary sources. An independent preflight checks source support and rubric
fairness before freeze; changes and reasons are preserved. These are convenience
cases, not a random sample of maintainer work or independent human authorship.

All participants get original AGENTS guidance and ordinary repository access;
generated RI and RI operations are unavailable. Knowing that RI exists through
ordinary instructions is disclosed and is not equivalent to using its outputs.
There is no treatment arm and no selection based on RI wins. Fixed slot order:
CP01 C1, CP02 C2, CP03 C3, CP04 C4, CP05 C1, CP06 C2, CP07 C3, CP08 C4.

Source is the accepted d4b1bc57b0f225b055dfc6f11732d5c9e4b4fd07 Git archive,
verified by a complete SHA-256 manifest. Same source, transport, inherited
native model configuration and 90-reader-operation limit for every slot,
including initial-message pages, fixture reads, errors and rereads. Pages are
10000 Unicode characters. Output target is up to 1400 words plus requested
replacement sections; no penalty for length alone. Fixtures are hypothetical
proposals, not authority or live repository changes. No model/reasoning override.
Exact backend, platform framing and actual token usage are unavailable.

## Execution and transport

Each slot is one fresh native Work agent with fork_turns=none. It receives
only its bootstrap, full logged starting message, its fixtures and allowed
pinned sources. Root AGENTS must be read in full and scoped instructions when
applicable, together with complete task-critical owning sources. Experimental
unavailability overrides instructions to call RI; ordinary fallback applies.

The reader checks the same manifest/path restrictions on read, search and list,
blocks generated RI, direct RI scripts and benchmark corpora, and denies escape
or symlink access. Other tools remain technically available: restriction to the
reader is instructional, not OS or platform isolation. Logs attest reader
traffic only. Preserve all observed/reported deviations. A known forbidden
read, materially incomplete required read, wrong source or missing first answer
makes that slot unusable for calibration, while its outcome remains published.
No follow-up hints, selective retries, outcome-driven revisions or replacements.

Participants return their first final substantive answer. Draft replacements
are returned as verbatim fenced text with exact target paths/headings, without
changing the live repository. Refusals and interruptions remain outcomes.
Save author/preflight decisions and smoke checks, then publish exact inputs,
criteria, messages, source manifest, reader and this protocol before dispatch.
Publish each first outcome and complete reader journal in its own PR commit,
verify the remote branch/tree, then dispatch a replacement queue slot. At most
three participants concurrently. Publication failure stops new dispatches.

## Assessment and predeclared classification

A fresh separate assessor receives shuffled opaque verbatim answers, task
inputs, frozen item-level criteria, reference solutions and ordinary evidence.
It does not receive session ordering, replicate mapping or cost. It marks each
criterion met, partial, unmet or ambiguous and explains concrete needed
corrections with sources. It separately reports false objections to legitimate
controls, serious errors, implementation completeness and rubric defects.
Assessment is agent judgment, not human replication. Freeze its first completed
assessment before joining the replicate mapping; no changing scores to favor
selection. Disclose answer text that reveals condition or task identity.

Primary calibration uses material criteria only: met=1, partial=0.5, unmet=0.
Report the numerator and denominator, not an understanding percentage. Minor
criteria, serious errors and false objections are separately visible. Exclude
ambiguous criteria from a descriptive total and report the original denominator;
any materially ambiguous task cannot qualify without a new independently frozen
variant. Missing/invalid outcomes likewise prevent qualification.

For two valid, unambiguous outcomes with n material criteria:
- Ceiling: both meet all material criteria and all legitimate controls, with
  no serious errors; task did not expose a relevant gap in this pilot.
- Floor: both meet fewer than half of material criteria; revise task scope or
  transport before using it, not evidence of useful discrimination.
- Candidate: at least one substantive material omission/error or false objection,
  neither outcome below half the material total, no rubric defect that explains
  the miss, and the task remains solvable from supplied sources. This merely
  nominates a task family; it does not validate RI sensitivity or efficacy.
- Mixed: any other valid pattern; further independent calibration needed.
- Ambiguous/invalid/transport-limited: classify explicitly, do not promote.

A failure caused only by the operation ceiling cannot establish task quality.
After exactly eight original slots, stop regardless of result. Report every
case, even if none qualify. No main-comparison launch is part of this pilot.

## Costs, interpretation and next study

Measure every rendered reader-response byte plus exact bootstrap bytes, all
reader operations by category, source paths and answer bytes. Bytes are not
tokens, money or latency. Tool elapsed time is not agent completion time;
authoring, review and scoring overhead are separate. Do not combine this study
with earlier trials for significance or equivalence claims.

Use the calibration results to propose task families and clarify rubrics for
NEW held-out tasks in a later AGENTS versus AGENTS+optional native RI comparison.
Do not recycle these answers, select tasks because RI wins, or assume a larger
sample cures ceiling. Freeze practical minimum effect, quality regressions,
cost metric, missing-data policy and sample size before that separate study.
If no task qualifies, explicitly report that a usable instrument was not found.
