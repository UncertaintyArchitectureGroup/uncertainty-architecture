# Contributing to Uncertainty Architecture

Thank you for your interest in contributing. This repository develops a shared doctrine, operational patterns, research record, and reference material for building and governing AI-integrated systems responsibly.

## 1. What this repository accepts

Contributions may include:

- doctrine and glossary clarifications in `00-doctrine/`;
- reusable system and interface patterns in `01-patterns/`;
- AI Control Plane material in `02-ai-control-plane/`;
- reference architectures in `03-reference-architectures/`;
- failure modes and anti-patterns in `04-failure-modes/`;
- research publications, notes, analyses, synthesis, and traceability material in `content/research/`;
- corrections or additions to project-history records in `content/history/`;
- provenance corrections for preserved source snapshots in `content/raw/`;
- diagrams and visual references in `assets/`.

We do not accept:

- large universal agent frameworks or SDKs unrelated to the specification;
- uncurated model-output dumps or prompt experiments without context and versioning;
- normative claims presented without rationale, scope, and operational implications;
- changes that silently rewrite attributed historical work;
- new top-level namespaces created without a clear canonical role.

## 2. Canonical repository locations

Use the existing namespace that matches the material:

- **Specification:** `SPECIFICATION.md` and modules `00-doctrine/` through `04-failure-modes/`.
- **Research:** `content/research/`.
- **Raw source snapshots:** `content/raw/`.
- **Project history and superseded records:** `content/history/`.
- **Visual assets:** `assets/`.
- **Publishing portal and implementation:** `content/index.md`, `quartz/`, and related build configuration.

Publishing infrastructure is not part of the normative specification. Do not create a parallel research, history, governance, or proposal directory when an existing canonical namespace already applies.

The project does not currently require an RFC document or RFC directory. Substantial framework changes should be proposed through a focused branch and pull request. A separate proposal document may be added when it makes a complex decision easier to review, but the document does not become normative merely because it exists.

## 3. Repository ownership and attribution

Vitalii Oborskyi is the project creator and primary maintainer. He retains final authority over repository scope and merges.

Attributed work by named contributors must not be materially changed, reassigned, or presented as consensus without involving the relevant contributor where reasonably possible.

External contributions are welcome. Reviewers may be invited based on subject matter rather than a fixed approval hierarchy.

## 4. Lightweight maintainer workflow

The project currently operates as a maintainer-led open specification.

A maintainer may commit minor changes directly when they are limited to:

- typos and formatting;
- navigation and broken links;
- metadata and frontmatter;
- changelog and roadmap maintenance;
- non-substantive editorial clarification.

A branch and pull request are recommended for:

- substantial documentation changes;
- automation-generated changes;
- multi-file updates;
- changes where reviewing the full diff is useful;
- externally contributed changes.

Draft pull requests are optional. External review is encouraged where it adds value, but it is not required for ordinary maintainer-authored work.

## 5. Changes requiring deliberate review

Use a branch and pull request, and seek appropriate review where practical, for changes that:

- modify normative doctrine;
- introduce or materially change a pattern;
- change core terminology;
- introduce mandatory roles, gates, controls, or processes;
- restructure major repository sections;
- promote research findings into the normative framework;
- make significant scientific, legal, safety, governance, or compliance claims;
- materially affect another contributor's attributed work.

The purpose of review is to improve the specification, not to create ceremony around routine maintenance.

## 6. External contribution process

1. Fork or branch from the current default branch.
2. Keep the change focused and use the current repository structure.
3. Explain what changed, why it changed, and whether the change is research, normative guidance, historical material, or maintenance.
4. Update local navigation or supporting documentation where needed.
5. Confirm licensing and attribution requirements.
6. Open a pull request for maintainer review.

One logical change per pull request is a useful default for substantial work, but tightly related updates may be grouped when that makes review clearer.

## 7. Writing guidelines

- Keep language clear, precise, and operational.
- Distinguish deterministic software behavior from probabilistic model judgment.
- Avoid magical or absolute claims about LLM capabilities.
- State scope, assumptions, and limitations.
- Use control-theory framing where it genuinely clarifies feedback, sensing, correction, and containment.
- Include examples or diagrams when they improve understanding.
- Keep research findings separate from normative requirements until deliberately adopted.
- Mark superseded process or terminology explicitly rather than silently rewriting history.

## 8. Licensing

This repository uses a dual-license model:

- documentation, doctrine, specifications, and research material: CC BY 4.0;
- code and reference implementations: Apache 2.0.

All contributions must comply with the applicable license and preserve required attribution. See [LICENSING.md](LICENSING.md).

## 9. Code of conduct

Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and help maintain a professional, constructive environment.