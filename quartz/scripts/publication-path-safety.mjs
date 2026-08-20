import { lstat, mkdir, mkdtemp, realpath, rename, rm, stat, writeFile } from "node:fs/promises"
import path from "node:path"

export function isInsidePath(parent, candidate) {
  const relative = path.relative(parent, candidate)
  return (
    relative === "" ||
    (!relative.startsWith(`..${path.sep}`) &&
      relative !== ".." &&
      !path.isAbsolute(relative))
  )
}

async function lstatIfExists(candidate) {
  try {
    return await lstat(candidate)
  } catch (error) {
    if (error?.code === "ENOENT") return null
    throw error
  }
}

async function statIfExists(candidate) {
  try {
    return await stat(candidate)
  } catch (error) {
    if (error?.code === "ENOENT") return null
    throw error
  }
}

async function assertExistingChainHasNoSymlinks(anchor, target) {
  const relative = path.relative(anchor, target)
  if (relative === "") return
  let cursor = anchor
  for (const part of relative.split(path.sep).filter(Boolean)) {
    cursor = path.join(cursor, part)
    const info = await lstatIfExists(cursor)
    if (!info) break
    if (info.isSymbolicLink()) {
      throw new Error(`Output path contains a symbolic-link component: ${cursor}`)
    }
  }
}

export async function assertSafeOutputPath(
  trustedRoot,
  allowedRoot,
  candidate,
  { allowRoot = false, createParent = true } = {},
) {
  const lexicalTrusted = path.resolve(trustedRoot)
  const lexicalAllowed = path.resolve(allowedRoot)
  const lexicalCandidate = path.resolve(candidate)

  if (!isInsidePath(lexicalTrusted, lexicalAllowed)) {
    throw new Error(`Allowed output root must remain inside trusted root ${lexicalTrusted}`)
  }
  if (
    !isInsidePath(lexicalAllowed, lexicalCandidate) ||
    (!allowRoot && lexicalCandidate === lexicalAllowed)
  ) {
    throw new Error(`Output must remain inside ${lexicalAllowed}`)
  }

  const trustedInfo = await lstat(lexicalTrusted)
  if (trustedInfo.isSymbolicLink() || !trustedInfo.isDirectory()) {
    throw new Error(`Trusted output root must be a real directory: ${lexicalTrusted}`)
  }
  const realTrusted = await realpath(lexicalTrusted)

  await assertExistingChainHasNoSymlinks(lexicalTrusted, lexicalAllowed)
  await mkdir(lexicalAllowed, { recursive: true })
  await assertExistingChainHasNoSymlinks(lexicalTrusted, lexicalAllowed)
  const realAllowed = await realpath(lexicalAllowed)
  if (!isInsidePath(realTrusted, realAllowed)) {
    throw new Error(`Allowed output root resolves outside trusted root: ${lexicalAllowed}`)
  }

  await assertExistingChainHasNoSymlinks(lexicalAllowed, lexicalCandidate)
  const parent = path.dirname(lexicalCandidate)
  if (createParent) await mkdir(parent, { recursive: true })
  await assertExistingChainHasNoSymlinks(lexicalAllowed, lexicalCandidate)

  const existingParent = await lstatIfExists(parent)
  if (!existingParent || existingParent.isSymbolicLink() || !existingParent.isDirectory()) {
    throw new Error(`Output parent must be a real directory: ${parent}`)
  }
  const realParent = await realpath(parent)
  if (!isInsidePath(realAllowed, realParent)) {
    throw new Error(`Output parent resolves outside allowed root: ${parent}`)
  }

  const targetInfo = await lstatIfExists(lexicalCandidate)
  if (targetInfo?.isSymbolicLink()) {
    throw new Error(`Output target must not be a symbolic link: ${lexicalCandidate}`)
  }

  return {
    trustedRoot: realTrusted,
    allowedRoot: realAllowed,
    candidate: lexicalCandidate,
  }
}

export async function assertIndependentOutputTarget(candidate, forbiddenPaths = []) {
  const lexicalCandidate = path.resolve(candidate)
  const linkInfo = await lstatIfExists(lexicalCandidate)
  if (linkInfo?.isSymbolicLink()) {
    throw new Error(`Output target must not be a symbolic link: ${lexicalCandidate}`)
  }
  if (linkInfo && !linkInfo.isFile()) {
    throw new Error(`Output target must be a regular file: ${lexicalCandidate}`)
  }
  const candidateInfo = await statIfExists(lexicalCandidate)
  if (!candidateInfo) return

  for (const forbiddenPath of forbiddenPaths) {
    const forbiddenInfo = await statIfExists(path.resolve(forbiddenPath))
    if (
      forbiddenInfo &&
      candidateInfo.dev === forbiddenInfo.dev &&
      candidateInfo.ino === forbiddenInfo.ino
    ) {
      throw new Error(`Output target aliases a protected source: ${lexicalCandidate}`)
    }
  }
}

export async function writeFileAtomically(
  target,
  data,
  {
    trustedRoot,
    allowedRoot,
    forbiddenPaths = [],
    renameImpl = rename,
  },
) {
  await assertSafeOutputPath(trustedRoot, allowedRoot, target)
  await assertIndependentOutputTarget(target, forbiddenPaths)

  const directory = path.dirname(path.resolve(target))
  const stagingDirectory = await mkdtemp(path.join(directory, ".ua-publication-stage-"))
  const stagedPath = path.join(stagingDirectory, path.basename(target))
  try {
    await writeFile(stagedPath, data, { flag: "wx" })
    await renameImpl(stagedPath, target)
  } finally {
    await rm(stagingDirectory, { recursive: true, force: true })
  }
}
