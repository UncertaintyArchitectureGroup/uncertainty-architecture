#!/usr/bin/env python3
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected one match, got {count}: {old[:120]!r}")
    write(path, text.replace(old, new, 1))


# Active Research Register -------------------------------------------------
path = "content/research/research-register.md"
text = read(path)
text = text.replace(
    "This register is the canonical cross-document inventory of **research concerns that require an identity and lifecycle outside any one paper, pull request, or conversation**.",
    "This register is the canonical cross-document inventory of **research concerns that require an identity and lifecycle outside any one paper, pull request, or conversation**. It preserves an item's origin separately from later evidence, dialogue, or review that changes its research state.",
    1,
)
new_table = '''## Current material items

| ID | Item | Class | Origin | Research state | Detailed owner / provenance | Next decision |
|---|---|---|---|---|---|---|
| `TS-TERM-001` | **Thinking Systems** formulation provenance | Term / provenance | External dialogue with Arkadiy Dobkin | Resolved | [`thinking-systems-formulation-provenance-arkadiy-dobkin.md`](notes/thinking-systems-formulation-provenance-arkadiy-dobkin.md); canonical meaning remains in the glossary | Preserve formulation provenance separately from authorship, endorsement, and definition authority |
| `TS-TERM-002` | **Explicitly Authored Software** | Terminology candidate | Maximiliano Armesto pre-publication review identified topology ambiguity in `Linear Software` | Under Validation | [`thinking-systems-pre-publication-review-maximiliano-armesto.md`](notes/thinking-systems-pre-publication-review-maximiliano-armesto.md); article blueprint owns the current paper-level test | Test whether the label is clearer and durable enough for separate framework terminology review; do not rename the glossary by implication |
| `TS-SCOPE-001` | Technology-neutral scope of the Thinking-System definition versus the release-contract thesis | Category-scope hypothesis | Current repository definition; external review exposed the breadth and a later consistency review exposed a release-contract tension | Under Validation | [`thinking-systems-release-contract-scope-review.md`](notes/thinking-systems-release-contract-scope-review.md) owns the current consistency issue; current glossary supplies the definition; blueprint owns the paper-level test | Test whether fixed learned probabilistic functions and runtime judgment processes belong to one category without weakening the release-contract distinction; narrow or generalize the definition/thesis if necessary |
| `TS-HIST-001` | Concrete pre-LLM Thinking-System boundary cases | Historical/category-boundary test | Maximiliano Armesto review raised earlier probabilistic systems as candidate cases | Under Validation | Same external-review record plus the scope-consistency note and article blueprint | Test concrete pre-LLM systems through causal and release-contract analysis before treating them as established examples or making prevalence claims |
| `TS-LOW-001` | Intentionally low-consequence Thinking-System boundary case | Proportionality/category-boundary test | Maximiliano Armesto review requested a deliberately low-consequence case | Under Validation | Same external-review record and article blueprint | Validate a low-consequence case independently of historical classification so the paper can show category membership ≠ severity ≠ control depth without assuming the example qualifies |
| `TS-PROP-001` | Category membership, consequence severity, and required control depth are distinct | Proportionality finding | Existing UA separation of consequentiality, severity, and control adequacy; sharpened by Maximiliano Armesto review | Resolved | Current glossary/doctrine support the distinction; review record preserves the later sharpening | Keep the resolved distinction visible in publication prose; validation of the illustrative low-consequence case remains under `TS-LOW-001` |
| `TS-LIFE-001` | Four-horizon lifecycle ownership and authorization refinement | Lifecycle / process hypothesis | Internal article synthesis against current Nested Control Lifecycle and project/delivery patterns | Under Validation | [`framework-traceability.md`](framework-traceability.md) conflict/evolution register; article blueprint owns the detailed hypothesis | Validate assessment eligibility, Project technical/design authority, Organization business/research authority, research-only versus production-capable Project Authorization, Business-Authorization coverage, and scoped-authorization semantics before any status-bearing lifecycle change |
| `TS-CARRIER-001` | Material-relationship carrier sufficiency and proportional application | Artifact / process hypothesis | Article §5 blueprint synthesis | Open | [`open-engineering-specification-article-blueprint.md`](notes/open-engineering-specification-article-blueprint.md) | Complete Article §5 mapping and test whether existing records/tools can carry each material relationship without UA-specific duplicate artifacts or semantic loss |
| `TS-COMP-001` | Four-horizon model relative to STAMP/STPA | Comparative hypothesis | Maximiliano Armesto review | Under Validation | Same review record; planned Article §6 landscape/substitution analysis | Perform bidirectional mapping and determine whether the four-horizon model adds useful lifecycle-decision specialization, merely renames existing semantics, or loses material relationships |
| `TS-SUB-001` | Semantic substitution and reverse-mapping test for existing methods/compositions | Comparative method hypothesis | Article §6 blueprint synthesis | Open | [`open-engineering-specification-article-blueprint.md`](notes/open-engineering-specification-article-blueprint.md) | Test whether equivalent-or-stronger semantics can substitute for UA relationships and whether reverse mapping exposes relationships the UA-derived map omitted or distorted |

## Machine-readable register'''
text, count = re.subn(r"## Current material items\n.*?\n## Machine-readable register", new_table, text, count=1, flags=re.S)
if count != 1:
    raise SystemExit("research-register: human table replacement failed")
