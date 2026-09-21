---
title: PMDay 2026 — Evidence Base
artifact_type: repository-guide
status: informative
maturity: draft
module: publishing
draft: true
topics:
  - provenance
  - sdlc
tags:
  - ua/module/publishing
  - ua/type/repository-guide
  - ua/status/informative
  - ua/topic/provenance
  - ua/topic/sdlc
---

# PMDay 2026 — Evidence Base

Джерела до [AI Changes Both Sides of Software Engineering](README.md). Стан посилань і використаних редакцій: **21 вересня 2026 року**.

Цей файл збирає бібліографію, прив'язку до слайдів і межі використання. [Сценарій](README.md) залишається джерелом екранних формулювань, нотаток і розрахунків; первинні публікації — джерелом емпіричних результатів. Це покажчик до погодженої доповіді, а не новий дослідницький аудит або реєстр статусів Subprime.

## Локальні копії та читабельні нотатки

[Evidence directory](evidence/README.md) містить завантажені CC BY 4.0 PDF Agarwal та офіційної інфографіки DORA, пошуковий текст Agarwal і окремі короткі нотатки для NBER, DORA, METR, GitClear, Xu та ToC. [sources.json](evidence/sources.json) фіксує URLs, версії, ліцензії й SHA-256. Для решти джерел збережено конспекти та посилання, без перевидання повних захищених текстів.

## Основні дослідження — слайд 4

