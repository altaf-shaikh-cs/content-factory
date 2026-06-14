# LinkedIn Channel

The LinkedIn pipeline of the [content-stratergy](../README.md) multi-channel factory. Consumes ideas from the shared `../raw-ideas/` library and produces publish-ready LinkedIn posts + images.

---

## Folder layout

```
linkedin-posts/
├── README.md                        ← you are here
├── CLAUDE.md                        ← AI agent contract (LinkedIn-specific)
├── TODO.md                          ← queue + done ledger for this channel
├── performance/                     ← analytics feedback loop
│   ├── tracker.md                   ← rolling post performance ledger + pattern summary
│   ├── HOWTO.md                     ← how to export LinkedIn analytics CSV
│   └── csv-imports/                 ← drop LinkedIn CSV/XLSX exports here
└── posts/
    └── <slug>-<YYYYMMDD>/
        ├── 01-post-plan.md          ← Strategist output
        ├── 02a-draft-story-first.md ← Copywriter A
        ├── 02b-draft-claim-first.md ← Copywriter B
        ├── 02c-draft-<angle>.md     ← Copywriter C (adaptive angle, always present)
        ├── 03-editor-verdict.json   ← Editor round 1
        ├── 02-revised-draft.md      ← (only if revision round triggered)
        ├── 03-editor-verdict-final.json ← (only if revision round)
        ├── impact-1.svg             ← Image concept 1 (format selected by content type)
        ├── impact-2.svg             ← Image concept 2 (different format from concept 1)
        └── final-post.md            ← 👈 PUBLISH THIS
```

Source ideas live ONE FOLDER UP at `../raw-ideas/`. They are shared with the X, Blog, and Presentation channels.

---

## Pipeline

```
../raw-ideas/<NNN>-<slug>.md
        ↓
[Performance Agent — only if new CSV/XLSX in csv-imports/ or unscored performance.md]
        ↓
Strategist (reads tracker.md for performance context → 01-post-plan.md)
        ↓
3 Copywriters in parallel (A: story-first · B: bold claim-first · C: adaptive angle)
        ↓
Editor (scores all 3, picks winner, may request 1 revision — max 2 rounds)
        ↓
Image Designer — invokes /image-gen-agent TWICE:
  impact-1.svg  (style: stat-card-dark,      format: content-driven)
  impact-2.svg  (style: real-image-inspired, format: different from concept 1)
  Both carry @teachmebro handle in accent color
        ↓
posts/<slug>-<YYYYMMDD>/final-post.md   ← publish-ready
```

**LinkedIn image formats used (selected automatically by content type):**

| Format | Dimensions | When chosen |
|--------|------------|-------------|
| Square | 1080×1080 | Qualitative posts, opinion, minimal data — most versatile |
| Portrait | 1080×1350 | Stat-heavy posts (≥3 data points) |
| Landscape | 1200×627 | Post includes a URL/link |

The two concepts always use **different formats** to give real publishing options.

---

## Consumption model

`../raw-ideas/` is **immutable** — files never move. This LinkedIn channel tracks consumption via the **Done** section in [`TODO.md`](./TODO.md). The same idea can later be consumed by the X channel, the blog channel, etc. — those channels track independently in their own `TODO.md`.

A LinkedIn queue at runtime =
```
ls ../raw-ideas/  MINUS  filenames in TODO.md "Done" + "In Progress" sections
```

---

## Daily workflow

**Loop runs (see [`../linkedin.agent.md`](../linkedin.agent.md)):**
1. Computes queue
2. Picks oldest unconsumed idea
3. Triggers `/linkedin-growth-agent`
4. Updates `TODO.md` Done section

**You publish:**
1. Open `posts/<slug>-<date>/final-post.md`
2. Copy the "Final Post" section → paste into LinkedIn
3. Pick your image — `impact-1.svg` (Square) or `impact-2.svg` (Portrait) — based on where you're posting and device context
4. Export to PNG:
   ```bash
   brew install librsvg   # once
   rsvg-convert -w 1080 -h 1080 impact-1.svg -o impact-1.png   # square
   rsvg-convert -w 1080 -h 1350 impact-2.svg -o impact-2.png   # portrait
   ```
5. Attach PNG, ship.

---

## Re-running an idea on LinkedIn

Remove the idea's line from `TODO.md` Done section. Next loop tick will re-queue it.

## Restricting an idea to specific channels

In the raw idea file (`../raw-ideas/NNN-slug.md`), add frontmatter:
```yaml
---
channels: [linkedin]
---
```
Only listed channels will consume the idea. If frontmatter is absent, all channels can consume.

---

## The skill

Full pipeline contract: `.claude/skills/linkedin-growth-agent/SKILL.md`.
