function escapeXml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function textBlock(
  x,
  y,
  lines,
  {
    size = 14,
    weight = 500,
    fill = "#314852",
    anchor = "middle",
    line = 18,
  } = {},
) {
  const tspans = lines
    .map(
      (value, index) =>
        `<tspan x="${x}" dy="${index === 0 ? 0 : line}">${escapeXml(value)}</tspan>`,
    )
    .join("");
  return `<text x="${x}" y="${y}" text-anchor="${anchor}" font-family="Arial, sans-serif" font-size="${size}" font-weight="${weight}" fill="${fill}">${tspans}</text>`;
}

function box(
  x,
  y,
  width,
  height,
  { fill = "#ffffff", stroke = "#496574", radius = 12 } = {},
) {
  return `<rect x="${x}" y="${y}" width="${width}" height="${height}" rx="${radius}" fill="${fill}" stroke="${stroke}" stroke-width="2"/>`;
}

function arrow(
  x1,
  y1,
  x2,
  y2,
  { dashed = false, color = "#46616f", marker = "ua8a-arrow" } = {},
) {
  return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="2.2"${dashed ? ' stroke-dasharray="8 7"' : ""} marker-end="url(#${marker})"/>`;
}

function curve(
  d,
  {
    dashed = false,
    color = "#46616f",
    marker = "ua8a-arrow",
    width = 2.2,
  } = {},
) {
  return `<path d="${d}" fill="none" stroke="${color}" stroke-width="${width}"${dashed ? ' stroke-dasharray="8 7"' : ""} marker-end="url(#${marker})"/>`;
}

const millimetersToPoints = 72 / 25.4;

export const figure8ReadabilityPolicy = Object.freeze({
  hardFloorPt: 5,
  preferredMinimumPt: 6,
  desktopMinimumPx: 12,
  desktopViewportPx: 1440,
});

export const figure8PanelSpecifications = Object.freeze({
  A: Object.freeze({
    panel: "A",
    title: "Decision-ownership model",
    page: "landscape",
    viewBoxWidth: 1400,
    viewBoxHeight: 920,
    minimumLabelUnits: 12.8,
    printWidthMm: 281,
    printHeightMm: 155,
    pngOutputWidthPx: 3200,
  }),
  B: Object.freeze({
    panel: "B",
    title: "Capability-family axis and orthogonality relationship",
    page: "portrait",
    viewBoxWidth: 1000,
    viewBoxHeight: 870,
    minimumLabelUnits: 16,
    printWidthMm: 178,
    printHeightMm: 190,
    pngOutputWidthPx: 2400,
  }),
});

function roundMetric(value) {
  return Number(value.toFixed(2));
}

export function calculateFigure8PdfLabelPoints(specification) {
  const scaleMmPerUnit = Math.min(
    specification.printWidthMm / specification.viewBoxWidth,
    specification.printHeightMm / specification.viewBoxHeight,
  );
  return roundMetric(
    specification.minimumLabelUnits * scaleMmPerUnit * millimetersToPoints,
  );
}

export function calculateFigure8DesktopLabelPixels(
  specification,
  viewportWidthPx = figure8ReadabilityPolicy.desktopViewportPx,
) {
  return roundMetric(
    specification.minimumLabelUnits *
      (viewportWidthPx / specification.viewBoxWidth),
  );
}

export function figure8ReadabilityReport() {
  const panels = Object.fromEntries(
    Object.entries(figure8PanelSpecifications).map(([panel, specification]) => {
      const effectivePdfLabelPt = calculateFigure8PdfLabelPoints(specification);
      const effectiveDesktopLabelPx =
        calculateFigure8DesktopLabelPixels(specification);
      return [
        panel,
        {
          ...specification,
          effective_pdf_label_pt: effectivePdfLabelPt,
          effective_desktop_label_px: effectiveDesktopLabelPx,
          pdf_hard_floor_met:
            effectivePdfLabelPt >= figure8ReadabilityPolicy.hardFloorPt,
          pdf_preferred_target_met:
            effectivePdfLabelPt >= figure8ReadabilityPolicy.preferredMinimumPt,
          desktop_readable:
            effectiveDesktopLabelPx >=
            figure8ReadabilityPolicy.desktopMinimumPx,
        },
      ];
    }),
  );
  return {
    hard_floor_pt: figure8ReadabilityPolicy.hardFloorPt,
    preferred_minimum_pt: figure8ReadabilityPolicy.preferredMinimumPt,
    desktop_minimum_px: figure8ReadabilityPolicy.desktopMinimumPx,
    desktop_viewport_px: figure8ReadabilityPolicy.desktopViewportPx,
    panels,
  };
}

export function assertFigure8PanelReadability({
  requirePreferred = true,
} = {}) {
  const report = figure8ReadabilityReport();
  const failures = [];
  for (const [panel, result] of Object.entries(report.panels)) {
    if (!result.pdf_hard_floor_met) {
      failures.push(
        `Figure 8${panel} effective PDF label size ${result.effective_pdf_label_pt} pt is below the ${report.hard_floor_pt} pt hard floor`,
      );
    }
    if (requirePreferred && !result.pdf_preferred_target_met) {
      failures.push(
        `Figure 8${panel} effective PDF label size ${result.effective_pdf_label_pt} pt misses the ${report.preferred_minimum_pt} pt publication target`,
      );
    }
    if (!result.desktop_readable) {
      failures.push(
        `Figure 8${panel} effective desktop label size ${result.effective_desktop_label_px} px is below the ${report.desktop_minimum_px} px no-zoom floor`,
      );
    }
  }
  if (failures.length > 0) {
    throw new Error(
      `Figure 8 rendition is not publication-readable: ${failures.join("; ")}`,
    );
  }
  return report;
}

export const figure8RenditionSemanticMarkers = Object.freeze({
  A: Object.freeze([
    "Decision ownership — where the decision belongs",
    "Organization",
    "Project / Architecture",
    "Delivery",
    "Runtime",
    "initial admissibility + assessment eligibility",
    "Selected design",
    "still a Thinking System?",
    "specific Bounded Research Authorization",
    "viable production basis",
    "research-only and/or production-capable",
    "Reassessment evidence",
    "Exogenous Organizational change",
  ]),
  B: Object.freeze([
    "Capability functions — one control architecture, not a sequence",
    "Actuators and corrective action",
    "Constraints and realizations",
    "Sensors and evidence",
    "Controllers / decision functions",
    "All four capability families may appear at every decision horizon.",
    "Decision horizons answer where a decision is owned",
    "There is no one-to-one mapping",
    "not an execution pipeline",
  ]),
});

export function assertFigure8RenditionSemantics(decisionSvg, capabilitySvg) {
  const missing = [];
  for (const marker of figure8RenditionSemanticMarkers.A) {
    if (!decisionSvg.includes(marker)) missing.push(`8A: ${marker}`);
  }
  for (const marker of figure8RenditionSemanticMarkers.B) {
    if (!capabilitySvg.includes(marker)) missing.push(`8B: ${marker}`);
  }
  if (missing.length > 0) {
    throw new Error(
      `Figure 8 publication rendition drifted from the reviewed semantic projection. Missing markers: ${missing.join(", ")}`,
    );
  }
  return true;
}

export const figure8SemanticMarkers = [
  "initial admissibility + assessment eligibility",
  "specific Bounded Research Authorization",
  "Selected technical design",
  "still a Thinking System?",
  "Exit Thinking-System-specific lifecycle",
  "viable production basis",
  "research-only and/or production-capable",
  "Delivery / Runtime reassessment evidence",
  "Exogenous Organizational change",
  "all four capability families may appear at every decision horizon",
];

export function assertFigure8SemanticSource(mermaid) {
  const missing = figure8SemanticMarkers.filter(
    (marker) => !mermaid.includes(marker),
  );
  if (missing.length > 0) {
    throw new Error(
      `Canonical Figure 8 changed; publication rendition requires review. Missing semantic markers: ${missing.join(", ")}`,
    );
  }
}

export function buildFigure8DecisionSvg() {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 920" style="width:100%;height:auto;max-width:none" role="img" aria-label="Decision ownership and reassessment across Organization, Project, Delivery, and Runtime">
<defs><marker id="ua8a-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#46616f"/></marker></defs>
${textBlock(700, 38, ["Decision ownership — where the decision belongs"], { size: 25, weight: 700, fill: "#17242c" })}

${box(28, 58, 1344, 322, { fill: "#f7fafb", stroke: "#c7d3d8", radius: 18 })}
${textBlock(55, 88, ["NORMAL AUTHORIZATION PATH"], { size: 13, weight: 700, fill: "#54736d", anchor: "start" })}
${box(52, 105, 280, 76, { fill: "#ffffff", stroke: "#496574" })}${textBlock(192, 134, ["Organization"], { size: 21, weight: 700, fill: "#17242c" })}${textBlock(192, 160, ["business · authority · reserved decisions"], { size: 12.8, fill: "#42545f" })}
${box(382, 105, 280, 76, { fill: "#ffffff", stroke: "#496574" })}${textBlock(522, 134, ["Project / Architecture"], { size: 21, weight: 700, fill: "#17242c" })}${textBlock(522, 160, ["technical selection · viability · control design"], { size: 12.8, fill: "#42545f" })}
${box(712, 105, 280, 76, { fill: "#ffffff", stroke: "#496574" })}${textBlock(852, 134, ["Delivery"], { size: 21, weight: 700, fill: "#17242c" })}${textBlock(852, 160, ["realization · evidence · release"], { size: 12.8, fill: "#42545f" })}
${box(1042, 105, 280, 76, { fill: "#ffffff", stroke: "#496574" })}${textBlock(1182, 134, ["Runtime"], { size: 21, weight: 700, fill: "#17242c" })}${textBlock(1182, 160, ["operation · correction · evidence"], { size: 12.8, fill: "#42545f" })}

${box(52, 220, 280, 96, { fill: "#ffffff", stroke: "#6c8795" })}${textBlock(192, 251, ["Standing Organizational basis"], { size: 17.5, weight: 700, fill: "#17242c" })}${textBlock(192, 278, ["initial admissibility + assessment eligibility", "authoritative / business basis"], { size: 13.5, line: 18, fill: "#42545f" })}
${box(382, 210, 280, 116, { fill: "#ffffff", stroke: "#6c8795" })}${textBlock(522, 244, ["Selected design"], { size: 18.5, weight: 700, fill: "#17242c" })}${textBlock(522, 272, ["technical design selected", "still a Thinking System?"], { size: 14.3, line: 19, fill: "#42545f" })}
${box(712, 220, 280, 96, { fill: "#ffffff", stroke: "#6c8795" })}${textBlock(852, 251, ["Bounded realization"], { size: 17.5, weight: 700, fill: "#17242c" })}${textBlock(852, 278, ["complete evidence and release", "inside Project Authorization"], { size: 13.5, line: 18, fill: "#42545f" })}
${box(1042, 220, 280, 96, { fill: "#ffffff", stroke: "#6c8795" })}${textBlock(1182, 251, ["Authorized operation"], { size: 17.5, weight: 700, fill: "#17242c" })}${textBlock(1182, 278, ["approved realization", "+ authorized exposure"], { size: 13.5, line: 18, fill: "#42545f" })}
${arrow(332, 268, 382, 268)}
${arrow(662, 268, 712, 268)}
${arrow(992, 268, 1042, 268)}
${textBlock(687, 191, ["Yes — continue", "applicable Project Authorization scope / set"], { size: 13.1, line: 18, weight: 600, fill: "#42545f" })}
${arrow(522, 326, 522, 334)}
${box(392, 334, 260, 46, { fill: "#f2f4f5", stroke: "#87959c", radius: 8 })}${textBlock(522, 350, ["No — category exit", "Exit Thinking-System-specific lifecycle"], { size: 12.8, line: 17, weight: 650, fill: "#42545f" })}

${box(28, 398, 1344, 248, { fill: "#fffaf2", stroke: "#dfc79e", radius: 18 })}
${textBlock(55, 428, ["RESERVED OR CHANGED BASIS PATH — ONLY WHEN THE STANDING BASIS IS NOT ENOUGH"], { size: 13, weight: 700, fill: "#8c622a", anchor: "start" })}
${box(58, 466, 360, 132, { fill: "#ffffff", stroke: "#b7853c" })}${textBlock(238, 497, ["Project / Architecture finding"], { size: 17.5, weight: 700, fill: "#17242c" })}${textBlock(238, 526, ["reserved-boundary research request / viable production basis", "or changed Organizational premise / continuation decision"], { size: 13.1, line: 19, fill: "#42545f" })}
${box(520, 466, 360, 132, { fill: "#ffffff", stroke: "#b7853c" })}${textBlock(700, 497, ["Organization decision"], { size: 17.5, weight: 700, fill: "#17242c" })}${textBlock(700, 526, ["specific Bounded Research Authorization", "Business Authorization or changed basis"], { size: 13.8, line: 20, fill: "#42545f" })}
${box(982, 466, 360, 132, { fill: "#ffffff", stroke: "#b7853c" })}${textBlock(1162, 497, ["Project / Architecture output"], { size: 17.5, weight: 700, fill: "#17242c" })}${textBlock(1162, 526, ["scoped Project Authorization", "research-only and/or production-capable where applicable"], { size: 13.2, line: 20, fill: "#42545f" })}
${arrow(418, 532, 520, 532, { color: "#a9742d" })}
${arrow(880, 532, 982, 532, { color: "#a9742d" })}
${textBlock(469, 512, ["request"], { size: 13, weight: 650, fill: "#8c622a" })}
${textBlock(931, 512, ["changed basis"], { size: 13, weight: 650, fill: "#8c622a" })}

${box(28, 664, 1344, 224, { fill: "#f8fbfc", stroke: "#c7d3d8", radius: 18 })}
${textBlock(55, 694, ["REASSESSMENT — EVIDENCE RETURNS TO THE OWNER OF THE DECISION BASIS IT CHALLENGES"], { size: 13, weight: 700, fill: "#54736d", anchor: "start" })}
${box(52, 728, 280, 118, { fill: "#fffaf2", stroke: "#b7853c" })}${textBlock(192, 760, ["Exogenous Organizational change"], { size: 16.2, weight: 700, fill: "#17242c" })}${textBlock(192, 790, ["authoritative or business basis", "activates Organization directly"], { size: 13.2, line: 19, fill: "#42545f" })}
${box(382, 718, 300, 138, { fill: "#ffffff", stroke: "#6c8795" })}${textBlock(532, 749, ["Project reassessment"], { size: 17.2, weight: 700, fill: "#17242c" })}${textBlock(532, 777, ["risk / feasibility / Model Judgment necessity", "capacity / economics invalidated", "or research answered"], { size: 13.1, line: 18, fill: "#42545f" })}
${box(732, 728, 250, 118, { fill: "#ffffff", stroke: "#6c8795" })}${textBlock(857, 760, ["Delivery reassessment"], { size: 17.2, weight: 700, fill: "#17242c" })}${textBlock(857, 790, ["implementation / realization", "/ evidence issue"], { size: 13.4, line: 19, fill: "#42545f" })}
${box(1032, 718, 290, 138, { fill: "#ffffff", stroke: "#597887" })}${textBlock(1177, 749, ["Reassessment evidence"], { size: 17.2, weight: 700, fill: "#17242c" })}${textBlock(1177, 777, ["Delivery / Runtime reassessment evidence", "realization / experiment evidence", "or operation evidence"], { size: 13, line: 18, fill: "#42545f" })}
${arrow(1032, 775, 982, 775, { dashed: true, color: "#6f848e" })}
${arrow(1032, 820, 682, 820, { dashed: true, color: "#6f848e" })}
${curve("M 192 728 L 12 700 L 12 248 L 52 248", { color: "#a9742d", width: 3.2 })}
${curve("M 852 316 L 1000 390 L 1000 690 L 1110 718", { dashed: true, color: "#6f848e" })}
${curve("M 1182 316 L 1350 390 L 1350 690 L 1245 718", { dashed: true, color: "#6f848e" })}
${textBlock(700, 906, ["Solid arrows carry authorization forward. Dashed arrows return evidence for reassessment."], { size: 13.2, weight: 650, fill: "#54736d" })}
</svg>`;
}
function capabilityBox(y, title, subtitle) {
  return `${box(175, y, 650, 105, { fill: "#e8f5e9", stroke: "#2e7d32" })}${textBlock(500, y + 34, [title], { size: 22, weight: 700, fill: "#1b5e20" })}${textBlock(500, y + 65, [subtitle], { size: 17, fill: "#2d5d39" })}`;
}

