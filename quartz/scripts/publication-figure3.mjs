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
  "Primarily explicitly authored consequential behavior",
  "Thinking System — changed responsibility structure",
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
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 500" style="width:100%;height:auto;max-width:none" role="img" aria-label="Side-by-side comparison of Linear Software and a Thinking System">
<defs>
  <marker id="ua3-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#496574"/></marker>
</defs>
${textBlock(700, 38, ["The controlled-object shift"], { size: 26, weight: 700, fill: "#17242c" })}
${box(24, 65, 660, 385, { fill: "#f7f9f8", stroke: "#b7c2c7", radius: 18 })}
${box(716, 65, 660, 385, { fill: "#f6fafb", stroke: "#9fb5bf", radius: 18 })}
${textBlock(354, 104, ["Linear Software"], { size: 24, weight: 700, fill: "#284b63" })}
${textBlock(1046, 104, ["Thinking System"], { size: 24, weight: 700, fill: "#284b63" })}
${textBlock(354, 132, ["Consequential mapping authored before release"], { size: 16, weight: 600, fill: "#54736d" })}
${textBlock(1046, 132, ["Part of the consequential mapping completed at runtime"], { size: 16, weight: 600, fill: "#54736d" })}

${box(52, 190, 170, 92)}
${textBlock(137, 224, ["Situation and", "operating conditions"], { size: 18, line: 24 })}
${box(255, 178, 205, 116)}
${textBlock(357.5, 213, ["Explicitly authored", "consequential", "responsibilities"], { size: 18, line: 24 })}
${box(493, 190, 163, 92)}
${textBlock(574.5, 218, ["Consequential", "output, action,", "or downstream state"], { size: 17, line: 22 })}
${arrow(222, 236, 255, 236)}
${arrow(460, 236, 493, 236)}
${textBlock(354, 352, ["No Consequential Runtime Responsibility depends partly", "on probabilistic Model Judgment."], { size: 16, line: 22, weight: 600, fill: "#42545f" })}

${box(744, 190, 170, 92)}
${textBlock(829, 224, ["Situation and", "operating conditions"], { size: 18, line: 24 })}
${box(958, 160, 220, 100)}
${textBlock(1068, 193, ["Explicitly authored", "responsibilities before,", "between, and after"], { size: 17, line: 22 })}
${box(958, 270, 220, 132, { fill: "#fce8e8", stroke: "#b43a3a", strokeWidth: 3 })}
${textBlock(1068, 298, ["One or more", "Judgment Nodes", "probabilistic", "Model Judgment"], { size: 16.5, line: 21, weight: 650, fill: "#7b1f1f" })}
${box(1216, 220, 136, 116)}
${textBlock(1284, 250, ["Consequential", "output, action,", "or downstream", "state"], { size: 16.5, line: 21 })}
${curve("M 914 226 C 930 226, 940 210, 958 210")}
${curve("M 914 246 C 930 270, 940 330, 958 338")}
${curve("M 1178 210 C 1195 210, 1202 250, 1216 258")}
${curve("M 1178 338 C 1195 338, 1202 300, 1216 292")}
${textBlock(1046, 414, ["Model Judgment changes the responsibility structure at a bounded node;", "the surrounding system still contains explicitly authored responsibilities."], { size: 15.5, line: 20, weight: 600, fill: "#42545f" })}
</svg>`;
}
