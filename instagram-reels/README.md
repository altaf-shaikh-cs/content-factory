# Instagram Reels Channel

The Instagram pipeline of the [content-factory](../README.md) multi-channel factory. Consumes ideas from the shared `../raw-ideas/` library and produces **reel suggestions + publish-ready shooting scripts + cover frames**.

---

## What's different about this channel

LinkedIn and X each take the **oldest single unconsumed idea** and turn it into one post. **Instagram doesn't work that way.** A reel is often *more* than one idea, and the best reels come from patterns that live *between* ideas. So this channel **mines the whole library** and suggests three kinds of reels:

| Reel type | Sources | Example |
|-----------|---------|---------|
| **Direct** | 1 raw idea | "I tested Claude vs Codex on the same task" |
| **Combo** | several related ideas merged | "Build an AI agent team in 60 seconds" (from two agent-team ideas) |
| **Pattern** | a theme derived ACROSS ideas, in no single file | "5 signs you're building AI agents the hard way" |

Because one idea can fuel many reels, **ideas are never "used up."** No subtractive queue — we track produced reels and coverage instead.

---

## Folder layout

```
instagram-reels/
├── README.md                        ← you are here
├── CLAUDE.md                        ← AI agent contract (Instagram-specific)
├── PLAYBOOK.md                      ← Reels best-practices; craft baseline (read every run)
├── reel-map.md                      ← living menu of reel candidates (refreshed every run)
├── TODO.md                          ← In Progress + Produced + Parked ledger
└── reels/
    └── <reel-slug>-<YYYYMMDD>/
        ├── 00-reel-brief.md             ← chosen candidate + sources + cross-channel signal
        ├── 01-reel-plan.md              ← Strategist (style + format + beats + angles)
        ├── 02a-script-demo.md           ← Scriptwriter 1 — Demo / how-to
        ├── 02b-script-hottake.md        ← Scriptwriter 2 — Hot-take / POV
        ├── 02c-script-story.md          ← Scriptwriter 3 — Story / build-in-public (N=3)
        ├── 03-editor-verdict.json       ← Editor round 1
        ├── 02-revised-script.md         ← (only if revision round)
        ├── cover-1.svg                  ← 9:16 reel cover
        ├── cover-2.svg                  ← 4:5 grid-safe cover
        └── reel-script.md               ← 👈 SHOOT THIS
```

Source ideas live ONE FOLDER UP at `../raw-ideas/`, shared with LinkedIn, X, Blog, and Presentation.

---

## Pipeline

```
../raw-ideas/  (the WHOLE library)
        ↓
Scout / Pattern-Miner  (reads every idea + LinkedIn/X signal read-only → reel-map.md)
        ↓  pick top unproduced candidate (by reel-worthiness score)
Reel Brief (sources + cross-channel signal → 00-reel-brief.md)
        ↓
Reel Strategist (decides FACELESS vs ON-CAMERA, format, length, beats → 01-reel-plan.md)
        ↓
3 Scriptwriters in parallel (1: demo/how-to · 2: hot-take/POV · 3: story/build-in-public)
        ↓
Editor (scores hook/retention/payoff/clarity/CTA; hard-fails weak hook, no payoff, non-shareable CTA — max 2 rounds)
        ↓
Cover Designer — /image-gen-agent (Channel: instagram) ×2:
  cover-1.svg (1080×1920, 9:16)
  cover-2.svg (1080×1350, 4:5)
        ↓
reels/<reel-slug>-<YYYYMMDD>/reel-script.md   ← publish-ready shooting script
```

---

## Run modes

| You want... | Command |
|-------------|---------|
| Just see reel ideas | "suggest reels" → refreshes & prints `reel-map.md`, scripts nothing |
| Ideas + script the best one | `/instagram-reels-agent` (default) |
| Script a specific candidate / topic | `/instagram-reels-agent <reel id or topic>` |
| 2 angles instead of 3 | `/instagram-reels-agent 2` |

---

## Daily workflow

**Loop runs (see [`../instagram.agent.md`](../instagram.agent.md)):**
1. Refreshes `reel-map.md` over the whole library
2. Picks the top unproduced candidate
3. Scripts it end-to-end
4. Updates `TODO.md` Produced + map coverage

**You shoot:**
1. Open `reels/<reel-slug>-<date>/reel-script.md`
2. Follow the **Shooting Script** table — record each beat (on-screen text + spoken/VO + visual)
3. Use the named **audio** (trending or original VO) and the **caption + hashtags**
4. Pick a cover — `cover-1.svg` (9:16) or `cover-2.svg` (4:5) — export to PNG:
   ```bash
   brew install librsvg   # once
   rsvg-convert -w 1080 -h 1920 cover-1.svg -o cover-1.png    # 9:16
   rsvg-convert -w 1080 -h 1350 cover-2.svg -o cover-2.png    # 4:5
   ```
5. Edit, set the cover, ship.

---

## The skill & the playbook

- Generation pipeline: `.claude/skills/instagram-reels-agent/SKILL.md`
- Craft baseline: [`PLAYBOOK.md`](./PLAYBOOK.md)

> **No performance loop — the playbook is its replacement.** Like the X channel, there's no analytics export, so the [`PLAYBOOK.md`](./PLAYBOOK.md) encodes what's known about Reels (hook in 1-2s, retention, audio, save/share triggers, a rookie-mistake checklist). The Scout, Strategist, Scriptwriters, and Editor all read it every run.

---

## Restricting an idea to specific channels

In the raw idea file, add frontmatter:
```yaml
---
channels: [instagram]
---
```
Only listed channels consume the idea. Absent frontmatter = all channels.
