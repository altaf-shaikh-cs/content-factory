# video-gen agent

Project-side home for the **deterministic** explainer-video agent. Produces silent, text-exact motion-graphics videos for any channel.

There is a second, different video agent: [`../video-gen-gemini/`](../video-gen-gemini/AGENT.md). Read [Which agent do I want?](#which-agent-do-i-want) before picking.

---

## Global skill

The agent brain (brief contract, scene planning, layout selection) lives at:

```
.claude/skills/video-gen-agent/SKILL.md
```

Edit that file to change how the agent behaves. This folder holds the renderer it drives.

---

## What this agent does

1. Reads a channel's `final-post.md` (or a `[VIDEO BRIEF]`)
2. Breaks the argument into 5-8 scenes
3. Writes a `spec.json` naming a layout and content per scene
4. Renders it to MP4 through a headless browser

No model is called at render time. The video is a pure function of the spec, so two renders of the same spec are byte-identical.

---

## Toolchain

| Stage | Tool | Notes |
|-------|------|-------|
| Author the spec | Claude | the only creative step |
| Lay out + animate | headless Chromium | HTML/CSS + Web Animations API, no animation library |
| Drive + capture | `playwright-core` | the sole npm dependency |
| Encode | `ffmpeg` | H.264, `yuv420p`, `+faststart` |
| Review | `magick montage` | contact sheets |

**Setup** (once): `cd renderer && npm install`. Chromium is reused from the Playwright browser cache if present; otherwise set `CHROME_PATH` or run `npx playwright install chromium`.

---

## Folder layout

```
agents/video-gen/
├── AGENT.md              ← this file
├── renderer/
│   ├── scene.html        ← layout + animation library (edit to add a layout)
│   ├── render.mjs        ← capture + encode
│   └── package.json
└── specs/
    └── example-token-usage-spike.json   ← reference spec, 7 scenes
```

---

## Running it

```bash
R=agents/video-gen/renderer

# fast: one image of every scene at its settled moment (~5s) — ALWAYS do this first
node $R/render.mjs <spec.json> /tmp/contact.png --contact

# fast: a single frame at an exact second
node $R/render.mjs <spec.json> /tmp/t12.png --still 12.5

# full render (~1176 frames for a 39s video)
node $R/render.mjs <spec.json> <post-folder>/explainer.mp4
```

Iterate on the contact sheet. Only run the full render once the layout is right.

---

## Spec format

```jsonc
{
  "width": 1080, "height": 1350, "fps": 30,
  "brand": { "domain": "AI ENGINEERING", "handle": "@teachmebro" },
  "scenes": [ { "layout": "...", "dur": 4.6, /* layout-specific fields */ } ]
}
```

`dur` is seconds. Total runtime is the sum. Inline HTML is allowed in text fields — use
`<span class="amber">`, `<span class="cyan">`, `<span class="dim">` to colour a phrase, and `<br>` to break a line.

### Layouts

| Layout | Fields | Use for |
|--------|--------|---------|
| `title` | `eyebrow?`, `lines[]`, `rule?`, `sub?`, `small?` | opening, closing, act breaks |
| `stats` | `title`, `cards[{value,label}]`, `sub?` | two numbers in contrast; values count up |
| `bars` | `eyebrow?`, `title`, `bars[{h,slab?}]`, `xlabels[2]`, `punch?` | growth, accumulation, before/after |
| `formula` | `title`, `parts[{t,k?}]`, `punch?`, `sub?` | an equation assembling term by term |
| `list` | `eyebrow?`, `title`, `items[{t,s?}]` | 2-3 takeaways or fixes |

`bars`: `h` is total height 0-1; `slab` is the amber fraction **of that bar**. To hold a
constant quantity while the total grows, keep `h × slab` equal across bars. That is the
whole argument in the reference spec: 21k tokens re-sent in every call while context triples.

`formula` `k`: `op` (grey operator), `hl` (amber), `hl2` (cyan).

### Adding a layout

Add a function to the `LAYOUT` object in `scene.html` with signature `(sceneEl, sc, t0, dur)`.
Build DOM with `mk(tag, class, html)`, animate with `A(el, keyframes, absoluteStart, dur)`,
and use `count(el, from, to, at, dur)` for a number that ticks up. All timing is absolute
seconds on the global timeline; `t0` is when the scene starts.

---

## Conventions

- **Silent.** LinkedIn autoplays muted; the text carries the message.
- **1080×1350** portrait by default, matching the image agent's LinkedIn default.
- **30-45s.** Long enough to explain, short enough to finish.
- **Palette matches the image agent** (`#0a0e1a`, amber `#f59e0b`, cyan `#22d3ee`), so
  video and stills read as one brand.
- Output lands in the post folder as `explainer.mp4`.

---

## Which agent do I want?

| | `video-gen` (this one) | [`video-gen-gemini`](../video-gen-gemini/AGENT.md) |
|---|---|---|
| Output | motion graphics, animated text and charts | illustrated stills, animated by camera move |
| Text fidelity | exact, it is real DOM text | model-rendered, must be proofread |
| Determinism | byte-identical re-renders | different every run |
| Needs network / key | no | yes, `GEMINI_API_KEY` |
| Cost | free | per image |
| Best for | data, mechanisms, numbers, formulas | tonal, editorial, metaphor, story |

Data-dense post: use this agent. Tonal or narrative post: try the Gemini one.
