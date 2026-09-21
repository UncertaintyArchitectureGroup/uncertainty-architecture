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

**[Evidence base — звіти й зовнішні посилання](EVIDENCE.md):** використані редакції, прив'язка до слайдів, обмеження, історичний контекст і матеріали Subprime / UA.

**Структуру відновлено буквально:** ті самі 14 назв, той самий порядок і та сама драматургія. Слайд 4 залишається спільним evidence slide. Слайди 5–7 — comprehension, відповідальність команди та пошук нового SDLC equilibrium, а не окремі слайди про звіти.

Головна дуга: технологічний зсув → HOW we build → дисбаланс SDLC → WHAT we build → Thinking Systems → requirements, QA, release, production і ролі → engineering rigor переходить у нові місця, а не зникає.

Таймінг: 38 хвилин + 2 хвилини резерву. Повноцінне Q&A — окремо. Англійська — для заголовків і коротких екранних формулювань; українська — для пояснень і виступу.

### Що і як перевірено

Відправна точка — [реєстр evidence/SOURCES.md у Subprime](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/blob/main/evidence/SOURCES.md), його бібліографія, звіт та NBER evidence brief. Реєстр не означає, що кожен запис уже пройшов повний аудит: стан Registered відрізняється від Verified. Для чисел нижче пріоритет мають самі автори досліджень.

Для актуальності додано новіші авторські публікації, навіть якщо їх ще немає в реєстрі Subprime: DORA 2025, METR за травень 2026, GitClear за червень 2026. Xu використано у v3 від 28 січня 2026, Agarwal — у v2 від 27 січня 2026. Нова дата версії не робить старі дані новими: це окремо зазначено.

Перевірка означає звірку таблиць, підписів, одиниць вимірювання, дат, дизайну досліджень і арифметики. Вона не означає незалежне відтворення оцінок на сирих даних. Для NBER прочитано наданий оригінальний PDF і візуально звірено ключові таблицю та графіки. Для DORA використано повний звіт v.2025.2 із public mirror, авторське резюме та офіційну інфографіку. Для GitClear — публічний виклад і доступний графік; перевірка повного закритого GitClear whitepaper не заявляється.

### Стиль і технічний контракт PPTX

Погоджено maintainer 21 вересня 2026. Ці вимоги стосуються саме цієї презентації, не всіх UA artifacts.

