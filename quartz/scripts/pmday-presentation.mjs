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
    if (data.images) throw new Error("This edition has no approved image exceptions")
    return { ...data, title: section[2] }
  })
}

export function createDeck(Presentation, data) {
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
  function box(s, label, x, y, w, h, color = C.line, font = 27) {
    const shape = rect(s, x, y, w, h, color)
    text(s, label, x + 12, y + 8, w - 24, h - 16, font, C.white, true, "center")
    return shape
  }
  function connect(s, a, b, color = C.cyan, from = "right", to = "left") {
    return s.shapes.connect(a, b, {
      kind: "straight",
      fromSide: from,
      toSide: to,
      line: { fill: color, width: 2.3, style: "solid" },
      tail: { type: "triangle", width: "sm", length: "sm" },
    })
  }
  function takeaway(s, value, color = C.white, y = 590, size = 30) {
    text(s, value, 48, y, 1184, 76, size, color, true, "center")
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
        cell.fill = r === 0 ? "#1A2734" : C.panel
        cell.text.style = {
          typeface: C.font,
          fontSize: r === 0 ? 23 : 26,
          color: c === values[0].length - 1 ? C.cyan : C.white,
          bold: r === 0 || c === 0,
          verticalAlignment: "middle",
          autoFit: "none",
          insets: { left: 16, right: 16, top: 10, bottom: 10 },
        }
      }
    }
    return t
  }
  for (const d of data) {
    const s = deck.slides.add()
    s.background.fill = C.bg
    if (d.layout !== "cover") {
      text(s, d.title, 48, 35, 1184, 105, 42, C.white, true)
      line(s, 48, 145, 1232, 145)
    }
    text(s, String(d.number).padStart(2, "0"), 1185, 680, 47, 22, 17, C.gray, false, "right")
    s.speakerNotes.textFrame.setText(
      d.notes + (d.sources ? "\n\nSources:\n" + d.sources.join("\n") : ""),
    )
    s.speakerNotes.setVisible(true)
    switch (d.layout) {
      case "cover": {
        text(
          s,
          "AI Changes Both Sides\nof Software Engineering",
          48,
          58,
          1180,
          145,
          54,
          C.white,
          true,
        )
        text(s, d.subtitle, 48, 225, 1140, 48, 31, C.gray)
        d.lanes.forEach(([label, result], i) => {
          const y = 337 + i * 102,
            color = i ? C.amber : C.cyan
          text(s, label, 48, y, 330, 46, 31, color, true)
          const a = rect(s, 402, y + 20, 2, 2, C.bg, C.bg, 0)
          const b = rect(s, 548, y + 20, 2, 2, C.bg, C.bg, 0)
          connect(s, a, b, color)
          text(s, result, 580, y, 640, 46, 34, C.white, true)
        })
        text(s, d.takeaway, 48, 590, 1120, 45, 27, C.gray)
        text(s, "Vitalii Oborskyi · PMDay", 48, 671, 800, 27, 20, C.gray)
        break
      }
      case "phase": {
        d.items.forEach(([name, meaning], i) => {
          const x = 48 + i * 405,
            color = i === 2 ? C.amber : C.cyan
          text(s, String(i + 1).padStart(2, "0"), x, 193, 100, 45, 28, color)
          line(s, x, 257, x + 350, 257, color, 3)
          text(s, name, x, 286, 370, 50, 37, C.white, true)
          text(s, meaning.replace(" ", "\n"), x, 349, 370, 96, 29, color)
        })
        text(s, d.caveat, 48, 497, 1184, 57, 24, C.gray, false, "center")
        takeaway(s, d.takeaway, C.white, 578, 30)
        break
      }
      case "sdlc": {
        const nodes = d.steps.map((v, i) =>
          box(
            s,
            v,
            48 + i * 150,
            294,
            133,
            76,
            i === 2 ? C.cyan : C.line,
            v === "Integrate" ? 20 : 22,
          ),
        )
        nodes.slice(1).forEach((n, i) => connect(s, nodes[i], n, C.gray))
        text(s, "↑↑↑", 348, 208, 133, 56, 44, C.cyan, true, "center")
        for (const i of [3, 4, 5, 7])
          text(s, "?", 48 + i * 150, 215, 133, 45, 31, C.amber, true, "center")
        text(s, d.caption, 48, 442, 1184, 76, 30, C.gray, false, "center")
        takeaway(s, d.takeaway, C.cyan)
        break
      }
      case "evidence": {
        rect(s, 48, 172, 596, 400, C.cyan)
        text(s, "NBER · MAY 2026", 68, 183, 550, 30, 22, C.cyan, true)
        d.nberMetrics.forEach(([value, label], i) => {
          const x = 68 + i * 188
          text(s, value, x, 227, 180, 61, 53, C.white, true)
          text(s, label, x, 292, 182, 34, 22, C.gray)
        })
        text(s, d.nberGeneration, 68, 335, 554, 32, 22, C.cyan, true)
        text(s, d.nberCaveat, 68, 375, 550, 42, 17, C.gray)
        line(s, 68, 433, 621, 433)
        text(s, d.marketHeadline, 68, 444, 550, 50, 25, C.white, true)
        d.marketNumbers.forEach(([label, value], i) => {
          text(s, label, 68, 502 + i * 29, 355, 28, 20, C.gray)
          text(s, value, 425, 502 + i * 29, 200, 28, 22, C.amber, true, "right")
        })
        d.cards.forEach(([source, value, caveat], i) => {
          const x = 668 + (i % 2) * 287,
            y = 172 + Math.floor(i / 2) * 205
          rect(s, x, y, 277, 195)
          text(s, source, x + 16, y + 14, 245, 36, 17, C.cyan, true)
          text(s, value, x + 16, y + 58, 245, 78, 27, C.white, true)
          text(s, caveat, x + 16, y + 142, 245, 44, 18, C.gray)
        })
        text(s, d.marketDetail, 48, 581, 1184, 33, 19, C.gray)
        takeaway(s, d.takeaway, C.white, 618, 27)
        break
      }
      case "comprehension": {
        line(s, 90, 505, 800, 505, C.gray)
        line(s, 90, 505, 90, 216, C.gray)
        const a = [
          [100, 479],
          [245, 444],
          [395, 375],
          [545, 286],
          [740, 190],
        ]
        const b = [
          [100, 479],
          [245, 463],
          [395, 447],
          [545, 428],
          [740, 401],
        ]
        for (const [points, color] of [
          [a, C.cyan],
          [b, C.amber],
        ]) {
          points.slice(1).forEach((point, i) => line(s, ...points[i], ...point, color, 4))
        }
        text(s, d.curves[0], 108, 176, 600, 42, 26, C.cyan, true)
        text(s, d.curves[1], 375, 437, 420, 50, 24, C.amber)
        text(s, "Potential\ncomprehension gap", 486, 319, 300, 66, 25, C.gray)
        d.questions.forEach((v, i) => text(s, v, 851, 234 + i * 104, 364, 80, 30, C.white, i === 2))
        text(s, d.caption, 90, 526, 1090, 32, 19, C.gray)
        takeaway(s, d.takeaway, C.white)
        break
      }
      case "recovery": {
        d.incident.forEach((v, i) =>
          text(
            s,
            v,
            48,
            195 + i * 71,
            665,
            61,
            i === 2 ? 46 : 34,
            i === 2 ? C.amber : C.white,
            i === 2,
          ),
        )
        const a = box(s, "AI AGENT", 825, 212, 345, 76, C.red, 31)
        const b = box(s, "TEAM", 825, 372, 345, 84, C.amber, 36)
        connect(s, a, b, C.amber, "bottom", "top")
        text(s, "Recovery fails", 1018, 311, 196, 33, 21, C.gray)
        text(s, "Hypothetical incident", 48, 425, 650, 30, 20, C.gray)
        text(s, "Watch: " + d.watch, 48, 493, 1184, 43, 23, C.gray)
        text(s, "Explore: " + d.explore, 48, 543, 1184, 43, 23, C.gray)
        takeaway(s, d.takeaway, C.white, 609, 29)
        break
      }
      case "equilibrium": {
        d.columns.forEach(([head, body], i) => {
          const x = 48 + i * 405
          text(s, head, x, 203, 376, 54, 24, i === 1 ? C.cyan : C.gray, true)
          line(s, x, 272, x + 358, 272, i === 1 ? C.cyan : C.line)
          text(
            s,
            body,
            x,
            301,
            366,
            224,
            i === 2 ? 126 : 30,
            i === 2 ? C.amber : C.white,
            i === 2,
            i === 2 ? "center" : "left",
          )
        })
        takeaway(s, d.takeaway, C.white, 564, 34)
        text(s, d.caption, 48, 640, 1184, 34, 27, C.cyan, false, "center")
        break
      }
      case "thinking": {
        text(s, "THINKING SYSTEMS", 48, 178, 1184, 36, 24, C.cyan, true)
        text(s, d.definition, 48, 233, 1184, 100, 33, C.white, true)
        d.labels.forEach((v, i) => {
          const x = 48 + i * 630
          text(s, v, x, 373, 555, 42, 25, C.gray)
          text(s, d.formulae[i], x, 429, 555, 82, 57, i ? C.amber : C.cyan, true)
        })
        text(s, d.caption, 48, 539, 1184, 35, 23, C.gray)
        takeaway(s, d.takeaway, C.white)
        break
      }
      case "boundaries": {
        text(s, "OLD", 48, 195, 300, 38, 24, C.gray, true)
        text(s, d.old, 48, 264, 370, 120, 35, C.white, true)
        text(s, "NEW", 471, 181, 740, 37, 24, C.cyan, true)
        rect(s, 470, 239, 551, 284, C.amber, C.bg, 2)
        rect(s, 496, 292, 510, 200, C.cyan, C.panel, 2)
        text(s, d.allowed, 518, 308, 472, 42, 20, C.cyan, true)
        d.topics.forEach((v, i) => text(s, v, 518, 358 + i * 31, 470, 29, 23, C.white))
        text(s, d.escalate, 488, 249, 700, 33, 24, C.amber)
        rect(s, 1040, 337, 176, 110, C.red, C.bg, 2)
        text(s, d.outside, 1044, 363, 168, 57, 20, C.red, true, "center")
        takeaway(s, d.takeaway, C.white, 580, 30)
        break
      }
      case "evaluation": {
        text(s, d.old, 48, 177, 1184, 48, 28, C.gray)
        const nodes = d.steps.map((v, i) =>
          box(s, v, 48 + i * 240, 265, 222, 92, i === 3 ? C.amber : C.cyan, 26),
        )
        nodes.slice(1).forEach((n, i) => connect(s, nodes[i], n, C.gray))
        text(s, d.overall, 48, 405, 470, 73, 52, C.cyan, true)
        text(s, d.critical, 545, 404, 670, 50, 30, C.white, true)
        text(s, d.decision, 545, 470, 670, 47, 33, C.red, true)
        text(s, d.caption, 48, 540, 1184, 38, 21, C.gray)
        takeaway(s, d.takeaway, C.white, 601, 29)
        break
      }
      case "risk": {
        table(s, d.table, 48, 197, 1184, 344, [174, 408, 602])
        takeaway(s, d.takeaway, C.white, 565, 30)
        text(s, d.caption, 48, 644, 1184, 30, 22, C.gray, false, "center")
        break
      }
      case "control": {
        const nodes = d.steps.map((v, i) =>
          box(s, v, 48 + i * 240, 229, 222, 84, i === 3 ? C.amber : C.cyan, 25),
        )
        nodes.slice(1).forEach((n, i) => connect(s, nodes[i], n, C.gray))
        const obs = box(s, d.loop[0], 574, 415, 222, 76, C.cyan, 27)
        const dec = box(s, d.loop[1], 303, 415, 222, 76, C.amber, 26)
        const act = box(s, d.loop[2], 48, 415, 209, 76, C.amber, 25)
        connect(s, nodes[2], obs, C.cyan, "bottom", "top")
        connect(s, obs, dec, C.amber, "left", "right")
        connect(s, dec, act, C.amber, "left", "right")
        // Feedback returns to the controlled process; policy gating remains on the action path.
        connect(s, act, nodes[1], C.amber, "top", "bottom")
        text(s, d.actions, 847, 409, 370, 100, 28, C.white)
        text(s, d.caption, 48, 547, 1184, 48, 22, C.gray)
        takeaway(s, d.takeaway, C.white, 615, 27)
        break
      }
      case "roles": {
        table(s, d.table, 48, 197, 1184, 373, [184, 382, 618])
        takeaway(s, d.takeaway, C.white, 600, 29)
        break
      }
      case "synthesis": {
        d.columns.forEach(([head, subtitle, list], i) => {
          const x = 48 + i * 625,
            color = i ? C.amber : C.cyan
          text(s, head, x, 177, 560, 38, 24, color, true)
          text(s, subtitle, x, 228, 560, 50, 38, C.white, true)
          list.forEach((v, j) => text(s, v, x, 300 + j * 47, 568, 43, 27, C.gray))
        })
        takeaway(s, d.takeaway, C.white, 570, 33)
        text(s, d.closing, 48, 648, 1184, 31, 24, C.gray, false, "center")
        break
      }
      default:
        throw new Error(`Unknown layout ${d.layout}`)
    }
  }
  return deck
}