match = re.search(r"<!--\s*ua-research-register\s*(\{.*?\})\s*-->", text, re.S)
if not match:
    raise SystemExit("research-register: machine block missing")
data = json.loads(match.group(1))
data["items"] = [
    {
        "id": "TS-TERM-001",
        "title": "Thinking Systems formulation provenance",
        "item_class": "term",
        "status": "resolved",
        "origin_kind": "external-dialogue",
        "provenance_record": "content/research/notes/thinking-systems-formulation-provenance-arkadiy-dobkin.md",
        "owning_record": "content/research/notes/thinking-systems-formulation-provenance-arkadiy-dobkin.md",
        "framework_destination": "00-doctrine/glossary.md",
        "next_step": "Preserve formulation provenance separately from authorship, endorsement, and definition authority."
    },
    {
        "id": "TS-TERM-002",
        "title": "Explicitly Authored Software",
        "item_class": "term",
        "status": "under-validation",
        "origin_kind": "external-review",
        "provenance_record": "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
        "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
        "next_step": "Test the paper-level label and submit any canonical rename to separate framework terminology review."
    },
    {
        "id": "TS-SCOPE-001",
        "title": "Technology-neutral scope of the Thinking-System definition versus the release-contract thesis",
        "item_class": "hypothesis",
        "status": "under-validation",
        "origin_kind": "repository-source",
        "provenance_record": "00-doctrine/glossary.md",
        "transition_record": "content/research/notes/thinking-systems-release-contract-scope-review.md",
        "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
        "next_step": "Test whether fixed learned probabilistic functions and runtime judgment processes belong to one category without weakening the release-contract distinction; narrow or generalize the definition/thesis if necessary."
    },
    {
        "id": "TS-HIST-001",
        "title": "Concrete pre-LLM Thinking-System boundary cases",
        "item_class": "example",
        "status": "under-validation",
        "origin_kind": "external-review",
        "provenance_record": "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
        "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
        "next_step": "Test concrete pre-LLM systems through causal and release-contract analysis before treating them as established examples or making prevalence claims."
    },
    {
        "id": "TS-LOW-001",
        "title": "Intentionally low-consequence Thinking-System boundary case",
        "item_class": "example",
        "status": "under-validation",
        "origin_kind": "external-review",
        "provenance_record": "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
        "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
        "next_step": "Validate a low-consequence case independently of historical classification so the paper can demonstrate proportionality without assuming the example qualifies."
    },
    {
        "id": "TS-PROP-001",
        "title": "Category membership, consequence severity, and required control depth are distinct",
        "item_class": "hypothesis",
        "status": "resolved",
        "origin_kind": "repository-source",
        "provenance_record": "00-doctrine/glossary.md",
        "transition_record": "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
        "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
        "next_step": "Keep the resolved distinction visible in publication prose; validation of the illustrative low-consequence case remains under TS-LOW-001."
    },
    {
        "id": "TS-LIFE-001",
        "title": "Four-horizon lifecycle ownership and authorization refinement",
        "item_class": "process",
        "status": "under-validation",
        "origin_kind": "internal-synthesis",
        "provenance_record": "content/research/framework-traceability.md",
        "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
        "next_step": "Validate the lifecycle ownership and authorization refinement before any status-bearing lifecycle change."
    },
    {
        "id": "TS-CARRIER-001",
        "title": "Material-relationship carrier sufficiency and proportional application",
        "item_class": "artifact",
        "status": "open",
        "origin_kind": "internal-synthesis",
        "provenance_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
        "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
        "next_step": "Complete Article 5 mapping and test the lightest credible carriers without semantic loss or duplicate UA-specific records."
    },
    {
        "id": "TS-COMP-001",
        "title": "Four-horizon model relative to STAMP/STPA",
        "item_class": "comparison",
        "status": "under-validation",
        "origin_kind": "external-review",
        "provenance_record": "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
        "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
        "next_step": "Perform the planned bidirectional STAMP/STPA mapping before making a contribution or substitution verdict."
    },
    {
        "id": "TS-SUB-001",
        "title": "Semantic substitution and reverse-mapping test for existing methods/compositions",
        "item_class": "comparison",
        "status": "open",
        "origin_kind": "internal-synthesis",
        "provenance_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
        "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
        "next_step": "Test equivalent-or-stronger semantic substitution and reverse mapping against the derived UA map."
    }
]
block = "<!-- ua-research-register\n" + json.dumps(data, indent=2) + "\n-->"
text = text[:match.start()] + block + text[match.end():]
write(path, text)

