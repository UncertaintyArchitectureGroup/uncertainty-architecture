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
        text(s, d.gitclearSource, 616, 446, 600, 28, 21, C.cyan, true)
        d.gitclearMetrics.slice(0, 2).forEach(([label, value], i) => {
          const y = 477 + i * 48
          text(s, label, 616, y, 391, 27, 22, C.white)
          text(s, value, 1007, y, 209, 27, 24, C.white, true, "right")
          text(s, d.gitclearDetails[i], 616, y + 27, 600, 21, 17, C.gray)
        })
        text(s, d.gitclearSecondary, 616, 574, 600, 22, 19, C.white)
        text(s, d.gitclearCaveat, 616, 598, 600, 20, 17, C.amber)
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
        text(s, "THINKING SYSTEMS", 64, 176, 1118, 28, 21, C.cyan, true)
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
        takeaway(s, d.takeaway)
        text(s, d.caption, 64, 608, 1152, 25, 19, C.gray)
        text(s, d.graphCaption, 64, 676, 1118, 24, 18, C.gray)
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
        text(s, d.roleDetail, 64, 400, 420, 45, 19, C.gray)
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
        text(s, d.envelopeHeading, 64, 482, 1152, 26, 20, C.amber, true)
        d.envelope.forEach((v, i) =>
          text(s, v, 64 + (i % 2) * 596, 513 + Math.floor(i / 2) * 28, 552, 26, 21, C.white),
        )
        text(s, d.specification, 64, 568, 1152, 28, 21, C.gray)
        text(s, d.gap, 64, 603, 1152, 27, 20, C.white)
        text(s, d.research, 64, 636, 1152, 25, 18, C.gray)
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
        text(s, d.ownershipLine, 64, 681, 1118, 27, 21, C.white, true)
        break
      }
      case "risk": {
        text(s, d.role, 64, 176, 1152, 32, 22, C.cyan, true)
        text(s, d.behavior, 64, 214, 1152, 28, 20, C.gray)
        const gates = table(s, d.table, 64, 249, 1152, 366, [115, 237, 500, 300], 18, 3)
        ;[38, 84, 56, 84, 104].forEach((h, i) => {
          gates.rows[i].height = h
        })
        text(s, d.syntax, 64, 620, 1152, 25, 20, C.amber)
        text(s, d.caption, 64, 648, 1152, 25, 19, C.gray)
        text(s, d.takeaway, 64, 675, 1118, 29, 25, C.white, true)
        break
      }
      case "control": {
        text(s, d.role, 64, 176, 1152, 32, 22, C.cyan, true)
        text(s, d.flowHeading, 64, 215, 368, 26, 18, C.gray, true)
        const reference = box(s, d.reference, 466, 219, 180, 38, C.gray, 17)
        const proposal = box(s, d.runtime[0], 64, 283, 148, 70, C.cyan, 21)
        const monitor = box(s, d.runtime[1], 250, 283, 176, 70, C.cyan, 20)
        const gate = box(s, d.runtime[2], 466, 283, 180, 70, C.amber, 20)
        const deliver = box(s, d.runtime[3], 706, 283, 150, 70, C.cyan, 21)
        connect(s, proposal, monitor, C.gray)
        connect(s, monitor, gate, C.gray)
        connect(s, reference, gate, C.gray, "bottom", "top")
        connect(s, gate, deliver, C.cyan)
        text(s, "PASS", 658, 286, 44, 22, 14, C.cyan, true)
        const stop = box(s, d.stop, 466, 389, 180, 62, C.red, 20)
        const fallback = box(s, d.fallback, 64, 389, 362, 62, C.amber, 19)
        connect(s, gate, stop, C.red, "bottom", "top")
        text(s, "BREACH / UNAVAILABLE", 466, 361, 180, 23, 13, C.red, true, "center")
        connect(s, stop, fallback, C.amber, "left", "right")
        const observe = box(s, d.observe, 706, 389, 150, 62, C.cyan, 18)
        connect(s, deliver, observe, C.cyan, "bottom", "top")
        line(s, 781, 451, 781, 479, C.cyan)
        line(s, 781, 479, 48, 479, C.cyan)
        line(s, 48, 479, 48, 318, C.cyan)
        const returnPoint = rect(s, 48, 317.5, 1, 1, "none", "none", 0)
        connect(s, returnPoint, proposal, C.cyan)
        text(s, d.feedback, 64, 485, 792, 39, 18, C.cyan)
        line(s, 884, 216, 884, 526)
        text(s, d.architectureHeading, 912, 215, 304, 26, 18, C.red, true)
        d.pressures.forEach(([head, detail], i) => {
          text(s, head, 912, 251 + i * 65, 304, 24, 20, C.white, true)
          text(s, detail, 912, 277 + i * 65, 304, 32, 17, C.gray)
        })
        text(s, d.veto, 912, 453, 304, 70, 19, C.red, true)
        line(s, 64, 534, 1216, 534)
        text(s, d.humanHeading, 64, 541, 1152, 25, 19, C.cyan, true)
        text(s, d.humanDetail, 64, 570, 1152, 26, 21, C.white)
        text(s, d.gate, 64, 604, 1152, 27, 19, C.gray)
        text(s, d.trialRule, 64, 637, 1152, 28, 20, C.amber)
        text(s, d.takeaway, 64, 678, 1118, 28, 24, C.white, true)
        break
      }
      case "roles": {
        text(s, d.role, 64, 176, 1152, 32, 22, C.cyan, true)
        text(s, d.foundation, 64, 216, 1152, 32, 22, C.white)
        text(s, "THREE OVERLAPPING HORIZONS", 64, 254, 1152, 26, 19, C.gray, true)
        const horizons = table(s, d.table, 64, 289, 1152, 310, [211, 490, 451], 20, 6)
        ;[40, 90, 90, 90].forEach((h, i) => {
          horizons.rows[i].height = h
        })
        text(s, d.statisticalLiteracy, 64, 613, 1152, 29, 21, C.amber)
        text(s, d.roleBoundary, 64, 647, 1152, 28, 20, C.gray)
        text(s, d.takeaway, 64, 682, 1118, 27, 23, C.white, true)
        break
      }
      case "synthesis": {
        text(s, d.factoryHeading, 64, 204, 460, 28, 21, C.gray, true)
        text(s, d.factoryFlow, 64, 248, 460, 35, 25, C.white, true)
        text(s, d.factoryDetail, 64, 294, 460, 58, 23, C.gray)
        text(s, d.labHeading, 64, 389, 460, 28, 21, C.cyan, true)
        text(s, d.labDetail, 64, 430, 460, 61, 24, C.white)
        line(s, 540, 207, 540, 491)
        const h = box(s, d.labSteps[0], 582, 220, 242, 68, C.cyan, 22)
        const m = box(s, d.labSteps[1], 954, 220, 242, 68, C.cyan, 24)
        const dcn = box(s, d.labSteps[2], 954, 414, 242, 68, C.amber, 24)
        const a = box(s, d.labSteps[3], 582, 414, 242, 68, C.amber, 24)
        connect(s, h, m, C.cyan)
        connect(s, m, dcn, C.cyan, "bottom", "top")
        connect(s, dcn, a, C.amber, "left", "right")
        connect(s, a, h, C.amber, "top", "bottom")
        text(s, d.loopCenter, 630, 318, 515, 67, 25, C.white, true, "center")
        line(s, 64, 513, 1216, 513)
        d.applications.forEach(([head, detail], i) => {
          const y = 526 + i * 66
          text(s, head, 64, y, 1152, 26, 20, i ? C.amber : C.cyan, true)
          text(s, detail, 64, y + 29, 1152, 28, 21, C.white)
        })
        text(s, d.takeaway, 64, 673, 1118, 31, 25, C.white, true)
        break
      }
      default:
        throw new Error(`Unknown layout ${d.layout}`)
    }
  }
  return deck
}
