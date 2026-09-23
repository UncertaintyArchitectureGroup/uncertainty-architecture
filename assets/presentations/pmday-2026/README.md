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
## Детальний сценарій 14 змістовних слайдів і завершального слайда з ресурсами

Дата перевірки джерел: 21 вересня 2026 року. Центральний опис і редаговані дані для PPTX; артефакт залишається review candidate.

**[Evidence base — звіти й зовнішні посилання](EVIDENCE.md):** використані редакції, прив'язка до слайдів, обмеження, історичний контекст і матеріали Subprime / UA.

### Зафіксовані слайди 1–11

За прямим запитом maintainer від 21 вересня 2026 року, після пояснення GitClear на слайді 4, **слайди 1–8 зафіксовано**. Не змінювати їхній зміст, числа, нотатки, геометрію, оформлення або спільні ресурси, що впливають на них, без наступного явного запиту maintainer на відповідні слайди. Наступний явний запит maintainer дозволив лише заміну шрифту на Roboto на всіх 14 слайдах; після повторного огляду запис захисту оновлено. Прямий запит від 22 вересня 2026 дозволяє додати графічне пояснення лише до слайда 8 за слайдом 3 старої презентації. Після перевірки його baseline оновлюється; слайди 1–7 незмінні, захист 1–8 надалі діє. Цей запит також дозволяє переробити 9–10 за наданими схемами. Наступний прямий запит 22 вересня дозволяє змінити тільки шрифт усіх 14 слайдів на стандартний міжплатформний Arial і доповнити 9, 11 та 12 за старими слайдами 16, 5, 14–15 відповідно (нумерація без обкладинки). Зміст, числа, нотатки й геометрія 1–8 залишаються захищеними; font-only baseline оновлюється після перевірки.

**Поточна межа захисту — слайди 1–11.** Наступним прямим запитом від 22 вересня 2026 maintainer погодив їхній поточний вигляд і розширив freeze з 1–8 до 1–11. Зміст, числа, нотатки, оформлення, геометрію, chart data та спільні ресурси цих слайдів можна змінювати лише за наступним явним запитом. Слайди 12–15 лишаються відкритими для роботи. Прямий запит 23 вересня дозволяє вузькі зміни захищених 1 (представлення й контакти) та 11 (DoR/DoD), а також переробку 12–14 і новий ресурсний 15. Слайди 2–10 та їхні залежності залишаються точними; після перевірки 1 і 11 знову входять до захищеної бази.

Прямий наступний запит 23 вересня 2026 на критичний перегляд зв’язності й залучених ролей дозволяє зміни другої частини, слайдів 8–14. У v14 уточнено відповідальності та переходи на 8–14; зміни захищених 8–11 переглядаються й записуються вузько. Слайди 1–7, ресурсний 15, усі назви й порядок та числові дані залишаються точними. Захист 1–11 зберігається після перевірки.

Прямий запит «Виправ» після змістовного review від 23 вересня 2026 авторизує v15: зменшення екранної щільності 4, наскрізний IT-assistant case на 8–12, pre-action permission/approval на 12, конкретні результати координації на 13 та пропорційність controls. Переглядаються лише 4 і 8–14. Назви, порядок, 1–3/5–7/15, попередні notes, числові дані та chart/workbook зберігаються; частина secondary evidence 4 переходить у notes. Freeze 1–11 оновлюється лише для дозволених 4/8–11 після огляду.

Пряме уточнення maintainer від 23 вересня 2026 авторизує v16 лише на 4/10/11/13: повернути двоколонковий 4, перевірити churn, виправити злитий chart label на 10, відновити statistical delivery contracts старого слайда на 11 та повернути на 13 обидва зсуви HOW/WHAT як причину еволюції ролей і operating model. Expertise gap лишається прикладом. Числа sample незмінні; у chart змінюються лише label text/style. Freeze 1–11 оновлюється після огляду лише для 4/10/11 та chart-label XML. Усі інші слайди й попередні notes збережено.

[frozen-slides.json](frozen-slides.json) зберігає контрольні суми секцій і нормалізованих частин PPTX разом із залежностями. Звичайна збірка/перевірка відхиляє розбіжність; автоматичного «перезаписати baseline» або bypass-прапорця немає. Оновлювати запис можна лише в межах явно замовленої зміни, з повторним оглядом захищених слайдів. Це захист від випадкового редагування, а не незалежне підтвердження особи, яка дозволила зміну.

**Основну структуру збережено:** ті самі 14 назв, той самий порядок і та сама драматургія. Прямим запитом від 23 вересня додано завершальний ресурсний слайд 15 із контактами й QR-кодами. Слайд 4 залишається спільним evidence slide. Слайди 5–7 — comprehension, відповідальність команди та пошук нового SDLC equilibrium, а не окремі слайди про звіти.

Головна дуга: технологічний зсув → HOW we build → дисбаланс SDLC → WHAT we build → Thinking Systems → requirements, QA, release, production і ролі → engineering rigor переходить у нові місця, а не зникає.

Таймінг: 38 хвилин + 2 хвилини резерву. Повноцінне Q&A — окремо. Англійська — для заголовків і коротких екранних формулювань; українська — для пояснень і виступу.


### Критичний перегляд v14: одна спільна система рішень

Поточний перегляд 23 вересня 2026 зберігає драматургію, числа й історію попередніх notes. Друга частина більше не читається як ізольовані «слайди для BA / QA / архітектора»: кожний етап пов’язаний із сусіднім через результат і decision owner. Назви ролей позначають відповідальності, які можуть поєднувати наявні люди; це не вимога нових посад.

| Слайд | Кого стосується й що змінюється |
|---|---|
| 8 | Product / PO, BA, Project Manager, engineering, QA, operations: спільний перехід від генерації коду до runtime judgment |
| 9 | Product Manager / Product Owner — value і пріоритети; BA — testable contract; Project Manager — stakeholder decisions і dependencies; business / risk owner — дозволені межі |
| 10 | QA / Dev + domain experts — evidence; Product / PO + BA — interpretation against limits; Project Manager — evidence readiness; authorized owner — release decision |
| 11 | PO / BA / Dev / QA / Project Manager / operations — спільні readiness і completion; release owner і service owner мають різні рішення |
| 12 | Architect / Dev — control path; QA — його перевірка; service owner — дієздатність у production; Product / risk owner — boundaries; Project Manager — залежності |
| 13 | Project Manager з’єднує обидва горизонти й власників рішень, не підмінюючи їхню предметну authority |
| 14 | Спільний цикл із явними учасниками planning, daily work, review та operations; один практичний перший крок |

Переходи: **новий об’єкт → погоджений контракт → evidence → readiness/completion/release → здійсненний контроль → delivery dependencies → постійний цикл навчання**. Це порядок пояснення, а не waterfall: архітектура, експлуатація й оцінювання проектуються разом. Продуктова користь перевіряється поряд із допустимістю ризику; Golden Set не видається за репрезентативну production-вибірку. PO не оголошується одноосібним власником DoD або довільного business risk. У Scrum DoD та емпіризм мають чинне значення; DoR — можлива практика команди, а Sprint Review не є release gate.

Першу частину перевірено без зміни зафіксованих 1–7. Її головний презентаційний ризик — щільність evidence на 4: у виступі варто провести аудиторію через кілька основних контрастів, а не зачитувати всі числа. На 3 і 5 треба озвучити позначену сценарність; різнорідні дослідження на 4 не доводять одну універсальну причинну величину. Ці обмеження вже присутні в джерелі й notes; емпіричних тверджень не розширено.

### Уточнення v15: рішення на одному прикладі

IT-асистент допомагає відновити доступ: 8 визначає outcome, 9 — контракт поведінки, 10 — evidence із забороненою disclosure, 11 — наслідок для candidate / release, 12 — permissions та required approval до виконання, а також control feedback після дії. Цей приклад ілюстративний, 200 відповідей не є production measurement. 13 показує результати координації PM, 14 завершує конкретним першим workflow. Pre-action checks і post-action feedback мають різні задачі; незворотний disclosure не виправляється rollback. Обсяг контролю залежить від consequence, authority і reversibility.

На 4 залишено три основні evidence contrasts; додаткові METR / Agarwal / Xu, DORA perceptions та арифметичні пояснення GitClear збережено в notes і попередньому source. Числа й методологічні caveats не переглядаються. Таблиця ролей v14 вище лишається чинною; у v15 екранний пріоритет мають їхні рішення та результати. Попередні notes збережено як точні prefixes; нове поточне пояснення наприкінці розв’язує застарілі описи композиції.

### Уточнення v16: відновлена ширина аргументу

