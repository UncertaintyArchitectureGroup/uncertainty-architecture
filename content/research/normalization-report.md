---
title: Historical Publication Normalization Report
artifact_type: research-normalization-report
status: draft
draft: true
created: 2026-07-25
updated: 2026-07-25
license: CC-BY-4.0
---

# Historical Publication Normalization Report

## Scope

This report covers all five Markdown source snapshots present in `content/raw/` on 2026-07-25. The raw files remain unchanged. Each normalized edition preserves the source's substantive argument and is research evidence rather than a normative Uncertainty Architecture requirement.

## Repository inventory

- `content/raw/` contains five imported historical article snapshots: two English articles with Medium export metadata, one English article with Towards AI export metadata, one Ukrainian article copied from DOU, and one English article without publication metadata.
- `content/research/` contains the public Research Track index, review process, publication and analysis templates, framework traceability scaffold, this report, and the normalized editions under `publications/`.
- The root-level `research/` directory contains three short legacy planning briefs about control theory, metrics, and reference implementations. They do not duplicate the public Research Track documents, although their proposed work is conceptually related. They should be retained unchanged until separately classified; active briefs could later be migrated as explicitly non-normative planning or research-note material, while superseded briefs could be archived. Nothing in that directory warrants removal without a separate review.

## Cleanup details

| Raw source | Normalized edition | Removed platform residue | Formatting repairs | Substantive corrections | Items requiring human review |
|---|---|---|---|---|---|
| `Architecting Uncertainty - A Modern Guide to LLM-Based Software.md` | `publications/architecting-uncertainty-a-modern-guide-to-llm-based-software.md` | Medium export metadata; comments solicitation; duplicated author/profile footer | Added repository frontmatter, status notice, and provenance; removed duplicated source H1; removed bold markup from headings; collapsed repeated blank lines | None | Medium-hosted images remain remote and may need a later asset-archiving decision |
| `UA - Ukr version.md` | `publications/arkhitektura-nevyznachenosti-suchasnyi-pidkhid-do-proiektuvannia-llm-zastosunkiv.md` | Feedback/comment solicitation; community-feedback CTA; duplicated author/profile block | Added repository frontmatter, status notice, and provenance; removed duplicated source H1; removed bold markup from headings; corrected the `6.6` heading level; collapsed repeated blank lines | None | Publication date and canonical DOU URL are absent from the snapshot; the DOU-hosted image remains remote |
| `Uncertainty Architecture - A Modern Approach to Designing LLM Applications.md` | `publications/uncertainty-architecture-a-modern-approach-to-designing-llm-applications.md` | Towards AI/Medium export metadata; feedback/comment solicitation; community-feedback CTA; duplicated author/profile footer | Added repository frontmatter, status notice, and provenance; removed duplicated source H1; nested numbered subsections under their parent sections; collapsed repeated blank lines | None | Medium-hosted images remain remote and may need a later asset-archiving decision |
| `Uncertainty Architecture - Beyond Embeddings- Neuro-Symbolic Verification of Semantic Drift in LLMs - EN.md` | `publications/beyond-embeddings-architecting-risk-and-logic-in-the-age-of-behavioral-software.md` | Chat-export citation markers and `utm_source=chatgpt.com` tracking parameters; trailing blank lines | Added repository frontmatter, status notice, and provenance; removed duplicated source H1; nested chapter, subsection, and reference headings beneath the repository H1; converted copied citation labels to ordinary Markdown link labels | None | Author, publication date, platform, and canonical URL are absent from the source snapshot |
| `Uncertainty Architecture - Why AI Governance is Actually Control Theory.md` | `publications/uncertainty-architecture-why-ai-governance-is-actually-control-theory.md` | Towards AI/Medium export metadata; duplicated author/profile footer; related/important-articles promotion block | Added repository frontmatter, status notice, and provenance; removed duplicated source H1; collapsed repeated blank lines | None | Medium-hosted images remain remote and may need a later asset-archiving decision |

## Quality checks

Each normalized edition was checked for a single H1, non-skipping heading levels, balanced fenced code blocks, repeated long paragraphs, and preservation of substantive source lines outside the residue ranges documented above. Links and images were retained unless only tracking metadata was removed. No footnotes or Markdown tables were present in the raw snapshots.
