import test from "node:test";
import assert from "node:assert/strict";

import {
  assertMediumUploadManifest,
  assertPlatformFigureInventory,
  countDataImages,
} from "./verify-publication-package.mjs";

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