# Validator + tests --------------------------------------------------------
path = ".github/scripts/validate_research_register.py"
text = read(path)
text = text.replace(
    'for field in ("provenance_record", "owning_record"):',
    'for field in ("provenance_record", "owning_record", "transition_record", "framework_destination"):',
    1,
)
anchor = '''        provenance = item.get("provenance_record")
        if isinstance(origin, str) and origin in EXTERNAL_ORIGINS and isinstance(provenance, str):'''
insert = '''        transition = item.get("transition_record")
        if isinstance(transition, str) and transition.strip():
            transition_path = resolved_paths.get("transition_record")
            if not transition.startswith("content/research/notes/"):
                findings.append(Finding("error", "{} transition_record must use a bounded research note under content/research/notes/".format(label)))
            else:
                basename = Path(transition).name
                if basename and basename not in notes_index:
                    findings.append(Finding("error", "{} transition record is not indexed in content/research/notes/README.md".format(label)))
                if transition_path is not None and isinstance(item_id, str):
                    transition_text = transition_path.read_text(encoding="utf-8")
                    if item_id not in transition_text:
                        findings.append(Finding("error", "{} transition record does not reference its stable research-item ID".format(label)))

        provenance = item.get("provenance_record")
        if isinstance(origin, str) and origin in EXTERNAL_ORIGINS and isinstance(provenance, str):'''
if anchor not in text:
    raise SystemExit("validator transition anchor missing")
text = text.replace(anchor, insert, 1)
write(path, text)

path = ".github/tests/research_register/test_research_register.py"
text = read(path)
text = text.replace(
    '"owning_record": "00-doctrine/glossary.md",',
    '"owning_record": "content/research/notes/provenance.md",\n        "framework_destination": "00-doctrine/glossary.md",',
    1,
)
anchor = '    failures.append(run_case("external provenance must reference stable ID", missing_id_in_provenance, "does not reference its stable research-item ID"))\n\n    validator = load_validator()'
insert = '''    failures.append(run_case("external provenance must reference stable ID", missing_id_in_provenance, "does not reference its stable research-item ID"))

    def transition_missing_id(root: Path, items: List[Dict[str, object]]) -> None:
        write(root / "content/research/notes/review.md", "# Review without item identity\\n")
        write(root / "content/research/notes/README.md", "- [provenance.md](provenance.md)\\n- [review.md](review.md)\\n")
        items[0]["transition_record"] = "content/research/notes/review.md"
    failures.append(run_case("transition provenance must reference stable ID", transition_missing_id, "transition record does not reference its stable research-item ID"))

    validator = load_validator()'''
if anchor not in text:
    raise SystemExit("test transition anchor missing")
text = text.replace(anchor, insert, 1)
write(path, text)