4 повертає попередню композицію з усіма visible evidence blocks. 10 відділяє count від share явними дужками. 11 знову пояснює загальний перехід до statistical readiness/completion/release, з cost усередині умов, control/HITL і production feedback. 13 синтезує HOW + WHAT: зміни flow / bottlenecks і runtime product перетворюють ролі та operating model. PM має розуміти й відстежувати цей новий баланс, інтегрувати рішення й трекати нові dependencies; expertise gap є одним прикладом, а не головною тезою.

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
- Окремі зображення дозволені для прямо погодженої концептуальної ілюстрації та QR-кодів; інформаційні схеми й дані робити native tools. За запитом maintainer у поточній редакції дозволено три зображення: концептуальна imagegen-ілюстрація на слайді 1 (artwork/ai-two-roles.png) та два точні QR-коди репозиторіїв на слайді 15 (artwork/qr-ua.png і artwork/qr-subprime.png). Вони не є фоном або запеченими слайдами; тексти, числа й схеми залишаються нативними. Prompt, точні URL і походження — в artwork/PROVENANCE.md.
- Рівно 15 слайдів: початкові 14 із погодженими назвами й порядком та завершальний ресурсний слайд за запитом від 23 вересня. Статична версія самодостатня; анімації не є умовою розуміння.
- English screen copy; українські speaker notes. Notes містять пояснення, джерела та обмеження, а не інструкції верстальнику.
- Центральний MD — editable source; pptx-slide blocks нижче задають екранні формулювання/дані. Прозу та відповідний block оновлювати разом. PPTX — derived artifact, не друге джерело змісту.
- Слайди 11 і 13 мають справжні PowerPoint tables. Схема слайда 5 не видається за емпіричний графік.
- Після кожної збірки: structural/editability checks, freshness hashes, render усіх 15 слайдів і огляд кожного. Для цієї редакції додатково перевіряти експортований PPTX через незалежний LibreOffice → PDF/PNG: внутрішній preview генератора сам по собі не підтверджує переносимість. Валідатор не доводить visual quality.
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
  "notes": "Відділити AI для розробки від Model Judgment усередині продукту. Перше змінює виробництво software, друге — поведінку системи. Не починати з реклами UA чи anti-AI тези.\nІлюстрація показує конкретні ролі: зліва розробник працює з AI coding assistant, справа користувач просить продукт скласти план подорожі. AI-generated illustration, OpenAI imagegen, 21 September 2026. Вона не задає архітектуру системи. Prompt: artwork/PROVENANCE.md.\n\nПоточне уточнення 23 вересня 2026:\nКоротке представлення: Vitalii Oborskyi, Head of Delivery & PMO, автор Uncertainty Architecture. Контакти: oborskyivitalii@gmail.com та https://www.linkedin.com/in/vitaliioborskyi/. Основний вступ і дві лінії HOW / WHAT збережено.",
  "illustrationAlt": "Two concrete scenes: a developer uses an AI coding assistant; a user asks an AI-powered travel application to plan a trip.",
  "author": "Vitalii Oborskyi",
  "bio": "Head of Delivery & PMO · Author of Uncertainty Architecture",
  "email": "oborskyivitalii@gmail.com",
  "linkedin": "https://www.linkedin.com/in/vitaliioborskyi/"
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
  "notes": "NBER WP 35275: May 2026, revised September 2026; current official PDF downloaded 2026-09-21. Понад 500 тисяч GitHub developers; matched event study, не RCT. Попередні 17.3× / 2.8×, 79→86% та 18→31% належали старій редакції й замінені. Changed LOC = additions + deletions, не чисте зростання кодової бази.\nTable 6, друкована с.33 / PDF p.35, тижні 21–30: Autocomplete — LOC +234.3%, files +50.0%, commits +30.2%, PRs +18.3%, repos +11.9%, releases +9.0%. Sync — LOC +957.5%, files +265.0%, commits +153.2%, PRs +86.0%, repos +47.3%, releases +19.8%. Async — LOC +1254.9%, files +83.3%, commits +60.7%, PRs +68.5%, repos +19.2%; releases не оцінено окремо. Figure 1, друкована с.2 / PDF p.4: авторські округлені cumulative levels — LOC 25.5×, files 5.0×, commits 3.4×, PRs 2.7×, repos 1.8×, releases 1.3×. Арифметика за округленою Table 6: 1+(234.3+957.5+1254.9)/100=25.467; commits 1+(30.2+153.2+60.7)/100=3.441; releases 1+(9.0+19.8)/100=1.288. Не перемножувати компоненти і не видавати ці суми за точні raw-data estimates. Прочерк async releases не означає нульового ефекту.\nFigure 11, друкована с.44 / PDF p.46; §7.2, с.43–46: iOS нові apps/month приблизно 33–45 тисяч у 2023–early 2025 → 108 тисяч у квітні 2026; Android 42 тисячі у січні 2025 → 99 тисяч у mid-2026; Chrome приблизно семикратне зростання від 2023, що почалося до agentic era. SourceForge показує невелике зростання new projects і винесений у Figure OA-17, без надійної usage-панелі. Usage за перші 3 місяці: iOS cohort ratings приблизно стабільні; Android downloads помірно зростають, але значно повільніше за entry; Chrome downloads падають. Тому коректно «usage does not keep pace», а не «usage ніде не зростає».\n§7.2.3, друкована с.46 / PDF p.48: January 2025 → April 2026, частка iOS із <10 ratings приблизно 78% → 87%; Chrome із <10 downloads 19% → 33%; Android із ≤100 downloads приблизно 22% → 26%. Авторські цілі відсотки; не точні частки з raw data. Це порівняння нових когорт за перші 3 місяці, не всіх existing apps, не весь software market і не пряме вимірювання consumer welfare. Зміни часток приблизно +9/+14/+4 відсоткових пункти відповідно.\nDORA 2025 v.2025.2: повний звіт отримано через публічне дзеркало; source URL, license і SHA-256 записано в evidence/sources.json. Figure 28, p.38: software delivery instability має standardized estimate приблизно +0.10 SD, 89% credible interval приблизно +0.07…+0.13, на +1 SD AI adoption. Це округлене зчитування графіка, не точна опублікована числова таблиця. Векторні координати та арифметика — evidence/dora-2025-figure28.json. Footnote 23, p.48 визначає стандартизацію. Appendix p.139: instability об’єднує change failure rate та deployment rework rate, тобто частку незапланованих deployments для виправлення user-facing bugs. Це оцінки респондентів у cross-sectional survey, не телеметрія CI/CD і не доведений причинний ефект. Не перекладати +0.10 SD як +10% failures. >80% і 59% — частки респондентів, які повідомляють про покращення productivity та code quality. Перевірений коефіцієнт 2024 +7.2% тут не підставляємо. Деталі: evidence/dora-2025.md.\nMETR, 11 травня 2026: 349 technical workers; 1.4–2× medians across 3 self-reported work-value questions; це не credible/confidence interval, 3× self-reported speed; є selection bias. Старий RCT 2025 із +19% часу — лише історичний контекст.\nGitClear 2026: частка moved code у changed lines 13% (2023) → 3.8% (YTD 2026), не кількість refactoring tasks і не весь reuse. Частота duplicated blocks приблизно +81% за цей період. Copy/paste share 9.4% (2022) → 15.7% (H1 2026), інший baseline. Публічне резюме GitClear 2026 прямо повідомляє +15% two-week code churn: частка нещодавно написаних рядків, переписаних/видалених упродовж двох тижнів. Це відносна зміна, не +15 відсоткових пунктів і не частка дефектів. Резюме не дає окремої пари базових значень churn. Function connectivity: 343 → 223 calls/1000 changed lines, 2023 → YTD 2026, приблизно −35%. Це щільність викликів, не весь reuse. Legacy update share: 1.7% → 0.46%; вступ каже 2022, детальний абзац 2023, тому baseline суперечливий і показник лишається в нотатках. Не змішувати churn, duplication та refactoring. Текст і графік 2026 суперечать щодо абсолютної одиниці duplication, тому залишаємо тільки відносні +81%. Це observational proxies, не причинний ефект AI. Деталі: evidence/gitclear.md.\nXu, v3 від січня 2026, дані 2020–22: top activity quartile — commits −19%, reviews +6.5%; bottom quartile — commits +43.5%, PRs +17.7%; rework +2.4%. Це не кадрові грейди й не агенти 2026 року.\nAgarwal, v2, Table 2: complexity Agent-first +34.85% / IDE-first +42.87%, warnings +17.73/+19.00%; зміна IDE-first warnings статистично незначуща. Не трактувати це як борг на одну фічу.\nDORA: позитивний зв’язок AI adoption з throughput одночасно з негативним зі stability. Small batches, p.58: сильніший позитивний зв’язок AI із product performance та менше friction, хоча індивідуальні gains можуть бути меншими. ToC / review-testing-integration queues, p.81. Це мотивує системну оптимізацію на слайді 7, не доводить універсальну причинність.\nПовторна числова перевірка 2026-09-21: DORA Fig.28 vector coordinates та сторінку звірено повторно; коефіцієнт і межі лише приблизні. >80% збережено як авторський поріг: сума округлених bars 41+31+13=85 не встановлює точного агрегату. GitClear calls 343→223 дають приблизно −35%; +81% — авторське округлення, +15% churn — число з резюме без окремої baseline-пари. Точний місяць публікації GitClear не підтверджено на перевіреній сторінці, тому на екрані лише 2026. Див. EVIDENCE.md та відповідні локальні нотатки.\nПояснення GitClear: Moved-code share — частка змінених рядків, класифікованих як переміщений наявний код. 3.8−13=−9.2 відсоткового пункту; (3.8/13−1)×100=−70.769…%, на екрані −70.8%. Це proxy активності рефакторингу: менша частка переміщень може означати менше реорганізації та повторного використання коду, але не кожне переміщення корисне і не весь рефакторинг є переміщенням. Calls / 1k changed lines — кількість викликів інших методів або функцій у новому коді на 1000 змінених рядків, не API throughput. 223−343=−120; (223/343−1)×100=−34.9854…%, приблизно −35%. GitClear трактує вищу щільність як більшу зв’язність нового й наявного коду. Менша може означати слабше reuse, але менша зв’язність іноді бажана; перевіряти дизайн і дублювання. Падіння цих двох proxy — привід перевірити підтримуваність, не автоматичний висновок про погану якість чи причинність AI. *Період 2023→YTD 2026 стосується moved/calls/duplication; для reported churn +15% окремої базової пари немає.\n\nПоточне пояснення: наскрізний приклад і рішення.\nЕкранна ієрархія: три контрасти. NBER — масштаб зміни коду, commits та releases не збігається; DORA — throughput і stability є різними outcomes; GitClear — зміни структурних proxy потребують контексту. Не зачитувати всі метрики. NBER числа 25.5× / 3.4× / 1.3× накопичені за трьома поколіннями інструментів, LOC означає additions + deletions, асинхронний effect для releases не оцінено. Marketplace: iOS <10 ratings ≈78% → 87%, Chrome <10 downloads 19% → 33%, Jan 2025 → Apr 2026 за перші три місяці. Це відмінні міри adoption, а не прямий доказ відсутності user value.\n\nДодаткові числа для обговорення: DORA >80% respondents повідомляли про productivity improvement, 59% — quality improvement; це self-reported perceptions, окремі від моделі delivery instability. Приблизна оцінка моделі: +0.10 SD instability на +1 SD AI adoption, 89% credible interval ≈+0.07…+0.13 SD. GitClear moved-code share 13% → 3.8% = −9.2 pp / −70.8%, calls per 1k changed lines 343 → 223 = −120 / ≈−35%; duplicates ≈+81% та two-week churn +15% мають окремо описані baseline/limitations. Нижче залишаються попередні джерельні пояснення. METR May 2026: medians 1.4–2× self-reported work value across three questions, не causal effect. Agarwal Jan 2026: complexity +34.85% Agent-first / +42.87% IDE-first; Xu описує workload shifts. Ці допоміжні свідчення доповнюють три основні контрасти, але не утворюють єдину сукупну оцінку.\n\nПоточне пояснення: два зсуви та статистичні умови delivery.\nУточнення churn за першоджерелами, 23 вересня 2026. Public GitClear Coding on Copilot, January 2024, описує дані 2020–2023 та прогноз приблизного подвоєння two-week churn у 2024 проти baseline 2021. Це близько +100% projected relative change, не вже виміряний результат 2024. Public 2026 Maintainability Gap прямо містить +15% two-week churn. У тексті не наведено окремої пари churn endpoints, тому тут це reported number із явно неповною baseline-пояснювальною базою, не independently recomputed effect. Не зіставляти +15% і старе ~2× як єдиний часовий ряд або свідчення зниження churn. Різні vintage / periods / samples потребують однакових визначень і baseline. Two-week churn означає частку нещодавно написаних рядків, які невдовзі переглянуто чи видалено; не duplication, не defect rate і не percentage-point increase. Екранна зірочка прямо попереджає про відсутній standalone baseline. Попередня двоколонкова композиція повертає на екран METR, Agarwal та арифметичне пояснення GitClear. Джерела: https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality ; https://www.gitclear.com/the_ai_code_quality_maintainability_gap .",
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
    "https://www.gitclear.com/industry_stats/ai_code_quality_signal_graphs",
    "https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality"
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
  "gitclearCaveat": "Proxies, not a quality verdict. *Churn baseline unspecified.",
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
  "gitclearSecondary": "Duplicated blocks ≈+81%   ·   Two-week churn +15%*",
  "comparisonCaveat": "Different studies and outcomes. These signals do not form one causal estimate."
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
  "takeaway": "IT assistant: help employees recover access\nusing approved guidance and permitted actions.",
  "caption": "Same request, different responses. Context, model and configuration also matter.",
  "notes": "Thinking Systems — інженерна категорія, не твердження про свідомість. Формули — спрощений контраст. Точніше P(y | x, c, m): контекст, модель і конфігурація також мають значення. Стабільне повторення не гарантує істинності. Наскрізний умовний кейс: IT-асистент використовує дозволені джерела, але не має права на неавторизовані зміни доступу.\n\nВізуальне уточнення за наданими скриншотами, 22 вересня 2026. Графічне пояснення за слайдом 3 старої презентації: зліва одиничний результат за фіксованих input, state і version у детермінованому випадку, справа схематичний розподіл можливих результатів. Висота стовпчиків передає відносну частоту лише концептуально. Це не виміряна вибірка, не оцінка ймовірності, не твердження про нормальний розподіл чи математично важкі хвости. Горизонтальна вісь — умовна проєкція варіантів результату. Реальна семантика багатовимірна й може бути категоріальною. Центральна область показує корисну варіативність у прикладі, краї — рідші варіанти, які також потрібно оцінити. Рідкість сама по собі не робить результат дефектом. Інженерне завдання — сформулювати й реалізувати межі корисної поведінки. Детерміновані обов’язки, права та інваріанти в продукті залишаються. Обидві формули є навчальним контрастом, а не класифікацією всього software за одним параметром.\n\nКритичний перегляд зв’язності та ролей, v14, 23 вересня 2026:\nЦе перехід від HOW до WHAT: у першій частині AI допомагав створювати код; тепер продукт делегує моделі частину runtime judgment. Обидві зміни можуть бути присутні разом, але потребують різних evidence. Новий об’єкт афектить Product Manager / Product Owner і BA через цінність та контракт поведінки; розробників, QA й архітектора через реалізацію та перевірку; Project Manager через залежності та план робіт; service owner / operations через дієздатність контролю після запуску. Ролі тут позначають відповідальності, а не обов’язкові нові посади: у невеликій команді їх можуть поєднувати. Наступні слайди — один спільний ланцюг define → evaluate → control → operate, а не передавання ізольованої роботи між відділами. Спочатку погодимо, яка поведінка корисна й дозволена.\n\nПоточне пояснення: наскрізний приклад і рішення.\nНаскрізний приклад другої частини — внутрішній IT-асистент, який допомагає працівнику відновити доступ за затвердженою інструкцією. Він може пояснити recovery steps, попросити уточнення або запропонувати дозволену дію; proposal залишається внутрішнім недовіреним результатом до перевірок та delivery/execution. Це ілюстративний design case, а не опис уже впровадженого продукту. Бажаний outcome — відновлений доступ, менше повторних звернень і прийнятні повні витрати. Текст відповіді може варіюватися, але authority, permissions і заборонені outcomes не розширюються. На 9 погоджуємо контракт, на 10 перевіряємо результати, на 11 вирішуємо readiness/completion/release, на 12 показуємо здійсненний control path. Це послідовність пояснення; design, evaluation й operational feasibility опрацьовують разом.",
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
  "graphCaption": "Schematic distribution, not measured data. Shape depends on the task.",
  "role": "PRODUCT / PO · BA · PROJECT MANAGER · ENGINEERING · QA · OPERATIONS"
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
  "role": "PRODUCT MANAGER / PRODUCT OWNER · BA · PROJECT MANAGER",
  "oldHeading": "SPECIFIED FLOW · STILL REQUIRED",
  "old": [
    "Request",
    "Verify user"
  ],
  "oldDetail": "Exact permissions and transitions\nstill apply to the IT assistant.",
  "roleDetail": "Product / PO: value and priorities.\nBA: testable acceptance examples.\nProject Manager: timely decisions.",
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
  "takeaway": "Output: an agreed contract the team can implement, evaluate and operate.",
  "notes": "Наскрізний приклад: внутрішній IT-асистент. Зліва — точний перехід Button A → Window B, permissions та інваріанти, які залишаються вимогами. Справа — додаткові вимоги до варіативної поведінки. Дозволено пояснити затверджену статтю підтримки різними словами, зберігаючи зміст і необхідні кроки. За відсутності контексту потрібно уточнити або ескалувати. Не можна вигадувати операційні кроки, розкривати чужі дані або виконувати дію в обхід approval. Одна картинка з областю сама не задає точного вимірюваного контракту.\nМовний розрив: природна мова неоднозначна; prompt не є точним описом усіх можливих відповідей. Теза «стандартів немає» надто категорична: ISO/IEC 25059:2023 надає quality model і узгоджену термінологію, NIST AI RMF — контекстне управління ризиком, GenAI Profile — спільне з domain experts документування допустимого використання. Вони не підставляють готові семантичні межі й прийнятність наслідків для нашого продукту. Не стверджуємо доведеної відсутності будь-якої формальної мови.\nПрактична пропозиція доповіді: Product Manager та BA разом із бізнесом збирають сценарії, приклади, контрприклади, клас наслідків і потрібну реакцію; фіксують rubric, джерело правила й того, хто його погоджує. CheckList (Ribeiro et al., ACL 2020) пропонує capability × test-type підхід до поведінкових перевірок NLP. Це допомога у формулюванні перевірок, не універсальний стандарт semantic acceptance. Project Manager планує доступ до stakeholders, рішення та залежності; не вигадує толерантність за бізнес.\nВимога ширша за Operating Envelope; точні інтерфейси, заборони й інваріанти зберігаються. BA/Product не зобов’язані самі вивести статистичний поріг: це спільна робота з бізнесом, QA, розробниками й власником ризику. Ролі описують відповідальність, не новий headcount.\nДеталізація бізнес-контракту. Два формулювання відповіді можуть бути однаково правильними: асистент має право скоротити пояснення або змінити тон, але повинен зберегти затверджені кроки, умови та застереження. Заміна тексту сама по собі не є дефектом. Порушення змісту, неправомірна дія або непрацездатний обов’язковий fallback — вже інше питання. Тому команда описує не всі речення наперед, а дозволені джерела й теми, потрібні semantic properties, неприйнятні наслідки та реакцію на невизначеність.\nProduct Manager і BA додають до прикладів контракт на експлуатацію: який ручний rework бізнес здатен обробити; скільки коштує корисно завершений запит з урахуванням перевірок, повторів і людей; яку затримку користувач витримає; за яких умов потрібні уточнення, людина або відмова. Якщо ці межі невідомі, це питання для дослідження зі stakeholders, а не число, яке QA має вгадати. Для IT-асистента питання бізнесу звучить так: «Коли краще не дати інструкцію, а передати звернення фахівцю, і чи зможемо ми обслужити цей потік?».\nСпільна мова формується через позначені приклади й контрприклади, rubric, класи наслідків, approved sources та decision owner. Prompt впливає на відповіді, але не задає повного acceptance specification. Графічна область і один semantic-distance score також не замінюють цей контракт. Межі якості, вартості й latency не стають жорсткими гарантіями без окремого реалізованого enforcement path.\n\nНа правій половині тепер зображено саме область можливих прийнятних результатів. Це концептуальна межа, а не графік з універсальною числовою віссю semantic distance. Коротке й докладне пояснення можуть бути однаково прийнятними, якщо обидва спираються на затверджену статтю та зберігають обов’язкові кроки. Вимога задає властивості області: дозволені теми й джерела, потрібний зміст, заборонені дії та дані, ресурсні межі, реакцію на нестачу контексту. CLARIFY — визначена контрактом дія, коли доказів для змістовної відповіді недостатньо; це не дозвіл порушити межу. PROHIBIT поза дозволеною областю показує неприйнятні наслідки. Саме формулювання межі її не реалізує: для критичних заборон потрібні конкретні контролі. Ліворуч лишаються точні стани, права й переходи. Нові обов’язки доповнюють ці сценарії. Product Manager та BA мають отримати від бізнесу приклади допустимих варіантів і контрприклади, а Project Manager забезпечує рішення та доступність потрібних учасників.\n\nВізуальне уточнення за наданими скриншотами, 22 вересня 2026. Візуальна модель тепер безпосередньо відтворює логіку слайда 5 старої презентації: зліва вузький маршрут A–B, справа площина можливостей із перспективною сіткою, зовнішнім бурштиновим контуром погоджених допусків та внутрішньою блакитною областю цільової поведінки. Обидва прийнятні варіанти — коротке та докладне пояснення — належать спільній області. Зовні показано заборонений результат. Внутрішній контур — робочий орієнтир, зовнішній — контракт прийнятності. Простір між ними не є автоматичним дозволом: кожен результат повинен виконувати всі умови контракту. Це концептуальна багатовимірна область, а не виміряна координатна система чи універсальна embedding-distance метрика. Площина стисло показує сукупність умов щодо тем, джерел, обов’язкового змісту, даних, дій, authority, вартості, latency та failure handling. Вимога включає й точний сценарій, і цю область. CLARIFY визначає належну реакцію на нестачу контексту, а не ослаблення заборони. Попередні ALLOW / CLARIFY / PROHIBIT і приклади залишаються в нотатках та уточнюють геометрію.\n\nІнтеграція старого слайда 16 (PDF page 17, PM: From Story Owner to Distribution Economist). Тут PM у старому заголовку означає Product Manager; Project Manager у нашій доповіді — окрема відповідальність за delivery та операційну модель. Product / BA організовують з бізнесом рішення: які варіації результату прийнятні; скільки та яких помилок можна допустити; за якої тяжкості, частоти або наслідку відповідь стає неприйнятною відповідальністю; коли потрібні зупинка, людина чи fallback. Не можна звести це до одного середнього відсотка або грошей: обов’язкові заборони залишаються заборонами. До контракту входять unsupported claims, визначена для продукту semantic rubric, правила ескалації, бюджет токенів та human review, latency і поведінка fallback. Ланцюжок Product value → Risk tolerance → Cost envelope → Release decision пояснює бізнес-сенс меж на діаграмі. QA та розробники разом із Product/BA переводять ці рішення у вимірювання та evidence; Project Manager забезпечує доступність stakeholder decisions, власників і залежностей. Prompt лише впливає на поведінку; контракт визначають погоджені вимоги, приклади та критерії. Попередні пояснення області, ALLOW / CLARIFY / PROHIBIT, мовного розриву та наявних стандартів зберігаються.\n\nКритичний перегляд зв’язності та ролей, v14, 23 вересня 2026:\nProduct Owner явно входить до цього слайда: відповідає за цінність, Product Goal і впорядкування backlog, робить потрібні вимоги, evidence та control work видимими й пріоритетними. Product Manager, якщо ця роль є окремо, додає продуктову стратегію, discovery та економіку; конкретний розподіл із PO залежить від організації. BA допомагає зробити domain rules, приклади, контрприклади та acceptance rules однозначними. Project Manager організовує своєчасні stakeholder decisions, доступність експертів, оцінювання залежностей, бюджету й capacity; не вигадує прийнятний ризик за бізнес. Dev, QA та архітектор уже тут перевіряють, чи можна критерії виміряти й межі забезпечити. Уповноважений business / risk owner погоджує допустимі наслідки в межах своїх прав; правові, privacy та security заборони не стають предметом довільного обміну на value. За потреби залучаємо відповідних фахівців. Назва Product Owner сама собою не надає права приймати будь-який risk або authorize release.\nКрім відсутності шкоди, задаємо ціль корисності. Для наскрізного support-assistant прикладу: чи вирішено звернення правильно, чи не перенесли ми роботу на користувача або оператора, яка повна вартість корисно завершеного звернення? Це питання для вибору продуктового показника, не нові емпіричні числа. Вимоги до exact states / permissions не зникають; поведінковий контракт їх доповнює. Передаємо на слайд 10 не список побажань, а погоджені приклади, заборони, критерії та власників рішень.\n\nПоточне пояснення: наскрізний приклад і рішення.\nДля IT-асистента Product / PO визначає цінність відновленого доступу та пріоритети, BA разом із QA / domain expert перетворює межі на приклади acceptance, Project Manager забезпечує своєчасність залежних рішень. Risk/business authority погоджує допустимі наслідки. Вихід — один придатний до перевірки контракт: approved knowledge і права поточного користувача, потрібне уточнення замість припущення, заборона іншої особи private data або обходу approval, support fallback. Вимірюємо успішне вирішення й repeat contacts разом із latency, token/review cost. Жодного універсального числового threshold цей приклад не задає. Попередні посилання ISO/IEC 25059, NIST AI RMF і CheckList лишаються вихідними матеріалами, а конкретну семантику продукту команда погоджує сама.",
  "sources": [
    "https://www.iso.org/standard/80655.html",
    "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf",
    "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf",
    "https://aclanthology.org/2020.acl-main.442/",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/requirements-correctness-and-bugs.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=5",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=7",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=17",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=5",
    "https://scrumguides.org/scrum-guide.html"
  ],
  "envelopeHeading": "IT ASSISTANT: AGREED BEHAVIOR CONTRACT",
  "envelope": [
    "Value: restored access, fewer repeat contacts",
    "Safety: no data disclosure or access bypass",
    "Budget: latency, token and review costs",
    "Fallback: support ticket with approved context"
  ],
  "specification": "Business / risk owner approves limits. Product / PO + BA make them testable with Dev + QA.",
  "regionCaption": "Approved tolerance boundary",
  "regionExamples": [
    "Approved recovery steps",
    "Clarifying question"
  ],
  "regionInner": "Target operating region",
  "regionOutside": "Another user’s\nprivate data",
  "regionAxis": "Conceptual space, not a universal semantic metric",
  "regionPolicy": "ALLOW approved guidance · ASK for context · DENY access bypass"
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
  "role": "QA + DOMAIN EXPERTS · DEVELOPERS · PRODUCT / PO · PROJECT MANAGER",
  "frequency": "ILLUSTRATIVE INDEPENDENT SAMPLE · n = 200",
  "observed": "4 / 200 = 2%",
  "interval": "95% Wilson interval ≈ 0.8%–5.0%",
  "rateLabel": "Any contract violation",
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
      "PRODUCT / PO + BA",
      "Elicit impact; specify approved acceptance"
    ],
    [
      "QA + DEVELOPERS + DOMAIN EXPERTS",
      "Sample, calibrate, compare versions"
    ],
    [
      "PROJECT MANAGER",
      "Coordinate evidence readiness and dependencies"
    ],
    [
      "RISK / RELEASE OWNER",
      "Decide acceptability for this scope"
    ]
  ],
  "takeaway": "Statistics estimate frequency. Business authority decides acceptable consequences.",
  "notes": "Статистичне оцінювання доповнює unit, integration, security та deterministic tests. Потрібно окремо оцінити: а) частоту виходу за погоджені межі; б) силу/тяжкість наслідку. «Сила відхилення» не має універсальної числової шкали: для latency це мілісекунди понад межу, для грошей — збиток, для semantic output — погоджена rubric і класи наслідків. Середній score або embedding distance сам по собі не встановлює business harm. Хвости й критичні групи оцінюємо окремо, а не приховуємо добрим агрегатом.\nНавчальний приклад, не реальні дані і не рекомендований sample size: 200 незалежних репрезентативно відібраних evaluation units із одного стабільного цільового розподілу; 196 прийнятних, 4 неприйнятні. Серед чотирьох: 3 неправильні інструкції та 1 витік даних. 4/200=2%; 196/200=98%. Двосторонній 95% Wilson score interval для частки неприйнятних: [0.780443%, 5.028709%], на слайді ≈0.8%–5.0%. Метод і формула — NIST Engineering Statistics Handbook §7.2.4.1. Інтервал відображає sampling uncertainty за припущень; не дає 95% ймовірності, що конкретний майбутній результат безпечний, і не гарантує поведінки після зміни контексту. Не можна рахувати повтори того самого кейсу як незалежні representative cases. Розмір вибірки, dependence, subgroup coverage, множинні порівняння, невизначеність оцінювача й baseline планують під рішення.\nУ прикладі витік порушує обов’язкову вимогу, тому release блокується незалежно від 98% aggregate acceptance. Відсутність витоків у тесті також не доводила б неможливості витоку: потрібні permissions, isolation, gate та перевірка припущень їх роботи.\nЗвідки взяти tolerance? QA не винаходить його. Product Manager та BA обговорюють із бізнесом зрозумілі сценарії: скільки ручного виправлення витримає support; кому і яку шкоду завдасть помилка; що треба технічно унеможливити; коли прийнятні уточнення або ручний шлях. Технічна команда перетворює це на measurement plan, оцінку частот, severity, confidence та тригери. Уповноважений власник ризику/релізу погоджує допустимість у конкретному scope. Project Manager організовує ці рішення до обіцянки релізу.\nModel drift пояснюємо бізнесу як зміну спостережуваних результатів/навантаження/наслідків за нової версії чи контексту, а не вимагаємо від stakeholders знання статистичних термінів. QA підтримує golden/reference sets, coverage, calibration із domain experts і перевірки підгруп. Developers роблять versioning, instrumentation, відтворювані evaluation runs і regression comparison. Пороги та rubric версіонуються; evidence для release перевіряється окремо від набору, на якому їх підбирали.\nЩо саме змінюється в QA. Golden Set — версіонований набір звичайних, крайових, adversarial і business-critical сценаріїв з очікуваними властивостями змісту та прикладами неприйнятного результату. Це інструмент вимірювання: він сам може бути неповним, застарілим або невдало розміченим. QA разом із domain experts калібрує rubric та evaluator: де він пропускає небезпечну відповідь, де помилково блокує корисну, як розходяться людські оцінки. Розробник забезпечує runner, конфігурацію, provenance та порівняння baseline із candidate.\nEval Gate пов’язує отримані evidence з погодженим рішенням: block, обмежена експозиція або release у визначених межах. Сам score ще не приймає business risk. Повторні запуски показують варіативність усередині сценарію, а різні сценарії — coverage. Цілеспрямовано зібраний Golden Set не є автоматично репрезентативною вибіркою production traffic; його pass rate не можна без обґрунтування підставити як реальну частоту помилок. Навчальні 4/200 та Wilson interval вище мають власні явно названі припущення.\nЗміна моделі, prompt, retrieval або складу запитів може змінити розподіл результатів навіть без зміни application code. Після інциденту додаємо відтворюваний regression case, перевіряємо чутливість evaluator і причину пропуску. Фінальну release evidence оцінюємо на незалежних від налаштування даних. Бізнесу показуємо не слово «drift», а зміну кількості виправлень, ескалацій, неприйнятних наслідків, затримки й вартості.\n\nГрафік показує емпіричний розподіл категорій тієї самої навчальної вибірки: 196 прийнятних результатів, 3 неправильні інструкції й 1 витік приватних даних. Разом 200, частки відповідно 98%, 1,5% та 0,5%. Це не 200 різних унікальних рядків тексту: результати групуються за погодженими семантичними властивостями та наслідками. Категорії в цьому прикладі взаємовиключні та вичерпні. Вісь починається з нуля, довжина стовпчиків пропорційна кількості. Малі стовпчики не означають малої тяжкості, тому точні значення та критичний наслідок підписано. Неприйнятні результати об’єднуються для оцінки частоти: (3+1)/200 = 2%. Попередній 95% Wilson interval приблизно 0,8%–5,0% стосується цієї бінарної події, а не кожної категорії окремо та не ймовірності майбутнього інциденту без припущень про вибірку. Ми не накладаємо нормальну криву на категоріальні дані та не вигадуємо baseline для порівняння. Для нового порівняння потрібні зафіксовані версії й порівнювані сценарії. Саме цей перехід до частот, розподілів та невизначеності запозичено зі слайдів 7 і 19 старої презентації. Бізнес має визначити допустимість частоти та сили наслідку, QA — які докази й невизначеність є для рішення.\n\nВізуальне уточнення за наданими скриншотами, 22 вересня 2026. Визначення дефекту й схематична область допусків адаптовані зі слайда 4 старої презентації з уточненням чинної UA doctrine Requirements, Correctness, and Bugs. Bug — порушення погодженої вимоги на рівні системи, яке спричинила або допустила реалізована система. Для model-mediated поведінки це, зокрема, вихід за погоджені умови чи допуски або заборонений наслідок. На схемі зелена область — дозволена варіативність, червоні стовпчики — наслідки за межами контракту, якщо система їх допустила. Графік концептуальний: висоти не є даними, нормальність не припускається, одиниць універсальної semantic distance немає. Схема і вибірка 196/3/1 — різні пояснювальні об’єкти; концептуальні стовпчики не відновлені з цих трьох категорій. Рідкісний результат не обов’язково Bug. Якщо запропоновану моделлю заборонену дію контролі належно зупинили до наслідку, це може бути коректним containment за контрактом. Якщо частота помилок допускається в певному контексті, потрібні також погоджені межі тяжкості, наслідків і правила обробки, а не тільки середній відсоток. Розподіл може змінюватися без змін коду, однак окремий tail event не доводить drift: для цього потрібні порівнювані вибірки, baseline, контекст і версії. Класичні детерміновані дефекти також залишаються. На екрані нижче збережено незалежний навчальний приклад: 196 прийнятних, 3 неправильні інструкції та 1 витік приватних даних, 4/200 = 2%, Wilson 95% приблизно 0,8%–5,0%. Частота і тяжкість — різні виміри рішення. У цьому прикладі витік порушує обов’язкову заборону й блокує release. Бізнес через Product/BA визначає прийнятність наслідків, QA/developers вимірюють і перевіряють evidence, уповноважений risk/release owner ухвалює рішення. Golden Set, Eval Gate, калібрування та incident regression залишаються робочими інструментами.\n\nКритичний перегляд зв’язності та ролей, v14, 23 вересня 2026:\nЦей слайд афектить не лише QA: Product / PO + BA уточнюють, що є корисним і прийнятним, domain experts допомагають калібрувати оцінювання, Dev робить відтворюване вимірювання версій, а Project Manager забезпечує час, дані, експертів та готовність evidence до рішення. Уповноважений risk / release owner ухвалює рішення в погодженому scope; статистична оцінка не надає права обійти заборону. Service owner приносить production outcomes та incidents.\nОкремо проговорити видиму різницю: curated Golden Set перевіряє важливі сценарії й класи відмов; оцінка частоти в цільовому usage потребує обґрунтованої репрезентативної вибірки. Для Wilson interval потрібні зазначені припущення незалежної бінарної вибірки; 95% — властивість методу інтервалу, не гарантія безпечності production. Навчальні 196/3/1 та 4/200 не змінені. Навіть добрий середній score не перекриває критичну заборону. Варіативність прийнятна лише всередині всього контракту; належно перехоплена заборонена пропозиція моделі може свідчити про правильний containment. Наступний крок — зробити ці evidence частиною readiness, completion і окремого release decision.\n\nПоточне пояснення: наскрізний приклад і рішення.\nТі самі 200 ілюстративних незалежних відповідей тепер явно стосуються IT-асистента: 196 допустимих, три з неправильними recovery instructions і одна з disclosure чужих приватних даних. Об’єднані 4/200 = 2% і 95% Wilson interval ≈0.8–5.0% оцінюють частоту any contract violation за умовами вибірки; вони не оцінюють окремо частоту critical harm і не перетворюють її на прийнятну. Інтервал потрібен для рішення про звичайну надійність та очікуване навантаження rework; він не компенсує заборонену подію. Для цього погодженого contract одна disclosure блокує candidate. Golden Set — curated набір важливих сценаріїв, а representative sample потрібна для rate estimation. Eval Gates — погоджені criteria порівняння evidence версії з умовами використання, не обіцянка математичного доведення безпеки. Нуль знайдених critical events також не доводить їх неможливість. Наступний слайд показує, як evidence впливає на завершеність і дозвіл використання.\n\nПоточне пояснення: два зсуви та статистичні умови delivery.\nПідписи outcome chart читаються як count (share): 196 (98%), 3 (1.5%), 1 (0.5%). Це ті самі 200 ілюстративних відповідей. Число 19698% не є метрикою. Відсотки стосуються часток відповідної категорії, а 4/200 і Wilson interval — сукупної події порушення контракту. Однорядковий запис чітко відділяє число випадків від частки.",
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
  "instruments": "Golden Set: probe known scenarios. Representative sample: estimate error rates.",
  "calibration": "QA + domain experts calibrate scoring. Eval Gates compare evidence with release criteria.",
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
    "196 (98%)",
    "3 (1.5%)",
    "1 (0.5%)"
  ],
  "chartAxis": "Observed counts by outcome",
  "bugHeading": "WHAT COUNTS AS A BUG",
  "bugDefinition": "System behavior violates\nan approved requirement.",
  "bugModel": "IT assistant: wrong recovery steps\nor another user’s private data.",
  "bugCode": "The code may stay unchanged while behavior changes.",
  "bugNuance": "Variation within the contract is acceptable. A contract violation is a defect.",
  "toleranceHeading": "APPROVED BUSINESS TOLERANCES",
  "insideLabel": "Allowed variation",
  "outsideLabel": "Outside the contract",
  "bugLabel": "Bug:\ncontract\nviolation",
  "schematicCaption": "Schematic projection, not measured data. Limits are product-specific.",
  "ownershipLine": "A low average error rate does not excuse a prohibited disclosure."
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
  "role": "PRODUCT / PO + BA · DEVELOPERS + QA · PROJECT MANAGER · OPERATIONS",
  "table": [
    [
      "CONTRACT",
      "TRADITIONAL DoR / DoD",
      "ADDED FOR THINKING SYSTEMS"
    ],
    [
      "DoR\nREADY",
      "Specified behavior + acceptance criteria\nDependencies and feasibility\nTest approach and operating limits",
      "Business tolerances + prohibited outcomes\nGolden Set, sampling and control / HITL plan\nCost, latency and response-capacity budget"
    ],
    [
      "DoD\nDONE",
      "Implementation reviewed\nRequired tests + acceptance checks pass\nOperational handover complete",
      "Eval Gates meet approved criteria\nCoverage + uncertainty documented\nControls / human fallback tested within budget"
    ],
    [
      "RELEASE",
      "Decision against agreed criteria\nOperational owner accepts the handover",
      "Error bounds + residual risk accepted\nMonitoring, response and rollback ready\nIncidents update regression / gates / monitors"
    ]
  ],
  "caption": "DoR is a team practice. DoD is a quality commitment. Release is an authorized decision.",
  "takeaway": "Beyond a green run: measured behavior within approved limits,\nwith a complete, operable control loop.",
  "notes": "Конкретизуємо абстрактні risk contracts через deliverables розробників для того самого IT-асистента. READY: визначено аудиторію, дозволені джерела, заборонені дії, приклади/rubric, evaluation plan, критичні залежності й власника ручного шляху. Якщо tolerance або feasibility ще невідомі, команда може бути Ready до обмеженого експерименту з питанням, бюджетом, stop condition та owner; це не дозвіл на production.\nDONE: developer поставляє відтворювану конфігурацію model version, prompt, retrieval/data snapshot, tool schema, policy та permissions; результати deterministic, behavioral і control-path tests; посилання на evaluation evidence, coverage й обмеження. Перевірені deny-path, unavailable-control behavior, telemetry та фактичний rollback/manual fallback. QA звіряє evaluation method і results, а не одноосібно приймає business risk. Для слайда скорочено до model/prompt/data; повний список тут.\nRELEASE: ідентифіковано саме цю версію, population, tool authority, exposure, monitoring, stop triggers, оперативного owner та fallback capacity. Уповноважена особа приймає залишковий ризик у межах повноважень або звужує scope, відкладає чи відхиляє реліз. Прийняття ризику не скасовує обов’язкову заборону й не розширює успадковану project authority. Попередній toy-example із privacy breach не пройде цей gate.\nРозробник тепер здає не лише endpoint, а відтворювану поведінку, evidence і працездатний recovery path. Project Manager відстежує незакриті залежності/рішення та не прирівнює Done до Ship. Ролі можуть поєднуватись однією людиною; достатньо існуючого review artifact, новий комітет не потрібний.\nПрактичний engineering object — версія поведінки, а не лише commit застосунку. Один і той самий endpoint із новим prompt, knowledge snapshot, моделлю, evaluator або правами інструментів може мати інший профіль якості й ризику. Тому evidence та rollback прив’язуються до узгодженого набору версій. Окремий Prompt Registry не обов’язковий: для малої команди достатньо наявного version control та deployment/configuration механізму, якщо вони дозволяють встановити, що саме працювало, хто погодив зміну і як повернутись.\nREADY включає quality, cost і latency budgets та місткість ручного шляху. Для експерименту потрібні обмеження експозиції й ресурсів до початку роботи. DONE включає deterministic tests, coverage поведінкових сценаріїв, невизначеність оцінки й порівняння з baseline. Валідний JSON перевіряє форму: структурно правильний об’єкт може містити вигадану інструкцію. Тому schema pass доповнюється semantic evidence, permissions і перевіреним recovery path.\nRELEASE має явні варіанти block, canary або scoped release. Canary також потребує попереднього дозволу, обмеженої аудиторії, моніторингу та можливості зупинити експозицію. Усі попередні критерії й власники залишаються. Rollback повертає конфігурацію, але не скасовує вже виконану зовнішню дію: для таких наслідків потрібні containment, ручне виправлення або компенсація.\n\nТаблиця тепер прямо порівнює звичний фокус DoR/DoD з додатковими зобов’язаннями для model-mediated behavior. Ліва колонка — спрощений навчальний фокус, а не твердження, що класичний software не має ризик-аналізу, навантажувальних тестів, моніторингу або incident management. Усі наявні вимоги організації залишаються. У DoR потрібен повний і правдоподібний дизайн керування для суттєвих сценаріїв: вимога й межа, спосіб її реалізації, спостереження, уповноважене рішення, виконавчий механізм та перевірка ефекту. Сюди входить human-in-the-loop: хто втручається, з якою інформацією, правами, часом і доступною потужністю, хто підміняє та що відбувається при недоступності. DoR до реалізації не вимагає вже збудованої системи, але має показати весь задум і залежності. Якщо feasibility ще невідома, Ready може означати лише готовність до окремо обмеженого дослідження. До експерименту з реальним exposure потрібні вже працездатні відповідні контролі. DoD підтверджує реалізацію й перевірку цього контуру, включно з людиною та fallback; версії, baseline, оцінка невизначеності, resource budgets і recovery evidence зберігаються. Release визначає population, tool permissions, residual risk, відповідальну особу, постійний моніторинг і triggers для stop/rollback. Block, canary або scoped release — різні дозволені результати рішення. Робота не закінчується релізом: production incidents породжують regression cases, зміни критеріїв Eval Gate та правил моніторингу. Такі зміни також версіонуються, перевіряються й погоджуються в межах повноважень; не можна тихо послабити бізнес-межу, щоб метрика стала зеленою.\n\nІнтеграція старого слайда 5 (PDF page 6, From Static Requirements to Statistical Gates). Чотири порівнювані рядки тепер видно безпосередньо: Ready, Budget, Done та Release / Operate. Окремий Budget повертає cost envelope зі старої презентації: токени, повторні виклики, evaluations, людська перевірка, latency та місткість fallback мають впливати на readiness і життєздатність. Статистичний контракт не означає, що великий n доводить безпеку: потрібні придатна вибірка, coverage, калібрований evaluator, припущення й оцінка невизначеності щодо погодженого порога. Приймають evidence у контексті бізнес-допусків, а не абстрактний confidence interval сам по собі. Старий фокус показаний як навчальне спрощення: класична інженерія також має nonfunctional requirements, ризик, вартість, навантажувальні тести та operations. Повний control/HITL design лишається в DoR, працездатність і rehearsal — в DoD. Release залишається окремим scoped decision із постійним monitoring та incident → regression / Eval Gates / monitoring rules loop. Зміна правил не може непомітно послабити затверджену межу.\n\nПоточне уточнення 23 вересня 2026:\nУточнена композиція повертає два основні контракти, як у старому слайді про DoR / DoD. Бюджет не є окремим gate: погоджені token/evaluation/human-review costs, latency та capacity входять до DoR, а перевірка фактичних показників — до DoD. DoR: маємо вимоги, business tolerances, forbidden outcomes, evaluation plan і повний design control loop включно з human authority, fallback та recovery. Ready для bounded experiment не означає production authorization. DoD: зберігаються code review, deterministic tests та інваріанти; додаються versioned model/prompt/context/data evidence, калібровані Eval Gates, coverage, sample uncertainty і перевірені controls. Велика вибірка чи один confidence interval не є доказом універсальної safety. Release відділений від DoD: уповноважений owner приймає residual risk і scope. Після релізу потрібні постійний monitoring, відповідальні responders та зворотний зв’язок від production incidents у regression, Eval Gates і monitoring rules. Product/BA узгоджують межі з бізнесом, архітектор проєктує контроль, Dev/QA реалізують та перевіряють, PM відстежує залежності й readiness. Лівий стовпчик є стислим порівнянням фокусу, а не твердженням, що традиційна розробка не мала risk/cost/operations.\n\nКритичний перегляд зв’язності та ролей, v14, 23 вересня 2026:\nDoR / DoD — спільний робочий контракт, тому цей слайд стосується Product Owner, BA, розробників, QA, Project Manager та operations. PO забезпечує ясність мети, цінність і пріоритети backlog; BA — зрозумілі критерії; Dev / QA — здійсненність, реалізацію та evidence; архітектор і service owner — реальні control / HITL paths та capacity; Project Manager — доступність цих результатів і рішень у delivery plan. Це не передача якості одному PO чи QA. У Scrum Definition of Done є commitment для Increment, Developers мають її виконувати, а за відсутності достатнього organizational standard її створює Scrum Team. Definition of Ready — можлива командна практика, не обов’язковий Scrum artifact чи формальний approval gate. Scrum Master, якщо команда працює в Scrum, допомагає емпіризму та ефективності процесу, не підмінює жодного decision owner.\nRelease owner авторизує scope, exposure та residual risk у межах своїх прав. Service owner / operations забезпечує named responders, часові межі втручання, peak capacity, backup, monitoring та перевірений rollback / fallback; Project Manager координує залежності готовності. Завершене за DoD не означає автоматичного дозволу на будь-який production scope. Інциденти повертаються не лише в тести, а й до Product / PO для зміни пріоритетів і до архітектора для перевірки control assumptions.\nПерехід до 12: порядок розповіді не є waterfall. Ми спершу назвали, що треба довести, а тепер розкриваємо архітектуру, яка робить ці докази й обіцянки credible. Контроль і operational ownership проектуються до релізу, а не додаються після DoD.\n\nПоточне пояснення: наскрізний приклад і рішення.\nНа цьому етапі прикладу IT-асистент ще не готовий до релізу: evidence з 10 містить заборонену disclosure. Стовпець IT ASSISTANT: ADDED REQUIREMENTS описує потрібні умови, а не стверджує, що candidate їх виконав. Команда виправляє джерело порушення, перевіряє permissions і containment, додає regression case, повторює релевантне оцінювання. Release owner не може довільно перекрити inherited prohibition низьким середнім error rate. Зміна меж або scope потребує відповідної authority і re-evaluation. Після виконання критеріїв окремо авторизують scope / residual risk і підтверджують operational capacity. Permission checks та rehearsal support fallback на 12 є частиною попереднього дизайну і реалізації, а не кроком після релізу.\n\nПоточне пояснення: два зсуви та статистичні умови delivery.\nПорівняння відновлює зміст слайда From Static Requirements to Statistical Gates зі старої Designing Non-Deterministic Systems (сторінка 6 PDF, змістовний слайд 5). Порівнюємо не один IT-case, а загальні умови роботи: готовність, завершеність та авторизацію використання. У традиційному software також є ризик, вартість, performance і нефункціональні вимоги; це не caricature «один unit test — і в production». Thinking Systems потребують явних behavioral tolerances і заборонених outcomes, контрольованого cost envelope, evaluation coverage, uncertainty та operating capacity.\n\nDoR: до розробки погоджуємо risk profile, допустиму варіативність, заборонені області, Golden Set / representative sampling, критерії Eval Gates і здійсненний повний control / human-response design. Token/evaluation/review costs, latency й спроможність responders входять у readiness budget, а не утворюють окремий рівнозначний DoR/DoD об’єкт. DoD: versioned evidence демонструє досягнення критеріїв на релевантних сценаріях і вибірках, межі невизначеності задокументовано, controls/fallback/HITL реалізовано й перевірено, limits підтверджено вимірюваннями. Велика вибірка не доводить universal safety: замість історичного «large-sample runs prove» говоримо про evidence та uncertainty під конкретними assumptions.\n\nRelease: уповноважений owner приймає evidence, релевантні error bounds і residual risk для визначеного scope. Confidence interval є input до рішення, а не самостійний дозвіл на harm; prohibited disclosure у прикладі з 10 залишається blocker. Потрібен повний і дієздатний control loop, включно з human authority там, де вона потрібна за approved architecture, моніторингом, response capacity, containment/fallback і rollback лише для оборотних ефектів. Production incidents живлять regression cases, Eval Gates і monitoring rules. Sprint Review не є формальним release gate, DoR — можлива командна практика, DoD — shared quality commitment. Product / PO, BA, Dev, QA, Architect, service / risk / release owners і PM мають різні внески в спільний контракт.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/01-patterns/thinking-system-review.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/nested-control-lifecycle.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=6",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=9",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=13",
    "https://scrumguides.org/scrum-guide.html"
  ],
  "behavior": "Thinking Systems add behavioral limits, cost envelopes and statistical evidence to delivery contracts.",
  "releaseHeading": "RELEASE OWNER: AUTHORIZE · SERVICE OWNER: OPERATE",
  "release": "Approve scope and residual risk after the team demonstrates criteria and working controls.",
  "incident": "Service owner verifies response capacity. Incidents become regression cases."
}
```

**Час:** 3:00.

**Композиція:** Два головні рядки native table: DoR / READY та DoD / DONE; дві порівнювані колонки Traditional та Added for Thinking Systems. Бюджет/latency/capacity вкладені до критеріїв. Release та operations — окрема нижня смуга з incident feedback.

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
  "role": "ARCHITECT + DEV: implement · QA: verify · SERVICE OWNER: operate · PM: dependencies",
  "steps": [
    "Model\nproposal",
    "Check permissions\n+ required approval",
    "Deliver / execute\nallowed result",
    "Observe outcomes\n+ control health"
  ],
  "gate": "Tool actions: deterministic permission / approval gate. Unavailable? Deny and use safe fallback.",
  "reference": "Approved boundaries + credible enforcement",
  "loop": [
    "Observe",
    "Decide / authorize\nsoftware + people",
    "Apply correction"
  ],
  "actions": "Rollback / disable tool / manual fallback · inside delegated authority",
  "caption": "Observe outcomes + gate health. Verify that the corrective action took effect.",
  "takeaway": "Architect + Dev build the path. QA tests it. Service owner keeps it operable.",
  "notes": "Наскрізний IT-асистент: approved context → model proposal → deterministic permission/approval gate → support tool. Модель пропонує дію; тільки gate дозволяє виконання в межах allowlist, user permissions і required approval. Приклад передбачає відсутність обхідного шляху; за недоступного gate дію відхиляють і пропонують ручний шлях. Схема показує конкретний tool-action path, не універсальну топологію всіх Thinking Systems і не гарантію семантичної коректності довільного тексту. User-facing answer path потребує власних scoped controls.\nНижній цикл: Observe збирає outcomes, incidents, затримку, fallback load, стан gate, bypass attempts, execution/effects корекцій. Compare/authorize зіставляє їх із явно показаними Approved operating limits; відповідальний Controller або людина вирішує, що дозволено змінити. Apply correction виконує rollback/disable/manual fallback у межах delegated authority. Зворотний зв’язок показує зміну operation; технічно correction може діяти на routing, tool access, model/configuration або реалізацію gate. Наступне спостереження підтверджує, чи action справді виконано й мало потрібний ефект.\nArchitect визначає enforced boundary, permissions, isolation, telemetry, decision rights, ефективні actuators, час реакції та fallback capacity. Prompt або probabilistic semantic detector сам собою не є Hard Constraint. Прямий deterministic gate може давати scoped hard claim тільки з перевіреним complete path та явними припущеннями. Developers реалізують і тестують paths; QA перевіряє bypass, degradation, false blocks і recovery; operational owner має повноваження та runbook.\nProject Manager планує operational ownership, rehearsal і залежності, а не закриває проект після deploy. Зміна в межах delivery authority допускає локальну корекцію; розширення tool authority, population чи invalidated business/control assumptions повертається до project reauthorization. Автоматичне відхилення/rollback не повинно непомітно розширювати повноваження.\nАрхітектор проектує, де саме дозволена невизначеність і де рішення має бути enforced до наслідку. Для IT-асистента можна дозволити різні пояснення approved knowledge, але окремо перевіряти tool authority, доступ до даних та обов’язкове approval. Синтаксичний validator не доводить правильність змісту, а semantic evaluator також помиляється. Закритий feedback loop не є автоматично доказом безпеки: оцінка може бути неправильною, реакція запізнілою, а actuator — недієвим.\nДо архітектурної відповідальності входять vendor/model changes, isolation boundaries, telemetry та конфігураційний rollback. Provider abstraction відокремлює контракт застосунку від конкретного API, але заміна provider не зберігає поведінку автоматично: потрібні нові evidence та рішення у відповідному scope. Human-in-the-loop означає людину з контекстом, повноваженнями, компетентністю, часом і пропускною здатністю, а не кнопку approve.\nДля кожного material signal визначаємо допустимий час реакції й спостережуваний ефект корекції. Якщо шкода може настати раніше, ніж надійде feedback, потрібний придатний попередній gate, менша authority або відмова від такого шляху. Fallback — конкретний режим: approved static guidance, ручний support або зрозуміла відмова, з перевіреною місткістю. Він має зменшувати наслідки, а не повторювати ту саму неперевірену генерацію під іншою назвою.\nАрхітектурне veto — обґрунтований висновок, що в даному scope немає достатнього контролю, evidence, економіки чи operational capacity. Архітектор документує цей висновок і вимагає звуження, redesign або зупинки відповідно до призначених decision rights. Це не довільне одноосібне право розширювати бізнес-політику. Уповноважений project owner приймає рішення про життєздатність і можливе подальше bounded research.\n\nHuman-in-the-loop є архітектурною залежністю сам по собі, а не фразою «людина перевірить». Потрібні призначені люди, компетентність, контекст для рішення, доступність, реальне право зупинити або змінити роботу, робочий інструмент, response time, звичайна й пікова пропускна здатність, підміна та режим при перевантаженні. Людина не обов’язково схвалює кожний запит: політика визначає точки та умови участі. На схемі люди беруть участь у Controller / authority, а також можуть виконувати дію. Повний контур пов’язує approved limits з Observe, Decide/authorize, Apply correction та наступним спостереженням за ефектом. Permission gate перед tool execution зберігає власну fail-closed поведінку. Окремо від цього повнота зворотного зв’язку не доводить коректність semantic evaluator або стабільність системи. Якщо навантаження, latency чи human-review demand неможливо надійно оцінити до запуску, архітектор має визначити гіпотезу та спершу перевірити доступні sandbox/shadow варіанти. Обмежений canary у production припустимий лише за окремим дозволом, в допустимій області ризику, з реально працюючими sensors, authority, stop/fallback, обмеженням population, duration, tools, spend та швидкості exposure. Canary не замінює архітектуру й не виправдовує порушення hard prohibition. Якщо немає дієвого керування або допустимого способу виміряти ризик, AI path слід заблокувати, звузити чи відкласти. Невизначеність також надходить з економіки та зовнішнього провайдера: ціна токенів, потреба в повторних викликах та evaluations, вартість human review, latency, доступність, непрозорі зміни model weights/routing/configuration можуть змінити поведінку та unit economics без локального коміту. Це можливі джерела змін, а не твердження, що кожний провайдер змінює все без попередження. Provider abstraction ізолює інтеграцію, але не доводить поведінкову еквівалентність моделі-замінника. Для змін потрібні спостереження, повторна оцінка та можливість rollback/disable/manual fallback в межах повноважень. Архітектор формує інженерний висновок про життєздатність, Product та уповноважені бізнес-особи погоджують допустимий ризик, а PM забезпечує operational model і залежності.\n\nІнтеграція старих слайдів 14 та 15 (PDF pages 15–16): Designing Stochastic Resilience і System Boundary States. Верхня схема робить containment видимим: model proposal → semantic monitor → controller / enforcement → дозволений delivery або execution. Approved limits є reference; semantic monitor є fallible Sensor; Decide + enforce об’єднує на навчальній схемі рішення Controller та реалізацію gate, а не ототожнює їх у доктрині. Детермінований permission/approval check перед tool execution зберігається. При порушенні або недоступному критичному контролі stop/isolate переводить запит у наперед визначений fallback: актуальна затверджена cached answer, safe template, human review або зрозуміла відмова. Cache не є автоматично безпечним: його доступність, актуальність, контекст і права також перевіряються. Якщо навіть fallback непридатний, потрібна відмова чи зупинка, а не мовчазне виконання. Semantic monitor не гарантує виявлення всіх небезпечних змістів.\nObserve збирає delivery outcomes, fallback outcomes, наслідки застосованої корекції, incidents і здоров’я самого контуру; зворотний зв’язок запускає уповноважений review, корекцію rules/configuration/versions та наступну перевірку ефекту. Інциденти оновлюють Golden Set / regression, prompts за потреби, критерії Eval Gates, monitoring thresholds і escalation policy у межах повноважень. Це розвиток існуючих контролів, не обов’язково новий окремий сервіс. Human authority є частиною Controller/approval та може виконувати Actuator; нижній рядок залишає власника, контекст, час, місткість і підміну як реальні архітектурні залежності.\nПраворуч видно три джерела невизначеності зі старого слайда: latency overhead від перевірок та ескалації; економіка token / retry / evaluation / human-review cost; непрозорі provider-side зміни моделі чи routing, що можуть змінювати поведінку без local code commit. Їхній спільний ефект може зробити систему непридатною у заданому scope. Архітектор формує обґрунтований veto-висновок і передає рішення про звуження/redesign/зупинку уповноваженому власнику. Критична обов’язкова заборона не обмінюється на економічну вигоду. Невідоме навантаження можна досліджувати в обмеженому дозволеному canary тільки з уже працездатним control path, stop/fallback, власниками, ресурсними та exposure limits. Canary не легалізує відсутність керування. Попередні схеми IT-assistant action path, повний контроль та всі застереження збережені в попередніх нотатках.\n\nПоточне уточнення 23 вересня 2026:\nПоправка до попередньої композиції: три pressures НЕ є причиною або формулою архітектурного вето. Вето спирається на неможливість побудувати й обґрунтувати достатньо надійний, дієвий та операційно здійсненний повний контур для погоджених меж і наслідків. Це може бути missing/late evidence, authority без effective actuator, correction поза consequence window, відсутній credible enforcement або номінальний HITL. Три джерела складності показано окремо: latency/людська capacity, змінна ціна токенів та контролю, непрозорі vendor changes. Вони ускладнюють роботу архітектора й можуть змінити assumptions, але не підмінюють оцінку контрольованості. Центральна схема адаптує старий Architect slide: весь інженерний периметр містить model-mediated process, approved boundaries і realizations, Sensor, Controller, Actuator та substantive Human Authority. Людина не зовнішній чекбокс: потрібні competence, context, права, response time, peak capacity та backup. Показані логічні функції, не обов’язкові окремі сервіси. Семантичний evaluator лишається fallible, а права на tool action реалізуються детермінованими permission/approval gates. Спостерігаємо як бізнес-результат, так і control health та ефект корекції. Для невідомого load спершу sandbox/shadow, а production canary — лише окремо дозволений bounded trial з працездатними controls, scope/exposure limits і stop/fallback. Якщо потрібного control path немає, canary не легалізує production. Архітектурний висновок та project authorization мають належного owner.\n\nКритичний перегляд зв’язності та ролей, v14, 23 вересня 2026:\nАрхітектор не є одноосібним власником усієї системи. Architect + Dev проектують та реалізують повний control path; QA перевіряє failure modes, недоступність evaluator / людини та результат втручання; business / risk owner задає дозволені межі й delegation; service owner / operations забезпечує responders, monitoring, capacity, backup та recovery у роботі. Project Manager узгоджує залежності, бюджет і строки цих результатів. Product / PO вирішує, чи залишився достатній value у звуженому scope; security / privacy specialists потрібні там, де відповідні наслідки суттєві. Архітектурний veto — виявлення неприйнятної технічної або операційної здійсненності; організаційні повноваження на stop/release мають бути названі, а не припущені за назвою посади.\nHuman Authority потребує evidence і контексту для рішення, компетенції та реального права впливати. Черга ескалацій, час реакції, duty coverage та резервний шлях — параметри системи. Номінальне human approval без часу й можливості зрозуміти ситуацію не є credible control. Для support assistant недоступний фахівець веде до погодженого hold / fallback / refusal, а не автоматичного розширення дій моделі. Усі signals та корекції мають перевіряти фактичний ефект. Перехід до 13: якщо люди, їхні знання й capacity є залежностями системи, їхня організація стає частиною роботи Project Manager.\n\nПоточне пояснення: наскрізний приклад і рішення.\nУ схемі proposal відокремлено від delivery/execution. Перевірка прав, scope дозволеного tool call і потрібного approval працює перед дією; рішення моделі саме по собі не може надати їй нові повноваження. У разі відмови або недоступності gate цей шлях відхиляє дію й використовує safe fallback. Контекст і retrieval також мають поважати access controls: не слід спочатку передавати моделі чужі дані, а потім покладатися лише на output judge. Доступні deterministic checks гарантують лише перевірювані властивості власної реалізації та trusted boundary, не всі семантичні наслідки природної мови. Semantic evaluation і human review можуть помилятися, тому дизайн обмежує authority/exposure і перевіряє реальну ефективність.\n\nПісля виконання sensor спостерігає outcome і control health, controller вирішує в межах delegated authority, actuator може зупинити або звузити подальшу роботу чи вимкнути tool. Human Authority має evidence/context, компетенцію, decision rights, доступний час, peak capacity і backup. Людина залучається там, де цього вимагає approved design, а не до кожної відповіді. Схематичний зв’язок з gate означає required approval, не обхід checks. Уже розкриті дані feedback або rollback не повертає; rollback придатний лише до оборотних змін.\n\nПропорційність: draft для компетентної людини перед використанням має іншу authority та reversibility, ніж автономна зміна доступу. Навіть draft може розкривати дані, тому access boundary лишається. Для автономної дії потрібні перевірки дозволів і required approval перед effect, дієздатний containment та response. Лише назва HITL не робить шлях керованим. Latency, людська спроможність, full token/evaluation/review costs і opaque vendor changes перевіряють в економіці та operability. Якщо обов’язковий контроль не можна реалізувати або забезпечити response capacity — звузити scope, змінити архітектуру чи відмовитися від цього AI path. Bounded trial допустимий тільки з working controls, exposure limits і stop criteria.",
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
  "veto": "Required control cannot be made reliable and operable within the approved boundaries?",
  "humanHeading": "HUMAN IN THE LOOP IS AN ARCHITECTURAL DEPENDENCY",
  "humanDetail": "Evidence, decision rights,\ncompetence, time and capacity",
  "trialRule": "Unknown load: bounded trial with working controls, exposure limits and stop criteria.",
  "trialLimits": "Canary limits exposure. If the control path is missing, block the AI path.",
  "flowHeading": "RUNTIME CONTAINMENT + FEEDBACK",
  "runtime": [
    "Model\nproposal",
    "Semantic\nmonitor",
    "Decide +\nenforce gate",
    "Deliver /\nexecute"
  ],
  "stop": "Stop / isolate",
  "fallback": "Deny / safe fallback",
  "observe": "Observe\n+ verify effects",
  "feedback": "Review + authorize corrections → update rules / versions → re-evaluate effects",
  "pressures": [
    [
      "Latency + human capacity",
      "Will detection and intervention be timely?"
    ],
    [
      "Token + control costs",
      "Calls, evaluation and review demand vary."
    ],
    [
      "Opaque vendor changes",
      "Behavior may change without a local commit."
    ]
  ],
  "perimeterHeading": "IT ASSISTANT: CONTROL BEFORE ACTION AND AFTER DEPLOYMENT",
  "core": "Model + tools\nBusiness action",
  "sensor": "Observe behavior\nand control health",
  "controller": "Decide within\nauthorized limits",
  "actuator": "Stop / narrow\nDisable tools",
  "human": "Human authority\nwhen required",
  "vetoHeading": "ARCHITECTURAL VETO",
  "vetoAction": "Cannot enforce the boundary or staff the response? Narrow, redesign or reject this path.",
  "vetoDetail": "Missing evidence, ineffective intervention or nominal human oversight can block production.",
  "complexityHeading": "WHY THIS DOMAIN IS HARD",
  "gateLabel": "Denied or\nunavailable",
  "controlCaveat": "Check access before disclosure. Feedback cannot undo an irreversible effect.",
  "proportionHeading": "CONTROL DEPENDS ON CONSEQUENCE, AUTHORITY AND REVERSIBILITY",
  "proportion": [
    [
      "DRAFT FOR HUMAN REVIEW",
      "Human accepts before use."
    ],
    [
      "AUTONOMOUS ACCESS CHANGE",
      "Enforce rights and required approval first."
    ]
  ]
}
```

