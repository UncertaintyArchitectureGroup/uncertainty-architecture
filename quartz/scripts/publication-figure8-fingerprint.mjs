import { createHash } from "node:crypto"

// Reviewed baseline for the repaired two-panel Figure 8 layout in PR #101.
// Any Mermaid or caption change must pass substantive review before this value moves.
export const canonicalFigure8Fingerprint = "54c622e1404e7ee760934f231bc81f9e9a5ce2dde30a7c85422316ecc138626a"

function normalize(value) {
  return String(value)
    .replaceAll("\r\n", "\n")
    .trim()
    .split("\n")
    .map((line) => line.trimEnd())
    .join("\n")
}

export function figure8Fingerprint(mermaid, caption) {
  return createHash("sha256")
    .update(`${normalize(mermaid)}\n\n${normalize(caption)}`)
    .digest("hex")
}

export function assertCanonicalFigure8Fingerprint(mermaid, caption) {
  const actual = figure8Fingerprint(mermaid, caption)
  if (actual !== canonicalFigure8Fingerprint) {
    throw new Error(
      `Canonical Figure 8 changed; publication Figure 8A/8B requires substantive review. Expected fingerprint ${canonicalFigure8Fingerprint}, received ${actual}.`,
    )
  }
  return actual
}
