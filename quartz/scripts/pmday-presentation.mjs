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
  const deck = Presentation.create({
    slideSize: { width: C.width, height: C.height },
  })
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
          36,
          1110,
          132,
          46,
          C.white,
          true,
        )
        text(s, d.subtitle, 64, 179, 1110, 44, 27, C.gray)
        if (!assets.cover) throw new Error("Approved cover illustration is required")
        s.images.add({
          blob: assets.cover,
          contentType: "image/png",
          alt: d.illustrationAlt,
          fit: "contain",
          position: { left: 96, top: 231, width: 1088, height: 363 },
        })
        d.lanes.forEach(([label, detail], i) => {
          const x = 96 + i * 584,
            color = i ? C.amber : C.cyan
          text(s, label, x, 602, 504, 31, 22, color, true)
          text(s, detail, x, 637, 504, 35, 24, C.white)
        })
        text(s, "Vitalii Oborskyi · PMDay", 64, 678, 1060, 26, 20, C.gray)
        break
      }
      case "phase": {
        const blocks = d.items.map(([name, meaning, example], i) => {
          const x = 112 + i * 378,
            color = i === 2 ? C.amber : C.cyan
          const block = rect(s, x, 231, 300, 245, color)
          text(s, name, x + 24, 249, 252, 48, 30, C.white, true)
          text(s, meaning, x + 24, 313, 252, 68, 27, color, true)
          text(s, example, x + 24, 395, 252, 60, 23, C.gray)
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
        text(s, d.scope, 96, 180, 1088, 34, 22, C.gray)
        const nodes = d.steps.map((v, i) =>
          box(
            s,
            v,
            96 + i * 138,
            245,
            122,
            56,
            i === 2 ? C.cyan : C.line,
            v === "Integrate" ? 18 : 19,
          ),
        )
        // Plain links avoid arrowheads being rendered as a spanning arrow by slide viewers.
        nodes.slice(1).forEach((_, i) => line(s, 218 + i * 138, 273, 234 + i * 138, 273, C.gray))
        for (const i of [0, 1, 3, 4, 5, 6, 7])
          text(s, "?", 96 + i * 138, 216, 122, 25, 21, C.amber, true, "center")
        text(s, d.exampleHeading, 96, 322, 1088, 30, 20, C.gray)
        d.exampleStages.forEach((v, i) =>
          text(s, v, 340 + i * 218, 360, 172, 30, 22, C.white, true, "center"),
        )
        text(s, "BACKLOG", 1006, 360, 178, 30, 20, C.gray, true, "center")
        d.exampleRows.forEach(([label, caption, rates, backlog], row) => {
          const y = 399 + row * 104
          text(s, label, 96, y + 3, 220, 31, 22, row ? C.cyan : C.gray, true)
          text(s, caption, 96, y + 37, 220, 43, 18, C.gray)
          const stages = rates.map((rate, i) => {
            const color = row && i === 0 ? C.cyan : row ? C.amber : C.line
            const shape = rect(s, 340 + i * 218, y, 172, 68, color)
            text(
              s,
              rate,
              352 + i * 218,
              y + 7,
              148,
              54,
              36,
              row && i === 0 ? C.cyan : C.white,
              true,
              "center",
            )
            return shape
          })
          stages
            .slice(1)
            .forEach((_, i) => line(s, 512 + i * 218, y + 34, 558 + i * 218, y + 34, C.gray))
          text(s, backlog, 1006, y + 3, 178, 49, 39, row ? C.amber : C.gray, true, "center")
          text(
            s,
            row ? "unfinished / week" : "no accumulation",
            1006,
            y + 51,
            178,
            28,
            17,
            C.gray,
            false,
            "center",
          )
        })
        line(s, 96, 599, 1184, 599)
        text(s, "THEORY OF CONSTRAINTS", 96, 612, 535, 27, 20, C.cyan, true)
        text(s, d.toc, 96, 645, 1088, 40, 25, C.white, true)
        text(s, d.exampleCaveat, 670, 612, 514, 30, 18, C.gray, false, "right")
        break
      }
      case "evidence": {
        line(s, 583, 194, 583, 608, C.line)
        text(s, d.nberSource, 64, 195, 500, 30, 22, C.cyan, true)
        d.nberMetrics.forEach(([value, label], i) => {
          const x = 64 + i * 169
          text(s, value, x, 246, 157, 60, 43, C.white, true)
          text(s, label, x, 307, 157, 30, 21, C.gray)
        })
        text(s, d.nberGeneration, 64, 349, 496, 32, 21, C.cyan, true)
        text(s, d.nberCaveat, 64, 384, 496, 51, 20, C.gray)
        text(s, d.marketHeadline, 64, 447, 496, 61, 24, C.white, true)
        d.marketNumbers.forEach(([label, value], i) => {
          const y = 518 + i * 34
          text(s, label, 64, y, 255, 29, 20, C.gray)
          text(s, value, 319, y, 241, 29, 23, C.amber, true, "right")
        })
        text(s, d.marketDetail, 64, 585, 496, 26, 19, C.gray)
        text(s, "DORA · 2025", 616, 195, 600, 30, 22, C.cyan, true)
        d.doraHeadline
          .split("\n")
          .forEach((value, i) =>
            text(s, value, 616, 230 + i * 33, 600, 32, 27, i ? C.amber : C.white, true),
          )
        text(
          s,
          `${d.doraInstability} instability per +1 SD AI adoption`,
          616,
          304,
          600,
          26,
          19,
          C.amber,
        )
        text(s, d.doraInterval, 616, 332, 600, 24, 18, C.gray)
        text(s, d.doraMeasures, 616, 362, 600, 45, 18, C.gray)
        text(s, d.doraPerceptions, 616, 406, 600, 25, 17, C.gray)
        line(s, 616, 441, 1216, 441)
        text(s, d.gitclearSource, 616, 452, 600, 28, 22, C.cyan, true)
        d.gitclearMetrics.forEach(([label, value], i) => {
          const y = 483 + i * 26
          text(s, label, 616, y, 405, 27, 23, C.white)
          text(s, value, 1015, y, 201, 27, 24, C.white, true, "right")
        })
        text(s, d.gitclearCaveat, 616, 591, 600, 21, 18, C.gray)
        line(s, 64, 618, 1216, 618)
        d.otherCards.forEach(([source, value, caveat], i) => {
          const x = 64 + i * 582
          text(s, source, x, 628, 304, 27, 20, C.cyan, true)
          text(s, value, x + 308, 626, 244, 30, i ? 21 : 23, C.white, true, "right")
          text(s, caveat, x, 658, 552, 25, 18, C.gray)
        })
        text(s, d.takeaway, 64, 689, 1095, 26, 20, C.white, true)
        break
      }
      case "comprehension": {
        line(s, 88, 493, 790, 493, C.gray)
        line(s, 88, 493, 88, 228, C.gray)
        // One dense native path samples a smooth conceptual curve. The nearly
        // fixed human capacity is an explicit scenario assumption, not measured data.
        const commands = Array.from({ length: 121 }, (_, i) => {
          const t = i / 120
          const point = { x: 645 * t, y: 230 - 230 * (0.18 * t + 0.82 * t * t) }
          return i ? { lineTo: point } : { moveTo: point }
        })
        s.shapes.add({
          geometry: "custom",
          position: { left: 100, top: 235, width: 645, height: 230 },
          fill: "none",
          line: { fill: C.cyan, width: 4, style: "solid" },
          customPaths: [{ width: 645, height: 230, commands }],
        })
        line(s, 100, 465, 745, 465, C.amber, 4)
        text(s, d.curves[0], 110, 193, 630, 38, 25, C.cyan, true)
        text(s, d.curves[1], 108, 510, 680, 34, 23, C.amber)
        text(s, "Potential\ncomprehension gap", 525, 370, 260, 64, 22, C.gray)
        text(s, "Adoption / time", 585, 493, 205, 25, 16, C.gray, false, "right")
        d.questions.forEach(([question, answer], i) => {
          const y = 220 + i * 115
          text(s, question, 845, y, 370, 62, 25, C.gray)
          text(s, answer, 845, y + 61, 370, 40, i === 2 ? 41 : 28, i ? C.amber : C.cyan, true)
        })
        text(s, d.caption, 88, 561, 1100, 30, 20, C.gray)
        takeaway(s, d.takeaway)
        break
      }
      case "recovery": {
        text(s, d.premise, 64, 190, 1152, 43, 29, C.white, true)
        text(s, d.risk, 64, 238, 1152, 42, 25, C.gray)
        const nodes = d.steps.map(([label, detail], i) => {
          const x = 64 + i * 300
          const color = i === 1 ? C.red : i === 2 ? C.amber : C.cyan
          const node = box(s, label, x, 324, 252, 88, color, 25)
          text(s, detail, x, 436, 252, 109, 22, C.gray)
          return node
        })
        nodes.slice(1).forEach((n, i) => connect(s, nodes[i], n, i === 1 ? C.amber : C.gray))
        text(s, d.caption, 64, 559, 1152, 31, 20, C.gray)
        takeaway(s, d.takeaway)
        break
      }
      case "equilibrium": {
        d.columns.forEach(([heading, summary], i) => {
          const x = 64 + i * 398
          text(s, heading, x, 194, 356, 29, 21, i === 1 ? C.cyan : C.gray, true)
          text(s, summary, x, 229, 356, 42, 22, i === 2 ? C.amber : C.white)
        })
        line(s, 64, 292, 1216, 292)
        ;[
          ["WATCH", d.watchRows, C.amber],
          ["EXPLORE", d.exploreRows, C.cyan],
        ].forEach(([heading, rows, color], column) => {
          const x = 64 + column * 596
          text(s, heading, x, 308, 552, 35, 27, color, true)
          rows.forEach(([label, detail], i) => {
            const y = 357 + i * 56
            text(s, label, x, y, 552, 28, 23, C.white, true)
            text(s, detail, x, y + 28, 552, 26, 20, C.gray)
          })
        })
        line(s, 64, 602, 1216, 602)
        text(s, d.takeaway, 64, 615, 1120, 42, 28, C.white, true)
        text(s, d.caption, 64, 664, 1120, 30, 23, C.cyan)
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
