#!/usr/bin/env node
// Exercise the emitted page through HTTP, including subpath hosting and failure UI.
import assert from "node:assert/strict"
import { createServer } from "node:http"
import fs from "node:fs/promises"
import path from "node:path"
import os from "node:os"
import handler from "serve-handler"
import { chromium } from "playwright"

const output = path.resolve(process.argv[2] || "public")
// Check emitted addresses, not just configuration: a successful Pages upload
// can still publish feeds and a 404 page that point outside the project site.
const canonicalBase = new URL(
  "https://uncertaintyarchitecturegroup.github.io/uncertainty-architecture/",
)
for (const [file, pattern] of [
  ["sitemap.xml", /<loc>(.*?)<\/loc>/g],
  ["index.xml", /<(?:link|guid)>(.*?)<\/(?:link|guid)>/g],
]) {
  const entries = [...(await fs.readFile(path.join(output, file), "utf8")).matchAll(pattern)]
  assert.ok(entries.length > 0, `${file} must contain published URLs`)
  for (const [, value] of entries) {
    const url = new URL(value)
    assert.equal(url.origin, canonicalBase.origin, `${file}: ${value}`)
    assert.ok(
      url.pathname === canonicalBase.pathname.slice(0, -1) ||
        url.pathname.startsWith(canonicalBase.pathname),
      `${file}: ${value} must stay under the project path`,
    )
  }
}
const evidence =
  process.env.UA_MAP_REVIEW_DIR || (await fs.mkdtemp(path.join(os.tmpdir(), "ua-map-browser-")))
