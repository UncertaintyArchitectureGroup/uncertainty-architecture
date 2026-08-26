import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import {
  buildFurnitureMarkdown,
  buildFurnitureHtml,
  buildFurnitureText,
  insertMarkdownFurniture,
  insertHtmlFurniture,
  insertTextFurniture,
} from "./render-platform-furniture.mjs";
import { repoRoot } from "./publication-rendition.mjs";

const profilePath = path.join(
  repoRoot,
  "quartz",
  "publication",
  "thinking-systems.platforms.json",
);

async function profile() {
  return JSON.parse(await readFile(profilePath, "utf8"));
}

test("publication furniture carries author identity and six-stage UA research path", async () => {
  const p = await profile();
  assert.equal(p.author_furniture.name, "Vitalii Oborskyi");
  assert.match(
    p.author_furniture.bio,
    /creator and principal author of Uncertainty Architecture/,
  );
  assert.equal(p.research_path.items.length, 6);
  assert.deepEqual(
    p.research_path.items.map((item) => item.stage),
    [
      "Practical precursor",
      "Early UA framework",
      "Control-theory reframing",
      "Verification consequence",
      "Control-loop critique",
      "Technical application",
    ],
  );
});

test("LinkedIn furniture uses LinkedIn navigation and Medium furniture prefers Medium navigation", async () => {
  const p = await profile();
  const linkedin = buildFurnitureMarkdown(p, "linkedin");
  const medium = buildFurnitureMarkdown(p, "medium");
  assert.match(linkedin, /recent-activity\/articles/);
  assert.match(linkedin, /linkedin\.com\/pulse\/architecting-uncertainty/);
  assert.match(medium, /medium\.com\/@undersmoker/);
  assert.match(
    medium,
    /medium\.com\/data-science-collective\/architecting-uncertainty/,
  );
});

test("furniture inserts once immediately before Resources in Markdown, HTML, and text", async () => {
  const p = await profile();
  const md = insertMarkdownFurniture(
    "# Article\n\nBody\n\n## Resources\n\n- Repo\n",
    buildFurnitureMarkdown(p, "linkedin"),
  );
  assert.ok(md.indexOf("## About the author") < md.indexOf("## Resources"));
  assert.throws(
    () => insertMarkdownFurniture(md, "again"),
    /already contains author furniture/,
  );

  const html = insertHtmlFurniture(
    "<main><p>Body</p><h2>Resources</h2></main>",
    buildFurnitureHtml(p, "medium"),
  );
  assert.ok(
    html.indexOf("publication-furniture") < html.indexOf("<h2>Resources</h2>"),
  );
  assert.throws(
    () => insertHtmlFurniture(html, "again"),
    /already contains publication furniture/,
  );

  const text = insertTextFurniture(
    "Article\n\nBody\n\nResources\n\n- Repo\n",
    buildFurnitureText(p, "linkedin"),
  );
  assert.ok(text.indexOf("About the author") < text.indexOf("Resources"));
  assert.match(text, /Explore all articles by Vitalii Oborskyi/);
  assert.throws(
    () => insertTextFurniture(text, "again"),
    /already contains author furniture/,
  );
});
