#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def replace_once(path, old, new):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected exactly one match, got {count}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")

# Standalone adaptation: preserve the original substantive formulation credit,
# but place it in Acknowledgments rather than in the argument body.
replace_once(
    "content/research/notes/thinking-systems-publication-draft.md",
    "The formulation **“Thinking Systems”** entered this research through my exchange with **Arkadiy Dobkin** following his LinkedIn post [_From Fall to Rise_](https://www.linkedin.com/posts/arkadiydobkin_from-fall-to-rise-activity-7477593508879724544-8-ZL). I am grateful to Arkadiy specifically for the formulation. Before publication, he reviewed the planned attribution and publication text and indicated that he was comfortable with both while reserving time for any later substantive critique. This records formulation and attribution provenance only; it does not attribute the UA-specific engineering definition or argument to him, and it does not imply endorsement.",
    "The formulation **“Thinking Systems”** entered this research through my exchange with **Arkadiy Dobkin** following his LinkedIn post [_From Fall to Rise_](https://www.linkedin.com/posts/arkadiydobkin_from-fall-to-rise-activity-7477593508879724544-8-ZL). I am grateful to Arkadiy specifically for that formulation. I use the term here for a narrower engineering category; the definition and responsibility boundary above are developed in the Uncertainty Architecture research track. This article does **not** claim coinage of the phrase.",
)

# Long-form manuscript: keep formulation provenance, remove publication-clearance
# details from the research argument itself.
replace_once(
    "content/research/notes/open-engineering-specification-article-draft.md",
    "The formulation **“Thinking Systems”** entered this research through my exchange with **Arkadiy Dobkin** following his public *From Fall to Rise* post. I am grateful to Arkadiy for the formulation. Before publication of the standalone adaptation, he reviewed the planned attribution and publication text and indicated that he was comfortable with both while reserving time for later substantive critique. This is formulation and attribution provenance, not authorship of the UA-specific definition, endorsement, or framework authority.",
    "The formulation **“Thinking Systems”** entered this research through my exchange with **Arkadiy Dobkin** following his public *From Fall to Rise* post. I am grateful to Arkadiy for the formulation. This is formulation provenance, not authorship of the UA-specific definition, endorsement, or framework authority.",
)

# Blueprint: own placement/synchronization only. The fact of Dobkin's
# pre-publication confirmation remains in the dedicated provenance note.
replace_once(
    "content/research/notes/open-engineering-specification-article-blueprint.md",
    "**Arkadiy Dobkin attribution disposition.** Dobkin reviewed the planned attribution and publication text before release, indicated that he was comfortable with both, and suggested that the formulation credit be stated cleanly in the Acknowledgements rather than delegated to a cross-reference. Treat this as an editorial/provenance clarification under the existing `TS-TERM-001`, not as a new research hypothesis or endorsement. The standalone adaptation should therefore carry one substantive Dobkin mention in Acknowledgements; the long-form manuscript may carry one compact provenance paragraph at the first formal definition until its final acknowledgements structure exists.",
    "**Arkadiy Dobkin attribution placement.** Preserve the existing substantive formulation credit under `TS-TERM-001` without expanding it into a review or endorsement claim. The standalone adaptation should carry that credit once, in Acknowledgements rather than in the argument body; the long-form manuscript may retain one compact formulation-provenance paragraph at the first formal definition until its final acknowledgements structure exists. Any pre-publication attribution-confirmation detail belongs in the dedicated provenance record rather than the paper prose.",
)
