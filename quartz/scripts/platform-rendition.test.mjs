import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";

import {
  applyFigureHtmlMarkdown,
  buildAssetMap,
  buildCandidatePublicationState,
  buildPlatformMarkdown,
  convertMarkdownTables,
  countCharacters,
  extractCanonicalFigure8Caption,
  extractLaunchPost,
  htmlToPlainText,
  replaceMermaidWithFigureTokens,
  rewriteRelativeLinks,
  standaloneHtml,
  stripCanonicalHeadingAndNote,
  validateProfile,
  verifyAssetManifest,
} from "./render-platform-renditions.mjs";
import { repoRoot, sha256 } from "./publication-rendition.mjs";

test("platform wrapper removes canonical publication furniture before adding platform furniture", () => {
  const source = `

# Uncertainty Architecture: Thinking Systems — When the Controlled Object Changes

> **Publication note.** Canonical source note.

## Who this article is for

Body

## Continue the work

- Repository
- Working paper`;
  const stripped = stripCanonicalHeadingAndNote(source);
  assert.doesNotMatch(stripped, /^# Uncertainty Architecture:/m);
  assert.doesNotMatch(stripped, /Publication note/);
  assert.doesNotMatch(stripped, /## Continue the work/);
  assert.match(stripped, /^## Who this article is for/m);
});

test("platform table conversion expands rows into labeled readable sections", () => {
  const input =
    "| Term | Meaning |\n|---|---|\n| Thinking System | A responsibility boundary |\n| Model Judgment | Probabilistic selection |";
  const output = convertMarkdownTables(input);
  assert.match(output, /### Thinking System/);
  assert.match(output, /\*\*Meaning:\*\* A responsibility boundary/);
  assert.doesNotMatch(output, /^\|/m);
});

test("platform links become immutable GitHub source links", () => {
  const output = rewriteRelativeLinks(
    "[Working paper](open-engineering-specification-article-draft.md#section)",
    "content/research/notes/thinking-systems-publication-draft.md",
    "Example/Repo",
    "abc123",
  );
  assert.equal(
    output,
    "[Working paper](https://github.com/Example/Repo/blob/abc123/content/research/notes/open-engineering-specification-article-draft.md#section)",
  );
});

test("launch post preserves attribution and stays below the headroom target", async () => {
  const source = await readFile(
    path.join(
      repoRoot,
      "content/research/notes/thinking-systems-linkedin-launch-post.md",
    ),
    "utf8",
  );
  const post = extractLaunchPost(source);
  assert.ok(countCharacters(post) <= 2900);
  assert.match(
    post,
    /thank Arkadiy specifically for the formulation “Thinking Systems\.”/,
  );
  assert.match(post, /Christophe Kolb, Maximiliano Armesto, Jan Rosen/);
  assert.match(post, /I need people to try to break it/);
  assert.match(post, /Read the article: \{\{LINKEDIN_ARTICLE_URL\}\}/);
});

test("editable-source packages never self-certify as frozen publication editions", () => {
  const state = buildCandidatePublicationState(
    { data: { draft: false, canonical_url: "https://example.com/article", additional_publication_urls: ["https://example.com/copy"] } },
    "a".repeat(40),
  );
  assert.equal(state.publication_state, "candidate");
  assert.equal(state.publication_ready, false);
  assert.equal(state.candidate_source_commit, "a".repeat(40));
  assert.equal(state.canonical_url, "https://example.com/article");
  assert.deepEqual(state.additional_publication_urls, ["https://example.com/copy"]);
});

test("platform wrapper does not append a second closing CTA", () => {
  const base = "## Try to Break the Argument\n\nUncertainty Architecture is open source and under validation.";
  const output = buildPlatformMarkdown(
    base,
    { title: "Thinking Systems", subtitle: "Subtitle", publication_note: "Note", closing_note: "DUPLICATE CTA" },
    { repository: "Example/Repo", resources: [] },
    "a".repeat(40),
  );
  assert.equal((output.match(/Uncertainty Architecture is open source and under validation\./g) || []).length, 1);
  assert.doesNotMatch(output, /DUPLICATE CTA/);
});

test("HTML and Markdown review paths consume figure tokens independently", () => {
  const profile = {
    figures: Object.fromEntries(
      ["01", "02", "03", "04", "05", "06", "07", "08a", "08b"].map((id) => [
        id,
        { alt: `Alt ${id}` },
      ]),
    ),
  };
  const assets = [
    ...[1, 2, 3, 4, 5, 6, 7].map((number) => ({
      number,
      panel: null,
      png_path: `dist/publication/thinking-systems/figures/png/figure-${number}.png`,
    })),
    {
      number: 8,
      panel: "A",
      png_path: "dist/publication/thinking-systems/figures/png/figure-8a.png",
    },
    {
      number: 8,
      panel: "B",
      png_path: "dist/publication/thinking-systems/figures/png/figure-8b.png",
    },
  ];
  const assetMap = buildAssetMap({ figures: assets });
  const tokenized = ["01", "02", "03", "04", "05", "06", "07", "08A", "08B"]
    .map((id) => `@@UA_FIGURE_${id}@@`)
    .join("\n\n");
  const htmlSource = applyFigureHtmlMarkdown(tokenized, profile, assetMap);
  assert.match(
    htmlSource,
    /<figure class="platform-figure" data-figure-id="01">/,
  );
  assert.match(htmlSource, /data-figure-id="08a"/);
  assert.match(htmlSource, /data-figure-id="08b"/);
  assert.doesNotMatch(htmlSource, /@@UA_FIGURE_/);
});

test("HTML preview keeps one platform title and one deck", () => {
  const html = standaloneHtml({
    title: "Thinking Systems",
    subtitle: "When the Controlled Object Changes",
    hero: "medium-hero.png",
    body: "<h1>Thinking Systems</h1><blockquote><p>When the Controlled Object Changes</p></blockquote><p>Body</p>",
    sourceCommit: "a".repeat(40),
    sourceState: "committed",
  });
  assert.equal((html.match(/<h1>/g) || []).length, 1);
  assert.equal(
    (html.match(/When the Controlled Object Changes/g) || []).length,
    1,
  );
  assert.match(html, /class="platform-hero"/);
});

test("plain-text conversion keeps image upload markers and link targets", () => {
  const text = htmlToPlainText(
    '<p>Read <a href="https://example.com">this</a>.</p><figure data-figure-id="01"><img/></figure>',
  );
  assert.match(text, /this \(https:\/\/example.com\)/);
  assert.match(text, /UPLOAD IMAGE: figure-01/);
});

test("unreviewed Mermaid remains a hard failure", () => {
  assert.throws(
    () =>
      replaceMermaidWithFigureTokens(
        "```mermaid\nflowchart LR\nA-->B\n```\n\nNo caption",
      ),
    /without a publication caption remains/,
  );
});

test("canonical Figure 8 caption extraction keeps the complete caption line", () => {
  const caption = extractCanonicalFigure8Caption(
    "Before\n\n**Figure 8 — Two orthogonal models.** Complete semantic caption continues here.\n\nAfter",
  );
  assert.equal(
    caption,
    "**Figure 8 — Two orthogonal models.** Complete semantic caption continues here.",
  );
});

test("asset map uses current publication-manifest number and panel identities", () => {
  const map = buildAssetMap({
    figures: [
      {
        number: 3,
        panel: null,
        png_path: "dist/publication/thinking-systems/figures/png/figure-3.png",
      },
      {
        number: 8,
        panel: "A",
        png_path: "dist/publication/thinking-systems/figures/png/figure-8a.png",
      },
      {
        number: 8,
        panel: "B",
        png_path: "dist/publication/thinking-systems/figures/png/figure-8b.png",
      },
    ],
  });
  assert.ok(map.has("03"));
  assert.ok(map.has("08a"));
  assert.ok(map.has("08b"));
});

test("asset manifest verification uses current content digest and Figure 8 fingerprint", () => {
  const raw = "# Publication source\n";
  const source = { raw };
  const profile = {
    source: "content/research/notes/thinking-systems-publication-draft.md",
  };
  const manifest = {
    artifact: "publication-platform-assets",
    source_path: profile.source,
    source_content_sha256: sha256(Buffer.from(raw)),
    figures: [
      ...[1, 2, 3, 4, 5, 6, 7].map((number) => ({
        number,
        panel: null,
        png_renderer: "chromium",
        png_background: "#ffffff",
        png_has_alpha: false,
      })),
      {
        number: 8,
        panel: "A",
        semantic_fingerprint: "f".repeat(64),
        png_renderer: "chromium",
        png_background: "#ffffff",
        png_has_alpha: false,
      },
      {
        number: 8,
        panel: "B",
        semantic_fingerprint: "f".repeat(64),
        png_renderer: "chromium",
        png_background: "#ffffff",
        png_has_alpha: false,
      },
    ],
    heroes: [
      { key: "linkedin_article_cover" },
      { key: "social_preview" },
      { key: "medium_hero" },
    ],
  };
  assert.doesNotThrow(() => verifyAssetManifest(manifest, profile, source));
});

test("platform profile matches current post-PDF asset dimensions and full Taller names", async () => {
  const profile = JSON.parse(
    await readFile(
      path.join(repoRoot, "quartz/publication/thinking-systems.platforms.json"),
      "utf8",
    ),
  );
  assert.equal(validateProfile(profile), profile);
  assert.equal(profile.linkedin.post_max_characters, 3000);
  assert.equal(profile.linkedin.post_url_mention_reserve_characters, 120);
  assert.equal(profile.linkedin.article_max_characters, 125000);
  assert.deepEqual(
    [profile.linkedin.cover.width, profile.linkedin.cover.height],
    [2000, 600],
  );
  assert.deepEqual(
    [profile.medium.hero.width, profile.medium.hero.height],
    [1600, 840],
  );
  assert.equal(profile.medium.image_min_width, 1192);
  assert.equal(profile.medium.image_max_bytes, 25 * 1024 * 1024);
  assert.deepEqual(profile.linkedin.mentions.slice(1), [
    "Christophe Kolb",
    "Maximiliano Armesto",
    "Jan Rosen",
  ]);
});
