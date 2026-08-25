#!/usr/bin/env python3
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(path, old, new):
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected exactly one match, got {count}: {old[:120]!r}")
    write(path, text.replace(old, new, 1))


def replace_all_in(path, old, new):
    text = read(path)
    if old not in text:
        return
    write(path, text.replace(old, new))

# -------------------------------------------------------------------------
# 1) Rename the conceptual register surface without renaming its stable path.
# -------------------------------------------------------------------------
for path in [
    "content/research/research-register.md",
    "content/research/AGENTS.md",
    "content/research/review-process.md",
    "content/research/index.md",
    "content/research/research-analysis-template.md",
    "content/research/framework-traceability.md",
    "content/research/notes/README.md",
    "ROADMAP.md",
]:
    replace_all_in(path, "Active Research Register", "Research State Register")

path = "content/research/research-register.md"
text = read(path)
text = text.replace("title: Active Research Register", "title: Research State Register", 1)
text = text.replace("  - active-research-register", "  - research-state-register", 1)
write(path, text)

path = ".github/scripts/validate_research_register.py"
text = read(path)
text = text.replace('"""Validate the canonical Active Research Register and provenance links."""', '"""Validate the canonical Research State Register and provenance links."""', 1)
text = text.replace('"Active Research Register is missing: {}"', '"Research State Register is missing: {}"', 1)
write(path, text)

# -------------------------------------------------------------------------
# 2) Support multiple transition-provenance records.
# -------------------------------------------------------------------------
path = "content/research/research-register.md"
text = read(path)
m = re.search(r"<!--\s*ua-research-register\s*(\{.*?\})\s*-->", text, re.S)
if not m:
    raise SystemExit("research-register: machine block missing")
data = json.loads(m.group(1))
for item in data["items"]:
    old = item.pop("transition_record", None)
    if item["id"] == "TS-SCOPE-001":
        item["transition_records"] = [
            "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
            "content/research/notes/thinking-systems-release-contract-scope-review.md",
        ]
    elif old:
        item["transition_records"] = [old]
block = "<!-- ua-research-register\n" + json.dumps(data, indent=2) + "\n-->"
text = text[:m.start()] + block + text[m.end():]
write(path, text)

path = ".github/scripts/validate_research_register.py"
text = read(path)
text = text.replace(
    'for field in ("provenance_record", "owning_record", "transition_record", "framework_destination"):',
    'for field in ("provenance_record", "owning_record", "framework_destination"):',
    1,
)
old = '''        transition = item.get("transition_record")
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

'''
new = '''        transitions = item.get("transition_records", [])
        if transitions is not None and not isinstance(transitions, list):
            findings.append(Finding("error", "{} transition_records must be a list when present".format(label)))
            transitions = []
        for transition in transitions:
            if not isinstance(transition, str) or not transition.strip():
                findings.append(Finding("error", "{} transition_records contains an empty or non-string path".format(label)))
                continue
            transition_path = repository_path(root, transition)
            if transition_path is None:
                findings.append(Finding("error", "{} transition record escapes repository: {!r}".format(label, transition)))
                continue
            if not transition_path.is_file():
                findings.append(Finding("error", "{} transition record does not exist: {!r}".format(label, transition)))
                continue
            if not transition.startswith("content/research/notes/"):
                findings.append(Finding("error", "{} transition record must use a bounded research note under content/research/notes/".format(label)))
                continue
            basename = Path(transition).name
            if basename and basename not in notes_index:
                findings.append(Finding("error", "{} transition record is not indexed in content/research/notes/README.md".format(label)))
            if isinstance(item_id, str):
                transition_text = transition_path.read_text(encoding="utf-8")
                if item_id not in transition_text:
                    findings.append(Finding("error", "{} transition record does not reference its stable research-item ID".format(label)))

'''
if old not in text:
    raise SystemExit("validator: singular transition block not found")
text = text.replace(old, new, 1)
write(path, text)

path = ".github/tests/research_register/test_research_register.py"
text = read(path)
text = text.replace('["transition_record"] = "content/research/notes/review.md"', '["transition_records"] = ["content/research/notes/review.md"]')
write(path, text)

