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
    await context.close()
  }
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
    `Control Map browser checks passed: desktop, touch viewports, keyboard, subpath, unavailable data and literal source text. Screenshots: ${evidence}`,
  )
} finally {
  await browser.close()
  await new Promise((resolve) => server.close(resolve))
}
