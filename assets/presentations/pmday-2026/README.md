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

### Зафіксовані слайди 1–11

За прямим запитом maintainer від 21 вересня 2026 року, після пояснення GitClear на слайді 4, **слайди 1–8 зафіксовано**. Не змінювати їхній зміст, числа, нотатки, геометрію, оформлення або спільні ресурси, що впливають на них, без наступного явного запиту maintainer на відповідні слайди. Наступний явний запит maintainer дозволив лише заміну шрифту на Roboto на всіх 14 слайдах; після повторного огляду запис захисту оновлено. Прямий запит від 22 вересня 2026 дозволяє додати графічне пояснення лише до слайда 8 за слайдом 3 старої презентації. Після перевірки його baseline оновлюється; слайди 1–7 незмінні, захист 1–8 надалі діє. Цей запит також дозволяє переробити 9–10 за наданими схемами. Наступний прямий запит 22 вересня дозволяє змінити тільки шрифт усіх 14 слайдів на стандартний міжплатформний Arial і доповнити 9, 11 та 12 за старими слайдами 16, 5, 14–15 відповідно (нумерація без обкладинки). Зміст, числа, нотатки й геометрія 1–8 залишаються захищеними; font-only baseline оновлюється після перевірки.

**Поточна межа захисту — слайди 1–11.** Наступним прямим запитом від 22 вересня 2026 maintainer погодив їхній поточний вигляд і розширив freeze з 1–8 до 1–11. Зміст, числа, нотатки, оформлення, геометрію, chart data та спільні ресурси цих слайдів можна змінювати лише за наступним явним запитом. Слайди 12–14 лишаються відкритими для роботи. Поточний запит щодо 12–13 — аналіз і пропозиція композиції; їхні render blocks не змінюються.

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
- Arial Regular / Bold за прямим запитом maintainer на стандартний шрифт для Keynote, PowerPoint і Google Slides. Усі text runs, charts і theme defaults посилаються на Arial; proprietary font bytes не додаються. Текст лишається редагованим. Для точної локальної верстки потрібен Arial; renderer без нього може підставляти інший шрифт. Попередній ліцензований Roboto archive збережений як історичний ресурс і не є поточним build input.
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
  "notes": "Thinking Systems — інженерна категорія, не твердження про свідомість. Формули — спрощений контраст. Точніше P(y | x, c, m): контекст, модель і конфігурація також мають значення. Стабільне повторення не гарантує істинності. Наскрізний умовний кейс: IT-асистент використовує дозволені джерела, але не має права на неавторизовані зміни доступу.\n\nВізуальне уточнення за наданими скриншотами, 22 вересня 2026. Графічне пояснення за слайдом 3 старої презентації: зліва одиничний результат за фіксованих input, state і version у детермінованому випадку, справа схематичний розподіл можливих результатів. Висота стовпчиків передає відносну частоту лише концептуально. Це не виміряна вибірка, не оцінка ймовірності, не твердження про нормальний розподіл чи математично важкі хвости. Горизонтальна вісь — умовна проєкція варіантів результату. Реальна семантика багатовимірна й може бути категоріальною. Центральна область показує корисну варіативність у прикладі, краї — рідші варіанти, які також потрібно оцінити. Рідкість сама по собі не робить результат дефектом. Інженерне завдання — сформулювати й реалізувати межі корисної поведінки. Детерміновані обов’язки, права та інваріанти в продукті залишаються. Обидві формули є навчальним контрастом, а не класифікацією всього software за одним параметром.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/uncertainty-in-the-controlled-object.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=3"
  ],
  "graphLabels": [
    "One fixed result",
    "Useful variation",
    "Less frequent outcomes"
  ],
  "deterministicDetail": "Same input, state and version: same result.",
  "probabilisticDetail": "The same request can produce different results.",
  "graphCaption": "Schematic distribution, not measured data. Shape depends on the task."
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

**Композиція:** Дві колонки з формулами. Ліворуч одиничний результат детермінованого випадку за фіксованих input/state/version. Праворуч native схема розподілу: блакитна центральна область корисної варіативності та бурштинові рідші варіанти з обох боків. Підпис прямо позначає схему як неметричну і невиміряну. Визначення Thinking Systems та попередні пояснення збережено.

**Що говорити:** «Thinking означає, що суттєвий runtime-крок делеговано Model Judgment. Це може бути вибір відповіді, інтерпретація звернення, пошук дії. Людина заздалегідь не виписала кожен допустимий результат».

Формула — контраст для пояснення. Реальне P залежить також від model version, prompt, retrieved context, tools і параметрів. Звичайне software теж може бути недетермінованим. Навіть стабільне повторення відповіді не гарантує її правильності.

**Наскрізний навчальний приклад для слайдів 8–12:** внутрішній IT-асистент відповідає за затвердженою базою знань і може підготувати заявку. Він не може сам собі надати права або змінювати доступ користувачів. Це вигаданий pilot, не реальний case study.

**Матеріал старої презентації:** зберегти deterministic/probabilistic контраст; не додавати окрему лекцію про LLM architecture.

**Перехід:** «Як написати вимогу, якщо правильна відповідь не одна?»

**Графічне пояснення за слайдами 3–5 старої презентації:** Графічне пояснення за слайдом 3 старої презентації: зліва одиничний результат за фіксованих input, state і version у детермінованому випадку, справа схематичний розподіл можливих результатів. Висота стовпчиків передає відносну частоту лише концептуально. Це не виміряна вибірка, не оцінка ймовірності, не твердження про нормальний розподіл чи математично важкі хвости. Горизонтальна вісь — умовна проєкція варіантів результату. Реальна семантика багатовимірна й може бути категоріальною. Центральна область показує корисну варіативність у прикладі, краї — рідші варіанти, які також потрібно оцінити. Рідкість сама по собі не робить результат дефектом. Інженерне завдання — сформулювати й реалізувати межі корисної поведінки. Детерміновані обов’язки, права та інваріанти в продукті залишаються. Обидві формули є навчальним контрастом, а не класифікацією всього software за одним параметром.

## 9. Requirements Become Boundaries

