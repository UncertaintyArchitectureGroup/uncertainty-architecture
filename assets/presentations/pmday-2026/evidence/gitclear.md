---
title: "GitClear: three different maintenance signals"
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

# GitClear: three different maintenance signals

Used on slide 4. Public materials checked 2026-09-21; closed whitepapers were not obtained.

## June 2026

[The Maintainability Gap](https://www.gitclear.com/the_ai_code_quality_maintainability_gap), sections *Block duplication climbing* and *Refactoring activity collapses as copy/paste thrives*.

| Indicator | Comparison | Interpretation |
|---|---|---|
| Moved-code share | 13% in 2023; 3.8% YTD 2026 | Share of changed lines classified as moved: a reuse/refactoring proxy, **not the number of refactoring tasks** |
| Duplicated-block frequency | Approximately +81%, 2023 versus YTD 2026 | More repeated blocks; separate from moved-code share |
| Copy/paste share | 9.4% in 2022; 15.7% H1 2026 | Different baseline; do not relabel it as 2023–2026 |

The text and chart disagree on absolute duplication units. Use the relative change only; 73/40.3 − 1 ≈ 81.1% does not resolve that unit conflict. Moved-code share falls by **9.2 percentage points**, not 9.2%.

## 2025 report: older data and churn

[AI Copilot Code Quality](https://www.gitclear.com/ai_assistant_code_quality_2025_research), public abstract: 211 million changed lines, 2020–2024. Refactoring-related share declines from 25% in 2021 to below 10% in 2024; copy/paste share rises from 8.3% to 12.3% over that period. The page also reports increasing short-term churn, without a verified churn coefficient here.

Churn concerns recently written code being revised/removed; duplication concerns repeated blocks; moved code approximates reuse/refactoring. They are not interchangeable. These observational proprietary classifications do not isolate AI as the sole cause or measure all reuse and all software quality.
