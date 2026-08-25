from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def replace_once(rel, old, new):
    p = ROOT / rel
    text = p.read_text(encoding='utf-8')
    n = text.count(old)
    if n != 1:
        raise SystemExit(f'{rel}: expected exactly one match, got {n}')
    p.write_text(text.replace(old, new, 1), encoding='utf-8')

# Blueprint: Figure 2 is classification-only while TS-SCOPE-001 remains open.
replace_once(
 'content/research/notes/open-engineering-specification-article-blueprint.md',
 '→ until `TS-SCOPE-001` is resolved, the controlled-object and release-contract deduction is scoped to the motivating class in which Model Judgment leaves part of a Consequential Runtime Responsibility unresolved until operation; the paper must not silently promote that property to every system admitted by the broader current wording\n→ category membership does not determine consequence severity or maximal control implementation;',
 '→ until `TS-SCOPE-001` is resolved, the controlled-object and release-contract deduction is scoped to the motivating class in which Model Judgment leaves part of a Consequential Runtime Responsibility unresolved until operation; the paper must not silently promote that property to every system admitted by the broader current wording\n→ Figure 2 is classification-only: `Yes → Thinking System` means only that a Consequential Runtime Responsibility depends partly on Model Judgment; the figure and adjacent Section 1 prose must not infer the runtime-unresolved release-contract property for every admitted case while `TS-SCOPE-001` remains open\n→ category membership does not determine consequence severity or maximal control implementation;'
)

# Manuscript: classification wording must not silently resolve TS-SCOPE-001.
replace_once(
 'content/research/notes/open-engineering-specification-article-draft.md',
 'If yes, the software contains the changed object described here even when orchestration is fixed. Deterministic code before, between, or after that judgment does not make the delegated judgment deterministic.',
 'If yes, the software satisfies the current Thinking-System classification test even when orchestration is fixed. Whether every system admitted by that wording also exhibits the runtime-unresolved responsibility structure developed in Section 2 remains under `TS-SCOPE-001`. Deterministic code before, between, or after a runtime judgment process does not make that delegated judgment deterministic.'
)
replace_once(
 'content/research/notes/open-engineering-specification-article-draft.md',
 'T["Yes → Thinking System<br/> part of consequential behavior<br/> is formed through runtime Model Judgment"]',
 'T["Yes → Thinking System<br/> Consequential Runtime Responsibility<br/> depends partly on Model Judgment"]'
)
replace_once(
 'content/research/notes/open-engineering-specification-article-draft.md',
 'Thinking-System engineering still requires product discovery, deterministic software engineering, testing, security, deployment discipline, observability, and incident response. The new category does not invalidate those practices. It changes the object they are controlling.',
 'Thinking-System engineering still requires product discovery, deterministic software engineering, testing, security, deployment discipline, observability, and incident response. The current category test does not invalidate those practices. For the motivating runtime-judgment class developed in Section 2, it identifies the responsibility structure that changes the object they are controlling; whether that deduction extends to every case admitted by the broader wording remains under `TS-SCOPE-001`.'
)

# Publication adaptation: same classification-only contract.
replace_once(
 'content/research/notes/thinking-systems-publication-draft.md',
 'If yes, the software contains the changed object described here even when orchestration is fixed. Orchestration topology, autonomy, and delegated authority affect architecture and control demand, but they do not decide the category.',
 'If yes, the software satisfies the current Thinking-System classification test even when orchestration is fixed. Whether every system admitted by that wording also exhibits the runtime-unresolved responsibility structure developed in Section 2 remains under `TS-SCOPE-001`. Orchestration topology, autonomy, and delegated authority affect architecture and control demand, but they do not decide the category.'
)
replace_once(
 'content/research/notes/thinking-systems-publication-draft.md',
 'T["Yes → Thinking System<br/>part of consequential behavior<br/>is formed through runtime Model Judgment"]',
 'T["Yes → Thinking System<br/>Consequential Runtime Responsibility<br/>depends partly on Model Judgment"]'
)