# Maximiliano review record ------------------------------------------------
path = "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md"
text = read(path)
pattern = r"### 2\. The definition is not LLM-exclusive\n.*?\n### 3\. Category membership must be separated from control depth"
replacement = '''### 2. The current definition exposes a non-LLM scope question

The reviewer pointed out that the current wording is not tied to LLMs and therefore appears capable of including earlier probabilistic systems. During reconciliation, that observation exposed a second-order consistency question that remains unresolved: some fixed learned models can produce probabilistic scores or classifications while their deployed input-to-output mapping is fully determined before release, whereas the paper's release-contract thesis emphasizes consequential mapping that remains partly unresolved until runtime and is completed by Model Judgment during operation.

The review therefore establishes that the **current definition is written broadly**, not that historical technology-neutral applicability is already proven.

**Research effect:** preserve separate research items:

- `TS-SCOPE-001` — **Under Validation:** whether the current technology-neutral wording coheres with the release-contract thesis across fixed learned probabilistic functions and runtime judgment processes, or whether the category/thesis needs refinement;
- `TS-HIST-001` — **Under Validation:** which concrete pre-LLM systems, if any, satisfy the resulting category test strongly enough to be treated as Thinking Systems.

The second-order consistency issue is preserved separately in [`thinking-systems-release-contract-scope-review.md`](thinking-systems-release-contract-scope-review.md). No historical prevalence claim follows from the current definition alone.

### 3. Category membership must be separated from control depth'''
text, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
if count != 1:
    raise SystemExit("review note section 2 replacement failed")
text = text.replace(
    "The proportionality distinction is resolved at the conceptual level; whether a particular low-consequence example satisfies the category remains under `TS-CASE-001`.",
    "The proportionality distinction is resolved at the conceptual level; whether the deliberately low-consequence example actually satisfies the category remains independently under `TS-LOW-001`.",
)
text = text.replace("**Register item:** `TS-PROP-001`.", "**Register items:** `TS-PROP-001` and `TS-LOW-001`.", 1)
text = text.replace(
    "| Definition-level LLM scope | Resolved: the definition is technology-neutral and not LLM-exclusive | No doctrine change implied |",
    "| Definition-level technology scope | Reopened: current wording is broad, but coherence with the release-contract thesis remains under validation | No doctrine change in this PR |",
)
text = text.replace(
    "| Concrete pre-LLM / low-consequence classification | Under validation; treat examples case by case | No historical or prevalence claim implied |",
    "| Concrete pre-LLM classification | Under validation under `TS-HIST-001` | No historical or prevalence claim implied |\n| Low-consequence boundary example | Under validation under `TS-LOW-001` | Used only if the case independently satisfies the category test |",
)
text = text.replace(
    "2. Which pre-LLM and intentionally low-consequence systems satisfy the category test under concrete causal analysis, and which only contain probabilistic components without transferring a Consequential Runtime Responsibility?",
    "2. Does the category or release-contract thesis need an additional condition that distinguishes fixed learned probabilistic functions whose deployed mapping is determined before release from runtime judgment processes that leave part of the consequential mapping unresolved until operation?\n3. Which concrete pre-LLM systems, if any, satisfy the resulting category test?\n4. Which intentionally low-consequence case can demonstrate proportionality without smuggling category membership into the example?",
)
text = text.replace("3. What historical or prevalence claims", "5. What historical or prevalence claims")
text = text.replace("4. What does the four-horizon model", "6. What does the four-horizon model")
text = text.replace("5. What does the four-horizon map", "7. What does the four-horizon map")
text = text.replace(
    "This review reopens terminology and comparative-contribution questions, resolves the definition-level non-LLM-exclusivity point, and leaves concrete historical/low-consequence classification under validation.",
    "This review reopens terminology and comparative-contribution questions and exposes a still-open consistency question between the broad technology wording of the category and the release-contract thesis. Historical pre-LLM classification and the low-consequence proportionality example remain independently under validation.",
)
write(path, text)

# Internal scope note ------------------------------------------------------
path = "content/research/notes/thinking-systems-release-contract-scope-review.md"
text = read(path)
if "TS-HIST-001" not in text:
    text = text.replace(
        "Concrete pre-LLM cases are tracked separately from this definition-level question. Low-consequence examples are also separate because they test proportionality rather than historical scope.",
        "Concrete pre-LLM cases are tracked separately as `TS-HIST-001`. Low-consequence examples are tracked as `TS-LOW-001` because they test proportionality rather than historical scope.",
    )
