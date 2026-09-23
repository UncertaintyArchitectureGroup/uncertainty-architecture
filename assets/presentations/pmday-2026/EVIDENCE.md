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

[Evidence directory](evidence/README.md) містить завантажені CC BY 4.0 PDF Agarwal та офіційної інфографіки DORA, пошуковий текст Agarwal і окремі короткі нотатки для NBER, DORA, METR, GitClear, Xu та ToC. Також додано повний DORA v.2025.2 PDF і текст із public mirror під окремою CC BY-NC-SA 4.0 attribution. [sources.json](evidence/sources.json) фіксує URLs, версії, ліцензії й SHA-256. Для решти джерел збережено конспекти та посилання, без перевидання повних захищених текстів.

## Основні дослідження — слайд 4

Усі шість джерел нижче використано у спільному evidence slide **The Evidence Is Already Messy**. Детальний розбір і арифметика — у [сценарії слайда 4](README.md#4-the-evidence-is-already-messy).

| Джерело та використана редакція | Що підтримує; де шукати | Межа висновку |
|---|---|---|
| **Demirer, Musolff & Yang — Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools.** NBER WP 35275, травень 2026, **вереснева редакція 2026**. [Сторінка роботи](https://www.nber.org/papers/w35275) · [Оригінальний PDF](https://www.nber.org/system/files/working_papers/w35275/w35275.pdf) | Розрив між зростанням coding activity та downstream output: **25,5× changed LOC; 3,4× commits; 1,3× releases** — округлення авторів. Figure 1, друкована с. 2 / PDF p.4; Table 6, друкована с. 33 / PDF p.35, weeks 21–30. | Понад 500 тис. GitHub developers; matched event study, не RCT. Working paper без peer review. Це кумулятивні оцінки авторів для різних outcomes, не conversion rate. Changed LOC = additions + deletions; окремий async release effect не оцінено. |
| **Та сама робота NBER — marketplaces.** [PDF](https://www.nber.org/system/files/working_papers/w35275/w35275.pdf) | Usage не встигає за зростанням нових застосунків: Figure 11, друкована с. 44 / PDF p.46, та §7.2.3. iOS приблизно стабільний; Android помірно зростає; Chrome падає. iOS <10 ratings ≈78% → 87%; Chrome <10 downloads 19% → 33%, January 2025 → April 2026. | Usage — ratings/download proxies за перші три місяці нових когорт, не весь ринок, не пряме вимірювання welfare. Три usage panels: Apple, Google Play, Chrome; SourceForge не має такого panel. Частина трендів передує агентам. |
| **DORA — State of AI-assisted Software Development 2025, v.2025.2.** [Official entry](https://dora.dev/research/2025/dora-report/) · [Local full report ZIP](evidence/originals/dora-2025-v2025.2.pdf.zip) · [Detailed note](evidence/dora-2025.md) | AI adoption positively associated with throughput and negatively with stability. **Figure 28, p.38**: approximately **+0.10 SD delivery instability**, **89% credible interval ≈ +0.07…+0.13**, per **+1 SD AI adoption**. Units: p.48, note 23. Definition: p.139, change failure rate + deployment rework rate. Separately, >80% report productivity improvement and 59% code-quality improvement. | Rounded chart reading, not an exact coefficient table; survey-based observational model, not CI/CD telemetry or proof of causation. +0.10 SD is not +10% failures. Full report obtained from an attributed public mirror; CC BY-NC-SA 4.0. [Chart-reading record](evidence/dora-2025-figure28.json). |
| **METR — AI usage survey, 11.05.2026.** [Авторська публікація з методологією й результатами](https://metr.org/blog/2026-05-11-ai-usage-survey/) | *Methodology*, *Results → Productivity gains around March 2026*. 349 technical workers; median self-reported work-value uplift **1,4–2×**, self-reported speed **3×**. | Самообрана вибірка; це сприйняття респондентів, не виміряний delivery effect. 1,4–2× — різні формулювання питання, не confidence interval. |
| **GitClear — The Maintainability Gap: 2026 AI Code Quality Research, публічне резюме 2026.** [Публічний виклад звіту](https://www.gitclear.com/the_ai_code_quality_maintainability_gap) | *Block duplication climbing*; *Refactoring activity collapses as copy/paste thrives*. Moved/refactoring-related share **13% у 2023 → 3,8% YTD 2026**; block duplication приблизно **+81%**; function-call density **343 → 223 / 1000 changed lines (≈−35%)**; two-week churn **+15%** у публічному резюме 2026. | Частка moved lines — proxy reuse/refactoring, не кількість refactoring tasks. Churn — окремий від duplication сигнал, із числом +15% у резюме 2026; окремі baseline values там не наведені ([визначення й періоди](evidence/gitclear.md)). Спостережні code-change proxies власної класифікації; не доказ, що AI — єдина причина. Перевірено публічний текст/графік, не повний закритий whitepaper. Одиниці duplication у тексті й графіку суперечать одна одній: абсолютні 40,3/73,0 не подаємо як надійно визначену метрику. |
| **Xu et al. — AI-Assisted Programming Decreases the Productivity of Experienced Developers by Increasing the Technical Debt and Maintenance Burden.** [arXiv 2510.10165v3](https://arxiv.org/html/2510.10165v3), 28.01.2026 | §4 *Main Results*, §6 *Individual Level Heterogeneous Analyses*. Верхній activity quartile: commits **−19%**, reviews **+6,5%**; нижній: commits **+43,5%**, PRs **+17,7%**. Project-level PR rework **+2,4%**. | Дані **2020–2022**, ранній Copilot; нова дата версії не оновлює період спостережень. Activity quartiles не дорівнюють Junior/Senior; reviews — кількість, не години. |
| **Agarwal et al. — AI IDEs or Autonomous Agents? Measuring the Impact of Coding Agents on Software Development.** [arXiv 2601.13597v2](https://arxiv.org/html/2601.13597v2), 27.01.2026 | **Table 2**. Agent-first / IDE-first: cognitive complexity **+34,85% / +42,87%**; static warnings **+17,73% / +19,00%**; друга warning estimate незначуща. | Repo-level DiD і статичні proxies, не «борг на кожну фічу». Agent-first означає відсутність виявлених попередніх IDE-слідів, не гарантовану відсутність AI. |

**Повторна перевірка всіх чисел слайда 4, 21.09.2026.** NBER завантажено з офіційного URL: це **May 2026, Revised September 2026**, 1 437 135 bytes, SHA-256 `a11c3c7442a4299b54654ba303e791c92166e807d2b6e4f12af50087ee713711`. Старі 17,3× / 2,8×, 79% → 86% і 18% → 31% замінено; зміни редакцій описані в [NBER note](evidence/nber-35275.md). Повний PDF тут не перевидається.

| Числа на оновленому слайді | Результат звірки та точність |
|---|---|
| NBER 25,5× / 3,4× / 1,3× | Прямо надруковані у Figure 1 вересневої редакції; авторське округлення до одного десяткового знака. Releases не включають окремо ідентифікованого async-компонента. |
| iOS ≈78% → 87%; Chrome 19% → 33% | Прямий текст §7.2.3, не зчитування pixels. Авторські цілі відсотки; January 2025 → April 2026. Пороги <10 ratings / <10 downloads; usage у перші 3 місяці. |
| DORA ≈+0,10 SD; 89% interval ≈+0,07…+0,13; +1 SD adoption | Figure 28 та note 23 звірено повторно. Коефіцієнт/межі приблизні, точна числова таблиця не опублікована в перевіреному звіті; 89% — явно надрукований рівень credible interval. |
| DORA >80%; 59% | Прямі формулювання p.30 та інфографіки; частки респондентів. Не замінюємо >80% сумою округлених bins. |
| GitClear 13% → 3,8%; 343 → 223 на 1 000 changed lines | Прямі числа публічного тексту, 2023 → YTD 2026. Початкові пари доповнено абсолютними/відносними змінами: moved −9,2 в.п. (−70,8%); calls −120 (≈−35%). |
| GitClear ≈+81%; +15% churn | +81% — округлена відносна зміна; абсолютні одиниці duplication суперечливі. +15% прямо повідомлено, але без baseline-пари, тому не називаємо незалежно перерахованим. |
| METR 1,4–2×; 3 питання; May 2026 | Прямо підтверджено авторською публікацією від 11.05.2026; діапазон медіан різних питань, не інтервал невизначеності. |
| Agarwal +34,85% / +42,87%; January 2026 | Table 2 у PDF та HTML v2 збігаються; відповідно Agent-first / IDE-first, cognitive complexity. Замінено округлені +35% / +43%; ці відсотки не належать Xu. |

GitClear на слайді датовано лише **2026**: точний місяць не підтверджено перевіреною сторінкою. DORA **2025 v.2025.2** відповідає поточним офіційним errata. Жодному джерелу не приписано більшої числової точності, ніж воно публікує.

## Вимоги, оцінювання та ролі — слайди 9–14

Перевірено 21.09.2026. Це джерела для навчальної адаптації й авторських практичних пропозицій, не новий нормативний процес UA.

| Джерело | Використання | Межа висновку |
|---|---|---|
| [ISO/IEC 25059:2023 — Quality model for AI systems](https://www.iso.org/standard/80655.html), офіційний public abstract | Слайд 9: стандартизована термінологія якості AI вже існує. | Прочитано public abstract, не повний платний стандарт. Quality model не задає готову acceptance rubric для кожної семантичної відповіді конкретного продукту. Не стверджуємо «стандартів немає». |
| [NIST AI RMF 1.0, NIST AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), 2023, §1.2.2 *Risk Tolerance*, MEASURE 2.1/2.5/2.6 | Слайди 9–10: risk tolerance контекстна; рамка не приписує універсального порога. Потрібні documented measurement, обмеження та співвіднесення з прийнятим ризиком. | Метод вимірювання не вирішує за бізнес, які наслідки прийнятні. Розподіл роботи між Product/BA/QA/Dev у доповіді — наша прикладна пропозиція, не prescribed NIST job titles. |
| [NIST Generative AI Profile, NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), 2024, GV-3.2-003; MP-1.1-002/003; MG-3.2-009 | Слайди 9–10: acceptable use, спільне з domain experts визначення контексту/меж, risk measurement plan і організаційна tolerance. | Не є мовою, яка однозначно класифікує всі можливі LLM outputs, і не робить prompt детермінованою гарантією. |
| [Ribeiro, Wu, Guestrin & Singh — Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://aclanthology.org/2020.acl-main.442/), ACL 2020, pp. 4902–4912 | Слайди 9–10: research proposal для структурування behavioral tests через linguistic capabilities та типи перевірок; приклади, контрприклади, invariance. | Робота про NLP behavioral testing, не універсальний стандарт для всіх Thinking Systems і не спосіб автоматично визначити business risk tolerance. Її емпіричні коефіцієнти на слайди не переносимо. |
| [NIST Engineering Statistics Handbook §7.2.4.1 — Confidence intervals](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm), Wilson score method | Слайд 10: двосторонній 95% interval для частки неприйнятних результатів у **навчальному** прикладі 4/200. | Незалежні репрезентативні evaluation units зі стабільного цільового розподілу; не повтори одного кейсу, не гарантія production, не рекомендований sample size. |

**Перерахунок прикладу:** `p̂ = 4/200 = 0.02`, `z = 1.959963984540054`; Wilson center `(p̂ + z²/(2n))/(1 + z²/n)`, half-width `z × sqrt(p̂(1−p̂)/n + z²/(4n²))/(1 + z²/n)`. Межі **0,78044264% та 5,02870869%**, на екрані **≈0,8%–5,0%**. 196/200 = 98% прийнятних; серед чотирьох неприйнятних — три неправильні інструкції та один privacy breach. Severity — погоджена шкала наслідків, не обов'язково числова відстань. У прикладі critical breach порушує обов'язкову вимогу та блокує release незалежно від aggregate score.

**Робоча пропозиція доповіді:** бізнес описує користь, шкоду й операційну місткість у зрозумілих сценаріях; Product Manager + BA перетворюють це на acceptance; QA + Developers — на measurement/evidence; risk/release owner ухвалює рішення в межах повноважень. Project Manager організовує доступ до stakeholders, budget, dependencies, evidence gaps, decision latency та operating capacity. Жодна роль не отримує всі рішення автоматично; новий headcount не вимагається.

**Стара презентація:** наданий maintainer PDF *Designing Non-Deterministic Systems: Maintaining Engineering Rigor in the AI Era*, slides 17–20 (Product responsibility, architect, QA, *Welcome to the Laboratory*). Використано рольові питання й empirical loop як педагогічний контекст. Не копіюємо старі надмірні метафори: Scrum вже емпіричний, requirements ширші за envelope, готовність до експерименту не дозволяє production, evidence не доводить універсальну correctness. Оригінальний PDF не редагується й не перевидається цією зміною.

**Поглиблене зіставлення з PDF:** після запиту maintainer деталізувати, не видаляючи попередній зміст, перевірено також slides 4–16 і closing. Наданий PDF байт-ідентичний збереженому `content/raw` (SHA-256 `891fbf94d30077b1e940c20c4b5ea1a6803b769a2a63c163e97fc00a6af23fa7`).

| Поточний слайд | Слайди старого PDF | Що повернуто у видимий зміст |
|---|---|---|
| 9 — Requirements | 5, 7, 17 | Корисна варіативність, незмінний обов’язковий зміст, tolerance contract для rework/cost/latency та escalation. Prompt не є повною acceptance specification. |
| 10 — Evaluation | 14, 19 | Golden Set, Eval Gate, калібрування evaluator із domain experts та incident-to-regression loop. Статистичний приклад і severity не змінено. |
| 11 — Delivery gates | 6, 9, 13 | Версії поведінки поза application code, quality/cost/latency budgets, coverage/uncertainty/baseline, block/canary/scoped release, синтаксична проти семантичної перевірки. |
| 12 — Architecture | 10, 11, 15, 16, 18 | Vendor changes, isolation, human-response capacity, fallible semantic checks і звуження/зупинка нежиттєздатного AI path. Feedback topology та попередні controls збережено. |
| 13 — Project process | 20 | Feasibility experiments поряд із delivery, конкретна trial hypothesis, evaluation time, time box дослідження до обіцянки production capability. |
| 14 — Synthesis | 22 | Практичний початок на одному workflow: tolerances, calibrated Golden Set, Eval Gate та rehearsed fallback, разом із попереднім HOW / WHAT. |

Розгорнуті українські нотатки пояснюють причинні зв’язки та приклад IT-асистента. Старі нотатки доповнено, усі попередні екранні тези збережено. Не переносимо буквально сильні старі твердження: variation не є автоматично bug; feedback сам не доводить stability/safety; semantic evaluator не є hard guarantee; provider replacement не зберігає поведінку; Golden Set не обов’язково репрезентує production traffic. Архітектурне veto — обґрунтований engineering висновок у межах визначених decision rights. Нових емпіричних чисел чи універсальних порогів не додано.

**UA owners для слайдів 11–14:** [Requirements, Correctness and Bugs](../../../00-doctrine/requirements-correctness-and-bugs.md), [Thinking System Review](../../../01-patterns/thinking-system-review.md), [Control-Loop Capability Anatomy](../../../00-doctrine/control-loop-anatomy.md), [Nested Control Lifecycle](../../../00-doctrine/nested-control-lifecycle.md). Схема слайда 12 показує scoped tool path із permission gate, reference, observation, decision та effective correction, не обов'язкову deployment topology.

## Історичний контекст і редакторський відбір

Ці джерела пояснюють еволюцію evidence base або залишаються у нотатках; вони не є додатковими headline-оцінками сучасних агентів.

| Джерело | Використання й обмеження |
|---|---|
| [METR — Early-2025 AI and experienced open-source developers, 10.07.2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | Датований RCT у нотатках слайда 4: 16 розробників, 246 задач, **на 19% більше часу** з early-2025 AI. Не переносити результат на всі сучасні інструменти. |
| [METR — We are Changing our Developer Productivity Experiment Design, 24.02.2026](https://metr.org/blog/2026-02-24-uplift-update/) | Пояснює selection bias в оновленому дослідженні; з нього не виводимо універсальний актуальний відсоток прискорення/сповільнення. |
| [Peng et al. — The Impact of AI on Developer Productivity: Evidence from GitHub Copilot, v1, 2023](https://arxiv.org/html/2302.06590v1) | Історичний позитивний експеримент: 95 рандомізованих учасників, 70 завершень, по 35 у групі; серед завершень 71,17 проти 160,89 хвилини, скорочення часу **55,8%**. Не 196 учасників; не оцінка повного SDLC. |
| [GitClear — AI Tool Impact on Developer Productive Output, 2022–2025](https://www.gitclear.com/research/ai_tool_impact_on_developer_productive_output_from_2022_to_2025) | Історичний code-output контекст: середні added LOC 1 314 → 3 037 (**+131,1%**), медіанні 921 → 1 624 (**+76,3%**). Це не delivery productivity; не змішуємо різні вибірки/композити. |
| [GitClear — AI Assistant Code Quality, 2025](https://www.gitclear.com/ai_assistant_code_quality_2025_research) | Для основного викладу замінено публічним звітом 2026. Старі **211 млн changed LOC** належать цьому звіту; не підставляємо цей обсяг під метрики 2026. |

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


## Уточнення змісту 22 вересня 2026 — слайди 9–14

Наступна редакція деталізує прямі уточнення автора та використовує ту саму незмінену Designing Non-Deterministic Systems. Нових емпіричних оцінок немає.

| Слайд | Підстава та зміна | Межа твердження |
|---|---|---|
| 9 | Старий слайд 5: простір прийнятних варіантів, обмежений умовами. Два допустимі формулювання всередині native області, CLARIFY за недостатніх підстав та PROHIBIT поза нею. | Концептуальна діаграма без універсальної числової semantic-distance осі. Operating Envelope є частиною Requirement. |
| 10 | Старі слайди 7 і 19: частоти та розподіли. Той самий навчальний приклад відображено native chart: 196 + 3 + 1 = 200, відповідно 98% + 1,5% + 0,5% = 100%. | Категорії взаємовиключні й вичерпні в цьому прикладі. Це не емпіричне дослідження, не нормальна апроксимація категорій та не новий baseline. Wilson interval стосується сукупної події 4/200. |
| 11 | Старий слайд 6 та [delivery review](../../../01-patterns/thinking-system-review.md), §§10–14: DoR / DoD / Release / Runtime. Видиме порівняння звичного фокусу й додаткової відповідальності. | DoR вимагає повного правдоподібного дизайну, DoD — реалізації й доказів. Ready до дослідження не дозволяє production. Класичні процеси також можуть мати статистику, risk management і monitoring. |
| 12 | Старі слайди 11, 15, 16, 18 та [project review](../../../01-patterns/project-control-architecture-and-viability-review.md), §§11–14: complete capability path, Human Authority, latency, capacity, control economics. | Невідоме навантаження можна вивчати лише в дозволеному bounded trial із працездатним керуванням. Canary обмежує exposure, але не скасовує заборон і не доводить safety. HITL не обов’язково означає ручне схвалення кожного запиту. |
| 13 | Авторський синтез попередніх слайдів: фундамент PM, змінений баланс SDLC, інженерія Thinking Systems та operating model з людьми. | Три горизонти співіснують, це не прогноз дат чи обов’язкова нова посада. PM координує й розуміє докази, але не привласнює всі технічні та бізнес-рішення. |
| 14 | Старі слайди 20 і 22: лабораторний цикл продовжується після релізу. Застосування до HOW і WHAT. | Scrum уже емпіричний. Постійне навчання не означає безконтрольних експериментів у production. |

Ці уточнення не змінюють нормативну модель UA. Числа, джерела та зафіксовані слайди 1–8 залишаються без змін. Попередні екранні пояснення, перенесені під час зміни композиції 11–14, розгорнуті у speaker notes поряд зі збереженим попереднім текстом.

## Графічне уточнення за скриншотами — слайди 8–10

Прямий запит maintainer від 22 вересня 2026 стосується конкретних графіків зі старих слайдів 3, 4 та 5. Переглянуто ці сторінки збереженого PDF як зображення, а також їхній текст. Попередня редакція надмірно скоротила саме візуальне пояснення.

| Поточний слайд | Старий слайд | Відновлений зміст і графіка | Межі інтерпретації |
|---|---|---|---|
| 8 | 3 — A World Where Variance Is Not Zero | Порівняння одиничного детермінованого результату з розподілом можливих відповідей, корисна область і рідші варіанти | Схема без емпіричних частот. Фіксовані input/state/version для лівого випадку. Праворуч не стверджується нормальність або heavy tails. |
| 9 | 5 — Designing the Space of Possibilities | Зліва маршрут A–B; справа перспективна площина, зовнішня межа допусків та внутрішня область цільової поведінки, різні відповіді й заборонений результат | Operating Envelope доповнює Requirement. Простір концептуальний, без універсальної семантичної метрики. Контур сам не реалізує контроль. |
| 10 | 4 — The New Definition of a Bug | Визначення порушення погодженої вимоги, зелена область допустимих варіантів і червоні наслідки за контрактом. Окремо збережено sample 196/3/1. | [Чинний власник визначень](../../../00-doctrine/requirements-correctness-and-bugs.md), §§4–5: рідкість, drift signal або зупинена належними контролями пропозиція самі собою не доводять Bug. Системна реалізація має спричинити або допустити порушення. |

Native bars на концептуальних схемах — редагована геометрія, не вигадані емпіричні дані. Лише окремий sample chart має числові дані та workbook: 196 + 3 + 1 = 200, частки 98%, 1,5%, 0,5%, сукупна частота 2%. Wilson interval не змінений. Схематична крива не апроксимує ці три категорії. Семантичні дефекти можуть виникати без зміни application code; один рідкісний результат не встановлює drift без baseline та порівнюваних даних.

Збережено Roboto, 14 назв і порядок, усі попередні speaker notes. Перекомпоновані екранні пояснення лишаються у джерелі й розгорнутих нотатках. Поточний запит явно дозволяє зміну слайда 8; його захисний baseline оновлено після огляду. Слайди 1–7 та 11–14 не змінені. Це локальна корекція змісту й композиції в наявних власниках, без нової доктрини, дослідницького статусу чи додаткових постійних agent instructions.


## Уточнення 22 вересня 2026: стандартний шрифт і старі слайди 5, 14–16

Нумерація запиту не рахує обкладинку. Безпосередньо оглянуті PDF pages 6, 15, 16 та 17 оригіналу: From Static Requirements to Statistical Gates; Designing Stochastic Resilience; System Boundary States; PM: From Story Owner to Distribution Economist. Оригінал не змінено.

- Слайд 9: бізнес-цінність, прийнятна частота **і** тяжкість помилок, cost envelope, liability / escalation / fallback. Розділено Product Manager та Project Manager; збережено область можливих поведінок.
- Слайд 11: Ready / Budget / Done / Release–Operate, старий і розширений контракти, людські залежності, статистичне evidence, production feedback. Розмір вибірки чи один confidence interval не є самостійним доказом безпеки.
- Слайд 12: fallible semantic monitor, deterministic tool gate, stop/isolate, safe fallback, human review, спостереження ефектів та дозволена корекція. Latency overhead, token/review economics і provider changes формують feasibility boundary; canary не замінює control path.

Канонічні власники змісту — Control-Loop Capability Anatomy, Nested Control Lifecycle та Thinking System Review; це навчальна адаптація, без нової доктрини чи research-state change. Усі попередні нотатки збережені як точні префікси. Зміст source blocks поза 9, 11 та 12 незмінний.

За прямим запитом стандартного шрифту вибрано Arial: [Apple system fonts](https://developer.apple.com/fonts/system-fonts/), [Microsoft Arial](https://learn.microsoft.com/en-us/typography/font-list/arial), [Google Slides text API](https://developers.google.com/workspace/slides/api/reference/rest/v1/presentations.pages/text). Arial менш округлий за Roboto, але має спільну платформну доступність. PPTX містить Arial references в тексті, charts і themes, без proprietary font binaries. Це свідома заміна попереднього embedded-Roboto контракту, а не видалення перевірок заради проходження CI; mutation tests захищають явні й успадковані font references. В Linux preview Arial підміняється Nimbus Sans; native acceptance у PowerPoint, Keynote і Google Slides не заявляється. Захист 1–8 діє надалі після явного font-only refresh з перевіркою точного змісту, notes і geometry.


## Захист 1–11 та пропозиція для 12–13, 22 вересня 2026

Прямий запит maintainer розширює freeze до 1–11. Жодний pptx-slide block, заголовок, попередні notes чи layout не змінено. Захист охоплює також native chart слайда 10, точний вміст embedded workbook та native table слайда 11. Workbook hash не залежить від ZIP entry timestamps/order/compression; байти кожного вкладеного файла залишаються захищеними.

Нижче — історична редакторська пропозиція від 22 вересня, тоді **ще не застосована**. Її наступна адаптація враховує прямі поправки 23 вересня, записані наприкінці цього документа. Прочитано поточну дугу всіх 14 слайдів і старий PDF, зокрема pages 15–20: resilience, veto, Product Manager, architect envelope, statistical QA, laboratory. Додаткові авторські джерела Beyond Embeddings і On-Device or Cloud розглянуті як контекст повної вартості контролю, human capacity та зовнішніх залежностей, без перенесення історичних product/version claims. Чинні UA doctrine/pattern залишаються власниками значень.

**Дуга:** 1–2 задають технологічний зсув і HOW / WHAT. 3–7 показують новий баланс SDLC та потребу зберігати людське розуміння/відновлення. 8–11 показують зміну інженерного об’єкта й requirements/evidence/delivery contract. 12 має завершити цю частину через повну архітектуру системи, включно з людьми. 13 повертає обидві лінії до Project Manager і керованого командного процесу. 14 підсумовує їх безперервним циклом навчання.

**12:** зберегти назву Production Needs a Control Loop. Центральний образ — весь інженерний периметр: model-mediated process, approved boundaries та їх realization, observation, decision authority, corrective action. Людина з context/authority/response time/peak capacity/backup має бути окремим пов’язаним елементом у цьому периметрі, а не тільки нижнім текстовим підписом. На одному IT-assistant сценарії показати: невизначеність → hold/escalation → людське рішення → дозволена дія чи fallback; недоступність людини не дозволяє автоматично розширити authority. Контроль збирає evidence і з delivery, і з fallback, а також перевіряє ефект корекції. Вартість токенів і перевірок, latency, provider changes та human capacity входять до рішення про viability. Внизу компактний висновок: без здійсненного контролю, допустимого response time або operational capacity — звуження/redesign/stop; unknown load — лише authorized bounded trial з робочими controls. Зберегти попередні технічні деталі й пояснення в notes. Не називати fallible evaluator детермінованою гарантією.

**13:** зберегти назву The Roles Move With the System. Повернути HOW WE BUILD / WHAT WE BUILD як два паралельні горизонти над незмінним фундаментом project management. Operating model є спільним наслідком обох змін, не незалежною третьою технологічною хвилею. Для HOW: PM разом із командою перебудовує flow, review/QA capacity, ownership і recovery readiness. Для WHAT: планує evidence work, з’єднує business limits з QA criteria, architecture, release decision і operational ownership/capacity. Замість довгого каталогу метрик показати зв’язок сигналу з управлінською дією: review queues/rework зростають → рішення про WIP, batch size і capacity; escalation queue/response time виходять за погоджені межі → уповноважене рішення про coverage/capacity, звуження rollout чи fallback. PM має статистичну грамотність і розуміє нові результати роботи ролей, але не підмінює Product, QA, architect або risk/operations owner.

**Перехід 12 → 13:** якщо люди, їхні права й готовність втрутитися входять до інженерного периметра, спосіб організації їхньої роботи стає умовою працездатності системи. **13 → 14:** цей спосіб роботи треба перевіряти на evidence та змінювати протягом життєвого циклу. Саме це пояснює, чому лабораторія залишається відкритою.


## Поправки 11–14, контакти й додаткові джерела, 23 вересня 2026

**11:** Відновлено порівняння Traditional / Thinking Systems навколо двох контрактів DoR та DoD. Бюджет був помилково піднятий до рівнозначного gate; тепер costs, latency й capacity є критеріями готовності та перевірки. Release/Operate виділено нижче. Incidents повертаються до regression, Eval Gates та monitoring rules. Ця поправка має пріоритет над попереднім four-row layout.

**12:** Причинна стрілка THREE PRESSURES → VETO була хибним стисненням. Вето випливає з нездійсненності потрібного надійного та операційно дієвого повного control path у погодженому scope. Latency, token/control cost та opaque vendor changes є окремими джерелами складності, а не формулою вето. Центральна схема адаптує повний периметр зі старого Architect slide, включно з substantive Human Authority, competence, context, response time, capacity та backup. Вона описує логічні функції, не фіксовану сервісну топологію. Чинні контрольні доктрини уточнюють історичні твердження про deterministic envelope: fallible semantic evaluator не є hard guarantee.

**13:** Конкретний сценарій maintainer — AI-компонент незнайомою команді мовою, який поступово стає критичним без qualified review та recovery ownership. Це вже наявний knowledge/competence issue, ризик росту й readiness dependency. PM забезпечує owner, trigger, план closure та свідчення розуміння/відновлення разом із технічними owners. Класичний PM-фундамент зберігається; HOW і WHAT потребують аналізу змінених ролей, evidence work та operating dependencies.

Додаткові первинні джерела перевірено 23 вересня 2026:

- [Shen & Tamkin, How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245), [авторський опис Anthropic, 29 January 2026](https://www.anthropic.com/research/AI-assistance-coding-skills): експеримент із незнайомою Python-бібліотекою виявив слабше негайне засвоєння в AI-групі. Обмеження: невелика вибірка, короткий горизонт, specific tutorial/tool setup; не доводить довгострокового занепаду навичок. Відмінності interaction patterns є qualitative associations, не окремий причинний експеримент. На слайд не перенесено відсотків або універсального прогнозу.
- [DORA, Working in small batches](https://dora.dev/capabilities/working-in-small-batches/), updated 8 December 2025: великі AI-generated зміни ускладнюють review/testing/integration; small batches підтримують швидкий feedback. Це підстава додати batch size, review capacity та delayed feedback до питань PM, а не новий закон, що кожний AI-проєкт сповільнюється.
- [Spracklen et al., USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen): package hallucinations як конкретний supply-chain failure mechanism у досліджених моделях і мовах. PM організовує ownership перевірки нових dependencies; не замінює security/engineering review. Числові результати не екстрапольовано на всі поточні моделі.

Сценарії неперевіреної спільної передумови у generated code/tests, неконтрольованого росту прототипу та knowledge gaps — інженерний синтез і приклад maintainer, не заявлений результат цих досліджень. Деталі й scope limits містяться в speaker notes.

**14:** Прямо адаптовано PDF pages 20 і 22: delivery зберігається, empirical loop працює до й після release. Planning ставить question/owner/evidence/stop rule; daily work показує версії, gaps та blockers; review оцінює results/uncertainty і приймає рішення; operations моніторить, реагує й навчається на incidents. HOW використовує цей режим для пошуку нового SDLC equilibrium, WHAT — протягом життєвого циклу. Scrum уже емпіричний; лабораторія не означає безмежного експериментування над користувачами.

**Контакти та захист:** Слайд 1 отримує коротке представлення, email та LinkedIn зі старого фінального PDF-слайда. Новий 15 дає обидва публічні репозиторії, native hyperlinks і точні QR-коди. Назви/порядок початкових 14 збережено. Прямий запит дозволяє зміну 1 і 11 та вузьке оновлення freeze; 2–10, їхній вміст і залежності залишаються точними. Причина помилок — надмірне стиснення різних decision surfaces у сусідні рядки/стрілки. Виправлено у чинних source/layout owners. Додаткових правил AGENTS або суб’єктивних keyword-gates не вводимо; чинний freeze перевіряє спостережувану незмінність, QR regression checks — точні assets і destinations.


## Критичний перегляд зв’язності й ролей, v14, 23 вересня 2026

Прямий запит maintainer: критично перевірити логіку, зв’язність і пропуски всієї презентації; переглянути другу частину й додати залучені ролі, зокрема Product Owner і Project Manager на 9. Перевірено поточні 15 слайдів, source blocks, notes і структуру переходів. Це локальна редакторська адаптація, не зміна UA doctrine, research state, Scrum або обов’язкового складу команд.

| Виявлена прогалина | Застосоване уточнення |
|---|---|
| 8–13 читаються як окремі території спеціалістів | 8 задає спільний ланцюг define/evaluate/control/operate; 9–14 показують учасників та їхній внесок, notes з’єднують виходи сусідніх слайдів |
| PO прихований у слові Product; Project Manager з’являється запізно | 9 явно називає Product Manager / Product Owner, BA та Project Manager; PO видимий на 10–14 через value, backlog і критерії; delivery coordination не підмінює domain authority |
| Release і робота після нього мають нечітке ownership | 11 розділяє authorized release owner та service owner; 12 називає implementation/testing/operability; 14 вказує responders та incident learning |
| Враження, що DoR/DoD належать лише Dev/QA або PO | 11 показує спільний контракт, DoR як можливу командну практику, DoD як shared quality commitment; notes пояснюють чинні Scrum accountabilities і окреме release authorization |
| Curated Golden Set поруч із Wilson interval може читатися як production frequency | 10 явно розрізняє перевірку сценаріїв та репрезентативне оцінювання частоти; counts 196/3/1, 4/200 та interval не змінені |
| Контроль ризику затуляє питання продуктової користі | 9 notes містять support outcome та full cost; 13–14 повертають business value / useful outcomes до evidence |
| Слайд 12 після DoD може створити waterfall-враження | Notes 11–12 пояснюють порядок розповіді: control design існує до релізу, а requirements/evaluation/architecture узгоджуються ітеративно |
| Фінал описує метод, але не дає короткої дії | 14 завершується одним workflow, value target, limits, evidence, owner і відрепетируваним fallback |

Першу частину 1–7 переглянуто без зміни зафіксованих джерел, notes або геометрії. Слайд 4 лишається найщільнішим: усно варто виділити кілька ключових контрастів і не зачитувати всі метрики. Вони описують різні populations, designs і outcomes, тому не утворюють одну універсальну causal estimate. На 3 і 5 треба озвучити вже наявні caveats: це сценарії, не виміряні часові ряди або прогноз. Теза 2 є концептуальним framing, не доказом свідомості моделей. 7 закриває HOW і явно переходить до WHAT. Нових емпіричних claims або чисел не додано.

Для role semantics звірено офіційний [Scrum Guide 2020](https://scrumguides.org/scrum-guide.html), розділи Scrum Team / Product Owner / Developers, Definition of Done та Sprint Review. PO accountable за maximizing value й effective Product Backlog management; Developers conform to DoD, відповідну DoD створює Scrum Team за відсутності organizational standard; Sprint Review не є release gate. Розподіл Product Manager / Project Manager / service owner у цій доповіді — організаційна інтерпретація, не Scrum prescription. Чинні UA owners залишаються `00-doctrine/nested-control-lifecycle.md`, `00-doctrine/control-loop-anatomy.md`, `01-patterns/project-control-architecture-and-viability-review.md` та `01-patterns/thinking-system-review.md`.

Збережено 15 назв і порядок, source sections 1–7/15, усі попередні notes як точний prefix, numerical evidence і native chart/workbook. Перевірка staged package проти v13 дозволила лише slide/notes XML 8–11 всередині freeze; shared parts лишилися точними. Freeze 1–11 не послаблено; baseline оновлено вузько після візуального огляду 8–11. Редакторська проблема локальна: виправлено existing source/layout/evidence owners. Нової persistent guidance, AGENTS rule, рольового keyword gate або workflow не запропоновано; суб’єктивна зв’язність не кодується в CI.

Підсумкова перевірка v14: усі 15 слайдів відкрито як незалежний LibreOffice render; source/package checks і pixel comparison підтвердили незмінність 1–7/15. Фінальний пакет відрізняється від першого переглянутого candidate лише уточненням Human Authority на 12, повторно оглянутим у повному розмірі. `npm run check`: 81 Quartz + 135 publication tests, TypeScript і production build пройшли; portable PPTX verification: 15 slides, 3 pictures, 2 native tables, 404 text runs. SHA-256 PPTX: `0713a9826b25b685a0936b53dc6874484ab8b6f2855b097e88827f21f0ef9993`. Linux використовує Nimbus Sans замість Arial; native PowerPoint / Keynote / Google Slides acceptance не заявляється.


## Застосування змістовного review, v15, 23 вересня 2026

Прямий запит maintainer «Виправ» після review дозволяє застосувати його висновки до 4 і 8–14. Це редакторське уточнення поточної презентації, без нових empirical claims, доктринальних або research-state змін. Назви й порядок збережено. IT-assistant case є ілюстрацією, а не заявою про deployed product.

| Висновок review | Застосована зміна |
|---|---|
| 12 показував лише feedback після business action | Native diagram відокремлює internal model proposal, перевірку permissions / required approval, дозволене delivery/execution і подальше observation. Відмова або недоступність gate веде у deny / safe fallback. Human authority з evidence, rights і capacity входить у required approval. Feedback controller / actuator змінює подальшу дію; незворотний disclosure не можна виправити rollback. Notes відмежовують перевірювані права від fallible semantic evaluation |
| Загальна рамка не мала видимого завершеного застосування | Один access-recovery assistant проходить через 8 (outcome), 9 (contract), 10 (evidence), 11 (blocked candidate / required conditions), 12 (control). Privacy breach не губиться між sample і release: цей candidate блокується |
| 4 та друга частина перевантажені | На 4 — три основні evidence contrasts. Допоміжні METR / Agarwal / Xu, DORA perceptions та GitClear arithmetic збережено в notes; числових оцінок не змінено. На 9 прибрано додатковий standards рядок з екрана, залишено його в notes. 11 використовує конкретний assistant у порівнянні DoR/DoD, 12 показує сам control path, 14 завершується одним workflow |
| Average rate може маскувати severity | 10 зберігає counts 196/3/1, 4/200 і Wilson interval, але прямо пояснює, що low average rate не виправдовує prohibited disclosure. Notes розділяють any-violation rate, ordinary rework і critical event. Golden Set та representative sampling залишаються різними джерелами evidence |
| Перелік ролей не показує змінену роботу | 13 WHAT називає agreed criteria, domain reviewer, named responder із verified capacity і наслідок unmet criteria для release. 9 зберігає Product Manager / PO / BA / PM із конкретним внеском |
| Обсяг controls міг сприйматися універсальним | 12 порівнює draft for human review та autonomous access change за consequence, authority і reversibility. Access boundary потрібний і draft. Архітектурне veto лишається явним; cost, latency, provider changes, human peak capacity/backup та bounded trial з робочими controls збережено в notes |

Джерельна база не розширюється: primary empirical evidence лишається описаною вище; control semantics спирається на чинні UA control-loop / nested-lifecycle / project / delivery owners і на вже надані Beyond Embeddings та On-Device/Cloud checklist. Приклади не є універсальною prescribed topology. Existing people можуть поєднувати ролі; нових посад, комітетів чи gates як організаційної вимоги не додано.

Збереження перевірено до оновлення freeze: source 1–3/5–7/15 і всі 15 titles/order точні; кожен попередній notes залишається точним prefix. У frozen dependency closure змінилися лише дозволені slide/notes XML 4/8–11; chart/workbook і shared dependencies точні. Виправлено зафіксовані під час рендеру перенесення Verify user і перетин denial label зі стрілкою. Freeze 1–11 не послаблено, автоматичного refresh/bypass немає. Mutation fixtures тепер перевіряють допоміжні DORA/Agarwal числа у notes, primary NBER/DORA — на екрані; word-fit fixture використовує поточні Request / Verify user. Редакторська корекція локальна: persistent agent guidance чи нова subjective CI policy не потрібні й не застосовувалися.