for path in ["content/research/AGENTS.md", "content/research/review-process.md", "content/research/research-analysis-template.md"]:
    text = read(path)
    text = text.replace("the latest material transition source", "the material transition source(s)")
    text = text.replace("transition provenance separately", "one or more transition-provenance records separately")
    write(path, text)

# -------------------------------------------------------------------------
# 3) Scope the controlled-object/release-contract claim to the motivating class.
# -------------------------------------------------------------------------
manuscript = "content/research/notes/open-engineering-specification-article-draft.md"
publication = "content/research/notes/thinking-systems-publication-draft.md"
blueprint = "content/research/notes/open-engineering-specification-article-blueprint.md"

replace_once(
    manuscript,
    "Thinking Systems move consequential uncertainty inside the controlled object. Once that happens, model quality and observability are no longer sufficient descriptions of the engineering problem.",
    "For the motivating class developed in this paper—systems in which Model Judgment leaves part of a Consequential Runtime Responsibility unresolved until operation—consequential uncertainty moves inside the controlled object. For that class, model quality and observability are no longer sufficient descriptions of the engineering problem. Whether the broader current Thinking-System definition should also include fixed learned probabilistic functions whose deployed mapping is determined before release remains under validation (`TS-SCOPE-001`).",
)
replace_once(
    manuscript,
    "Thinking Systems add a distinct source of uncertainty. The uncertainty is not only in what should be built or in the environment in which software runs. It also appears in the runtime selection or construction of behavior inside the controlled object.",
    "The motivating class in this paper adds a distinct source of uncertainty. The uncertainty is not only in what should be built or in the environment in which software runs. It also appears where Model Judgment leaves part of a Consequential Runtime Responsibility unresolved until operation and the consequential behavior is selected or constructed inside the controlled object. The broader category boundary remains under `TS-SCOPE-001` rather than being assumed by this deduction.",
)
replace_once(
    manuscript,
    "Thinking Systems change this object by making one or more Consequential Runtime Responsibilities depend partly on probabilistic Model Judgment. The change can occur in the first model-enabled iteration; it does not require autonomous agents, dynamic orchestration, multiple models, memory, or a mature AI platform.",
    "The controlled-object argument developed here concerns the motivating class in which one or more Consequential Runtime Responsibilities depend on Model Judgment in a way that leaves part of the consequential mapping unresolved until operation. That change can occur in the first model-enabled iteration; it does not require autonomous agents, dynamic orchestration, multiple models, memory, or a mature AI platform. Whether the broader current definition should also include fixed learned probabilistic functions whose deployed mapping is determined before release remains an explicit boundary question under `TS-SCOPE-001`.",
)
replace_once(
    manuscript,
    "A Thinking-System release also places into operation a judgment process that will complete part of that mapping at runtime.",
    "A release in the motivating class examined here also places into operation a judgment process that will complete part of that mapping at runtime.",
)

replace_once(
    publication,
    "**Thinking Systems add a distinct source of uncertainty.** The uncertainty is not only in what should be built or in the environment in which software runs. It also appears in the runtime selection or construction of behavior inside the controlled object.",
    "**The motivating class examined in this article adds a distinct source of uncertainty.** The uncertainty is not only in what should be built or in the environment in which software runs. It also appears where Model Judgment leaves part of a Consequential Runtime Responsibility unresolved until operation and consequential behavior is selected or constructed inside the controlled object. Whether the broader current Thinking-System definition should also include fixed learned probabilistic functions whose deployed mapping is determined before release remains under validation rather than being assumed by this argument.",
)
replace_once(
    publication,
    "Thinking Systems change this object by making one or more Consequential Runtime Responsibilities depend partly on probabilistic Model Judgment. The change can occur in the first model-enabled iteration; it does not require autonomous agents, dynamic orchestration, multiple models, memory, or a mature AI platform.",
    "The controlled-object argument developed here concerns the motivating class in which one or more Consequential Runtime Responsibilities depend on Model Judgment in a way that leaves part of the consequential mapping unresolved until operation. The change can occur in the first model-enabled iteration; it does not require autonomous agents, dynamic orchestration, multiple models, memory, or a mature AI platform. Whether the broader current definition should also include fixed learned probabilistic functions whose deployed mapping is determined before release remains an explicit boundary question.",
)
replace_once(
    publication,
    "A Thinking-System release also places into operation a judgment process that will complete part of that mapping at runtime.",
    "A release in the motivating class examined here also places into operation a judgment process that will complete part of that mapping at runtime.",
)

