---
title: AI Changes Both Sides of Software Engineering
artifact_type: repository-guide
status: informative
maturity: draft
module: publishing
draft: true
topics:
  - thinking-systems
  - sdlc
  - evidence
tags:
  - ua/module/publishing
  - ua/type/repository-guide
  - ua/status/informative
  - ua/topic/thinking-systems
  - ua/topic/sdlc
---

# AI Changes Both Sides of Software Engineering
## Детальний сценарій погоджених 14 слайдів

Дата перевірки джерел: 21 вересня 2026 року. Центральний опис і редаговані дані для PPTX; артефакт залишається review candidate.

**Структуру відновлено буквально:** ті самі 14 назв, той самий порядок і та сама драматургія. Слайд 4 залишається спільним evidence slide. Слайди 5–7 — comprehension, відповідальність команди та пошук нового SDLC equilibrium, а не окремі слайди про звіти.

Головна дуга: технологічний зсув → HOW we build → дисбаланс SDLC → WHAT we build → Thinking Systems → requirements, QA, release, production і ролі → engineering rigor переходить у нові місця, а не зникає.

Таймінг: 38 хвилин + 2 хвилини резерву. Повноцінне Q&A — окремо. Англійська — для заголовків і коротких екранних формулювань; українська — для пояснень і виступу.

### Що і як перевірено

Відправна точка — [реєстр evidence/SOURCES.md у Subprime](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/blob/main/evidence/SOURCES.md), його бібліографія, звіт та NBER evidence brief. Реєстр не означає, що кожен запис уже пройшов повний аудит: стан Registered відрізняється від Verified. Для чисел нижче пріоритет мають самі автори досліджень.

Для актуальності додано новіші авторські публікації, навіть якщо їх ще немає в реєстрі Subprime: DORA 2025, METR за травень 2026, GitClear за червень 2026. Xu використано у v3 від 28 січня 2026, Agarwal — у v2 від 27 січня 2026. Нова дата версії не робить старі дані новими: це окремо зазначено.

Перевірка означає звірку таблиць, підписів, одиниць вимірювання, дат, дизайну досліджень і арифметики. Вона не означає незалежне відтворення оцінок на сирих даних. Для NBER прочитано наданий оригінальний PDF і візуально звірено ключові таблицю та графіки. Для DORA використано публічне авторське резюме, для GitClear — публічний виклад і доступний графік; перевірка повного закритого звіту не заявляється.

### Стиль і технічний контракт PPTX

Погоджено maintainer 21 вересня 2026. Ці вимоги стосуються саме цієї презентації, не всіх UA artifacts.

- Суцільний темний фон #0B0F14 на КОЖНОМУ слайді, заданий властивістю background. Жодних фонових картинок, градієнтів або full-slide screenshot.
- Світлий текст #F4F7FA; допоміжний #ADB8C5. Cyan #28C7F7 для можливостей/потоку; amber #F5B61C для меж/контролю; red #FF6B75 лише для failure/block.
- 16:9, 1280×720 design canvas; одна узгоджена сітка з полями 64 px.
- DejaVu Sans, наявний у зафіксованому authoring runtime. На машині доповідача шрифт має бути встановлений або узгоджено замінений із повторною visual QA. Текст не перетворювати на криві для обходу відсутнього шрифту.
- Заголовки 40 px (30 pt), довгі — у два зафіксовані рядки; головний текст 28–32 px; великі числа 44–66 px; щільні evidence labels 20–24 px. Для заголовків і схем залишати запас ширини, а не впритул до країв. Не приховувати substantive caveats у мікрошрифті.
- Усі заголовки, абзаци, формули, блоки, стрілки, таблиці та схематичні криві — НАТИВНІ РЕДАГОВАНІ об'єкти PowerPoint.
- Для даних використовувати native charts або точні числові підписи; для схем — shapes/connectors. Не rasterize SVG/Mermaid/HTML як зручний обхід.
- Окреме зображення дозволене лише коли змістовний об'єкт неможливо адекватно зробити native tools. Воно не є фоном, не містить запеченого заголовка/тексту слайда і має записаний exception rationale. У поточній версії винятків немає: 0 зображень.
- Рівно 14 слайдів із погодженими назвами й порядком. Статична версія самодостатня; анімації не є умовою розуміння.
- English screen copy; українські speaker notes. Notes містять пояснення, джерела та обмеження, а не інструкції верстальнику.
- Центральний MD — editable source; pptx-slide blocks нижче задають екранні формулювання/дані. Прозу та відповідний block оновлювати разом. PPTX — derived artifact, не друге джерело змісту.
- Слайди 11 і 13 мають справжні PowerPoint tables. Схема слайда 5 не видається за емпіричний графік.
- Після кожної збірки: structural/editability checks, freshness hashes, render усіх 14 слайдів і огляд кожного. Для цієї редакції додатково перевіряти експортований PPTX через незалежний LibreOffice → PDF/PNG: внутрішній preview генератора сам по собі не підтверджує переносимість. Валідатор не доводить visual quality.
- Згенерований PPTX збережено поруч як review snapshot за прямим запитом maintainer; це не запис про вже проведений виступ і не нова нормативна редакція UA.

Build/verification contract: [PPTX export](../../../quartz/PPTX-EXPORT.md).
Generated review snapshot: [ai-changes-both-sides.pptx](ai-changes-both-sides.pptx).

### Спільні правила оформлення

- 16:9; темний фон, світлий текст; cyan — можливості/основний потік, amber — межі/контроль. Не робити всю презентацію однаковими картками.
- Розміри шрифтів визначає технічний контракт вище. Методологія в нотатках; критичне обмеження — також видимим коротким підписом.
- Докладний опис не дорівнює великій кількості тексту на екрані. Кожен слайд має один головний візуальний об'єкт.
- Реальні результати досліджень, авторські висновки доповіді та навчальні приклади чітко відділені.
- Не підміняти LOC delivered value, reviews — годинами роботи, releases — успіхом продукту, downloads/ratings — споживчим добробутом.
- Зберігати також позитивні, нульові й суперечливі результати. Це не anti-AI доповідь.

# ACT 0 — Що саме сталося?

## 1. AI Changes Both Sides of Software Engineering

```pptx-slide
{
  "number": 1,
  "layout": "cover",
  "subtitle": "How we build software. And what software is.",
  "lanes": [
    [
      "HOW WE BUILD",
      "AI-assisted engineering"
    ],
    [
      "WHAT WE BUILD",
      "Thinking Systems"
    ]
  ],
  "takeaway": "They are related. They are not the same.",
  "notes": "Відділити AI для розробки від Model Judgment усередині продукту. Перше змінює виробництво software, друге — поведінку системи. Не починати з реклами UA чи anti-AI тези."
}
```

**Час:** 1:00.

**Роль:** одразу відділити дві різні трансформації. Не починати з UA, Subprime Code чи переліку загроз.

**На екрані:**

Підзаголовок: **How we build software. And what software is.**

Дві рівнозначні стрілки:
- HOW WE BUILD → AI-assisted engineering
- WHAT WE BUILD → Thinking Systems

Нижче: **We tend to mix these two transformations. They are related. They are not the same.**