```pptx-slide
{
  "number": 9,
  "layout": "boundaries",
  "role": "PRODUCT MANAGER + BA · define acceptable outcomes, harm and cost",
  "oldHeading": "SPECIFIED FLOW · STILL REQUIRED",
  "old": [
    "Button A",
    "Window B"
  ],
  "oldDetail": "Exact states, permissions\nand transitions.",
  "roleDetail": "Product / BA: tolerance contract.\nProject Manager: decisions + dependencies.",
  "newHeading": "SPACE OF POSSIBLE BEHAVIORS",
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
  "takeaway": "From story ownership to an agreed contract for a range of outcomes.",
  "notes": "Наскрізний приклад: внутрішній IT-асистент. Зліва — точний перехід Button A → Window B, permissions та інваріанти, які залишаються вимогами. Справа — додаткові вимоги до варіативної поведінки. Дозволено пояснити затверджену статтю підтримки різними словами, зберігаючи зміст і необхідні кроки. За відсутності контексту потрібно уточнити або ескалувати. Не можна вигадувати операційні кроки, розкривати чужі дані або виконувати дію в обхід approval. Одна картинка з областю сама не задає точного вимірюваного контракту.\nМовний розрив: природна мова неоднозначна; prompt не є точним описом усіх можливих відповідей. Теза «стандартів немає» надто категорична: ISO/IEC 25059:2023 надає quality model і узгоджену термінологію, NIST AI RMF — контекстне управління ризиком, GenAI Profile — спільне з domain experts документування допустимого використання. Вони не підставляють готові семантичні межі й прийнятність наслідків для нашого продукту. Не стверджуємо доведеної відсутності будь-якої формальної мови.\nПрактична пропозиція доповіді: Product Manager та BA разом із бізнесом збирають сценарії, приклади, контрприклади, клас наслідків і потрібну реакцію; фіксують rubric, джерело правила й того, хто його погоджує. CheckList (Ribeiro et al., ACL 2020) пропонує capability × test-type підхід до поведінкових перевірок NLP. Це допомога у формулюванні перевірок, не універсальний стандарт semantic acceptance. Project Manager планує доступ до stakeholders, рішення та залежності; не вигадує толерантність за бізнес.\nВимога ширша за Operating Envelope; точні інтерфейси, заборони й інваріанти зберігаються. BA/Product не зобов’язані самі вивести статистичний поріг: це спільна робота з бізнесом, QA, розробниками й власником ризику. Ролі описують відповідальність, не новий headcount.\nДеталізація бізнес-контракту. Два формулювання відповіді можуть бути однаково правильними: асистент має право скоротити пояснення або змінити тон, але повинен зберегти затверджені кроки, умови та застереження. Заміна тексту сама по собі не є дефектом. Порушення змісту, неправомірна дія або непрацездатний обов’язковий fallback — вже інше питання. Тому команда описує не всі речення наперед, а дозволені джерела й теми, потрібні semantic properties, неприйнятні наслідки та реакцію на невизначеність.\nProduct Manager і BA додають до прикладів контракт на експлуатацію: який ручний rework бізнес здатен обробити; скільки коштує корисно завершений запит з урахуванням перевірок, повторів і людей; яку затримку користувач витримає; за яких умов потрібні уточнення, людина або відмова. Якщо ці межі невідомі, це питання для дослідження зі stakeholders, а не число, яке QA має вгадати. Для IT-асистента питання бізнесу звучить так: «Коли краще не дати інструкцію, а передати звернення фахівцю, і чи зможемо ми обслужити цей потік?».\nСпільна мова формується через позначені приклади й контрприклади, rubric, класи наслідків, approved sources та decision owner. Prompt впливає на відповіді, але не задає повного acceptance specification. Графічна область і один semantic-distance score також не замінюють цей контракт. Межі якості, вартості й latency не стають жорсткими гарантіями без окремого реалізованого enforcement path.\n\nНа правій половині тепер зображено саме область можливих прийнятних результатів. Це концептуальна межа, а не графік з універсальною числовою віссю semantic distance. Коротке й докладне пояснення можуть бути однаково прийнятними, якщо обидва спираються на затверджену статтю та зберігають обов’язкові кроки. Вимога задає властивості області: дозволені теми й джерела, потрібний зміст, заборонені дії та дані, ресурсні межі, реакцію на нестачу контексту. CLARIFY — визначена контрактом дія, коли доказів для змістовної відповіді недостатньо; це не дозвіл порушити межу. PROHIBIT поза дозволеною областю показує неприйнятні наслідки. Саме формулювання межі її не реалізує: для критичних заборон потрібні конкретні контролі. Ліворуч лишаються точні стани, права й переходи. Нові обов’язки доповнюють ці сценарії. Product Manager та BA мають отримати від бізнесу приклади допустимих варіантів і контрприклади, а Project Manager забезпечує рішення та доступність потрібних учасників.\n\nВізуальне уточнення за наданими скриншотами, 22 вересня 2026. Візуальна модель тепер безпосередньо відтворює логіку слайда 5 старої презентації: зліва вузький маршрут A–B, справа площина можливостей із перспективною сіткою, зовнішнім бурштиновим контуром погоджених допусків та внутрішньою блакитною областю цільової поведінки. Обидва прийнятні варіанти — коротке та докладне пояснення — належать спільній області. Зовні показано заборонений результат. Внутрішній контур — робочий орієнтир, зовнішній — контракт прийнятності. Простір між ними не є автоматичним дозволом: кожен результат повинен виконувати всі умови контракту. Це концептуальна багатовимірна область, а не виміряна координатна система чи універсальна embedding-distance метрика. Площина стисло показує сукупність умов щодо тем, джерел, обов’язкового змісту, даних, дій, authority, вартості, latency та failure handling. Вимога включає й точний сценарій, і цю область. CLARIFY визначає належну реакцію на нестачу контексту, а не ослаблення заборони. Попередні ALLOW / CLARIFY / PROHIBIT і приклади залишаються в нотатках та уточнюють геометрію.\n\nІнтеграція старого слайда 16 (PDF page 17, PM: From Story Owner to Distribution Economist). Тут PM у старому заголовку означає Product Manager; Project Manager у нашій доповіді — окрема відповідальність за delivery та операційну модель. Product / BA організовують з бізнесом рішення: які варіації результату прийнятні; скільки та яких помилок можна допустити; за якої тяжкості, частоти або наслідку відповідь стає неприйнятною відповідальністю; коли потрібні зупинка, людина чи fallback. Не можна звести це до одного середнього відсотка або грошей: обов’язкові заборони залишаються заборонами. До контракту входять unsupported claims, визначена для продукту semantic rubric, правила ескалації, бюджет токенів та human review, latency і поведінка fallback. Ланцюжок Product value → Risk tolerance → Cost envelope → Release decision пояснює бізнес-сенс меж на діаграмі. QA та розробники разом із Product/BA переводять ці рішення у вимірювання та evidence; Project Manager забезпечує доступність stakeholder decisions, власників і залежностей. Prompt лише впливає на поведінку; контракт визначають погоджені вимоги, приклади та критерії. Попередні пояснення області, ALLOW / CLARIFY / PROHIBIT, мовного розриву та наявних стандартів зберігаються.",
  "sources": [
    "https://www.iso.org/standard/80655.html",
    "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf",
    "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf",
    "https://aclanthology.org/2020.acl-main.442/",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/requirements-correctness-and-bugs.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=5",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=7",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=17",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=5"
  ],
  "envelopeHeading": "PRODUCT VALUE → RISK TOLERANCE → COST ENVELOPE → RELEASE DECISION",
  "envelope": [
    "Meaning: approved steps; wording may vary",
    "Errors: acceptable frequency AND impact",
    "Economics: token + review cost; latency",
    "Liability: prohibit, escalate or use fallback"
  ],
  "specification": "Business sets tolerances; Product / BA turn them into examples, limits and acceptance rules.",
  "regionCaption": "Approved tolerance boundary",
  "regionExamples": [
    "Short explanation",
    "Detailed explanation"
  ],
  "regionInner": "Target operating region",
  "regionOutside": "Prohibited outcome",
  "regionAxis": "Conceptual space, not a universal semantic metric",
  "regionPolicy": "ALLOW approved sources   ·   CLARIFY missing context   ·   PROHIBIT unsafe actions"
}
```

**Час:** 3:00.

**Композиція:** Ліва Button A → Window B збережена. Праворуч native площина можливостей із перспективною сіткою, зовнішнім бурштиновим контуром допусків і внутрішньою блакитною областю цільової поведінки. Усередині — різні прийнятні пояснення, зовні — заборонений результат. Підписи ALLOW / CLARIFY / PROHIBIT, business tolerance contract та рольове пояснення зберігають зміст. Це концептуальна область, не універсальна числова semantic-distance вісь.

