# Editable PowerPoint export

The PMDay deck is an informative presentation rendition, not a new UA doctrine or research edition. Its [central Markdown description](../assets/presentations/pmday-2026/README.md) owns the approved 14-slide order, style, screen copy, speaker notes, evidence limits and source URLs. Each `pptx-slide` JSON block is the render input for the corresponding slide. Update the prose and render block together. The [evidence base](../assets/presentations/pmday-2026/EVIDENCE.md) links local source notes, attributed Creative Commons originals and their retrieval checksums.

## Consolidation of PRs #113 and #129

PR #113 is the continuing presentation workstream. The September 1 head (`7c91ab9`) contained only a plan; its claimed local 22-slide prototype and PptxGenJS implementation were not in that PR. The executable PMDay slice from PR #129 is carried into #113 together with the layout corrections. PR #129 is superseded after that transfer, without merging either PR into `main`.

This document owns the implemented contract. `PRESENTATION-PIPELINE.md` is a migration pointer, not a second implementation specification. The PMDay Markdown owns this deck's screen copy, notes and design.

| Original #113 requirement | Current disposition |
|---|---|
| Markdown content separated from layout code | Implemented for the 14-slide PMDay deck |
| Dark background and native editable slide objects | Implemented; one requested foreground cover illustration, no background pictures or rasterized slides |
| Reuse publication path safety, stage and preserve last valid output | Implemented for PPTX/manifest promotion; previews use new isolated directories |
| Notes, checksums, slide count and package verification | Implemented |
| Independent PPTX → PDF/PNG visual evidence | Implemented via `pptx:preview`; manual visual review remains necessary |
| Generic multi-deck source schema and reusable renderer | Pending; current adapter is PMDay-specific |
| Generation on a standard GitHub runner, manual dispatch and path-scoped export | Pending; CI validates the committed snapshot only |
| Preserve and modernize the original 22-slide Designing Non-Deterministic Systems deck | Pending; its historical PPTX is not in this branch and is not replaced by PMDay |
| PptxGenJS dependency/OOXML normalization decisions | Not adopted by this backend; re-evaluate if a portable backend is selected |
| Native Microsoft PowerPoint acceptance | Pending |

