import test from "node:test";
import assert from "node:assert/strict";

import {
  assertMediumPreviewImageManifest,
  assertMediumUploadManifest,
  assertPlatformFigureInventory,
  countDataImages,
  extractEmbeddedDataImages,
} from "./verify-publication-package.mjs";
import { sha256 } from "./publication-rendition.mjs";

test("platform verifier requires nine figures with Figure 8A and 8B coupled", () => {
  const figures = Array.from(
    { length: 7 },
    (_, index) => ({
      number: index + 1,
      panel: null,
    }),
  );
  figures.push(
    { number: 8, panel: "A" },
    { number: 8, panel: "B" },
  );
  assert.doesNotThrow(() =>
    assertPlatformFigureInventory({ figures }),
  );
});

test("platform verifier rejects incomplete Figure 8 coupling", () => {
  const figures = Array.from(
    { length: 8 },
    (_, index) => ({
      number: index + 1,
      panel: null,
    }),
  );
  figures.push({ number: 8, panel: "A" });
  assert.throws(
    () =>
      assertPlatformFigureInventory({ figures }),
    /Figure 8A and Figure 8B/,
  );
});

test("embedded image counter distinguishes data-URI payloads", () => {
  assert.equal(
    countDataImages(
      '<img src="data:image/png;base64,a"><img src="https://example.com/x.png">',
    ),
    1,
  );
});

function validMediumManifest() {
  const images = Array.from(
    { length: 10 },
    (_, index) => {
      const id =
        index === 0
          ? "hero"
          : index === 8
            ? "08a"
            : index === 9
              ? "08b"
              : `figure-${index}`;
      const filename =
        index === 0
          ? "00-medium-hero.png"
          : index === 8
            ? "08-figure-08a.png"
            : index === 9
              ? "09-figure-08b.png"
              : `${String(index).padStart(
                  2,
                  "0",
                )}-figure.png`;
      return {
        order: index,
        id,
        path: `medium/upload/${filename}`,
        sha256: "a".repeat(64),
      };
    },
  );
  return {
    medium_manual_upload_required: true,
    medium_clipboard_images_supported: false,
    medium_image_strategy:
      "embedded-data-uri-preview",
    medium_upload_asset_count: 10,
    medium_upload_kit:
      "medium/upload/README.md",
    medium_upload_assets: [
      ...images,
      {
        order: 10,
        id: "instructions",
        path: "medium/upload/README.md",
        sha256: "b".repeat(64),
      },
    ],
  };
}

test("Medium upload manifest requires ten ordered images plus instructions", () => {
  assert.doesNotThrow(() =>
    assertMediumUploadManifest(
      validMediumManifest(),
    ),
  );
});

test("Medium upload manifest rejects any claim that clipboard images are supported", () => {
  const manifest = validMediumManifest();
  manifest.medium_clipboard_images_supported = true;
  assert.throws(
    () => assertMediumUploadManifest(manifest),
    /must not be claimed/,
  );
});

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
