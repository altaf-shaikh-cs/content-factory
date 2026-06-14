---
name: linkedin-growth-agent
description: "Daily-loop LinkedIn post factory inside a multi-channel content factory. Reads ideas from a SHARED ../raw-ideas/ library (immutable) and writes LinkedIn-specific outputs into ./linkedin-posts/. Each run picks the oldest unconsumed idea (queue = ls raw-ideas/ minus this channel's TODO.md Done section), runs a 3-agent pipeline (Strategist → N Copywriters → Editor) + an Image Designer, saves every handoff to a per-post folder, and updates TODO.md. The source idea NEVER moves — it stays in the shared library so other channels (X, blog, presentation) can also consume it. If no unconsumed ideas exist for LinkedIn, the run exits quietly. Use when user says /linkedin-growth-agent, 'write a LinkedIn post', 'draft a post about X', 'process my LinkedIn ideas', or when invoked via /loop. Always trigger this skill."
trigger: /linkedin-growth-agent
---

# /linkedin-growth-agent

A daily-loop LinkedIn post factory. The user keeps dropping raw ideas into a folder; each invocation processes ONE new idea end-to-end (or no-ops if there are none).

**Default variations per post: 3. Override with `/linkedin-growth-agent 2` to use 2 variants for this run.**

---

## Project folder layout (canonical)

This skill operates inside a multi-channel content factory. The raw idea library is SHARED with other channels (X, blog, presentation) and lives ONE FOLDER UP from the LinkedIn channel folder. LinkedIn-specific outputs are isolated to `./linkedin-posts/`.

```
content-stratergy/                          ← project root
├── raw-ideas/                              ← SHARED, immutable, read-only from this skill
│   ├── 001-<slug>.md                       ← raw idea files (.md or .txt)
│   └── 002-<slug>.md
├── linkedin.agent.md                       ← daily /loop prompt (calls this skill)
└── linkedin-posts/                         ← LinkedIn channel folder (this skill writes here)
    ├── README.md
    ├── CLAUDE.md
    ├── TODO.md                             ← Queue + In Progress + Done sections
    ├── performance/                        ← analytics feedback loop
    │   ├── tracker.md                      ← rolling ledger: one row per post, patterns summary
    │   ├── HOWTO.md                        ← instructions for exporting LinkedIn CSV
    │   └── csv-imports/                    ← drop LinkedIn CSV exports here
    │       └── processed/                  ← Agent 0 moves CSVs here after parsing
    └── posts/                              ← one folder per generated post
        └── <slug>-<YYYYMMDD>/
            ├── 01-post-plan.md
            ├── 02a-draft-story-first.md
            ├── 02b-draft-claim-first.md
            ├── 02c-draft-<angle-slug>.md       (if N≥3; slug = adaptive angle name)
            ├── 02d-draft-<angle-slug>.md       (if N=4; slug = adaptive angle name)
            ├── 03-editor-verdict.json
            ├── 02-revised-draft.md             (if revision round)
            ├── 03-editor-verdict-final.json    (if revision round)
            ├── impact-1.svg
            ├── impact-2.svg
            ├── exports/
            │   ├── impact-1.png                ← auto-converted by image-gen-agent
            │   └── impact-2.png
            ├── performance.md                  ← written by Agent 0 after CSV import or manual entry
            └── final-post.md
```

**`../raw-ideas/` is immutable.** Never move, rename, or delete files in it — it's the shared library for all channels. Consumption is tracked in `./linkedin-posts/TODO.md` Done section.

**Bootstrap on first run:** if `./linkedin-posts/` doesn't exist, create `linkedin-posts/posts/` and an empty `TODO.md` (template below). If `../raw-ideas/` doesn't exist, create it as well. Then tell the user where to drop ideas and exit.

---

## Step 0 — Compute the queue and pick the idea

**Mode A — Loop / autonomous run** (no idea content passed in args, or invoked via `/loop`):

1. List files in `../raw-ideas/` (relative to `./linkedin-posts/`). Accept `.md` and `.txt`.
2. Read `./linkedin-posts/TODO.md`. Extract the filenames listed in the **Done** section and the **In Progress** section.
3. Compute the LinkedIn queue:
   ```
   queue = (files in ../raw-ideas/) MINUS (Done filenames) MINUS (In Progress filenames)
   ```