- Суцільний темний фон #0B0F14 на КОЖНОМУ слайді, заданий властивістю background. Жодних фонових картинок, градієнтів або full-slide screenshot.
- Світлий текст #F4F7FA; допоміжний #ADB8C5. Cyan #28C7F7 для можливостей/потоку; amber #F5B61C для меж/контролю; red #FF6B75 лише для failure/block.
- 16:9, 1280×720 design canvas; одна узгоджена сітка з полями 64 px.
- DejaVu Sans, наявний у зафіксованому authoring runtime. На машині доповідача шрифт має бути встановлений або узгоджено замінений із повторною visual QA. Текст не перетворювати на криві для обходу відсутнього шрифту.
- Заголовки 40 px (30 pt), довгі — у два зафіксовані рядки; головний текст 28–32 px; великі числа 44–66 px; щільні evidence labels 20–24 px. Для заголовків і схем залишати запас ширини, а не впритул до країв. Не приховувати substantive caveats у мікрошрифті.
- Усі заголовки, абзаци, формули, блоки, стрілки, таблиці та схематичні криві — НАТИВНІ РЕДАГОВАНІ об'єкти PowerPoint.
- Для даних використовувати native charts або точні числові підписи; для схем — shapes/connectors. Не rasterize SVG/Mermaid/HTML як зручний обхід.
- Окреме зображення дозволене для прямо погодженої концептуальної ілюстрації; інформаційні схеми й дані робити native tools. Воно не є фоном, не містить запеченого заголовка/тексту слайда і має записаний exception rationale. За запитом maintainer у поточній редакції дозволено один виняток: концептуальна imagegen-ілюстрація на слайді 1 (artwork/ai-two-roles.png). Вона не є фоном або джерелом даних; усі тексти, числа й схеми залишаються нативними. Prompt і походження — в artwork/PROVENANCE.md.
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
      "AI helps a developer write software."
    ],
    [
      "WHAT WE BUILD",
      "AI interprets a user’s request at runtime."
    ]
  ],
  "takeaway": "They are related. They are not the same.",
  "notes": "Відділити AI для розробки від Model Judgment усередині продукту. Перше змінює виробництво software, друге — поведінку системи. Не починати з реклами UA чи anti-AI тези.\nІлюстрація показує конкретні ролі: зліва розробник працює з AI coding assistant, справа користувач просить продукт скласти план подорожі. AI-generated illustration, OpenAI imagegen, 21 September 2026. Вона не задає архітектуру системи. Prompt: artwork/PROVENANCE.md.",
  "illustrationAlt": "Two concrete scenes: a developer uses an AI coding assistant; a user asks an AI-powered travel application to plan a trip."
}
```

**Час:** 1:00.

**Роль:** одразу відділити дві різні трансформації. Не починати з UA, Subprime Code чи переліку загроз.

**На екрані:**

Підзаголовок: **How we build software. And what software is.**

Два змістові блоки без стрілок:
- HOW WE BUILD — AI helps a developer write software.
- WHAT WE BUILD — AI interprets a user’s request at runtime.

**Композиція:** великий заголовок зверху, широка ілюстрація двох конкретних сцен: зліва розробник із AI coding assistant; справа користувач просить AI-продукт спланувати подорож. Підписи під сценами пояснюють HOW / WHAT. Це художня метафора, не технічна схема чи виміряні дані. Увесь текст — окремі редаговані об'єкти. Ім'я й PMDay — підпис унизу.

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
      "Externalized\nMemory",
      "Records we\ncan retrieve"
    ],
    [
      "Computers",
      "Externalized\nCalculation",
      "Rules we\nexplicitly encode"
    ],
    [
      "Large Models",
      "Externalized\nCognition",
      "Judgment shaped\nby context"
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

**Композиція:** три рівні блоки завширшки 300 px з однаковими зовнішніми полями 112 px та проміжками 78 px, зі стрілками, приєднаними до середини їхніх бічних граней: текст/пам'ять, обчислення, робота з мовою та контекстом. Останній блок виділити кольором, а не намалювати «штучний мозок». Нижній ряд про engineering consequence з'являється після пояснення трьох блоків.

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
  "notes": "Theory of Constraints (Goldratt): оптимізуємо потік через реальне обмеження системи. Якщо coding не bottleneck, його прискорення саме по собі не збільшує пропускну здатність delivery. Якщо був bottleneck, після зміни обмеження може переміститися. AI може змінювати Intent і Design так само, як Review, Test, Integration, Deploy та Operate; знак і величину ефекту треба вимірювати.\nНавчальний приклад, не дослідження. ДО AI: code виробляє 8 змін/тиждень, review може опрацювати 8, integration може інтегрувати 8. Потік збалансований. ПІСЛЯ AI: генерація коду зростає до 100 зіставних змін/тиждень, але review та integration лишаються на 8. Інші етапи не прискорилися автоматично. За незмінної потужності та push без WIP limits/відкидання роботи загальний backlog зростає на 100 − 8 = 92 зміни за тиждень. Integration позначено як умовний bottleneck, не універсальний bottleneck команд.\nЦе не твердження, що будь-яка оптимізація не-bottleneck автоматично погіршує систему: економія витрат або вільна потужність теж можуть бути корисні. Черга виникає, коли реально збільшується надходження понад вихід. Rework, більші batches, затриманий feedback і тиск на review можуть погіршити якість; це механізм ризику, а не математично неминучий ефект. Джерела й межі: evidence/toc-wip.md.\nНа слайді немає фонового зображення чи стрілок: етапи з’єднані короткими нейтральними лініями.",
  "scope": "AI can affect every stage. Downstream gains are not automatic.",
  "toc": "Delivery stays at 8/week. WIP grows; overload can reduce quality.",
  "exampleCaveat": "Push system: no WIP limit, no discarded work.",
  "sources": [
    "https://dora.dev/capabilities/wip-limits/",
    "https://dora.dev/capabilities/working-in-small-batches/",
    "https://www.nber.org/papers/w35275"
  ],
  "exampleHeading": "Illustrative team: changes per week; comparable work, fixed downstream capacity.",
  "exampleStages": [
    "Code",
    "Review",
    "Integrate"
  ],
  "exampleRows": [
    [
      "BEFORE",
      "Balanced flow",
      [
        "8",
        "8",
        "8"
      ],
      "0"
    ],
    [
      "AFTER AI",
      "Other stages have\nnot sped up",
      [
        "100",
        "8",
        "8"
      ],
      "+92"
    ]
  ]
}
```

