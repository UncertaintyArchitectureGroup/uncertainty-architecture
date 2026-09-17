# UA Presentation Pipeline

## 1. Goal

Provide a reproducible, reviewable path from a structured presentation source in Git to an editable `.pptx` plus rendered review evidence.

The pipeline is intentionally **on demand**. Ordinary doctrine, research, or code pull requests do not create presentations. A presentation is prepared in its own pull request when the maintainer asks for one.

The first acceptance deck is `Designing Non-Deterministic Systems`, rebuilt from the maintainer-supplied historical editable PPTX and modernized against the current UA specification.

## 2. Non-goals

This pipeline does not:

- synchronize every research edit into PowerPoint;
- make PPTX the source of truth for UA meaning;
- treat a generated rendition as the historical original;
- rasterize complete slides merely to make generation easier;
- replace human visual review with automated layout heuristics;
- claim that LibreOffice rendering proves native Microsoft PowerPoint compatibility.

## 3. Source and artifact model

### Historical source

Original third-party or maintainer-supplied presentation files are provenance artifacts. When deliberately preserved, they live under `content/raw/` and retain their original binary form.

### Repository presentation source

A maintained presentation lives under:

```text
content/presentations/<slug>/deck.md
content/presentations/<slug>/layout.mjs
```

`deck.md` is the maintained editable presentation source. It owns deck metadata, canonical source references, slide IDs, presenter notes, and human-readable slide content. The companion `layout.mjs` may select layout variants or supply presentation-specific geometry, but it must not become a second prose source of truth. Reusable rendering implementation stays under `quartz/presentations/`.

This split follows the scoped Quartz invariant that canonical editable content remains Markdown while still allowing precise native-PowerPoint composition where a slide needs more than a generic Markdown-to-bullets conversion.

### Generated outputs

Generated files live under:

```text
dist/presentations/<slug>/
```

A full review bundle contains:

```text
<slug>.pptx
<slug>.pdf
<slug>.manifest.json
contact-sheet.png
visual-verification.json
slides/*.png
```

`dist/` outputs are generated renditions and are not historical-source evidence.

## 4. Visual system — `ua-dark-v1`

The initial theme formalizes the visual language of the historical deck rather than inventing a disconnected brand:

- graphite background;
- cyan for control/information paths;
- amber for uncertainty, decision boundaries, and transition;
- green for allowed/safe states;
- red for violations, containment, or risk;
- thin engineering-style strokes;
- large margins and consistent grids;
- native PowerPoint text, shapes, connectors, and diagrams whenever practical.

Typography uses broadly available editable fonts (`Arial Narrow`, `Arial`, `Courier New`) instead of requiring bundled font files.

## 5. Reusable presentation primitives

`quartz/presentations/` owns reusable rendering implementation:

- `theme.mjs` — theme tokens;
- `contract.mjs` — presentation-source validation;
- `components.mjs` — reusable cards, labels, nodes, arrows, metrics, notes, and chrome;
- `diagrams.mjs` — reusable UA diagram primitives;
- `build.mjs` — PPTX generation;
- `normalize.mjs` — explicit OOXML compatibility normalization;
- `verify.mjs` — structural verification;
- `preview.mjs` — LibreOffice/PDF/PNG review rendering;
- `bundle.mjs` — end-to-end orchestration;
- `presentation.test.mjs` — source/theme regression tests;
- `fixtures/` — small source-contract fixtures.

Native editable PPTX objects are preferred. Whole-slide rasterization is an exception, not the normal rendering path.

## 6. Build workflow

From the repository root:

```bash
npm run pptx:build -- content/presentations/<slug>/deck.md
npm run pptx:normalize -- content/presentations/<slug>/deck.md
npm run pptx:verify -- content/presentations/<slug>/deck.md
npm run pptx:preview -- content/presentations/<slug>/deck.md
```

The normal review command is:

```bash
npm run pptx:bundle -- content/presentations/<slug>/deck.md
```

`pptx:bundle` runs:

```text
build → OOXML normalization → structural verification → rendered preview → verification with preview evidence
```

## 7. Repository safety and finalization

Presentation generation is part of the UA-owned publication layer and therefore reuses the existing publication safety surface instead of creating a parallel implementation.