4. Filter the queue: drop any file whose frontmatter declares `channels: [...]` without `"linkedin"` in the list.
5. If queue is empty → print one line: `No new LinkedIn ideas. Skipping.` and exit. **Do not generate anything.**
6. Otherwise pick the **oldest by filename sort** (lexical — so `001-` runs before `002-`).
7. Read the chosen file. Its full content (minus frontmatter) is the **raw idea**.
8. Derive `<slug>` from the filename (strip extension AND any numeric prefix, kebab-case it).

**Mode B — Direct invocation with content in args** (user typed `/linkedin-growth-agent <idea text>`):

1. Treat the args as the raw idea.
2. Derive `<slug>` from the first 3-5 meaningful words.
3. Determine the next available numeric prefix in `../raw-ideas/` (e.g. if 001–005 exist, use 006).
4. Write the raw idea to `../raw-ideas/<NNN>-<slug>.md` so other channels can also consume it later. Then continue.

**N parsing:** if the args start with a small integer (e.g. `/linkedin-growth-agent 3 ...`), that's N. Otherwise N=2. Max N=4.

If the idea is too vague to plan around, ask ONE clarifying question. Otherwise start immediately.

Create the per-post folder: `./linkedin-posts/posts/<slug>-<YYYYMMDD>/`.
Update `./linkedin-posts/TODO.md`: move this idea's filename to **In Progress** with the date.

---

## Pipeline overview

```
[On every run — before picking an idea]
LinkedIn Performance Agent (conditional) → performance.md per post + tracker.md update
    ↓ (only runs if csv-imports/ has unprocessed files OR performance.md awaiting verdict)

[Raw Idea from ../raw-ideas/<NNN>-<slug>.md]
    ↓
Strategist (once)           → 01-post-plan.md  (reads tracker.md for context)
    ↓
Copywriters × N (parallel)  → 02a..02d-draft-*.md
    ↓
Editor                      → 03-editor-verdict.json
    ↓ if needs_revision AND round < 2
Copywriter (winner)         → 02-revised-draft.md
    ↓
Editor (final verdict)      → 03-editor-verdict-final.json
    ↓
Image Designer (/image-gen-agent × 2) → impact-1.svg, impact-2.svg
    ↓
[FINAL OUTPUT]              → final-post.md
    ↓
DO NOT touch ../raw-ideas/  (immutable, shared with other channels)
Update ./linkedin-posts/TODO.md: move filename from In Progress → Done with link to post folder
```

Max revision rounds: **2**.

---

## LinkedIn Performance Agent (conditional, runs before idea selection)

**Skill:** `linkedin-performance-agent` (extends `performance-marketing-agent`)
**Full spec:** `.claude/skills/linkedin-performance-agent/SKILL.md` — read it for the complete LinkedIn algorithm signals, CSV parsing spec, engagement type breakdowns, and verdict format. This section is the trigger contract only.

**Run this agent if ANY of the following is true:**
- `./linkedin-posts/performance/csv-imports/` contains `.csv` or `.xlsx` files (not in `processed/`)
- Any post folder in `./linkedin-posts/posts/` contains a `performance.md` with metrics filled in but no `## Agent Verdict` section yet

**If neither condition is true → skip Agent 0 entirely. Do not print anything.**

**Outputs:**
- `posts/<slug>-<date>/performance.md` — updated with Agent Verdict (LinkedIn-specific format from linkedin-performance-agent)
- `performance/tracker.md` — updated Post Performance Log + Pattern Summary (rewritten if ≥3 posts)
- Processed CSVs moved to `csv-imports/processed/`

Print `[HANDOFF: LINKEDIN PERFORMANCE AGENT]` with a one-line summary: posts processed, unmatched rows, whether Pattern Summary was updated.

---

## Strategist (runs once)

**Job:** Analyze the raw idea → produce a single master plan AND define N distinct angles for the Copywriters.

**Before planning, read `./linkedin-posts/performance/tracker.md`.** If the Pattern Summary section has content (≥3 posts logged), extract the key signals and add a `## Performance Context` block to the plan (template below). If tracker has <3 rows or no Pattern Summary, omit the block silently.

