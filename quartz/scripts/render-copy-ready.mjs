#!/usr/bin/env node

import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { repoRoot, sha256 } from "./publication-rendition.mjs";

const publicationRoot = path.join(
  repoRoot,
  "dist",
  "publication",
  "thinking-systems",
);
const renditionRoot = path.join(publicationRoot, "renditions");
const pngDataUriPrefix = "data:image/png;base64";

function isInside(root, candidate) {
  const relative = path.relative(root, candidate);
  return relative === "" || (!relative.startsWith("..") && !path.isAbsolute(relative));
}

function mimeTypeFor(filePath) {
  const extension = path.extname(filePath).toLowerCase();
  if (extension === ".png") return "image/png";
  if (extension === ".jpg" || extension === ".jpeg") return "image/jpeg";
  if (extension === ".webp") return "image/webp";
  throw new Error(`Unsupported copy-ready image type: ${extension || "none"}`);
}

export async function embedLocalImages(html, articlePath, allowedRoot = publicationRoot) {
  const pattern = /<img\b([^>]*?)\bsrc="([^"]+)"([^>]*)>/gi;
  const matches = [...html.matchAll(pattern)];
  let output = html;
  let embedded = 0;

  for (const match of matches) {
    const [full, before, source, after] = match;
    if (/^(?:data:|https?:|mailto:|tel:|#)/i.test(source)) continue;

    const resolved = path.resolve(path.dirname(articlePath), source);
    if (!isInside(allowedRoot, resolved)) {
      throw new Error(`Copy-ready image escapes publication root: ${source}`);
    }
    const bytes = await readFile(resolved);
    if (bytes.length === 0) throw new Error(`Copy-ready image is empty: ${source}`);
    const mimeType = mimeTypeFor(resolved);
    const prefix = mimeType === "image/png" ? pngDataUriPrefix : `data:${mimeType};base64`;
    const dataUri = `${prefix},${bytes.toString("base64")}`;
    output = output.replace(full, `<img${before}src="${dataUri}"${after}>`);
    embedded += 1;
  }

  return { html: output, embedded };
}

export function buildCopyReadyDocument(html, platformName) {
  let value = html
    .replace(
      /<figcaption><strong>Upload file:<\/strong>[\s\S]*?<\/figcaption>/gi,
      "",
    )
    .replace(/<p class="provenance">[\s\S]*?<\/p>/gi, "")
    .replace("<main>", '<main id="copy-surface">');

  if (!value.includes('id="copy-surface"')) {
    throw new Error("Copy-ready source is missing the article <main> element");
  }

  const platformLabel = platformName === "linkedin" ? "LinkedIn" : "Medium";
  const toolbar = `<div class="copy-ready-toolbar" role="region" aria-label="Copy-ready controls"><strong>${platformLabel} copy-ready article</strong><span>All inline article images are embedded in this one HTML file. On iPad or when browser clipboard access is blocked, use Select article and then tap Copy in the system menu.</span><button id="copy-article" type="button">Copy article</button><button id="select-article" type="button">Select article</button><span id="copy-status" aria-live="polite"></span></div>`;
  value = value.replace("<body>", `<body>${toolbar}`);
  value = value.replace(
    "</style>",
    ".copy-ready-toolbar{position:sticky;top:0;z-index:10;display:flex;gap:12px;align-items:center;flex-wrap:wrap;padding:12px 16px;background:#111827;color:white;font-family:Arial,sans-serif}.copy-ready-toolbar button{padding:8px 14px;border:0;border-radius:6px;font-weight:700;cursor:pointer}.copy-ready-toolbar span{font-size:13px}.copy-ready-toolbar #copy-status{font-weight:700;color:#bbf7d0}\n</style>",
  );
  const script = `<script>
(function(){
  const copyButton=document.getElementById('copy-article');
  const selectButton=document.getElementById('select-article');
  const status=document.getElementById('copy-status');
  const surface=document.getElementById('copy-surface');

  function selectArticle(message='Article selected — tap Copy in the system menu.'){
    const selection=window.getSelection();
    const range=document.createRange();
    range.selectNodeContents(surface);
    selection.removeAllRanges();
    selection.addRange(range);
    status.textContent=message;
  }

  async function copyArticle(){
    status.textContent='';
    try{
      if(navigator.clipboard && window.ClipboardItem){
        const htmlBlob=new Blob([surface.innerHTML],{type:'text/html'});
        const textBlob=new Blob([surface.innerText],{type:'text/plain'});
        await navigator.clipboard.write([new ClipboardItem({'text/html':htmlBlob,'text/plain':textBlob})]);
        status.textContent='Copied';
        return;
      }
    }catch(error){}
    selectArticle('Automatic copy is unavailable. Article selected — tap Copy in the system menu.');
  }

  copyButton.addEventListener('click',copyArticle);
  selectButton.addEventListener('click',()=>selectArticle());
})();
</script>`;
  value = value.replace("</body>", `${script}</body>`);
  return value;
}

async function writeCopyReady(platformName) {
  const platformDir = path.join(renditionRoot, platformName);
  const articlePath = path.join(platformDir, "article.html");
  const source = await readFile(articlePath, "utf8");
  const embedded = await embedLocalImages(source, articlePath);
  const copyReady = buildCopyReadyDocument(embedded.html, platformName);
  const target = path.join(platformDir, "copy-ready.html");
  await writeFile(target, `${copyReady}\n`, "utf8");

  const expected = platformName === "medium" ? 10 : 9;
  if (embedded.embedded !== expected) {
    throw new Error(
      `${platformName} copy-ready HTML embedded ${embedded.embedded} images; expected ${expected}`,
    );
  }
  if ((copyReady.match(/src="data:image\//g) || []).length !== expected) {
    throw new Error(`${platformName} copy-ready HTML still has non-embedded article images`);
  }
  return { target, embedded: embedded.embedded, sha256: sha256(Buffer.from(`${copyReady}\n`)) };
}

async function main() {
  const medium = await writeCopyReady("medium");
  const linkedin = await writeCopyReady("linkedin");

  const readme = `# Copy-ready platform articles\n\nOpen the platform-specific \`copy-ready.html\` locally in a browser. Use **Copy article** when browser clipboard access is available. On iPad, local-file clipboard access may be blocked; use **Select article**, then tap **Copy** in the system selection menu. The selection is intentionally left active so the manual copy path remains usable.\n\nThe HTML is self-contained: inline article images are embedded as data URIs, so no image folder is required for the primary copy/paste path.\n\n- LinkedIn: \`linkedin/copy-ready.html\` embeds ${linkedin.embedded} article figures. The LinkedIn cover remains a separate platform upload.\n- Medium: \`medium/copy-ready.html\` embeds the hero plus ${medium.embedded - 1} article figures.\n- Keep the generated PNG files as fallback because LinkedIn or Medium may sanitize embedded images during paste. If an image is dropped, use the normal \`article.md\` placement guide and upload the matching PNG.\n\nThis convenience artifact is a distribution rendition only; canonical content remains the repository Markdown source.\n`;
  const readmePath = path.join(renditionRoot, "copy-ready-readme.md");
  await writeFile(readmePath, readme, "utf8");

  const manifestPath = path.join(renditionRoot, "platform-renditions.manifest.json");
  const manifest = JSON.parse(await readFile(manifestPath, "utf8"));
  manifest.copy_ready = {
    self_contained_html: true,
    clipboard_behavior: "best-effort-platform-dependent",
    selection_fallback: true,
    selection_fallback_preserves_selection: true,
    linkedin_embedded_article_images: linkedin.embedded,
    medium_embedded_article_images: medium.embedded,
    linkedin_cover_separate: true,
    png_fallback_retained: true,
  };
  manifest.outputs["linkedin/copy-ready.html"] = linkedin.sha256;
  manifest.outputs["medium/copy-ready.html"] = medium.sha256;
  manifest.outputs["copy-ready-readme.md"] = sha256(Buffer.from(readme));
  await writeFile(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`, "utf8");

  console.log(`Copy-ready LinkedIn HTML: ${path.relative(repoRoot, linkedin.target)} (${linkedin.embedded} embedded images)`);
  console.log(`Copy-ready Medium HTML: ${path.relative(repoRoot, medium.target)} (${medium.embedded} embedded images)`);
}

const isEntryPoint =
  process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isEntryPoint) {
  main().catch((error) => {
    console.error(`Copy-ready rendering failed: ${error instanceof Error ? error.message : String(error)}`);
    process.exitCode = 1;
  });
}
