---
title: Contributing to Uncertainty Architecture
artifact_type: repository-process
status: informative
maturity: active
module: repository
topics:
  - repository-architecture
  - navigation
  - provenance
tags:
  - ua/module/repository
  - ua/type/repository-process
  - ua/status/informative
  - ua/topic/repository-architecture
  - ua/topic/navigation
  - ua/topic/provenance
canonical_for:
  - contribution-workflow
---

# Contributing to Uncertainty Architecture

Thank you for your interest in contributing. This repository develops a shared doctrine, operational patterns, research record, and reference material for building and governing AI-integrated systems responsibly.

## 1. What this repository accepts

Contributions may include:

- doctrine and glossary clarifications in `00-doctrine/`;
- reusable system and interface patterns in `01-patterns/`;
- AI Control Plane material in `02-ai-control-plane/`;
- reference architectures in `03-reference-architectures/`;
- failure modes and anti-patterns in `04-failure-modes/`;
- research publications, notes, analyses, synthesis, worked-application observations, and traceability material in `content/research/`;
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
- **Document metadata and tag vocabulary:** `DOCUMENT-METADATA.md`.
- **Repository orientation for AI agents:** `AGENTS.md`.

Publishing infrastructure is not part of the normative specification. Do not create a parallel research, history, governance, or proposal directory when an existing canonical namespace already applies.

The project does not currently require an RFC document or RFC directory. Substantial framework changes should be proposed through a focused branch and pull request. A separate proposal document may be added when it makes a complex decision easier to review, but the document does not become normative merely because it exists.

## 3. Document metadata and navigation

New maintained conceptual documents should follow [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md).

At minimum, classify the document by:

- `artifact_type`;
- `status`;
- `module`;
- a small set of controlled `topics`;
- corresponding hierarchical `ua/...` tags.

Use `maturity` for lifecycle state such as draft, active, stable, or superseded. Do not use `draft` as a substitute for normative status.

Metadata supports navigation, Obsidian queries, publishing, and machine retrieval. It does not make a document normative and must not contradict `SPECIFICATION.md` or the relevant module README.

Do not mechanically rewrite raw source snapshots or historical publication bodies merely to normalize metadata. The convention is applied incrementally when maintained documents are created or materially edited.

### Local navigation validation

Before pushing a change to framework navigation or compact breadcrumbs, run from the repository root:

```bash
python3 .github/scripts/validate_navigation.py
```

The validator has no third-party Python dependencies and is compatible with Python 3.8 or later. It verifies the declared entry pages, navigation order, owning destinations, lifecycle fragments, and selected leaf breadcrumbs. It resolves the repository root from the script location, so the same validator may also be invoked through an appropriate relative or absolute script path from another working directory.

GitHub Actions additionally runs the validator and an offline `lychee` scan on every pull request and every push to `main`. The CI scan validates maintained repository-relative links, directory indexes, Markdown heading fragments, and explicit HTML compatibility anchors. External-network availability is intentionally outside the deterministic repository-integrity check.

### Local repository contract validation

Before pushing a repository-policy change or any change that adds, removes, renames, or materially edits a protected path or landing-page function, run:

```bash
python3 .github/scripts/validate_repository_contract.py
python3 .github/tests/repository_contract/test_repository_contract.py
```

The machine-readable contract is maintained in [`.github/policy/repository-contract.json`](.github/policy/repository-contract.json). It protects critical files and sections, required canonical and compatibility paths, stable repository links, explicit compatibility markers, and the current top-level namespace. It does not freeze complete Markdown documents or replace architectural review.

A legitimate contract change must update the owning document, the contract, and an appropriate regression fixture in the same pull request. Do not remove a protected rule merely because a check fails; determine whether the repository change is wrong, the contract is stale, or a deliberate compatibility decision is required.

GitHub Actions runs the real-repository contract validation and the independent mutation fixtures as separate checks on every pull request and every push to `main`.

### Local metadata and canonical-ownership validation

Before pushing a maintained-document, metadata-policy, glossary, or canonical-ownership change, run:

```bash
python3 .github/scripts/validate_metadata.py --mode all
python3 .github/tests/metadata_contract/test_metadata.py
```

The machine-readable metadata policy is maintained in [`.github/policy/metadata-contract.json`](.github/policy/metadata-contract.json). It checks required frontmatter on the declared baseline, controlled values, structural and topic tag projection, active `canonical_for` uniqueness, protected glossary entries, and selected terminology warnings.

Metadata errors fail CI. Warnings identify review candidates such as title/H1 drift, unusually large tag sets, or selected superseded terminology and do not fail by default.

A responsibility transfer must not leave two active documents claiming the same `canonical_for` value. Mark the prior owner superseded, remove its claim, or make another explicit ownership decision in the same pull request.

Publication bodies, raw sources, and legacy historical material may retain distinct publishing or provenance metadata. Do not normalize them mechanically to satisfy the current UA classification schema.

