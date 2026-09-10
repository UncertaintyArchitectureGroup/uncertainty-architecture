# Repository Intelligence A/B Evaluation Protocol

> Protocol version: 11 — bounded initial comparison; supersedes unexecuted v10.

## Purpose and scope

Decide whether the normal connector-based RI workflow helps with real repository tasks enough to justify its cost. This is a **preliminary engineering comparison of 12 tasks / 24 fresh sessions**, not completion of every [RI-EVAL-001 acceptance requirement](../../REPOSITORY-INTELLIGENCE.md#14-evaluation-and-acceptance), a statistical claim, or proof of graph/Control Map value. Publish the per-task evidence and remaining scenario gaps with any conclusion.

## 1. Prepare one study

Use [`ab_preregistration.example.json`](ab_preregistration.example.json) for the study settings and 12 tasks. An assessor independent of the RI implementation selects real maintainer requests before seeing A/B outcomes. Record the selection rationale and each request's source reference. Include known-owner, ambiguous/near-synonym, new-artifact/overlap, validation-routing, authority, and fallback decisions where actual work supplies them. Preserve the original language; repository outputs remain English.

For each task freeze the exact prompt, acceptable outcomes and required owning evidence in `expected`, and concrete `serious_errors`. Keep answers and the other tasks out of model sessions. Global scoring anchors are: **0** materially incorrect; **1** partially correct but needs a maintainer correction; **2** meets all frozen expectations, including sources, authority and applicable companions. A serious error always scores 0. The independent scorer judges semantic correctness; JSON validation cannot do that.

Freeze the study file before execution, including model/thinking/client settings, exact repository commit, complete compact-surface SHA-256, one context metric, and a concrete `follow_up_rule`. Fix task order before running; odd-numbered tasks run Control then Treatment, even-numbered tasks Treatment then Control. This counterbalances order without separate randomization files. The convenience sample and alternating order limit generalization; do not call it a random population sample.

A follow-up is a separate study with new frozen tasks if the initial evidence leaves a specified decision unresolved. Report the initial outcome unchanged. No selective reruns or corpus/threshold changes after observing results.

## 2. Arms and ordinary workflow

Both arms use the same applicable `AGENTS.md`, source-reading and authority rules, model/client settings and task prompt.

- **A / `RI-AB-CONTROL`:** ordinary live-GitHub reading/search with RI aids unavailable.
- **B / `RI-AB-TREATMENT`:** the normal [connector agent route](../../REPOSITORY-INTELLIGENCE.md#operational-agent-route). A known owner can be read directly. Fetch the compact surface when useful, verify it, reuse it within that session, and read authoritative sources. Do not force an index fetch for every task.

Missing, stale or truncated RI is an observed operational condition: record the attempt and use ordinary-source fallback. Do not treat it as successful verified delivery. B may legitimately never read RI. The report records attempted and verified RI use; no verified use means the study cannot label a difference as RI benefit. Accepting unverifiable RI as current evidence is a serious scoring error.

Local CLI, dedicated adapters, task-specific RI query helpers, full Graph View and Control Map are outside this connector comparison. There is no third data-only arm. Fresh sessions intentionally do not measure cross-session caching. The model sees its arm marker, so observer effects remain a limitation.

## 3. Source state, smoke and execution window

Prepare tasks and scoring expectations before requesting an execution window. Smoke-test the actual client without scoring: ordinary search, exact-ref reads, compact delivery/fallback, access parity and capture of visible tool events. Record the smoke evidence once. Verify the compact surface's freshness at the study commit using the normal RI route and record its full-content SHA-256.

Only for the 24 primary sessions, hold the default branch at the study commit. Record one GitHub branch-tip observation immediately before the first session and another immediately after the last, with immutable evidence references in `source_window`. Release the mutation freeze as soon as primary evidence is captured; preparation and scoring do not hold it. If the branch has moved since preparation, recheck tasks/keys against the new study commit and freeze the updated study **before** any primary run. If the execution lock fails, report INCONCLUSIVE.

Every direct read uses the full 40-hex study SHA, or the default branch/null ref with its own `observed_ref_sha` proving the study SHA. Ordinary search/code search may use the default branch/null ref under the shared execution lock. A contradictory explicit/resolved ref is invalid. These per-read checks remain even though repetitive per-session tip events are removed.

Each run uses a fresh conversation with Memory disabled, no Project/workspace/prior repository context, no previous-arm output and no scoring feedback. Confirm these conditions and configuration parity once for the run bundle; record exceptions in the affected run's `deviations`. A session ID cannot be reused. These are auditable execution obligations, not facts proved by a boolean.

## 4. Record primary evidence once

Generate the 24 ordered message/record skeletons with `init`. Paste each `submitted_message` into its own session. Fill its session ID, exact visible response, immutable transcript/capture `evidence` reference, chronological `events`, deviations, and actual exposed input tokens or null. Do not put scores into this file. [`ab_run_record.example.json`](ab_run_record.example.json) shows one completed record; `init` creates the complete structure.

For each repository interaction record actual normalized `tool: GitHub`, operation, repository, resource, ref, and `response_bytes` (non-negative integer or null). Use `fetch` for file reads with canonical repository-relative paths, `search|code_search` for search, and `inspect` for repository/tree/commit/check metadata with the actual endpoint or record identifier. Metadata reads, including the normal RI freshness check, must establish the study SHA too. Preserve real transport and source evidence; do not relabel local calls. All recorded calls count toward orientation cost, including failed RI attempts and repeated reads. There is no phase field to hide context acquisition as infrastructure.

Ordinary events need no RI metadata. RI events use `kind: ri_compact|ri_other`. The compact path or its content hash also identifies RI regardless of the label. A compact fetch records `delivery: verified|unavailable|unverified`; verified delivery needs the SHA-256 of the **complete returned content** matching the frozen surface. For chunked/truncated responses, record each actual call, reconstruct complete bytes only when observable, and mark verification on the completing call; an unverifiable payload requires fallback. No byte offsets, per-chunk hashes, or compulsory exactly-once coverage ledger is required. Inspect response text/transcript for unlabelled RI excerpts; classification of content without a known path/hash remains the recorder's responsibility.

The evaluator derives all counts, bytes, response IDs and hashes. It checks the supplied structured records; it does not re-extract events from arbitrary client transcripts or prove settings, independence, immutability of a reference, or external scorer blindness. Preserve raw evidence for audit rather than manufacture missing measurements. `input_tokens` and `response_bytes` accept only non-negative integers or null, never estimates, strings, booleans or fractions.

## 5. Blind scoring

After primary evidence is frozen, `prepare` builds an arm-hidden packet from the study and records: opaque response IDs, task prompts, frozen expectations, exact responses and blank scores. Entries are sorted by opaque ID, not execution order. Give the scorer only that packet; withhold the study settings/order and run bundle. The packet exposes no arm, tools, cost or delivery metadata. Response text itself may reveal the route; report that limitation rather than rewrite responses.

The scorer fills only `scorer`, `scored_before_reveal`, `quality` and `serious_error`. Freeze the scored packet before revealing arms. `score` binds it to the exact study/run digests and response content. Unknown packet fields or altered task/answer content are rejected. [`ab_blind_scoring.example.json`](ab_blind_scoring.example.json) illustrates the shape; generate actual packets instead of entering hashes manually.

## 6. Four outcomes and visible tradeoffs

Always report every pair, invalidity reasons, quality wins/losses/ties, new/removed serious errors, calls, bytes, available tokens and RI use. There is one fixed engineering rule for this initial sample:

| Outcome | Rule |
|---|---|
| `INCONCLUSIVE` | Any missing/invalid pair, unconfirmed session conditions or failed source window; partial valid results remain descriptive |
| `REGRESSION` | All 12 pairs valid and any Treatment quality loss or new serious error |
| `BENEFIT SHOWN` | All pairs valid, no quality loss/new serious error, at least one verified B RI read, and either at least two quality wins reaching score 2 with total connector calls B/A <=1.50, or every B answer scores 2 with total calls B/A <=0.80 and measured total context B/A <=1.00 |
| `NO BENEFIT SHOWN` | Complete valid sample meets neither regression nor benefit rule |

Costs use totals over the **same 12 task pairs**, with per-pair values visible. Freeze the context metric as `repository_response_utf8_bytes`, `input_tokens`, or `unavailable`; do not choose the favorable metric afterwards. Any missing measurement disables that context comparison and efficiency claim. `0/0` is 1; positive/0 is unbounded (JSON null and a failed gate). A quality benefit may still cost more context; show that tradeoff explicitly. These modest thresholds are an initial decision aid, not significance or universal acceptance floors. A known regression remains visible in the per-pair evidence even if another invalid pair makes the overall result inconclusive.

## 7. Commands and completion

Three evidence files are sufficient: study, runs (including raw-evidence references), and blind scores. No sampling-frame/pool files, hidden seeds, separate wave packs, or manual aggregate fields are needed.

```bash
python3 .github/scripts/score_repository_intelligence_ab.py init \
  --study /secure/study.json --output /secure/runs.json
# Run the sessions and complete runs.json, then freeze it.
python3 .github/scripts/score_repository_intelligence_ab.py prepare \
  --study /secure/study.json --runs /secure/runs.json --output /secure/blind.json
# The independent scorer completes and freezes blind.json before arm reveal.
python3 .github/scripts/score_repository_intelligence_ab.py score \
  --study /secure/study.json --runs /secure/runs.json \
  --scores /secure/blind.json --output /secure/report.json
```

Commands use Python's standard library. Schema/evidence contradictions return exit code 2; a well-formed but invalid/incomplete experiment writes INCONCLUSIVE with exit code 0. Output files must be new paths, so a rerun cannot overwrite frozen evidence accidentally. This tool prepares records and analyzes evidence; it does not execute model sessions.

Publish a separate results PR regardless of outcome, with selected tasks, frozen evidence, measured costs, limitations, actual client identity and remaining RI-EVAL scenario gaps. Existing deterministic boundary tests remain required; passing this preliminary comparison does not replace independent agent-judgment coverage, physical-device acceptance, or the architecture stop/go decision.
