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
  { dashed = false, color = "#46616f", marker = "ua8a-arrow" } = {},
) {
  return `<path d="${d}" fill="none" stroke="${color}" stroke-width="2.2"${dashed ? ' stroke-dasharray="8 7"' : ""} marker-end="url(#${marker})"/>`;
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
    "Capability functions — how control becomes operational",
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
  const lifelines = [170, 500, 850, 1180]
    .map(
      (x) =>
        `<line x1="${x}" y1="145" x2="${x}" y2="860" stroke="#c7d1d6" stroke-width="1.5" stroke-dasharray="6 8"/>`,
    )
    .join("");

  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 920" style="width:100%;height:auto;max-width:none">
<defs><marker id="ua8a-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#46616f"/></marker></defs>
${textBlock(700, 38, ["Decision ownership — where the decision belongs"], { size: 24, weight: 700, fill: "#17242c" })}
${box(35, 62, 270, 84)}${textBlock(170, 93, ["Organization"], { size: 21, weight: 700, fill: "#17242c" })}${textBlock(170, 120, ["business · authority", "reserved decisions"], { size: 12.8, line: 16, fill: "#42545f" })}
${box(365, 62, 270, 84)}${textBlock(500, 93, ["Project / Architecture"], { size: 21, weight: 700, fill: "#17242c" })}${textBlock(500, 120, ["technical selection · viability", "control design"], { size: 12.8, line: 16, fill: "#42545f" })}
${box(715, 62, 270, 84)}${textBlock(850, 93, ["Delivery"], { size: 21, weight: 700, fill: "#17242c" })}${textBlock(850, 120, ["realization · evidence · release"], { size: 12.8, fill: "#42545f" })}
${box(1045, 62, 270, 84)}${textBlock(1180, 93, ["Runtime"], { size: 21, weight: 700, fill: "#17242c" })}${textBlock(1180, 120, ["operation · correction", "reassessment evidence"], { size: 12.8, line: 16, fill: "#42545f" })}
${lifelines}
${arrow(170, 210, 500, 210)}${textBlock(335, 184, ["initial admissibility + assessment eligibility", "authoritative / business basis"], { size: 14.5, line: 18, weight: 550 })}
${box(390, 255, 220, 90, { fill: "#f7fafb", stroke: "#6c8795" })}${textBlock(500, 286, ["Selected design"], { size: 18, weight: 700, fill: "#17242c" })}${textBlock(500, 313, ["still a Thinking System?"], { size: 15, fill: "#42545f" })}
${box(690, 255, 300, 90, { fill: "#fafafa", stroke: "#87959c" })}${textBlock(840, 286, ["No → category exit"], { size: 18, weight: 700, fill: "#17242c" })}${textBlock(840, 313, ["Thinking-System-specific lifecycle ends", "ordinary product/software governance continues"], { size: 13.5, line: 19, fill: "#42545f" })}
${arrow(610, 300, 690, 300)}${textBlock(650, 286, ["No"], { size: 14, weight: 550 })}
${curve("M 500 345 C 455 372, 455 392, 500 408")}${textBlock(400, 370, ["Yes → continue", "Project analysis"], { size: 13.8, line: 18, weight: 550 })}
${arrow(500, 438, 170, 438)}${textBlock(335, 411, ["reserved-boundary research request / viable production basis", "or changed Organizational premise / continuation decision"], { size: 13.7, line: 18, weight: 550 })}
${arrow(170, 510, 500, 510)}${textBlock(335, 484, ["specific Bounded Research Authorization", "Business Authorization or changed basis"], { size: 14.2, line: 18, weight: 550 })}
${arrow(500, 585, 850, 585)}${textBlock(675, 558, ["applicable Project Authorization scope / set", "research-only and/or production-capable where applicable"], { size: 13.7, line: 18, weight: 550 })}
${arrow(850, 655, 1180, 655)}${textBlock(1015, 630, ["approved realization", "+ authorized exposure"], { size: 14.5, line: 18, weight: 550 })}
${box(865, 725, 300, 105, { fill: "#f8fbfc", stroke: "#597887" })}${textBlock(1015, 756, ["Reassessment evidence"], { size: 18, weight: 700, fill: "#17242c" })}${textBlock(1015, 783, ["realization / experiment evidence", "operation evidence that challenges a decision basis"], { size: 13.5, line: 19, fill: "#42545f" })}
${curve("M 850 680 C 860 705, 895 710, 930 725", { dashed: true })}${textBlock(850, 710, ["Delivery"], { size: 13, weight: 550 })}
${curve("M 1180 680 C 1170 705, 1135 710, 1100 725")}${textBlock(1190, 710, ["Runtime"], { size: 13, weight: 550 })}
${curve("M 925 830 C 870 865, 830 850, 850 705", { dashed: true })}${textBlock(770, 842, ["implementation / realization", "/ evidence issue → Delivery"], { size: 13.3, line: 18, weight: 550 })}
${curve("M 1000 830 C 720 900, 520 875, 500 690", { dashed: true })}${textBlock(630, 888, ["risk / feasibility / Model Judgment necessity", "capacity / economics invalidated or research answered → Project"], { size: 13.1, line: 18, weight: 550 })}
${box(25, 710, 275, 94, { fill: "#fffaf2", stroke: "#b7853c" })}${textBlock(162.5, 741, ["Exogenous Organizational change"], { size: 16.5, weight: 700, fill: "#17242c" })}${textBlock(162.5, 768, ["authoritative or business basis", "activates Organization directly"], { size: 13.2, line: 19, fill: "#42545f" })}
${curve("M 165 710 C 55 610, 65 250, 160 150", { color: "#a9742d" })}${textBlock(86, 590, ["independent", "Organizational input"], { size: 13, line: 18, weight: 550, fill: "#8c622a" })}
</svg>`;
}

function capabilityBox(y, title, subtitle) {
  return `${box(210, y, 650, 105, { fill: "#e8f5e9", stroke: "#2e7d32" })}${textBlock(535, y + 34, [title], { size: 22, weight: 700, fill: "#1b5e20" })}${textBlock(535, y + 65, [subtitle], { size: 17, fill: "#2d5d39" })}`;
}

export function buildFigure8CapabilitySvg() {
  const railYs = [158, 313, 468, 623];
  const rail = `<line x1="120" y1="158" x2="120" y2="623" stroke="#7f949d" stroke-width="2"/>${railYs.map((y) => `<circle cx="120" cy="${y}" r="7" fill="#ffffff" stroke="#597887" stroke-width="2"/><line x1="127" y1="${y}" x2="195" y2="${y}" stroke="#7f949d" stroke-width="2"/>`).join("")}`;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 870" style="width:100%;height:auto;max-width:none">
${textBlock(500, 45, ["Capability functions — how control becomes operational"], { size: 25, weight: 700, fill: "#1d4327" })}
${rail}
${capabilityBox(105, "Actuators and corrective action", "execute authorized change")}
${capabilityBox(260, "Constraints and realizations", "define and operationalize boundaries")}
${capabilityBox(415, "Sensors and evidence", "observe behavior, conditions, and control state")}
${capabilityBox(570, "Controllers / decision functions", "interpret evidence and select bounded response")}
${textBlock(500, 750, ["All four capability families may appear at every decision horizon."], { size: 20, weight: 700, fill: "#1b5e20" })}
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
