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

### Зафіксовані слайди 1–8

За прямим запитом maintainer від 21 вересня 2026 року, після пояснення GitClear на слайді 4, **слайди 1–8 зафіксовано**. Не змінювати їхній зміст, числа, нотатки, геометрію, оформлення або спільні ресурси, що впливають на них, без наступного явного запиту maintainer на відповідні слайди. Поточна робоча область — слайди 9–14.

[frozen-slides.json](frozen-slides.json) зберігає контрольні суми секцій і нормалізованих частин PPTX разом із залежностями. Звичайна збірка/перевірка відхиляє розбіжність; автоматичного «перезаписати baseline» або bypass-прапорця немає. Оновлювати запис можна лише в межах явно замовленої зміни, з повторним оглядом захищених слайдів. Це захист від випадкового редагування, а не незалежне підтвердження особи, яка дозволила зміну.

**Структуру відновлено буквально:** ті самі 14 назв, той самий порядок і та сама драматургія. Слайд 4 залишається спільним evidence slide. Слайди 5–7 — comprehension, відповідальність команди та пошук нового SDLC equilibrium, а не окремі слайди про звіти.

Головна дуга: технологічний зсув → HOW we build → дисбаланс SDLC → WHAT we build → Thinking Systems → requirements, QA, release, production і ролі → engineering rigor переходить у нові місця, а не зникає.

Таймінг: 38 хвилин + 2 хвилини резерву. Повноцінне Q&A — окремо. Англійська — для заголовків і коротких екранних формулювань; українська — для пояснень і виступу.

### Що і як перевірено

Відправна точка — [реєстр evidence/SOURCES.md у Subprime](https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis/blob/main/evidence/SOURCES.md), його бібліографія, звіт та NBER evidence brief. Реєстр не означає, що кожен запис уже пройшов повний аудит: стан Registered відрізняється від Verified. Для чисел нижче пріоритет мають самі автори досліджень.

Для актуальності додано новіші авторські публікації, навіть якщо їх ще немає в реєстрі Subprime: DORA 2025, METR за травень 2026, GitClear за 2026; NBER — вереснева редакція 2026. Xu використано у v3 від 28 січня 2026, Agarwal — у v2 від 27 січня 2026. Нова дата версії не робить старі дані новими: це окремо зазначено.