**Композиція:** великий заголовок зверху; у центрі дві горизонтальні смуги, одна під одною, з однаковою візуальною вагою. Не з'єднувати їх причинною стрілкою. Ім'я й PMDay — невеликий підпис унизу. Жодних графіків adoption.

**Що говорити:** «Можна будувати звичайний детермінований сервіс за допомогою AI. А можна будувати сервіс, який сам делегує моделі частину рішень під час роботи. Перше змінює процес виробництва. Друге — поведінку продукту. Сьогодні нам потрібні обидві розмови, але не в одній купі».

**Що не стверджуємо:** AI-assisted development не обов'язково створює Thinking System; Thinking System не обов'язково написана AI.

**Перехід:** «Що саме стало доступним, щоб одночасно запустити обидві зміни?»

## 2. This Is a Real Phase Transition

```pptx-slide
{
  "number": 2,
  "layout": "phase",
  "items": [
    [
      "Writing",
      "Externalized Memory"
    ],
    [
      "Computers",
      "Externalized Calculation"
    ],
    [
      "Large Models",
      "Externalized Cognition"
    ]
  ],
  "caveat": "No assumption of will, consciousness or human-like understanding is required.",
  "takeaway": "We design the environment in which behavior is generated at runtime.",
  "notes": "Phase transition — функціональна рамка, не фізичний закон. Cognition-like operations: інтерпретація запиту, зіставлення контексту, пропозиція коду чи плану. Engineering consequence: ми задаємо контекст, інструменти, межі та перевірку поведінки."
}
```

**Час:** 3:00.

**Роль:** пояснити масштаб зсуву, не сперечаючись про свідомість.

**На екрані:**

| Технологія | Що стало зовнішнім інструментом |
|---|---|
| Writing | Externalized Memory |
| Computers | Externalized Calculation |
| Large Models | Externalized Cognition |

Під рядом: **No assumption of will, consciousness, or human-like understanding is required.**

Фінальна фраза: **Developers now design the environment in which behavior is generated at runtime.**

**Композиція:** три великі послідовні блоки: текст/пам'ять, обчислення, робота з мовою та контекстом. Останній блок виділити кольором, а не намалювати «штучний мозок». Нижній ряд про engineering consequence з'являється після пояснення трьох блоків.

**Що говорити:** «Мені не потрібно доводити, що LLM думають як люди. Достатньо того, що вони виконують корисні cognition-like operations: інтерпретують запит, зіставляють контекст, пропонують код або план дій. Це дозволяє делегувати машині кроки, для яких раніше потрібна була людина або велика кількість спеціально написаних правил».

Далі: «Раніше ми переважно явно задавали виконання. Тепер у частині систем ми задаємо контекст, інструменти, обмеження та спосіб перевірки поведінки, яка виникне під час конкретного виклику».

**Важливе уточнення:** phase transition — рамка доповіді, не результат фізичного вимірювання чи доведений універсальний закон. Externalized Cognition — функціональна аналогія, не твердження про свідомість. Не потрібні застарілі benchmark-цифри для легітимації цього слайда.

**Матеріал старої презентації:** зберегти її Writing / Computers / Large Models ідею та візуальну простоту.

**Перехід:** «Спочатку подивімося, як ця можливість змінює саму розробку».

# ACT I — AI змінює HOW we build

## 3. We Accelerated a Step. Not the System.

```pptx-slide
{
  "number": 3,
  "layout": "sdlc",
  "steps": [
    "Intent",
    "Design",
    "Code",
    "Review",
    "Test",
    "Integrate",
    "Deploy",
    "Operate"
  ],
  "takeaway": "Local acceleration ≠ system throughput",
  "caption": "If coding is the bottleneck, the bottleneck can move.",
  "notes": "Навчальний приклад, не виміряні дані: writing capacity 20 змін/тиждень, review 10, integration 8. Зростання writing до 100 не змінює незмінну потужність integration. AI може прискорювати інші етапи; ефект треба перевіряти, а не припускати."
}
```

**Час:** 2:30.

**Роль:** відділити локальну швидкість від пропускної здатності delivery system.

**На екрані:** один наскрізний SDLC:

Intent → Design → Code → Review → Test → Integrate → Deploy → Operate

CODE підсвічений і позначений ↑↑↑; над Review / Test / Integrate / Operate — знаки питання.

Основна теза: **Local acceleration ≠ system throughput.**

**Композиція:** процес займає центральні 70% висоти, не вісім карток із довгим текстом. Анімація спочатку прискорює Code, потім показує можливу чергу перед Review. Позначка: **Illustrative bottleneck — not a measured team result.**

**Конкретний навчальний приклад для нотаток:** умовна команда може написати 20 змін за тиждень, перевірити 10, інтегрувати 8. Якщо генерація стає 100 змін/тиждень, це саме по собі не збільшує межу інтеграції 8. Приклад припускає зіставні зміни та незмінну потужність інших етапів; це не дані дослідження.

**Що говорити:** «Якщо coding не був bottleneck, прискорення coding не дає такого самого прискорення delivery. Якщо був — обмеження переміститься. AI може допомогти також у review, testing, design чи operations. Але їхнє прискорення треба перевіряти, а не вважати автоматичним наслідком швидшої генерації».

**Що вимірювати в реальній команді:** час від intent до production, час очікування review, незавершену роботу, rework, частку невдалих змін і користувацький результат. Цей список — в усному поясненні, не ще один великий блок слайда.

**Перехід:** «Саме тому дослідження дають не одну універсальну цифру AI productivity».

## 4. The Evidence Is Already Messy

