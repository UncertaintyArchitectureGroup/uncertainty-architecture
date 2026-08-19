import { createHash } from "node:crypto"

export const canonicalFigure8Fingerprint = "0d97647ea773cb2e48c5c4394a634e21dab267abad475905347a9d00bda18047"

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