**Час:** 2:30.

**Роль:** відділити локальну швидкість від пропускної здатності delivery system.

**На екрані:** один наскрізний SDLC:

Intent → Design → Code → Review → Test → Integrate → Deploy → Operate

CODE підсвічений; питання стоять також над Intent і Design та рештою етапів. AI може впливати на весь SDLC, а не тільки на Code. Усі зв’язки показані короткими нейтральними лініями без наконечників; стрілок і фонових зображень на слайді немає.

Основна теза: **Local acceleration ≠ system throughput.**

**Композиція:** компактний SDLC із рівними полями 96 px; нижче явні ряди BEFORE та AFTER AI. До AI: Code 8 → Review 8 → Integrate 8, backlog 0. Після AI: Code 100 → Review 8 → Integrate 8, backlog +92/тиждень за push без WIP limit. Review та integration не прискорюються автоматично. Схема не потребує анімації. Це навчальний приклад із незмінною потужністю, не дані дослідження.

**Theory of Constraints:** прискорення не-bottleneck не збільшує throughput за незмінного обмеження. Якщо реально подавати більше роботи, ніж bottleneck пропускає, накопичуються WIP і очікування. Під навантаженням можуть зростати rework і ризик погіршення якості. Не стверджувати автоматичну деградацію від будь-якої локальної оптимізації. Джерела й припущення: [ToC / WIP](evidence/toc-wip.md).