**Час:** 3:00.

**Композиція:** Повний bounded control perimeter із моделлю, evidence, decision/authority, corrective action та явним людським компонентом. Праворуч окрема умова architectural veto. Нижче окремо три джерела складності архітектора, без причинної стрілки pressures → veto.

**Рольова зміна:** Architect визначає boundary, complete enforcement path, assumptions, sensing, authority та effective correction. Developers реалізують, QA перевіряє degradation/bypass/recovery, operational owner діє; Project Manager планує ownership і capacity. Це scoped example, а не універсальний deployment diagram або гарантія всіх semantic outputs.

**Перехід:** «Такий продукт потребує іншого наповнення командного процесу, а не лише нового компонента в архітектурі».

**Поглиблення змісту:** До попереднього operational loop додаємо vendor/model changes, isolation, реальну human-response capacity та fallibility semantic checks. Окремо видно підставу звузити або зупинити AI path, якщо control/economics не підтверджені; у нотатках — reaction time та обмеження feedback.


**Уточнення 22 вересня:** Human-in-the-loop є архітектурною залежністю сам по собі, а не фразою «людина перевірить». Потрібні призначені люди, компетентність, контекст для рішення, доступність, реальне право зупинити або змінити роботу, робочий інструмент, response time, звичайна й пікова пропускна здатність, підміна та режим при перевантаженні. Людина не обов’язково схвалює кожний запит: політика визначає точки та умови участі. На схемі люди беруть участь у Controller / authority, а також можуть виконувати дію. Повний контур пов’язує approved limits з Observe, Decide/authorize, Apply correction та наступним спостереженням за ефектом. Permission gate перед tool execution зберігає власну fail-closed поведінку. Окремо від цього повнота зворотного зв’язку не доводить коректність semantic evaluator або стабільність системи. Якщо навантаження, latency чи human-review demand неможливо надійно оцінити до запуску, архітектор має визначити гіпотезу та спершу перевірити доступні sandbox/shadow варіанти. Обмежений canary у production припустимий лише за окремим дозволом, в допустимій області ризику, з реально працюючими sensors, authority, stop/fallback, обмеженням population, duration, tools, spend та швидкості exposure. Canary не замінює архітектуру й не виправдовує порушення hard prohibition. Якщо немає дієвого керування або допустимого способу виміряти ризик, AI path слід заблокувати, звузити чи відкласти. Невизначеність також надходить з економіки та зовнішнього провайдера: ціна токенів, потреба в повторних викликах та evaluations, вартість human review, latency, доступність, непрозорі зміни model weights/routing/configuration можуть змінити поведінку та unit economics без локального коміту. Це можливі джерела змін, а не твердження, що кожний провайдер змінює все без попередження. Provider abstraction ізолює інтеграцію, але не доводить поведінкову еквівалентність моделі-замінника. Для змін потрібні спостереження, повторна оцінка та можливість rollback/disable/manual fallback в межах повноважень. Архітектор формує інженерний висновок про життєздатність, Product та уповноважені бізнес-особи погоджують допустимий ризик, а PM забезпечує operational model і залежності.

