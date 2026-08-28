#!/usr/bin/env python3
"""Apply the final scoped review fixes for PR #93, then delete this helper."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def write(relative: str, content: str) -> None:
    (ROOT / relative).write_text(content, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


# 1. Keep public category wording aligned with the article contract.
profile_path = "quartz/publication/thinking-systems.platforms.json"
profile = json.loads(read(profile_path))
profile["author_furniture"]["bio"] = (
    "Vitalii Oborskyi is the creator and principal author of Uncertainty Architecture, "
    "an open engineering specification and research program for systems in which one or "
    "more Consequential Runtime Responsibilities depend partly on probabilistic Model "
    "Judgment. He is Head of Delivery & Operations at Developex and has more than two "
    "decades of experience across software engineering, delivery, and engineering "
    "governance. His current work focuses on non-deterministic systems, AI governance, "
    "socio-technical control architectures, and the changing mechanics of software delivery."
)
write(profile_path, json.dumps(profile, indent=2, ensure_ascii=False) + "\n")

launch_path = "content/research/notes/thinking-systems-linkedin-launch-post.md"
launch = read(launch_path)
launch = replace_once(
    launch,
    "In the article, a Thinking System is software in which one or more consequential runtime responsibilities depend partly on probabilistic Model Judgment rather than being fully specified through explicitly encoded logic in advance.",
    "In the article, a Thinking System is a software system in which one or more Consequential Runtime Responsibilities depend partly on probabilistic Model Judgment rather than being fully specified through explicitly encoded logic in advance.",
    "LinkedIn launch-post category definition",
)
match = re.search(
    r"<!-- platform-copy:start -->\s*([\s\S]*?)\s*<!-- platform-copy:end -->",
    launch,
)
if not match:
    raise RuntimeError("LinkedIn launch post lost platform-copy markers")
post_length = len(match.group(1).strip())
if post_length > 2900 or post_length + 120 > 3000:
    raise RuntimeError(
        f"LinkedIn launch post no longer preserves required headroom: {post_length}"
    )
write(launch_path, launch)


# 2. Make the Medium checklist point to one canonical publication path.
rendition_path = "quartz/scripts/render-platform-renditions.mjs"
rendition = read(rendition_path)
new_checklist = r'''export function buildChecklist(
  platformName,
  profile,
  source,
  sourceCommit,
  publicationReady,
) {
  const official = profile.official_sources;
  const lines = [
    `# ${platformName === "linkedin" ? "LinkedIn" : "Medium"} Publishing Checklist`,
    "",
    `- Source: \`${source.relative}\``,
    `- Source commit: \`${sourceCommit}\``,
    `- Package state: ${publicationReady ? "published edition" : "CANDIDATE — generated from the editable publication draft; publication itself comes before repository freeze"}`,
    "- Review `article.html` and the native platform preview before publishing.",
    "- Recheck links, captions, table conversion, and the Figure 8A/8B sequence.",
  ];
  if (platformName === "linkedin") {
    lines.push(
      "- Use `article.md` as the image-placement and alt-text guide.",
      "- Upload every image named by an `UPLOAD IMAGE` marker; do not paste Mermaid source.",
      "- Upload `../../cover-linkedin-article.png` as the article cover.",
      "- Apply `seo.json` in LinkedIn SEO settings.",
      "- Publish the native LinkedIn article first, copy its exact URL, and replace `{{LINKEDIN_ARTICLE_URL}}` in `launch-post.txt` before publishing the launch post.",
      "- Convert the names in `launch-post.txt` into actual LinkedIn mentions before publishing the launch post.",
      `- Keep the launch post at or below ${profile.linkedin.post_max_characters} characters after replacing the URL placeholder.`,
      "- Verify the generated labeled-section replacement for source tables.",
      "",
      `Official references: ${official.linkedin_article_limits} · ${official.linkedin_article_images} · ${official.linkedin_seo}`,
    );
  } else {
    lines.push(
      "- Open `copy-ready.html` and confirm that the Medium hero and all nine article figures are visible before copying.",
      "- Use **Select All → Copy → Paste** to transfer the rich text; this package does not claim Medium clipboard image transfer.",
      "- Follow `upload/README.md` and upload `00-medium-hero.png` through `09-figure-08b.png` in order.",
      "- Use `article.md` as the exact image-placement and alt-text guide.",
      "- Keep Figure 8A and Figure 8B together under the shared Figure 8 caption.",
      "- After the first external publication establishes the principal canonical URL, use Medium import from that URL where appropriate or set the canonical URL manually.",
      "- Confirm each uploaded figure meets the 1,192 px minimum when full placement options are needed.",
      "",
      `Official references: ${official.medium_images} · ${official.medium_import} · ${official.medium_canonical}`,
    );
  }
  return `${lines.join("\n")}\n`;
}'''
pattern = re.compile(
    r"function buildChecklist\([\s\S]*?\n}\n\nasync function main\(\)",
    re.MULTILINE,
)
rendition, count = pattern.subn(new_checklist + "\n\nasync function main()", rendition, count=1)
if count != 1:
    raise RuntimeError(f"Medium checklist function replacement matched {count} times")
write(rendition_path, rendition)


# 3. Verify that the self-contained Medium preview and manual upload kit are byte-identical.
verifier_path = "quartz/scripts/verify-publication-package.mjs"
verifier = read(verifier_path)
count_block = '''export function countDataImages(html) {
  return (String(html).match(/src="data:image\\//g) || []).length;
}
'''
helpers = '''export function countDataImages(html) {
  return (String(html).match(/src="data:image\\//g) || []).length;
}

export function extractEmbeddedDataImages(html) {
  const images = [];
  const pattern =
    /<img\\b[^>]*\\bsrc=(["'])data:([^;,"']+);base64,([^"']+)\\1[^>]*>/gi;
  for (const match of String(html).matchAll(pattern)) {
    const bytes = Buffer.from(match[3], "base64");
    assert(bytes.length > 0, "Embedded preview image is empty");
    images.push({
      mimeType: match[2].toLowerCase(),
      bytes,
      sha256: sha256(bytes),
    });
  }
  return images;
}

export function assertMediumPreviewImageManifest(html, copyReady) {
  const listed = copyReady?.medium_upload_assets;
  const assets = Array.isArray(listed)
    ? listed.filter((asset) => asset.id !== "instructions")
    : [];
  const embedded = extractEmbeddedDataImages(html);
  assert(
    assets.length === 10,
    "Medium preview comparison requires ten ordered upload images",
  );
  assert(
    embedded.length === assets.length,
    `Medium preview contains ${embedded.length} embedded images; expected ${assets.length}`,
  );
  for (const [index, image] of embedded.entries()) {
    const asset = assets[index];
    assert(
      image.mimeType === "image/png",
      `Medium preview image ${index} is not PNG`,
    );
    assert(
      image.sha256 === asset.sha256,
      `Medium preview image ${index} does not match ${asset.path}`,
    );
  }
  return { embedded, assets };
}
'''
verifier = replace_once(
    verifier,
    count_block,
    helpers,
    "embedded Medium image verifier insertion",
)
old_medium_branch = '''  } else {
    assertMediumUploadManifest(manifest.copy_ready);
    const uploadReadme = await readFile(
      path.join(directory, "upload", "README.md"),
      "utf8",
    );
    assert(
      uploadReadme.includes(
        "Medium preserves the pasted rich text but drops clipboard images",
      ),
      "Medium upload instructions do not record the observed platform limitation",
    );
    assert(
      uploadReadme.includes("Figure 8A") && uploadReadme.includes("Figure 8B"),
      "Medium upload instructions lost Figure 8 coupling",
    );
  }
'''
new_medium_branch = '''  } else {
    assertMediumUploadManifest(manifest.copy_ready);
    const preview = assertMediumPreviewImageManifest(
      copyReady,
      manifest.copy_ready,
    );
    for (const [index, asset] of preview.assets.entries()) {
      const uploadBytes = await readFile(path.join(renditionRoot, asset.path));
      assert(
        uploadBytes.equals(preview.embedded[index].bytes),
        `Medium preview image ${index} is not byte-identical to ${asset.path}`,
      );
    }

    const [uploadReadme, checklist] = await Promise.all([
      readFile(path.join(directory, "upload", "README.md"), "utf8"),
      readFile(path.join(directory, "publishing-checklist.md"), "utf8"),
    ]);
    assert(
      uploadReadme.includes(
        "Medium preserves the pasted rich text but drops clipboard images",
      ),
      "Medium upload instructions do not record the observed platform limitation",
    );
    assert(
      uploadReadme.includes("Figure 8A") && uploadReadme.includes("Figure 8B"),
      "Medium upload instructions lost Figure 8 coupling",
    );
    assert(
      checklist.includes("copy-ready.html") &&
        checklist.includes("upload/README.md") &&
        checklist.includes("article.md"),
      "Medium publishing checklist is not bound to the copy-ready and ordered-upload path",
    );
    assert(
      !checklist.includes("../../medium-hero.png") &&
        !checklist.includes("Upload every image named by an `UPLOAD IMAGE` marker"),
      "Medium publishing checklist still exposes the obsolete generic image route",
    );
  }
'''
verifier = replace_once(
    verifier,
    old_medium_branch,
    new_medium_branch,
    "Medium final-package verification branch",
)
write(verifier_path, verifier)


# 4. Add regression coverage for exact terminology, one Medium checklist, and image identity.
furniture_test_path = "quartz/scripts/platform-furniture.test.mjs"
furniture_test = read(furniture_test_path)
furniture_test = replace_once(
    furniture_test,
    '''  assert.match(
    p.author_furniture.bio,
    /creator and principal author of Uncertainty Architecture/,
  );
''',
    '''  assert.match(
    p.author_furniture.bio,
    /creator and principal author of Uncertainty Architecture/,
  );
  assert.match(
    p.author_furniture.bio,
    /systems in which one or more Consequential Runtime Responsibilities depend partly on probabilistic Model Judgment/,
  );
  assert.doesNotMatch(
    p.author_furniture.bio,
    /can materially influence runtime behavior/,
  );
''',
    "author-furniture terminology regression",
)
write(furniture_test_path, furniture_test)

platform_test_path = "quartz/scripts/platform-rendition.test.mjs"
platform_test = read(platform_test_path)
platform_test = replace_once(
    platform_test,
    "  buildCandidatePublicationState,\n",
    "  buildCandidatePublicationState,\n  buildChecklist,\n",
    "platform checklist test import",
)
platform_test = replace_once(
    platform_test,
    '''  assert.match(post, /I need people to try to break it/);
  assert.match(post, /Read the article: \\{\\{LINKEDIN_ARTICLE_URL\\}\\}/);
});
''',
    '''  assert.match(post, /I need people to try to break it/);
  assert.match(
    post,
    /a Thinking System is a software system in which one or more Consequential Runtime Responsibilities depend partly on probabilistic Model Judgment/,
  );
  assert.match(post, /Read the article: \\{\\{LINKEDIN_ARTICLE_URL\\}\\}/);
});

test("Medium checklist exposes one ordered manual-upload path", () => {
  const checklist = buildChecklist(
    "medium",
    {
      medium: {},
      official_sources: {
        medium_images: "https://example.com/images",
        medium_import: "https://example.com/import",
        medium_canonical: "https://example.com/canonical",
      },
    },
    { relative: "content/research/notes/article.md" },
    "a".repeat(40),
    false,
  );
  assert.match(checklist, /copy-ready\\.html/);
  assert.match(checklist, /upload\\/README\\.md/);
  assert.match(checklist, /00-medium-hero\\.png/);
  assert.match(checklist, /09-figure-08b\\.png/);
  assert.match(checklist, /article\\.md/);
  assert.doesNotMatch(checklist, /\\.\\.\\/\\.\\.\\/medium-hero\\.png/);
  assert.doesNotMatch(checklist, /Upload every image named by/);
});
''',
    "launch-post terminology and Medium checklist tests",
)
write(platform_test_path, platform_test)

verifier_test_path = "quartz/scripts/verify-publication-package.test.mjs"
verifier_test = read(verifier_test_path)
verifier_test = replace_once(
    verifier_test,
    '''  assertMediumUploadManifest,
  assertPlatformFigureInventory,
  countDataImages,
} from "./verify-publication-package.mjs";
''',
    '''  assertMediumPreviewImageManifest,
  assertMediumUploadManifest,
  assertPlatformFigureInventory,
  countDataImages,
  extractEmbeddedDataImages,
} from "./verify-publication-package.mjs";
import { sha256 } from "./publication-rendition.mjs";
''',
    "Medium preview verifier test imports",
)
append_tests = '''

function mediumPreviewFixture() {
  const buffers = Array.from({ length: 10 }, (_, index) =>
    Buffer.from(`medium-preview-${index}`, "utf8"),
  );
  const manifest = validMediumManifest();
  const images = manifest.medium_upload_assets.filter(
    (asset) => asset.id !== "instructions",
  );
  images.forEach((asset, index) => {
    asset.sha256 = sha256(buffers[index]);
  });
  const html = buffers
    .map(
      (bytes) =>
        `<img src="data:image/png;base64,${bytes.toString("base64")}" alt=""/>`,
    )
    .join("");
  return { buffers, manifest, html };
}

test("embedded image extraction preserves Medium preview order and bytes", () => {
  const fixture = mediumPreviewFixture();
  const images = extractEmbeddedDataImages(fixture.html);
  assert.equal(images.length, 10);
  images.forEach((image, index) => {
    assert.equal(image.mimeType, "image/png");
    assert.ok(image.bytes.equals(fixture.buffers[index]));
  });
  assert.doesNotThrow(() =>
    assertMediumPreviewImageManifest(fixture.html, fixture.manifest),
  );
});

test("Medium preview image mismatch against the upload manifest is rejected", () => {
  const fixture = mediumPreviewFixture();
  fixture.manifest.medium_upload_assets[3].sha256 = "f".repeat(64);
  assert.throws(
    () => assertMediumPreviewImageManifest(fixture.html, fixture.manifest),
    /does not match/,
  );
});
'''
if "embedded image extraction preserves Medium preview order and bytes" in verifier_test:
    raise RuntimeError("Medium preview identity tests already exist")
verifier_test = verifier_test.rstrip() + append_tests + "\n"
write(verifier_test_path, verifier_test)


# 5. Protect stable publication invariants without freezing private function names or test titles.
contract_path = ".github/policy/repository-contract-change-coupling.json"
contract = json.loads(read(contract_path))
required_paths = contract["required_paths"]
required_index = {item["path"] for item in required_paths}
for path in [
    "quartz/scripts/render-publication-assets.mjs",
    "quartz/scripts/publication-assets.test.mjs",
    "quartz/scripts/platform-rendition.test.mjs",
    "quartz/scripts/platform-furniture.test.mjs",
    "quartz/scripts/copy-ready.test.mjs",
    "quartz/scripts/render-copy-ready.test.mjs",
    "quartz/scripts/protect-platform-heading-links.test.mjs",
    "quartz/scripts/verify-publication-package.test.mjs",
]:
    if path not in required_index:
        required_paths.append({"path": path, "type": "file"})
        required_index.add(path)

remove_critical = {
    "quartz/scripts/publication-assets.test.mjs",
    "quartz/scripts/platform-rendition.test.mjs",
    "quartz/scripts/platform-furniture.test.mjs",
    "quartz/scripts/copy-ready.test.mjs",
    "quartz/scripts/render-copy-ready.test.mjs",
    "quartz/scripts/protect-platform-heading-links.test.mjs",
    "quartz/scripts/verify-publication-package.test.mjs",
    "quartz/scripts/render-publication-assets.mjs",
}
contract["critical_files"] = [
    rule for rule in contract["critical_files"] if rule["path"] not in remove_critical
]
critical = {rule["path"]: rule for rule in contract["critical_files"]}

critical["quartz/scripts/render-platform-renditions.mjs"]["required_text"] = [
    'publication_state: "candidate"',
    "publication_ready: false",
    'launch_post_article_url_binding: "required-placeholder"',
    "figure_8_panels_must_travel_together: true",
    '"platform-renditions.manifest.json"',
]
critical["quartz/scripts/render-copy-ready.mjs"]["required_text"] = [
    'clipboard_behavior: "manual-select-all-copy"',
    "javascript_copy_controls: false",
    'linkedin_image_strategy: "embedded-data-uri"',
    'medium_image_strategy: "embedded-data-uri-preview"',
    "medium_clipboard_images_supported: false",
    "medium_manual_upload_required: true",
    'medium_upload_kit: "medium/upload/README.md"',
]
critical["quartz/scripts/protect-platform-heading-links.mjs"]["required_text"] = [
    'mechanism: "visible-source-line-after-linked-heading"',
    'parser: "remark-ast"',
    "body_links_duplicated: false",
    "deterministic_multiple_links: true",
]
critical["quartz/scripts/verify-publication-package.mjs"]["required_text"] = [
    'platformManifest.publication_state === "candidate"',
    "platformManifest.publication_ready === false",
    "manifest.copy_ready?.medium_clipboard_images_supported === false",
    "manifest.copy_ready?.medium_manual_upload_required === true",
    "platformManifest.figure_8_panels_must_travel_together === true",
    'checklist.includes("upload/README.md")',
]
critical["quartz/publication/thinking-systems.platforms.json"]["required_text"] = [
    '"post_max_characters": 3000',
    '"article_max_characters": 125000',
    '"width": 2000',
    '"image_min_width": 1192',
    "one or more Consequential Runtime Responsibilities depend partly on probabilistic Model Judgment",
    "Maximiliano Armesto",
    "Jan Rosen",
]
critical["content/research/notes/thinking-systems-linkedin-launch-post.md"]["required_text"] = [
    "important ideas often do not appear as isolated flashes of genius",
    "following his From Fall to Rise post",
    "a Thinking System is a software system in which one or more Consequential Runtime Responsibilities depend partly on probabilistic Model Judgment",
    "{{LINKEDIN_ARTICLE_URL}}",
]

write(contract_path, json.dumps(contract, indent=2, ensure_ascii=False) + "\n")


# 6. Record the correction in the repository change log.
changelog_path = "CHANGELOG.md"
changelog = read(changelog_path)
entry = (
    "- Corrected the platform publication contract so public category wording matches the "
    "article definition, the Medium checklist exposes one ordered manual-upload path, and "
    "final verification proves that the ten self-contained Medium preview images are "
    "byte-identical to the ten upload-kit PNGs; repository-contract protection now focuses "
    "on stable publication invariants rather than private function names or test titles."
)
if entry not in changelog:
    changelog = replace_once(
        changelog,
        "### Fixed\n",
        f"### Fixed\n\n{entry}\n",
        "CHANGELOG Fixed section",
    )
write(changelog_path, changelog)

print("PR #93 substantive review fixes applied successfully")