The original plan and its decisions remain retrievable in [the recorded #113 source revision](https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/7c91ab9176af74106513e2c979fd311758ad9d1e/quartz/PRESENTATION-PIPELINE.md). Pending items are not claimed complete by consolidation. No obsolete dependency-security exception is carried into the current backend.

## Why this is separate from PDF

Quartz/Chromium PDF printing cannot preserve native PowerPoint objects. The PPTX path therefore sits alongside the existing publication scripts, without changing Quartz core or the PDF contract. It reuses the existing path-safety and rollback-capable pair installer. There is no slide-image conversion step.

The generated review snapshot and manifest are committed under `assets/presentations/pmday-2026/` at the maintainer's explicit request. This is a bounded exception for a deliverable, not a claim that the talk has already been presented or externally published. Staging output and visual QA stay under ignored `dist/pptx/`.

## Editing and verification

1. Edit the central Markdown, keeping the approved titles/order and updating the relevant render block.
2. Generate a new candidate in the authoring environment.
3. Render all 14 slides and inspect each at full size. Fix crowding, wrong connectors or unreadable text before acceptance.
4. Promote the checked candidate and matching manifest together.
5. Commit source, generator changes if any, PPTX and manifest in the same PR.

```bash
npm ci --ignore-scripts
npm run pptx:verify
npm run test:publication
```

Verification is portable: Node.js 22 and Python 3 standard library are sufficient. Existing Build Integrity already runs the publication-test glob, including PPTX source/mutation tests and the committed snapshot check. No new workflow or runner permission is required.

The central Markdown owns the maintainer-requested **slides 1–11 freeze**, extended from 1–8 by the explicit September 22 follow-up. The existing record retains the earlier authorization history. Exact source-section hashes and normalized package-part hashes protect slides, notes and their entire dependency closure, including shared presentation settings, layouts, masters, themes, cover, the slide 10 chart and its embedded workbook, and the slide 11 table. Generated relationship/creation IDs are normalized by meaning. Workbook ZIP compression, entry order and timestamps are ignored, but every member path and its exact bytes are protected; values, formulas, styles, relationships and workbook metadata remain covered. Source, content, geometry and other asset bytes are not ignored. Slides 12–14 remain editable. The freeze record is a manifest input; generation cannot silently replace it, and there is no auto-refresh or bypass flag. This protects against accidental changes, not an independent human-authorization boundary.

## Independent exported-file preview

The prior authoring preview did not catch all layout problems. `npm run pptx:preview` opens the exported PPTX through LibreOffice, produces a PDF and one PNG per slide, and binds the render evidence to the exact PPTX checksum. It also checks the SDLC label that previously broke across lines. Inspect every PNG at readable size; a successful conversion is not visual acceptance.

```bash
npm run pptx:preview
# Optional candidate path, contained inside the repository:
npm run pptx:preview -- dist/pptx/<stage>/output/ai-changes-both-sides.pptx
```

Install LibreOffice, Poppler, and Python with `pypdf`, or supply their executable paths in `UA_SOFFICE`, `UA_PDFTOPPM`, and `UA_PDF_PYTHON`. The command uses neither the authoring backend nor a network service. New review evidence stays under `dist/pptx/libreoffice-*/`; missing tools or failed conversion leave the committed pair untouched. PDF/PNG evidence is derived and contains no editable source. No workflow is added or enabled by this command.

## Authoring dependency and honest CI boundary

The current authoring backend is the Codex-bundled `@oai/artifact-tool` **2.8.59**, runtime bundle **26.903.11726**. It is not installed by this repository's `npm ci` and is not redistributed here. A stock GitHub-hosted runner **does not regenerate the deck**. CI independently checks the committed candidate; generation runs in the configured authoring environment. Do not advertise this as a fully autonomous GitHub PPTX build.

The authoring environment supplies `CODEX_PRIMARY_RUNTIME_NODE`, `CODEX_PRIMARY_RUNTIME_NODE_MODULES`, `CODEX_PRIMARY_RUNTIME_PYTHON` and `CODEX_PRIMARY_RUNTIME_BUNDLE_VERSION`. Set `UA_PRESENTATION_SKILL_DIR` to the installed presentation-skill directory before authoring. The skill's authoring-start marker and final visual-review workflow remain required in that environment.

```bash
npm run pptx:pmday
npm run pptx:pmday -- --promote
```

The first command leaves a checked candidate under `dist/pptx/`. The second installs a newly generated, checked PPTX and its manifest together with rollback protection. Promotion alone does not attest human visual acceptance. The command fails explicitly without the reviewed authoring runtime. A future portable backend needs a separate decision, fidelity/editability comparison and regression coverage; no private package, credential or environment dump belongs in Git.

## Observable acceptance contract

- Exactly 14 slides in the source order, 16:9 at 1280×720 design pixels.
- Every slide has solid `#0B0F14` background.
- One fixed foreground illustration on slide 1, requested by the maintainer, with asset checksum and provenance. The package must embed that exact image within the bounded panoramic cover region (96 px side margins; below the title). No other slide/master/layout pictures or image fills. Titles, body text, numbers, diagrams and tables remain native.
- Block rows on slides 2 and 3 stay within symmetric safe margins of at least 96 px.
- Slide 3 uses short neutral links without arrowheads. Slide 5 uses one smooth native generation path and a flat human-capacity scenario line; it is explicitly illustrative. Slide 6 includes the human diagnosis/fix/recovery path. Watch / Explore belong to slide 7.
- Slides 8–10 adapt the supplied historical slides 3–5 as native conceptual diagrams: possible-result distribution, a perspective operating space, and violations outside an approved band. These diagrams carry explicit schematic labels, have no measured numerical axes and do not assert a normal distribution or universal semantic-distance metric. Their bar heights are illustrative geometry, separate from the sample chart.
- Real PowerPoint tables on slides 11 and 13. Slide 10 adds a native outcome-frequency chart with a new embedded workbook snapshot of the explicitly illustrative 196/3/1 counts. Authoring finalization requires that chart and checks its category/value references; the snapshot is not a source workbook with formulas.
- All slide titles, substantive notes and load-bearing evidence numbers are present. The current slide 4 acceptance fixture uses NBER’s September 2026 revision (25.5× / 3.4× / 1.3×), published marketplace shares and Agarwal’s unrounded-to-integers Table 2 percentages; mutation checks reject obsolete NBER and rounded Agarwal replacements. DORA chart readings retain approximation signs.
- Source/generator/validator hashes and the PPTX checksum match the manifest. All explicit text, chart and theme font references must use the requested standard Arial family; unexpected embedded fonts are rejected.
- Authoring finalization additionally checks package integrity, geometry, font policy and re-import.

These checks do not establish research validity, perfect visual layout, Microsoft PowerPoint application compatibility or semantic equivalence between prose and render blocks. No PowerPoint desktop acceptance is claimed without opening it there. The maintainer requested a standard family across PowerPoint, Keynote and Google Slides: Arial Regular/Bold is referenced without redistributing proprietary font binaries. For exact local typography install Arial; otherwise document the renderer’s substitution. The v11 Linux preview resolves Arial to Nimbus Sans and is a layout check, not native application/font acceptance. The old licensed Roboto archive remains historical and is no longer an active build input. Native PowerPoint, Keynote and Google Slides acceptance remains pending.

## Provenance and failure behavior

The manifest binds the exact Markdown bytes, approved cover image and executable generation/validation inputs to the PPTX checksum. It intentionally does not claim a circular self-referential final commit SHA; Git supplies commit provenance after the pair is committed. A stale input fails CI rather than silently leaving an apparently current deck. Local evidence snapshots have their own retrieval manifest and are reference material, not executable render inputs.

Generation stages new files and refuses mixed inputs if source bytes change during the run. Existing output is replaced only after checks pass. The existing publication pair installer verifies checksums, backs up both outputs and restores both after an installation failure. It checks the old pair's internal checksum, not its freshness against newly edited sources, so legitimate regeneration remains possible.

The deck's source remains a teaching adaptation. It does not modify source state in Subprime, redefine UA terminology, promote research or turn illustrative thresholds into universal requirements.
