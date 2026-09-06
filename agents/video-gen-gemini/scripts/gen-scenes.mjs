#!/usr/bin/env node
// Generate one illustrated still per scene with a Gemini image model.
//   node gen-scenes.mjs <scenes.json> <outDir>
// Reads GEMINI_API_KEY (or GOOGLE_API_KEY) from the environment.
import { requireKey } from './key.mjs';
import fs from 'node:fs';
import path from 'node:path';

const { key: KEY, source: KEYSRC } = requireKey();
const BASE = 'https://generativelanguage.googleapis.com/v1beta';

const [specPath, outDir] = process.argv.slice(2);
if (!specPath || !outDir) { console.error('usage: gen-scenes.mjs <scenes.json> <outDir>'); process.exit(2); }
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const model = spec.model || 'gemini-3-pro-image-preview';
fs.mkdirSync(outDir, { recursive: true });

// A style reference is worth more than any amount of adjectives.
let ref = null;
if (spec.style) {
  const ext = path.extname(spec.style).toLowerCase();
  ref = {
    inlineData: {
      mimeType: ext === '.png' ? 'image/png' : ext === '.webp' ? 'image/webp' : 'image/jpeg',
      data: fs.readFileSync(spec.style).toString('base64'),
    },
  };
}

const NO_TEXT = '\n\nCRITICAL: render NO text, letters, numbers, words, labels or logos anywhere in the image. Illustration only.';
const TEXT_OK = '\n\nRender the quoted text exactly as written, spelled correctly, as the dominant element. No other text.';

async function gen(scene, attempt = 1) {
  const parts = [{
    text: `${spec.styleNote ? spec.styleNote + '\n\n' : ''}${scene.prompt}${spec.mode === 'art' ? NO_TEXT : TEXT_OK}`,
  }];
  if (ref) parts.push(ref);
  const body = {
    contents: [{ role: 'user', parts }],
    generationConfig: spec.aspect ? { imageConfig: { aspectRatio: spec.aspect } } : undefined,
  };
  const r = await fetch(`${BASE}/models/${model}:generateContent?key=${KEY}`, {
    method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body),
  });
  const txt = await r.text();
  if (!r.ok) {
    // Older image models reject imageConfig; drop it once and retry.
    if (attempt === 1 && spec.aspect && /imageConfig|aspectRatio|Unknown name/i.test(txt)) {
      delete spec.aspect;
      return gen(scene, 2);
    }
    throw new Error(`HTTP ${r.status}: ${txt.slice(0, 400)}`);
  }
  const cand = JSON.parse(txt).candidates?.[0];
  const img = cand?.content?.parts?.find(p => p.inlineData);
  if (!img) throw new Error(`no image (finishReason=${cand?.finishReason})`);
  return Buffer.from(img.inlineData.data, 'base64');
}

let failed = 0;
for (const scene of spec.scenes) {
  const out = path.join(outDir, `${scene.id}.png`);
  process.stdout.write(`  ${scene.id} ... `);
  try {
    const t0 = Date.now();
    fs.writeFileSync(out, await gen(scene));
    console.log(`✓ ${(fs.statSync(out).size / 1024).toFixed(0)} KB  ${((Date.now() - t0) / 1000).toFixed(1)}s`);
  } catch (e) { console.log(`✗ ${e.message}`); failed++; }
}
console.log(failed ? `\n  ${failed} scene(s) failed — rerun or reword those prompts` : `\n  all ${spec.scenes.length} scenes generated → ${outDir}`);
process.exit(failed ? 1 : 0);