write(path, text)

# Blueprint ---------------------------------------------------------------
path = "content/research/notes/open-engineering-specification-article-blueprint.md"
text = read(path)
text = text.replace(
    "1. defines Thinking Systems and states that the definition is not LLM-exclusive while treating concrete pre-LLM systems as boundary cases requiring case-specific classification;",
    "1. defines Thinking Systems, makes explicit that the current wording is not LLM-specific, and keeps open whether that breadth remains coherent with the release-contract thesis across fixed learned models and runtime judgment processes; concrete pre-LLM systems remain separate historical boundary tests;",
    1,
)
tracked = "**Tracked research items for this reconciliation:** `TS-TERM-002` (opposite-side terminology), `TS-SCOPE-001` (definition scope versus release-contract coherence), `TS-HIST-001` (pre-LLM historical cases), `TS-LOW-001` (low-consequence boundary case), `TS-PROP-001` (proportionality distinction), and `TS-COMP-001` (STAMP/STPA comparison). These IDs are the cross-document identities; this blueprint owns the detailed article-level reasoning for them.\n\n"
anchor = "This iteration uses **Explicitly Authored Software** as a paper-level comparative label under validation."
if tracked not in text:
    if anchor not in text:
        raise SystemExit("blueprint tracked-ID anchor missing")
    text = text.replace(anchor, tracked + anchor, 1)
text = text.replace(
    "→ the Thinking-System definition is not LLM-exclusive; concrete earlier systems remain case-specific classification tests, while general-purpose LLMs make model-mediated interpretation, synthesis, generation, routing, planning, and action selection much easier to embed across ordinary software",
    "→ the current Thinking-System definition is written without an LLM-only condition, but whether that breadth coheres with the release-contract thesis remains under validation; fixed learned probabilistic models and runtime judgment processes must be tested rather than collapsed by definition, while concrete earlier systems remain separate historical boundary cases",
    1,
)
text = text.replace(
    "Thinking Systems are software systems in which one or more **Consequential Runtime Responsibilities** depend partly on probabilistic Model Judgment rather than being fully specified through explicitly encoded logic in advance. The definition is technology-neutral and therefore not LLM-exclusive; concrete pre-LLM systems remain case-specific classification questions. General-purpose LLMs are the practical trigger for this paper because they make model-mediated judgment widely available across ordinary software.",
    "Thinking Systems are software systems in which one or more **Consequential Runtime Responsibilities** depend partly on probabilistic Model Judgment rather than being fully specified through explicitly encoded logic in advance. The current definition is written without an LLM-only condition, but that breadth remains under validation because some fixed learned probabilistic functions can have a deployed mapping fully determined before release while the paper's release-contract thesis depends on part of the consequential mapping remaining unresolved until runtime. Concrete pre-LLM systems are therefore boundary tests, not established category members. General-purpose LLMs remain the practical trigger for this paper because they make runtime model-mediated judgment widely available across ordinary software.",
    1,
)
text = text.replace(
    "State explicitly that this definition is not LLM-exclusive. Traditional probabilistic systems are candidate historical cases when a Consequential Runtime Responsibility materially depends on their output; classify concrete systems case by case rather than treating category applicability or historical prevalence as already established. General-purpose LLMs make this responsibility pattern more accessible and semantically broad. Also state that category membership, consequence severity, and implementation depth are separate decisions.",
    "State explicitly that the current definition is not written as LLM-exclusive, but treat that breadth as `TS-SCOPE-001` under validation rather than a resolved historical claim. Test whether fixed learned probabilistic functions whose deployed mapping is determined before release belong to the same engineering category as runtime judgment processes that leave part of the consequential situation-to-consequence mapping unresolved until operation. Track concrete pre-LLM systems separately under `TS-HIST-001`. Track the intentionally low-consequence publication example separately under `TS-LOW-001`; its job is to test proportionality, not historical scope. Keep `TS-PROP-001` as the resolved conceptual distinction that category membership, consequence severity, and implementation depth are separate decisions.",
    1,
)
write(path, text)