**Конкретний навчальний приклад для нотаток:** умовна команда пише 8 змін за тиждень, перевіряє 8 та інтегрує 8. Якщо генерація стає 100 змін/тиждень, це саме по собі не збільшує межу інтеграції 8. Приклад припускає зіставні зміни та незмінну потужність інших етапів; це не дані дослідження.

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
  "nberGeneration": "Cumulative across three tool generations",
  "nberCaveat": "Changed LOC = additions + deletions.\nAsync release effect not estimated.",
  "marketHeadline": "More apps. Aggregate usage\nflat or lower in these cohorts.",
  "marketDetail": "New cohorts; first 3 months. Usage proxies.",
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
  "takeaway": "Code activity, delivery and user value are different outcomes.",
  "notes": "NBER: понад 100 тисяч GitHub developers; matched event study, не RCT. Changed LOC = additions + deletions, не чисте зростання кодової бази.\nTable 5, друкована с. 33, тижні 21–30: Autocomplete — LOC +228.2%, commits +35.9%, PRs +11.0%, releases +10.2%. Synchronous agents — LOC +741.3%, commits +109.1%, PRs +65.5%, releases +20.3%. Asynchronous agents — LOC +658.3%, commits +33.6%, PRs +71.8%; releases не оцінено окремо. Figure 1, с. 3: cumulative LOC 17.3×, files 3.9×, commits 2.8×, PRs 2.5×, repos 1.5×, releases 1.3×. Не перемножувати компоненти.\nFigure 12, с. 41; §8.2, с. 42–43: iOS — 30–50 тисяч нових apps/month → близько 100 тисяч у квітні 2026; Android — 42 тисячі у січні 2025 → близько 60 тисяч у середині 2026; Chrome — 5 тисяч у 2023 → близько 13 тисяч у середині 2026. Total cohort usage за перші 3 місяці стабільне або знижується. Частка iOS apps із <10 ratings: 79→86%; Chrome extensions із <10 downloads: 18→31%. SourceForge без прискорення entry, не входить у три usage panels. Це не всі existing apps, не весь software market і не пряме вимірювання consumer welfare. Chrome decline передував agentic era.\nDORA 2025 v.2025.2: повний звіт отримано через публічне дзеркало; source URL, license і SHA-256 записано в evidence/sources.json. Figure 28, p.38: software delivery instability має standardized estimate приблизно +0.10 SD, 89% credible interval приблизно +0.07…+0.13, на +1 SD AI adoption. Це округлене зчитування графіка, не точна опублікована числова таблиця. Векторні координати та арифметика — evidence/dora-2025-figure28.json. Footnote 23, p.48 визначає стандартизацію. Appendix p.139: instability об’єднує change failure rate та deployment rework rate, тобто частку незапланованих deployments для виправлення user-facing bugs. Це оцінки респондентів у cross-sectional survey, не телеметрія CI/CD і не доведений причинний ефект. Не перекладати +0.10 SD як +10% failures. >80% і 59% — частки респондентів, які повідомляють про покращення productivity та code quality. Перевірений коефіцієнт 2024 +7.2% тут не підставляємо. Деталі: evidence/dora-2025.md.\nMETR, травень 2026: 349 technical workers; 1.4–2× median self-reported work value залежно від питання, 3× self-reported speed; є selection bias. Старий RCT 2025 із +19% часу — лише історичний контекст.\nGitClear 2026: частка moved code у changed lines 13% (2023) → 3.8% (YTD 2026), не кількість refactoring tasks і не весь reuse. Частота duplicated blocks приблизно +81% за цей період. Copy/paste share 9.4% (2022) → 15.7% (H1 2026), інший baseline. Публічне резюме GitClear 2026 прямо повідомляє +15% two-week code churn: частка нещодавно написаних рядків, переписаних/видалених упродовж двох тижнів. Це відносна зміна, не +15 відсоткових пунктів і не частка дефектів. Резюме не дає окремої пари базових значень churn. Function connectivity: 343 → 223 calls/1000 changed lines, 2023 → YTD 2026, приблизно −35%. Це щільність викликів, не весь reuse. Legacy update share: 1.7% → 0.46%; вступ каже 2022, детальний абзац 2023, тому baseline суперечливий і показник лишається в нотатках. Не змішувати churn, duplication та refactoring. Текст і графік 2026 суперечать щодо абсолютної одиниці duplication, тому залишаємо тільки відносні +81%. Це observational proxies, не причинний ефект AI. Деталі: evidence/gitclear.md.\nXu, v3 від січня 2026, дані 2020–22: top activity quartile — commits −19%, reviews +6.5%; bottom quartile — commits +43.5%, PRs +17.7%; rework +2.4%. Це не кадрові грейди й не агенти 2026 року.\nAgarwal, v2, Table 2: complexity +34.85/+42.87%, warnings +17.73/+19.00%; зміна IDE-first warnings статистично незначуща. Не трактувати це як борг на одну фічу.\nDORA: позитивний зв’язок AI adoption з throughput одночасно з негативним зі stability. Small batches, p.58: сильніший позитивний зв’язок AI із product performance та менше friction, хоча індивідуальні gains можуть бути меншими. ToC / review-testing-integration queues, p.81. Це мотивує системну оптимізацію на слайді 7, не доводить універсальну причинність.",
  "sources": [
    "https://www.nber.org/papers/w35275",
    "https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report",
    "https://metr.org/blog/2026-05-11-ai-usage-survey/",
    "https://www.gitclear.com/the_ai_code_quality_maintainability_gap",
    "https://arxiv.org/html/2510.10165v3",
    "https://arxiv.org/html/2601.13597v2",
    "https://dora.dev/research/2025/2025-DORA-Report-Infographic.pdf",
    "https://www.gitclear.com/ai_assistant_code_quality_2025_research",
    "https://www.shaunabram.com/wp-content/uploads/2025/10/2025_state_of_ai_assisted_software_development.pdf",
    "https://dora.dev/research/2025/questions/"
  ],
  "gitclearMetrics": [
    [
      "Moved-code share",
      "13% → 3.8%"
    ],
    [
      "Calls / 1k changed lines",
      "−35%"
    ],
    [
      "Duplicated blocks",
      "+81%"
    ],
    [
      "Two-week code churn",
      "+15%"
    ]
  ],
  "gitclearCaveat": "Observed code proxies; not a causal AI estimate.",
  "otherCards": [
    [
      "METR · MAY 2026",
      "1.4–2× work value",
      "Median self-reported work value; survey, not causal uplift"
    ],
    [
      "XU + AGARWAL · 2026",
      "+35% / +43%",
      "Agarwal: complexity proxy. Xu: contributor workload shifts."
    ]
  ],
  "doraInstability": "≈ +0.10 SD",
  "doraInterval": "89% credible interval ≈ +0.07 to +0.13",
  "doraMeasures": "Survey model, rounded reading of Fig. 28.\nSD = standard deviation, not a failure percentage.",
  "doraPerceptions": "Report improvement: >80% productivity; 59% code quality.",
  "doraHeadline": "Higher throughput\nLower delivery stability"
}
```

**Час:** 4:30.

**Роль:** показати різні рівні вимірювання — активність розробника, delivery, підтримуваність, командну роботу та використання продукту. Це один слайд, не новий act із шести слайдів.

### Що саме має бути на екрані

Дві колонки з чіткою вертикальною межею. Зліва — NBER та marketplace outcomes. Справа — одночасний позитивний зв’язок AI із throughput і негативний зі stability у DORA; приблизний standardized coefficient є підписом. Нижче — чотири окремі метрики GitClear. Унизу спільний ряд METR та Xu / Agarwal. Жодних стрілок між несумірними дослідженнями або outcomes; усі числа мають власні підписи. Докладні таблиці залишаються у нотатках.

**Велика картка NBER — May 2026:**
- **17.3× changed LOC**
- **2.8× commits**
- **1.3× releases**
- Видимий ряд: **Cumulative across three tool generations**
- Нижній блок: **More apps. No aggregate usage increase in the observed cohorts.**
- Один конкретний сигнал: **iOS apps with <10 ratings: 79% → 86%**.
- Критична примітка: **Cumulative estimates; separate async release effect not identified.**

**METR — May 2026:** **1.4–2× self-reported work value**; підпис **Survey, not measured causal uplift**.

**DORA — 2025:** **Higher throughput / Lower delivery stability** при вищому AI adoption. Підпис: **≈ +0.10 SD delivery instability per +1 SD AI adoption**, **89% credible interval ≈ +0.07 to +0.13**. Округлене зчитування Figure 28, p.38; survey model, не CI/CD telemetry. Instability = change failures + unplanned bug-fix deployments. Окремим рядком: >80% report productivity improvement; 59% report code-quality improvement — частки респондентів, не відсотки зміни швидкості/якості.

**GitClear — June 2026:** **Moved-code share: 13% → 3.8%**, **Calls / 1k changed lines: −35%**, **Duplicated blocks: +81%**, **Two-week code churn: +15%**. Видимий підпис: **Observed code proxies; not a causal AI estimate.** Періоди й визначення пояснюються в нотатках: moved lines — proxy refactoring, function calls — connectivity, churn — швидка переробка.

**Xu + Agarwal — 2026 versions:** **Workload shifts. Complexity rises in studied samples.** Один числовий ряд: **Complexity +35% / +43%**; назвати Agent-first / IDE-first. Цифри Xu — в нотатках, щоб не перетворити картку на таблицю.

Унизу слайда: **Code activity, delivery and user value are different outcomes.**

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

**DORA 2025.** [Офіційна інфографіка](evidence/originals/dora-2025-infographic.pdf) також містить **59%**, які повідомляють про покращення code quality. Це self-report, не зміна якості на 59%. Delivery stability — окремий outcome; говорити «якість коду впала» за цією association некоректно. Повний v.2025.2, Figure 28, p.38 тепер перевірено: приблизно +0.10 SD instability на +1 SD AI adoption, 89% credible interval приблизно +0.07…+0.13. Це зчитування графіка з округленням, не +10% failures, не telemetry й не causal estimate. Визначення та розрахунок див. у локальній нотатці. [Детальний запис](evidence/dora-2025.md). Майже 5 000 респондентів; 90% використовують AI, понад 80% повідомляють про вищу продуктивність, 30% мало або зовсім не довіряють AI-коду. Зв'язок adoption із throughput і product performance позитивний, зі stability — негативний. Це не причинні коефіцієнти. Числа DORA 2024 сюди не переносимо. [Офіційне авторське резюме DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report).

**METR, 11 травня 2026.** 349 technical workers; median self-reported work-value multiplier 1,4–2× залежно від формулювання питання, self-reported speed — 3×. Це не confidence interval і не об'єктивне вимірювання delivery. Вибірка самообрана. [METR survey](https://metr.org/blog/2026-05-11-ai-usage-survey/).

Історичний контрольований результат METR 2025: 16 розробників, 246 задач, +19% часу з early-2025 AI. Залишити як датований контекст, не актуальний вирок сучасним агентам. [METR RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). У [лютневому оновленні 2026](https://metr.org/blog/2026-02-24-uplift-update/) самі автори вказують на selection bias; не виводити з нього надійний універсальний поточний відсоток.

**GitClear, червень 2026.** Moved-code share — частка переміщених рядків серед changed lines: proxy reuse/refactoring, а не кількість refactoring tasks. Two-week churn **+15%** прямо наведено в публічному резюме 2026; це окрема від duplication метрика. Function calls **343 → 223 на 1000 changed lines**, приблизно **−35%**, 2023 → YTD 2026. Обидві метрики повернуто на екран. [Визначення, періоди й межі](evidence/gitclear.md). Moved/refactoring-related share: 13% у 2023 → 3,8% YTD 2026; function-call density −35%; block duplication приблизно +81%; two-week churn +15%. Це спостережні показники власної класифікації, не весь reuse і не встановлений причинний ефект AI. У тексті й графіку duplication є суперечність одиниць; тому абсолютні 40,3 і 73,0 не використовуємо як навантажену метрику. Відносна зміна узгоджується. [GitClear 2026](https://www.gitclear.com/the_ai_code_quality_maintainability_gap).

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
    [
      "Can we generate faster?",
      "YES"
    ],
    [
      "Can review keep pace?",
      "NOT AT THIS RATE"
    ],
    [
      "Will we understand it\nin 5 years?",
      "?"
    ]
  ],
  "takeaway": "Generation scales differently from comprehension.",
  "caption": "Illustrative overload scenario. Not measured trends or a five-year forecast.",
  "notes": "Концептуальний сценарій: генерація зростає значно швидше за майже незмінну спроможність цієї команди розуміти й перевіряти код. Горизонтальна людська лінія — припущення сценарію, не біологічна межа: AI, навчання й кращі інструменти можуть допомагати comprehension. YES стосується прискорення генерації; NOT AT THIS RATE — нездатності review в цьому сценарії встигати за заданим потоком. Знак питання про 5 років — ризик довгострокового розуміння, не емпіричний прогноз втрати знань. Comprehension debt тут рамка ризику, не готова метрика. Ні NBER, ні GitClear не вимірювали ці криві."
}
```