**Рольова зміна:** Product Manager + BA переводять бізнес-сценарії в приклади, контрприклади та rubric; Project Manager забезпечує своєчасні рішення stakeholders. ISO/IEC 25059 і NIST існують, але не вирішують за команду межі конкретного продукту. Research proposal: CheckList як метод структурування behavioral tests. [Джерела й межі](EVIDENCE.md#вимоги-оцінювання-та-ролі--слайди-914).

**Перехід:** «Домовитися, що прийнятно, ще недостатньо. Як виміряти, наскільки часто система дотримується цієї домовленості?»

**Поглиблення змісту:** Додаємо видимий business tolerance contract: дозволена варіативність, обов’язковий зміст, rework/cost/latency та escalation. Product і BA переводять бізнес-сценарії в цей контракт; prompt залишається лише одним засобом впливу на поведінку.


**Уточнення 22 вересня:** На правій половині тепер зображено саме область можливих прийнятних результатів. Це концептуальна межа, а не графік з універсальною числовою віссю semantic distance. Коротке й докладне пояснення можуть бути однаково прийнятними, якщо обидва спираються на затверджену статтю та зберігають обов’язкові кроки. Вимога задає властивості області: дозволені теми й джерела, потрібний зміст, заборонені дії та дані, ресурсні межі, реакцію на нестачу контексту. CLARIFY — визначена контрактом дія, коли доказів для змістовної відповіді недостатньо; це не дозвіл порушити межу. PROHIBIT поза дозволеною областю показує неприйнятні наслідки. Саме формулювання межі її не реалізує: для критичних заборон потрібні конкретні контролі. Ліворуч лишаються точні стани, права й переходи. Нові обов’язки доповнюють ці сценарії. Product Manager та BA мають отримати від бізнесу приклади допустимих варіантів і контрприклади, а Project Manager забезпечує рішення та доступність потрібних учасників.

**Графічне пояснення за слайдами 3–5 старої презентації:** Візуальна модель тепер безпосередньо відтворює логіку слайда 5 старої презентації: зліва вузький маршрут A–B, справа площина можливостей із перспективною сіткою, зовнішнім бурштиновим контуром погоджених допусків та внутрішньою блакитною областю цільової поведінки. Обидва прийнятні варіанти — коротке та докладне пояснення — належать спільній області. Зовні показано заборонений результат. Внутрішній контур — робочий орієнтир, зовнішній — контракт прийнятності. Простір між ними не є автоматичним дозволом: кожен результат повинен виконувати всі умови контракту. Це концептуальна багатовимірна область, а не виміряна координатна система чи універсальна embedding-distance метрика. Площина стисло показує сукупність умов щодо тем, джерел, обов’язкового змісту, даних, дій, authority, вартості, latency та failure handling. Вимога включає й точний сценарій, і цю область. CLARIFY визначає належну реакцію на нестачу контексту, а не ослаблення заборони. Попередні ALLOW / CLARIFY / PROHIBIT і приклади залишаються в нотатках та уточнюють геометрію.

**Уточнення за старим слайдом 16 (PDF page 17):** Product value → Risk tolerance → Cost envelope → Release decision. Product/BA погоджують з бізнесом частоту й тяжкість помилок, ціну варіативності, заборонені наслідки та правила escalation/fallback; Project Manager забезпечує рішення й залежності. Геометрія області лишається.

## 10. One Green Test Proves Almost Nothing

```pptx-slide
{
  "number": 10,
  "layout": "evaluation",
  "role": "QA + DEVELOPERS · estimate behavior, uncertainty and consequences",
  "frequency": "ILLUSTRATIVE SAMPLE · n = 200",
  "observed": "4 / 200 = 2%",
  "interval": "95% Wilson interval ≈ 0.8%–5.0%",
  "rateLabel": "Observed unacceptable outputs",
  "severity": "FREQUENCY + CONSEQUENCES",
  "harms": [
    "3 incorrect instructions → rework",
    "1 privacy leak → critical breach"
  ],
  "decision": "Critical breach → BLOCK RELEASE",
  "sample": "Illustrative independent sample, grouped by outcome. No production guarantee.",
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
  "notes": "Статистичне оцінювання доповнює unit, integration, security та deterministic tests. Потрібно окремо оцінити: а) частоту виходу за погоджені межі; б) силу/тяжкість наслідку. «Сила відхилення» не має універсальної числової шкали: для latency це мілісекунди понад межу, для грошей — збиток, для semantic output — погоджена rubric і класи наслідків. Середній score або embedding distance сам по собі не встановлює business harm. Хвости й критичні групи оцінюємо окремо, а не приховуємо добрим агрегатом.\nНавчальний приклад, не реальні дані і не рекомендований sample size: 200 незалежних репрезентативно відібраних evaluation units із одного стабільного цільового розподілу; 196 прийнятних, 4 неприйнятні. Серед чотирьох: 3 неправильні інструкції та 1 витік даних. 4/200=2%; 196/200=98%. Двосторонній 95% Wilson score interval для частки неприйнятних: [0.780443%, 5.028709%], на слайді ≈0.8%–5.0%. Метод і формула — NIST Engineering Statistics Handbook §7.2.4.1. Інтервал відображає sampling uncertainty за припущень; не дає 95% ймовірності, що конкретний майбутній результат безпечний, і не гарантує поведінки після зміни контексту. Не можна рахувати повтори того самого кейсу як незалежні representative cases. Розмір вибірки, dependence, subgroup coverage, множинні порівняння, невизначеність оцінювача й baseline планують під рішення.\nУ прикладі витік порушує обов’язкову вимогу, тому release блокується незалежно від 98% aggregate acceptance. Відсутність витоків у тесті також не доводила б неможливості витоку: потрібні permissions, isolation, gate та перевірка припущень їх роботи.\nЗвідки взяти tolerance? QA не винаходить його. Product Manager та BA обговорюють із бізнесом зрозумілі сценарії: скільки ручного виправлення витримає support; кому і яку шкоду завдасть помилка; що треба технічно унеможливити; коли прийнятні уточнення або ручний шлях. Технічна команда перетворює це на measurement plan, оцінку частот, severity, confidence та тригери. Уповноважений власник ризику/релізу погоджує допустимість у конкретному scope. Project Manager організовує ці рішення до обіцянки релізу.\nModel drift пояснюємо бізнесу як зміну спостережуваних результатів/навантаження/наслідків за нової версії чи контексту, а не вимагаємо від stakeholders знання статистичних термінів. QA підтримує golden/reference sets, coverage, calibration із domain experts і перевірки підгруп. Developers роблять versioning, instrumentation, відтворювані evaluation runs і regression comparison. Пороги та rubric версіонуються; evidence для release перевіряється окремо від набору, на якому їх підбирали.\nЩо саме змінюється в QA. Golden Set — версіонований набір звичайних, крайових, adversarial і business-critical сценаріїв з очікуваними властивостями змісту та прикладами неприйнятного результату. Це інструмент вимірювання: він сам може бути неповним, застарілим або невдало розміченим. QA разом із domain experts калібрує rubric та evaluator: де він пропускає небезпечну відповідь, де помилково блокує корисну, як розходяться людські оцінки. Розробник забезпечує runner, конфігурацію, provenance та порівняння baseline із candidate.\nEval Gate пов’язує отримані evidence з погодженим рішенням: block, обмежена експозиція або release у визначених межах. Сам score ще не приймає business risk. Повторні запуски показують варіативність усередині сценарію, а різні сценарії — coverage. Цілеспрямовано зібраний Golden Set не є автоматично репрезентативною вибіркою production traffic; його pass rate не можна без обґрунтування підставити як реальну частоту помилок. Навчальні 4/200 та Wilson interval вище мають власні явно названі припущення.\nЗміна моделі, prompt, retrieval або складу запитів може змінити розподіл результатів навіть без зміни application code. Після інциденту додаємо відтворюваний regression case, перевіряємо чутливість evaluator і причину пропуску. Фінальну release evidence оцінюємо на незалежних від налаштування даних. Бізнесу показуємо не слово «drift», а зміну кількості виправлень, ескалацій, неприйнятних наслідків, затримки й вартості.\n\nГрафік показує емпіричний розподіл категорій тієї самої навчальної вибірки: 196 прийнятних результатів, 3 неправильні інструкції й 1 витік приватних даних. Разом 200, частки відповідно 98%, 1,5% та 0,5%. Це не 200 різних унікальних рядків тексту: результати групуються за погодженими семантичними властивостями та наслідками. Категорії в цьому прикладі взаємовиключні та вичерпні. Вісь починається з нуля, довжина стовпчиків пропорційна кількості. Малі стовпчики не означають малої тяжкості, тому точні значення та критичний наслідок підписано. Неприйнятні результати об’єднуються для оцінки частоти: (3+1)/200 = 2%. Попередній 95% Wilson interval приблизно 0,8%–5,0% стосується цієї бінарної події, а не кожної категорії окремо та не ймовірності майбутнього інциденту без припущень про вибірку. Ми не накладаємо нормальну криву на категоріальні дані та не вигадуємо baseline для порівняння. Для нового порівняння потрібні зафіксовані версії й порівнювані сценарії. Саме цей перехід до частот, розподілів та невизначеності запозичено зі слайдів 7 і 19 старої презентації. Бізнес має визначити допустимість частоти та сили наслідку, QA — які докази й невизначеність є для рішення.\n\nВізуальне уточнення за наданими скриншотами, 22 вересня 2026. Визначення дефекту й схематична область допусків адаптовані зі слайда 4 старої презентації з уточненням чинної UA doctrine Requirements, Correctness, and Bugs. Bug — порушення погодженої вимоги на рівні системи, яке спричинила або допустила реалізована система. Для model-mediated поведінки це, зокрема, вихід за погоджені умови чи допуски або заборонений наслідок. На схемі зелена область — дозволена варіативність, червоні стовпчики — наслідки за межами контракту, якщо система їх допустила. Графік концептуальний: висоти не є даними, нормальність не припускається, одиниць універсальної semantic distance немає. Схема і вибірка 196/3/1 — різні пояснювальні об’єкти; концептуальні стовпчики не відновлені з цих трьох категорій. Рідкісний результат не обов’язково Bug. Якщо запропоновану моделлю заборонену дію контролі належно зупинили до наслідку, це може бути коректним containment за контрактом. Якщо частота помилок допускається в певному контексті, потрібні також погоджені межі тяжкості, наслідків і правила обробки, а не тільки середній відсоток. Розподіл може змінюватися без змін коду, однак окремий tail event не доводить drift: для цього потрібні порівнювані вибірки, baseline, контекст і версії. Класичні детерміновані дефекти також залишаються. На екрані нижче збережено незалежний навчальний приклад: 196 прийнятних, 3 неправильні інструкції та 1 витік приватних даних, 4/200 = 2%, Wilson 95% приблизно 0,8%–5,0%. Частота і тяжкість — різні виміри рішення. У цьому прикладі витік порушує обов’язкову заборону й блокує release. Бізнес через Product/BA визначає прийнятність наслідків, QA/developers вимірюють і перевіряють evidence, уповноважений risk/release owner ухвалює рішення. Golden Set, Eval Gate, калібрування та incident regression залишаються робочими інструментами.",
  "sources": [
    "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf",
    "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf",
    "https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm",
    "https://aclanthology.org/2020.acl-main.442/",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/01-patterns/thinking-system-review.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=14",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=19",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=4",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/requirements-correctness-and-bugs.md"
  ],
  "instruments": "Golden Set: routine, edge and adversarial cases. Eval Gate: compare versions against agreed limits.",
  "calibration": "QA calibrates the evaluator with domain experts. Incidents become new regression cases.",
  "chartCategories": [
    "Acceptable",
    "Incorrect steps",
    "Privacy leak"
  ],
  "chartCounts": [
    196,
    3,
    1
  ],
  "chartLabels": [
    "196\n98%",
    "3\n1.5%",
    "1\n0.5%"
  ],
  "chartAxis": "Observed counts by outcome",
  "bugHeading": "WHAT COUNTS AS A BUG",
  "bugDefinition": "System behavior violates\nan approved requirement.",
  "bugModel": "Model behavior can leave agreed tolerances\nor produce a prohibited outcome.",
  "bugCode": "The code may stay unchanged while behavior changes.",
  "bugNuance": "Variation alone is acceptable. A contract violation is a defect.",
  "toleranceHeading": "APPROVED BUSINESS TOLERANCES",
  "insideLabel": "Allowed variation",
  "outsideLabel": "Outside the contract",
  "bugLabel": "Bug:\ncontract\nviolation",
  "schematicCaption": "Schematic projection, not measured data. Limits are product-specific.",
  "ownershipLine": "Product + BA agree limits. QA + Dev measure. Risk / release owner decides."
}
```

**Час:** 3:00.

**Композиція:** Угорі ліворуч визначення Bug як порушення погодженої вимоги, праворуч native схематичний розподіл з дозволеною зеленою областю й червоними результатами поза контрактом. Унизу збережено окремий native chart навчальної вибірки 196 / 3 / 1 з точною шкалою 0–200, частоту 4/200 = 2%, Wilson 95% interval ≈0,8%–5,0%, тяжкість і block release. Схема не є апроксимацією цієї категоріальної вибірки. Інструменти й відповідальність залишаються на слайді та розгорнуті в нотатках.

**Рольова зміна:** QA + Developers будують sample/evaluation plan, calibration, subgroup coverage, version comparisons та instrumentation. Product + BA отримують tolerance через зрозумілі бізнесу наслідки; risk/release owner погоджує acceptability. Статистика не вибирає business tolerance. Severity може бути сумою збитку, часом або категорією наслідку; універсального semantic distance немає.

**Перехід:** «Ці докази й домовленості повинні бути частиною Ready, Done та окремого рішення про release».

**Поглиблення змісту:** Поруч із незміненим прикладом 4/200 показано інструменти QA: Golden Set, Eval Gate, калібрування evaluator із domain experts і повернення інцидентів у regression cases. Цілеспрямований Golden Set не прирівнюється до representative production sample.


**Уточнення 22 вересня:** Графік показує емпіричний розподіл категорій тієї самої навчальної вибірки: 196 прийнятних результатів, 3 неправильні інструкції й 1 витік приватних даних. Разом 200, частки відповідно 98%, 1,5% та 0,5%. Це не 200 різних унікальних рядків тексту: результати групуються за погодженими семантичними властивостями та наслідками. Категорії в цьому прикладі взаємовиключні та вичерпні. Вісь починається з нуля, довжина стовпчиків пропорційна кількості. Малі стовпчики не означають малої тяжкості, тому точні значення та критичний наслідок підписано. Неприйнятні результати об’єднуються для оцінки частоти: (3+1)/200 = 2%. Попередній 95% Wilson interval приблизно 0,8%–5,0% стосується цієї бінарної події, а не кожної категорії окремо та не ймовірності майбутнього інциденту без припущень про вибірку. Ми не накладаємо нормальну криву на категоріальні дані та не вигадуємо baseline для порівняння. Для нового порівняння потрібні зафіксовані версії й порівнювані сценарії. Саме цей перехід до частот, розподілів та невизначеності запозичено зі слайдів 7 і 19 старої презентації. Бізнес має визначити допустимість частоти та сили наслідку, QA — які докази й невизначеність є для рішення.

**Графічне пояснення за слайдами 3–5 старої презентації:** Визначення дефекту й схематична область допусків адаптовані зі слайда 4 старої презентації з уточненням чинної UA doctrine Requirements, Correctness, and Bugs. Bug — порушення погодженої вимоги на рівні системи, яке спричинила або допустила реалізована система. Для model-mediated поведінки це, зокрема, вихід за погоджені умови чи допуски або заборонений наслідок. На схемі зелена область — дозволена варіативність, червоні стовпчики — наслідки за межами контракту, якщо система їх допустила. Графік концептуальний: висоти не є даними, нормальність не припускається, одиниць універсальної semantic distance немає. Схема і вибірка 196/3/1 — різні пояснювальні об’єкти; концептуальні стовпчики не відновлені з цих трьох категорій. Рідкісний результат не обов’язково Bug. Якщо запропоновану моделлю заборонену дію контролі належно зупинили до наслідку, це може бути коректним containment за контрактом. Якщо частота помилок допускається в певному контексті, потрібні також погоджені межі тяжкості, наслідків і правила обробки, а не тільки середній відсоток. Розподіл може змінюватися без змін коду, однак окремий tail event не доводить drift: для цього потрібні порівнювані вибірки, baseline, контекст і версії. Класичні детерміновані дефекти також залишаються. На екрані нижче збережено незалежний навчальний приклад: 196 прийнятних, 3 неправильні інструкції та 1 витік приватних даних, 4/200 = 2%, Wilson 95% приблизно 0,8%–5,0%. Частота і тяжкість — різні виміри рішення. У цьому прикладі витік порушує обов’язкову заборону й блокує release. Бізнес через Product/BA визначає прийнятність наслідків, QA/developers вимірюють і перевіряють evidence, уповноважений risk/release owner ухвалює рішення. Golden Set, Eval Gate, калібрування та incident regression залишаються робочими інструментами.

## 11. DoR / DoD Become Risk Contracts

```pptx-slide
{
  "number": 11,
  "layout": "risk",
  "role": "DEVELOPERS + QA · from a green run to a statistical quality contract",
  "table": [
    [
      "GATE",
      "CLASSIC FOCUS",
      "ADDED FOR MODEL BEHAVIOR",
      "DECISION / OWNER"
    ],
    [
      "READY\nDoR",
      "Story + acceptance\nDependencies understood",
      "Risk tolerances + prohibited outcomes\nEvaluation plan + complete control design\nHuman authority, capacity and fallback",
      "Product / BA + Architect\nPM resolves dependencies"
    ],
    [
      "BUDGET",
      "Runtime cost +\nperformance requirements",
      "Token + evaluation + human-review costs\nExplicit spend, latency and capacity limits",
      "Product agrees economics\nArchitect checks feasibility"
    ],
    [
      "DONE\nDoD",
      "Code review + tests\nAcceptance verified",
      "Versioned model / prompt / data\nEval Gates: sample, uncertainty, coverage\nWorking controls + human / recovery tests",
      "Developer + QA verify\nValid JSON ≠ correct meaning"
    ],
    [
      "RELEASE\nOPERATE",
      "Release approval\nDeployment + operations",
      "Accepted evidence + scoped release\nLive monitoring + responders + stop rules\nIncidents update regression, Eval Gates\nand monitoring rules",
      "Authorized owner: accept,\nnarrow, defer or reject\nPM tracks operating readiness"
    ]
  ],
  "caption": "Classic focus is simplified; risk, cost and operations already matter in conventional software.",
  "takeaway": "“Done” is an evidence package. Release is a separate, scoped decision.",
  "notes": "Конкретизуємо абстрактні risk contracts через deliverables розробників для того самого IT-асистента. READY: визначено аудиторію, дозволені джерела, заборонені дії, приклади/rubric, evaluation plan, критичні залежності й власника ручного шляху. Якщо tolerance або feasibility ще невідомі, команда може бути Ready до обмеженого експерименту з питанням, бюджетом, stop condition та owner; це не дозвіл на production.\nDONE: developer поставляє відтворювану конфігурацію model version, prompt, retrieval/data snapshot, tool schema, policy та permissions; результати deterministic, behavioral і control-path tests; посилання на evaluation evidence, coverage й обмеження. Перевірені deny-path, unavailable-control behavior, telemetry та фактичний rollback/manual fallback. QA звіряє evaluation method і results, а не одноосібно приймає business risk. Для слайда скорочено до model/prompt/data; повний список тут.\nRELEASE: ідентифіковано саме цю версію, population, tool authority, exposure, monitoring, stop triggers, оперативного owner та fallback capacity. Уповноважена особа приймає залишковий ризик у межах повноважень або звужує scope, відкладає чи відхиляє реліз. Прийняття ризику не скасовує обов’язкову заборону й не розширює успадковану project authority. Попередній toy-example із privacy breach не пройде цей gate.\nРозробник тепер здає не лише endpoint, а відтворювану поведінку, evidence і працездатний recovery path. Project Manager відстежує незакриті залежності/рішення та не прирівнює Done до Ship. Ролі можуть поєднуватись однією людиною; достатньо існуючого review artifact, новий комітет не потрібний.\nПрактичний engineering object — версія поведінки, а не лише commit застосунку. Один і той самий endpoint із новим prompt, knowledge snapshot, моделлю, evaluator або правами інструментів може мати інший профіль якості й ризику. Тому evidence та rollback прив’язуються до узгодженого набору версій. Окремий Prompt Registry не обов’язковий: для малої команди достатньо наявного version control та deployment/configuration механізму, якщо вони дозволяють встановити, що саме працювало, хто погодив зміну і як повернутись.\nREADY включає quality, cost і latency budgets та місткість ручного шляху. Для експерименту потрібні обмеження експозиції й ресурсів до початку роботи. DONE включає deterministic tests, coverage поведінкових сценаріїв, невизначеність оцінки й порівняння з baseline. Валідний JSON перевіряє форму: структурно правильний об’єкт може містити вигадану інструкцію. Тому schema pass доповнюється semantic evidence, permissions і перевіреним recovery path.\nRELEASE має явні варіанти block, canary або scoped release. Canary також потребує попереднього дозволу, обмеженої аудиторії, моніторингу та можливості зупинити експозицію. Усі попередні критерії й власники залишаються. Rollback повертає конфігурацію, але не скасовує вже виконану зовнішню дію: для таких наслідків потрібні containment, ручне виправлення або компенсація.\n\nТаблиця тепер прямо порівнює звичний фокус DoR/DoD з додатковими зобов’язаннями для model-mediated behavior. Ліва колонка — спрощений навчальний фокус, а не твердження, що класичний software не має ризик-аналізу, навантажувальних тестів, моніторингу або incident management. Усі наявні вимоги організації залишаються. У DoR потрібен повний і правдоподібний дизайн керування для суттєвих сценаріїв: вимога й межа, спосіб її реалізації, спостереження, уповноважене рішення, виконавчий механізм та перевірка ефекту. Сюди входить human-in-the-loop: хто втручається, з якою інформацією, правами, часом і доступною потужністю, хто підміняє та що відбувається при недоступності. DoR до реалізації не вимагає вже збудованої системи, але має показати весь задум і залежності. Якщо feasibility ще невідома, Ready може означати лише готовність до окремо обмеженого дослідження. До експерименту з реальним exposure потрібні вже працездатні відповідні контролі. DoD підтверджує реалізацію й перевірку цього контуру, включно з людиною та fallback; версії, baseline, оцінка невизначеності, resource budgets і recovery evidence зберігаються. Release визначає population, tool permissions, residual risk, відповідальну особу, постійний моніторинг і triggers для stop/rollback. Block, canary або scoped release — різні дозволені результати рішення. Робота не закінчується релізом: production incidents породжують regression cases, зміни критеріїв Eval Gate та правил моніторингу. Такі зміни також версіонуються, перевіряються й погоджуються в межах повноважень; не можна тихо послабити бізнес-межу, щоб метрика стала зеленою.\n\nІнтеграція старого слайда 5 (PDF page 6, From Static Requirements to Statistical Gates). Чотири порівнювані рядки тепер видно безпосередньо: Ready, Budget, Done та Release / Operate. Окремий Budget повертає cost envelope зі старої презентації: токени, повторні виклики, evaluations, людська перевірка, latency та місткість fallback мають впливати на readiness і життєздатність. Статистичний контракт не означає, що великий n доводить безпеку: потрібні придатна вибірка, coverage, калібрований evaluator, припущення й оцінка невизначеності щодо погодженого порога. Приймають evidence у контексті бізнес-допусків, а не абстрактний confidence interval сам по собі. Старий фокус показаний як навчальне спрощення: класична інженерія також має nonfunctional requirements, ризик, вартість, навантажувальні тести та operations. Повний control/HITL design лишається в DoR, працездатність і rehearsal — в DoD. Release залишається окремим scoped decision із постійним monitoring та incident → regression / Eval Gates / monitoring rules loop. Зміна правил не може непомітно послабити затверджену межу.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/01-patterns/thinking-system-review.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/nested-control-lifecycle.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=6",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=9",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=13"
  ],
  "behavior": "Requirements stay. Readiness, completion and release also need risk, cost and confidence evidence.",
  "syntax": "A green run is an observation. Acceptance needs agreed tolerances and sufficient evidence."
}
```

**Час:** 3:00.

**Композиція:** Native table порівнює GATE / STILL REQUIRED / ADDED FOR MODEL BEHAVIOR / DECISION–OWNER. DoR містить повний дизайн керування з людьми, DoD — реалізацію та докази, Release + Operate — live monitoring і повернення інцидентів у regression, Eval Gates та monitoring rules.

**Рольова зміна:** Developer здає відтворювану capability разом із evidence та recovery path. QA перевіряє докази, Product + BA — acceptance, Project Manager — залежності/рішення. Done не дозволяє production автоматично. Ready до bounded experiment також не є production authorization. Release належить уповноваженому owner у межах успадкованих constraints.

**Перехід:** «Після релізу та сама відповідальність має технічний шлях дії».

**Поглиблення змісту:** DoR / DoD / Release зберігають попередні evidence та owners. Додано cost/latency budgets, coverage та uncertainty, baseline comparison і block/canary/scoped-release outcomes. Версія поведінки може змінитись без зміни application code; валідна структура не доводить правильність інструкції.


**Уточнення 22 вересня:** Таблиця тепер прямо порівнює звичний фокус DoR/DoD з додатковими зобов’язаннями для model-mediated behavior. Ліва колонка — спрощений навчальний фокус, а не твердження, що класичний software не має ризик-аналізу, навантажувальних тестів, моніторингу або incident management. Усі наявні вимоги організації залишаються. У DoR потрібен повний і правдоподібний дизайн керування для суттєвих сценаріїв: вимога й межа, спосіб її реалізації, спостереження, уповноважене рішення, виконавчий механізм та перевірка ефекту. Сюди входить human-in-the-loop: хто втручається, з якою інформацією, правами, часом і доступною потужністю, хто підміняє та що відбувається при недоступності. DoR до реалізації не вимагає вже збудованої системи, але має показати весь задум і залежності. Якщо feasibility ще невідома, Ready може означати лише готовність до окремо обмеженого дослідження. До експерименту з реальним exposure потрібні вже працездатні відповідні контролі. DoD підтверджує реалізацію й перевірку цього контуру, включно з людиною та fallback; версії, baseline, оцінка невизначеності, resource budgets і recovery evidence зберігаються. Release визначає population, tool permissions, residual risk, відповідальну особу, постійний моніторинг і triggers для stop/rollback. Block, canary або scoped release — різні дозволені результати рішення. Робота не закінчується релізом: production incidents породжують regression cases, зміни критеріїв Eval Gate та правил моніторингу. Такі зміни також версіонуються, перевіряються й погоджуються в межах повноважень; не можна тихо послабити бізнес-межу, щоб метрика стала зеленою.

**Уточнення за старим слайдом 5 (PDF page 6):** Native таблиця прямо порівнює classic focus та додатковий статистичний контракт у чотирьох рядках Ready, Budget, Done, Release/Operate. Окремо показані токени/evaluations/human review, statistical uncertainty, повний control/HITL design, rehearsal та постійний incident feedback.

## 12. Production Needs a Control Loop

```pptx-slide
{
  "number": 12,
  "layout": "control",
  "role": "ARCHITECT · design containment, recovery and the boundary of feasibility",
  "steps": [
    "Approved context",
    "Model proposal",
    "Permission gate",
    "Support tool"
  ],
  "gate": "Tool actions: deterministic permission / approval gate. Unavailable? Deny and use safe fallback.",
  "reference": "Approved limits",
  "loop": [
    "Observe",
    "Decide / authorize\nsoftware + people",
    "Apply correction"
  ],
  "actions": "Rollback / disable tool / manual fallback · inside delegated authority",
  "caption": "Observe outcomes + gate health. Verify that the corrective action took effect.",
  "takeaway": "Production readiness requires a complete, operable control path.",
  "notes": "Наскрізний IT-асистент: approved context → model proposal → deterministic permission/approval gate → support tool. Модель пропонує дію; тільки gate дозволяє виконання в межах allowlist, user permissions і required approval. Приклад передбачає відсутність обхідного шляху; за недоступного gate дію відхиляють і пропонують ручний шлях. Схема показує конкретний tool-action path, не універсальну топологію всіх Thinking Systems і не гарантію семантичної коректності довільного тексту. User-facing answer path потребує власних scoped controls.\nНижній цикл: Observe збирає outcomes, incidents, затримку, fallback load, стан gate, bypass attempts, execution/effects корекцій. Compare/authorize зіставляє їх із явно показаними Approved operating limits; відповідальний Controller або людина вирішує, що дозволено змінити. Apply correction виконує rollback/disable/manual fallback у межах delegated authority. Зворотний зв’язок показує зміну operation; технічно correction може діяти на routing, tool access, model/configuration або реалізацію gate. Наступне спостереження підтверджує, чи action справді виконано й мало потрібний ефект.\nArchitect визначає enforced boundary, permissions, isolation, telemetry, decision rights, ефективні actuators, час реакції та fallback capacity. Prompt або probabilistic semantic detector сам собою не є Hard Constraint. Прямий deterministic gate може давати scoped hard claim тільки з перевіреним complete path та явними припущеннями. Developers реалізують і тестують paths; QA перевіряє bypass, degradation, false blocks і recovery; operational owner має повноваження та runbook.\nProject Manager планує operational ownership, rehearsal і залежності, а не закриває проект після deploy. Зміна в межах delivery authority допускає локальну корекцію; розширення tool authority, population чи invalidated business/control assumptions повертається до project reauthorization. Автоматичне відхилення/rollback не повинно непомітно розширювати повноваження.\nАрхітектор проектує, де саме дозволена невизначеність і де рішення має бути enforced до наслідку. Для IT-асистента можна дозволити різні пояснення approved knowledge, але окремо перевіряти tool authority, доступ до даних та обов’язкове approval. Синтаксичний validator не доводить правильність змісту, а semantic evaluator також помиляється. Закритий feedback loop не є автоматично доказом безпеки: оцінка може бути неправильною, реакція запізнілою, а actuator — недієвим.\nДо архітектурної відповідальності входять vendor/model changes, isolation boundaries, telemetry та конфігураційний rollback. Provider abstraction відокремлює контракт застосунку від конкретного API, але заміна provider не зберігає поведінку автоматично: потрібні нові evidence та рішення у відповідному scope. Human-in-the-loop означає людину з контекстом, повноваженнями, компетентністю, часом і пропускною здатністю, а не кнопку approve.\nДля кожного material signal визначаємо допустимий час реакції й спостережуваний ефект корекції. Якщо шкода може настати раніше, ніж надійде feedback, потрібний придатний попередній gate, менша authority або відмова від такого шляху. Fallback — конкретний режим: approved static guidance, ручний support або зрозуміла відмова, з перевіреною місткістю. Він має зменшувати наслідки, а не повторювати ту саму неперевірену генерацію під іншою назвою.\nАрхітектурне veto — обґрунтований висновок, що в даному scope немає достатнього контролю, evidence, економіки чи operational capacity. Архітектор документує цей висновок і вимагає звуження, redesign або зупинки відповідно до призначених decision rights. Це не довільне одноосібне право розширювати бізнес-політику. Уповноважений project owner приймає рішення про життєздатність і можливе подальше bounded research.\n\nHuman-in-the-loop є архітектурною залежністю сам по собі, а не фразою «людина перевірить». Потрібні призначені люди, компетентність, контекст для рішення, доступність, реальне право зупинити або змінити роботу, робочий інструмент, response time, звичайна й пікова пропускна здатність, підміна та режим при перевантаженні. Людина не обов’язково схвалює кожний запит: політика визначає точки та умови участі. На схемі люди беруть участь у Controller / authority, а також можуть виконувати дію. Повний контур пов’язує approved limits з Observe, Decide/authorize, Apply correction та наступним спостереженням за ефектом. Permission gate перед tool execution зберігає власну fail-closed поведінку. Окремо від цього повнота зворотного зв’язку не доводить коректність semantic evaluator або стабільність системи. Якщо навантаження, latency чи human-review demand неможливо надійно оцінити до запуску, архітектор має визначити гіпотезу та спершу перевірити доступні sandbox/shadow варіанти. Обмежений canary у production припустимий лише за окремим дозволом, в допустимій області ризику, з реально працюючими sensors, authority, stop/fallback, обмеженням population, duration, tools, spend та швидкості exposure. Canary не замінює архітектуру й не виправдовує порушення hard prohibition. Якщо немає дієвого керування або допустимого способу виміряти ризик, AI path слід заблокувати, звузити чи відкласти. Невизначеність також надходить з економіки та зовнішнього провайдера: ціна токенів, потреба в повторних викликах та evaluations, вартість human review, latency, доступність, непрозорі зміни model weights/routing/configuration можуть змінити поведінку та unit economics без локального коміту. Це можливі джерела змін, а не твердження, що кожний провайдер змінює все без попередження. Provider abstraction ізолює інтеграцію, але не доводить поведінкову еквівалентність моделі-замінника. Для змін потрібні спостереження, повторна оцінка та можливість rollback/disable/manual fallback в межах повноважень. Архітектор формує інженерний висновок про життєздатність, Product та уповноважені бізнес-особи погоджують допустимий ризик, а PM забезпечує operational model і залежності.\n\nІнтеграція старих слайдів 14 та 15 (PDF pages 15–16): Designing Stochastic Resilience і System Boundary States. Верхня схема робить containment видимим: model proposal → semantic monitor → controller / enforcement → дозволений delivery або execution. Approved limits є reference; semantic monitor є fallible Sensor; Decide + enforce об’єднує на навчальній схемі рішення Controller та реалізацію gate, а не ототожнює їх у доктрині. Детермінований permission/approval check перед tool execution зберігається. При порушенні або недоступному критичному контролі stop/isolate переводить запит у наперед визначений fallback: актуальна затверджена cached answer, safe template, human review або зрозуміла відмова. Cache не є автоматично безпечним: його доступність, актуальність, контекст і права також перевіряються. Якщо навіть fallback непридатний, потрібна відмова чи зупинка, а не мовчазне виконання. Semantic monitor не гарантує виявлення всіх небезпечних змістів.\nObserve збирає delivery outcomes, fallback outcomes, наслідки застосованої корекції, incidents і здоров’я самого контуру; зворотний зв’язок запускає уповноважений review, корекцію rules/configuration/versions та наступну перевірку ефекту. Інциденти оновлюють Golden Set / regression, prompts за потреби, критерії Eval Gates, monitoring thresholds і escalation policy у межах повноважень. Це розвиток існуючих контролів, не обов’язково новий окремий сервіс. Human authority є частиною Controller/approval та може виконувати Actuator; нижній рядок залишає власника, контекст, час, місткість і підміну як реальні архітектурні залежності.\nПраворуч видно три джерела невизначеності зі старого слайда: latency overhead від перевірок та ескалації; економіка token / retry / evaluation / human-review cost; непрозорі provider-side зміни моделі чи routing, що можуть змінювати поведінку без local code commit. Їхній спільний ефект може зробити систему непридатною у заданому scope. Архітектор формує обґрунтований veto-висновок і передає рішення про звуження/redesign/зупинку уповноваженому власнику. Критична обов’язкова заборона не обмінюється на економічну вигоду. Невідоме навантаження можна досліджувати в обмеженому дозволеному canary тільки з уже працездатним control path, stop/fallback, власниками, ресурсними та exposure limits. Canary не легалізує відсутність керування. Попередні схеми IT-assistant action path, повний контроль та всі застереження збережені в попередніх нотатках.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/control-loop-anatomy.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/nested-control-lifecycle.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/01-patterns/thinking-system-review.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=10",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=11",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=15",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=16",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=18"
  ],
  "architectureHeading": "THREE PRESSURES → VETO",
  "architecture": [
    "Token prices + control cost",
    "Opaque provider changes",
    "Latency + fallible evaluators"
  ],
  "veto": "Control or viable operation missing?\nNarrow, redesign or stop this AI path.",
  "humanHeading": "HUMAN IN THE LOOP IS AN ARCHITECTURAL DEPENDENCY",
  "humanDetail": "Owner + authority + context + response time + peak capacity + backup",
  "trialRule": "Unknown load: authorized canary only with working controls, exposure limits and stop criteria.",
  "trialLimits": "Canary limits exposure. If the control path is missing, block the AI path.",
  "flowHeading": "RUNTIME CONTAINMENT + FEEDBACK",
  "runtime": [
    "Model\nproposal",
    "Semantic\nmonitor",
    "Decide +\nenforce gate",
    "Deliver /\nexecute"
  ],
  "stop": "Stop / isolate",
  "fallback": "Safe template / valid cache\nHuman review / clear refusal",
  "observe": "Observe\n+ verify effects",
  "feedback": "Review + authorize corrections → update rules / versions → re-evaluate effects",
  "pressures": [
    [
      "Latency overhead",
      "Checks + escalation consume time."
    ],
    [
      "Token / review cost",
      "Price or call volume breaks economics."
    ],
    [
      "Opaque vendor changes",
      "Model behavior can change remotely."
    ]
  ]
}
```

**Час:** 3:00.

**Композиція:** Збережено tool path, permission gate, approved limits і замкнений Observe → Decide/authorize → Apply correction. У Controller явно присутні люди. Окремо — HITL як архітектурна залежність, token/control cost, opaque provider changes, latency та fallible evaluation. Умови bounded trial не дозволяють запуск без керуючого контуру.

**Рольова зміна:** Architect визначає boundary, complete enforcement path, assumptions, sensing, authority та effective correction. Developers реалізують, QA перевіряє degradation/bypass/recovery, operational owner діє; Project Manager планує ownership і capacity. Це scoped example, а не універсальний deployment diagram або гарантія всіх semantic outputs.

**Перехід:** «Такий продукт потребує іншого наповнення командного процесу, а не лише нового компонента в архітектурі».

**Поглиблення змісту:** До попереднього operational loop додаємо vendor/model changes, isolation, реальну human-response capacity та fallibility semantic checks. Окремо видно підставу звузити або зупинити AI path, якщо control/economics не підтверджені; у нотатках — reaction time та обмеження feedback.


**Уточнення 22 вересня:** Human-in-the-loop є архітектурною залежністю сам по собі, а не фразою «людина перевірить». Потрібні призначені люди, компетентність, контекст для рішення, доступність, реальне право зупинити або змінити роботу, робочий інструмент, response time, звичайна й пікова пропускна здатність, підміна та режим при перевантаженні. Людина не обов’язково схвалює кожний запит: політика визначає точки та умови участі. На схемі люди беруть участь у Controller / authority, а також можуть виконувати дію. Повний контур пов’язує approved limits з Observe, Decide/authorize, Apply correction та наступним спостереженням за ефектом. Permission gate перед tool execution зберігає власну fail-closed поведінку. Окремо від цього повнота зворотного зв’язку не доводить коректність semantic evaluator або стабільність системи. Якщо навантаження, latency чи human-review demand неможливо надійно оцінити до запуску, архітектор має визначити гіпотезу та спершу перевірити доступні sandbox/shadow варіанти. Обмежений canary у production припустимий лише за окремим дозволом, в допустимій області ризику, з реально працюючими sensors, authority, stop/fallback, обмеженням population, duration, tools, spend та швидкості exposure. Canary не замінює архітектуру й не виправдовує порушення hard prohibition. Якщо немає дієвого керування або допустимого способу виміряти ризик, AI path слід заблокувати, звузити чи відкласти. Невизначеність також надходить з економіки та зовнішнього провайдера: ціна токенів, потреба в повторних викликах та evaluations, вартість human review, latency, доступність, непрозорі зміни model weights/routing/configuration можуть змінити поведінку та unit economics без локального коміту. Це можливі джерела змін, а не твердження, що кожний провайдер змінює все без попередження. Provider abstraction ізолює інтеграцію, але не доводить поведінкову еквівалентність моделі-замінника. Для змін потрібні спостереження, повторна оцінка та можливість rollback/disable/manual fallback в межах повноважень. Архітектор формує інженерний висновок про життєздатність, Product та уповноважені бізнес-особи погоджують допустимий ризик, а PM забезпечує operational model і залежності.

**Уточнення за старими слайдами 14–15 (PDF pages 15–16):** Native runtime flow розгалужується після порівняння/дозволу на delivery або stop/isolate → safe fallback/human review/refusal; спостереження запускає дозволену корекцію й повторну перевірку. Праворуч latency, token/review economics і opaque vendor changes ведуть до narrow/redesign/stop. HITL лишається архітектурною залежністю, canary потребує вже працездатних controls.

## 13. The Roles Move With the System

```pptx-slide
{
  "number": 13,
  "layout": "roles",
  "role": "PROJECT MANAGER · the scope of management expands",
  "steps": [
    "Hypothesis",
    "Bounded trial",
    "Evidence",
    "Decision"
  ],
  "cycle": "Adapt or stop; production evidence feeds the next iteration.",
  "table": [
    [
      "HORIZON",
      "WHAT THE PM MUST UNDERSTAND",
      "WHAT THE PM WATCHES"
    ],
    [
      "AI-assisted SDLC",
      "Generation moves bottlenecks.\nRebalance review, QA and ownership.",
      "Lead time, review queues, rework,\nstability + retained understanding"
    ],
    [
      "Thinking Systems",
      "An added engineering discipline:\nrequirements, evals and control design.\nPeople + authority are system dependencies.",
      "Outcome frequency + severity,\ncost / latency, human workload"
    ],
    [
      "Operating model",
      "Changed roles, evidence and decision rights.\nFind gaps in process and team organization.",
      "Coverage, response time, control health,\nincidents + decisions to reassess"
    ]
  ],
  "takeaway": "Progress = working capability + reduced uncertainty + explicit decisions.",
  "notes": "Стара презентація Designing Non-Deterministic Systems, slide 20 Welcome to the Laboratory, дає педагогічну метафору Hypothesize → Measure → Adapt. Тут не стверджуємо, що Scrum або попередня інженерія не були емпіричними. Процес додає явно керований цикл поведінкових гіпотез, measurement та адаптації поряд зі звичайним delivery. Titles/order цієї 14-slide доповіді збережено.\nProject Manager відрізняється від Product Manager. Product разом із BA та бізнесом уточнює цінність, наслідки й acceptance; Project Manager організовує delivery і навчання: stakeholder availability, dependencies, доступ до даних/domain experts, evaluation cost, час на аналіз і remediation, decision latency, release/operations readiness. Він не стає одноосібним власником risk acceptance.\nPlanning: backlog містить не тільки features, а й перевірювані невідомі, наприклад «чи достатньо approved knowledge для типових support cases?». Для trial фіксуємо питання, hypothesis, evidence plan, ресурсну межу, owner і stop condition; якщо треба — погоджений обмежений scope до остаточних tolerance. Sprint review: разом зі working software показуємо versioned evidence, проблемні групи, consequences, uncertainty та unresolved decisions. Результат може бути accept, redesign, narrow, bounded further trial або stop. Це корисний результат роботи, а не автоматична невдача спринту, якщо доказано, що задум нежиттєздатний.\nRelease/operate: окремо від Done підтверджуємо authorization конкретного rollout, monitoring, on-call/ручний шлях і їхню місткість; runtime evidence повертає backlog і за потреби project reauthorization. Не рахувати кількість проведених експериментів як цінність саму по собі: прогрес — робоча capability, зменшення матеріальної невизначеності та прийняте рішення. Один живий review artifact і звичні командні події можуть містити ці записи; не потрібні нові ролі або комітет.\nРозподіл 9–13: Product + BA формулюють acceptance; QA + Developers роблять measurement; Developers доставляють evidence/recovery package; Architect замикає bounded control; Project Manager координує весь цикл, рішення, бюджет і залежності.\nФабрика й лабораторія співіснують. Команда продовжує постачати перевірені deterministic features, але для поведінкових невідомих спочатку формулює гіпотезу й план evidence. Робочий приклад: «Чи достатньо approved knowledge, щоб асистент корисно обробляв типові IT-звернення без вигаданих кроків у допустимих межах вартості та затримки?». Експеримент може показати, що потрібні нові знання, інший scope, ручний support або взагалі інше технічне рішення.\nProject Manager закладає в план підготовку даних, час domain experts, evaluation runs, аналіз, реалізацію controls і rehearsal. Фіксує resource/time box дослідження та decision date. Можна погодити термін отримання evidence й рішення, але не видавати невідому feasibility за гарантовану production capability. Після trial команда уточнює прогноз, scope і залежності; це кероване перепланування за новими даними.\nНа planning розділяємо work із відомим способом реалізації та material unknowns. На sprint review поряд із demo показуємо baseline/candidate, проблемні сценарії, cost/latency, evaluator uncertainty і рішення. На retrospective перевіряємо, які припущення та засоби вимірювання підвели. Production incidents повертаються в Golden Set, backlog і review тієї межі, яка виявилася неадекватною. Звичайні Scrum events можуть бути цими контрольними точками без створення окремої бюрократії.\nНегативний експеримент є корисним, коли він закриває важливе питання й змінює рішення, а не просто збільшує лічильник проведених дослідів. Кількість tickets, LOC або красивих demo окремо не описує готовність до відповідальної експлуатації.\n\nЦе синтез попередніх слайдів у портрет майбутнього Project Manager, а не нова назва Product Manager. Фундамент не зникає: project management theory, планування, ризики, залежності, бюджет, комунікації, stakeholders і delivery залишаються. До нього додаються горизонти, що співіснують. Перший — AI-assisted SDLC. Кодогенерація змінює співвідношення швидкості створення, review, QA, integration та людського розуміння. PM має розуміти систему, якою керує, бачити зміну bottleneck і разом із командою знаходити новий баланс. Ми не знаємо універсального нового equilibrium наперед: його перевіряємо end-to-end flow, review queues, rework, stability та здатністю людей пояснити й відновити систему. Другий — побудова агентних/Thinking Systems як додаткова інженерна дисципліна: probabilistic judgment є частиною runtime, тому requirement, evaluation, control design та operating model стають частиною проєктованої системи. Люди з їхніми правами, компетенціями, latency й capacity входять до її інженерного периметра. Третій — управління цією роботою: PM розуміє, як змінилися завдання Product/BA, QA, developers і architect, хто виробляє докази, хто приймає рішення, хто вміє застосувати корекцію. PM має бачити пропущені функції, нерозв’язані залежності та неузгоджений поділ відповідальності, принаймні робити їх видимими, організовувати рішення й моніторити стан. Потрібна статистична грамотність: відрізняти частоту від наслідку, точкову оцінку від невизначеності, coverage від кількості повторів, sample від production population, correlation від causality. Це не робить PM одноосібним статистиком, QA, архітектором або власником бізнес-ризику. Практичні метрики доповнюють delivery: частка неприйнятних результатів за сценаріями та тяжкістю, task success за погодженим rubric, cost per accepted outcome, latency, частка і черга ескалацій, response time, доступність контролів, результативність stop/fallback, incident recurrence. Вони мають denominators, період, сегмент, active version, межу та owner реакції. Система не стає коректною через один aggregate score. Попередній цикл Hypothesis → Bounded trial → Evidence → Decision залишається механікою: у planning визначаємо evidence gap, бюджет, owner і stop condition; на review приймаємо рішення з Product/BA, QA, Dev та Architect; після release стежимо за authorization і capacity. Приклад trial для IT-асистента: чи може він використовувати затверджені знання без вигаданих кроків. Дослідження обмежене в часі до обіцянки production capability. Прогрес — working capability, reduced uncertainty та явні рішення.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/01-patterns/thinking-system-review.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/nested-control-lifecycle.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=20"
  ],
  "process": "Delivery now includes experiments, evaluation time and decisions about feasibility.",
  "trial": "Trial: can approved knowledge answer routine cases without unsupported steps?",
  "planningRule": "Time-box the investigation before promising production capability.",
  "foundation": "Project management theory still matters: scope, schedule, cost, risk and stakeholders.",
  "statisticalLiteracy": "Statistical literacy: question sampling, uncertainty, thresholds and the strength of evidence.",
  "roleBoundary": "Coordinate specialists and business owners. Make missing evidence and control capacity visible."
}
```

**Час:** 2:00.

**Композиція:** Фундамент project management зверху, під ним native table трьох горизонтів: AI-assisted SDLC, Thinking Systems та operating model. Поруч із кожним — що PM має розуміти та що спостерігати. Унизу статистична грамотність і координація спеціалістів; попередні planning/review/operations checkpoints розгорнуті в нотатках.

**Project Manager:** координує learning loop поряд із delivery: evidence gaps, stakeholders, dependencies, experiment cost/time, decision latency та operational capacity. Product Manager відповідає за продуктову сторону домовленості, це інша функція. Working capability + reduced uncertainty + explicit decisions — видимий прогрес. Відкрите питання має owner і наступну дію.

**Зв’язок зі старою презентацією:** надана Designing Non-Deterministic Systems, slides 17–20, особливо Welcome to the Laboratory. Зберігаємо емпіричний цикл, уточнюємо старі метафори: Scrum вже емпіричний, ризик не належить автоматично лише PM, один aggregate score не доводить safety. Новий headcount або новий комітет не потрібні.

**Перехід:** «Ролі й процес повертають нас до двох змін із першого слайда».

**Поглиблення змісту:** Зберігаємо цикл і всі checkpoints Project Manager. Додаємо конкретне питання для trial, планування evaluation time і feasibility decisions, а також обмежений час дослідження до обіцянки production capability. У нотатках — planning, review, retrospective та повернення incidents у backlog.


**Уточнення 22 вересня:** Це синтез попередніх слайдів у портрет майбутнього Project Manager, а не нова назва Product Manager. Фундамент не зникає: project management theory, планування, ризики, залежності, бюджет, комунікації, stakeholders і delivery залишаються. До нього додаються горизонти, що співіснують. Перший — AI-assisted SDLC. Кодогенерація змінює співвідношення швидкості створення, review, QA, integration та людського розуміння. PM має розуміти систему, якою керує, бачити зміну bottleneck і разом із командою знаходити новий баланс. Ми не знаємо універсального нового equilibrium наперед: його перевіряємо end-to-end flow, review queues, rework, stability та здатністю людей пояснити й відновити систему. Другий — побудова агентних/Thinking Systems як додаткова інженерна дисципліна: probabilistic judgment є частиною runtime, тому requirement, evaluation, control design та operating model стають частиною проєктованої системи. Люди з їхніми правами, компетенціями, latency й capacity входять до її інженерного периметра. Третій — управління цією роботою: PM розуміє, як змінилися завдання Product/BA, QA, developers і architect, хто виробляє докази, хто приймає рішення, хто вміє застосувати корекцію. PM має бачити пропущені функції, нерозв’язані залежності та неузгоджений поділ відповідальності, принаймні робити їх видимими, організовувати рішення й моніторити стан. Потрібна статистична грамотність: відрізняти частоту від наслідку, точкову оцінку від невизначеності, coverage від кількості повторів, sample від production population, correlation від causality. Це не робить PM одноосібним статистиком, QA, архітектором або власником бізнес-ризику. Практичні метрики доповнюють delivery: частка неприйнятних результатів за сценаріями та тяжкістю, task success за погодженим rubric, cost per accepted outcome, latency, частка і черга ескалацій, response time, доступність контролів, результативність stop/fallback, incident recurrence. Вони мають denominators, період, сегмент, active version, межу та owner реакції. Система не стає коректною через один aggregate score. Попередній цикл Hypothesis → Bounded trial → Evidence → Decision залишається механікою: у planning визначаємо evidence gap, бюджет, owner і stop condition; на review приймаємо рішення з Product/BA, QA, Dev та Architect; після release стежимо за authorization і capacity. Приклад trial для IT-асистента: чи може він використовувати затверджені знання без вигаданих кроків. Дослідження обмежене в часі до обіцянки production capability. Прогрес — working capability, reduced uncertainty та явні рішення.

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
  "takeaway": "The learning cycle continues after release. The team remains accountable.",
  "closing": "More capability still requires engineering responsibility.",
  "titleLines": [
    "Engineering Rigor Moves —",
    "It Doesn’t Disappear"
  ],
  "notes": "Повертаємо HOW і WHAT із першого слайда, тепер із конкретними ролями й процесом. HOW: швидше створювати код недостатньо — команда зберігає comprehension та ownership, Project Manager організовує flow, evidence, залежності та рішення. Малими партіями й обмеженими експериментами перевіряємо невідомі. WHAT: Product + BA узгоджують acceptance з бізнесом; QA + Developers створюють калібровані докази й реалізацію; Architect проектує ефективні control paths; уповноважений release owner приймає scope і residual risk у своїх межах. Це розширення, а не вичерпні нові job descriptions або передача відповідальності одній ролі.\nГоловна зміна процесу: hypothesize → measure → decide → adapt, з робочим software, явними business outcomes і runtime feedback. Детерміновані requirements, tests та delivery discipline залишаються; додається контроль варіативної поведінки і наслідків. Немає нових чисел, нової архітектурної нормативності чи реклами UA.\nФінал: «AI розширює наші можливості. Команда все одно відповідає за систему цілком: як ми її будуємо, яку поведінку дозволяємо, на яких доказах випускаємо і як виправляємо відхилення». Пауза, Q&A.\nКонкретний перший крок для команди: обрати один AI workflow із реальним бізнес-наслідком. Узгодити корисний результат, дозволену варіативність, неприйнятні наслідки, cost/latency та escalation. Підготувати невеликий початковий Golden Set із domain experts, перевірити evaluator й розширювати evidence відповідно до рішення та ризику, без універсального мінімального sample size. Зв’язати Eval Gate з дозволеним block/canary/release, перевірити fallback і людину, яка зможе діяти.\nСаме тут поєднуються дві половини доповіді. HOW: команда має розуміти реалізацію, докази, обмеження і способи відновлення навіть за великого обсягу AI-generated code. WHAT: оскільки частина поведінки формується під час роботи, специфікація, тестування і відповідальність продовжуються через runtime evidence та контроль. Відповідальність не переноситься на модель або на одного QA; вона проходить через узгоджені boundaries, evidence, authority і реальну здатність змінити роботу системи.\n\nФінал збирає HOW we build та WHAT we build через лабораторний цикл зі старого слайда 20. Звичний delivery cycle Plan → Build → Verify → Ship залишається. Лабораторний цикл додає гіпотезу, обмежений експеримент, вимірювання, рішення й адаптацію; нові дані повертають команду до наступної гіпотези. Scrum уже містить емпіризм та адаптацію, тому ми не оголошуємо їх винаходом AI. Змінюється те, що саме треба вимірювати й керувати: поведінкова варіативність, доказова база, operational control і людська частина системи. Для HOW we build цей підхід потрібен, поки команда перевіряє, як AI code generators змінюють її звичний SDLC, де виник bottleneck, чи є реальне покращення end-to-end delivery та чи зберігаються understanding/ownership. Порівнюємо сумісні типи задач і умови, не приймаємо більше generated lines за delivery improvement. Для WHAT we build — Thinking Systems — цикл триває весь час роботи, бо змінюються входи, usage, дані, поведінкові конфігурації та зовнішні залежності. Production evidence й incidents оновлюють Golden Sets, regression, Eval Gates, monitoring та рішення про scope. «Лабораторія не закінчується» означає постійне навчання й reassessment, а не безперервні неконтрольовані експерименти над користувачами: кожний trial має дозвіл, межі та stop/fallback. З попереднього HOW/WHAT лишаються всі відповідальності: команда — comprehension та ownership; Project Manager — evidence і flow; Product/BA — agreed acceptance; QA/Dev — calibrated evidence; Architect — effective control paths; release owner — scope та residual risk. Перший практичний крок лишається: один workflow, погоджені tolerances, калібрований Golden Set, Eval Gate і відрепетируваний fallback. Оцінюємо рішення та наслідки, не лише демонстрацію. Більше capability не скасовує engineering responsibility.",
  "firstStepHeading": "START WITH ONE WORKFLOW",
  "firstStep": "Agree tolerances, calibrate a Golden Set, connect an Eval Gate and rehearse the fallback.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=22"
  ],
  "factoryHeading": "DELIVERY CONTINUES",
  "factoryFlow": "Plan → Build → Verify → Ship",
  "factoryDetail": "Scope, quality, cost and schedule\nremain part of the job.",
  "labHeading": "THE LABORATORY STAYS OPEN",
  "labDetail": "Evidence reopens assumptions.\nRelease feeds the next experiment.",
  "labSteps": [
    "Hypothesize\n+ bounded trial",
    "Measure",
    "Decide",
    "Adapt"
  ],
  "loopCenter": "Production evidence\nreturns to the team",
  "applications": [
    [
      "HOW WE BUILD · while AI changes the SDLC",
      "Measure flow, rework, stability and the team’s retained understanding."
    ],
    [
      "WHAT WE BUILD · throughout Thinking Systems operation",
      "Measure outcomes, control capacity and cost. Incidents revise tests and control rules."
    ]
  ]
}
```

**Час:** 3:00.

**Композиція:** Ліворуч звичний delivery cycle та пояснення постійної лабораторної роботи. Праворуч замкнений native цикл Hypothesize + bounded trial → Measure → Decide → Adapt, із production evidence всередині. Унизу два застосування: HOW для пошуку балансу AI-assisted SDLC і WHAT для всього часу роботи Thinking Systems.

**Фінал:** «AI розширює наші можливості. Команда все одно відповідає за систему цілком: як ми її будуємо, яку поведінку дозволяємо, на яких доказах випускаємо і як виправляємо відхилення».

Детерміновані вимоги, тести та звичайні обов’язки не зникають. Без нових даних чи рекламного фіналу. Пауза, Q&A.


**Поглиблення змісту:** Поряд із збереженим HOW / WHAT додаємо практичний старт на одному workflow: tolerances, calibrated Golden Set, Eval Gate і rehearsed fallback. Це збирає зміни ролей у спільну роботу команди.

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


**Уточнення 22 вересня:** Фінал збирає HOW we build та WHAT we build через лабораторний цикл зі старого слайда 20. Звичний delivery cycle Plan → Build → Verify → Ship залишається. Лабораторний цикл додає гіпотезу, обмежений експеримент, вимірювання, рішення й адаптацію; нові дані повертають команду до наступної гіпотези. Scrum уже містить емпіризм та адаптацію, тому ми не оголошуємо їх винаходом AI. Змінюється те, що саме треба вимірювати й керувати: поведінкова варіативність, доказова база, operational control і людська частина системи. Для HOW we build цей підхід потрібен, поки команда перевіряє, як AI code generators змінюють її звичний SDLC, де виник bottleneck, чи є реальне покращення end-to-end delivery та чи зберігаються understanding/ownership. Порівнюємо сумісні типи задач і умови, не приймаємо більше generated lines за delivery improvement. Для WHAT we build — Thinking Systems — цикл триває весь час роботи, бо змінюються входи, usage, дані, поведінкові конфігурації та зовнішні залежності. Production evidence й incidents оновлюють Golden Sets, regression, Eval Gates, monitoring та рішення про scope. «Лабораторія не закінчується» означає постійне навчання й reassessment, а не безперервні неконтрольовані експерименти над користувачами: кожний trial має дозвіл, межі та stop/fallback. З попереднього HOW/WHAT лишаються всі відповідальності: команда — comprehension та ownership; Project Manager — evidence і flow; Product/BA — agreed acceptance; QA/Dev — calibrated evidence; Architect — effective control paths; release owner — scope та residual risk. Перший практичний крок лишається: один workflow, погоджені tolerances, калібрований Golden Set, Eval Gate і відрепетируваний fallback. Оцінюємо рішення та наслідки, не лише демонстрацію. Більше capability не скасовує engineering responsibility.
