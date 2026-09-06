#!/usr/bin/env node
// Assemble generated stills into a video: slow Ken Burns per still, crossfade between.
//   node assemble.mjs <scenes.json> <stillsDir> <out.mp4>
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

const [specPath, dir, out] = process.argv.slice(2);
if (!specPath || !dir || !out) { console.error('usage: assemble.mjs <scenes.json> <stillsDir> <out.mp4>'); process.exit(2); }
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const W = spec.width || 1080, H = spec.height || 1350, FPS = spec.fps || 30, T = spec.xfade ?? 0.7;

const shots = spec.scenes.map(s => ({ ...s, file: path.join(dir, `${s.id}.png`), dur: s.dur || 5 }))
  .filter(s => { if (!fs.existsSync(s.file)) { console.error(`  missing ${s.file}, skipping`); return false; } return true; });
if (!shots.length) { console.error('no stills to assemble'); process.exit(1); }

const args = ['-y', '-loglevel', 'error'];
// -framerate here + zoompan d=1 below: zoompan emits d frames PER INPUT frame, so any
// d > 1 on a looped still multiplies the duration. One in, one out, zoom driven by `on`.
for (const s of shots) args.push('-loop', '1', '-framerate', String(FPS), '-t', String(s.dur), '-i', s.file);

// Upscale before zoompan: it samples on an integer grid, so a bigger source hides the step.
const chains = shots.map((s, i) => {
  const frames = Math.max(2, Math.round(s.dur * FPS));
  const LO = 1.02, HI = 1.14, step = ((HI - LO) / (frames - 1)).toFixed(6);
  // alternate push-in / pull-out so consecutive scenes don't feel mechanical
  const z = i % 2 === 0
    ? `min(${LO}+${step}*on,${HI})`
    : `max(${HI}-${step}*on,${LO})`;
  return `[${i}:v]scale=${W * 2}:${H * 2}:force_original_aspect_ratio=increase,`
    + `crop=${W * 2}:${H * 2},`
    + `zoompan=z='${z}':d=1:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=${W}x${H}:fps=${FPS},`
    + `setsar=1,format=yuv420p[v${i}]`;
});

let filter = chains.join(';');
if (shots.length === 1) {
  filter += `;[v0]null[vout]`;
} else {
  let prev = 'v0', acc = shots[0].dur;
  shots.slice(1).forEach((s, k) => {
    const label = k === shots.length - 2 ? 'vout' : `x${k}`;
    filter += `;[${prev}][v${k + 1}]xfade=transition=fade:duration=${T}:offset=${(acc - T).toFixed(3)}[${label}]`;
    acc += s.dur - T;
    prev = label;
  });
}

args.push('-filter_complex', filter, '-map', '[vout]',
  '-c:v', 'libx264', '-preset', 'slow', '-crf', '19', '-pix_fmt', 'yuv420p',
  '-movflags', '+faststart', out);

fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true });
const total = shots.reduce((a, s) => a + s.dur, 0) - T * (shots.length - 1);
console.log(`  ${shots.length} stills · ${total.toFixed(1)}s · ${W}×${H} @ ${FPS}fps`);
execFileSync('ffmpeg', args, { stdio: 'inherit' });
console.log(`  ✓ ${out}  ${(fs.statSync(out).size / 1e6).toFixed(1)} MB`);
