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

Used on slide 4. Public materials checked 2026-09-21; closed whitepapers were not obtained.

## Public 2026 summary

[The Maintainability Gap](https://www.gitclear.com/the_ai_code_quality_maintainability_gap), sections *Block duplication climbing* and *Refactoring activity collapses as copy/paste thrives*.

| Indicator | Comparison | Interpretation |
|---|---|---|
| Moved-code share | 13% in 2023; 3.8% YTD 2026 | Share of changed lines classified as moved: a reuse/refactoring proxy, **not the number of refactoring tasks** |
| Duplicated-block frequency | Approximately +81%, 2023 versus YTD 2026 | More repeated blocks; separate from moved-code share |
| Function-call density | 343 → 223 calls per 1,000 changed lines, 2023 → YTD 2026 (≈−35%) | Connectivity proxy, not all reuse |
| Two-week churn | +15% in the 2026 public summary; standalone baseline values not provided | Recently written lines revised/removed within two weeks; relative change, not percentage points or a defect rate |
| Legacy-update share | 1.7% → 0.46% YTD 2026 | Summary says baseline 2022, detailed paragraph says 2023; retained in notes with this discrepancy |
| Copy/paste share | 9.4% in 2022; 15.7% H1 2026 | Different baseline; do not relabel it as 2023–2026 |

The text and chart disagree on absolute duplication units. Use the relative change only; 73/40.3 − 1 ≈ 81.1% does not resolve that unit conflict. Moved-code share falls by **9.2 percentage points**, not 9.2%.

## 2025 report: older data and churn

[AI Copilot Code Quality](https://www.gitclear.com/ai_assistant_code_quality_2025_research), public abstract: 211 million changed lines, 2020–2024. Refactoring-related share declines from 25% in 2021 to below 10% in 2024; copy/paste share rises from 8.3% to 12.3% over that period. The page also reports increasing short-term churn, without a verified churn coefficient here.

Churn concerns recently written code being revised/removed; duplication concerns repeated blocks; moved code approximates reuse/refactoring. They are not interchangeable. These observational proprietary classifications do not isolate AI as the sole cause or measure all reuse and all software quality.

## Current slide interpretation

The four visible metrics separate moved lines, function calls, block duplication and two-week churn. Public text rechecked on 2026-09-21 in the sections *New code increasingly stands alone*, *Legacy code: not gone, just forgotten*, and the introductory summary. The heading graph indexes reuse/risk signals to 2023, while the introductory legacy baseline says 2022. Do not silently apply one period to every signal. The historical 2025 note above describes the older report; it does not negate the explicitly reported 2026 churn result.

## Numerical recheck, 2026-09-21

The public summary directly prints 13% and 3.8%, 343 and 223, +81% and +15%. The slide now displays the **343 → 223 calls per 1,000 changed lines** pair; `(223/343 − 1) × 100 = −34.9854…%`, so −35% was a correct rounded relative decrease. Duplication is explicitly approximate on the slide: `(73.0/40.3 − 1) × 100 = 81.1414…%`; this arithmetic does not resolve the source's conflicting absolute units. Churn **+15%** remains labeled as reported: a separate baseline pair is unavailable in the public summary, so it cannot be independently recomputed from that page. These are not percentage-point changes.

The checked page does not establish an exact publication month. The visible heading therefore says **2026 summary**, replacing the previously assigned June date. The moved/calls/duplication period is **2023 → YTD 2026**; the slide explicitly distinguishes the unstated churn baseline. No raw-data replication or full-whitepaper verification is claimed.

## Meaning and direction of the two proxies

The public [signal definitions](https://www.gitclear.com/industry_stats/ai_code_quality_signal_graphs) describe moved-line share as a refactoring proxy and method-call density as connectivity between newly authored and existing code. Rechecked 2026-09-21.

- Moved share: `3.8 − 13 = −9.2` percentage points; `(3.8 / 13 − 1) × 100 = −70.769…%`, displayed as **−70.8%**. It counts moved lines, not refactoring tasks or all beneficial restructuring.
- Calls: `223 − 343 = −120` per 1,000 changed lines; `(223 / 343 − 1) × 100 = −34.9854…%`, displayed as **≈−35%**. These are code-level function/method invocations, not API traffic, rate limits or requests per second.

The talk's interpretation is conditional: less restructuring/connectivity can flag maintainability and reuse concerns, but moving code is not always an improvement and lower coupling can be intentional. Neither proxy alone decides quality, captures all refactoring/reuse, or establishes AI causality. Slide 4 states this visibly. The churn asterisk keeps its unavailable raw baseline separate from the 2023→YTD 2026 comparisons.


## Churn comparison rechecked, 2026-09-23

The older [Coding on Copilot public abstract](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality) covers 2020–2023 and **projects** roughly twice the two-week churn in 2024 relative to 2021. That is approximately +100% relative growth in a projection, not an observed 2024 endpoint. The [2026 summary](https://www.gitclear.com/the_ai_code_quality_maintainability_gap) explicitly reports +15%, without separate churn endpoints. Different periods, samples and forecast/observation status prevent a direct comparison or a claim that churn improved. Slide 4 now makes the missing standalone baseline explicit. No full-whitepaper or raw-data verification is claimed.