# Long-form manuscript ----------------------------------------------------
path = "content/research/notes/open-engineering-specification-article-draft.md"
text = read(path)
text = text.replace(
    "The definition is technology-neutral and therefore not LLM-exclusive; whether particular pre-LLM systems satisfy it remains a case-specific historical classification question.",
    "The current definition is written without an LLM-only condition, but whether that breadth remains coherent with the paper's release-contract thesis is still under validation—especially for fixed learned models whose deployed mapping may be fully determined before release. Particular pre-LLM systems therefore remain boundary tests rather than established members.",
    1,
)
old_caption = "**Figure 1 — Engineering expands its feedback model as consequential uncertainty moves closer to runtime and eventually enters the controlled object.** The final transition identifies the problem of engineering and operating systems in which consequential behavior is partly produced through probabilistic Model Judgment inside the controlled object. The category definition is not LLM-exclusive; this figure does not establish which earlier systems satisfy the category or how prevalent they were. LLMs and other general-purpose models make the pattern substantially easier to instantiate across ordinary software."
new_caption = "**Figure 1 — Engineering expands its feedback model as consequential uncertainty moves closer to runtime and eventually enters the controlled object.** The final transition identifies the problem of engineering and operating systems in which consequential behavior is partly produced through probabilistic Model Judgment inside the controlled object. The current definition is written without an LLM-only condition, but this figure does not establish that fixed learned probabilistic systems and runtime judgment processes share the same release-contract property, which remains under validation. LLMs and other general-purpose models make runtime model-mediated judgment substantially easier to instantiate across ordinary software."
if old_caption not in text:
    raise SystemExit("manuscript Figure 1 caption anchor missing")
text = text.replace(old_caption, new_caption, 1)
pattern = r"The Thinking-System definition is technology-neutral rather than LLM-specific\..*?LLMs are the practical trigger for this paper because they make model-mediated interpretation, synthesis, generation, routing, planning, and action selection general-purpose and easy to embed across ordinary software\."
replacement = "The current Thinking-System definition is written in technology-neutral terms, but that breadth is now an explicit research question rather than a resolved historical claim. A traditional credit-scoring model may use a learned probabilistic function whose deployed input-to-output mapping is fixed before release; such a system can look like Model Judgment under the current wording without necessarily sharing the release-contract property developed in Section 2, where part of the consequential situation-to-consequence mapping remains unresolved until runtime. Credit scoring and other pre-LLM models are therefore historical boundary tests, not established examples. Separately, a document summarizer or code-completion suggestion tests a different axis: Output Mediation may make a low-consequence responsibility materially consequential, but that case must independently satisfy the category test. LLMs remain the practical trigger for this paper because they make runtime model-mediated interpretation, synthesis, generation, routing, planning, and action selection general-purpose and easy to embed across ordinary software."
text, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
if count != 1:
    raise SystemExit("manuscript scope paragraph replacement failed")
text = text.replace(
    "Category membership does not determine consequence severity or control depth. An internal summarizer used for a reversible, inspectable prioritization decision may require only a small explicit control surface;",
    "Category membership does not determine consequence severity or control depth. If an internal summarizer used for a reversible, inspectable prioritization decision independently satisfies the category test, it may require only a small explicit control surface;",
    1,
)
write(path, text)

# Publication adaptation --------------------------------------------------
path = "content/research/notes/thinking-systems-publication-draft.md"
text = read(path)
old_caption = "**Figure 1 — Engineering expands its feedback model as consequential uncertainty moves closer to runtime and eventually enters the controlled object.** The category definition is not LLM-exclusive; this transition does not establish which earlier systems satisfy the category or how prevalent they were. LLMs and other general-purpose models make the pattern substantially easier to instantiate across ordinary software. Waterfall, Agile, and DevOps are shown as familiar examples of broader engineering responses. The progression is conceptual, not replacement history."
new_caption = "**Figure 1 — Engineering expands its feedback model as consequential uncertainty moves closer to runtime and eventually enters the controlled object.** The current definition is written without an LLM-only condition, but whether fixed learned probabilistic systems and runtime judgment processes belong to one engineering category remains under validation. This transition therefore does not establish which earlier systems satisfy the category or how prevalent they were. LLMs and other general-purpose models make runtime model-mediated judgment substantially easier to instantiate across ordinary software. Waterfall, Agile, and DevOps are shown as familiar examples of broader engineering responses. The progression is conceptual, not replacement history."
if old_caption not in text:
    raise SystemExit("publication Figure 1 caption anchor missing")