**Час:** 2:30.

**Роль:** показати асиметрію між генерацією й колективною здатністю розуміти, перевіряти та підтримувати прийнятий код.

**На екрані:** плавна висхідна лінія generation capacity і горизонтальна comprehension capacity. Без числової шкали. Обидві лінії — native editable paths. Сценарій явно позначено як illustrative overload, не виміряний тренд чи прогноз на п’ять років.

| Питання | Відповідь у показаному сценарії |
|---|---|
| Can we generate faster? | YES |
| Can review keep pace? | NOT AT THIS RATE |
| Will we understand it in 5 years? | ? |

**Композиція:** графік ліворуч, відповіді праворуч. Горизонтальна людська лінія показує фіксовану командну capacity у цьому сценарії; це не вічна межа людського розуміння.

**Що говорити:** «Генерувати швидше ми можемо. Але за цього темпу review вже не встигає. Чи збережемо достатнє розуміння системи через п’ять років? Відповідь залежить від процесу, який побудуємо зараз. AI також може допомагати comprehension, але цей ефект треба перевіряти окремо від generated volume».

**Перехід:** «Перевірка цього розуміння настає тоді, коли кодогенератор не може вирішити production-інцидент».

## 6. The Team Is the Last Line of Defense

```pptx-slide
{
  "number": 6,
  "layout": "recovery",
  "takeaway": "If AI cannot recover the system, the team still must.",
  "notes": "AI кодогенератор сам є технічною системою: обмеження контексту, доступних інструментів, модельних можливостей і надійності роблять його потенційною точкою відмови у delivery та recovery. Особливо в складному проекті ця залежність належить risk analysis і плану реагування. Умовний інцидент: сервіс недоступний; AI не знаходить придатного fix у межах дозволеного бюджету спроб. Команда спершу обмежує наслідки, використовує безпечний rollback/fallback де можливо, зупиняє безрезультатний цикл. Далі люди відновлюють розуміння задуму, інваріантів і залежностей, локалізують причину та пропонують fix. Перевірка repair і відновлення відбуваються під incident owner. Containment може йти паралельно з діагностикою; схема показує відповідальність, а не обов’язкове очікування відмови AI перед реагуванням. Генератор може продовжувати допомагати, але команда мусить мати перевірену спроможність діяти без його успіху. Не кожна людина пам’ятає всі рядки: потрібна достатня колективна спроможність. Watch / Explore перенесено на слайд 7.",
  "premise": "AI code generators are technical systems with limits.",
  "risk": "Their failure to fix an incident belongs in the project risk model.",
  "steps": [
    [
      "Production\nincident",
      "Contain impact.\nRoll back or use\nfallback where safe."
    ],
    [
      "AI cannot\nrecover",
      "Stop at the agreed\nretry limit. Preserve\ntraces and changes."
    ],
    [
      "Team diagnoses\n& proposes fix",
      "Reconstruct intent,\ndependencies and\nsystem invariants."
    ],
    [
      "Validate fix\nand restore",
      "Test the repair.\nRestore under incident\nowner authority."
    ]
  ],
  "caption": "Hypothetical scenario. Rehearse the human recovery path before production."
}
```