replace_once(
    blueprint,
    "- state directly that the definition is not LLM-exclusive; treat concrete earlier systems as case-specific boundary tests, while explaining that general-purpose LLMs are the practical trigger and amplifier for the current engineering problem rather than proof of its historical origin;",
    "- state directly that the current wording is not LLM-exclusive, while keeping the resulting category breadth under validation against the release-contract thesis; treat concrete earlier systems as case-specific boundary tests, while explaining that general-purpose LLMs are the practical trigger and amplifier for the current engineering problem rather than proof of its historical origin;",
)
anchor = "→ the current Thinking-System definition is written without an LLM-only condition, but whether that breadth coheres with the release-contract thesis remains under validation; fixed learned probabilistic models and runtime judgment processes must be tested rather than collapsed by definition, while concrete earlier systems remain separate historical boundary cases\n"
if anchor not in read(blueprint):
    raise SystemExit("blueprint scope anchor missing")
text = read(blueprint).replace(
    anchor,
    anchor + "→ until `TS-SCOPE-001` is resolved, the controlled-object and release-contract deduction is scoped to the motivating class in which Model Judgment leaves part of a Consequential Runtime Responsibility unresolved until operation; the paper must not silently promote that property to every system admitted by the broader current wording\n",
    1,
)
write(blueprint, text)

# -------------------------------------------------------------------------
# 4) Put a primary-source link directly in the early STAMP positioning claim.
# -------------------------------------------------------------------------
stamp_old = "**STAMP already models hierarchical socio-technical control structures that can extend from software and operators through management and regulatory authority; STPA applies that systems-theoretic model to analyze unsafe control actions and causal scenarios.**"
stamp_new = "**[STAMP](https://mitpress.mit.edu/9780262533690/engineering-a-safer-world/) already models hierarchical socio-technical control structures that can extend from software and operators through management and regulatory authority; [STPA](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf) applies that systems-theoretic model to analyze unsafe control actions and causal scenarios.**"
replace_once(manuscript, stamp_old, stamp_new)
replace_once(publication, stamp_old, stamp_new)
text = read(blueprint)
text = text.replace(
    "**Early STAMP/STPA positioning rule.** Article §4 must include one bounded paragraph acknowledging that STAMP models hierarchical socio-technical control structures extending into management and regulatory authority and that STPA applies that model in systems-theoretic safety analysis.",
    "**Early STAMP/STPA positioning rule.** Article §4 must include one bounded paragraph, with direct primary-source links to Leveson's STAMP work and the STPA handbook, acknowledging that STAMP models hierarchical socio-technical control structures extending into management and regulatory authority and that STPA applies that model in systems-theoretic safety analysis.",
    1,
)
write(blueprint, text)

# -------------------------------------------------------------------------
# 5) Arkadiy Dobkin editorial clarification: no new research item.
#    Keep one substantive mention per surface and update existing provenance.
# -------------------------------------------------------------------------
# Publication: remove the body attribution paragraph and place the full credit in Acknowledgements.
body_credit = "The formulation **“Thinking Systems”** entered this research through my exchange with **Arkadiy Dobkin** following his LinkedIn post [_From Fall to Rise_](https://www.linkedin.com/posts/arkadiydobkin_from-fall-to-rise-activity-7477593508879724544-8-ZL). I am grateful to Arkadiy specifically for that formulation. I use the term here for a narrower engineering category; the definition and responsibility boundary below are developed in the Uncertainty Architecture research track. This article does **not** claim coinage of the phrase.\n\n"
text = read(publication)
if body_credit not in text:
    raise SystemExit("publication Arkadiy body credit missing")
text = text.replace(body_credit, "", 1)
old_ack = "The formulation provenance for **Thinking Systems** is recorded where the term is introduced above. That credit concerns the formulation and exchange, not authorship of the UA-specific definition or endorsement of this article."
new_ack = "The formulation **“Thinking Systems”** entered this research through my exchange with **Arkadiy Dobkin** following his LinkedIn post [_From Fall to Rise_](https://www.linkedin.com/posts/arkadiydobkin_from-fall-to-rise-activity-7477593508879724544-8-ZL). I am grateful to Arkadiy specifically for the formulation. Before publication, he reviewed the planned attribution and publication text and indicated that he was comfortable with both while reserving time for any later substantive critique. This records formulation and attribution provenance only; it does not attribute the UA-specific engineering definition or argument to him, and it does not imply endorsement."
if old_ack not in text:
    raise SystemExit("publication Arkadiy acknowledgment anchor missing")