Перевірка означає звірку таблиць, підписів, одиниць вимірювання, дат, дизайну досліджень і арифметики. Вона не означає незалежне відтворення оцінок на сирих даних. Для NBER повторно завантажено поточний офіційний PDF із вересневою редакцією й візуально звірено Figure 1 та Table 6; старий наданий PDF не використовується для поточних чисел. Для DORA використано повний звіт v.2025.2 із public mirror, авторське резюме та офіційну інфографіку. Для GitClear — публічний виклад і доступний графік; перевірка повного закритого GitClear whitepaper не заявляється.

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
      "25.5×",
      "changed LOC"
    ],
    [
      "3.4×",
      "commits"
    ],
    [
      "1.3×",
      "releases"
    ]
  ],
  "nberGeneration": "Cumulative across three tool generations",
  "nberCaveat": "Fig. 1 rounded; LOC = additions + deletions.\nAsync release effect not estimated.",
  "marketHeadline": "More apps. Usage does not\nkeep pace with new releases.",
  "marketDetail": "Jan 2025 → Apr 2026; first 3 months.",
  "marketNumbers": [
    [
      "iOS: <10 ratings",
      "≈78% → 87%"
    ],
    [
      "Chrome: <10 downloads",
      "19% → 33%"
    ]
  ],
  "takeaway": "Code activity, delivery and user value are different outcomes.",
  "notes": "NBER WP 35275: May 2026, revised September 2026; current official PDF downloaded 2026-09-21. Понад 500 тисяч GitHub developers; matched event study, не RCT. Попередні 17.3× / 2.8×, 79→86% та 18→31% належали старій редакції й замінені. Changed LOC = additions + deletions, не чисте зростання кодової бази.\nTable 6, друкована с.33 / PDF p.35, тижні 21–30: Autocomplete — LOC +234.3%, files +50.0%, commits +30.2%, PRs +18.3%, repos +11.9%, releases +9.0%. Sync — LOC +957.5%, files +265.0%, commits +153.2%, PRs +86.0%, repos +47.3%, releases +19.8%. Async — LOC +1254.9%, files +83.3%, commits +60.7%, PRs +68.5%, repos +19.2%; releases не оцінено окремо. Figure 1, друкована с.2 / PDF p.4: авторські округлені cumulative levels — LOC 25.5×, files 5.0×, commits 3.4×, PRs 2.7×, repos 1.8×, releases 1.3×. Арифметика за округленою Table 6: 1+(234.3+957.5+1254.9)/100=25.467; commits 1+(30.2+153.2+60.7)/100=3.441; releases 1+(9.0+19.8)/100=1.288. Не перемножувати компоненти і не видавати ці суми за точні raw-data estimates. Прочерк async releases не означає нульового ефекту.\nFigure 11, друкована с.44 / PDF p.46; §7.2, с.43–46: iOS нові apps/month приблизно 33–45 тисяч у 2023–early 2025 → 108 тисяч у квітні 2026; Android 42 тисячі у січні 2025 → 99 тисяч у mid-2026; Chrome приблизно семикратне зростання від 2023, що почалося до agentic era. SourceForge показує невелике зростання new projects і винесений у Figure OA-17, без надійної usage-панелі. Usage за перші 3 місяці: iOS cohort ratings приблизно стабільні; Android downloads помірно зростають, але значно повільніше за entry; Chrome downloads падають. Тому коректно «usage does not keep pace», а не «usage ніде не зростає».\n§7.2.3, друкована с.46 / PDF p.48: January 2025 → April 2026, частка iOS із <10 ratings приблизно 78% → 87%; Chrome із <10 downloads 19% → 33%; Android із ≤100 downloads приблизно 22% → 26%. Авторські цілі відсотки; не точні частки з raw data. Це порівняння нових когорт за перші 3 місяці, не всіх existing apps, не весь software market і не пряме вимірювання consumer welfare. Зміни часток приблизно +9/+14/+4 відсоткових пункти відповідно.\nDORA 2025 v.2025.2: повний звіт отримано через публічне дзеркало; source URL, license і SHA-256 записано в evidence/sources.json. Figure 28, p.38: software delivery instability має standardized estimate приблизно +0.10 SD, 89% credible interval приблизно +0.07…+0.13, на +1 SD AI adoption. Це округлене зчитування графіка, не точна опублікована числова таблиця. Векторні координати та арифметика — evidence/dora-2025-figure28.json. Footnote 23, p.48 визначає стандартизацію. Appendix p.139: instability об’єднує change failure rate та deployment rework rate, тобто частку незапланованих deployments для виправлення user-facing bugs. Це оцінки респондентів у cross-sectional survey, не телеметрія CI/CD і не доведений причинний ефект. Не перекладати +0.10 SD як +10% failures. >80% і 59% — частки респондентів, які повідомляють про покращення productivity та code quality. Перевірений коефіцієнт 2024 +7.2% тут не підставляємо. Деталі: evidence/dora-2025.md.\nMETR, 11 травня 2026: 349 technical workers; 1.4–2× medians across 3 self-reported work-value questions; це не credible/confidence interval, 3× self-reported speed; є selection bias. Старий RCT 2025 із +19% часу — лише історичний контекст.\nGitClear 2026: частка moved code у changed lines 13% (2023) → 3.8% (YTD 2026), не кількість refactoring tasks і не весь reuse. Частота duplicated blocks приблизно +81% за цей період. Copy/paste share 9.4% (2022) → 15.7% (H1 2026), інший baseline. Публічне резюме GitClear 2026 прямо повідомляє +15% two-week code churn: частка нещодавно написаних рядків, переписаних/видалених упродовж двох тижнів. Це відносна зміна, не +15 відсоткових пунктів і не частка дефектів. Резюме не дає окремої пари базових значень churn. Function connectivity: 343 → 223 calls/1000 changed lines, 2023 → YTD 2026, приблизно −35%. Це щільність викликів, не весь reuse. Legacy update share: 1.7% → 0.46%; вступ каже 2022, детальний абзац 2023, тому baseline суперечливий і показник лишається в нотатках. Не змішувати churn, duplication та refactoring. Текст і графік 2026 суперечать щодо абсолютної одиниці duplication, тому залишаємо тільки відносні +81%. Це observational proxies, не причинний ефект AI. Деталі: evidence/gitclear.md.\nXu, v3 від січня 2026, дані 2020–22: top activity quartile — commits −19%, reviews +6.5%; bottom quartile — commits +43.5%, PRs +17.7%; rework +2.4%. Це не кадрові грейди й не агенти 2026 року.\nAgarwal, v2, Table 2: complexity Agent-first +34.85% / IDE-first +42.87%, warnings +17.73/+19.00%; зміна IDE-first warnings статистично незначуща. Не трактувати це як борг на одну фічу.\nDORA: позитивний зв’язок AI adoption з throughput одночасно з негативним зі stability. Small batches, p.58: сильніший позитивний зв’язок AI із product performance та менше friction, хоча індивідуальні gains можуть бути меншими. ToC / review-testing-integration queues, p.81. Це мотивує системну оптимізацію на слайді 7, не доводить універсальну причинність.\nПовторна числова перевірка 2026-09-21: DORA Fig.28 vector coordinates та сторінку звірено повторно; коефіцієнт і межі лише приблизні. >80% збережено як авторський поріг: сума округлених bars 41+31+13=85 не встановлює точного агрегату. GitClear calls 343→223 дають приблизно −35%; +81% — авторське округлення, +15% churn — число з резюме без окремої baseline-пари. Точний місяць публікації GitClear не підтверджено на перевіреній сторінці, тому на екрані лише 2026. Див. EVIDENCE.md та відповідні локальні нотатки.\nПояснення GitClear: Moved-code share — частка змінених рядків, класифікованих як переміщений наявний код. 3.8−13=−9.2 відсоткового пункту; (3.8/13−1)×100=−70.769…%, на екрані −70.8%. Це proxy активності рефакторингу: менша частка переміщень може означати менше реорганізації та повторного використання коду, але не кожне переміщення корисне і не весь рефакторинг є переміщенням. Calls / 1k changed lines — кількість викликів інших методів або функцій у новому коді на 1000 змінених рядків, не API throughput. 223−343=−120; (223/343−1)×100=−34.9854…%, приблизно −35%. GitClear трактує вищу щільність як більшу зв’язність нового й наявного коду. Менша може означати слабше reuse, але менша зв’язність іноді бажана; перевіряти дизайн і дублювання. Падіння цих двох proxy — привід перевірити підтримуваність, не автоматичний висновок про погану якість чи причинність AI. *Період 2023→YTD 2026 стосується moved/calls/duplication; для reported churn +15% окремої базової пари немає.",
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
    "https://dora.dev/research/2025/questions/",
    "https://www.gitclear.com/industry_stats/ai_code_quality_signal_graphs"
  ],
  "gitclearMetrics": [
    [
      "Moved-code share",
      "13% → 3.8%"
    ],
    [
      "Calls / 1k changed lines",
      "343 → 223"
    ],
    [
      "Duplicated blocks",
      "≈+81%"
    ],
    [
      "Two-week churn (reported)",
      "+15%"
    ]
  ],
  "gitclearCaveat": "Less restructuring / reuse? Signals, not a quality verdict.",
  "otherCards": [
    [
      "METR · MAY 2026",
      "1.4–2× work value",
      "Medians across 3 questions; self-reported, not causal."
    ],
    [
      "AGARWAL · JAN 2026",
      "+34.85% / +42.87%",
      "Complexity: Agent-first / IDE-first. Xu: workload shifts."
    ]
  ],
  "doraInstability": "≈ +0.10 SD",
  "doraInterval": "89% credible interval ≈ +0.07 to +0.13",
  "doraMeasures": "Survey model, rounded reading of Fig. 28.\nSD = standard deviation, not a failure percentage.",
  "doraPerceptions": "Respondents reporting improvement: >80% productivity; 59% quality.",
  "doraHeadline": "Higher throughput\nLower delivery stability",
  "nberSource": "NBER · SEP 2026 REVISION",
  "gitclearSource": "GITCLEAR · 2023 → 2026 YTD*",
  "gitclearDetails": [
    "Moved / changed lines: −9.2 pp (−70.8%). Refactoring proxy.",
    "Other-function calls: −120 (≈−35%). Connectivity proxy."
  ],
  "gitclearSecondary": "Duplicated blocks ≈+81%   ·   Two-week churn +15%*"
}
```

**Час:** 4:30.

**Роль:** показати різні рівні вимірювання — активність розробника, delivery, підтримуваність, командну роботу та використання продукту. Це один слайд, не новий act із шести слайдів.

### Що саме має бути на екрані

Дві колонки з чіткою вертикальною межею. Зліва — NBER та marketplace outcomes. Справа — одночасний позитивний зв’язок AI із throughput і негативний зі stability у DORA; приблизний standardized coefficient є підписом. Нижче — чотири окремі метрики GitClear. Унизу спільний ряд METR та Xu / Agarwal. Жодних стрілок між несумірними дослідженнями або outcomes; усі числа мають власні підписи. Докладні таблиці залишаються у нотатках.

**Велика картка NBER — September 2026 revision:**
- **25.5× changed LOC**, **3.4× commits**, **1.3× releases** — округлені значення авторів із Figure 1.
- Видимий ряд: **Cumulative across three tool generations**.
- Примітка: **Fig. 1 rounded; LOC = additions + deletions. Async release effect not estimated.**
- Marketplace headline: **More apps. Usage does not keep pace with new releases.**
- **iOS: <10 ratings ≈78% → 87%; Chrome: <10 downloads 19% → 33%.**
- Період порівняння когорт: **Jan 2025 → Apr 2026; first 3 months.**

**METR — May 2026:** **1.4–2× work value**. Це медіани відповідей на три питання, self-report, не causal uplift і не інтервал невизначеності.

**DORA — 2025:** **Higher throughput / Lower delivery stability** при вищому AI adoption. Підпис: **≈ +0.10 SD delivery instability per +1 SD AI adoption**, **89% credible interval ≈ +0.07 to +0.13**. Повторно звірене округлене зчитування Figure 28, p.38, а не точний опублікований коефіцієнт. Survey model, не CI/CD telemetry. Instability = change failures + unplanned bug-fix deployments. Окремо: **>80% productivity; 59% quality** — частки респондентів, які повідомляють про покращення.

**GitClear — 2026 public summary:** **Moved-code share: 13% → 3.8%**, **Calls / 1k changed lines: 343 → 223**, **Duplicated blocks: ≈+81%**, **Two-week churn (reported): +15%**. Moved lines, calls і duplication порівнюють 2023 із YTD 2026; окремої baseline-пари churn немає. Показники observational. Місяць публікації не приписуємо без підтвердження.

**Пояснення GitClear на екрані:** moved / changed lines −9,2 в.п. (−70,8%) — proxy рефакторингу; other-function calls −120 (≈−35%) — proxy зв’язності. Перша частка говорить про переміщення наявного коду, друга — про виклики інших функцій/методів у новому коді на 1 000 змінених рядків. Менші значення можуть сигналізувати менше реорганізації/reuse, але не є автоматичним вердиктом якості: не кожне переміщення корисне й надмірна зв’язність також небажана. На екрані: **Less restructuring / reuse? Signals, not a quality verdict.** Зірочка біля GitClear відсилає до невідомої окремої baseline-пари churn у нотатках.

**Agarwal — January 2026, v2:** **+34.85% / +42.87%**, cognitive complexity для **Agent-first / IDE-first** відповідно, Table 2. Xu лишається окремим якісним сигналом про workload shifts; ці відсотки належать тільки Agarwal.

Унизу слайда: **Code activity, delivery and user value are different outcomes.**

### NBER: повні перевірені цифри для нотаток

Джерело: Demirer, Musolff & Yang, [Writing Code vs. Shipping Code, NBER WP 35275](https://www.nber.org/papers/w35275). May 2026, **revised September 2026**, офіційний PDF отримано 21 вересня 2026. Понад **500 тисяч** GitHub developers, AI telemetry та matched event-study design; не RCT. Попередня редакція зі старими 17,3× / 2,8× більше не є основою слайда. [Версія та SHA-256](evidence/nber-35275.md).

**Table 6, друкована с.33 / PDF p.35.** Тижні **21–30** після adoption; нормалізація на середнє до adoption, **1% winsorization**. Це компоненти, а не три кумулятивні підсумки.

| Компонент | Changed LOC | Distinct files | Commits | Created PRs | Distinct repos | Releases |
|---|---:|---:|---:|---:|---:|---:|
| Autocomplete | +234,3% | +50,0% | +30,2% | +18,3% | +11,9% | +9,0% |
| Synchronous agents | +957,5% | +265,0% | +153,2% | +86,0% | +47,3% | +19,8% |
| Asynchronous agents | +1254,9% | +83,3% | +60,7% | +68,5% | +19,2% | Не оцінено окремо |

**Покоління:** autocomplete доповнює код; synchronous agent працює з розробником інтерактивно; asynchronous agent автономніше виконує делеговану задачу до завершення.

**Figure 1, друкована с.2 / PDF p.4:** cumulative levels **25,5× LOC; 5,0× files; 3,4× commits; 2,7× PRs; 1,8× repos; 1,3× releases**. Це авторські округлення. Суми за надрукованою Table 6: LOC 1 + (234,3 + 957,5 + 1254,9)/100 = 25,467×; commits 1 + (30,2 + 153,2 + 60,7)/100 = 3,441×; releases 1 + (9,0 + 19,8)/100 = 1,288×. Додаткові десяткові знаки цих сум не означають точніших raw-data estimates. Компоненти не перемножуються. Async releases не можна відділити від human-authored components; прочерк не доводить нульового ефекту.

**Changed LOC = additions + deletions**, не лише нові рядки й не чисте зростання кодової бази. Це не вимір бізнес-цінності.

### NBER: маркетплейси та кінцевий користувач

**Figure 11, друкована с.44 / PDF p.46; §7.2.2–7.2.3, друковані с.45–46 / PDF pp.47–48.**

| Майданчик | Нові публікації: приблизні рівні з тексту авторів | Usage нових когорт за перші 3 місяці |
|---|---|---|
| Apple App Store | 33–45 тис./місяць у 2023–early 2025 → близько 108 тис. у квітні 2026 | Cohort ratings приблизно стабільні між 2024 і 2025 |
| Google Play | Близько 42 тис. у січні 2025 → 99 тис./місяць до mid-2026 | Downloads зростають помірно, значно повільніше за кількість нових apps |
| Chrome Web Store | Приблизно семикратне зростання від 2023; прискорення почалося до agentic era | Cohort downloads падають; спад передував agentic era |
| SourceForge | Невелике зростання нових projects; Appendix Figure OA-17 | Download counts замалі для змістовної usage-панелі |

**January 2025 → April 2026**, частки нових когорт за перші три місяці:
- iOS, **<10 ratings: приблизно 78% → 87%** (≈+9 відсоткових пунктів).
- Chrome, **<10 downloads: 19% → 33%** (+14 пунктів за надрукованими округленнями).
- Android, **≤100 downloads: приблизно 22% → 26%** (≈+4 пункти).

Автори друкують цілі відсотки; не приписуємо їм невідомих десяткових часток. Це порівняння когорт, не всіх застосунків у магазині. Ratings/downloads — proxies, не прямі welfare, revenue чи time-spent measures.

**Як сказати усно:** «Нових застосунків більше, але використання не встигає за їхньою кількістю. На iOS воно приблизно стабільне, на Android помірно зростає, у Chrome падає. Частка нових застосунків, які не досягли навіть невеликої аудиторії, збільшується».

**Межа висновку:** не казати «використання ніде не зросло» або «користі немає». Часовий збіг не доводить AI як єдину причину; коротке вікно не виключає пізніших вигод.

### Інші картки: числа й межі

**DORA 2025.** [Офіційна інфографіка](evidence/originals/dora-2025-infographic.pdf) також містить **59%**, які повідомляють про покращення code quality. Це self-report, не зміна якості на 59%. Delivery stability — окремий outcome; говорити «якість коду впала» за цією association некоректно. Повний v.2025.2, Figure 28, p.38 тепер перевірено: приблизно +0.10 SD instability на +1 SD AI adoption, 89% credible interval приблизно +0.07…+0.13. Це зчитування графіка з округленням, не +10% failures, не telemetry й не causal estimate. Визначення та розрахунок див. у локальній нотатці. [Детальний запис](evidence/dora-2025.md). Майже 5 000 респондентів; 90% використовують AI, понад 80% повідомляють про вищу продуктивність, 30% мало або зовсім не довіряють AI-коду. Зв'язок adoption із throughput і product performance позитивний, зі stability — негативний. Це не причинні коефіцієнти. Числа DORA 2024 сюди не переносимо. [Офіційне авторське резюме DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report).

**METR, 11 травня 2026.** 349 technical workers; median self-reported work-value multiplier 1,4–2× залежно від формулювання питання, self-reported speed — 3×. Це не confidence interval і не об'єктивне вимірювання delivery. Вибірка самообрана. [METR survey](https://metr.org/blog/2026-05-11-ai-usage-survey/).

Історичний контрольований результат METR 2025: 16 розробників, 246 задач, +19% часу з early-2025 AI. Залишити як датований контекст, не актуальний вирок сучасним агентам. [METR RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). У [лютневому оновленні 2026](https://metr.org/blog/2026-02-24-uplift-update/) самі автори вказують на selection bias; не виводити з нього надійний універсальний поточний відсоток.

**GitClear, публічне резюме 2026.** Moved-code share — частка переміщених рядків серед changed lines: proxy reuse/refactoring, а не кількість refactoring tasks. Two-week churn **+15%** прямо наведено в публічному резюме 2026; це окрема від duplication метрика. Function calls **343 → 223 на 1000 changed lines**, приблизно **−35%**, 2023 → YTD 2026. На екрані calls наведено як 343 → 223, без додаткового округлення до −35%. [Визначення, періоди й межі](evidence/gitclear.md). Moved/refactoring-related share: 13% у 2023 → 3,8% YTD 2026; function-call density −35%; block duplication приблизно +81%; two-week churn +15%. Це спостережні показники власної класифікації, не весь reuse і не встановлений причинний ефект AI. У тексті й графіку duplication є суперечність одиниць; тому абсолютні 40,3 і 73,0 не використовуємо як навантажену метрику. Відносна зміна узгоджується. [GitClear 2026](https://www.gitclear.com/the_ai_code_quality_maintainability_gap).

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
  "role": "PRODUCT MANAGER + BA · agree what acceptable behavior means",
  "oldHeading": "SPECIFIED FLOW · STILL REQUIRED",
  "old": [
    "Button A",
    "Window B"
  ],
  "oldDetail": "Exact states, permissions\nand transitions.",
  "roleDetail": "Product + BA: examples and rubric.\nProject Manager: stakeholder decisions.",
  "newHeading": "VARIABLE BEHAVIOR · ALSO REQUIRED",
  "boundaries": [
    [
      "ALLOW",
      "Explain an approved support article."
    ],
    [
      "CLARIFY",
      "Missing context? Ask before advising."
    ],
    [
      "PROHIBIT",
      "Invent steps, expose data, bypass approval."
    ]
  ],
  "gap": "Shared quality vocabulary exists. Product-specific semantic limits still need agreement.",
  "research": "Starting points: ISO/IEC 25059 · NIST AI RMF · CheckList (ACL 2020)",
  "takeaway": "Business scenarios → examples + counterexamples → acceptance rules",
  "notes": "Наскрізний приклад: внутрішній IT-асистент. Зліва — точний перехід Button A → Window B, permissions та інваріанти, які залишаються вимогами. Справа — додаткові вимоги до варіативної поведінки. Дозволено пояснити затверджену статтю підтримки різними словами, зберігаючи зміст і необхідні кроки. За відсутності контексту потрібно уточнити або ескалувати. Не можна вигадувати операційні кроки, розкривати чужі дані або виконувати дію в обхід approval. Одна картинка з областю сама не задає точного вимірюваного контракту.\nМовний розрив: природна мова неоднозначна; prompt не є точним описом усіх можливих відповідей. Теза «стандартів немає» надто категорична: ISO/IEC 25059:2023 надає quality model і узгоджену термінологію, NIST AI RMF — контекстне управління ризиком, GenAI Profile — спільне з domain experts документування допустимого використання. Вони не підставляють готові семантичні межі й прийнятність наслідків для нашого продукту. Не стверджуємо доведеної відсутності будь-якої формальної мови.\nПрактична пропозиція доповіді: Product Manager та BA разом із бізнесом збирають сценарії, приклади, контрприклади, клас наслідків і потрібну реакцію; фіксують rubric, джерело правила й того, хто його погоджує. CheckList (Ribeiro et al., ACL 2020) пропонує capability × test-type підхід до поведінкових перевірок NLP. Це допомога у формулюванні перевірок, не універсальний стандарт semantic acceptance. Project Manager планує доступ до stakeholders, рішення та залежності; не вигадує толерантність за бізнес.\nВимога ширша за Operating Envelope; точні інтерфейси, заборони й інваріанти зберігаються. BA/Product не зобов’язані самі вивести статистичний поріг: це спільна робота з бізнесом, QA, розробниками й власником ризику. Ролі описують відповідальність, не новий headcount.",
  "sources": [
    "https://www.iso.org/standard/80655.html",
    "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf",
    "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf",
    "https://aclanthology.org/2020.acl-main.442/",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/requirements-correctness-and-bugs.md"
  ]
}
```