```pptx-slide
{
  "number": 4,
  "layout": "evidence",
  "nberMetrics": [
    [
      "17.3×",
      "changed LOC"
    ],
    [
      "2.8×",
      "commits"
    ],
    [
      "1.3×",
      "releases"
    ]
  ],
  "nberGeneration": "Autocomplete + sync + async agents",
  "nberCaveat": "Changed LOC = additions + deletions.\nSeparate async release effect not estimated.",
  "marketHeadline": "More apps. No aggregate usage gain\nin these cohorts.",
  "marketDetail": "New cohorts, first 3 months. Usage proxies, not welfare.",
  "marketNumbers": [
    [
      "iOS: <10 ratings",
      "79% → 86%"
    ],
    [
      "Chrome: <10 downloads",
      "18% → 31%"
    ]
  ],
  "cards": [
    [
      "METR · MAY 2026",
      "1.4–2× work value",
      "Self-reported survey; not causal uplift"
    ],
    [
      "DORA · 2025",
      "Throughput ↑   Stability ↓",
      "Product performance ↑; associations"
    ],
    [
      "GITCLEAR · JUN 2026",
      "13% → 3.8%",
      "Refactoring share; 2023 → YTD 2026"
    ],
    [
      "XU + AGARWAL · 2026",
      "Complexity +35% / +43%",
      "Agarwal: complexity proxy.\nXu: contributor workload."
    ]
  ],
  "takeaway": "Code activity, delivery and user value are different outcomes.",
  "notes": "NBER: понад 100 тисяч GitHub developers; matched event study, не RCT. Changed LOC = additions + deletions, не чисте зростання кодової бази.\nTable 5, друкована с. 33, тижні 21–30: Autocomplete — LOC +228.2%, commits +35.9%, PRs +11.0%, releases +10.2%. Synchronous agents — LOC +741.3%, commits +109.1%, PRs +65.5%, releases +20.3%. Asynchronous agents — LOC +658.3%, commits +33.6%, PRs +71.8%; releases не оцінено окремо. Figure 1, с. 3: cumulative LOC 17.3×, files 3.9×, commits 2.8×, PRs 2.5×, repos 1.5×, releases 1.3×. Не перемножувати компоненти.\nFigure 12, с. 41; §8.2, с. 42–43: iOS — 30–50 тисяч нових apps/month → близько 100 тисяч у квітні 2026; Android — 42 тисячі у січні 2025 → близько 60 тисяч у середині 2026; Chrome — 5 тисяч у 2023 → близько 13 тисяч у середині 2026. Total cohort usage за перші 3 місяці стабільне або знижується. Частка iOS apps із <10 ratings: 79→86%; Chrome extensions із <10 downloads: 18→31%. SourceForge без прискорення entry, не входить у три usage panels. Це не всі existing apps, не весь software market і не пряме вимірювання consumer welfare. Chrome decline передував agentic era.\nDORA 2025: позитивні associations AI adoption із throughput і product performance, негативні — зі stability; не підставляти коефіцієнти 2024 року.\nMETR, травень 2026: 349 technical workers; 1.4–2× median self-reported work value залежно від питання, 3× self-reported speed; є selection bias. Старий RCT 2025 із +19% часу — лише історичний контекст.\nGitClear 2026: refactoring share 13→3.8%, duplication приблизно +81%; observational proxies.\nXu, v3 від січня 2026, дані 2020–22: top activity quartile — commits −19%, reviews +6.5%; bottom quartile — commits +43.5%, PRs +17.7%; rework +2.4%. Це не кадрові грейди й не агенти 2026 року.\nAgarwal, v2, Table 2: complexity +34.85/+42.87%, warnings +17.73/+19.00%; зміна IDE-first warnings статистично незначуща. Не трактувати це як борг на одну фічу.",
  "sources": [
    "https://www.nber.org/papers/w35275",
    "https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report",
    "https://metr.org/blog/2026-05-11-ai-usage-survey/",
    "https://www.gitclear.com/the_ai_code_quality_maintainability_gap",
    "https://arxiv.org/html/2510.10165v3",
    "https://arxiv.org/html/2601.13597v2"
  ]
}
```

**Час:** 4:30.

**Роль:** показати різні рівні вимірювання — активність розробника, delivery, підтримуваність, командну роботу та використання продукту. Це один слайд, не новий act із шести слайдів.

### Що саме має бути на екрані

П'ять карток. Ліві 52% — одна велика NBER; праві 48% — чотири менші: METR, DORA, GitClear, Xu + Agarwal. Відкривати послідовно в межах того самого слайда; не розміщувати всі таблиці нижче на екрані.

**Велика картка NBER — May 2026:**
- **17.3× changed LOC**
- **2.8× commits**
- **1.3× releases**
- Видимий ряд: **Autocomplete + synchronous + asynchronous agents**
- Нижній блок: **More apps. No aggregate usage increase in the observed cohorts.**
- Один конкретний сигнал: **iOS apps with <10 ratings: 79% → 86%**.
- Критична примітка: **Cumulative estimates; separate async release effect not identified.**

**METR — May 2026:** **1.4–2× self-reported work value**; підпис **Survey, not measured causal uplift**.

**DORA — 2025:** **Throughput ↑ · Product performance ↑ · Stability ↓**; підпис **Associations, not an experiment**.

**GitClear — June 2026:** **Refactoring-related share: 13% → 3.8%**; підпис **2023 → YTD 2026 · observational proxy**.

**Xu + Agarwal — 2026 versions:** **Workload shifts. Complexity rises in studied samples.** Один числовий ряд: **Complexity +35% / +43%**; назвати Agent-first / IDE-first. Цифри Xu — в нотатках, щоб не перетворити картку на таблицю.

Унизу слайда: **These studies do not prove “AI makes engineering worse.” More code faster is not the same measurement as more value delivered.**

### NBER: повні перевірені цифри для нотаток