Усі шість джерел нижче використано у спільному evidence slide **The Evidence Is Already Messy**. Детальний розбір і арифметика — у [сценарії слайда 4](README.md#4-the-evidence-is-already-messy).

| Джерело та використана редакція | Що підтримує; де шукати | Межа висновку |
|---|---|---|
| **Demirer, Musolff & Yang — Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools.** NBER WP 35275, травень 2026. [Сторінка роботи](https://www.nber.org/papers/w35275) · [Оригінальний PDF](https://www.nber.org/system/files/working_papers/w35275/w35275.pdf) | Розрив між зростанням coding activity та downstream output: **17,3× changed LOC → 2,8× commits → 1,3× releases**. Figure 1, друкована с. 3; Table 5, с. 33, weeks 21–30. | Понад 100 тис. GitHub developers; matched event study, не RCT. Working paper без peer review. Це кумулятивні оцінки авторів для різних outcomes, не conversion rate. Changed LOC = additions + deletions; окремий async release effect не оцінено. |
| **Та сама робота NBER — marketplaces.** [PDF](https://www.nber.org/system/files/working_papers/w35275/w35275.pdf) | Більше нових застосунків без відповідного aggregate usage gain у розглянутих когортах: Figure 12, друкована с. 41, та §8.2. | Usage — ratings/download proxies за перші три місяці нових когорт, не весь ринок, не пряме вимірювання welfare. Три usage panels: Apple, Google Play, Chrome; SourceForge не має такого panel. Частина трендів передує агентам. |
| **DORA — State of AI-assisted Software Development, 2025.** [Сторінка повного звіту](https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report) · [Офіційне авторське резюме, 23.09.2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) · [DORA research overview](https://dora.dev/research/2025/) | У резюме: *AI, the great amplifier* та *Key findings*. 90% використовують AI; понад 80% повідомляють про приріст продуктивності; **59% — про покращення code quality** в [офіційній інфографіці](evidence/originals/dora-2025-infographic.pdf). Adoption позитивно пов'язаний із throughput/product performance і негативно — зі stability. | Майже 5 000 респондентів; асоціації та self-reports, не причинний експеримент. Звірено публічне резюме та інфографіку; повний звіт за формою не отримано. Це частки респондентів, а не відсотки приросту. Delivery stability не тотожна code quality; числовий stability coefficient тут не встановлено. Негативний throughput result 2024 не переноситься на 2025. |
| **METR — AI usage survey, 11.05.2026.** [Авторська публікація з методологією й результатами](https://metr.org/blog/2026-05-11-ai-usage-survey/) | *Methodology*, *Results → Productivity gains around March 2026*. 349 technical workers; median self-reported work-value uplift **1,4–2×**, self-reported speed **3×**. | Самообрана вибірка; це сприйняття респондентів, не виміряний delivery effect. 1,4–2× — різні формулювання питання, не confidence interval. |
| **GitClear — The Maintainability Gap: 2026 AI Code Quality Research, червень 2026.** [Публічний виклад звіту](https://www.gitclear.com/the_ai_code_quality_maintainability_gap) | *Block duplication climbing*; *Refactoring activity collapses as copy/paste thrives*. Moved/refactoring-related share **13% у 2023 → 3,8% YTD 2026**; block duplication приблизно **+81%**. | Частка moved lines — proxy reuse/refactoring, не кількість refactoring tasks. Churn — окремий сигнал зі звіту 2025 ([визначення й періоди](evidence/gitclear.md)). Спостережні code-change proxies власної класифікації; не доказ, що AI — єдина причина. Перевірено публічний текст/графік, не повний закритий whitepaper. Одиниці duplication у тексті й графіку суперечать одна одній: абсолютні 40,3/73,0 не подаємо як надійно визначену метрику. |
| **Xu et al. — AI-Assisted Programming Decreases the Productivity of Experienced Developers by Increasing the Technical Debt and Maintenance Burden.** [arXiv 2510.10165v3](https://arxiv.org/html/2510.10165v3), 28.01.2026 | §4 *Main Results*, §6 *Individual Level Heterogeneous Analyses*. Верхній activity quartile: commits **−19%**, reviews **+6,5%**; нижній: commits **+43,5%**, PRs **+17,7%**. Project-level PR rework **+2,4%**. | Дані **2020–2022**, ранній Copilot; нова дата версії не оновлює період спостережень. Activity quartiles не дорівнюють Junior/Senior; reviews — кількість, не години. |
| **Agarwal et al. — AI IDEs or Autonomous Agents? Measuring the Impact of Coding Agents on Software Development.** [arXiv 2601.13597v2](https://arxiv.org/html/2601.13597v2), 27.01.2026 | **Table 2**. Agent-first / IDE-first: cognitive complexity **+34,85% / +42,87%**; static warnings **+17,73% / +19,00%**; друга warning estimate незначуща. | Repo-level DiD і статичні proxies, не «борг на кожну фічу». Agent-first означає відсутність виявлених попередніх IDE-слідів, не гарантовану відсутність AI. |

**Доступ до NBER.** Під час повторної перевірки офіційний PDF повертав HTTP 403. Зміст, сторінки й таблиці звірено з наданим оригінальним `w35275.pdf` за травень 2026; його SHA-256: `edf1a41a6e4e4cf562571b5fac79eac07693281f88d460a81ee9f8ce1a1c65bb`. Це ідентифікує використаний файл, а не гарантує незмінність документа за зовнішнім URL. Повний copyrighted PDF тут не перевидається.

## Історичний контекст і редакторський відбір

Ці джерела пояснюють еволюцію evidence base або залишаються у нотатках; вони не є додатковими headline-оцінками сучасних агентів.

| Джерело | Використання й обмеження |
|---|---|
| [METR — Early-2025 AI and experienced open-source developers, 10.07.2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | Датований RCT у нотатках слайда 4: 16 розробників, 246 задач, **на 19% більше часу** з early-2025 AI. Не переносити результат на всі сучасні інструменти. |
| [METR — We are Changing our Developer Productivity Experiment Design, 24.02.2026](https://metr.org/blog/2026-02-24-uplift-update/) | Пояснює selection bias в оновленому дослідженні; з нього не виводимо універсальний актуальний відсоток прискорення/сповільнення. |
| [Peng et al. — The Impact of AI on Developer Productivity: Evidence from GitHub Copilot, v1, 2023](https://arxiv.org/html/2302.06590v1) | Історичний позитивний експеримент: 95 рандомізованих учасників, 70 завершень, по 35 у групі; серед завершень 71,17 проти 160,89 хвилини, скорочення часу **55,8%**. Не 196 учасників; не оцінка повного SDLC. |
| [GitClear — AI Tool Impact on Developer Productive Output, 2022–2025](https://www.gitclear.com/research/ai_tool_impact_on_developer_productive_output_from_2022_to_2025) | Історичний code-output контекст: середні added LOC 1 314 → 3 037 (**+131,1%**), медіанні 921 → 1 624 (**+76,3%**). Це не delivery productivity; не змішуємо різні вибірки/композити. |
| [GitClear — AI Assistant Code Quality, 2025](https://www.gitclear.com/ai_assistant_code_quality_2025_research) | Для основного викладу замінено звітом June 2026. Старі **211 млн changed LOC** належать цьому звіту; не підставляємо цей обсяг під метрики 2026. |

METR task-horizon estimates за березень 2025 залишаються у бібліографії Subprime; на слайд 2 їх не винесено. DORA 2024 також не використовується як доказ сучасного негативного throughput effect. Реєстрація джерела не зобов'язує використовувати його на екрані.

## Слайд 3 — Theory of Constraints і WIP

[Локальна нотатка](evidence/toc-wip.md) фіксує умови прикладу 100 − 8 = 92 зміни/тиждень. [DORA WIP limits](https://dora.dev/capabilities/wip-limits/) і [Small batches](https://dora.dev/capabilities/working-in-small-batches/) підтримують software-specific пояснення черг і затриманого feedback. ToC тут — концептуальна рамка; погіршення якості є ризиком перевантаження, а не неминучим результатом будь-якої локальної оптимізації.

## Subprime — звіт, бібліографія і provenance

- [The Subprime Code Crisis — звіт, Part 1: The Illusion of Speed](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/blob/main/report/01_the_illusion.md) — вхід до повного багаточастинного аргументу про delivery-system risk.
- [Source Registry — evidence/SOURCES.md](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/blob/main/evidence/SOURCES.md) — класифікація, стани перевірки й фактичне використання джерел у Subprime.
- [Bibliography and Data Sources — REFERENCES.md](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/blob/main/REFERENCES.md) — компактна бібліографія й навігація.
- [NBER evidence brief — Writing Code vs. Shipping Code](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/blob/main/evidence/primary/2026-writing-code-vs-shipping-code.md) — розбір результатів і меж цієї роботи.

Subprime дає synthesis і provenance для слайдів 3–7; числа атрибутуються первинним авторам вище. Його `Registered` не дорівнює `Verified`. Посилання на `main` ведуть до живих документів; цей покажчик не переносить їхні статуси автоматично в UA.

## UA — концептуальна основа другої половини

Це джерела інженерних понять і review practices, а не незалежні емпіричні підтвердження результатів AI adoption. Зафіксовані зовнішні посилання ведуть до перевіреного UA `main` **d4b1bc57b0f225b055dfc6f11732d5c9e4b4fd07**.

| Слайди | Джерело |
|---|---|
| 8 — Thinking Systems | [Uncertainty in the Controlled Object](https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/d4b1bc57b0f225b055dfc6f11732d5c9e4b4fd07/00-doctrine/uncertainty-in-the-controlled-object.md) |
| 9 — requirements і boundaries | [Requirements, Correctness, and Bugs](https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/d4b1bc57b0f225b055dfc6f11732d5c9e4b4fd07/00-doctrine/requirements-correctness-and-bugs.md) |
| 11 — DoR / DoD / Release Gate; 13 — відповідальність | [Thinking System Review](https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/d4b1bc57b0f225b055dfc6f11732d5c9e4b4fd07/01-patterns/thinking-system-review.md) |
| 12 — production control loop | [Control-Loop Capability Anatomy](https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/d4b1bc57b0f225b055dfc6f11732d5c9e4b4fd07/00-doctrine/control-loop-anatomy.md) |

**Авторський синтез та ілюстрації.** Схематична comprehension-крива слайда 5 не є виміряним графіком. Слайди 6–7 і 13–14 містять інженерну інтерпретацію та пропозиції доповідача. IT-асистент і eval **196/200 = 98%** на слайді 10 — навчальний приклад, не результат зовнішнього дослідження. Джерела не підтверджують автоматично кожен елемент авторської схеми.

## Як читати ці докази

Звірка посилань, версій, таблиць, одиниць і арифметики не є незалежним відтворенням досліджень на сирих даних. RCT, self-reports, observational DiD та commercial code proxies тут не об'єднуються в один pooled effect. LOC, releases, downloads і delivered value залишаються різними outcomes.
