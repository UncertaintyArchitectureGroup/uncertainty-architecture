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
content/presentations/<slug>/deck.mjs
```

The module exports structured metadata, canonical source references, slide IDs, content, and speaker notes. Text and semantic decisions stay reviewable in Git; renderer implementation stays under `quartz/presentations/`.

The `.mjs` source format is deliberate: the repository already runs Node 22, and a structured module avoids adding a second parser or embedding large text blocks in rendering code.

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
npm run pptx:build -- content/presentations/<slug>/deck.mjs
npm run pptx:normalize -- content/presentations/<slug>/deck.mjs
npm run pptx:verify -- content/presentations/<slug>/deck.mjs
npm run pptx:preview -- content/presentations/<slug>/deck.mjs
```

The normal review command is:

```bash
npm run pptx:bundle -- content/presentations/<slug>/deck.mjs
```

`pptx:bundle` runs:

```text
build → OOXML normalization → structural verification → rendered preview → verification with preview evidence
```

## 7. Why OOXML normalization is part of the pipeline

The current PptxGenJS 4.0.1 release has two upstream PowerPoint-repair defects relevant to generated decks:

1. multi-slide files can contain `[Content_Types].xml` overrides for non-existent `slideMaster2.xml`, `slideMaster3.xml`, and so on (upstream issue #1444);
2. the generated notes master contains placeholder shapes that native PowerPoint removes during repair (upstream issue #1443).

`normalize.mjs` does not silently ignore these defects. It:

- removes slide-master content-type overrides that do not correspond to actual archive parts;
- replaces the notes-master shape tree with the minimal structure PowerPoint leaves after its repair pass;
- rewrites the manifest checksum and records normalization evidence.

`verify.mjs` then fails if phantom master overrides remain or if the notes master still carries the problematic placeholder shapes.

This compatibility normalization should be removed or narrowed when the pinned generator version no longer requires it.

### Dependency-security caveat

The target generator is pinned to `pptxgenjs@4.0.1` as development-only presentation tooling. Upstream issue #1474 documents that this release declares `image-size` even though the dependency is not referenced by the published bundles/source, and that the declared package currently carries two HIGH advisories with no patched release.

This must be treated as an explicit merge-time dependency decision rather than hidden by the presentation pipeline. The final target branch must choose one of: a documented temporary development-tool exception, a reviewed patched/forked package, or a generator change. CI installs dependencies with lifecycle scripts disabled, but that does not by itself resolve dependency-audit policy.

The local smoke environment available while this PR was prepared contains PptxGenJS `4.0.0`; `package.json` targets `4.0.1`. Therefore local rendering proves the pipeline shape and the repair normalizer, while the final locked `4.0.1` execution must be re-run by repository CI before merge.

## 8. Verification model

### Structural verification

The verifier checks at least:

- valid ZIP/OOXML archive;
- expected slide count;
- expected notes-page count;
- 16:9 page size;
- actual slide-master/content-type consistency;
- normalized notes master;
- minimum declared font-size floor;
- source and output checksums;
- manifest consistency.

### Render verification

The preview step converts the PPTX through headless LibreOffice, then renders every page to PNG with Poppler and creates a contact sheet. It also rejects apparently blank slides using a simple pixel-variance guard.

### Human review

Automated checks are necessary but not sufficient. A presentation PR should review:

1. the structured source diff;
2. the contact sheet / rendered PDF;
3. the editable PPTX when needed.

Native Microsoft PowerPoint opening remains the final application-specific smoke test when available; do not report it as completed merely because LibreOffice accepts the file.

## 9. GitHub Actions behavior

`.github/workflows/export-presentation.yml` has two entry points:

### Presentation pull requests

It runs only when presentation source/tooling, its workflow, or relevant package files change. The workflow determines the affected presentation decks, builds and verifies them, and uploads `dist/presentations/**` as a review artifact.

### Manual export

`workflow_dispatch` accepts one deck source path and creates the same verified review bundle from the selected ref.

Ordinary UA pull requests should not pay the PPTX/LibreOffice rendering cost.

## 10. Historical deck modernization

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

## 11. Implementation status

- [x] Architecture agreed
- [x] Original editable PPTX located and verified
- [x] Current repository contracts and PR #108 interaction reviewed
- [x] Create implementation branch `agent/pptx-presentation-pipeline` from current `main` after PR #108 merged
- [x] Add canonical `quartz/PRESENTATION-PIPELINE.md`
- [x] Implement presentation source contract
- [x] Implement `ua-dark-v1`
- [x] Add reusable layouts/components and diagram primitives
- [x] Add smoke fixture and contract tests
- [x] Add PPTX generation
- [x] Add OOXML compatibility normalization
- [x] Add structural verification
- [x] Add PPTX → PDF/PNG/contact-sheet verification
- [x] Add path-scoped GitHub Actions workflow + manual dispatch
- [x] Preserve the original PPTX locally as provenance/reference source
- [x] Rebuild the real 22-slide deck as presentation-as-code
- [x] Modernize deck semantics against current UA
- [x] Local semantic review of the revised deck; canonical Bug definition/tail diagnosis correction applied
- [x] Perform visual redesign / consistency pass
- [x] Run local presentation-source unit tests
- [x] Run local LibreOffice render verification
- [x] Run `slides_test.py` overflow verification
- [x] Local implementation review; provenance checksum, generator metadata, workflow path hardening, and reproducibility wording corrections applied
- [ ] Integrate `package.json`, resolve the PptxGenJS dependency-security disposition, and regenerate the repository `package-lock.json` from the final target branch
- [ ] Reconcile source-intake / research index and repository changelog in the actual branch
- [ ] Run final repository-wide validators from the final target branch
- [ ] Run native Microsoft PowerPoint smoke test when available
- [ ] Independent final semantic review against the complete PR diff
- [ ] Independent final implementation review against the complete PR diff
- [ ] Live GitHub CI / readiness review

## 12. Decisions and deviations

### D001 — One vertical-slice PR

Infrastructure and the first real deck stay together. The renderer is therefore proven against a difficult production presentation before merge rather than against only a trivial demo.

### D002 — Historical original and generated rendition remain distinct

The maintainer-supplied `.pptx` is historical editable source material. The new repository deck is explicitly a generated/revised rendition and does not replace the provenance semantics of the original.

### D003 — PR #108 is a dependency boundary, not part of this change

PR #108 merged into `main` as `4fbaa94b721f91134796ae18bfefd87481ef5876`. This presentation change is based on that resulting repository contract and must not duplicate or weaken it.

### D004 — Structured `.mjs` source instead of `deck.md`

The initial design considered a Markdown/YAML presentation DSL. The implementation uses a structured ESM object because it is directly diffable, type-like, dependency-light, and compatible with the repository's existing Node 22 toolchain. Presentation content stays separate from rendering implementation.

### D005 — Explicit generator-compatibility normalization

Testing exposed current PptxGenJS repair-triggering OOXML. The pipeline therefore normalizes and verifies the exact problematic structures rather than pretending successful file generation means native PowerPoint compatibility.

### D006 — Keep speaker notes, but normalize the notes master

Speaker notes are useful in the historical deck and in future talks. The pipeline preserves them in structured source and in the generated PPTX, while normalizing only the upstream-invalid notes-master placeholders.

### D007 — Reproducible pipeline, not byte-identical output

The contract promises one repeatable source → build → normalize → verify path. It does not promise byte-identical PPTX archives across runs because generator/archive metadata may vary. Review provenance is carried through source, historical-source, output, and rendered-artifact checksums in the manifest.

### D008 — Generator provenance is part of the artifact manifest

The manifest records PptxGenJS version, Node version, renderer-contract identifier, source checksum, historical-source checksum, and generated-output checksum. This makes a rendition traceable to both its maintained source and the preserved original without pretending that the generated deck is the historical file.

## 13. Acceptance criteria

The first PR is merge-ready only when all of the following are true on the final target branch:

- a presentation source builds reproducibly through one defined pipeline into an editable PPTX;
- the historical original remains separately identifiable;
- the real 22-slide deck builds through the same public pipeline used by future decks;
- source-contract tests pass;
- OOXML structural checks pass;
- slide count, notes count, aspect ratio, and manifest checks pass;
- rendered PDF/PNG/contact-sheet review evidence exists;
- automated overflow verification passes;
- the presentation workflow is path-scoped and remains on demand outside presentation PRs;
- the final dependency/security disposition is explicit;
- repository-wide validators and GitHub checks pass;
- the PR remains Draft until the repository's AI-assisted readiness protocol is satisfied.
