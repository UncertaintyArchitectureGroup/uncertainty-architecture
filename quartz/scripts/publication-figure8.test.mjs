import assert from "node:assert/strict";
import test from "node:test";

import {
  assertFigure8PanelReadability,
  assertFigure8RenditionSemantics,
  buildFigure8RenditionAssets,
  figure8ReadabilityPolicy,
  figure8ReadabilityReport,
} from "./publication-figure8.mjs";
import { canonicalFigure8Fingerprint } from "./publication-figure8-fingerprint.mjs";
import { assertCurrentArticleFigure8Rendition } from "./publication-rendition.mjs";

test("Figure 8 panels meet the PDF hard floor, preferred target, and desktop no-zoom floor", () => {
  const report = assertFigure8PanelReadability({ requirePreferred: true });
  assert.equal(report.hard_floor_pt, 5);
  assert.equal(report.preferred_minimum_pt, 6);
  assert.equal(report.desktop_minimum_px, 12);
  for (const panel of ["A", "B"]) {
    assert.ok(
      report.panels[panel].effective_pdf_label_pt >=
        figure8ReadabilityPolicy.hardFloorPt,
    );
    assert.ok(
      report.panels[panel].effective_pdf_label_pt >=
        figure8ReadabilityPolicy.preferredMinimumPt,
    );
    assert.ok(
      report.panels[panel].effective_desktop_label_px >=
        figure8ReadabilityPolicy.desktopMinimumPx,
    );
    assert.equal(report.panels[panel].pdf_hard_floor_met, true);
    assert.equal(report.panels[panel].pdf_preferred_target_met, true);
    assert.equal(report.panels[panel].desktop_readable, true);
  }
});

test("Figure 8 panel builders retain the reviewed semantic projection", () => {
  const assets = buildFigure8RenditionAssets();
  assert.equal(
    assertFigure8RenditionSemantics(assets.decision.svg, assets.capability.svg),
    true,
  );
  assert.throws(
    () =>
      assertFigure8RenditionSemantics(
        assets.decision.svg.replace(
          "specific Bounded Research Authorization",
          "removed",
        ),
        assets.capability.svg,
      ),
    /semantic projection/,
  );
});

test("current article Figure 8 acceptance requires exact panels, fingerprint, and readability", () => {
  const readability = figure8ReadabilityReport();
  const rendition = {
    figure8Split: true,
    figure8Fingerprint: canonicalFigure8Fingerprint,
    figure8Readability: readability,
    canonicalFigures: [
      { number: 8, panel: null, title: "Two orthogonal models" },
    ],
    renditionFigures: [
      { number: 8, panel: "A", title: "Decision-ownership model" },
      {
        number: 8,
        panel: "B",
        title: "Capability-family axis and orthogonality relationship",
      },
    ],
  };
  assert.doesNotThrow(() => assertCurrentArticleFigure8Rendition(rendition));
  assert.throws(
    () =>
      assertCurrentArticleFigure8Rendition({
        ...rendition,
        figure8Fingerprint: "0".repeat(64),
      }),
    /fingerprint/,
  );
  assert.throws(
    () =>
      assertCurrentArticleFigure8Rendition({
        ...rendition,
        figure8Readability: {
          ...readability,
          panels: {
            ...readability.panels,
            A: {
              ...readability.panels.A,
              effective_pdf_label_pt: 4.99,
              pdf_hard_floor_met: false,
            },
          },
        },
      }),
    /readability acceptance/,
  );
});
