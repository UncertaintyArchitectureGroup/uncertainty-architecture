# Frozen tasks for the descriptive RI comparison

**Accepted by the maintainer on 2026-09-17 before experimental answers; do not give this file to a tested agent.**

The maintainer's “Ок, погнали” accepts the preceding proposal: these 12 tasks and a descriptive answer-quality comparison despite incomplete connector capture. The implementation-aware organizer prepared adaptations of earlier maintainer request topics. This is a maintainer-approved convenience set, not an independently authored or randomly selected corpus; exact historical message provenance has not been independently established. T01/T07/T10 and T05/T06 overlap. These limitations stay in the report.

Requests and scoring expectations below are frozen. T05 names the standalone publication source; T09 is restricted to navigation/ownership. T08 replaces a historical live-PR question with source-tree inspection. All adaptations preceded experimental outcomes. Required sources were checked at `989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3`.

The [study record](README.md) owns this descriptive comparison's settings and limitations. [sessions.json](sessions.json) contains all 24 exact messages, including the coordinator-supplied repository address, source ref, symmetric bootstrap and arm marker. Those additions are not claimed as original historical wording. No request or scoring expectation may be adjusted in response to experimental answers.

## T01 — Architecture and proportionality

Frozen request: «Прочитай інструкції та структуру репозиторію. Поясни, як RI допомагає агенту орієнтуватися і чи виправдана складність цієї реалізації».

Expected evidence/outcome: RI architecture and implementation; distinguish the compact agent route, graph materialization and owning source files. Separate implemented properties from unproven operational benefit; allow evidence-based criticism of complexity. Serious errors: declare benefit proved by deterministic tests, treat the graph as semantic authority, or require a full graph for every task.

## T02 — Freshness and activation

Frozen request: «Коли оновлюється RI, як агент починає ним користуватися і що відбувається, якщо дані застаріли?»

Expected evidence/outcome: CONTRIBUTING.md, the RI operational route and actual freshness workflow. Explain source-driven regeneration, verified checkout/blob identity, optional direct-owner reads and ordinary-source fallback. Serious errors: invent continuous updates, equate Pages activation with agent use, or accept unverifiable RI as current evidence.

## T03 — Existing code-style owner

Frozen request: «Ми вже пишемо багато коду для Quartz і пайплайнів. Чи треба додати правила стилю коду для агента, зокрема про коментарі?»

Expected evidence/outcome: existing CONTRIBUTING.md code guidance, scoped instructions and Quartz documentation before proposing a change. Refine a genuine gap in the existing owner; comments explain why/invariants. Serious errors: a parallel style owner without discovery, comments for every line, or root-instruction bloat duplicating local standards.

## T04 — Existing code rules and enforcement

Frozen request: «Які в нас правила стилю коду, чому вони такі та які з них реально перевіряються автоматично?»

Expected evidence/outcome: distinguish general/scoped rules, formatting, types, behavior tests and review conventions using actual source/configuration. Serious errors: invent a standard/check, omit scoped rules while claiming completeness, or claim formatting proves behavior.

## T05 — Existing PDF exporter

Frozen request: «Хочу отримати PDF статті `content/research/notes/thinking-systems-publication-draft.md`. Знайди наявний маршрут експорту та поясни порядок дій. Markdown має залишитися на місці; нічого не запускай і не змінюй».

Expected evidence/outcome: quartz/PDF-EXPORT.md, quartz/README.md, package scripts and relevant exporter/workflow configuration; identify the standalone article route rather than the separate working paper, actual setup, derived PDF/manifest destination, canonical Markdown preservation, provenance and visual verification. Serious errors: a competing converter without discovery, replacing canonical Markdown, confusing the two publication objects, requiring a deployed website, or claiming an export was performed. The source path and read-only boundary are accepted adaptations for this connector test.

## T06 — PDF without deployed Pages

Frozen request: «Чи працюватиме наявний Markdown-to-PDF exporter, якщо Quartz-сайт не опублікований? Поясни залежності й порядок дій».

Expected evidence/outcome: temporary local Quartz build and browser rendering, actual dependencies, independent hosting activation. Serious errors: Pages is required for PDF, temporary rendering equals publication, or altering canonical publication state to bypass an imagined dependency. This is a standalone edit of a context-dependent historical question; approve that edit explicitly.

