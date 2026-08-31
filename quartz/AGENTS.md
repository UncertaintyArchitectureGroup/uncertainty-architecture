# Quartz Integration Protocol for AI Contributors

## Scope

This file applies to `quartz/` and supplements the root [`AGENTS.md`](../AGENTS.md). Read [`CONTRIBUTING.md#code-contributions`](../CONTRIBUTING.md#code-contributions) and the architecture map in [`README.md`](README.md) before changing Quartz or publication code.

Read [`PDF-EXPORT.md`](PDF-EXPORT.md) when PDF behavior is affected and [`PLATFORM-RENDITIONS.md`](PLATFORM-RENDITIONS.md) when Medium/LinkedIn packaging is affected.

## Required route

Classify the target before editing:

- **Quartz-derived core** — parser, renderer, components, processors, utilities, browser scripts, shared styles, locales, and build internals;
- **repository integration** — root package/configuration, layout, presentation, and compatibility declarations;
- **UA-owned publication layer** — `quartz/scripts/`, `quartz/publication/`, PDF export, platform renditions, provenance, safety, finalization, and verification;
- **generated output** — `public/` and `dist/`, which are derived artifacts rather than editable sources.

Prefer configuration or an existing UA-owned extension surface over editing Quartz-derived core. When core changes are necessary, preserve the recorded upstream baseline and keep the local delta narrow enough to port during an upgrade.

## Scoped invariants

- Canonical Markdown remains the editable source.
- Reuse existing path-containment, provenance, staging, atomic-finalization, and rollback helpers instead of creating parallel safety implementations.
- A generation or verification failure must preserve the last valid artifact.
- Treat source/output paths, manifests, checksums, and repository references as untrusted until validated inside the declared boundary.
- Keep rendering changes explicit about parsing, resources, links, state, and presentation effects.
- Every defect fix needs a regression that fails without the fix; output/layout changes also require the appropriate integration render or verification path.
- Root companions such as `package.json`, `quartz.config.ts`, `quartz.layout.ts`, `tsconfig.json`, and `quartz/types/` are part of the Quartz integration surface even when outside this directory.
- Generated output is committed only when an explicit publication or historical record requires it.

Update [`README.md`](README.md) only when ownership, upstream provenance, execution topology, or test architecture changes. Update the narrower PDF or platform contract when behavior changes within those existing boundaries.
