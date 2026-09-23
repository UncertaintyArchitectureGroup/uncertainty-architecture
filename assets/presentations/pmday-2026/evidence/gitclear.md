---
title: "GitClear: distinct maintenance signals"
artifact_type: repository-guide
status: informative
maturity: draft
module: publishing
draft: true
topics:
  - provenance
tags:
  - ua/module/publishing
  - ua/type/repository-guide
  - ua/status/informative
  - ua/topic/provenance
---

# GitClear: distinct maintenance signals

Used on slide 4. Rechecked 2026-09-23 using the **full official 2025 PDF**, the **2026 public summary**, and the author's **2023-indexed chart**. The full 2026 whitepaper and raw database were not obtained. This record supersedes earlier notes saying no full report was read or that the +15% churn baseline year was unknown; earlier speaker-note prefixes remain historical, with the current clarification appended.

## Sources and data status

- [2025 PDF v2025.2.5](https://gitclear-public.s3.us-west-2.amazonaws.com/GitClear-AI-Copilot-Code-Quality-2025.pdf): February 2025, observations for 2020–2024 and projections for 2025. Use **Appendix A1, PDF page index 23 (24th page)** consistently for precise percentages. The body table on page index 6 has slightly different rounded values; do not mix the two tables. A0 defines the operations and two-week churn.
- [2026 Maintainability Gap summary](https://www.gitclear.com/the_ai_code_quality_maintainability_gap): moved-code endpoint is YTD 2026; copy/paste endpoint is H1 2026. Calls and duplicated blocks compare 2023 with 2026. The full closed 2026 report is not claimed reviewed.
- [Author's September 2026 announcement](https://www.gitclear.com/blog/annual_ai_code_quality_research_2026_diff_digest_git_ai_diff_viewer) and [index chart](https://images.amplenote.com/737e289c-975f-11f1-ac66-bd429d4d2367/7c7d67bc-a292-4aae-8de4-7476ff61bba9.png): the chart explicitly sets **2023 = 100**, with churn around 115 in 2026. This establishes the baseline year for the reported +15%, not an absolute churn rate.

## 2021 and 2026 snapshots

| Indicator | 2021: 2025 report A1 | 2026: public summary | Arithmetic comparison |
|---|---:|---:|---|
| Moved-code share of changed lines | 24.65% | 3.8% YTD | −20.85 percentage points; −84.58%, shown as −85% |
| Copy/paste share | 8.66% | 15.7% H1 | +7.04 percentage points; +81.29%, shown as +81% |
| Two-week churn | 3.27% | Absolute rate unavailable | No exact 2021→2026 calculation |

These are **cross-edition snapshots with different samples**, not one harmonized panel or an estimate of AI causality. Even the overlapping year changes: 2023 moved share is **15.88% in 2025 A1** versus **13% in the 2026 summary**. Consequently, never multiply an older churn rate by 1.15 to invent a 2026 endpoint. The visible slide keeps this caveat beside the two snapshot rows.

2021 is a baseline before **widespread adoption**, not a full year with no AI coding tools: [GitHub announced Copilot technical preview on June 29, 2021](https://github.blog/news-insights/product-news/introducing-github-copilot-ai-pair-programmer/).

## Churn: observed, forecast, and indexed

Churn denotes authored/pushed lines substantially revised or reverted within two weeks. It is neither a defect rate nor duplication. Use A1's all-line series, not the different new-line denominator in Appendix A7.

| Period/status | Published rates | Relative change |
|---|---|---|
| **Observed 2021→2024**, 2025 A1 | 3.27% → 5.67% | `(5.67/3.27−1)×100 = +73.39%`, or +2.40 pp; slide rounds to +73% |
| **Forecast for 2025**, versus 2021, same A1 | 3.27% → projected 6.87% | +110.09%; slide rounds to +110%, explicitly forecast / not observed |
| **2023→2026 index**, 2026 public summary/chart | 2023 = 100; 2026 ≈115 | Reported +15%; no absolute 2026 rate provided |

The forecast explains the remembered growth above 100%. The older [January 2024 abstract](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality) also projected roughly doubled churn in 2024 versus 2021. Neither projection is an observed 2026 value. +15% does not show that churn improved against 2021; its baseline, report vintage and sample differ.

## Other signals retained

| Indicator | Comparison | Limits |
|---|---|---|
| Function-call density | 343 → 223 per 1,000 changed lines, 2023→2026; −120 or ≈−35% | Code-level function/method calls, not API traffic. No 2021 counterpart established. |
| Duplicated-block frequency | ≈+81%, 2023→2026 | Public text and chart disagree on absolute units, so only the relative change is used. |
| Legacy-update share | 1.7% → 0.46% | Intro baseline says 2022, detail says 2023; retained in notes, not the headline comparison. No 2021 counterpart established. |

The older PDF's duplicated-block metric is **share of commits**: 0.48% in 2021 → 6.66% in 2024 (13.875×). It must not be joined to the 2026 metric normalized by changed lines. Copy/paste share and duplicate-block frequency also have distinct definitions; their similar +81% comparisons have different periods and denominators.

Moved lines are a refactoring proxy; calls approximate connectivity, not all reuse. Smaller values may flag maintenance concerns but can also reflect intentional design. No individual proxy decides software quality or isolates AI as the cause. [GitClear's signal definitions](https://www.gitclear.com/industry_stats/ai_code_quality_signal_graphs) provide further context.