## T07 — Graph versus SDD

Frozen request: «Це knowledge graph для LLM, шар spec-driven development чи щось інше? Поясни за фактичною реалізацією».

Expected evidence/outcome: deterministic repository projection and source routing; surrounding documents/contracts/validators own the specification and controls. Serious errors: graph as a new specification, complete SDD claim without evidence, or describing the actual baseline as embeddings/RAG.

## T08 — Publication routes

Frozen request: «Поясни наявні маршрути підготовки статті для PDF, LinkedIn та Medium, їхні залежності й перевірки. Чи потрібен ще один pipeline?»

Expected evidence/outcome: quartz/PDF-EXPORT.md, quartz/PLATFORM-RENDITIONS.md, quartz/README.md and related automation; distinct outputs with canonical source/provenance, only genuine missing work. Serious errors: competing publication flow without discovery or conflating platform outputs. This accepted source-tree-only replacement for a historical live-PR question does not require external PR-state verification.

## T09 — Next-section planning owner

Frozen request: «Хочемо продовжити довгу статтю “Uncertainty Architecture: Engineering Thinking Systems with Consequential Runtime Responsibilities”. Знайди її чинні blueprint і рукопис. Де має жити план наступної секції та які матеріали треба прочитати перед її написанням? Потрібна лише навігація й порядок роботи; план і текст секції зараз не пиши».

Expected evidence/outcome: scoped research instructions and the article's two-document process identify `content/research/notes/open-engineering-specification-article-blueprint.md` as the living editorial owner and `content/research/notes/open-engineering-specification-article-draft.md` as the long-form manuscript. Route future drafting through complete blueprint/manuscript reading, applicable research-state/provenance records and the cumulative iteration loop. The standalone `thinking-systems-publication-draft.md` is a different publication object. At the preparation commit, the long manuscript contains Abstract and numbered sections 1–4; this was checked in current headings, not assumed from history. This navigation task does not ask for full-manuscript semantic assessment. Serious errors: a third competing planning document, substituting the standalone article for the long manuscript, claiming full comparative review from headings, or promoting research into specification authority. This is the accepted bounded adaptation of the earlier next-section planning request.

## T10 — Implementation versus benefit evidence

Frozen request: «За файлами репозиторію визнач, які можливості RI реалізовані, що перевірено автоматичними тестами, а що ще потребує реальних агентних сесій. Який наступний мінімальний крок?»

Expected evidence/outcome: current RI architecture, tests, evaluation protocol and roadmap; distinguish technical properties from independent agent benefit and propose a bounded unresolved next step. Serious errors: CI proves usefulness, historical PR body as sole authority, or replaying completed work. This accepted adaptation replaces a historical merged-PR question.

## T11 — Dependency validation routing

Frozen request: «Планується оновлення залежностей Quartz і Playwright. Знайди чинні правила, файли залежностей та перевірки сумісності й впливу на GitHub Pages. Склади план перевірки за файлами репозиторію».

Expected evidence/outcome: package/lockfile, scoped rules, build/tests and Pages configuration; distinguish a validation plan from results. Serious errors: unperformed compatibility checks reported as successful or Dependabot metadata treated as runtime proof. This replaces historical live PR reviews; local build execution is outside this connector task.

## T12 — Extraction boundary

Frozen request: «Оціни за кодом і документацією, наскільки RI придатний до виділення в окремий open-source інструмент: що універсальне, що прив’язане до UA, чого бракує? Не роби висновків про попит або глобальну новизну без зовнішніх доказів».

Expected evidence/outcome: implementation/configuration boundaries, UA-specific metadata and contracts, packaging/docs/example gaps, and evidence-triggered proportionality. Serious errors: global novelty/demand from internal sources alone, extraction as mere renaming, or product expansion without a concrete consumer or measured problem. Market research remains separate.

## Selection disposition

The maintainer accepted all 12 proposed requests and their review expectations before outcomes. Their overlap and adapted provenance remain disclosed limitations. No rejected alternatives, keys or other tasks enter a tested session. Subsequent changes require a separately frozen follow-up; this corpus is not adapted to observed answers.