**Уточнення за старими слайдами 14–15 (PDF pages 15–16):** Native runtime flow розгалужується після порівняння/дозволу на delivery або stop/isolate → safe fallback/human review/refusal; спостереження запускає дозволену корекцію й повторну перевірку. Праворуч умова вето відокремлена від джерел складності: необхідний надійний та операційно дієвий контур має бути здійсненним. Latency, token/review economics і opaque vendor changes пояснюють складність домену. HITL лишається архітектурною залежністю, canary потребує вже працездатних controls.

## 13. The Roles Move With the System

```pptx-slide
{
  "number": 13,
  "layout": "roles",
  "role": "PROJECT MANAGER · Product / PO · BA · QA · Dev · Architect · Operations",
  "steps": [
    "Hypothesis",
    "Bounded trial",
    "Evidence",
    "Decision"
  ],
  "cycle": "Adapt or stop; production evidence feeds the next iteration.",
  "table": [
    [
      "SHIFT",
      "HOW WE BUILD",
      "WHAT WE BUILD"
    ],
    [
      "New balance",
      "Faster generation shifts bottlenecks\nReview, integration and team understanding",
      "Probabilistic behavior enters the product\nEvaluation, control and incident feedback"
    ],
    [
      "New work",
      "Rebalance capacity, review and learning\nProtect ownership and recovery capability",
      "Assign evaluation and response ownership\nPlan for model changes and human capacity"
    ]
  ],
  "takeaway": "Delivery includes the ability to understand, evaluate and recover the system.",
  "notes": "Стара презентація Designing Non-Deterministic Systems, slide 20 Welcome to the Laboratory, дає педагогічну метафору Hypothesize → Measure → Adapt. Тут не стверджуємо, що Scrum або попередня інженерія не були емпіричними. Процес додає явно керований цикл поведінкових гіпотез, measurement та адаптації поряд зі звичайним delivery. Titles/order цієї 14-slide доповіді збережено.\nProject Manager відрізняється від Product Manager. Product разом із BA та бізнесом уточнює цінність, наслідки й acceptance; Project Manager організовує delivery і навчання: stakeholder availability, dependencies, доступ до даних/domain experts, evaluation cost, час на аналіз і remediation, decision latency, release/operations readiness. Він не стає одноосібним власником risk acceptance.\nPlanning: backlog містить не тільки features, а й перевірювані невідомі, наприклад «чи достатньо approved knowledge для типових support cases?». Для trial фіксуємо питання, hypothesis, evidence plan, ресурсну межу, owner і stop condition; якщо треба — погоджений обмежений scope до остаточних tolerance. Sprint review: разом зі working software показуємо versioned evidence, проблемні групи, consequences, uncertainty та unresolved decisions. Результат може бути accept, redesign, narrow, bounded further trial або stop. Це корисний результат роботи, а не автоматична невдача спринту, якщо доказано, що задум нежиттєздатний.\nRelease/operate: окремо від Done підтверджуємо authorization конкретного rollout, monitoring, on-call/ручний шлях і їхню місткість; runtime evidence повертає backlog і за потреби project reauthorization. Не рахувати кількість проведених експериментів як цінність саму по собі: прогрес — робоча capability, зменшення матеріальної невизначеності та прийняте рішення. Один живий review artifact і звичні командні події можуть містити ці записи; не потрібні нові ролі або комітет.\nРозподіл 9–13: Product + BA формулюють acceptance; QA + Developers роблять measurement; Developers доставляють evidence/recovery package; Architect замикає bounded control; Project Manager координує весь цикл, рішення, бюджет і залежності.\nФабрика й лабораторія співіснують. Команда продовжує постачати перевірені deterministic features, але для поведінкових невідомих спочатку формулює гіпотезу й план evidence. Робочий приклад: «Чи достатньо approved knowledge, щоб асистент корисно обробляв типові IT-звернення без вигаданих кроків у допустимих межах вартості та затримки?». Експеримент може показати, що потрібні нові знання, інший scope, ручний support або взагалі інше технічне рішення.\nProject Manager закладає в план підготовку даних, час domain experts, evaluation runs, аналіз, реалізацію controls і rehearsal. Фіксує resource/time box дослідження та decision date. Можна погодити термін отримання evidence й рішення, але не видавати невідому feasibility за гарантовану production capability. Після trial команда уточнює прогноз, scope і залежності; це кероване перепланування за новими даними.\nНа planning розділяємо work із відомим способом реалізації та material unknowns. На sprint review поряд із demo показуємо baseline/candidate, проблемні сценарії, cost/latency, evaluator uncertainty і рішення. На retrospective перевіряємо, які припущення та засоби вимірювання підвели. Production incidents повертаються в Golden Set, backlog і review тієї межі, яка виявилася неадекватною. Звичайні Scrum events можуть бути цими контрольними точками без створення окремої бюрократії.\nНегативний експеримент є корисним, коли він закриває важливе питання й змінює рішення, а не просто збільшує лічильник проведених дослідів. Кількість tickets, LOC або красивих demo окремо не описує готовність до відповідальної експлуатації.\n\nЦе синтез попередніх слайдів у портрет майбутнього Project Manager, а не нова назва Product Manager. Фундамент не зникає: project management theory, планування, ризики, залежності, бюджет, комунікації, stakeholders і delivery залишаються. До нього додаються горизонти, що співіснують. Перший — AI-assisted SDLC. Кодогенерація змінює співвідношення швидкості створення, review, QA, integration та людського розуміння. PM має розуміти систему, якою керує, бачити зміну bottleneck і разом із командою знаходити новий баланс. Ми не знаємо універсального нового equilibrium наперед: його перевіряємо end-to-end flow, review queues, rework, stability та здатністю людей пояснити й відновити систему. Другий — побудова агентних/Thinking Systems як додаткова інженерна дисципліна: probabilistic judgment є частиною runtime, тому requirement, evaluation, control design та operating model стають частиною проєктованої системи. Люди з їхніми правами, компетенціями, latency й capacity входять до її інженерного периметра. Третій — управління цією роботою: PM розуміє, як змінилися завдання Product/BA, QA, developers і architect, хто виробляє докази, хто приймає рішення, хто вміє застосувати корекцію. PM має бачити пропущені функції, нерозв’язані залежності та неузгоджений поділ відповідальності, принаймні робити їх видимими, організовувати рішення й моніторити стан. Потрібна статистична грамотність: відрізняти частоту від наслідку, точкову оцінку від невизначеності, coverage від кількості повторів, sample від production population, correlation від causality. Це не робить PM одноосібним статистиком, QA, архітектором або власником бізнес-ризику. Практичні метрики доповнюють delivery: частка неприйнятних результатів за сценаріями та тяжкістю, task success за погодженим rubric, cost per accepted outcome, latency, частка і черга ескалацій, response time, доступність контролів, результативність stop/fallback, incident recurrence. Вони мають denominators, період, сегмент, active version, межу та owner реакції. Система не стає коректною через один aggregate score. Попередній цикл Hypothesis → Bounded trial → Evidence → Decision залишається механікою: у planning визначаємо evidence gap, бюджет, owner і stop condition; на review приймаємо рішення з Product/BA, QA, Dev та Architect; після release стежимо за authorization і capacity. Приклад trial для IT-асистента: чи може він використовувати затверджені знання без вигаданих кроків. Дослідження обмежене в часі до обіцянки production capability. Прогрес — working capability, reduced uncertainty та явні рішення.\n\nПоточне уточнення 23 вересня 2026:\nЕволюція PM означає глибше розуміння нової реальності праці, без заміни його класичного професійного фундаменту. Він має знати, що змінилося у вимогах, роботі BA/Product, developer, QA та architect, які нові результати роботи потрібні і де організація команди їх не забезпечує. Конкретний приклад maintainer: AI швидко генерує невеликий компонент мовою, якої команда не знає. Компонент росте й стає бізнес-критичним, але з початку не було компетентного code review, knowledge owner або здатності діагностувати й виправляти його без цього генератора. Тут є вже наявний issue — прогалина компетенції, ризик від її зростання та dependency для готовності: потрібна доступна експертиза й перевірене розуміння до розширення criticality. PM разом із технічними owners робить цю залежність видимою, призначає owner, дату/trigger, план training/pairing/hiring або звуження stack/scope, і критерій закриття. Свідчення закриття — змістовне review, пояснення design/trade-offs і recovery exercise відповідального інженера, а не позначка «AI написав тести». Не потрібен окремий новий реєстр: використовуємо чинні risk/dependency/backlog механізми.\nДодаткові ризики для PM: (1) output випереджає набуття компетенції; (2) великі generated batches перевантажують review й затримують feedback; (3) нові бібліотеки/сервіси несуть supply-chain, security та maintenance зобов’язання, які слід передати компетентним owners; (4) одночасне генерування реалізації й тестів за одним неперевіреним припущенням може залишити blind spot — це інженерний сценарій, не виміряна тут частота; (5) prototype-to-production promotion непомітно збільшує consequence і ownership burden; (6) модель, agent instructions, environment/configuration та vendor availability впливають на відтворення й recovery. Для Thinking Systems додаються competence/capacity людського контуру, якість оцінювання, drift, помилки різної тяжкості, повна вартість accepted outcome і час реакції. PM організовує рішення, а не сам погоджує всі бізнес-ризики й архітектуру.\nДжерела перевірено 23 вересня 2026. Shen & Tamkin / Anthropic, January 2026: контрольований експеримент з незнайомою Python-бібліотекою показав слабше негайне засвоєння в AI-групі; невелика вибірка, короткий горизонт, інший інструментальний setup — не доказ багаторічної втрати навичок команди. Спосіб використання AI має значення; qualitative interaction patterns не встановлюють causal effect. DORA Working in small batches пояснює review/test/integration burden великих generated changes; практики були потрібні й раніше. Spracklen et al., USENIX Security 2025 документують вигадані package names та supply-chain mechanism для досліджених моделей/мов; не переносимо відсотки на нинішню команду чи всі моделі. Управлінські дії та scenario про невідомий stack — наш синтез цих сигналів і прикладу maintainer, не висновок одного дослідження.\n\nКритичний перегляд зв’язності та ролей, v14, 23 вересня 2026:\nProject Manager з’єднує роботу Product Manager / Product Owner, BA, Dev, QA, архітектора, service owner та уповноважених decision owners. Він не отримує автоматично право визначати product value, переписувати технічні межі або приймати business risk. Його робота — зробити залежності й пропуски видимими, отримати власника, час і evidence, домогтися рішення належної особи. У Scrum це окремо від відповідальності Scrum Master за Scrum та ефективність команди; наявність окремої посади Project Manager не є вимогою Scrum або UA.\nОбидва горизонти зводимо до корисного результату. HOW: review queues / rework ростуть — команда з Project Manager переглядає WIP, batch size, reviewer coverage та scope. WHAT: human escalation queue чи response time виходить за погоджені межі — service / release owner вирішує щодо capacity, exposure, fallback чи stop, Product / PO переоцінює value та пріоритети. Project Manager забезпечує своєчасність цих рішень. Більше коду та кращий eval score самі по собі не доводять більшої продуктової цінності. Перехід до 14: одне погодження не закриває невизначеність назавжди; потрібен повторюваний командний цикл evidence → decision → adaptation.\n\nПоточне пояснення: наскрізний приклад і рішення.\nWHAT-стовпець тепер показує результат координації: погоджені критерії, компетентний domain reviewer, визначений responder із перевіреною спроможністю та evidence, достатня для рішення. Для IT-асистента відсутність такого responder або невиконаний privacy criterion є delivery dependency, яку не закриває демонстрація working code. Project Manager організовує owner, час і proof of closure, але не підмінює продуктову, технічну або risk authority. На HOW так само потрібні qualified reviewer та людина, здатна підтримати й відновити незнайомий компонент. Existing people можуть поєднувати ці відповідальності. Не створюємо обов’язкового нового headcount чи комітетів.\n\nПоточне пояснення: два зсуви та статистичні умови delivery.\nОсновна теза: одночасно змінюються HOW — система delivery, її bottlenecks і баланс — та WHAT — продукт, у якому runtime judgment частково ймовірнісний. Саме їхній спільний вплив змінює ролі, розподіл роботи, feedback cadence й операційну модель. Геп експертизи — один ілюстративний наслідок, а не тема всього слайда.\n\nHOW: прискорення generation не означає однакового прискорення review, integration, validation або team understanding. Потрібно бачити поточне constraint, WIP / queues / rework, якість review, ability to maintain/recover та зміну навантаження; перевіряти локальний evidence, а не проголошувати універсальне падіння productivity. Це може вимагати інших batch sizes, capacity allocation, learning time, ownership і delivery commitments. WHAT: evaluation, monitoring, drift/provider/model changes, full operating cost і timely human response стають частиною повсякденної роботи. QA, Product / PO / BA, architect/engineers та service owners переузгоджують критерії, evidence, authority й handoffs; назви відповідальностей не зобов’язують створювати нові посади.\n\nНовий напрям роботи PM — підтримувати придатність operating model під ці зміни: розуміти механізм двох зсувів, регулярно аналізувати bottlenecks і нові dependencies, добиватися owner / часу / capacity / evidence для їх закриття й адаптувати план та спосіб роботи разом із профільними власниками. PM не стає одноосібним technical чи risk authority, але відповідає за інтеграцію залежних рішень у delivery. Це практичний напрям розвитку ролі, а не універсальна нова job description.\n\nПриклад: генератор швидко додає код на незнайомій команді мові. Невелика частина стає critical dependency, а qualified review / maintenance / recovery coverage не зростає разом із нею. Expertise gap впливає на оцінки, acceptance, терміни, operational recovery і клієнтські commitments, тому його слід трекати як delivery dependency. PM разом із tech owner погоджує closure plan: навчання, reviewer/backup, staffing, звуження scope або заміна технології, потрібний час і доказ реальної спроможності. Інші приклади того самого класу — недостатня eval capacity, model/provider dependency, response staffing, review queue і latency/cost envelope. Старі scope / schedule / cost / risk / stakeholder responsibilities зберігаються, але їхній предмет суттєво розширюється.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/01-patterns/thinking-system-review.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/00-doctrine/nested-control-lifecycle.md",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=20",
    "https://www.anthropic.com/research/AI-assistance-coding-skills",
    "https://arxiv.org/abs/2601.20245",
    "https://dora.dev/capabilities/working-in-small-batches/",
    "https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen"
  ],
  "process": "Delivery now includes experiments, evaluation time and decisions about feasibility.",
  "trial": "Trial: can approved knowledge answer routine cases without unsupported steps?",
  "planningRule": "Time-box the investigation before promising production capability.",
  "foundation": "Two shifts change the delivery system, its roles and operating model.",
  "statisticalLiteracy": "Ask: is the sample relevant, how uncertain is it, and what decision does it support?",
  "roleBoundary": "Project Manager coordinates decisions. Product, technical and risk owners retain authority.",
  "caseHeading": "ONE NEW DEPENDENCY: EXPERTISE",
  "caseSteps": [
    "AI adds code in a language\nthe team does not know",
    "The component becomes\na critical dependency",
    "A review and recovery gap\nnow threatens delivery"
  ],
  "caseAction": "Expertise gaps affect estimates, acceptance and recovery, so they belong in the delivery plan.",
  "pmHeading": "PM RESPONSIBILITY: KEEP THE OPERATING MODEL FIT FOR DELIVERY",
  "pmAction": "Track new bottlenecks and dependencies. Secure owners, capacity and closure evidence."
}
```