**Час:** 2:30.

**Роль:** перетворити ownership на конкретну спроможність діагностувати, виправляти та відновлювати систему.

**На екрані:** AI code generators are technical systems with limits. Їхню нездатність усунути інцидент слід враховувати як ризик проекту.

Чотири послідовні етапи: **Production incident → AI cannot recover → Team diagnoses and proposes fix → Validate fix and restore**. Під кожним — конкретні дії. Схема native/editable; hypothetical-сценарій позначений явно.

**Що говорити:** «Контекстне вікно, інструменти й можливості моделі не безмежні. Коли генератор не знаходить виправлення, відповідальність не зникає. Команда має розібратись у коді та залежностях, локалізувати причину і запропонувати перевірений fix. Таку можливість не можна вперше перевіряти на продакшні».

**Порядок реагування:** containment починається одразу; безпечний rollback/fallback може йти паралельно з діагностикою. Безрезультатні спроби AI зупиняються за погодженим бюджетом, traces зберігаються. Incident owner контролює рішення про відновлення.

**Практична перевірка:** команда вміє пояснити задум та інваріанти, має актуальні залежності/owner map, перевірені тести й runbook, а також відпрацьований шлях recovery без успішного AI-fix.

**Перехід:** «Це задає, за чим спостерігати й які практики випробовувати в новому SDLC».