### Local diff-aware change-coupling validation

Before pushing a pull request that changes maintained framework material, repository policy, research-state decisions, or maintained paths, compare the branch with its intended base and validate the machine-readable PR declaration:

```bash
python3 .github/scripts/validate_change_coupling.py \
  --base origin/main \
  --head HEAD \
  --pr-body-file /path/to/pr-body.md
python3 .github/tests/change_coupling/test_change_coupling.py
```

The policy is maintained in [`.github/policy/change-coupling-contract.json`](.github/policy/change-coupling-contract.json). It checks that the `ua-change-contract` block is valid and consistent with the actual diff, and that notable changes carry the companion updates they claim or require.

The validator enforces:

- changelog coupling for notable changes;
- declaration/file consistency for glossary, roadmap, and research traceability;
- traceability updates for explicit research-state decisions;
- compatibility decisions and changelog updates for deletion or rename of maintained material;
- intersection between declared `owning_paths` and the actual diff;
- repository-policy baseline coupling to the roadmap.

Exception labels are narrow, category-specific maintenance escapes. They are not ordinary contributor controls and must not be used to hide a stale contract or incomplete change. Applying an exception requires maintainer authority through repository permissions and a visible explanation in the pull-request body.

## 4. Repository ownership and attribution

Vitalii Oborskyi is the project creator and primary maintainer. He retains final authority over repository scope and merges.

Attributed work by named contributors must not be materially changed, reassigned, or presented as consensus without involving the relevant contributor where reasonably possible.

External contributions are welcome. Reviewers may be invited based on subject matter rather than a fixed approval hierarchy.

## 5. Lightweight maintainer workflow

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

For a repository-changing pull request:

1. identify the owning documents and actual change class;
2. determine required changelog, glossary, roadmap, traceability, and compatibility updates from the change itself;
3. make the smallest coherent diff and required companion updates;
4. complete the machine-readable `ua-change-contract` block;
5. run the applicable navigation, repository-contract, metadata, and change-coupling checks;
6. reconcile the pull-request description with the final diff before requesting review or merge.

## 6. Changes requiring deliberate review

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

## 7. External contribution process

1. Fork or branch from the current default branch.
2. Keep the change focused and use the current repository structure.
3. Explain what changed, why it changed, and whether the change is research, normative guidance, reference material, historical material, or maintenance.
4. Add or update metadata, local navigation, and cross-links where needed.
5. When the change resolves, narrows, rejects, supersedes, reopens, or promotes a research question, reconcile the affected source-intake note, working note, analysis, or [`framework-traceability.md`](content/research/framework-traceability.md) under the [`Research Review Process`](content/research/review-process.md).
6. Confirm licensing and attribution requirements.
7. Determine required changelog, glossary, roadmap, traceability, and compatibility updates from the actual diff.
8. Complete the human-readable companion-update fields and machine-readable `ua-change-contract` block in the pull-request template.
9. Run the applicable local navigation, repository-contract, metadata, change-coupling, and policy self-test commands.
10. Open the pull request for maintainer review and keep its description synchronized with the final diff.

One logical change per pull request is a useful default for substantial work, but tightly related updates may be grouped when that makes review clearer.

Research reconciliation records meaningful changes in evidence, interpretation, question state, or framework destination. It should not duplicate pull-request history or become a session log.

## 8. Writing guidelines

- Keep language clear, precise, and operational.
- Distinguish deterministic software behavior from probabilistic model judgment.
- Use **Thinking Systems** as the current category; preserve earlier terminology only in historical context.
- Avoid magical or absolute claims about LLM capabilities.
- State scope, assumptions, and limitations.
- Use control-theory framing where it genuinely clarifies feedback, sensing, correction, and containment.
- Include examples or diagrams when they improve understanding.
- Keep research findings separate from normative requirements until deliberately adopted.
- Mark superseded process or terminology explicitly rather than silently rewriting history.
- Treat numerical thresholds, sample sizes, role names, and review cadences as contextual unless a normative document deliberately establishes them.
- Keep structured metadata and `ua/...` tags consistent with the document's actual role and status.

## 9. Agent-assisted changes

Language models and coding agents should read [`AGENTS.md`](AGENTS.md) before making repository-wide or normative changes.

Agent-assisted work must preserve the same boundaries as human-authored work. In particular, an agent must not promote research by implication, rewrite provenance, create parallel canonical entry points, or infer authority from tags, recency, visibility, or external attention.

Agents should use the research reconciliation trigger in `AGENTS.md` when source-derived framework work, worked applications, incidents, or operational observations change research state.

## 10. Licensing

This repository uses a dual-license model:

- documentation, doctrine, specifications, and research material: CC BY 4.0;
- code and reference implementations: Apache 2.0.

All contributions must comply with the applicable license and preserve required attribution. See [LICENSING.md](LICENSING.md).

## 11. Code of conduct

Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and help maintain a professional, constructive environment.