export function buildFigure8CapabilitySvg() {
  const connector = (y1, y2) => `<line x1="500" y1="${y1}" x2="500" y2="${y2}" stroke="#4f8a5b" stroke-width="3"/>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 870" style="width:100%;height:auto;max-width:none">
${textBlock(500, 45, ["Capability functions — one control architecture, not a sequence"], { size: 25, weight: 700, fill: "#1d4327" })}
${capabilityBox(105, "Controllers / decision functions", "interpret evidence and select bounded response")}
${connector(210, 250)}
${capabilityBox(250, "Sensors and evidence", "observe behavior, conditions, and control state")}
${connector(355, 395)}
${capabilityBox(395, "Constraints and realizations", "define and operationalize boundaries")}
${connector(500, 540)}
${capabilityBox(540, "Actuators and corrective action", "execute authorized change")}
${textBlock(500, 710, ["Non-directional lines show one control architecture; they do not encode execution order."], { size: 17, weight: 700, fill: "#1b5e20" })}
${textBlock(500, 750, ["All four capability families may appear at every decision horizon."], { size: 18, weight: 700, fill: "#1b5e20" })}
${textBlock(500, 790, ["Decision horizons answer where a decision is owned; capability families answer how control becomes operational."], { size: 16, fill: "#365f40" })}
${textBlock(500, 825, ["There is no one-to-one mapping. The vertical ordering is a reading aid, not an execution pipeline."], { size: 16, weight: 600, fill: "#365f40" })}
</svg>`;
}

export function buildFigure8RenditionAssets() {
  const decisionSvg = buildFigure8DecisionSvg();
  const capabilitySvg = buildFigure8CapabilitySvg();
  assertFigure8RenditionSemantics(decisionSvg, capabilitySvg);
  const readability = assertFigure8PanelReadability({ requirePreferred: true });
  return {
    decision: {
      ...figure8PanelSpecifications.A,
      svg: decisionSvg,
    },
    capability: {
      ...figure8PanelSpecifications.B,
      svg: capabilitySvg,
    },
    readability,
  };
}
