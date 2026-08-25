import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
const root=path.resolve(fileURLToPath(new URL("../..",import.meta.url)));
const pub=readFileSync(path.join(root,"content/research/notes/thinking-systems-publication-draft.md"),"utf8");
const man=readFileSync(path.join(root,"content/research/notes/open-engineering-specification-article-draft.md"),"utf8");
const bp=readFileSync(path.join(root,"content/research/notes/open-engineering-specification-article-blueprint.md"),"utf8");
function fig(src,n,title=""){const re=new RegExp("```mermaid\\n((?:(?!```)[\\s\\S])*?)\\n```\\n\\n\\*\\*Figure "+n+" —([^\\n]+)","g");const ms=[...src.matchAll(re)].filter(m=>!title||m[2].includes(title));assert.equal(ms.length,1);return ms[0][1];}
function f3(src){const m=fig(src,3,"controlled-object shift");assert.match(m,/^flowchart TB/m);assert.match(m,/subgraph ROW3\[" "\][\s\S]*direction LR/);assert.match(m,/subgraph A\["Explicitly Authored Software[\s\S]*direction TB/);assert.match(m,/subgraph B\["Motivating runtime-judgment class[\s\S]*direction TB/);assert.match(m,/A2 ~~~ J1/);}
function ortho(src,n){const m=fig(src,n,"Two orthogonal models");assert.match(m,/^flowchart TB/m);assert.match(m,/subgraph ROW_ORTHO\[" "\][\s\S]*direction LR/);assert.match(m,/subgraph L\["Decision ownership/);assert.match(m,/subgraph F\["Capability functions/);assert.match(m,/subgraph CAP_TOP\[" "\][\s\S]*direction LR/);assert.match(m,/subgraph CAP_BOTTOM\[" "\][\s\S]*direction LR/);assert.match(m,/initial admissibility \+ assessment eligibility/);assert.match(m,/specific Bounded Research Authorization/);assert.match(m,/Business Authorization or changed basis/);assert.match(m,/applicable Project Authorization scope \/ set/);assert.match(m,/research-only and\/or production-capable/);assert.match(m,/realization \/ experiment evidence/);assert.match(m,/risk \/ feasibility \/ Model Judgment necessity/);assert.match(m,/Exogenous Organizational change/);assert.doesNotMatch(m,/classDef railpoint|\bJ2\b|\bJ3\b|\bJ4\b/);}
test("Figure 3 stays as two top-down columns side by side",()=>{f3(pub);f3(man);});
test("orthogonal model stays as two side-by-side panels",()=>{ortho(pub,8);ortho(man,9);});
test("blueprint owns the structural layout contract",()=>{assert.match(bp,/outer row subgraph `ROW3` with `direction LR`/);assert.match(bp,/`ROW_ORTHO` subgraph with `direction LR`/);assert.match(bp,/two horizontal rows \(`CAP_TOP`, `CAP_BOTTOM`\)/);});