Джерело: Demirer, Musolff & Yang, [Writing Code vs. Shipping Code, NBER WP 35275](https://www.nber.org/papers/w35275). Травень 2026; working paper. Понад 100 тисяч GitHub developers, телеметрія використання AI та matched event-study design; це не рандомізований експеримент.

**Table 5, друкована сторінка 33.** Тижні 21–30 після adoption; нормалізація на середнє до adoption, 1% winsorization. У цій таблиці — компоненти ефекту, а не три кумулятивні підсумки.

| Компонент | Changed LOC | Distinct files | Commits | Created PRs | Distinct repos | Releases |
|---|---:|---:|---:|---:|---:|---:|
| Autocomplete | +228,2% | +50,8% | +35,9% | +11,0% | +13,6% | +10,2% |
| Synchronous agents | +741,3% | +187,0% | +109,1% | +65,5% | +25,5% | +20,3% |
| Asynchronous agents | +658,3% | +52,4% | +33,6% | +71,8% | +13,8% | Не оцінено окремо |

**Що означають покоління:** autocomplete доповнює код; synchronous agent працює з розробником інтерактивно; asynchronous agent отримує делеговану задачу і працює до її завершення автономніше, без постійного синхронного ведення.

**Figure 1, сторінка 3, кумулятивно до останнього покоління:** changed LOC 17,3×; файли 3,9×; commits 2,8×; PRs 2,5×; repositories 1,5×; releases 1,3×. Це авторський спосіб підсумувати компоненти, а не вимірювання «17,3-кратної корисності розробника».

Зокрема, 228,2 + 741,3 + 658,3 = 1627,8% приросту; рівень відносно бази — 17,278× ≈ 17,3×. Для commits: 35,9 + 109,1 + 33,6 = 178,6%, тобто ≈2,8×. Для releases ідентифіковані компоненти дають 30,5%, тобто ≈1,3×; окремого async-компонента немає. НЕ трактувати прочерк як доведений нульовий ефект.

**LOC означає additions + deletions**, а не тільки нові рядки і не чисте зростання кодової бази. Сильно більша активність у коді не є прямо виміряним зростанням бізнес-цінності.

### NBER: маркетплейси та кінцевий користувач — повернутий блок

**Figure 12, друкована сторінка 41; розділи 8.2.2–8.2.3, сторінки 42–43.**

| Майданчик | Нові публікації за місяць: приблизні рівні з тексту авторів | Використання нових когорт у перші 3 місяці |
|---|---|---|
| Apple App Store | 30–50 тис. у 2023 — на початку 2025 → близько 100 тис. у квітні 2026 | Сукупна кількість ratings приблизно стабільна при порівнянні когорт 2024 і 2025 |
| Google Play | Близько 42 тис. у січні 2025 → близько 60 тис. до середини 2026 | Сукупні downloads приблизно стабільні |
| Chrome Web Store | Близько 5 тис. у 2023 → близько 13 тис. до середини 2026 | Download proxy знижується; спад почався ще до agentic era |
| SourceForge | Прискорення кількості нових публікацій не виявлено | Не входить до трьох панелей usage у Figure 12 |

Частка застосунків/розширень, які за перші три місяці не досягли навіть невеликої аудиторії, протягом 2025 зросла:
- iOS, менш як 10 ratings: приблизно **79% → 86%**, тобто +7 відсоткових пунктів.
- Chrome, менш як 10 downloads: приблизно **18% → 31%**, тобто +13 відсоткових пунктів.
- Android: автори описують менше зростання цієї частки; точного додаткового відсотка тут не приписуємо.

**Як це сказати усно:** «Дослідження доходить не тільки до commits і releases. Воно питає: чи хтось використовує додатковий software? Нових застосунків стає більше. Але у досліджених когортах сукупне використання за перші три місяці не зростає; частка релізів, які майже не знайшли аудиторії, збільшується».

**Межа висновку:** це показники нових когорт, а не всіх застосунків у магазині чи всього світового software. Ratings і download proxies — не пряме вимірювання user welfare, виручки або часу використання. Часовий збіг не ідентифікує AI як єдину причину. Коротке вікно не виключає пізніх вигод. Коректно: «помітного агрегованого приросту використання тут не видно», а не «AI нічого не дав користувачам».

### Інші картки: числа й межі

**DORA 2025.** Майже 5 000 респондентів; 90% використовують AI, понад 80% повідомляють про вищу продуктивність, 30% мало або зовсім не довіряють AI-коду. Зв'язок adoption із throughput і product performance позитивний, зі stability — негативний. Це не причинні коефіцієнти. Числа DORA 2024 сюди не переносимо. [Офіційне авторське резюме DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report).

**METR, 11 травня 2026.** 349 technical workers; median self-reported work-value multiplier 1,4–2× залежно від формулювання питання, self-reported speed — 3×. Це не confidence interval і не об'єктивне вимірювання delivery. Вибірка самообрана. [METR survey](https://metr.org/blog/2026-05-11-ai-usage-survey/).

Історичний контрольований результат METR 2025: 16 розробників, 246 задач, +19% часу з early-2025 AI. Залишити як датований контекст, не актуальний вирок сучасним агентам. [METR RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). У [лютневому оновленні 2026](https://metr.org/blog/2026-02-24-uplift-update/) самі автори вказують на selection bias; не виводити з нього надійний універсальний поточний відсоток.

**GitClear, червень 2026.** Moved/refactoring-related share: 13% у 2023 → 3,8% YTD 2026; block duplication приблизно +81%. Це спостережні показники власної класифікації, не весь reuse і не встановлений причинний ефект AI. У тексті й графіку duplication є суперечність одиниць; тому абсолютні 40,3 і 73,0 не використовуємо як навантажену метрику. Відносна зміна узгоджується. [GitClear 2026](https://www.gitclear.com/the_ai_code_quality_maintainability_gap).

**Xu, v3, січень 2026.** У нижнього квартиля за попередньою активністю commits +43,5%, PRs +17,7%; у верхнього commits −19%, reviews +6,5%. Project-level PR rework +2,4%. Це activity quartiles, не Junior/Senior; reviews — кількість, не години. Дані 2020–2022 про ранній Copilot: використовуємо для механізму перерозподілу роботи, не оцінки агентів 2026. [Xu et al.](https://arxiv.org/html/2510.10165v3).

**Agarwal, v2, січень 2026, Table 2.** Agent-first / IDE-first: cognitive complexity +34,85% / +42,87%; commits +36,25% / +3,06% (друге незначуще); static warnings +17,73% / +19,00% (друге незначуще). Repo-level DiD, не «борг на кожну фічу». Agent-first — без виявлених попередніх IDE-слідів, не гарантовано без AI. [Agarwal et al.](https://arxiv.org/html/2601.13597v2).

### Що говорити і в якому порядку

1. Приблизно 2 хвилини: NBER — три покоління, різні рівні результату, маркетплейси.
2. Приблизно 1 хвилина: DORA і METR — позитивні сигнали реальні, але методи й outcomes різні.
3. Приблизно 1 хвилина: GitClear, Xu, Agarwal — maintenance/review/complexity не зникають із прискоренням генерації.
4. 30 секунд: «Ці результати не складаються в одну середню цифру. Вони показують, що generation, delivery та user value — різні речі».

**Перехід:** «Якщо генерувати стає дешевше, який ресурс системи стає дефіцитнішим?»

## 5. The New Scarcity Is Human Comprehension

```pptx-slide
{
  "number": 5,
  "layout": "comprehension",
  "curves": [
    "Machine generation capacity",
    "Human comprehension capacity"
  ],
  "questions": [
    "Can we generate it?",
    "Can we review it?",
    "Can we own it for 5 years?"
  ],
  "takeaway": "Generation scales differently from comprehension.",
  "caption": "Conceptual illustration; not measured trend data.",
  "notes": "AI може допомагати й comprehension. Криві не виміряні, людська спроможність не є незмінною. Comprehension debt — рамка ризику: прийняті зміни випереджають розуміння системи. Complexity, volume, duplication, ownership, architecture comprehension — signals, не прямий вимір боргу."
}
```

**Час:** 2:30.

**Роль:** повернути власну сильну тезу доповіді — асиметрію між генерацією та здатністю команди розуміти й підтримувати прийняте.

**На екрані:** дві схематичні криві:
- Machine code generation capacity — швидко вгору.
- Human comprehension capacity — повільніше.

Між ними — заштрихована область: **Potential comprehension gap**.

Три питання:
- Can we generate it?
- Can we review it?
- Can we own it for 5 years?

Головна теза: **Generation scales differently from comprehension.**

**Композиція:** графік займає ліві дві третини; три питання — праворуч. Вісь X — adoption/time, Y — умовна capacity. Без числової шкали; видима позначка **Conceptual illustration — not measured trend data**. Не малювати горизонтальну «вічну межу» людського розуміння.

**Що говорити:** «AI може допомагати і з comprehension: пояснювати код, знаходити залежності, будувати документацію. Але з того, що він генерує більше, не випливає, що команда настільки ж швидко набуває здатності пояснити, перевірити й змінити все прийняте».

Далі: «Comprehension debt — наша рамка ризику: система накопичує зміни швидше, ніж формується надійне розуміння її поведінки та меж. Це не готова наукова метрика».

**Конкретні сигнали для нотаток:** зміни без зрозумілого owner; review без пояснення впливу; невідомі залежності; зростання незрозумілого коду; розбіжність документації та реалізації. Complexity, volume, duplication і reuse — допоміжні indicators, не прямі вимірювачі людського розуміння.

**Зв'язок із попереднім:** дані NBER і quality studies мотивують питання про comprehension, але самі не вимірюють цей gap.

**Перехід:** «Найжорсткіша перевірка такого боргу відбувається не під час демо, а під час інциденту».

## 6. The Team Is the Last Line of Defense

```pptx-slide
{
  "number": 6,
  "layout": "recovery",
  "incident": [
    "Production is down.",
    "Three agent fixes fail.",
    "Now what?"
  ],
  "takeaway": "If AI cannot recover the system, the team still must.",
  "watch": "Complexity / volume / duplication / reuse / ownership / comprehension",
  "explore": "SDD / living architecture docs / code + docs / repository intelligence",
  "notes": "Умовний сценарій, не case study. Перевірити, хто розуміє інваріанти й залежності, хто може обмежити наслідки, зупинити зміни, відкотити й відновити систему. SDD = spec-driven development. Документація та repository intelligence — гіпотези/інструменти, не доведена універсальна відповідь."
}
```

**Час:** 2:30.

**Роль:** зробити відповідальність команди операційною, а не моральною декларацією.

**На екрані:**

Production is down.\
The agent tries three fixes.\
None works.\
**Now what?**

Коротка схема: AI Agent → failed recovery → TEAM.

Під нею: **Does anyone still understand the system well enough to take over?**

Головна теза: **If AI cannot recover the system, the team still must.**

**Композиція:** на перших 40 секундах лише incident-сценарій і точка передачі людині. Потім у нижній третині відкриваються два короткі рядки:
- Watch: complexity · volume · duplication · reuse · ownership · architecture comprehension
- Explore: SDD · living architecture docs · code + docs · repository intelligence

Позначити сценарій як hypothetical, не видавати його за досліджений кейс.

**Що говорити:** «Використовувати AI під час recovery цілком нормально. Питання в тому, що робить команда, коли він не знаходить рішення. Чи знає вона, як обмежити наслідки, зупинити зміни, відкотити систему, знайти інваріанти й відновити сервіс?»

**Практична перевірка ownership:**
1. Людина може пояснити задум зміни, залежності й найнебезпечніші failure modes.
2. Є тести/спостережуваність, runbook і перевірений шлях rollback або fallback.
3. Відомо, хто має право зупиняти, приймати ризик і повертати систему до роботи.

**SDD і супутні практики:** тут SDD = spec-driven development. Living documentation та code/documentation co-generation — гіпотези й інструменти. Згенерована документація не стає правильною автоматично. Потрібні перевірка актуальності та вправи на recovery.

**Що не стверджуємо:** кожна людина не мусить пам'ятати кожен рядок. Потрібна достатня колективна спроможність відновлення. Ми ще не знаємо, яка комбінація практик стане найкращою рівновагою.

**Перехід:** «Отже, задача не повернути старий процес, а знайти новий стійкий баланс».

## 7. We Are Searching for a New SDLC Equilibrium

```pptx-slide
{
  "number": 7,
  "layout": "equilibrium",
  "columns": [
    [
      "OLD EQUILIBRIUM",
      "Human writes\nHuman reviews\nHuman tests\nHuman operates"
    ],
    [
      "TODAY",
      "AI generation ↑↑\nReview adapting\nTesting adapting\nOwnership adapting"
    ],
    [
      "NEW EQUILIBRIUM",
      "?"
    ]
  ],
  "takeaway": "But this is only half of the transition.",
  "caption": "AI is entering the software itself.",
  "notes": "Невідоме не те, чи AI допомагає взагалі. Позитивні результати реальні. Ми ще шукаємо умови стійкої конверсії локальних gains у командну продуктивність. Old equilibrium — спрощення, не заперечення попередньої автоматизації.",
  "titleLines": [
    "We Are Searching for a New",
    "SDLC Equilibrium"
  ]
}
```

**Час:** 2:00.

**Роль:** завершити HOW we build і перейти до WHAT we build.

**На екрані:** три колонки:

| OLD EQUILIBRIUM | TODAY | NEW EQUILIBRIUM |
|---|---|---|
| Human writes | AI generation ↑↑ | ? |
| Human reviews | Review adapting | |
| Human tests | Evals/tests adapting | |
| Human operates | Ownership adapting | |

Під ними: **We don’t yet know how consistently local AI gains convert into sustainable system productivity.**

Після паузи: **But this is only half of the transition.**

**Композиція:** old зменшеної контрастності, today — активний центр, future — відкритий контур, а не вже спроєктований ідеальний workflow. Не малювати графік неминучої катастрофи або гарантованого прогресу.

**Що говорити:** «Нові дані вже показують позитивні результати. Невідоме не те, чи AI взагалі допомагає. Невідоме — за яких умов локальні gains стабільно стають командною продуктивністю, без накопичення неприйнятного rework, ризику чи втрати ownership».

Старий equilibrium — спрощений людсько-центричний образ, не твердження, що до AI не було автоматизації.

**Pivot дослівно:** «AI isn’t only changing how we build software. It is entering the software itself».

# ACT II — AI змінює WHAT we build

## 8. When Software Starts Thinking

```pptx-slide
{
  "number": 8,
  "layout": "thinking",
  "definition": "A system where consequential runtime responsibility partly depends on probabilistic Model Judgment.",
  "labels": [
    "Software 1.0",
    "Software with Model Judgment"
  ],
  "formulae": [
    "y = f(x)",
    "y ~ P(y | x)"
  ],
  "takeaway": "Engineer the useful region of behavior.",
  "caption": "Distribution also depends on context, model and configuration.",
  "notes": "Thinking Systems — інженерна категорія, не твердження про свідомість. Формули — спрощений контраст. Точніше P(y | x, c, m): контекст, модель і конфігурація також мають значення. Стабільне повторення не гарантує істинності. Наскрізний умовний кейс: IT-асистент використовує дозволені джерела, але не має права на неавторизовані зміни доступу.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/uncertainty-in-the-controlled-object.md"
  ]
}
```

**Час:** 3:00.

**Роль:** запровадити Thinking Systems як інженерний термін, не антропоморфізм.

**На екрані:**

**Thinking Systems**\
A system where consequential runtime responsibility partly depends on probabilistic Model Judgment.

Два поля:
- Software 1.0: **y = f(x)**
- Software with Model Judgment: **y ~ P(y | x)**

Нижче: **Engineer the useful region of behavior.**

**Композиція:** зліва один input → один заданий output. Справа той самий input → кілька можливих відповідей; допустимі обведені однією межею, неприйнятна поза нею. Не показувати, ніби всі outputs рівноймовірні або весь продукт перестає мати звичайну логіку.

**Що говорити:** «Thinking означає, що суттєвий runtime-крок делеговано Model Judgment. Це може бути вибір відповіді, інтерпретація звернення, пошук дії. Людина заздалегідь не виписала кожен допустимий результат».

Формула — контраст для пояснення. Реальне P залежить також від model version, prompt, retrieved context, tools і параметрів. Звичайне software теж може бути недетермінованим. Навіть стабільне повторення відповіді не гарантує її правильності.

**Наскрізний навчальний приклад для слайдів 8–12:** внутрішній IT-асистент відповідає за затвердженою базою знань і може підготувати заявку. Він не може сам собі надати права або змінювати доступ користувачів. Це вигаданий pilot, не реальний case study.

**Матеріал старої презентації:** зберегти deterministic/probabilistic контраст; не додавати окрему лекцію про LLM architecture.

**Перехід:** «Як написати вимогу, якщо правильна відповідь не одна?»

## 9. Requirements Become Boundaries

```pptx-slide
{
  "number": 9,
  "layout": "boundaries",
  "old": "Button A → Window B",
  "topics": [
    "Topics & sources",
    "Constraints",
    "Acceptable semantic movement",
    "Business risk"
  ],
  "allowed": "APPROVED OPERATING ENVELOPE",
  "outside": "FORBIDDEN",
  "escalate": "Clarify / escalate",
  "takeaway": "Requirements define where acceptable behavior may exist.",
  "notes": "Для IT-асистента: лише затверджені джерела й доступний цьому користувачу контекст. Можна перефразувати, але не вигадувати кроки чи прибирати approval. Недостатні докази означають уточнення або ескалацію. Заборони реалізуються також поза моделлю. Operating Envelope доповнює повний Requirement, не підміняє його. API, права доступу та детерміновані інваріанти залишаються.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/requirements-correctness-and-bugs.md"
  ]
}
```

**Час:** 3:00.

**Роль:** конкретизувати safe operating envelope.

**На екрані:**
- OLD: **Button A → Window B**
- NEW: **Define the safe operating envelope**

У центрі область допустимої поведінки з підписами:
- Topics & sources
- Constraints
- Forbidden regions
- Acceptable semantic movement
- Business risk

Висновок: **Requirements define where acceptable behavior may exist.**

**Композиція:** ліворуч маленький детермінований приклад; праворуч велика область allowed, тонке кільце clarify/escalate і чітка forbidden zone. Це семантичні категорії, не виміряні координати та не probability density.

**Конкретне наповнення прикладом IT-асистента:**

| Вимір | Контракт |
|---|---|
| Topics / sources | Внутрішні IT-процедури; лише дозволені документи та доступний цьому користувачу контекст |
| Acceptable movement | Можна перефразувати чи скоротити; не можна вигадати крок, змінити необхідність approval або приховати важливе попередження |
| Hard constraints | Не розкривати чужі дані й не виконувати неавторизовані зміни доступу |
| Missing evidence | Уточнити запит або передати людині; не домислювати інструкцію |
| Business envelope | Погоджені показники корисності, latency, cost і частки ескалацій |

Таблиця — у нотатках або як три короткі callout-приклади, не паралельно з усіма підписами області.

**Що говорити:** «Не “асистент має бути helpful”, а: з яких джерел він може відповідати, що може змінювати у формулюванні, яких дій не має права робити і що робить, коли доказів недостатньо».

**Уточнення:** звичайні requirements не зникають. Схеми даних, API, права доступу й інваріанти залишаються точними. Behavioral envelope додається там, де працює judgment. Заборону реалізуємо також поза моделлю, не лише prompt.

**Перехід:** «Тепер нам потрібні докази, що поведінка лишається в цих межах».

## 10. One Green Test Proves Almost Nothing

```pptx-slide
{
  "number": 10,
  "layout": "evaluation",
  "steps": [
    "Golden Set",
    "Repeated runs",
    "Distribution",
    "Metric gates",
    "Release"
  ],
  "old": "Input → Expected Output → PASS",
  "overall": "98% overall",
  "critical": "1 critical boundary violation",
  "decision": "BLOCK RELEASE",
  "takeaway": "Release evidence must match the risk being controlled.",
  "caption": "Illustrative: 196/200 acceptable evaluations; not a sample-size recommendation.",
  "notes": "Навчальний приклад: 99/100 routine, 39/40 ambiguous, 39/40 missing evidence, 19/20 access/privacy = 196/200 = 98%. Одна помилка — витік чужих даних. Загальний utility gate не перекриває critical boundary. Golden Set потребує покриття сценаріїв; repeated runs не роблять нерепрезентативні дані репрезентативними. Semantic judges калібруємо. Unit, integration і security tests залишаються."
}
```

**Час:** 3:00.

**Роль:** перейти від одного вдалого output до оцінки поведінки в релевантних умовах.

**На екрані:**
- OLD: Input → Expected Output → PASS
- NEW: Golden Set → Repeated Runs → Distribution → Metric Gates → Release

Головна теза: **One correct answer is one observation.**\
Друга: **Release evidence must match the risk being controlled.**

**Композиція:** старий шлях — тонка верхня смуга; новий — основний. Під Distribution — кілька компактних груп результатів за сценаріями, не декоративна Gaussian curve. Під Gate — дві окремі перевірки: utility і critical failures.

**Числовий навчальний приклад, чітко позначений Illustrative — not study data:**

| Сегмент | Прийнятні оцінювання |
|---|---:|
| Routine IT questions | 99 / 100 |
| Ambiguous requests | 39 / 40 |
| Missing/outdated evidence | 39 / 40 |
| Access / privacy boundary | 19 / 20 |
| Усього | 196 / 200 = 98% |

Умовно один із чотирьох неприйнятних результатів — розкриття чужих даних. Загальні 98% тоді не означають «можна релізити»: критична межа порушена. 200 — кількість оцінювань у прикладі, не універсально достатній розмір вибірки.

**На екрані з прикладу:** тільки **98% overall** і **1 critical boundary violation → block release**. Повна таблиця в нотатках.

**Що говорити:** Golden Set покриває типові, неоднозначні, adversarial, рідкісні та дорогі помилки. Повторні запуски допомагають побачити мінливість, але не замінюють репрезентативності кейсів. Автоматичні semantic judges потрібно калібрувати за людською рубрикою; модель-оцінювач не є безпомилковим oracle.

**Уточнення заголовка:** один тест може довести конкретну властивість конкретного шляху. «Almost nothing» стосується широкого висновку про надійність імовірнісної поведінки. Unit, integration, security та property-based тести зберігаємо.

**Перехід:** «Це змінює практичний зміст Ready, Done і рішення про release».

## 11. DoR / DoD Become Risk Contracts

```pptx-slide
{
  "number": 11,
  "layout": "risk",
  "table": [
    [
      "",
      "Traditional shorthand",
      "Thinking System"
    ],
    [
      "READY",
      "Specification known",
      "Tolerance / risk envelope known"
    ],
    [
      "DONE",
      "Tests pass",
      "Evaluation evidence within boundaries"
    ],
    [
      "RELEASE",
      "Yes / no",
      "Measured risk accepted"
    ]
  ],
  "takeaway": "Quality is released as a measured distribution.",
  "caption": "Evidence, decision owner and fallback belong in the contract.",
  "notes": "Ready: scope, заборонені дії, ризики, рубрика, Golden Set, ескалація та decision owner. Done: зафіксована конфігурація model/prompt/retrieval/tools/policy, результати за сегментами, перевірені permissions і rollback. Release: погоджені аудиторія пілота, monitoring та умови зупинки. Класичний engineering також працює з ризиком. PM координує, але не привласнює security/business authority. Delivery release не розширює project authorization.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/01-patterns/thinking-system-review.md"
  ]
}
```

**Час:** 3:00.

**Роль:** центральний для PMDay слайд: прив'язати delivery commitments до меж ризику й доказів.

**На екрані:** одна матриця:

| | Traditional shorthand | Thinking System |
|---|---|---|
| READY | Specification known | Tolerance / risk envelope known |
| DONE | Tests pass | Evaluation evidence within boundaries |
| RELEASE | Yes / no | Measured risk accepted |

Внизу: **Quality is released as a measured distribution, not a one-off observation.**

**Композиція:** три великі рядки; права колонка займає 55–60%. READY, DONE, RELEASE розрізняються кольором/іконкою стану, а не трьома окремими схемами. Під таблицею невеликий підпис: **Evidence, owner, fallback.**

**Конкретний risk contract для умовного IT-пілота:**

- **Ready:** відомі користувачі й scope; заборонені дії; типи помилок; рубрика; Golden Set; правила ескалації; відповідальний за прийняття залишкового ризику.
- **Done:** зафіксована конфігурація model/prompt/retrieval/tools/policy; є результати за сегментами, review критичних кейсів, перевірені permission gates і rollback.
- **Release:** відповідальний погодив цільову аудиторію пілота, межі ризику, rollout, monitoring та умови зупинки.

**За потреби конкретні числа — лише навчальні:** gate ≥95% acceptable evaluations overall; жодного виявленого критичного порушення в погодженому наборі; обов'язкове ручне approval для змін доступу. Показник 98% зі слайда 10 проходить utility gate, але падає на critical gate.

**Що говорити:** «Done тепер не просто “демо відповіло правильно”. Ми маємо вказати, за якою версією системи, на яких сценаріях і з якими обмеженнями отримали evidence. Release — явне рішення про залишковий ризик, а не магічне обнулення ризику тестами».

**Не створювати straw man:** класичний engineering також керує ризиками. Тут ризикові межі й evaluation evidence стають видимішою частиною контракту. PM координує рішення; юридичні, security чи бізнес-повноваження не переходять до PM автоматично.

**Перехід:** «Але конфігурація й потік запитів після релізу не залишаються незмінними».

## 12. Production Needs a Control Loop

```pptx-slide
{
  "number": 12,
  "layout": "control",
  "steps": [
    "Intent",
    "Model",
    "Proposed action",
    "Policy gate",
    "User / tool"
  ],
  "loop": [
    "Observe",
    "Evaluate / decide",
    "Act within authority"
  ],
  "actions": "Correct / retry / escalate / fallback / stop",
  "takeaway": "Production needs evidence connected to corrective action.",
  "caption": "Gate consequential actions before execution. Review incidents into Golden Sets.",
  "notes": "Архітектура спрощена. Policy gate стоїть перед зовнішньою дією. Evidence саме по собі не control: потрібні reference conditions, уповноважене рішення й ефективний шлях виконання. Runtime не розширює меж вищого рівня. Retry має бюджет. Kill switch має owner і runbook. Монітор має false positives / false negatives. Інцидент після review поповнює Golden Set; автоматичного навчання на приватних даних не припускаємо.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/control-loop-anatomy.md"
  ]
}
```

**Час:** 3:00.

**Роль:** пояснити production architecture без окремої лекції з control theory.

**На екрані:** основний шлях Intent → Model → Proposed output / action. До зовнішньої дії — Policy / permission gate.

Від результату й контексту — гілка Measure → Evaluate → Control, яка повертається до процесу. Під Control: **Correct · Retry · Escalate · Fallback · Stop**.

Головна теза: **Observe → Evaluate → Control.**

**Композиція:** компактний замкнений контур, що вміщується у 5 основних блоків. Safe output → user, небезпечна пропозиція → blocked/escalated. Стрілку feedback from incidents вести до Golden Set / policy маленьким нижнім контуром. Не дублювати всі старі UA layers.

**Що саме стоїть за блоками:**

| Observe / measure | Decide | Act |
|---|---|---|
| Запит, доступний контекст, версії, tool calls, output, latency/cost, feedback | Перевірка прав, рубрика, пороги, сегмент, ознаки drift | Обмежений retry, уточнення, safe fallback, HITL, зупинка функції |

**Приклад:** асистент пропонує операцію з доступом. Право виконання перевіряє окремий механізм. Якщо потрібного дозволу немає — дія блокується і йде на approval; не чекаємо, поки післядієвий монітор знайде шкоду. Низька якість відповіді може вести до уточнення чи пошуку іншого документа, але з бюджетом повторів.

**Що говорити:** «Pre-release eval — фотографія конкретної конфігурації на конкретних даних. У production змінюються model, prompt, context, documents, tools і user distribution. Тому потрібен механізм помічати відхилення й безпечно діяти».

**Уточнення:** semantic monitor має false positives і false negatives. Самооцінка confidence моделі — не автоматично калібрована ймовірність. Kill switch має owner і перевірений runbook. Retry не безмежний. Incidents потрапляють у Golden Set після review; автоматичного навчання на сирих приватних даних не припускаємо.

**Перехід:** «Якщо змінився об'єкт, який ми контролюємо, переміщується й відповідальність ролей».

## 13. The Roles Move With the System

```pptx-slide
{
  "number": 13,
  "layout": "roles",
  "table": [
    [
      "Role",
      "Before",
      "Increasingly owns"
    ],
    [
      "PM",
      "Story / acceptance",
      "Risk & tolerance"
    ],
    [
      "QA",
      "Pass / fail cases",
      "Measurement & evaluation"
    ],
    [
      "Architect",
      "Components & flows",
      "Boundaries & failure containment"
    ],
    [
      "Developer",
      "Implementation",
      "Behavioral / operational ownership"
    ]
  ],
  "takeaway": "The job titles may stay. The object of responsibility changes.",
  "notes": "Функції розширюються, а попередні обов'язки не зникають. PM координує tolerance. QA калібрує вимірювання. Architect визначає дозволений judgment, permissions і containment. Developer відповідає за implementation, ownership, instrumentation та runbooks. Це не вимога нового headcount і не передача всіх рішень PM."
}
```

**Час:** 2:00.

**Роль:** підсумувати трансформацію ролей однією матрицею.

**На екрані:**

| Role | Before: familiar emphasis | Increasingly owns |
|---|---|---|
| PM | Story / acceptance | Risk & tolerance |
| QA | Pass/fail cases | Measurement & evaluation |
| Architect | Components & flows | Boundaries & failure containment |
| Developer | Implementation | Implementation + behavioral / operational ownership |

Внизу: **The job titles may stay. The object of responsibility changes.**

**Композиція:** матриця на весь центральний простір; виділити праву колонку, без чотирьох персонажів і чотирьох мініслайдів. Кожен ряд — одна коротка фраза на комірку. Старі функції не закреслювати: це розширення, не заміна.

**Що конкретно змінюється:**
- **PM — tolerance operator:** допомагає визначити, що вважаємо допустимим результатом, яка помилка найдорожча, де потрібна людина; узгоджує decision owner.
- **QA — sensor calibrator:** будує Golden Sets, рубрики й eval coverage; перевіряє калібрування оцінювача, drift і невизначеність, а не тільки формальне pass/fail.
- **Architect — systems risk engineer:** вирішує, де judgment допустимий; задає deterministic permissions, isolation, fallback і containment.
- **Developer:** відповідає за реалізацію, зрозумілість прийнятого коду, інструменти моделі, instrumentation, runbooks та поведінку компонента.

**Що говорити:** «Це не прогноз, що завтра перейменують усі посади. Це опис нових питань, на які має бути відповідальна людина. Якщо це вже хтось робить — чудово. Якщо ні — сама наявність чотирьох job titles не закриває прогалину».

**Перехід:** «Тепер можемо звести HOW і WHAT в один висновок».

# ACT III — Зводимо дві половини разом

## 14. Engineering Rigor Moves — It Doesn’t Disappear

```pptx-slide
{
  "number": 14,
  "layout": "synthesis",
  "columns": [
    [
      "HOW WE BUILD",
      "Scarcity moves",
      [
        "Code generation gets cheaper",
        "Comprehension becomes scarce",
        "Bottlenecks move",
        "SDLC seeks a new equilibrium"
      ]
    ],
    [
      "WHAT WE BUILD",
      "Rigor moves",
      [
        "Output → Distribution",
        "Requirement → Boundary",
        "Test → Measurement",
        "Release → Risk decision",
        "Production → Control loop"
      ]
    ]
  ],
  "takeaway": "The team remains accountable for the whole system.",
  "closing": "Leverage does not remove engineering responsibility.",
  "notes": "AI gives us extraordinary leverage. But leverage does not remove engineering responsibility. It moves where engineering rigor has to live. Для HOW: protect comprehension and ownership. Для WHAT: measure, bound and control judgment. Стрілки означають розширення предмета інженерії, не усунення tests або requirements.",
  "titleLines": [
    "Engineering Rigor Moves —",
    "It Doesn’t Disappear"
  ]
}
```

**Час:** 3:00.

**Роль:** завершити тією самою двочастинною картою, з якої почали.

**На екрані:** дві колонки:

| AI changes HOW we build | AI changes WHAT we build |
|---|---|
| **Scarcity moves** | **Rigor moves** |
| Code generation gets cheaper | Output → Distribution |
| Comprehension becomes scarce | Requirement → Boundary |
| Bottlenecks move | Test → Measurement |
| SDLC seeks a new equilibrium | Release → Risk decision |
| | Production → Control loop |

Між/під колонками великим: **The team remains accountable for the whole system.**

**Композиція:** та сама геометрія й кольори, що на слайді 1. Без нових графіків, нових даних та UA-реклами. QR на матеріали, якщо потрібен, не конкурує з фінальною тезою.

**Фінальний текст виступу:**

«AI gives us extraordinary leverage.

But leverage does not remove engineering responsibility.
It moves where engineering rigor has to live».

Українське розгортання: «У розробці недостатньо оптимізувати генерацію окремо від усього потоку. Нам треба зберегти comprehension і ownership. У продукті недостатньо поводитися з probabilistic judgment так, ніби це завжди точна функція. Його треба вимірювати, обмежувати та контролювати».

**Два практичні висновки:**
- For AI-assisted development: don’t optimize generation in isolation. Protect comprehension and ownership.
- For Thinking Systems: measure judgment, bound its authority, and control its consequences.

**Важливе уточнення:** стрілки Output → Distribution та Test → Measurement означають розширення предмета інженерії; outputs, тести та звичайні вимоги нікуди не зникають.

**Закінчення:** пауза після whole system / engineering responsibility, потім Q&A. Не закінчувати списком невизначеностей без позиції: позиція — можливості AI великі, відповідальність і контроль залишаються.

# Додаток для підготовки — не додаткові слайди

## Реєстр джерел і редакторські рішення

| Джерело у базі Subprime / додане оновлення | Використання в цій доповіді |
|---|---|
| NBER WP 35275, May 2026 | Основний наскрізний доказ для слайда 4: покоління інструментів, downstream attenuation, marketplace consumption |
| METR developer RCT, July 2025 | Датований контрольований контекст у нотатках; не headline сучасних агентів |
| METR task horizons, March 2025 | Не виводити старі capability-цифри: для погодженого слайда 2 вони не потрібні |
| Xu, v3 January 2026 | Перерозподіл contribution/review; прямо назвати старий період даних |
| Agarwal, v2 January 2026 | Repo-level complexity/warnings; точні групові оцінки та значущість |
| Peng, 2023 | Залишається історичним позитивним експериментом у базі; не витісняє актуальні джерела на слайді |
| GitClear quality, 2025 | Для основного викладу замінено новішим звітом June 2026 |
| GitClear productivity, 2025 | Історичні показники не змішувати з quality report; не headline 2026 |
| DORA 2025 — доповнення | Основний DORA; не переносити коефіцієнти 2024 |
| METR May 2026 — доповнення | Нові self-reports із видимим обмеженням методу |
| GitClear June 2026 — доповнення | Актуальні публічні quality indicators, не причинна оцінка |

Історичні перевірки, корисні для чистоти evidence base, але не для основного екрана:
- [Peng 2023](https://arxiv.org/html/2302.06590v1): 95 рандомізованих учасників, 70 завершень (по 35); 71,17 проти 160,89 хвилини серед завершень, скорочення часу 55,8%. Не 196 учасників.
- [GitClear productivity 2025](https://www.gitclear.com/research/ai_tool_impact_on_developer_productive_output_from_2022_to_2025): середні added LOC 1 314 → 3 037 (+131,1%), медіанні 921 → 1 624 (+76,3%). Це не тотожне «delivery productivity». Не зводити різні вибірки й композити до одного причинного ефекту.
- [GitClear quality 2025](https://www.gitclear.com/ai_assistant_code_quality_2025_research): старі 211 млн changed LOC — інший звіт; не підставляти цей обсяг під нові метрики 2026.
- DORA 2024 не використовується як доказ сучасного негативного throughput effect. Звіт 2025 змінює цю частину картини.

## Додаткова перевірка арифметики й формулювань

- NBER, LOC: 1 + (228,2 + 741,3 + 658,3) / 100 = 17,278 → 17,3×.
- NBER, commits: 1 + (35,9 + 109,1 + 33,6) / 100 = 2,786 → 2,8×.
- NBER, releases: 1 + (10,2 + 20,3) / 100 = 1,305 → 1,3×; async окремо не ідентифіковано.
- NBER: +1627,8% — приріст, 1727,8% базового рівня — рівень; це не однакові записи.
- iOS: 86 − 79 = 7 відсоткових пунктів; Chrome: 31 − 18 = 13 пунктів.
- GitClear duplication: 73 / 40,3 − 1 ≈ 81,1%. Відносна арифметика правильна, абсолютна одиниця в публічних матеріалах неузгоджена.
- Refactoring share 13% → 3,8%: падіння на 9,2 відсоткових пункту, не на 9,2% відносно бази.
- Навчальний eval: 99 + 39 + 39 + 19 = 196; 196 / 200 = 98%; критична помилка не зникає від агрегування.
- Ми не обчислюємо універсальний conversion rate LOC → releases → user value з різних наборів outcomes.
- Ми не об'єднуємо self-report, RCT, observational DiD та комерційні code proxies в один pooled effect.
- Ми не вважаємо відсутність видимого aggregate usage приросту доказом відсутності будь-якої користі для будь-якого користувача.

## Таймінг

| Слайд | Час |
|---|---:|
| 1 | 1:00 |
| 2 | 3:00 |
| 3 | 2:30 |
| 4 | 4:30 |
| 5 | 2:30 |
| 6 | 2:30 |
| 7 | 2:00 |
| 8 | 3:00 |
| 9 | 3:00 |
| 10 | 3:00 |
| 11 | 3:00 |
| 12 | 3:00 |
| 13 | 2:00 |
| 14 | 3:00 |
| **Виступ** | **38:00** |
| **Резерв** | **2:00** |

## Що не змінюємо й не додаємо

Не додаємо окремих слайдів NBER/METR/GitClear, окремих слайдів для кожної ролі, повного UA stack, Prompt Registry, token economics чи рекламного фіналу. Не вигадуємо емпіричних чисел для концептуальних слайдів 1–3 і 5–14. Потрібна деталізація змісту погодженої структури, а не нова структура.