The pipeline must:

- resolve maintained and historical source paths inside the repository boundary;
- constrain generated outputs to `dist/presentations/`;
- reuse `quartz/scripts/publication-path-safety.mjs` for path containment, symlink/hardlink protection, and atomic file writes;
- build into a staging directory, verify the complete candidate bundle there, and only then replace the previously valid rendition;
- preserve the last valid deck bundle if build, normalization, rendering, or verification fails;
- record source and generator provenance in the manifest rather than trusting caller-supplied paths or refs.

This is a correction from the first local prototype, which had its own path resolver and wrote directly into the final deck directory. That prototype proved rendering feasibility but is **not** the merge implementation.

## 8. Why OOXML normalization is part of the pipeline

The current PptxGenJS 4.0.1 release has several upstream OOXML defects that matter for native Microsoft PowerPoint even when LibreOffice accepts the same file:

1. geometry-only shapes can be emitted as `<p:sp>` without the required `<p:txBody>`, which triggers PowerPoint repair (upstream issue #1441);
2. solid-color `<p:bgPr>` backgrounds can omit `<a:effectLst/>`, which triggers PowerPoint repair (upstream issue #1442);
3. the generated notes master contains placeholder shapes that PowerPoint removes during repair, and its theme relationship is not isolated from the presentation theme (upstream issues #1443 and #1449);
4. multi-slide files can contain `[Content_Types].xml` overrides for non-existent `slideMaster2.xml`, `slideMaster3.xml`, and so on (upstream issue #1444).

A lower-severity packaging defect also registers `<Default>` extension content types for media or embedding formats that are not present in the archive (upstream issue #1449). It does not itself trigger repair, but keeping the package declaration aligned with actual parts is cheap and independently verifiable.

`normalize.mjs` therefore:

- inserts the minimal required `<p:txBody>` into geometry-only shapes that lack one;
- inserts `<a:effectLst/>` into solid backgrounds that lack it;
- removes slide-master content-type overrides that do not correspond to actual archive parts;
- replaces the notes-master shape tree with the minimal structure PowerPoint leaves after repair;
- gives the notes master its own `theme2.xml` relationship while preserving speaker-note pages;
- removes unused default-extension declarations by deriving the keep-set from the actual archive parts;
- rewrites the manifest checksum and records normalization evidence.

`verify.mjs` fails if any of those normalized invariants regress. The compatibility layer is deliberately explicit and should be removed or narrowed when the pinned generator version no longer requires it.

### Dependency-security caveat

The target generator is pinned to `pptxgenjs@4.0.1` as development-only presentation tooling. That release still declares `image-size: ^1.2.1`. GitHub advisories `GHSA-w3rx-r6r6-pgpr` and `GHSA-5p2g-fcmc-qvqq` classify all published `image-size` versions through `2.0.2` as affected by denial-of-service infinite-loop bugs, with no installable patched release currently available.

Current PptxGenJS source/package metadata indicates that `image-size` is a declared dependency but not part of the active image-dimension path used by this pipeline; the presentation source also does not accept untrusted runtime image input. That makes exploit reachability through this generator path appear absent, but it does **not** make the dependency-audit finding disappear.

The merge-time disposition should therefore be explicit and time-bounded: document a development-tool exception if repository policy permits it, record the two advisory IDs and the lack of a patched release, and remove the exception as soon as PptxGenJS drops the dead dependency or a reviewed replacement is adopted. Disabling install lifecycle scripts is useful hardening but is not a security fix for this advisory.

The local smoke environment available while this PR was prepared contains PptxGenJS `4.0.0`; `package.json` targets `4.0.1`. Therefore local rendering proves the pipeline shape and normalizer behavior, while the exact locked generator version must be exercised by repository CI before merge.

## 9. Verification model

### Structural verification

The verifier checks at least:

- valid ZIP/OOXML archive;
- expected slide count;
- expected notes-page count;
- 16:9 page size;
- actual slide-master/content-type consistency;
- normalized notes master;
- minimum declared font-size floor;
- source paths resolved through real filesystem containment checks (including symlink escape rejection);
- source and output checksums;
- manifest consistency;
- required OOXML shape text bodies and solid-background effect lists;
- notes-master shape/theme normalization;
- absence of phantom slide-master overrides and unused default-extension declarations.

### Render verification

The preview step converts the PPTX through headless LibreOffice, then renders every page to PNG with Poppler and creates a contact sheet. It also rejects apparently blank slides using a simple pixel-variance guard.

### Human review

Automated checks are necessary but not sufficient. A presentation PR should review:

1. the structured source diff;
2. the contact sheet / rendered PDF;
3. the editable PPTX when needed.

Native Microsoft PowerPoint opening remains the final application-specific smoke test when available; do not report it as completed merely because LibreOffice accepts the file.

## 10. GitHub Actions behavior

`.github/workflows/export-presentation.yml` has two entry points:

### Presentation pull requests

It runs only when presentation source/tooling, its workflow, or relevant package files change. The workflow determines the affected presentation decks, builds and verifies them, and uploads `dist/presentations/**` as a review artifact.

### Manual export

`workflow_dispatch` accepts one deck source path and creates the same verified review bundle from the selected ref.

Ordinary UA pull requests should not pay the PPTX/LibreOffice rendering cost.

## 11. Historical deck modernization

The first maintained deck is deliberately more than a visual port. The repository rendition updates the old teaching shorthand against current UA semantics, including:

- Thinking-System classification based on Consequential Runtime Responsibility and Model Judgment;
- undesirable output / tail event as evidence rather than an automatic Bug;
- Operating Envelope as one part of an approved Requirement;
- closed feedback loop distinguished from complete bounded control architecture;
- capability families treated as logical functions rather than a mandatory four-service stack;
- function-based classification of Prompt Registry, evals, Release Gate, rollback, kill switch, and HITL;
- project authorization distinguished from delivery release;
- deterministic QA retained alongside behavioral evidence;
- UA described as an open engineering specification, not as an already implemented control-engine product.

The historical editable PPTX remains provenance evidence and is not overwritten by this generated rendition.

## 12. Implementation status

- [x] Architecture agreed
- [x] Original editable PPTX located and verified
- [x] Current repository contracts and PR #108 interaction reviewed
- [x] Create implementation branch `agent/pptx-presentation-pipeline` and Draft PR #113 from post-#108 `main`
- [x] Add canonical `quartz/PRESENTATION-PIPELINE.md`
- [x] Prototype presentation source contract locally
- [ ] Refactor maintained deck content from `deck.mjs` to canonical `deck.md` + layout-only `layout.mjs`
- [x] Implement `ua-dark-v1`
- [x] Add reusable layouts/components and diagram primitives
- [x] Add smoke fixture and contract tests
- [x] Prototype PPTX generation locally
- [ ] Reuse repository publication path/provenance helpers; remove the parallel local path-safety implementation
- [ ] Stage and atomically finalize a fully verified presentation bundle so failure preserves the last valid artifact
- [x] Add OOXML compatibility normalization
- [x] Add structural verification
- [x] Add PPTX → PDF/PNG/contact-sheet verification
- [x] Prototype path-scoped GitHub Actions workflow + manual dispatch locally
- [ ] Reconcile workflow and output finalization with current `.github/` and Quartz publication contracts
- [x] Preserve the original PPTX locally as provenance/reference source
- [x] Rebuild the real 22-slide deck as presentation-as-code
- [x] Modernize deck semantics against current UA
- [x] Local semantic review of the revised deck; canonical Bug definition/tail diagnosis correction applied
- [x] Perform visual redesign / consistency pass
- [x] Run local presentation-source unit tests
- [x] Run local LibreOffice render verification
- [x] Run `slides_test.py` overflow verification
- [x] Local implementation review; provenance checksum, generator metadata, workflow path hardening, OOXML repair/conformance normalization, and reproducibility wording corrections applied
- [x] Analyze generator dependency-security exposure and document a proposed time-bounded advisory disposition
- [ ] Integrate `package.json`, resolve the PptxGenJS dependency-security disposition, and regenerate the repository `package-lock.json` from the final target branch
- [ ] Reconcile source-intake / research index and repository changelog in the actual branch
- [ ] Run final repository-wide validators from the final target branch
- [ ] Run native Microsoft PowerPoint smoke test when available
- [ ] Independent final semantic review against the complete PR diff
- [ ] Independent final implementation review against the complete PR diff
- [ ] Live GitHub CI / readiness review

## 13. Decisions and deviations

### D001 — One vertical-slice PR

Infrastructure and the first real deck stay together. The renderer is therefore proven against a difficult production presentation before merge rather than against only a trivial demo.

### D002 — Historical original and generated rendition remain distinct

The maintainer-supplied `.pptx` is historical editable source material. The new repository deck is explicitly a generated/revised rendition and does not replace the provenance semantics of the original.

### D003 — PR #108 is a dependency boundary, not part of this change

PR #108 merged into `main` as `4fbaa94b721f91134796ae18bfefd87481ef5876`. PR #113 is based on that resulting repository contract and must not duplicate or weaken it.

### D004 — Markdown is the editable presentation source

The first local prototype used a structured `deck.mjs`. Re-reading the scoped `quartz/AGENTS.md` exposed that as the wrong repository fit: canonical editable content in the publication layer remains Markdown. The merge design therefore uses `deck.md` for metadata, slide content, source references, and notes, with a companion layout-only module where precise geometry is needed. This keeps semantic edits reviewable as prose without reducing the deck to generic Markdown bullets.

### D005 — Explicit generator-compatibility normalization

Testing exposed current PptxGenJS repair-triggering OOXML. The pipeline therefore normalizes and verifies the exact problematic structures rather than pretending successful file generation means native PowerPoint compatibility.

### D006 — Keep speaker notes, but normalize the notes master

Speaker notes are useful in the historical deck and in future talks. The pipeline preserves them in structured source and in the generated PPTX, while normalizing only the upstream-invalid notes-master placeholders.

### D007 — Reproducible pipeline, not byte-identical output

The contract promises one repeatable source → build → normalize → verify path. It does not promise byte-identical PPTX archives across runs because generator/archive metadata may vary. Review provenance is carried through source, historical-source, output, and rendered-artifact checksums in the manifest.

### D008 — Generator provenance is part of the artifact manifest

The manifest records PptxGenJS version, Node version, renderer-contract identifier, source checksum, historical-source checksum, and generated-output checksum. This makes a rendition traceable to both its maintained source and the preserved original without pretending that the generated deck is the historical file.

### D009 — Time-bounded dependency exception is preferable to a fake fix

`pptxgenjs@4.0.1` still declares `image-size`, while the two current high-severity `image-size` advisories have no installable patched release. The active presentation path does not use that parser for untrusted image input, so the proposed disposition is a documented, reviewable development-tool exception if the repository audit policy requires one. The exception must name `GHSA-w3rx-r6r6-pgpr` and `GHSA-5p2g-fcmc-qvqq`, explain reachability, and carry an explicit removal condition. An override to another vulnerable published version or `--ignore-scripts` would not be presented as remediation.

### D010 — Reuse publication safety ownership rather than fork it

The local prototype created a presentation-specific repository path resolver and wrote directly to final output locations. The scoped Quartz contract explicitly forbids parallel safety implementations and requires failed generation to preserve the last valid artifact. The merge implementation will therefore import the existing publication path-safety/provenance helpers, use staged candidate outputs, and perform verified finalization only after the full bundle passes.

## 14. Acceptance criteria

The first PR is merge-ready only when all of the following are true on the final target branch:

- canonical Markdown presentation source builds reproducibly through one defined pipeline into an editable PPTX;
- presentation layout code does not duplicate maintained slide prose;
- the implementation reuses repository publication safety/provenance helpers and preserves the last valid bundle on failure;
- the historical original remains separately identifiable;
- the real 22-slide deck builds through the same public pipeline used by future decks;
- source-contract tests pass;
- OOXML structural checks pass;
- slide count, notes count, aspect ratio, and manifest checks pass;
- rendered PDF/PNG/contact-sheet review evidence exists;
- automated overflow verification passes;
- the presentation workflow is path-scoped and manually dispatchable;
- ordinary unrelated PRs do not invoke presentation rendering;
- package manifest and lockfile are synchronized, with the generator dependency-security disposition explicitly resolved;
- applicable repository validators and live GitHub CI pass;
- final semantic and implementation reviews have no unresolved blockers.
