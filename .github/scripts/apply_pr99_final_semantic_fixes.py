#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_if_present(path, old, new):
    text = read(path)
    count = text.count(old)
    if count > 1:
        raise SystemExit(f"{path}: ambiguous replacement ({count} matches): {old[:100]!r}")
    if count == 1:
        write(path, text.replace(old, new, 1))

manuscript = "content/research/notes/open-engineering-specification-article-draft.md"
publication = "content/research/notes/thinking-systems-publication-draft.md"
blueprint = "content/research/notes/open-engineering-specification-article-blueprint.md"

replace_if_present(
    manuscript,
    "Thinking Systems change this object by making one or more **Consequential Runtime Responsibilities** depend partly on probabilistic Model Judgment. The change can occur in the first model-enabled iteration; it does not require autonomous agents, dynamic orchestration, multiple models, memory, or a mature AI platform.\n\n",
    "",
)

for path in (manuscript, publication):
    replace_if_present(path, 'subgraph B["Thinking System — changed responsibility structure"]', 'subgraph B["Motivating class — changed responsibility structure"]')

replace_if_present(
    manuscript,
    "**Figure 3 — The controlled-object shift.** On the left, Consequential Runtime Responsibilities are fulfilled through explicitly authored logic. On the right, explicitly authored responsibilities remain part of the system while one or more Consequential Runtime Responsibilities depend partly on probabilistic Model Judgment, so part of the consequential mapping is completed at runtime.",
    "**Figure 3 — The controlled-object shift for the motivating class.** On the left, Consequential Runtime Responsibilities are fulfilled through explicitly authored logic. On the right, the motivating runtime-judgment class retains explicitly authored responsibilities while Model Judgment leaves part of a Consequential Runtime Responsibility unresolved until operation, so part of the consequential mapping is completed at runtime. The figure does not resolve whether fixed learned probabilistic functions with a release-time-determined mapping belong to the broader Thinking-System category.",
)
replace_if_present(
    publication,
    "**Figure 3 — The controlled-object shift.** Explicitly authored responsibilities remain part of the system while one or more Consequential Runtime Responsibilities depend partly on probabilistic Model Judgment, so part of the consequential mapping is completed at runtime.",
    "**Figure 3 — The controlled-object shift for the motivating class.** Explicitly authored responsibilities remain part of the system while Model Judgment leaves part of a Consequential Runtime Responsibility unresolved until operation, so part of the consequential mapping is completed at runtime. The figure does not resolve whether fixed learned probabilistic functions with a release-time-determined mapping belong to the broader Thinking-System category.",
)

replace_if_present(
    manuscript,
    "| **Thinking System (this paper)** | A **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment | Directly identifies the controlled-object change examined in the rest of the paper |",
    "| **Thinking System (this paper)** | A **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment | Identifies the responsibility boundary under test; the controlled-object/release-contract shift is developed for the motivating runtime-judgment class while broader scope remains under validation |",
)
replace_if_present(
    publication,
    "| **Thinking System (this article)**                                                                                           | A Consequential Runtime Responsibility depends partly on probabilistic Model Judgment            | Directly identifies the controlled-object change examined in the rest of the article                                                |",
    "| **Thinking System (this article)**                                                                                           | A Consequential Runtime Responsibility depends partly on probabilistic Model Judgment            | Identifies the responsibility boundary under test; the controlled-object/release-contract shift is developed for the motivating runtime-judgment class while broader scope remains under validation |",
)

replace_if_present(
    blueprint,
    "3. explains why making a Consequential Runtime Responsibility depend partly on probabilistic Model Judgment changes the controlled object;",
    "3. develops the controlled-object and release-contract shift for the motivating class in which Model Judgment leaves part of a Consequential Runtime Responsibility unresolved until operation, while keeping the broader category scope under `TS-SCOPE-001`;",
)
replace_if_present(
    blueprint,
    "→ Thinking-System Delivery also places a runtime judgment process into operation that completes part of the consequential mapping;",
    "→ for the motivating class covered by the release-contract deduction, Delivery also places a runtime judgment process into operation that completes part of the consequential mapping;",
)

print("Remaining PR99 semantic cleanup applied")