text = text.replace(old_ack, new_ack, 1)
write(publication, text)

# Manuscript: one compact provenance paragraph immediately after the category definition.
anchor = "> A software system in which one or more **Consequential Runtime Responsibilities** depend partly on probabilistic Model Judgment rather than being fully specified through explicitly encoded logic in advance.\n\n"
credit = "The formulation **“Thinking Systems”** entered this research through my exchange with **Arkadiy Dobkin** following his public *From Fall to Rise* post. I am grateful to Arkadiy for the formulation. Before publication of the standalone adaptation, he reviewed the planned attribution and publication text and indicated that he was comfortable with both while reserving time for later substantive critique. This is formulation and attribution provenance, not authorship of the UA-specific definition, endorsement, or framework authority.\n\n"
text = read(manuscript)
if anchor not in text:
    raise SystemExit("manuscript definition anchor missing")
text = text.replace(anchor, anchor + credit, 1)
write(manuscript, text)

# Blueprint: record the editorial disposition, not a new hypothesis.
anchor = "This iteration uses **Explicitly Authored Software** as a paper-level comparative label under validation."
text = read(blueprint)
if anchor not in text:
    raise SystemExit("blueprint editorial anchor missing")
insert = "**Arkadiy Dobkin attribution disposition.** Dobkin reviewed the planned attribution and publication text before release, indicated that he was comfortable with both, and suggested that the formulation credit be stated cleanly in the Acknowledgements rather than delegated to a cross-reference. Treat this as an editorial/provenance clarification under the existing `TS-TERM-001`, not as a new research hypothesis or endorsement. The standalone adaptation should therefore carry one substantive Dobkin mention in Acknowledgements; the long-form manuscript may carry one compact provenance paragraph at the first formal definition until its final acknowledgements structure exists.\n\n"
text = text.replace(anchor, insert + anchor, 1)
write(blueprint, text)

# Existing provenance note: preserve the confirmation without a new ID.
path = "content/research/notes/thinking-systems-formulation-provenance-arkadiy-dobkin.md"
text = read(path)
anchor = "**Register item:** `TS-TERM-001`.\n"
if anchor not in text:
    raise SystemExit("Dobkin provenance register anchor missing")
addition = "\n## Pre-publication attribution confirmation\n\nBefore release of the standalone publication adaptation, Dobkin reviewed the planned attribution and publication text. He indicated that he was comfortable with both and did not want additional review time to delay publication, while reserving the possibility of later substantive critique. He also suggested a cleaner editorial placement for the credit in the article's Acknowledgements. This updates the existing formulation-provenance record only; it does not create a new research hypothesis, constitute substantive validation, or imply endorsement.\n"
text = text.replace(anchor, anchor + addition, 1)
write(path, text)

# -------------------------------------------------------------------------
# 6) Changelog language + research-process wording.
# -------------------------------------------------------------------------
path = "CHANGELOG.md"
text = read(path)
needle = "- Added durable provenance records for Maximiliano Armesto's pre-publication review and for the Arkadiy Dobkin exchange through which the formulation **Thinking Systems** entered the current research line, while separating attribution from authorship, endorsement, and framework authority."
if needle in text:
    repl = needle + " Dobkin's later pre-publication confirmation of the planned attribution/text and his acknowledgement-placement suggestion are preserved as an editorial update to the existing provenance record, not as a new research item or substantive validation."
    text = text.replace(needle, repl, 1)
write(path, text)

# Ensure process prose acknowledges multiple transition records.
for path in ["content/research/AGENTS.md", "content/research/review-process.md", "content/research/research-analysis-template.md"]:
    text = read(path)
    text = text.replace("origin/transition provenance", "origin and transition provenance")
    text = text.replace("origin versus transition provenance", "origin versus one-or-more transition provenance")
    write(path, text)

print("PR99 final semantic fixes applied")
