// Native editable PowerPoint rendition of the maintainer-approved Markdown.
// Content lives in pptx-slide blocks; this module owns geometry, not research claims.
export const slideCount = 14
export const theme = {
  bg: "#0B0F14",
  panel: "#141C26",
  white: "#F4F7FA",
  gray: "#ADB8C5",
  line: "#344454",
  cyan: "#28C7F7",
  amber: "#F5B61C",
  red: "#FF6B75",
  font: "DejaVu Sans",
  width: 1280,
  height: 720,
}

const layouts = [
  "cover",
  "phase",
  "sdlc",
  "evidence",
  "comprehension",
  "recovery",
  "equilibrium",
  "thinking",
  "boundaries",
  "evaluation",
  "risk",
  "control",
  "roles",
  "synthesis",
]

export function parseDeck(markdown) {
  const sections = [
    ...markdown.matchAll(/^## (\d+)\. (.+)\n([\s\S]*?)(?=^## \d+\. |$(?![\s\S]))/gm),
  ]
  if (sections.length !== slideCount) throw new Error("Expected exactly 14 approved slide sections")
  return sections.map((section, i) => {
    const blocks = [...section[3].matchAll(/```pptx-slide\n([\s\S]*?)\n```/g)]
    if (blocks.length !== 1) throw new Error(`Slide ${i + 1}: expected one pptx-slide block`)
    const data = JSON.parse(blocks[0][1])
    if (+section[1] !== i + 1 || data.number !== i + 1 || data.layout !== layouts[i]) {
      throw new Error(`Slide ${i + 1}: approved order/layout changed`)
    }
    if (typeof data.notes !== "string" || !data.notes.trim())
      throw new Error(`Slide ${i + 1}: missing notes`)
    if (data.images)
      throw new Error(
        "Only the fixed cover asset is approved; arbitrary image exceptions are forbidden",
      )
    if (data.titleLines && data.titleLines.join(" ") !== section[2])
      throw new Error(`Slide ${i + 1}: title line breaks changed the approved title`)
    return { ...data, title: section[2] }
  })
}

export function createDeck(Presentation, data, assets = {}) {
  const C = theme
  const deck = Presentation.create({ slideSize: { width: C.width, height: C.height } })
  function text(s, value, x, y, w, h, size = 28, color = C.white, bold = false, align = "left") {
    const shape = s.shapes.add({
      geometry: "textbox",
      position: { left: x, top: y, width: w, height: h },
      fill: "none",
      line: { fill: "none", width: 0 },
    })
    shape.text = value
    shape.text.style = {
      typeface: C.font,
      fontSize: size,
      color,
      bold,
      alignment: align,
      verticalAlignment: "middle",
      autoFit: "none",
      wrap: "square",
      insets: { left: 0, right: 0, top: 0, bottom: 0 },
    }
    return shape
  }
  function rect(s, x, y, w, h, stroke = C.line, fill = C.panel, width = 1.5) {
    return s.shapes.add({
      geometry: "rect",
      position: { left: x, top: y, width: w, height: h },
      fill,
      line: { fill: stroke, width, style: "solid" },
    })
  }
  function line(s, x1, y1, x2, y2, color = C.line, width = 2) {
    return s.shapes.add({
      geometry: "line",
      position: {
        left: Math.min(x1, x2),
        top: Math.min(y1, y2),
        width: Math.abs(x2 - x1),
        height: Math.abs(y2 - y1),
        horizontalFlip: x2 < x1,
        verticalFlip: y2 < y1,
      },
      fill: "none",
      line: { fill: color, width, style: "solid" },
    })
  }
  function box(s, label, x, y, w, h, color = C.line, font = 26) {
    const shape = rect(s, x, y, w, h, color)
    text(s, label, x + 12, y + 8, w - 24, h - 16, font, C.white, true, "center")
    return shape
  }
  function connect(s, a, b, color = C.cyan, from = "right", to = "left", kind = "straight") {
    return s.shapes.connect(a, b, {
      kind,
      fromSide: from,
      toSide: to,
      line: { fill: color, width: 2.3, style: "solid" },
      tail: { type: "triangle", width: "med", length: "med" },
    })
  }
  function takeaway(s, value, color = C.white, size = 28) {
    line(s, 64, 602, 1216, 602)
    text(s, value, 64, 620, 1118, 70, size, color, true)
  }
  function table(s, values, x, y, w, h, widths) {
    const t = s.tables.add({
      rows: values.length,
      columns: values[0].length,
      left: x,
      top: y,
      width: w,
      height: h,
      columnWidths: widths,
      values,
    })
    t.borders.assign({ fill: C.line, width: 1, style: "solid" })
    for (let r = 0; r < values.length; r++) {
      t.rows[r].height = h / values.length
      for (let c = 0; c < values[0].length; c++) {
        const cell = t.getCell(r, c)
        cell.fill = r === 0 ? "#1A2734" : C.bg
        cell.text.style = {
          typeface: C.font,
          fontSize: r === 0 ? 23 : 25,
          color: c === values[0].length - 1 ? C.cyan : C.white,
          bold: r === 0 || c === 0,
          verticalAlignment: "middle",
          autoFit: "none",
          insets: { left: 18, right: 18, top: 12, bottom: 12 },
        }
      }
    }
    return t
  }
  for (const d of data) {
    const s = deck.slides.add()
    s.background.fill = C.bg
    if (d.layout !== "cover") {
      text(s, d.titleLines?.join("\n") || d.title, 64, 34, 1152, 108, 40, C.white, true)
      line(s, 64, 160, 1216, 160)
    }
    text(s, String(d.number).padStart(2, "0"), 1180, 690, 36, 20, 16, C.gray, false, "right")
    s.speakerNotes.textFrame.setText(
      d.notes + (d.sources ? "\n\nSources:\n" + d.sources.join("\n") : ""),
    )
    s.speakerNotes.setVisible(true)
    switch (d.layout) {
      case "cover": {
        text(
          s,
          d.title.replace(" of Software", "\nof Software"),
          64,
          50,
          1110,
          144,
          50,
          C.white,
          true,
        )
        text(s, d.subtitle, 64, 219, 1110, 48, 28, C.gray)
        if (!assets.cover) throw new Error("Approved cover illustration is required")
        s.images.add({
          blob: assets.cover,
          contentType: "image/png",
          alt: d.illustrationAlt,
          fit: "contain",
          position: { left: 598, top: 273, width: 618, height: 412 },
        })
        d.lanes.forEach(([label, result, detail], i) => {
          const y = 324 + i * 160,
            color = i ? C.amber : C.cyan
          text(s, label, 64, y, 510, 34, 23, color, true)
          text(s, result, 64, y + 38, 510, 44, 31, C.white, true)
          text(s, detail, 64, y + 84, 495, 55, 24, C.gray)
        })
        text(s, "Vitalii Oborskyi · PMDay", 64, 678, 1060, 26, 20, C.gray)
        break
      }
      case "phase": {
        const blocks = d.items.map(([name, meaning, example], i) => {
          const x = 64 + i * 410,
            color = i === 2 ? C.amber : C.cyan
          const block = rect(s, x, 231, 332, 245, color)
          text(s, name, x + 24, 249, 284, 48, 31, C.white, true)
          text(s, meaning, x + 24, 313, 284, 68, 27, color, true)
          text(s, example, x + 24, 395, 284, 60, 23, C.gray)
          return block
        })
        // Centered connectors attach to the actual blocks, so no arrows float in space.
        connect(s, blocks[0], blocks[1], C.cyan)
        connect(s, blocks[1], blocks[2], C.amber)
        text(s, d.caveat, 64, 522, 1120, 48, 22, C.gray)
        takeaway(s, d.takeaway)
        break
      }
      case "sdlc": {
        text(s, d.scope, 64, 183, 1152, 36, 23, C.gray)
        const nodes = d.steps.map((v, i) =>
          box(
            s,
            v,
            64 + i * 145,
            270,
            130,
            82,
            i === 2 ? C.cyan : i === 5 ? C.amber : C.line,
            v === "Integrate" ? 19 : 21,
          ),
        )
        nodes.slice(1).forEach((n, i) => connect(s, nodes[i], n, C.gray))
        for (const i of [0, 1, 3, 4, 5, 6, 7])
          text(s, "?", 64 + i * 145, 225, 130, 32, 25, C.amber, true, "center")
        text(s, d.codeRate, 340, 358, 158, 54, 21, C.cyan, true, "center")
        text(s, d.constraintRate, 775, 358, 158, 54, 21, C.amber, true, "center")
        text(s, "THEORY OF CONSTRAINTS", 64, 432, 738, 30, 22, C.cyan, true)
        text(s, d.toc, 64, 470, 710, 92, 26, C.white, true)
        text(s, d.risk, 64, 568, 720, 90, 23, C.gray)
        line(s, 826, 432, 826, 651, C.line)
        text(s, d.queueRate, 866, 445, 350, 68, 50, C.amber, true)
        text(s, d.queueLabel, 866, 514, 350, 56, 25, C.white, true)
        text(s, d.exampleCaveat, 866, 582, 350, 76, 20, C.gray)
        break
      }
      case "evidence": {
        line(s, 583, 194, 583, 650, C.line)
        text(s, "NBER · 2026", 64, 195, 500, 30, 22, C.cyan, true)
        d.nberMetrics.forEach(([value, label], i) => {
          const x = 64 + i * 169
          text(s, value, x, 246, 157, 60, 43, C.white, true)
          text(s, label, x, 307, 157, 30, 21, C.gray)
        })
        text(s, d.nberGeneration, 64, 352, 496, 54, 22, C.cyan, true)
        text(s, d.nberCaveat, 64, 411, 496, 55, 20, C.gray)
        text(s, d.marketHeadline, 64, 477, 496, 61, 24, C.white, true)
        d.marketNumbers.forEach(([label, value], i) => {
          const y = 551 + i * 35
          text(s, label, 64, y, 255, 29, 20, C.gray)
          text(s, value, 319, y, 241, 29, 23, C.amber, true, "right")
        })
        text(s, d.marketDetail, 64, 625, 496, 32, 20, C.gray)
        text(s, "DORA · 2025", 616, 195, 600, 30, 22, C.cyan, true)
        d.doraMetrics.forEach(([value, label], i) => {
          const x = 616 + i * 300
          text(s, value, x, 232, 282, 48, 35, C.white, true)
          text(s, label, x, 280, 282, 51, 21, C.gray)
        })
        text(s, d.doraAssociation, 616, 340, 600, 43, 20, C.amber)
        line(s, 616, 392, 1216, 392)
        text(s, "GITCLEAR · JUN 2026", 616, 406, 600, 28, 22, C.cyan, true)
        text(s, d.gitclearMetrics[0], 616, 443, 600, 37, 27, C.white, true)
        text(s, d.gitclearMetrics[1], 616, 482, 600, 36, 27, C.white, true)
        text(s, d.gitclearCaveat, 616, 521, 600, 39, 20, C.gray)
        line(s, 616, 573, 1216, 573)
        d.otherCards.forEach(([source, value, caveat], i) => {
          const x = 616 + i * 306
          text(s, source, x, 584, 294, 25, 20, C.cyan, true)
          text(s, value, x, 611, 294, 33, 24, C.white, true)
          text(s, caveat, x, 644, 294, 25, 20, C.gray)
        })
        text(s, d.takeaway, 64, 677, 1095, 27, 22, C.white, true)
        break
      }
      case "comprehension": {
        line(s, 88, 486, 792, 486, C.gray)
        line(s, 88, 486, 88, 222, C.gray)
        const curves = [
          [
            [100, 469],
            [240, 441],
            [390, 388],
            [545, 302],
            [745, 223],
          ],
          [
            [100, 469],
            [240, 457],
            [390, 439],
            [545, 414],
            [745, 385],
          ],
        ]
        curves.forEach((points, index) =>
          points
            .slice(1)
            .forEach((p, i) => line(s, ...points[i], ...p, index ? C.amber : C.cyan, 4)),
        )
        text(s, d.curves[0], 110, 193, 630, 38, 25, C.cyan, true)
        text(s, d.curves[1], 108, 502, 680, 34, 23, C.amber)
        text(s, "Potential\ncomprehension gap", 540, 310, 240, 64, 22, C.gray)
        d.questions.forEach((q, i) =>
          text(s, q, 850, 229 + i * 115, 350, 84, 30, i === 2 ? C.white : C.gray, i === 2),
        )
        text(s, d.caption, 88, 552, 1090, 34, 21, C.gray)
        takeaway(s, d.takeaway)
        break
      }
      case "recovery": {
        d.incident.forEach((v, i) =>
          text(
            s,
            v,
            64,
            222 + i * 78,
            700,
            64,
            i === 2 ? 48 : 34,
            i === 2 ? C.amber : C.white,
            i === 2,
          ),
        )
        const a = box(s, "AI AGENT", 910, 216, 280, 74, C.red, 28)
        const b = box(s, "TEAM", 910, 386, 280, 78, C.amber, 34)
        connect(s, a, b, C.amber, "bottom", "top")
        text(s, "Recovery\nfails", 778, 308, 220, 66, 23, C.gray)
        text(s, "Hypothetical incident", 64, 459, 610, 30, 20, C.gray)
        text(s, "Watch", 64, 512, 118, 30, 22, C.amber, true)
        text(s, d.watch, 196, 501, 1014, 52, 23, C.gray)
        text(s, "Explore", 64, 562, 118, 30, 22, C.cyan, true)
        text(s, d.explore, 196, 551, 1014, 52, 23, C.gray)
        takeaway(s, d.takeaway)
        break
      }
      case "equilibrium": {
        d.columns.forEach(([head, body], i) => {
          const x = 64 + i * 400,
            color = i === 1 ? C.cyan : C.gray
          text(s, head, x, 218, 352, 50, 23, color, true)
          line(s, x, 284, x + 352, 284, color)
          if (i === 2) text(s, body, x, 331, 352, 168, 118, C.amber, true, "center")
          else body.split("\n").forEach((v, j) => text(s, v, x, 323 + j * 52, 352, 44, 28, C.white))
        })
        line(s, 64, 602, 1216, 602)
        text(s, d.takeaway, 64, 615, 1120, 42, 31, C.white, true)
        text(s, d.caption, 64, 661, 1120, 34, 27, C.cyan)
        break
      }
      case "thinking": {
        text(s, "THINKING SYSTEMS", 64, 202, 1118, 32, 23, C.cyan, true)
        text(s, d.definition, 64, 251, 1104, 100, 32, C.white, true)
        d.labels.forEach((v, i) => {
          const x = 64 + i * 600
          text(s, v, x, 388, 540, 40, 24, C.gray)
          text(s, d.formulae[i], x, 447, 540, 80, 59, i ? C.amber : C.cyan, true)
        })
        text(s, d.caption, 64, 554, 1118, 32, 22, C.gray)
        takeaway(s, d.takeaway)
        break
      }
      case "boundaries": {
        text(s, "OLD", 64, 209, 330, 32, 23, C.gray, true)
        text(s, d.old.replace(" → ", "\n→ "), 64, 286, 330, 130, 36, C.white, true)
        text(s, "NEW", 436, 209, 720, 32, 23, C.cyan, true)
        rect(s, 436, 265, 550, 297, C.amber, C.bg, 2)
        text(s, d.escalate, 458, 284, 510, 38, 25, C.amber)
        rect(s, 458, 343, 506, 196, C.cyan, C.panel, 2)
        text(s, d.allowed, 478, 356, 466, 34, 20, C.cyan, true)
        d.topics.forEach((v, i) => text(s, v, 478, 400 + i * 30, 466, 29, 22, C.white))
        rect(s, 1010, 353, 206, 118, C.red, C.bg, 2)
        text(s, d.outside, 1026, 383, 174, 52, 21, C.red, true, "center")
        takeaway(s, d.takeaway)
        break
      }
      case "evaluation": {
        text(s, d.old, 64, 203, 1120, 42, 27, C.gray)
        const nodes = d.steps.map((v, i) =>
          box(s, v, 64 + i * 236, 280, 208, 86, i === 3 ? C.amber : C.cyan, 24),
        )
        nodes.slice(1).forEach((n, i) => connect(s, nodes[i], n, C.gray))
        text(s, d.overall, 64, 423, 454, 68, 51, C.cyan, true)
        text(s, d.critical, 562, 418, 640, 50, 29, C.white, true)
        text(s, d.decision, 562, 480, 640, 48, 32, C.red, true)
        text(s, d.caption, 64, 548, 1120, 38, 21, C.gray)
        takeaway(s, d.takeaway)
        break
      }
      case "risk": {
        table(s, d.table, 64, 208, 1152, 326, [166, 350, 636])
        text(s, d.caption, 64, 552, 1120, 37, 23, C.gray)
        takeaway(s, d.takeaway, C.white, 31)
        break
      }
      case "control": {
        const nodes = d.steps.map((v, i) =>
          box(s, v, 64 + i * 236, 220, 208, 80, i === 3 ? C.amber : C.cyan, 24),
        )
        nodes.slice(1).forEach((n, i) => connect(s, nodes[i], n, C.gray))
        const obs = box(s, d.loop[0], 1008, 410, 208, 80, C.cyan, 26)
        const dec = box(s, d.loop[1], 700, 410, 236, 80, C.amber, 25)
        const act = box(s, d.loop[2], 300, 410, 280, 80, C.amber, 25)
        connect(s, nodes[4], obs, C.cyan, "bottom", "top")
        connect(s, obs, dec, C.amber, "left", "right")
        connect(s, dec, act, C.amber, "left", "right")
        connect(s, act, nodes[1], C.amber, "top", "bottom", "elbow")
        text(s, d.actions, 64, 520, 1144, 36, 26, C.white)
        text(s, d.caption, 64, 567, 1144, 30, 21, C.gray)
        takeaway(s, d.takeaway)
        break
      }
      case "roles": {
        table(s, d.table, 64, 211, 1152, 360, [178, 344, 630])
        takeaway(s, d.takeaway)
        break
      }
      case "synthesis": {
        d.columns.forEach(([head, subtitle, list], i) => {
          const x = 64 + i * 600,
            color = i ? C.amber : C.cyan
          text(s, head, x, 207, 550, 36, 23, color, true)
          text(s, subtitle, x, 260, 550, 52, 36, C.white, true)
          line(s, x, 334, x + 550, 334, color)
          list.forEach((v, j) => text(s, v, x, 354 + j * 44, 550, 40, 26, C.gray))
        })
        takeaway(s, d.takeaway, C.white, 30)
        // The closing sentence is spoken; it remains in the source and notes.
        break
      }
      default:
        throw new Error(`Unknown layout ${d.layout}`)
    }
  }
  return deck
}