await fs.mkdir(evidence, { recursive: true })
const server = createServer((request, response) => {
  // GitHub project Pages serves under a repository prefix.
  request.url = request.url.replace(/^\/uncertainty-architecture/, "") || "/"
  void handler(request, response, { public: output })
})
await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve))
const base = `http://127.0.0.1:${server.address().port}/uncertainty-architecture/`
const browser = await chromium.launch({
  headless: true,
  executablePath: process.env.UA_MAP_CHROMIUM_EXECUTABLE,
})
try {
  for (const [name, viewport, touch] of [
    ["desktop", { width: 1440, height: 1050 }, false],
    ["tablet", { width: 1024, height: 1366 }, true],
    ["phone", { width: 390, height: 844 }, true],
  ]) {
    const context = await browser.newContext({
      viewport,
      hasTouch: touch,
      reducedMotion: "reduce",
    })
    const page = await context.newPage()
    const errors = []
    page.on("pageerror", (error) => errors.push(error.message))
    if (name === "desktop") {
      await page.goto(base)
      await page.getByRole("link", { name: "Repository Control Map" }).click()
      await page.waitForURL(/\/control-map(?:\/|$)/)
    } else await page.goto(base + "control-map/")
    await page.waitForSelector('body[data-map-ready="true"]')
    assert.match(await page.locator("#source-state").innerText(), /snapshot|preview/)
    assert.ok((await page.locator("#graph canvas").count()) > 0)
    assert.equal(
      await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1),
      true,
    )
    await page.screenshot({
      path: path.join(evidence, `${name}.png`),
      fullPage: true,
    })
    // Simulate persisted lifecycle events explicitly: the headless browser is
    // not evidence that a real Safari/iPad back-forward cache was exercised.
    const canvasCount = await page.locator("#graph canvas").count()
    const originalCount = await page.locator("#visible-count").innerText()
    for (let cycle = 0; cycle < 2; cycle++) {
      await page.evaluate(() => {
        window.dispatchEvent(new PageTransitionEvent("pagehide", { persisted: true }))
        window.dispatchEvent(new PageTransitionEvent("pageshow", { persisted: true }))
      })
      assert.equal(await page.locator("#graph canvas").count(), canvasCount)
      assert.equal(await page.locator("#visible-count").innerText(), originalCount)
    }
    await page.locator("#map-controls details summary").click()
    for (const [id, value] of [
      ["family", "Responsibility"],
      ["module", "patterns"],
      ["boundary", "research"],
    ]) {
      await page.locator(`#${id}`).selectOption(value)
      assert.ok((await page.locator("#visible-records button").count()) > 0, `Local ${id}=${value}`)
      await page.locator("#reset-filters").click()
    }
    await page.locator("#map-controls details summary").click()
    for (const lens of ["architecture", "impact", "diagnostics", "explore"]) {
      const mode = page.locator(`[data-lens="${lens}"]`)
      if (touch) await mode.tap()
      else await mode.click()
      assert.equal(await page.locator(`[data-lens="${lens}"]`).getAttribute("aria-pressed"), "true")
    }
    await page.locator("#search").fill("quartz/PDF-EXPORT.md")
    await page.locator("#search-results button").first().focus()
    await page.keyboard.press("Enter")
    assert.match(await page.locator("#inspector h2").innerText(), /PDF/i)
    const source = await page.locator("#inspector .source-link").first().getAttribute("href")
    assert.match(
      source,
      /^https:\/\/github.com\/UncertaintyArchitectureGroup\/uncertainty-architecture\/blob\//,
    )
    await page.locator("#global").check()
    await page.locator("#map-controls details summary").click()
    await page.locator("#family").selectOption("Responsibility")
    assert.match(await page.locator("#visible-count").innerText(), /0 links/)
    await page.locator("#reset-filters").click()
    await page.locator("#controls").check()
    await page.locator("#record-list summary").click()
    assert.ok((await page.locator("#visible-records button").count()) > 20)
    await page.locator("#visible-edges button").first().click()
    assert.match(await page.locator("#inspector").innerText(), /Impact direction/)
    assert.deepEqual(errors, [])
    await page.evaluate(() =>
      window.dispatchEvent(new PageTransitionEvent("pagehide", { persisted: false })),
    )
    assert.equal(
      await page.locator("#graph canvas").count(),
      0,
      "Final departure still destroys the renderer after cached restores",
    )
    await context.close()
  }
  const notFound = await browser.newPage()
  await notFound.goto(base + "404.html")
  const resources = await notFound
    .locator('link[rel="stylesheet"], link[rel="icon"]')
    .evaluateAll((links) =>
      links.map((link) => link.href).filter((href) => new URL(href).origin === location.origin),
    )
  assert.ok(resources.length >= 2)
  for (const href of resources) {
    assert.ok(new URL(href).pathname.startsWith(new URL(base).pathname), `404 resource: ${href}`)
    assert.equal((await notFound.request.get(href)).status(), 200)
  }
  const home = await notFound.locator("article a").getAttribute("href")
  assert.equal(
    new URL(home, base).pathname.replace(/\/$/, ""),
    new URL(base).pathname.replace(/\/$/, ""),
  )
  await notFound.close()
  for (const [name, status, body] of [
    ["missing", 404, ""],
    ["malformed", 200, '{"map_version":99}'],
  ]) {
    const page = await browser.newPage()
    await page.route("**/control-map/map.json", (route) =>
      route.fulfill({ status, body, contentType: "application/json" }),
    )
    await page.goto(base + "control-map/")
    await page.waitForSelector("#load-error:not([hidden])")
    assert.equal(await page.locator("#source-state").innerText(), "Map unavailable", name)
    assert.ok(await page.locator("#load-error a").getAttribute("href"))
    await page.close()
  }
  const data = JSON.parse(await fs.readFile(path.join(output, "control-map/map.json"), "utf8"))
  const hostile = '<img src=x onerror="window.injected=true">'
  data.projection.graph.nodes.find(
    (n) => n.id === "document:00-doctrine/control-loop-anatomy.md",
  ).title = hostile
  const page = await browser.newPage()
  await page.route("**/control-map/map.json", (route) =>
    route.fulfill({
      body: JSON.stringify(data),
      contentType: "application/json",
    }),
  )
  await page.goto(base + "control-map/")
  await page.waitForSelector('body[data-map-ready="true"]')
  assert.equal(await page.locator("#inspector h2").innerText(), hostile)
  assert.equal(await page.evaluate(() => window.injected), undefined)
  await page.close()
  console.log(
    `Control Map browser checks passed: desktop, touch viewports, keyboard, local filters, simulated cached restores, publication URLs, subpath, unavailable data and literal source text. Screenshots: ${evidence}`,
  )
} finally {
  await browser.close()
  await new Promise((resolve) => server.close(resolve))
}