Print `[HANDOFF: STRATEGIST]` AND save to `01-post-plan.md`:

```
## Core Insight
<the central idea in one sentence — the "so what" of this post>

## Target Audience
<who specifically — not "professionals", be precise>

## Structure
1. <Point 1>
2. <Point 2>
3. <Point 3>
4. <Point 4> (optional)

## CTA
<one specific call to action — all variants must end with this>

## Tone Range
<conversational | authoritative | vulnerable | provocative | educational>

## Hashtags
<3-5 specific tags — same for all variants>

## Image Brief
<3-6 numbers/data points the image should carry · 1 tagline · before/after framing if applicable>

## Performance Context
<only include if tracker.md has ≥3 posts with data — omit block entirely if not>
- Best performing angle so far: <angle type + avg engagement rate>
- Hook styles that drove comments: <observation>
- Hook styles that drove passive reactions only: <observation>
- Topics/themes that resonated: <pattern>
- What to avoid repeating: <pattern>
- Implication for THIS post: <one sentence on how this context should shape angle/hook choice>

## Angle Assignments
Fixed angles (always used):
  - Angle A: Story-first — open with a personal moment or real scenario, let the insight emerge
  - Angle B: Bold claim-first — lead with the provocative insight, then back it with evidence/story

If N=3, the Strategist CHOOSES Angle C adaptively based on the idea's shape — do NOT default. Pick the one that will produce material the other two angles structurally cannot. Decision rules (apply in order, first match wins):
  1. Idea contains a clear "I was wrong / I learned" moment, a reversed belief, or builder-honest reflection → **Angle C: Vulnerability/confession-first** — open with the mistake or shift, let the new understanding emerge
  2. Idea teaches a concrete method, checklist, or repeatable process → **Angle C: Tactical/how-to-first** — lead with the practical outcome, walk through the steps
  3. Idea is structurally a comparison (A vs B, before/after two systems) → **Angle C: Comparison/split-screen-first** — bake the two sides into the opening line itself
  4. Idea has a hero number or stat that the image will carry → **Angle C: Data/number-first** — open with the most shocking number, let the text earn it
  5. None of the above → **Angle C: Contrarian** — challenge a common belief in the space, reframe the conventional wisdom

If N=4, add a second adaptive angle — pick the next-best match from the same list (skip the one already used as C).

State the chosen Angle C (and D if N=4) here AND give a one-line rationale: "Chose <angle> because <which decision rule matched + brief evidence from the idea>."
```

---

## Copywriters (N instances, run in parallel)

Run all N Copywriters simultaneously. Each receives the plan + its assigned angle.

**Rules for every Copywriter:**
- First line = a hook aligned with the assigned angle
- Short lines — 1-2 sentences per line max. White space is engagement.
- No corporate jargon. Write like Altaf talks.
- End with the exact CTA from the plan
- **CTA must be public-shareable** — no offers to pair / share access to internal tools. If the raw idea hints at internal tooling, frame the CTA as a builder-identity hook (positions Altaf as a builder, invites peers in the space to connect) OR as an open question. Never offer DM access to proprietary tools.
- Never add ideas not in the plan
- No emojis unless Altaf explicitly asks
- No "In this post I will..." ever
- Never invent stats, quotes, or claims not in the raw input
- Strip company names, internal tool names, private details — keep the lesson, drop the specifics

Each Copywriter prints its block AND writes the corresponding file. Block format uses `[HANDOFF: COPYWRITER-<ANGLE>]`:
- Angle A → `02a-draft-story-first.md`
- Angle B → `02b-draft-claim-first.md`
- Angle C → `02c-draft-<angle-slug>.md` (slug = kebab-case of the adaptive angle chosen, e.g. `vulnerability-first`, `tactical`, `comparison`, `data-first`, `contrarian`)
- Angle D → `02d-draft-<angle-slug>.md` (same naming convention)

Block format:
```
[HANDOFF: COPYWRITER — <Angle Name>]

<full post text — paste-ready>

---
Angle: <angle name>
Hook: <exact first line>
Word count: <N>
```

