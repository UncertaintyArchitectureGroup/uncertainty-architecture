// Native editable PowerPoint rendition of the maintainer-approved Markdown.
// Content lives in pptx-slide blocks; this module owns geometry, not research claims.
export const slideCount = 15
export const theme = {
  bg: "#0B0F14",
  panel: "#141C26",
  white: "#F4F7FA",
  gray: "#ADB8C5",
  line: "#344454",
  cyan: "#28C7F7",
  amber: "#F5B61C",
  red: "#FF6B75",
  font: "Arial",
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
  "resources",
]

export function parseDeck(markdown) {
  const sections = [
    ...markdown.matchAll(/^## (\d+)\. (.+)\n([\s\S]*?)(?=^## \d+\. |$(?![\s\S]))/gm),
  ]
  if (sections.length !== slideCount) throw new Error("Expected exactly 15 approved slide sections")
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
        "Only the fixed cover and closing QR assets are approved; arbitrary image exceptions are forbidden",
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
  function table(s, values, x, y, w, h, widths, font = 25, padding = 12) {
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
          fontSize: r === 0 ? 21 : font,
          color: c === values[0].length - 1 ? C.cyan : C.white,
          bold: r === 0 || c === 0,
          verticalAlignment: "middle",
          autoFit: "none",
          insets: { left: 18, right: 18, top: padding, bottom: padding },
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
          position: { left: 96, top: 231, width: 1088, height: 300 },
        })
        d.lanes.forEach(([label, detail], i) => {
          const x = 96 + i * 584,
            color = i ? C.amber : C.cyan
          text(s, label, x, 540, 504, 31, 22, color, true)
          text(s, detail, x, 575, 504, 35, 24, C.white)
        })
        line(s, 64, 618, 1216, 618)
        text(s, d.author, 64, 631, 260, 30, 24, C.white, true)
        text(s, d.bio, 344, 632, 872, 29, 20, C.gray)
        const mail = text(s, d.email, 64, 674, 432, 25, 19, C.cyan)
        mail.text.get(d.email).link = { uri: `mailto:${d.email}`, isExternal: true }
        const linkedin = text(s, d.linkedin, 518, 674, 636, 25, 19, C.cyan)
        linkedin.text.get(d.linkedin).link = { uri: d.linkedin, isExternal: true }
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
        line(s, 440, 195, 440, 590)
        line(s, 838, 195, 838, 590)
        text(s, d.nberSource, 64, 195, 352, 30, 20, C.cyan, true)
        text(s, d.nberGeneration, 64, 233, 352, 28, 18, C.gray)
        d.nberMetrics.forEach(([value, label], i) => {
          text(s, value, 64, 276 + i * 64, 156, 52, 42, C.white, true)
          text(s, label, 228, 288 + i * 64, 188, 32, 22, C.gray)
        })
        text(s, d.nberCaveat, 64, 466, 352, 44, 17, C.gray)
        text(s, d.marketHeadline, 64, 521, 352, 26, 19, C.white, true)
        d.marketNumbers.forEach(([label, value], i) => {
          text(s, label, 64, 551 + i * 28, 224, 25, 17, C.gray)
          text(s, value, 288, 551 + i * 28, 128, 25, 20, C.amber, true, "right")
        })
        text(s, d.marketDetail, 64, 609, 352, 24, 16, C.gray)
        text(s, "DORA · 2025", 464, 195, 350, 30, 20, C.cyan, true)
        d.doraHeadline
          .split("\n")
          .forEach((value, i) =>
            text(s, value, 464, 259 + i * 41, 350, 36, 28, i ? C.amber : C.white, true),
          )
        text(s, d.doraInstability, 464, 369, 350, 50, 40, C.amber, true)
        text(s, "instability per +1 SD AI adoption", 464, 425, 350, 30, 20, C.gray)
        text(s, d.doraInterval, 464, 479, 350, 58, 23, C.white)
        text(s, d.doraMeasures, 464, 565, 350, 55, 18, C.gray)
        text(s, d.gitclearSource, 862, 195, 354, 30, 20, C.cyan, true)
        d.gitclearMetrics.slice(0, 2).forEach(([label, value], i) => {
          text(s, label, 862, 257 + i * 112, 354, 30, 23, C.gray)
          text(s, value, 862, 294 + i * 112, 354, 48, 38, C.white, true)
        })
        text(s, "Duplicated blocks ≈+81%\nTwo-week churn +15%*", 862, 492, 354, 59, 23, C.white)
        text(s, d.gitclearCaveat, 862, 574, 354, 46, 17, C.amber)
        line(s, 64, 642, 1216, 642)
        text(s, d.comparisonCaveat, 64, 649, 1152, 25, 19, C.gray)
        text(s, d.takeaway, 64, 681, 1118, 29, 26, C.white, true)
        break
      }
      case "comprehension": {
        line(s, 88, 493, 790, 493, C.gray)
        line(s, 88, 493, 88, 228, C.gray)
        // One dense native path samples a smooth conceptual curve. The nearly
        // fixed human capacity is an explicit scenario assumption, not measured data.
        const commands = Array.from({ length: 121 }, (_, i) => {
          const t = i / 120
          const point = {
            x: 645 * t,
            y: 230 - 230 * (0.18 * t + 0.82 * t * t),
          }
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
        text(s, d.role, 64, 176, 1118, 28, 21, C.cyan, true)
        text(s, d.definition, 64, 212, 1152, 62, 27, C.white, true)
        d.labels.forEach((v, i) => {
          const x = 64 + i * 600
          text(s, v, x, 292, 552, 31, 23, C.gray)
          text(s, d.formulae[i], x, 328, 552, 67, 52, i ? C.amber : C.cyan, true)
        })
        // Requested conceptual distribution, not a fitted density or observed sample.
        line(s, 640, 292, 640, 552)
        line(s, 100, 510, 570, 510, C.gray)
        rect(s, 324, 410, 26, 100, C.cyan, C.cyan, 0)
        text(s, d.graphLabels[0], 140, 518, 400, 26, 21, C.cyan, true, "center")
        const heights = [16, 28, 48, 76, 105, 122, 105, 76, 48, 28, 16]
        heights.forEach((h, i) => {
          const color = i < 2 || i > 8 ? C.amber : C.cyan
          rect(s, 780 + i * 29, 510 - h, 21, h, color, color, 0)
        })
        line(s, 695, 510, 1206, 510, C.gray)
        text(s, d.graphLabels[2], 687, 524, 145, 39, 17, C.amber, false, "center")
        text(s, d.graphLabels[1], 839, 521, 225, 28, 20, C.cyan, true, "center")
        text(s, d.graphLabels[2], 1071, 524, 145, 39, 17, C.amber, false, "center")
        text(s, d.deterministicDetail, 64, 563, 552, 27, 20, C.white)
        text(s, d.probabilisticDetail, 664, 563, 552, 27, 20, C.white)
        line(s, 64, 602, 1216, 602)
        text(s, d.takeaway, 64, 633, 1118, 54, 26, C.white, true)
        text(s, d.caption, 64, 606, 1152, 24, 18, C.gray)
        text(s, d.graphCaption, 64, 695, 1118, 19, 16, C.gray)
        break
      }
      case "boundaries": {
        text(s, d.role, 64, 176, 1152, 32, 22, C.cyan, true)
        line(s, 508, 220, 508, 440)
        text(s, d.oldHeading, 64, 220, 420, 30, 19, C.gray, true)
        const a = box(s, d.old[0], 64, 259, 169, 58, C.gray, 26)
        const b = box(s, d.old[1], 302, 259, 182, 58, C.gray, 26)
        connect(s, a, b, C.gray)
        text(s, d.oldDetail, 64, 330, 420, 57, 25, C.white)
        text(s, d.roleDetail, 64, 397, 420, 67, 20, C.gray)
        text(s, d.newHeading, 536, 220, 680, 30, 19, C.cyan, true)
        // Match the supplied possibility-space topology using editable geometry.
        // The perspective plane is conceptual, with no universal semantic-distance scale.
        for (let i = 0; i < 5; i++) line(s, 557, 279 + i * 32, 1205, 279 + i * 32)
        for (let i = 0; i < 6; i++) line(s, 557 + i * 110, 409, 611 + i * 110, 267)
        line(s, 557, 411, 1205, 411, C.gray)
        line(s, 557, 411, 557, 263, C.gray)
        const plane = (x, y, w, h, slant, color, fill) =>
          s.shapes.add({
            geometry: "custom",
            position: { left: x, top: y, width: w, height: h },
            fill,
            line: { fill: color, width: 2, style: "solid" },
            customPaths: [
              {
                width: w,
                height: h,
                commands: [
                  { moveTo: { x: slant, y: 0 } },
                  { lineTo: { x: w, y: 0 } },
                  { lineTo: { x: w - slant, y: h } },
                  { lineTo: { x: 0, y: h } },
                  { close: {} },
                ],
              },
            ],
          })
        plane(615, 277, 470, 120, 44, C.amber, "#24231B")
        plane(701, 305, 322, 80, 23, C.cyan, "#122934")
        text(s, d.regionCaption, 746, 249, 440, 26, 19, C.amber, true)
        text(s, d.regionInner, 724, 310, 278, 23, 18, C.cyan, true, "center")
        d.regionExamples.forEach((v, i) => {
          text(s, v, 730, 339 + i * 22, 270, 21, 17, C.white, false, "center")
        })
        rect(s, 1166, 329, 10, 10, C.red, C.red, 0)
        text(s, d.regionOutside, 1086, 347, 130, 43, 18, C.red, false, "center")
        text(s, d.regionAxis, 557, 413, 659, 24, 17, C.gray)
        text(s, d.regionPolicy, 536, 442, 680, 25, 16, C.white)
        line(s, 64, 477, 1216, 477)
        text(s, d.envelopeHeading, 64, 492, 1152, 28, 22, C.amber, true)
        d.envelope.forEach((v, i) =>
          text(s, v, 64 + (i % 2) * 596, 534 + Math.floor(i / 2) * 35, 552, 30, 21, C.white),
        )
        text(s, d.specification, 64, 616, 1152, 28, 20, C.gray)
        text(s, d.takeaway, 64, 667, 1118, 32, 25, C.white, true)
        break
      }
      case "evaluation": {
        text(s, d.role, 64, 176, 1152, 32, 22, C.cyan, true)
        text(s, d.bugHeading, 64, 221, 470, 25, 18, C.amber, true)
        text(s, d.bugDefinition, 64, 251, 470, 68, 28, C.white, true)
        text(s, d.bugModel, 64, 326, 485, 53, 21, C.gray)
        text(s, d.bugCode, 64, 384, 485, 24, 17, C.gray)
        const accepted = "#57CB8F"
        text(s, d.toleranceHeading, 704, 221, 396, 25, 18, accepted, true, "center")
        rect(s, 802, 253, 231, 134, "none", "#132A23", 0)
        const bars = [15, 23, 36, 52, 72, 98, 121, 103, 77, 54, 35, 24, 15]
        bars.forEach((h, i) => {
          const color = i < 4 || i > 10 ? C.red : accepted
          rect(s, 682 + i * 32, 387 - h, 23, h, color, color, 0)
        })
        line(s, 802, 251, 802, 388, accepted)
        line(s, 1033, 251, 1033, 388, accepted)
        line(s, 598, 389, 1216, 389, C.gray)
        line(s, 1082, 370, 1110, 338, C.red)
        text(s, d.bugLabel, 1116, 288, 100, 57, 18, C.red)
        text(s, d.outsideLabel, 594, 393, 200, 24, 17, C.red, false, "center")
        text(s, d.insideLabel, 810, 393, 212, 24, 19, accepted, true, "center")
        text(s, d.outsideLabel, 1037, 393, 179, 24, 17, C.red, false, "center")
        text(s, d.schematicCaption, 594, 419, 622, 23, 16, C.gray)
        line(s, 64, 451, 1216, 451)
        text(s, d.frequency, 64, 456, 540, 26, 19, C.cyan, true)
        // Exact categories from the illustrative 200-output sample; no fitted density.
        s.charts.add("bar", {
          position: { left: 64, top: 484, width: 540, height: 129 },
          categories: d.chartCategories,
          series: [
            {
              name: "Observed outputs",
              values: d.chartCounts,
              fill: C.cyan,
              points: [C.cyan, C.amber, C.red].map((fill, idx) => ({
                idx,
                fill,
                line: { fill: "none", width: 0 },
              })),
              dataLabelOverrides: d.chartLabels.map((value, idx) => ({
                idx,
                text: value,
                position: "outEnd",
                showValue: false,
                textStyle: {
                  typeface: C.font,
                  fontSize: 16,
                  fill: C.white,
                  bold: true,
                },
              })),
            },
          ],
          hasLegend: false,
          barOptions: {
            direction: "column",
            grouping: "clustered",
            gapWidth: 95,
          },
          chartFill: C.bg,
          chartLine: { fill: "none", width: 0 },
          plotAreaFill: C.bg,
          plotAreaLine: { fill: "none", width: 0 },
          xAxis: {
            textStyle: { typeface: C.font, fontSize: 16, fill: C.gray },
            line: { fill: C.line, width: 1 },
            majorGridlines: null,
          },
          yAxis: {
            min: 0,
            max: 200,
            majorUnit: 100,
            numberFormatCode: "0",
            textStyle: { typeface: C.font, fontSize: 15, fill: C.gray },
            line: { fill: "none", width: 0 },
            majorGridlines: { fill: C.line, width: 1 },
          },
          dataLabels: {
            showValue: true,
            position: "outEnd",
            textStyle: {
              typeface: C.font,
              fontSize: 16,
              fill: C.white,
              bold: true,
            },
          },
        })
        line(s, 625, 461, 625, 605)
        text(s, d.observed, 660, 456, 244, 39, 31, C.white, true)
        text(s, d.rateLabel, 909, 463, 307, 28, 18, C.gray)
        text(s, d.interval, 660, 497, 556, 27, 22, C.cyan)
        d.harms.forEach((v, i) => text(s, v, 660, 529 + i * 27, 556, 25, 20, i ? C.red : C.white))
        text(s, d.decision, 660, 584, 556, 28, 23, C.red, true)
        text(s, d.instruments, 64, 621, 1152, 26, 19, C.cyan, true)
        text(s, d.calibration, 64, 651, 1152, 25, 19, C.white)
        text(s, d.ownershipLine, 64, 681, 1118, 27, 20, C.white, true)
        break
      }
      case "risk": {
        text(s, d.role, 64, 176, 1152, 32, 22, C.cyan, true)
        text(s, d.behavior, 64, 213, 1152, 28, 21, C.gray)
        const gates = table(s, d.table, 64, 250, 1152, 292, [164, 400, 588], 21, 8)
        ;[40, 126, 126].forEach((h, i) => {
          gates.rows[i].height = h
        })
        text(s, d.releaseHeading, 64, 553, 1152, 26, 19, C.amber, true)
        text(s, d.release, 64, 582, 1152, 28, 21, C.white)
        text(s, d.incident, 64, 613, 1152, 28, 20, C.cyan)
        text(s, d.caption, 64, 645, 1152, 25, 18, C.gray)
        text(s, d.takeaway, 64, 676, 1118, 28, 22, C.white, true)
        break
      }
      case "control": {
        text(s, d.role, 64, 176, 1152, 32, 21, C.cyan, true)
        text(s, d.perimeterHeading, 64, 218, 1152, 26, 21, C.white, true)
        const flow = d.steps.map((label, i) =>
          box(s, label, 64 + i * 302, 278, 246, 74, i === 1 ? C.amber : C.cyan, 22),
        )
        flow.slice(1).forEach((node, i) => connect(s, flow[i], node, C.cyan))
        const human = box(s, d.human, 64, 439, 246, 69, C.gray, 21)
        connect(s, human, flow[1], C.gray, "right", "left", "elbow")
        text(s, d.humanDetail, 64, 513, 246, 44, 17, C.gray, false, "center")
        const fallback = box(s, d.fallback, 366, 439, 246, 69, C.amber, 21)
        connect(s, flow[1], fallback, C.amber, "bottom", "top")
        text(s, d.gateLabel, 501, 383, 155, 45, 18, C.amber)
        const controller = box(s, d.controller, 970, 439, 246, 69, C.amber, 21)
        const actuator = box(s, d.actuator, 668, 439, 246, 69, C.amber, 21)
        connect(s, flow[3], controller, C.cyan, "bottom", "top")
        connect(s, controller, actuator, C.amber, "left", "right")
        connect(s, actuator, flow[2], C.amber, "top", "bottom")
        text(s, d.controlCaveat, 348, 522, 868, 30, 20, C.white, true)
        line(s, 64, 568, 1216, 568)
        text(s, d.proportionHeading, 64, 577, 1152, 25, 19, C.cyan, true)
        d.proportion.forEach(([head, detail], i) => {
          text(s, head, 64 + i * 596, 610, 552, 25, 19, C.white, true)
          text(s, detail, 64 + i * 596, 640, 552, 27, 21, C.gray)
        })
        text(s, d.vetoAction, 64, 679, 1118, 29, 22, C.red, true)
        break
      }
      case "roles": {
        text(s, d.role, 64, 176, 1152, 32, 22, C.cyan, true)
        text(s, d.foundation, 64, 213, 1152, 28, 21, C.gray)
        text(s, d.caseHeading, 64, 247, 1152, 26, 19, C.amber, true)
        const examples = d.caseSteps.map((v, i) =>
          box(s, v, 64 + i * 410, 281, 332, 54, i === 2 ? C.red : C.line, 21),
        )
        connect(s, examples[0], examples[1], C.gray)
        connect(s, examples[1], examples[2], C.red)
        text(s, d.caseAction, 64, 343, 1152, 28, 21, C.white, true)
        const horizons = table(s, d.table, 64, 385, 1152, 210, [236, 458, 458], 19, 4)
        ;[36, 58, 58, 58].forEach((h, i) => {
          horizons.rows[i].height = h
        })
        text(s, d.statisticalLiteracy, 64, 609, 1152, 29, 21, C.amber)
        text(s, d.roleBoundary, 64, 646, 1152, 28, 20, C.gray)
        text(s, d.takeaway, 64, 682, 1118, 27, 23, C.white, true)
        break
      }
      case "synthesis": {
        text(s, d.factoryHeading, 64, 195, 438, 28, 21, C.gray, true)
        text(s, d.factoryFlow, 64, 235, 438, 34, 25, C.white, true)
        text(s, d.factoryDetail, 64, 275, 438, 52, 22, C.gray)
        text(s, d.labHeading, 64, 354, 438, 28, 21, C.cyan, true)
        text(s, d.labDetail, 64, 393, 438, 55, 23, C.white)
        line(s, 530, 199, 530, 448)
        const h = box(s, d.labSteps[0], 568, 209, 230, 60, C.cyan, 21)
        const m = box(s, d.labSteps[1], 976, 209, 230, 60, C.cyan, 22)
        const dcn = box(s, d.labSteps[2], 976, 385, 230, 60, C.amber, 22)
        const a = box(s, d.labSteps[3], 568, 385, 230, 60, C.amber, 22)
        connect(s, h, m, C.cyan)
        connect(s, m, dcn, C.cyan, "bottom", "top")
        connect(s, dcn, a, C.amber, "left", "right")
        connect(s, a, h, C.amber, "top", "bottom")
        text(s, d.loopCenter, 622, 293, 526, 62, 24, C.white, true, "center")
        line(s, 64, 465, 1216, 465)
        text(s, d.teamHeading, 64, 475, 1152, 27, 19, C.cyan, true)
        d.ceremonies.forEach(([head, detail], i) => {
          const x = 64 + i * 293
          text(s, head, x, 509, 273, 25, 19, C.white, true)
          text(s, detail, x, 540, 273, 48, 18, C.gray)
        })
        line(s, 64, 599, 1216, 599)
        d.applications.forEach(([head, detail], i) => {
          text(s, head, 64, 609 + i * 30, 367, 26, 19, i ? C.amber : C.cyan, true)
          text(s, detail, 441, 609 + i * 30, 775, 26, 20, C.white)
        })
        text(s, d.takeaway, 64, 680, 1118, 28, 22, C.white, true)
        break
      }
      case "resources": {
        text(s, d.subtitle, 64, 182, 1152, 35, 25, C.gray)
        d.resources.forEach(([title, description, url, label], i) => {
          const x = 64 + i * 608
          text(s, title, x, 237, 544, 40, 29, i ? C.amber : C.cyan, true, "center")
          text(s, description, x, 281, 544, 56, 23, C.white, false, "center")
          const qr = i ? assets.qrSubprime : assets.qrUa
          if (!qr) throw new Error("Requested closing QR asset is required")
          s.images.add({
            blob: qr,
            contentType: "image/png",
            alt: `QR code: ${url}`,
            fit: "contain",
            position: { left: x + 164, top: 350, width: 216, height: 216 },
          })
          const prefix = text(
            s,
            "github.com/UncertaintyArchitectureGroup/",
            x,
            579,
            544,
            25,
            18,
            C.gray,
            false,
            "center",
          )
          prefix.text.get("github.com/UncertaintyArchitectureGroup/").link = {
            uri: url,
            isExternal: true,
          }
          const link = text(s, label, x, 608, 544, 28, 22, i ? C.amber : C.cyan, true, "center")
          link.text.get(label).link = { uri: url, isExternal: true }
        })
        line(s, 640, 237, 640, 636)
        line(s, 64, 653, 1216, 653)
        text(s, d.author, 64, 667, 236, 28, 21, C.white, true)
        const mail = text(s, d.email, 315, 667, 345, 28, 18, C.cyan)
        mail.text.get(d.email).link = { uri: `mailto:${d.email}`, isExternal: true }
        const link = text(s, d.linkedin, 676, 667, 478, 28, 17, C.cyan)
        link.text.get(d.linkedin).link = { uri: d.linkedin, isExternal: true }
        break
      }
      default:
        throw new Error(`Unknown layout ${d.layout}`)
    }
  }
  return deck
}