**Час:** 2:00.

**Композиція:** Фундамент PM, конкретний сценарій зростання компонента без експертизи, native table HOW / WHAT через expertise, evidence/flow та decision dependencies. Прогалина знань має owner, trigger та closure evidence.

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
        "Product / PO + BA: approved acceptance",
        "QA + Dev: calibrated evidence",
        "Architect: effective control paths",
        "Release owner: scope + residual risk",
        "Service owner: operability + response"
      ]
    ]
  ],
  "cycle": "Team process: hypothesize → measure → decide → adapt",
  "takeaway": "First step: one access-recovery workflow, approved limits and a rehearsed support fallback.",
  "closing": "More capability still requires engineering responsibility.",
  "titleLines": [
    "Engineering Rigor Moves —",
    "It Doesn’t Disappear"
  ],
  "notes": "Повертаємо HOW і WHAT із першого слайда, тепер із конкретними ролями й процесом. HOW: швидше створювати код недостатньо — команда зберігає comprehension та ownership, Project Manager організовує flow, evidence, залежності та рішення. Малими партіями й обмеженими експериментами перевіряємо невідомі. WHAT: Product + BA узгоджують acceptance з бізнесом; QA + Developers створюють калібровані докази й реалізацію; Architect проектує ефективні control paths; уповноважений release owner приймає scope і residual risk у своїх межах. Це розширення, а не вичерпні нові job descriptions або передача відповідальності одній ролі.\nГоловна зміна процесу: hypothesize → measure → decide → adapt, з робочим software, явними business outcomes і runtime feedback. Детерміновані requirements, tests та delivery discipline залишаються; додається контроль варіативної поведінки і наслідків. Немає нових чисел, нової архітектурної нормативності чи реклами UA.\nФінал: «AI розширює наші можливості. Команда все одно відповідає за систему цілком: як ми її будуємо, яку поведінку дозволяємо, на яких доказах випускаємо і як виправляємо відхилення». Пауза, Q&A.\nКонкретний перший крок для команди: обрати один AI workflow із реальним бізнес-наслідком. Узгодити корисний результат, дозволену варіативність, неприйнятні наслідки, cost/latency та escalation. Підготувати невеликий початковий Golden Set із domain experts, перевірити evaluator й розширювати evidence відповідно до рішення та ризику, без універсального мінімального sample size. Зв’язати Eval Gate з дозволеним block/canary/release, перевірити fallback і людину, яка зможе діяти.\nСаме тут поєднуються дві половини доповіді. HOW: команда має розуміти реалізацію, докази, обмеження і способи відновлення навіть за великого обсягу AI-generated code. WHAT: оскільки частина поведінки формується під час роботи, специфікація, тестування і відповідальність продовжуються через runtime evidence та контроль. Відповідальність не переноситься на модель або на одного QA; вона проходить через узгоджені boundaries, evidence, authority і реальну здатність змінити роботу системи.\n\nФінал збирає HOW we build та WHAT we build через лабораторний цикл зі старого слайда 20. Звичний delivery cycle Plan → Build → Verify → Ship залишається. Лабораторний цикл додає гіпотезу, обмежений експеримент, вимірювання, рішення й адаптацію; нові дані повертають команду до наступної гіпотези. Scrum уже містить емпіризм та адаптацію, тому ми не оголошуємо їх винаходом AI. Змінюється те, що саме треба вимірювати й керувати: поведінкова варіативність, доказова база, operational control і людська частина системи. Для HOW we build цей підхід потрібен, поки команда перевіряє, як AI code generators змінюють її звичний SDLC, де виник bottleneck, чи є реальне покращення end-to-end delivery та чи зберігаються understanding/ownership. Порівнюємо сумісні типи задач і умови, не приймаємо більше generated lines за delivery improvement. Для WHAT we build — Thinking Systems — цикл триває весь час роботи, бо змінюються входи, usage, дані, поведінкові конфігурації та зовнішні залежності. Production evidence й incidents оновлюють Golden Sets, regression, Eval Gates, monitoring та рішення про scope. «Лабораторія не закінчується» означає постійне навчання й reassessment, а не безперервні неконтрольовані експерименти над користувачами: кожний trial має дозвіл, межі та stop/fallback. З попереднього HOW/WHAT лишаються всі відповідальності: команда — comprehension та ownership; Project Manager — evidence і flow; Product/BA — agreed acceptance; QA/Dev — calibrated evidence; Architect — effective control paths; release owner — scope та residual risk. Перший практичний крок лишається: один workflow, погоджені tolerances, калібрований Golden Set, Eval Gate і відрепетируваний fallback. Оцінюємо рішення та наслідки, не лише демонстрацію. Більше capability не скасовує engineering responsibility.\n\nПоточне уточнення 23 вересня 2026:\nМаксимально адаптовано зміст старих Welcome to the Laboratory (PDF20) та FINAL OPERATING MODEL (PDF22). Збережено звичний delivery і додано постійний empirical loop: гіпотеза та погоджені межі, bounded experiment, measurement/comparison, decision/adaptation. Межі й stop criteria існують до експерименту. Model variance та зміна умов повертають нас до гіпотези, а production outcomes й incidents продовжують цей цикл. Командна операційна модель конкретна: planning формулює питання, owner, budget/time і needed evidence; daily work versionує trials і показує blockers/knowledge gaps; review розглядає результати, uncertainty/coverage і рішення accept/narrow/rework/stop; після релізу є monitoring, responders, incident learning та reassessment. Інциденти змінюють regression/Golden Sets, Eval Gates, monitoring і control rules після належного погодження. Scrum вже емпіричний; ми адаптуємо предмет evidence і decision checkpoints, а не оголошуємо винахід наукового методу. Для HOW це спосіб перевіряти новий баланс AI-assisted SDLC, не плутати більше коду з delivery value та зберігати understanding/ownership. Для WHAT це робота протягом усього життєвого циклу, бо model-mediated behavior, inputs, дані й vendor assumptions можуть змінюватись. Лабораторний режим не означає неконтрольованих експериментів над користувачами. Один experiment закінчується рішенням, а здатність команди вчитися, моніторити й переглядати assumptions триває. Наступний слайд дає матеріали й контакти для Q&A.\n\nКритичний перегляд зв’язності та ролей, v14, 23 вересня 2026:\nРолі на фінальному слайді показують провідний внесок на етапі, а не виключне право участі. Planning: Product / PO + BA разом із командою визначають value target, питання, межі, потрібні evidence й owner. Daily work: Dev + QA + Architect будують, versionують trial, перевіряють і закривають gaps; інші потрібні фахівці також залучені. Review: Product / PO оцінює value, команда пояснює evidence й невизначеність, уповноважений release / risk owner ухвалює scope-specific рішення. After release: service owner + responders моніторять, реагують і повертають findings до всієї команди. Project Manager координує залежності та своєчасність рішень у всьому циклі; Scrum Master у Scrum підтримує емпіризм та ефективність командної взаємодії. Це не новий обов’язковий склад команди й не зміна значення Scrum events; зокрема Sprint Review не перетворюється на формальний release gate.\nОбидві частини доповіді сходяться тут: HOW перевіряє реальне delivery improvement із збереженим розумінням; WHAT перевіряє корисні outcomes, допустиму поведінку, дієвий контроль та повну вартість. Experiment завершується рішенням, а learning, monitoring та reassessment тривають. Завершити конкретною дією для аудиторії: оберіть один workflow; назвіть, яку корисну зміну очікуєте; погодьте межі; визначте evidence і decision / service owners; відрепетируйте fallback. Це можна почати з наявними людьми. Наступний ресурсний слайд дає матеріали для такого першого кроку.\n\nПоточне пояснення: наскрізний приклад і рішення.\nПрактичний перший крок після доповіді: обрати один workflow відновлення доступу, визначити observable useful outcome й погоджені межі, призначити існуючих відповідальних за evidence / decisions / operations та відрепетирувати support fallback. Порівняти evidence з погодженими умовами і вирішити continue, narrow або stop. Розмір controls залежить від consequences, authority й reversibility, показаних на 12, а не від вимоги максимальної governance до кожного AI feature. Existing team cadence включає ці рішення в planning, роботу, review й operations. Laboratory loop доповнює delivery commitments; він не є підставою для нескінченного експерименту без критеріїв рішення.",
  "firstStepHeading": "START WITH ONE WORKFLOW",
  "firstStep": "Choose one workflow, a value target, approved limits, evidence and decision owners; rehearse the fallback.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=20",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/content/raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf#page=22",
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/main/01-patterns/thinking-system-review.md",
    "https://scrumguides.org/scrum-guide.html"
  ],
  "factoryHeading": "DELIVERY STILL RUNS",
  "factoryFlow": "Plan → Build → Verify → Ship",
  "factoryDetail": "Delivery commitments and\noperational ownership.",
  "labHeading": "THE LABORATORY STAYS OPEN",
  "labDetail": "Re-evaluate after material changes\nin model, data or authority.",
  "labSteps": [
    "Hypothesis\n+ approved limits",
    "Bounded\nexperiment",
    "Measure\n+ compare",
    "Decide\n+ adapt"
  ],
  "loopCenter": "Production outcomes\nand incidents feed back",
  "applications": [
    [
      "HOW: AI-assisted SDLC",
      "Review throughput, rework and team understanding."
    ],
    [
      "WHAT: Thinking Systems",
      "Useful outcomes, failure impact and full operating cost."
    ]
  ],
  "teamHeading": "EXISTING TEAM CADENCE · Project Manager coordinates decisions",
  "ceremonies": [
    [
      "PLANNING",
      "Product / PO + BA + team\nValue, limits, evidence + owner"
    ],
    [
      "DAILY WORK",
      "Dev + QA + Architect\nBuild, evaluate + close gaps"
    ],
    [
      "REVIEW",
      "Product / PO + release owner\nEvidence → accept / narrow / stop"
    ],
    [
      "AFTER RELEASE",
      "Service owner + responders\nMonitor, recover + learn"
    ]
  ]
}
```

**Час:** 3:00.

**Композиція:** Ліворуч delivery та лабораторна робота, праворуч empirical loop; унизу командні planning/daily/review/operations checkpoints і застосування до HOW / WHAT.

**Фінал:** «AI розширює наші можливості. Команда все одно відповідає за систему цілком: як ми її будуємо, яку поведінку дозволяємо, на яких доказах випускаємо і як виправляємо відхилення».

Детерміновані вимоги, тести та звичайні обов’язки не зникають. Без нових даних чи рекламного фіналу. Пауза, Q&A.


**Поглиблення змісту:** Поряд із збереженим HOW / WHAT додаємо практичний старт на одному workflow: tolerances, calibrated Golden Set, Eval Gate і rehearsed fallback. Це збирає зміни ролей у спільну роботу команди.

## 15. Continue the Conversation

```pptx-slide
{
  "number": 15,
  "layout": "resources",
  "subtitle": "Two parts of the argument. Sources, framework and discussion.",
  "resources": [
    [
      "Uncertainty Architecture",
      "Designing and governing\nThinking Systems",
      "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture",
      "uncertainty-architecture"
    ],
    [
      "The Subprime Code Crisis",
      "AI-assisted delivery, understanding\nand long-term ownership",
      "https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis",
      "The-Subprime-Code-Crisis"
    ]
  ],
  "author": "Vitalii Oborskyi",
  "email": "oborskyivitalii@gmail.com",
  "linkedin": "https://www.linkedin.com/in/vitaliioborskyi/",
  "notes": "Завершальний слайд із двома перевіреними публічними репозиторіями. Uncertainty Architecture — концептуальна рамка, специфікація та практичні матеріали про проєктування й керування Thinking Systems. Не представляємо її як готовий універсальний software engine. The Subprime Code Crisis — дослідницький синтез про AI-assisted delivery, review/QA/architecture/maintenance, людське розуміння й ownership. QR-коди кодують точно надруковані цільові GitHub URL без стороннього redirect. Email і LinkedIn для продовження розмови. Це Q&A ресурсний слайд, який не змінює змістовний фінал 14.",
  "sources": [
    "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture",
    "https://github.com/UncertaintyArchitectureGroup/The-Subprime-Code-Crisis",
    "https://www.linkedin.com/in/vitaliioborskyi/"
  ]
}
```

**Композиція:** Два великі QR-коди з назвами, описами й клікабельними прямими посиланнями. Контакти автора внизу. **Час:** Q&A, без додаткової змістовної секції.

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
| 15 | Q&A |
| **Виступ** | **38:00** |
| **Резерв** | **2:00** |

## Що не змінюємо й не додаємо

Не додаємо окремих слайдів NBER/METR/GitClear, окремих слайдів для кожної ролі, повного UA stack, Prompt Registry, token economics чи рекламного фіналу. За прямим запитом додано нейтральний ресурсний слайд 15 з двома QR-кодами. Не вигадуємо емпіричних чисел для концептуальних слайдів 1–3 і 5–14. Потрібна деталізація змісту погодженої структури, а не нова структура.


**Уточнення 22 вересня:** Фінал збирає HOW we build та WHAT we build через лабораторний цикл зі старого слайда 20. Звичний delivery cycle Plan → Build → Verify → Ship залишається. Лабораторний цикл додає гіпотезу, обмежений експеримент, вимірювання, рішення й адаптацію; нові дані повертають команду до наступної гіпотези. Scrum уже містить емпіризм та адаптацію, тому ми не оголошуємо їх винаходом AI. Змінюється те, що саме треба вимірювати й керувати: поведінкова варіативність, доказова база, operational control і людська частина системи. Для HOW we build цей підхід потрібен, поки команда перевіряє, як AI code generators змінюють її звичний SDLC, де виник bottleneck, чи є реальне покращення end-to-end delivery та чи зберігаються understanding/ownership. Порівнюємо сумісні типи задач і умови, не приймаємо більше generated lines за delivery improvement. Для WHAT we build — Thinking Systems — цикл триває весь час роботи, бо змінюються входи, usage, дані, поведінкові конфігурації та зовнішні залежності. Production evidence й incidents оновлюють Golden Sets, regression, Eval Gates, monitoring та рішення про scope. «Лабораторія не закінчується» означає постійне навчання й reassessment, а не безперервні неконтрольовані експерименти над користувачами: кожний trial має дозвіл, межі та stop/fallback. З попереднього HOW/WHAT лишаються всі відповідальності: команда — comprehension та ownership; Project Manager — evidence і flow; Product/BA — agreed acceptance; QA/Dev — calibrated evidence; Architect — effective control paths; release owner — scope та residual risk. Перший практичний крок лишається: один workflow, погоджені tolerances, калібрований Golden Set, Eval Gate і відрепетируваний fallback. Оцінюємо рішення та наслідки, не лише демонстрацію. Більше capability не скасовує engineering responsibility.