**On revision round** (winner only): print `[HANDOFF: COPYWRITER — REVISED <Winning Angle>]`, save to `02-revised-draft.md`:
```
[HANDOFF-2: REVISED DRAFT — <Winning Angle>]

<full revised post text — paste-ready>

---
Angle: <winning angle>
Changes made: <bulleted list of what was fixed per editor issues>
Borrowed from runner-up: <what was grafted in, if anything>
Word count: <N>
```

---

## Editor

**Round 1:** score every variant, pick the winner, decide on revision.
**Round 2:** final verdict on the revised draft — approve or output best available.

Print `[HANDOFF: EDITOR]` — valid JSON only. Save to `03-editor-verdict.json` (round 1) or `03-editor-verdict-final.json` (round 2):

```json
{
  "round": 1,
  "variants_reviewed": ["A", "B"],
  "status": "approved | needs_revision",
  "winner": "A | B | C | D",
  "why_winner": "<1-2 sentences>",
  "scores": {
    "A": { "hook_strength": 8, "authenticity": 9, "readability": 7, "plan_compliance": 10, "cta_clarity": 8, "avg": 8.4 },
    "B": { "hook_strength": 7, "authenticity": 8, "readability": 9, "plan_compliance": 9, "cta_clarity": 8, "avg": 8.2 }
  },
  "runner_up_notes": {
    "B": "<what was strong in B that the winner should borrow>"
  },
  "issues": [
    {
      "type": "weak_hook | off_plan | missing_cta | too_long | jargon | inauthentic | wrong_tone | buries_insight | non_shareable_cta",
      "severity": "high | medium | low",
      "description": "<exact problem in the WINNER draft>",
      "action": "<exact fix instruction>"
    }
  ]
}
```

**Decision logic:**
- `status: "approved"` → proceed to Image Designer
- `status: "needs_revision"` AND round < 2 → loop winner back through one Copywriter
- round = 2 → output best available regardless, list unresolved issues

---

## Image Designer (runs once, after final post is locked)

**Job:** Generate TWO distinct image variations for the final post by invoking the `/image-gen-agent` skill once with `Variations: 2`. The image agent reads the full post, reasons about the best dimension AND style for each variation independently, then generates both SVGs. Do NOT pre-select dimensions or styles here.

**Prepare the brief and invoke `/image-gen-agent`**

Pass the complete final post text, all stats/contrast pairs from `01-post-plan.md` Image Brief, and the winning angle. Set `Dimensions: reason` and `Style hint: reason` so the image agent drives the reasoning.

```
[IMAGE BRIEF]
Channel: linkedin
Variations: 2
Dimensions: reason
Style hint: reason
Final post: <paste full final post text>
Stats:
  - <label>: <value>
  - <label>: <value>
  (extract from final post and 01-post-plan.md Image Brief; if no numeric stats, use qualitative contrast pairs)
Winning angle: <angle name from editor verdict, e.g. "Comparison/split-screen">
Tagline: <from Image Brief in 01-post-plan.md>
Author: Altaf Shaikh
Handle: @teachmebro
Domain: <e.g. "AI Engineering">
Output path: ./linkedin-posts/posts/<slug>-<YYYYMMDD>/impact
```

The image-gen-agent will emit a `[IMAGE REASONING]` block (showing its dimension + style choices for each variation), then generate `impact-1.svg` and `impact-2.svg`. Do NOT write SVG inline. Always delegate to `/image-gen-agent`.

**After `/image-gen-agent` completes, the pipeline is NOT done. Immediately proceed to Step N below — write `final-post.md` and update `TODO.md`. Do not stop after image generation.**

---

## Step N — Finalize and update the queue

**This step is mandatory. Run it immediately after the Image Designer, every time — never skip it.**

1. **Write `final-post.md`** in the per-post folder using the template below. Include the image dimensions and styles surfaced by the image-gen-agent in the `## Images` table.
2. **DO NOT touch `../raw-ideas/`.** It's immutable and shared across channels. The source file stays where it is.
3. **Update `./linkedin-posts/TODO.md`:** remove the entry from "In Progress"; prepend a line to "Done" with the source filename, a link to the post folder, and the date.
4. **Print the final output block** (template below) in the conversation.

---

## `TODO.md` template

Create on first run if missing. Update on every run.

