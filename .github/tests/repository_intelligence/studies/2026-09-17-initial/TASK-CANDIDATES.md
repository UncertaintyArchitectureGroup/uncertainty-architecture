# Task candidates for maintainer selection

**Draft; not frozen and not independently selected. Do not give this file to a tested agent.**

These candidates condense real request topics from the maintainer's earlier conversations. The implementation-aware assistant prepared the wording and review expectations. Exact original references and any edits still require maintainer verification before conversion into v11 study records. Nothing here is a model response or scored evidence.

Requests remain in Ukrainian; expected outcomes and repository documentation are in English. Before freezing, include the full repository address in each selected task's context: https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture. Record that addition separately from the historical wording in the selection note.

## T01 — Architecture and proportionality

Proposed request: «Прочитай інструкції та структуру репозиторію. Поясни, як RI допомагає агенту орієнтуватися і чи виправдана складність цієї реалізації».

Expected evidence/outcome: RI architecture and implementation; distinguish the compact agent route, graph materialization and owning source files. Separate implemented properties from unproven operational benefit; allow evidence-based criticism of complexity. Serious errors: declare benefit proved by deterministic tests, treat the graph as semantic authority, or require a full graph for every task.

## T02 — Freshness and activation

Proposed request: «Коли оновлюється RI, як агент починає ним користуватися і що відбувається, якщо дані застаріли?»

Expected evidence/outcome: CONTRIBUTING.md, the RI operational route and actual freshness workflow. Explain source-driven regeneration, verified checkout/blob identity, optional direct-owner reads and ordinary-source fallback. Serious errors: invent continuous updates, equate Pages activation with agent use, or accept unverifiable RI as current evidence.

## T03 — Existing code-style owner

Proposed request: «Ми вже пишемо багато коду для Quartz і пайплайнів. Чи треба додати правила стилю коду для агента, зокрема про коментарі?»

Expected evidence/outcome: existing CONTRIBUTING.md code guidance, scoped instructions and Quartz documentation before proposing a change. Refine a genuine gap in the existing owner; comments explain why/invariants. Serious errors: a parallel style owner without discovery, comments for every line, or root-instruction bloat duplicating local standards.

## T04 — Existing code rules and enforcement

Proposed request: «Які в нас правила стилю коду, чому вони такі та які з них реально перевіряються автоматично?»

Expected evidence/outcome: distinguish general/scoped rules, formatting, types, behavior tests and review conventions using actual source/configuration. Serious errors: invent a standard/check, omit scoped rules while claiming completeness, or claim formatting proves behavior.

## T05 — Existing PDF exporter

Proposed request: «Хочу отримувати PDF із цього рукопису. Знайди, що для цього вже є в репозиторії, та поясни, як цим скористатися».

Pending: name the exact manuscript before selection. Expected evidence/outcome: quartz/PDF-EXPORT.md, quartz/README.md, scripts/tests/workflows; existing setup and export route, canonical Markdown, separate derived output, provenance and visual verification. Serious errors: a competing converter without discovery, replacing canonical Markdown, or requiring a deployed website.

## T06 — PDF without deployed Pages

Proposed request: «Чи працюватиме наявний Markdown-to-PDF exporter, якщо Quartz-сайт не опублікований? Поясни залежності й порядок дій».

Expected evidence/outcome: temporary local Quartz build and browser rendering, actual dependencies, independent hosting activation. Serious errors: Pages is required for PDF, temporary rendering equals publication, or altering canonical publication state to bypass an imagined dependency. This is a standalone edit of a context-dependent historical question; approve that edit explicitly.

## T07 — Graph versus SDD

Proposed request: «Це knowledge graph для LLM, шар spec-driven development чи щось інше? Поясни за фактичною реалізацією».

Expected evidence/outcome: deterministic repository projection and source routing; surrounding documents/contracts/validators own the specification and controls. Serious errors: graph as a new specification, complete SDD claim without evidence, or describing the actual baseline as embeddings/RAG.

## T08 — Publication routes

Proposed request: «Поясни наявні маршрути підготовки статті для PDF, LinkedIn та Medium, їхні залежності й перевірки. Чи потрібен ще один pipeline?»

Expected evidence/outcome: quartz/PDF-EXPORT.md, quartz/PLATFORM-RENDITIONS.md, quartz/README.md and related automation; distinct outputs with canonical source/provenance, only genuine missing work. Serious errors: competing publication flow without discovery or conflating platform outputs. Approve this source-tree-only replacement for a historical live-PR question; do not require external PR-state verification in the frozen task.

## T09 — Blueprint/manuscript alignment

Proposed request: «Порівняй зазначені blueprint і рукопис. Що треба змінити в плані наступних секцій з огляду на вже написаний матеріал?»

Pending: identify both files and confirm their actual current sections. Expected evidence/outcome: complete scoped research instructions, blueprint, manuscript and applicable research-state owners; concrete cumulative-argument gaps/repetition with the plan owned by the blueprint. Serious errors: planning from a fragment, a third competing planning document, or promoting a research hypothesis into a framework requirement. Do not silently reuse the historical “only Sections 1–4 exist” premise.

## T10 — Implementation versus benefit evidence

Proposed request: «За файлами репозиторію визнач, які можливості RI реалізовані, що перевірено автоматичними тестами, а що ще потребує реальних агентних сесій. Який наступний мінімальний крок?»

Expected evidence/outcome: current RI architecture, tests, evaluation protocol and roadmap; distinguish technical properties from independent agent benefit and propose a bounded unresolved next step. Serious errors: CI proves usefulness, historical PR body as sole authority, or replaying completed work. This proposed edit replaces a historical merged-PR question.

## T11 — Dependency validation routing

Proposed request: «Планується оновлення залежностей Quartz і Playwright. Знайди чинні правила, файли залежностей та перевірки сумісності й впливу на GitHub Pages. Склади план перевірки за файлами репозиторію».

Expected evidence/outcome: package/lockfile, scoped rules, build/tests and Pages configuration; distinguish a validation plan from results. Serious errors: unperformed compatibility checks reported as successful or Dependabot metadata treated as runtime proof. This replaces historical live PR reviews; local build execution is outside this connector task.

## T12 — Extraction boundary

Proposed request: «Оціни за кодом і документацією, наскільки RI придатний до виділення в окремий open-source інструмент: що універсальне, що прив’язане до UA, чого бракує? Не роби висновків про попит або глобальну новизну без зовнішніх доказів».

Expected evidence/outcome: implementation/configuration boundaries, UA-specific metadata and contracts, packaging/docs/example gaps, and evidence-triggered proportionality. Serious errors: global novelty/demand from internal sources alone, extraction as mere renaming, or product expansion without a concrete consumer or measured problem. Market research remains separate.

## Selection decisions still needed

T01/T07/T10 and T05/T06 overlap. The maintainer may replace candidates with more representative real tasks before freeze. For each selected task, verify its request provenance, finalize a standalone prompt and owning source paths, and agree concrete acceptable outcomes/serious errors against the actual study commit. Keep all rejected/replaced proposals out of model inputs; do not adapt the corpus to observed primary answers.