text = text.replace(old_caption, new_caption, 1)
pattern = r"The Thinking-System definition is technology-neutral rather than LLM-specific\..*?LLMs are the practical trigger for this article because they make model-mediated interpretation, synthesis, generation, routing, planning, and action selection general-purpose and easy to embed across ordinary software\."
replacement = "The current Thinking-System definition is written in technology-neutral terms, but this breadth remains under validation. A fixed learned model such as traditional credit scoring may produce probabilistic scores while its deployed input-to-output mapping is fully determined before release; that does not automatically establish the release-contract shift developed below, where part of the consequential mapping remains unresolved until runtime. Such pre-LLM systems are therefore boundary tests rather than established examples. A document summarizer or code-completion suggestion tests a different question: whether Output Mediation can make a low-consequence responsibility materially consequential. LLMs remain the practical trigger for this article because they make runtime model-mediated interpretation, synthesis, generation, routing, planning, and action selection general-purpose and easy to embed across ordinary software."
text, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
if count != 1:
    raise SystemExit("publication scope paragraph replacement failed")
text = text.replace(
    "Category membership does not determine consequence severity or control depth. An internal summarizer used for a reversible, inspectable prioritization decision may need only a small explicit control surface;",
    "Category membership does not determine consequence severity or control depth. If an internal summarizer used for a reversible, inspectable prioritization decision independently satisfies the category test, it may need only a small explicit control surface;",
    1,
)
write(path, text)

# Framework traceability --------------------------------------------------
path = "content/research/framework-traceability.md"
text = read(path)
text, count = re.subn(
    r"^\| Technology scope of the Thinking-System definition \|.*$",
    "| Technology scope of the Thinking-System definition | Current wording can be read as applying to any probabilistic Model Judgment, including fixed learned functions | Whether fixed learned probabilistic functions and runtime judgment processes share the same changed release-contract property remains under validation | Needs Resolution | Track `TS-SCOPE-001`; do not promote technology-neutral historical applicability as resolved until the definition and release-contract thesis are shown to cohere or the category/thesis is narrowed. |",
    text,
    count=1,
    flags=re.M,
)
if count != 1:
    raise SystemExit("traceability technology-scope row missing")
text, count = re.subn(
    r"^\| Concrete pre-LLM and low-consequence boundary cases \|.*$",
    "| Concrete pre-LLM boundary cases | Earlier probabilistic systems may appear to satisfy the current wording | Specific historical systems qualify only if causal and release-contract analysis shows the relevant Consequential Runtime Responsibility has the same material judgment-dependent structure | Needs Resolution | Test concrete historical cases separately under `TS-HIST-001`; do not infer historical prevalence from probabilistic component presence. |\n| Low-consequence boundary case | Proportionality needs an example that does not imply maximal control | A low-consequence example must independently satisfy the category test before it can demonstrate lighter proportionate control | Needs Resolution | Validate the illustrative case under `TS-LOW-001`; keep the conceptual proportionality distinction itself separate and Active. |",
    text,
    count=1,
    flags=re.M,
)
if count != 1:
    raise SystemExit("traceability combined-case row missing")
text = text.replace(
    "- pre-LLM Thinking-System boundary cases, including systems where probabilistic output is advisory versus materially determinative of a Consequential Runtime Responsibility;",
    "- technology-neutral category scope versus the release-contract distinction, including fixed learned probabilistic functions whose deployed mapping may be fully determined before release;\n- concrete pre-LLM boundary cases under `TS-HIST-001`;\n- a deliberately low-consequence boundary case under `TS-LOW-001` for proportionality testing;",
    1,
)
write(path, text)