```markdown
# LinkedIn — Queue & Status

This is the LinkedIn channel's consumption ledger. Raw ideas live in `../raw-ideas/` (shared across all channels). Queue = files in `../raw-ideas/` MINUS the filenames listed under **Done** below.

## Queue (unprocessed for LinkedIn)
- [ ] <NNN>-<slug>.md — <one-line preview>

## In Progress
- [ ] <NNN>-<slug>.md — started <YYYY-MM-DD>

## Done
- [x] <NNN>-<slug>.md → [posts/<slug>-<YYYYMMDD>/final-post.md](./posts/<slug>-<YYYYMMDD>/final-post.md) — <YYYY-MM-DD>
```

Regenerate the Queue section each run: list files in `../raw-ideas/`, subtract filenames already in Done and In Progress. Append to Done; never delete entries from Done unless the user explicitly asks to re-run an idea.

---

## `final-post.md` template

```markdown
# <slug>

**Source idea:** [../../../raw-ideas/<NNN>-<slug>.md](../../../raw-ideas/<NNN>-<slug>.md)
**Generated:** <YYYY-MM-DD>
**Rounds:** <1 or 2>  ·  **Revised:** <yes/no>

## Variation Scores (Round 1)

| Variant | Angle            | Hook | Authenticity | Readability | Compliance | CTA | Avg |
|---------|------------------|------|--------------|-------------|------------|-----|-----|
| A       | Story-first      |  8   |      9       |      7      |     10     |  8  | 8.4 |
| B       | Bold claim-first |  7   |      8       |      9      |      9     |  8  | 8.2 |

**Winner:** Variant <X> — <why_winner>

---

## Final Post

<paste-ready LinkedIn post — no labels, no meta, just the post>

---

## Images

| File | Format | Style | Carries |
|------|--------|-------|---------|
| [impact-1.svg](./impact-1.svg) | <W>×<H> (<Portrait\|Square\|Landscape>) | <style name> | <stats/elements> |
| [impact-2.svg](./impact-2.svg) | <W>×<H> (<Portrait\|Square\|Landscape>) | <style name> | <stats/elements> |

**Exported PNGs:** `exports/impact-1.png` · `exports/impact-2.png`

---

**Unresolved issues:** <list or "none">
```

---

## Conversation output (every run)

Whether the run processed an idea or no-op'd, print one of:

**No-op:**
```
No new LinkedIn ideas. Skipping.
```

**Processed an idea:**
```
Channel: LinkedIn
Processed: <NNN>-<slug>.md
Post folder: ./linkedin-posts/posts/<slug>-<YYYYMMDD>/
Final post: ./linkedin-posts/posts/<slug>-<YYYYMMDD>/final-post.md
Images (SVG): impact-1.svg · impact-2.svg
Images (PNG): exports/impact-1.png · exports/impact-2.png
Queue remaining (LinkedIn): <N> idea(s)
```

---

## Loop integration (`/loop`)

This skill is wrapped by the loop prompt in `../linkedin.agent.md`:

```
/loop 1d <paste linkedin.agent.md prompt>
```

Each daily firing:
- Computes LinkedIn queue = `../raw-ideas/` MINUS TODO.md Done + In Progress
- Processes ONE idea if queue non-empty
- No-ops silently if queue is empty
- Never re-processes a filename already in TODO.md Done section
- Respects `channels:` frontmatter — skips ideas that exclude "linkedin"

To process multiple ideas in one day, invoke the skill manually as many times as needed — each invocation drains one entry from the LinkedIn queue. Other channels (X, blog) maintain independent queues against the same shared library.

---

## Shared rules (all agents)

- Never invent statistics, quotes, or claims not in the raw input
- If Altaf gave a real story or example, anchor every variant to it — don't replace with a generic one
- Strip any company names, internal tool names, or private details — keep the lesson, drop the specifics
- No emojis unless Altaf explicitly asks
- No "In this post I will..." openings — ever
- Authenticity beats polish — a slightly rough real line beats a smooth generic one
- Every handoff is BOTH printed in the conversation AND written to the per-post folder — never one without the other
- Never write outside `./linkedin-posts/` (except: Mode B may write a NEW file to `../raw-ideas/<NNN>-<slug>.md` to register a direct-args idea for other channels). No extra folders. No scratch files elsewhere.
- Never move, rename, or delete anything in `../raw-ideas/`. It's shared and immutable.