**Час:** 3:00.

**Композиція:** дві явно розділені колонки. Ліворуч окремі native boxes Button A → Window B без переносу назви чи стрілки; праворуч три конкретні режими ALLOW / CLARIFY / PROHIBIT. Нижче — мовний розрив та перевірені starting points.

**Рольова зміна:** Product Manager + BA переводять бізнес-сценарії в приклади, контрприклади та rubric; Project Manager забезпечує своєчасні рішення stakeholders. ISO/IEC 25059 і NIST існують, але не вирішують за команду межі конкретного продукту. Research proposal: CheckList як метод структурування behavioral tests. [Джерела й межі](EVIDENCE.md#вимоги-оцінювання-та-ролі--слайди-914).

**Перехід:** «Домовитися, що прийнятно, ще недостатньо. Як виміряти, наскільки часто система дотримується цієї домовленості?»

## 10. One Green Test Proves Almost Nothing

```pptx-slide
{
  "number": 10,
  "layout": "evaluation",
  "role": "QA + DEVELOPERS · estimate behavior, uncertainty and consequences",
  "frequency": "HOW OFTEN?",
  "observed": "4 / 200 = 2%",
  "interval": "95% Wilson interval ≈ 0.8%–5.0%",
  "rateLabel": "Observed unacceptable outputs",
  "severity": "HOW HARMFUL?",
  "harms": [
    "3 incorrect instructions → rework",
    "1 privacy leak → critical breach"
  ],
  "decision": "Critical breach → BLOCK RELEASE",
  "sample": "Illustrative independent sample; 196 / 200 acceptable. No production guarantee.",
  "businessQuestion": "Ask the business: “How much rework is tolerable? Which harm must be prevented?”",
  "responsibilities": [
    [
      "PRODUCT + BA",
      "Elicit impact; agree acceptance"
    ],
    [
      "QA + DEVELOPERS",
      "Sample, calibrate, compare versions"
    ],
    [
      "RISK / RELEASE OWNER",
      "Decide acceptability for this scope"
    ]
  ],
  "takeaway": "Statistics estimate frequency. Business authority decides acceptable consequences.",
  "notes": "Статистичне оцінювання доповнює unit, integration, security та deterministic tests. Потрібно окремо оцінити: а) частоту виходу за погоджені межі; б) силу/тяжкість наслідку. «Сила відхилення» не має універсальної числової шкали: для latency це мілісекунди понад межу, для грошей — збиток, для semantic output — погоджена rubric і класи наслідків. Середній score або embedding distance сам по собі не встановлює business harm. Хвости й критичні групи оцінюємо окремо, а не приховуємо добрим агрегатом.\nНавчальний приклад, не реальні дані і не рекомендований sample size: 200 незалежних репрезентативно відібраних evaluation units із одного стабільного цільового розподілу; 196 прийнятних, 4 неприйнятні. Серед чотирьох: 3 неправильні інструкції та 1 витік даних. 4/200=2%; 196/200=98%. Двосторонній 95% Wilson score interval для частки неприйнятних: [0.780443%, 5.028709%], на слайді ≈0.8%–5.0%. Метод і формула — NIST Engineering Statistics Handbook §7.2.4.1. Інтервал відображає sampling uncertainty за припущень; не дає 95% ймовірності, що конкретний майбутній результат безпечний, і не гарантує поведінки після зміни контексту. Не можна рахувати повтори того самого кейсу як незалежні representative cases. Розмір вибірки, dependence, subgroup coverage, множинні порівняння, невизначеність оцінювача й baseline планують під рішення.\nУ прикладі витік порушує обов’язкову вимогу, тому release блокується незалежно від 98% aggregate acceptance. Відсутність витоків у тесті також не доводила б неможливості витоку: потрібні permissions, isolation, gate та перевірка припущень їх роботи.\nЗвідки взяти tolerance? QA не винаходить його. Product Manager та BA обговорюють із бізнесом зрозумілі сценарії: скільки ручного виправлення витримає support; кому і яку шкоду завдасть помилка; що треба технічно унеможливити; коли прийнятні уточнення або ручний шлях. Технічна команда перетворює це на measurement plan, оцінку частот, severity, confidence та тригери. Уповноважений власник ризику/релізу погоджує допустимість у конкретному scope. Project Manager організовує ці рішення до обіцянки релізу.\nModel drift пояснюємо бізнесу як зміну спостережуваних результатів/навантаження/наслідків за нової версії чи контексту, а не вимагаємо від stakeholders знання статистичних термінів. QA підтримує golden/reference sets, coverage, calibration із domain experts і перевірки підгруп. Developers роблять versioning, instrumentation, відтворювані evaluation runs і regression comparison. Пороги та rubric версіонуються; evidence для release перевіряється окремо від набору, на якому їх підбирали.",
  "sources": [
    "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf",
    "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf",
    "https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm",
    "https://aclanthology.org/2020.acl-main.442/",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/01-patterns/thinking-system-review.md"
  ]
}
```

**Час:** 3:00.

**Композиція:** ліворуч частота та interval plot; праворуч тяжкість наслідків. 4 / 200 = 2%, Wilson 95% CI ≈0,8%–5,0%; 196 / 200 прийнятних. Це навчальна незалежна вибірка, не production guarantee. Три неправильні інструкції й один privacy breach; останній блокує реліз за обов’язковою вимогою.

**Рольова зміна:** QA + Developers будують sample/evaluation plan, calibration, subgroup coverage, version comparisons та instrumentation. Product + BA отримують tolerance через зрозумілі бізнесу наслідки; risk/release owner погоджує acceptability. Статистика не вибирає business tolerance. Severity може бути сумою збитку, часом або категорією наслідку; універсального semantic distance немає.

**Перехід:** «Ці докази й домовленості повинні бути частиною Ready, Done та окремого рішення про release».

## 11. DoR / DoD Become Risk Contracts

```pptx-slide
{
  "number": 11,
  "layout": "risk",
  "role": "DEVELOPERS · deliver a reproducible evidence and recovery package",
  "table": [
    [
      "GATE",
      "CONCRETE EVIDENCE",
      "DECISION / OWNER"
    ],
    [
      "READY",
      "Scope, rubric, evaluation plan\nFallback owner + dependencies",
      "Product + BA agree criteria\nProject Manager clears blockers"
    ],
    [
      "DONE",
      "Versioned model / prompt / data\nTests, evals, rollback rehearsal",
      "Developer + QA verify the build\nDone does not authorize release"
    ],
    [
      "RELEASE",
      "Population + tool permissions\nResidual risk + stop triggers",
      "Authorized owner accepts scope\nOr narrows, defers, rejects"
    ]
  ],
  "caption": "IT assistant: approved sources → traceable build → restricted rollout + manual fallback.",
  "takeaway": "“Done” is an evidence package. Release is a separate, scoped decision.",
  "notes": "Конкретизуємо абстрактні risk contracts через deliverables розробників для того самого IT-асистента. READY: визначено аудиторію, дозволені джерела, заборонені дії, приклади/rubric, evaluation plan, критичні залежності й власника ручного шляху. Якщо tolerance або feasibility ще невідомі, команда може бути Ready до обмеженого експерименту з питанням, бюджетом, stop condition та owner; це не дозвіл на production.\nDONE: developer поставляє відтворювану конфігурацію model version, prompt, retrieval/data snapshot, tool schema, policy та permissions; результати deterministic, behavioral і control-path tests; посилання на evaluation evidence, coverage й обмеження. Перевірені deny-path, unavailable-control behavior, telemetry та фактичний rollback/manual fallback. QA звіряє evaluation method і results, а не одноосібно приймає business risk. Для слайда скорочено до model/prompt/data; повний список тут.\nRELEASE: ідентифіковано саме цю версію, population, tool authority, exposure, monitoring, stop triggers, оперативного owner та fallback capacity. Уповноважена особа приймає залишковий ризик у межах повноважень або звужує scope, відкладає чи відхиляє реліз. Прийняття ризику не скасовує обов’язкову заборону й не розширює успадковану project authority. Попередній toy-example із privacy breach не пройде цей gate.\nРозробник тепер здає не лише endpoint, а відтворювану поведінку, evidence і працездатний recovery path. Project Manager відстежує незакриті залежності/рішення та не прирівнює Done до Ship. Ролі можуть поєднуватись однією людиною; достатньо існуючого review artifact, новий комітет не потрібний.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/01-patterns/thinking-system-review.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/nested-control-lifecycle.md"
  ]
}
```

**Час:** 3:00.

**Композиція:** native PowerPoint table GATE / CONCRETE EVIDENCE / DECISION–OWNER. Замість загальних гасел — scope/rubric, versioned configuration, тести, evals, rollback rehearsal, population, permissions і stop triggers.

**Рольова зміна:** Developer здає відтворювану capability разом із evidence та recovery path. QA перевіряє докази, Product + BA — acceptance, Project Manager — залежності/рішення. Done не дозволяє production автоматично. Ready до bounded experiment також не є production authorization. Release належить уповноваженому owner у межах успадкованих constraints.

**Перехід:** «Після релізу та сама відповідальність має технічний шлях дії».

## 12. Production Needs a Control Loop

```pptx-slide
{
  "number": 12,
  "layout": "control",
  "role": "ARCHITECT · make boundaries and corrective actions operational",
  "steps": [
    "Approved context",
    "Model proposal",
    "Permission gate",
    "Support tool"
  ],
  "gate": "Allowlist + required approval; deny when the gate is unavailable.",
  "reference": "Approved limits",
  "loop": [
    "Observe",
    "Compare / authorize",
    "Apply correction"
  ],
  "actions": "Rollback / disable tool / manual fallback · inside delegated authority",
  "caption": "Observe outcomes + gate health. Verify that the corrective action took effect.",
  "takeaway": "A dashboard sees a problem. An authorized control path can change operation.",
  "notes": "Наскрізний IT-асистент: approved context → model proposal → deterministic permission/approval gate → support tool. Модель пропонує дію; тільки gate дозволяє виконання в межах allowlist, user permissions і required approval. Приклад передбачає відсутність обхідного шляху; за недоступного gate дію відхиляють і пропонують ручний шлях. Схема показує конкретний tool-action path, не універсальну топологію всіх Thinking Systems і не гарантію семантичної коректності довільного тексту. User-facing answer path потребує власних scoped controls.\nНижній цикл: Observe збирає outcomes, incidents, затримку, fallback load, стан gate, bypass attempts, execution/effects корекцій. Compare/authorize зіставляє їх із явно показаними Approved operating limits; відповідальний Controller або людина вирішує, що дозволено змінити. Apply correction виконує rollback/disable/manual fallback у межах delegated authority. Зворотний зв’язок показує зміну operation; технічно correction може діяти на routing, tool access, model/configuration або реалізацію gate. Наступне спостереження підтверджує, чи action справді виконано й мало потрібний ефект.\nArchitect визначає enforced boundary, permissions, isolation, telemetry, decision rights, ефективні actuators, час реакції та fallback capacity. Prompt або probabilistic semantic detector сам собою не є Hard Constraint. Прямий deterministic gate може давати scoped hard claim тільки з перевіреним complete path та явними припущеннями. Developers реалізують і тестують paths; QA перевіряє bypass, degradation, false blocks і recovery; operational owner має повноваження та runbook.\nProject Manager планує operational ownership, rehearsal і залежності, а не закриває проект після deploy. Зміна в межах delivery authority допускає локальну корекцію; розширення tool authority, population чи invalidated business/control assumptions повертається до project reauthorization. Автоматичне відхилення/rollback не повинно непомітно розширювати повноваження.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/control-loop-anatomy.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/nested-control-lifecycle.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/01-patterns/thinking-system-review.md"
  ]
}
```

**Час:** 3:00.

**Композиція:** зверху конкретний IT-assistant tool path, унизу замкнений Observe → Compare/authorize → Apply correction → operation; approved operating limits явно надходять до decision function. Показано permission gate перед tool execution, а не магічний post-hoc filter.

**Рольова зміна:** Architect визначає boundary, complete enforcement path, assumptions, sensing, authority та effective correction. Developers реалізують, QA перевіряє degradation/bypass/recovery, operational owner діє; Project Manager планує ownership і capacity. Це scoped example, а не універсальний deployment diagram або гарантія всіх semantic outputs.

**Перехід:** «Такий продукт потребує іншого наповнення командного процесу, а не лише нового компонента в архітектурі».

## 13. The Roles Move With the System

```pptx-slide
{
  "number": 13,
  "layout": "roles",
  "role": "PROJECT MANAGER · manage the learning loop as well as delivery",
  "steps": [
    "Hypothesis",
    "Bounded trial",
    "Evidence",
    "Decision"
  ],
  "cycle": "Adapt or stop; production evidence feeds the next iteration.",
  "table": [
    [
      "CHECKPOINT",
      "PROJECT MANAGER’S WORK",
      "VISIBLE RESULT"
    ],
    [
      "Planning",
      "Sequence evidence gaps + dependencies",
      "Trial budget, owner, stop condition"
    ],
    [
      "Sprint review",
      "Bring Product, BA, QA, Dev, Architect together",
      "Accept, adjust, narrow or stop"
    ],
    [
      "Release + operate",
      "Track authorization + response capacity",
      "Scoped rollout; trigger to reopen"
    ]
  ],
  "takeaway": "Progress = working capability + reduced uncertainty + explicit decisions.",
  "notes": "Стара презентація Designing Non-Deterministic Systems, slide 20 Welcome to the Laboratory, дає педагогічну метафору Hypothesize → Measure → Adapt. Тут не стверджуємо, що Scrum або попередня інженерія не були емпіричними. Процес додає явно керований цикл поведінкових гіпотез, measurement та адаптації поряд зі звичайним delivery. Titles/order цієї 14-slide доповіді збережено.\nProject Manager відрізняється від Product Manager. Product разом із BA та бізнесом уточнює цінність, наслідки й acceptance; Project Manager організовує delivery і навчання: stakeholder availability, dependencies, доступ до даних/domain experts, evaluation cost, час на аналіз і remediation, decision latency, release/operations readiness. Він не стає одноосібним власником risk acceptance.\nPlanning: backlog містить не тільки features, а й перевірювані невідомі, наприклад «чи достатньо approved knowledge для типових support cases?». Для trial фіксуємо питання, hypothesis, evidence plan, ресурсну межу, owner і stop condition; якщо треба — погоджений обмежений scope до остаточних tolerance. Sprint review: разом зі working software показуємо versioned evidence, проблемні групи, consequences, uncertainty та unresolved decisions. Результат може бути accept, redesign, narrow, bounded further trial або stop. Це корисний результат роботи, а не автоматична невдача спринту, якщо доказано, що задум нежиттєздатний.\nRelease/operate: окремо від Done підтверджуємо authorization конкретного rollout, monitoring, on-call/ручний шлях і їхню місткість; runtime evidence повертає backlog і за потреби project reauthorization. Не рахувати кількість проведених експериментів як цінність саму по собі: прогрес — робоча capability, зменшення матеріальної невизначеності та прийняте рішення. Один живий review artifact і звичні командні події можуть містити ці записи; не потрібні нові ролі або комітет.\nРозподіл 9–13: Product + BA формулюють acceptance; QA + Developers роблять measurement; Developers доставляють evidence/recovery package; Architect замикає bounded control; Project Manager координує весь цикл, рішення, бюджет і залежності.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/01-patterns/thinking-system-review.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/nested-control-lifecycle.md"
  ]
}
```

**Час:** 2:00.

**Композиція:** Hypothesis → Bounded trial → Evidence → Decision, під ним native table з planning, sprint review та release/operations.

**Project Manager:** координує learning loop поряд із delivery: evidence gaps, stakeholders, dependencies, experiment cost/time, decision latency та operational capacity. Product Manager відповідає за продуктову сторону домовленості, це інша функція. Working capability + reduced uncertainty + explicit decisions — видимий прогрес. Відкрите питання має owner і наступну дію.

**Зв’язок зі старою презентацією:** надана Designing Non-Deterministic Systems, slides 17–20, особливо Welcome to the Laboratory. Зберігаємо емпіричний цикл, уточнюємо старі метафори: Scrum вже емпіричний, ризик не належить автоматично лише PM, один aggregate score не доводить safety. Новий headcount або новий комітет не потрібні.

**Перехід:** «Ролі й процес повертають нас до двох змін із першого слайда».

## 14. Engineering Rigor Moves — It Doesn’t Disappear

```pptx-slide
{
  "number": 14,
  "layout": "synthesis",
  "columns": [
    [
      "HOW WE BUILD",
      "Protect delivery",
      [
        "Team: comprehension + ownership",
        "Project Manager: evidence + flow",
        "Small batches, bounded experiments",
        "Review decisions, not just demos"
      ]
    ],
    [
      "WHAT WE BUILD",
      "Govern behavior",
      [
        "Product + BA: agreed acceptance",
        "QA + Dev: calibrated evidence",
        "Architect: effective control paths",
        "Release owner: scope + residual risk"
      ]
    ]
  ],
  "cycle": "Team process: hypothesize → measure → decide → adapt",
  "takeaway": "The team remains accountable for the whole system.",
  "closing": "More capability still requires engineering responsibility.",
  "titleLines": [
    "Engineering Rigor Moves —",
    "It Doesn’t Disappear"
  ],
  "notes": "Повертаємо HOW і WHAT із першого слайда, тепер із конкретними ролями й процесом. HOW: швидше створювати код недостатньо — команда зберігає comprehension та ownership, Project Manager організовує flow, evidence, залежності та рішення. Малими партіями й обмеженими експериментами перевіряємо невідомі. WHAT: Product + BA узгоджують acceptance з бізнесом; QA + Developers створюють калібровані докази й реалізацію; Architect проектує ефективні control paths; уповноважений release owner приймає scope і residual risk у своїх межах. Це розширення, а не вичерпні нові job descriptions або передача відповідальності одній ролі.\nГоловна зміна процесу: hypothesize → measure → decide → adapt, з робочим software, явними business outcomes і runtime feedback. Детерміновані requirements, tests та delivery discipline залишаються; додається контроль варіативної поведінки і наслідків. Немає нових чисел, нової архітектурної нормативності чи реклами UA.\nФінал: «AI розширює наші можливості. Команда все одно відповідає за систему цілком: як ми її будуємо, яку поведінку дозволяємо, на яких доказах випускаємо і як виправляємо відхилення». Пауза, Q&A."
}
```

**Час:** 3:00.

**Композиція:** HOW / WHAT з початку доповіді, тепер із відповідальностями ролей. Унизу спільний empirical team loop.

**Фінал:** «AI розширює наші можливості. Команда все одно відповідає за систему цілком: як ми її будуємо, яку поведінку дозволяємо, на яких доказах випускаємо і як виправляємо відхилення».

Детерміновані вимоги, тести та звичайні обов’язки не зникають. Без нових даних чи рекламного фіналу. Пауза, Q&A.

# Додаток для підготовки — не додаткові слайди

## Реєстр джерел і редакторські рішення

Повний покажчик перенесено до [EVIDENCE.md](EVIDENCE.md): прямі посилання на первинні звіти, використані версії, місця в джерелах, історичні перевірки й редакторський відбір. Цей розділ зберігається як навігаційна точка; детальні пояснення слайда 4 та арифметика нижче залишаються тут.

## Додаткова перевірка арифметики й формулювань

- NBER September revision, LOC: 1 + (234,3 + 957,5 + 1254,9) / 100 = 25,467 → 25,5×.
- NBER, commits: 1 + (30,2 + 153,2 + 60,7) / 100 = 3,441 → 3,4×.
- NBER, releases: 1 + (9,0 + 19,8) / 100 = 1,288 → 1,3×; async окремо не ідентифіковано.
- NBER: +2446,7% — приріст, 2546,7% базового рівня — рівень; це суми округленої таблиці, не точні raw-data coefficients.
- iOS: 87 − 78 = 9 відсоткових пунктів; Chrome: 33 − 19 = 14 пунктів; вихідні частки округлені авторами.
- GitClear duplication: 73 / 40,3 − 1 ≈ 81,1%. Відносна арифметика правильна, абсолютна одиниця в публічних матеріалах неузгоджена.
- Refactoring share 13% → 3,8%: падіння на 9,2 відсоткових пункту, не на 9,2% відносно бази.
- Навчальний eval: 196 / 200 = 98% прийнятних; 4 / 200 = 2% неприйнятних (3 неправильні інструкції + 1 privacy breach). Wilson 95% interval для частки неприйнятних ≈0,8%–5,0% за припущень незалежної репрезентативної вибірки. Критична помилка не зникає від агрегування.
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
