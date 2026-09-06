#!/usr/bin/env node
// Deterministic explainer-video renderer.
//   node render.mjs <spec.json> <out.mp4>            full render
//   node render.mjs <spec.json> <out.png> --contact  one contact sheet, ~2s per render
//   node render.mjs <spec.json> <out.png> --still 12.5
//
// The browser is a pure function from time to picture: every animation is paused
// on one shared timeline and seeked frame by frame. Two renders are byte-identical.
import { chromium } from 'playwright-core';
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const SCENE = path.join(HERE, 'scene.html');

function findChrome() {
  if (process.env.CHROME_PATH) return process.env.CHROME_PATH;
  const cache = path.join(process.env.HOME, 'Library/Caches/ms-playwright');
  if (fs.existsSync(cache)) {
    const dirs = fs.readdirSync(cache).filter(d => /^chromium-\d+$/.test(d))
      .sort((a, b) => +b.split('-')[1] - +a.split('-')[1]);
    for (const d of dirs) {
      for (const app of ['Google Chrome for Testing', 'Chromium']) {
        const p = path.join(cache, d, 'chrome-mac-arm64', `${app}.app/Contents/MacOS/${app}`);
        if (fs.existsSync(p)) return p;
      }
    }
  }
  const sys = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
  if (fs.existsSync(sys)) return sys;
  throw new Error('No Chromium found. Set CHROME_PATH or run: npx playwright install chromium');
}

const [specPath, outPath] = process.argv.slice(2);
if (!specPath || !outPath) { console.error('usage: render.mjs <spec.json> <out.mp4|out.png> [--contact | --still <sec>]'); process.exit(2); }
const contact = process.argv.includes('--contact');
const stillIdx = process.argv.indexOf('--still');
const still = stillIdx > -1 ? parseFloat(process.argv[stillIdx + 1]) : null;

const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const outDir = path.dirname(path.resolve(outPath));
fs.mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch({ executablePath: findChrome() });
const page = await browser.newPage({ viewport: { width: spec.width, height: spec.height }, deviceScaleFactor: 1 });
page.on('pageerror', e => { console.error('  scene.html error:', e.message); });
await page.goto('file://' + SCENE);
const total = await page.evaluate(s => window.build(s), spec);
console.log(`  ${spec.scenes.length} scenes · ${total.toFixed(1)}s · ${spec.width}×${spec.height} @ ${spec.fps}fps`);

// --- preview modes: cheap, for iterating on layout before committing to a full render
if (still !== null) {
  await page.evaluate(t => window.seek(t), still);
  await page.screenshot({ path: outPath });
  await browser.close();
  console.log(`  ✓ still @ ${still}s → ${outPath}`);
  process.exit(0);
}
if (contact) {
  const tmp = fs.mkdtempSync(path.join(outDir, '.contact-'));
  const shots = [];
  // mid-point of each scene, where it is fully settled
  let t0 = 0;
  for (const sc of spec.scenes) {
    const t = t0 + sc.dur * 0.78;
    await page.evaluate(x => window.seek(x), t);
    const p = path.join(tmp, `${shots.length.toString().padStart(2, '0')}.png`);
    await page.screenshot({ path: p });
    shots.push(p);
    t0 += sc.dur;
  }
  await browser.close();
  const cols = Math.min(4, shots.length);
  execFileSync('magick', ['montage', ...shots, '-tile', `${cols}x`, '-geometry', '360x450+8+8',
    '-background', '#111827', outPath], { stdio: 'inherit' });
  fs.rmSync(tmp, { recursive: true, force: true });
  console.log(`  ✓ contact sheet (${shots.length} scenes) → ${outPath}`);
  process.exit(0);
}

// --- full render
const frameDir = path.join(outDir, '.frames');
fs.rmSync(frameDir, { recursive: true, force: true });
fs.mkdirSync(frameDir, { recursive: true });
const frames = Math.round(total * spec.fps);
const t0 = Date.now();
for (let i = 0; i < frames; i++) {
  await page.evaluate(t => window.seek(t), i / spec.fps);
  await page.screenshot({ path: path.join(frameDir, String(i).padStart(5, '0') + '.png') });
  if (i % 60 === 0) process.stdout.write(`\r  capturing ${i}/${frames}`);
}
await browser.close();
console.log(`\r  ${frames} frames in ${((Date.now() - t0) / 1000).toFixed(0)}s        `);

execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(spec.fps),
  '-i', path.join(frameDir, '%05d.png'),
  '-c:v', 'libx264', '-preset', 'slow', '-crf', '19', '-pix_fmt', 'yuv420p',
  '-movflags', '+faststart', outPath], { stdio: 'inherit' });
fs.rmSync(frameDir, { recursive: true, force: true });
console.log(`  ✓ ${outPath}  ${(fs.statSync(outPath).size / 1e6).toFixed(1)} MB  ${total.toFixed(1)}s`);