# Research process documents ---------------------------------------------
for path in ["content/research/review-process.md", "content/research/AGENTS.md"]:
    text = read(path)
    addition = "\n\n**Origin versus transition provenance.** Record where a research item first entered the work separately from later evidence, dialogue, or review that reopens, narrows, sharpens, or resolves it. A later reviewer who materially changes an existing hypothesis is a transition source, not retroactively the origin of that hypothesis. Preserve both when the distinction matters."
    if addition.strip() not in text:
        needle = "Private correspondence does not need to be reproduced verbatim." if path.endswith("review-process.md") else "Do not publish private correspondence verbatim merely to prove provenance."
        if needle not in text:
            raise SystemExit(f"{path}: provenance insertion anchor missing")
        text = text.replace(needle, needle + addition, 1)
    write(path, text)

path = "content/research/research-analysis-template.md"
text = read(path)
text = text.replace(
    "- the source or reviewed artifact;\n- whether provenance is public, maintainer-attested, or otherwise bounded;",
    "- the source or reviewed artifact;\n- the item's original source, when different from the source that later changed its state;\n- the latest material transition source (review, evidence, dialogue, incident, or worked application), when applicable;\n- whether provenance is public, maintainer-attested, or otherwise bounded;",
    1,
)
if "Do not rewrite an item's origin" not in text:
    text = text.replace(
        "- whether a bounded provenance/review note is required under `content/research/notes/`.\n",
        "- whether a bounded provenance/review note is required under `content/research/notes/`.\n\nDo not rewrite an item's origin when a later reviewer merely reopens, sharpens, narrows, or resolves it. Preserve origin provenance and transition provenance separately when that distinction matters.\n",
        1,
    )
write(path, text)

# Notes index -------------------------------------------------------------
path = "content/research/notes/README.md"
text = read(path)
entry = "- [`thinking-systems-release-contract-scope-review.md`](thinking-systems-release-contract-scope-review.md) — internal consistency review that reopens whether the current technology-neutral Thinking-System wording coheres with the paper's release-contract thesis across fixed learned probabilistic functions and runtime judgment processes; it tracks `TS-SCOPE-001` without treating the issue as external evidence.\n"
anchor = "- [`thinking-systems-pre-publication-review-maximiliano-armesto.md`](thinking-systems-pre-publication-review-maximiliano-armesto.md)"
if entry not in text:
    pos = text.find(anchor)
    if pos < 0:
        raise SystemExit("notes index insertion anchor missing")
    line_end = text.find("\n", pos)
    text = text[: line_end + 1] + entry + text[line_end + 1 :]
write(path, text)

# Changelog ---------------------------------------------------------------
path = "CHANGELOG.md"
text = read(path)
old = "stated that the Thinking-System definition is not LLM-exclusive while concrete pre-LLM systems remain case-specific classification tests, and that general-purpose LLMs make model-mediated judgment substantially easier to embed across ordinary software; separated category membership from consequence severity and proportionate control depth through an intentionally low-consequence case;"
new = "made explicit that the current Thinking-System wording is not LLM-specific while reopening whether fixed learned probabilistic functions and runtime judgment processes share the same release-contract property; split concrete pre-LLM historical cases from the independently validated low-consequence proportionality case; and kept the conceptual distinction between category membership, consequence severity, and proportionate control depth;"
if old not in text:
    raise SystemExit("changelog reconciliation wording missing")
text = text.replace(old, new, 1)
write(path, text)

# Stale merged-case ID must be gone from canonical research state.
for path in [
    "content/research/research-register.md",
    "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
    "content/research/framework-traceability.md",
    "content/research/notes/open-engineering-specification-article-blueprint.md",
]:
    if "TS-CASE-001" in read(path):
        raise SystemExit(f"{path}: stale TS-CASE-001 remains")

# Restore Metadata integrity workflow to normal read-only operation and
# remove one-shot transport files before the commit.
workflow = " .github/workflows/metadata-integrity.yml".strip()
text = read(workflow)
text = text.replace("permissions:\n  contents: write", "permissions:\n  contents: read", 1)
text, count = re.subn(r"\n  apply-pr99-fixes:\n.*\Z", "\n", text, count=1, flags=re.S)
if count != 1:
    raise SystemExit("metadata workflow one-shot job removal failed")
write(workflow, text)

for temporary in [
    ROOT / ".github/workflows/apply-pr99-semantic-fixes.yml",
    ROOT / ".github/scripts/apply_pr99_semantic_fixes.py",
]:
    if temporary.exists():
        temporary.unlink()
