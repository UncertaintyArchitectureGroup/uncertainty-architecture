# Repository-intelligence agent benchmark

This directory measures the [repository-intelligence architecture](../../REPOSITORY-INTELLIGENCE.md#14-evaluation-and-acceptance). It separates deterministic retrieval contracts, candidate-data boundaries, connector transport, and agent judgment. The corpus is not a new vocabulary or responsibility registry.

## Scope and authorship

`benchmark_cases.json` contains 12 source-derived cases specified by the integration agent against accepted commit `9facd534c7e8aeb59c2ee3003e37e44b83488516`, after exploratory baseline queries. Each case names the owning evidence. The producer and retrieval ranking were left unchanged while adding the corpus and runner.

This is **not an independently authored blind cold-start corpus**. The same agent had already implemented and reviewed the producer and knew the repository. These fixtures and the connector replay cannot establish independent decision accuracy or productivity improvement. The independent assessment required by RI-EVAL-001 remains open.

The cases cover exact responsibility recovery, historical terminology, ambiguous near-synonyms, an existing publication owner, a potentially new presentation artifact, policy validation, research authority, declared provenance, Ukrainian wording, and an English paraphrase. Cases involving creation, promotion, or synonym equivalence require source review; a passed retrieval assertion is not permission to make that decision.

## Reproduction

Use a clean explicit source state and its current generated surface:

```bash
python3 .github/scripts/repository_intelligence.py verify
python3 .github/tests/repository_intelligence/test_repository_intelligence.py
python3 .github/tests/repository_intelligence/test_agent_workflow.py
python3 .github/scripts/benchmark_repository_intelligence.py --output /tmp/repository-intelligence-benchmark.json
```

The runner reports the corpus hash, source and producer identity, per-case candidates/rank/misses, full-inventory counts, and serialized response bytes. It exits 1 for mandatory failures and 2 for invalid inputs or unavailable/stale context. The default `repository-preflight-v1` suite requires all 12 stable case IDs, their operations, and their eight mandatory/four advisory classifications; missing or reclassified cases fail before scoring. CI explicitly selects this suite. Small or independently authored exploratory corpora require `--suite exploratory`, and the report labels that limited scope. Changing `--cases` alone cannot disable the standard coverage check.

Every term/artifact preflight compares its complete returned inventory with the verified source inventory, including record contents and duplicate multiplicity; matching one glossary path or a subset is insufficient. Cases can require exact role sets for specified owner paths. Those role assertions check machine-visible classification, not an agent's semantic decision. CI runs this inside the existing metadata-integrity job and uploads the report for seven days on PR runs, including a report containing mandatory failures when generation succeeded.

CI also passes `--record-checkout`. After successful freshness validation, the runner requires a clean Git checkout and a committed surface whose bytes match its Git blob. Its report and `Verified context checkout` log line record the actual checkout commit/tree, surface path, Git blob SHA, and content SHA-256. A connector reader checks that record against the intended source state and pinned JSON. On `pull_request`, the check/run head SHA can differ from the checked merge SHA. The record cannot certify another ref, replace current-target/head/merge verification, or provide target-owned attestation for candidate-modifiable code.

Raw and source-grounded queries are evaluated separately. A successful grounded retry never rewrites a failed raw result. The runner queries the local producer and makes no model/network calls. The Git-boundary regressions exercise the producer API in disposable repositories; candidate CI results remain implementation evidence, not target-owned attestation.

## Initial deterministic observations

Baseline source: accepted `9facd534c7e8aeb59c2ee3003e37e44b83488516`, producer version 6. The compact surface contains 48 artifacts, 46 terms, and 167 high-value edges.

| Group | Observed result | Meaning |
|---|---|---|
| Eight mandatory cases | 8 passed | Declared retrieval/inventory/routing expectations were met |
| Four advisory language cases | 2 raw passes, 2 raw misses | The current lexical baseline does not understand arbitrary Ukrainian wording |
| Four separately grounded retries | Expected owner at rank 1 in all four | Canonical names/paths work after source-grounded interpretation |
| Historical predecessor | `Behavioral Software` includes `Thinking System` | Source reading must preserve the distinction between current term and historical wording |
| Potential new presentation artifact | Full inventory remains visible; ranked candidates empty | Creation still requires owner/proportionality review |
| Source-basis query | Control-loop anatomy appears at rank 5 | Direct provenance is usable retrieval evidence, without dependency propagation |

The two raw misses are RI-COLD-009 and RI-COLD-010. They are retained as misses. The agent route uses explicit source-grounded retries or live-source fallback; no translation dictionary, embeddings, or semantic authority rules were added to the producer.

Initial narrow-operation responses ranged from 322 to 59,154 UTF-8 bytes. `context-for-task` measured 23,180 bytes for `contribution-workflow`, 48,895 for `PDF export`, and 33,625 for `research-state-register`. These are serialized local response sizes, not model token measurements or connector traffic.

## Live connector transport observation

The same five files were fetched successfully through the connected GitHub tool in ChatGPT Work at the accepted commit above. Every complete response was compared byte-for-byte with the pinned Git blob; the JSON parsed with all 48 artifacts and 46 terms. The physical client/device and its screen rendering were not instrumented.

| Pinned file | UTF-8 bytes | SHA-256 of returned content |
|---|---:|---|
| `AGENTS.md` | 22,390 | `2d770fcd28a4ee05adaaf6199c0cd5dbbf2328ba6ebd2e3681f9f19ffd2a6076` |
| `CONTRIBUTING.md` | 27,803 | `08d18aa2f06f09d6cccfff8bb4bc06fea3660b0db42668e2dd00d263591ced7d` |
| `00-doctrine/glossary.md` | 22,176 | `93d267311faca69d8180b9196dd471f936910d352586b88702674b112b733270` |
| `quartz/PDF-EXPORT.md` | 13,093 | `b582a0c99c9ba80ed4813c24c2878da7d1c5b6f51eaaeb41be88a623f403827e` |
| `assets/repository-intelligence/agent-context.json` | 207,713 | `7bd0dbe91660d710572ef4437fb78e83345bb15d47e3324b9735ed8864cf199e` |

For the known contribution-workflow case, the direct file selection (`AGENTS.md` plus `CONTRIBUTING.md`) totals 50,193 bytes in two reads. Adding the complete context surface totals 257,906 bytes in three reads. These are two cost profiles calculated from the observed file responses, **not two independently observed cold-start sessions**. This exact-owner case does not benefit from an additional cold index read. The operational route therefore retains direct source reading for known owners and reuses a verified index at the same source state when broader preflight is useful.

Broad searches before decision, files opened before a correct material decision, model input tokens, duplicate proposals, missed companions in actual work, and maintainer corrections remain unmeasured. They must not be reported as zero. Passing transport/fixture checks does not establish overall iPad acceptance.

## Trust and impact evidence

`test_agent_workflow.py` supplements the producer's behavioral suite with explicit behind-target head, current-target tested-merge, candidate symlink/submodule/byte-limit, producer/schema self-change, and candidate-instruction override cases. It also rejects missing/reclassified standard scenarios, incomplete or altered preflight inventories, and wrong owner roles; a stale-head/fresh-merge fixture verifies that checkout evidence identifies the merge rather than the head. The existing suite supplies relation direction/provenance, shared-control-hub, full-tree projection equivalence, and bounded interpretation-read coverage. A changed candidate instruction cannot override an accepted input limit.

For the first real post-merge PR, run the producer from a separate checkout of the current accepted target, independently verify its interpretation blobs, and pass that PR's live tested-merge SHA as data. Keep target/head/merge IDs and the comparison outcome in the checked PR description; do not embed a self-referential current head SHA into this source record. The producer/parser/interpretation contract are unchanged in this integration PR, so comparison can use the already accepted implementation.

## Independent acceptance still required

1. Have a separate assessor author or select held-out tasks without adapting them to observed rankings, then freeze their expected evidence and corpus hash before the run.
2. Run manual-live and compact-preflight routes in separate fresh sessions at the same Git state, preserving the original query and every source-grounded retry.
3. Record actual connector reads/searches, opened sources, and available token measurements; assess proposals and material decisions against owning sources with maintainer review.
4. Exercise missing/stale context, language/paraphrase cases, a valid new artifact, near-synonyms, and the actual iPad/client fallback path. Record failures and unavailable measurements explicitly.
5. Decide whether measured mistakes or cost justify a specific retrieval change. Do not mark the independent benchmark or the architecture stop/go gate complete solely because this fixture job is green.
