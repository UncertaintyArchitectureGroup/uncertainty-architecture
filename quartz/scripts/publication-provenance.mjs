import { spawn } from "node:child_process"
import path from "node:path"
import { fileURLToPath } from "node:url"

export const repoRoot = path.resolve(fileURLToPath(new URL("../..", import.meta.url)))

export function gitOutput(args) {
  return new Promise((resolve, reject) => {
    const child = spawn("git", args, {
      cwd: repoRoot,
      stdio: ["ignore", "pipe", "pipe"],
    })
    let stdout = ""
    let stderr = ""
    child.stdout.on("data", (chunk) => (stdout += chunk))
    child.stderr.on("data", (chunk) => (stderr += chunk))
    child.once("error", reject)
    child.once("exit", (code) => {
      if (code === 0) return resolve(stdout.trim())
      reject(new Error(`git ${args.join(" ")} failed: ${stderr.trim()}`))
    })
  })
}

export async function resolveSourceCommit(sourceReference) {
  const reference = String(sourceReference ?? "").trim()
  if (!reference) throw new Error("A declared source ref is required")

  let resolved
  try {
    resolved = await gitOutput([
      "rev-parse",
      "--verify",
      "--end-of-options",
      `${reference}^{commit}`,
    ])
  } catch (error) {
    throw new Error(
      `Unable to resolve declared source ref ${reference}: ${error.message}`,
    )
  }

  if (!/^[0-9a-f]{40}$/i.test(resolved)) {
    throw new Error(
      `Declared source ref ${reference} did not resolve to a full Git commit SHA`,
    )
  }
  return resolved.toLowerCase()
}

export async function determineSourceProvenance(
  source,
  sourceReference,
  { allowDirtyPreview = false } = {},
) {
  const sourceCommit = await resolveSourceCommit(sourceReference)
  const workingBlob = await gitOutput(["hash-object", source.absolute])
  let committedBlob = null
  try {
    committedBlob = await gitOutput(["rev-parse", `${sourceCommit}:${source.relative}`])
  } catch {
    if (!allowDirtyPreview) {
      throw new Error(
        `Publication source is not present at declared source commit ${sourceCommit}: ${source.relative}. Commit the source or use --allow-dirty-preview for a non-versioned local preview.`,
      )
    }
  }

  const dirty = committedBlob !== workingBlob
  if (dirty && !allowDirtyPreview) {
    throw new Error(
      `Publication source bytes do not match declared source commit ${sourceCommit}: ${source.relative}. Commit the source before producing a versioned publication, or use --allow-dirty-preview for an explicitly dirty local preview.`,
    )
  }

  return {
    state: dirty ? "dirty-preview" : "committed",
    workingBlob,
    committedBlob,
    sourceCommit,
  }
}