## 7. We Are Searching for a New SDLC Equilibrium

```pptx-slide
{
  "number": 7,
  "layout": "equilibrium",
  "columns": [
    [
      "OLD EQUILIBRIUM",
      "Human-led flow"
    ],
    [
      "TODAY",
      "Generation outpaces review"
    ],
    [
      "NEW EQUILIBRIUM",
      "Sustainable flow?"
    ]
  ],
  "takeaway": "The new equilibrium must preserve understanding and recovery.",
  "caption": "Measure delivery and recovery. Next: AI inside the product.",
  "notes": "Watch і Explore перенесено зі слайда 6 та конкретизовано. Watch: review age, batch size, WIP; churn/duplication/reuse/complexity; зміни без owner та застаріла документація; практична здатність людей діагностувати й відновити систему. Це індикатори, не готовий індекс comprehension. Explore: small batches/WIP limits, spec-driven development та living architecture з code+docs review, repository intelligence для залежностей/owners, recovery drills без успішного AI. Для кожної практики перевіряти end-to-end lead time, rework, stability і recovery, а не generated LOC. DORA 2025 p.58 мотивує small batches, p.81 розглядає ToC і downstream queues. Документація й RI не мають тут доведеної універсальної ефективності. Потрібні baseline, актуальність і практична перевірка. Old equilibrium спрощений; попередня автоматизація не заперечується. Pivot: AI змінює не лише спосіб розробки, а й сам продукт.",
  "titleLines": [
    "We Are Searching for a New",
    "SDLC Equilibrium"
  ],
  "watchRows": [
    [
      "Flow pressure",
      "Review age, batch size and WIP"
    ],
    [
      "Rework and structure",
      "Churn, duplication, reuse, complexity"
    ],
    [
      "Ownership gaps",
      "Unowned changes and stale docs"
    ],
    [
      "Recovery readiness",
      "Unaided diagnosis and restore time"
    ]
  ],
  "exploreRows": [
    [
      "Small batches and WIP limits",
      "Keep intake within review capacity"
    ],
    [
      "Specs and living architecture",
      "Review code and docs together"
    ],
    [
      "Repository intelligence",
      "Trace dependencies and owners"
    ],
    [
      "Human recovery drills",
      "Diagnose and fix without the agent"
    ]
  ],
  "sources": [
    "https://dora.dev/capabilities/wip-limits/",
    "https://www.shaunabram.com/wp-content/uploads/2025/10/2025_state_of_ai_assisted_software_development.pdf"
  ]
}
```

