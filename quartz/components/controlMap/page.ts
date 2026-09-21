/** Standalone page keeps the map renderer off ordinary article pages. */
export const controlMapPage = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Explore the documents, terminology, ownership and review relationships of Uncertainty Architecture.">
<title>Repository Control Map · Uncertainty Architecture</title><link rel="stylesheet" href="map.css">
<script type="module" src="map.js"></script></head>
<body><a class="skip" href="#map-controls">Skip to map controls</a>
<header><div><a class="brand" href="../">UA / UNCERTAINTY ARCHITECTURE</a><h1>Repository Control Map</h1><p class="intro">Find the source. Follow the relationships. Understand what a change touches.</p></div><a class="repository" href="https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture">Open repository ↗</a></header>
<main><div class="statusbar"><span id="source-state">Loading repository snapshot…</span><span id="counts"></span></div>
<p id="load-error" role="alert" hidden></p>
<noscript>This map needs JavaScript. Read the repository through the source link above.</noscript>
<nav class="lenses" aria-label="Map mode"><button data-lens="explore" aria-pressed="true">01 <strong>Explore</strong></button><button data-lens="architecture" aria-pressed="false">02 <strong>Architecture</strong></button><button data-lens="impact" aria-pressed="false">03 <strong>Impact</strong></button><button data-lens="diagnostics" aria-pressed="false">04 <strong>Diagnostics</strong></button></nav>
<p id="lens-description">Browse the immediate neighbourhood of a document or term.</p>
<div class="workspace">
<aside id="map-controls" class="controls" aria-label="Map controls"><label for="search">Find a document or term</label><input id="search" type="search" placeholder="Search names, paths, terms…" autocomplete="off"><div id="search-results" class="search-results" aria-label="Search results"></div>
<details><summary>Filter the view</summary><div class="filter-grid">
<label>Module<select id="module"><option value="">All modules</option></select></label>
<label>Node type<select id="family"><option value="">All types</option></select></label>
<label>Document status<select id="status"><option value="">All statuses</option></select></label>
<label>Boundary<select id="boundary"><option value="">All boundaries</option><option value="framework">Framework</option><option value="research">Research</option><option value="repository">Repository / supporting</option></select></label>
<label>Relation<select id="relation"><option value="">All relations</option></select></label>
<label>Edge class<select id="edge-class"><option value="">All classes</option></select></label>
<label>Impact role<select id="impact-role"><option value="">All roles</option></select></label>
</div><button id="reset-filters" class="text-button">Reset filters</button></details>
<div class="view-options"><label><input id="global" type="checkbox"> Whole repository</label><label>Neighbourhood<select id="depth"><option value="1">1 hop</option><option value="2">2 hops</option></select></label><label><input id="extras" type="checkbox"> Include supporting files</label><label><input id="controls" type="checkbox"> Expand control links</label></div>
<div class="legend"><span><i class="document"></i>Document</span><span><i class="term"></i>Term</span><span><i class="responsibility"></i>Responsibility</span><span><i class="control"></i>Control</span><span><i class="research"></i>Research item</span></div>
</aside>
<section class="canvas-panel" aria-label="Graph and visible records"><div class="graph-tools"><span id="visible-count" aria-live="polite"></span><div><button id="zoom-out" aria-label="Zoom out">−</button><button id="zoom-in" aria-label="Zoom in">+</button><button id="fit">Fit</button></div></div><div id="graph" role="img" aria-label="Interactive repository graph. Use the visible records list for keyboard navigation."></div><p id="view-note" class="view-note"></p><details id="record-list"><summary>Visible records · keyboard navigation</summary><div id="visible-records"></div><div id="visible-edges"></div></details><section id="diagnostics" hidden aria-label="Diagnostic results"></section></section>
<aside class="inspector" aria-label="Source and relationship inspector"><div class="eyebrow">SELECTED RECORD</div><div id="inspector"><p>Select a node, a connection, or a search result.</p></div></aside>
</div>
<footer><p><strong>Read the owning source before deciding.</strong> Links and ranking help navigation; they do not establish authority. Impact shows only relationships represented by this projection.</p><details><summary>Snapshot and live state</summary><div id="identity"></div><p>Live PR overlay: unavailable. Selected-artifact impact uses this snapshot. Proposed PR graphs and current reviews/checks are not connected.</p></details></footer>
</main></body></html>`
