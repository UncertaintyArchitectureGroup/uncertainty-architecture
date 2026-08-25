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
    size = 18,
    weight = 500,
    fill = "#314852",
    anchor = "middle",
    line = 23,
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
  { fill = "#ffffff", stroke = "#6c8795", radius = 12, strokeWidth = 2 } = {},
) {
  return `<rect x="${x}" y="${y}" width="${width}" height="${height}" rx="${radius}" fill="${fill}" stroke="${stroke}" stroke-width="${strokeWidth}"/>`;
}

function arrow(
  x1,
  y1,
  x2,
  y2,
  { color = "#496574", marker = "ua3-arrow" } = {},
) {
  return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="2.4" marker-end="url(#${marker})"/>`;
}

function curve(d, { color = "#496574", marker = "ua3-arrow" } = {}) {
  return `<path d="${d}" fill="none" stroke="${color}" stroke-width="2.4" marker-end="url(#${marker})"/>`;
}

export const figure3SemanticMarkers = Object.freeze([
  "Explicitly Authored Software — consequential mapping authored before release",
  "Motivating runtime-judgment class — part of mapping completed at runtime",
  "Situation and operating conditions",
  "Explicitly authored consequential",
  "Explicitly authored responsibilities",
  "One or more Judgment Nodes",
  "probabilistic Model Judgment",
  "Consequential output, action",
]);

export function assertFigure3SemanticSource(mermaid) {
  const missing = figure3SemanticMarkers.filter(
    (marker) => !mermaid.includes(marker),
  );
  if (missing.length > 0) {
    throw new Error(
      `Canonical Figure 3 changed; publication comparison requires review. Missing semantic markers: ${missing.join(", ")}`,
    );
  }
}

export function buildFigure3ControlledObjectSvg() {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 690" style="width:100%;height:auto;max-width:none" role="img" aria-label="Side-by-side top-down comparison of Explicitly Authored Software and the motivating runtime-judgment class" data-ua-flow="top-down">
<defs>
  <marker id="ua3-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#496574"/></marker>
</defs>
${textBlock(700, 38, ["The controlled-object shift"], { size: 26, weight: 700, fill: "#17242c" })}
${box(24, 62, 660, 570, { fill: "#f7f9f8", stroke: "#b7c2c7", radius: 18 })}
${box(716, 62, 660, 570, { fill: "#f6fafb", stroke: "#9fb5bf", radius: 18 })}
${textBlock(354, 103, ["Explicitly Authored Software"], { size: 24, weight: 700, fill: "#284b63" })}
${textBlock(1046, 103, ["Motivating runtime-judgment class"], { size: 24, weight: 700, fill: "#284b63" })}
${textBlock(354, 132, ["Consequential mapping authored before release"], { size: 16, weight: 600, fill: "#54736d" })}
${textBlock(1046, 132, ["Part of the consequential mapping completed at runtime"], { size: 16, weight: 600, fill: "#54736d" })}

${box(150, 165, 408, 72)}
${textBlock(354, 193, ["Situation and", "operating conditions"], { size: 18, line: 23 })}
${arrow(354, 237, 354, 260)}
${box(150, 260, 408, 94)}
${textBlock(354, 289, ["Explicitly authored", "consequential responsibilities"], { size: 18, line: 24 })}
${arrow(354, 354, 354, 378)}
${box(150, 378, 408, 92)}
${textBlock(354, 407, ["Consequential output, action,", "or downstream state"], { size: 18, line: 24 })}
${textBlock(354, 515, ["No Consequential Runtime Responsibility depends partly", "on probabilistic Model Judgment."], { size: 16, line: 22, weight: 600, fill: "#42545f" })}

${box(835, 150, 422, 60)}
${textBlock(1046, 176, ["Situation and operating conditions"], { size: 17.5 })}
${arrow(1046, 210, 1046, 227)}
${box(835, 227, 422, 72)}
${textBlock(1046, 253, ["Explicitly authored responsibilities", "before / between Judgment Nodes"], { size: 17, line: 22 })}
${arrow(1046, 299, 1046, 316)}
${box(850, 316, 392, 88, { fill: "#fce8e8", stroke: "#b43a3a", strokeWidth: 3 })}
${textBlock(1046, 342, ["One or more Judgment Nodes", "probabilistic Model Judgment"], { size: 17, line: 23, weight: 650, fill: "#7b1f1f" })}
${arrow(1046, 404, 1046, 421)}
${box(835, 421, 422, 64)}
${textBlock(1046, 447, ["Explicitly authored responsibilities", "after Judgment Nodes"], { size: 17, line: 22 })}
${arrow(1046, 485, 1046, 502)}
${box(835, 502, 422, 72)}
${textBlock(1046, 529, ["Consequential output, action,", "or downstream state"], { size: 17, line: 22 })}
${textBlock(1046, 604, ["Model Judgment leaves part of a consequential responsibility unresolved until operation;", "the surrounding system still contains explicitly authored responsibilities."], { size: 15.5, line: 20, weight: 600, fill: "#42545f" })}
</svg>`;
}