**Час:** 2:00.

**Роль:** завершити HOW we build конкретними сигналами й перевірюваними практиками, потім перейти до WHAT we build.

**На екрані:** компактний ряд OLD EQUILIBRIUM / TODAY / NEW EQUILIBRIUM. Під ним дві змістові колонки:

| Watch | Explore |
|---|---|
| Review age, batch size, WIP | Small batches та WIP limits |
| Churn, duplication, reuse, complexity | SDD та living architecture з code+docs review |
| Зміни без owner, stale docs | Repository intelligence: залежності й owners |
| Діагностика й відновлення без успішного AI | Human recovery drills |

**Що говорити:** «Це сигнали й практики для перевірки. Результат оцінюємо за end-to-end delivery, rework, stability і здатністю відновити систему. Згенерована документація не гарантує розуміння. Граф репозиторію теж має сенс лише тоді, коли допомагає знаходити правильні залежності й рішення».

DORA 2025, p.58: малі порції змін посилюють позитивний зв’язок AI із product performance та зменшують friction; індивідуальні gains можуть бути меншими. P.81: ToC і черги review/testing/integration. Це аргументи для системної оптимізації, а не універсальна гарантія всіх практик у Explore.

**Композиція:** Watch і Explore займають основну площу; новий equilibrium лишається відкритим питанням. Не вводимо нових посад, реєстрів або обов’язкових інструментів.

**Pivot:** «AI змінює не лише те, як ми пишемо software. Він входить у сам software».

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

Повний покажчик перенесено до [EVIDENCE.md](EVIDENCE.md): прямі посилання на первинні звіти, використані версії, місця в джерелах, історичні перевірки й редакторський відбір. Цей розділ зберігається як навігаційна точка; детальні пояснення слайда 4 та арифметика нижче залишаються тут.

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
