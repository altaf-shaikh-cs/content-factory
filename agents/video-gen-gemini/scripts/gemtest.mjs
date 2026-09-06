#!/usr/bin/env node
// Gemini image-gen evaluation harness for the content factory.
// Usage:
//   node gemtest.mjs models
//   node gemtest.mjs gen <model> <promptFile> <out.png> [refImage]
import { requireKey } from './key.mjs';
import fs from 'node:fs';
import path from 'node:path';

const { key: KEY, source: KEYSRC } = requireKey();
const BASE = 'https://generativelanguage.googleapis.com/v1beta';
const cmd = process.argv[2];

if (cmd === 'models') {
  const r = await fetch(`${BASE}/models?key=${KEY}&pageSize=200`);
  if (!r.ok) { console.error(`HTTP ${r.status}: ${(await r.text()).slice(0, 400)}`); process.exit(1); }
  const { models = [] } = await r.json();
  const img = models.filter(m => /image/i.test(m.name));
  console.log(`${models.length} models visible to this key; ${img.length} image-capable:\n`);
  for (const m of img) {
    console.log(`  ${m.name.replace('models/', '')}`);
    console.log(`      ${m.displayName || ''}  |  methods: ${(m.supportedGenerationMethods || []).join(', ')}`);
  }
  process.exit(0);
}

if (cmd === 'gen') {
  const [, , , model, promptFile, out, ref] = process.argv;
  if (!model || !promptFile || !out) { console.error('gen <model> <promptFile> <out.png> [refImage]'); process.exit(2); }
  const parts = [{ text: fs.readFileSync(promptFile, 'utf8') }];
  if (ref) {
    const ext = path.extname(ref).toLowerCase();
    const mime = ext === '.png' ? 'image/png' : ext === '.webp' ? 'image/webp' : 'image/jpeg';
    parts.push({ inlineData: { mimeType: mime, data: fs.readFileSync(ref).toString('base64') } });
    console.log(`  conditioning on ${path.basename(ref)}`);
  }
  const t0 = Date.now();
  const r = await fetch(`${BASE}/models/${model}:generateContent?key=${KEY}`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ contents: [{ role: 'user', parts }] }),
  });
  const body = await r.text();
  if (!r.ok) { console.error(`  HTTP ${r.status}: ${body.slice(0, 600)}`); process.exit(1); }
  const j = JSON.parse(body);
  const cand = j.candidates?.[0];
  const imgPart = cand?.content?.parts?.find(p => p.inlineData);
  const txtPart = cand?.content?.parts?.filter(p => p.text).map(p => p.text).join(' ');
  if (!imgPart) {
    console.error(`  no image returned. finishReason=${cand?.finishReason}`);
    if (txtPart) console.error(`  model said: ${txtPart.slice(0, 300)}`);
    process.exit(1);
  }
  fs.writeFileSync(out, Buffer.from(imgPart.inlineData.data, 'base64'));
  const kb = (fs.statSync(out).size / 1024).toFixed(0);
  console.log(`  ✓ ${out}  ${kb} KB  ${((Date.now() - t0) / 1000).toFixed(1)}s  (${j.usageMetadata?.totalTokenCount ?? '?'} tok)`);
  process.exit(0);
}
console.error('commands: models | gen');
process.exit(2);
