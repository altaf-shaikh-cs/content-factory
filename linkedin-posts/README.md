# LinkedIn Channel

The LinkedIn pipeline of the [content-stratergy](../README.md) multi-channel factory. Consumes ideas from the shared `../raw-ideas/` library and produces publish-ready LinkedIn posts + images.

---

## Folder layout

```
linkedin-posts/
├── README.md                        ← you are here
├── CLAUDE.md                        ← AI agent contract (LinkedIn-specific)
├── TODO.md                          ← queue + done ledger for this channel
└── posts/
    └── <slug>-<YYYYMMDD>/
        ├── 01-post-plan.md          ← Strategist
        ├── 02a-draft-story-first.md ← Copywriter A
        ├── 02b-draft-claim-first.md ← Copywriter B
        ├── 02c-draft-<angle>.md     ← Copywriter C (if N≥3, adaptive)
        ├── 03-editor-verdict.json   ← Editor
        ├── 02-revised-draft.md      ← (only if revision round)
        ├── impact.svg               ← 1080×1350 LinkedIn image
        └── final-post.md            ← 👈 PUBLISH THIS
```

Source ideas live ONE FOLDER UP at `../raw-ideas/`. They are shared with the X, Blog, and Presentation channels.

---

## Pipeline

```
../raw-ideas/<NNN>-<slug>.md
        ↓
Strategist (plan)
        ↓
N Copywriters (parallel drafts — default N=2)
        ↓
Editor (scores, picks winner, may request 1 revision)
        ↓
Image Designer (1080×1350 SVG)
        ↓
posts/<slug>-<YYYYMMDD>/final-post.md   ← publish-ready
```

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
3. Export `impact.svg` → PNG (`rsvg-convert -w 1080 -h 1350 impact.svg -o impact.png`)
4. Attach PNG, ship.

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

Full pipeline contract: `~/.claude/skills/linkedin-growth-agent/SKILL.md`.
