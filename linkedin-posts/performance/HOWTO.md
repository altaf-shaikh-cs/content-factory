# How to Feed LinkedIn Analytics Into the Agent

Two paths — use whichever fits the moment.

---

## Path A — LinkedIn Content Analytics CSV (preferred)

LinkedIn lets you export post analytics from the Creator Analytics page.

### Steps

1. Go to **linkedin.com/analytics/creator/**
2. Set the date range to cover the posts you want to capture
3. Click the **Export** button (top-right — requires Creator Mode)
4. LinkedIn downloads an `.xlsx` file named `AggregateAnalytics_<YourName>_<start>_<end>.xlsx`
5. Drop it into:
   ```
   linkedin-posts/performance/csv-imports/
   ```
6. Run `/linkedin-growth-agent` — the LinkedIn Performance Agent detects the file, reads all 5 sheets, matches posts to folders by publish date, writes `performance.md` per post, updates `tracker.md`, and moves the file to `csv-imports/processed/`

### What the export contains (5 sheets)

| Sheet | What's in it |
|-------|-------------|
| DISCOVERY | Total impressions + members reached for the selected period |
| ENGAGEMENT | Daily impressions + engagements totals (not per post) |
| TOP POSTS | Per-post: URL · Publish Date · Engagements · Impressions — **this is the key sheet** |
| FOLLOWERS | Daily new follower counts + total followers |
| DEMOGRAPHICS | Audience breakdown by company, location, seniority, job title, industry |

**Important:** `Engagements` in TOP POSTS is a combined total — reactions + comments + reposts + clicks. There is no per-type breakdown, and **no saves and no followers-gained**. The aggregate export cannot tell you whether a post's reach actually grew the account. For that, use Path A2.

---

## Path A2 — Single-post export (do this for any post over ~1,000 impressions)

The aggregate export will happily report a huge month that gained you nothing. This is the export that catches it.

### Steps

1. Open the post on LinkedIn → click **View analytics** under the post
2. Click **Export** (top-right of the analytics panel)
3. LinkedIn downloads `SinglePostAnalytics_<YourName>_<postId>.xlsx` — one sheet
4. Drop it into `linkedin-posts/performance/csv-imports/` alongside the aggregate file
5. Run `/linkedin-growth-agent` — Agent 0 parses both and cross-references them

### What this export adds that the aggregate doesn't have

| Field | Why it matters |
|---|---|
| **Followers gained from this post** | The only number that compounds. Drives **capture rate** = followers gained / members reached. |
| **Profile viewers from this post** | Did anyone want to know who wrote it? Leading indicator of capture. |
| **Saves** | For carousels and frameworks, this is the real success metric. |
| **Reposts** | For memes and humour, this is the real success metric. Reactions without reposts means it never travelled. |
| Reactions / Comments split | Comment rate is LinkedIn's strongest distribution signal. |
| Post viewer demographics | Who *that post* reached, as opposed to who follows you. |

**Worked example (2026-08-09):** the aggregate export showed a 6,387-impression post and a +123% month. The single-post export showed **0 followers gained, 0 saves, 0 reposts, 1 comment**. Same post, opposite conclusion. Pull both.

---

## Path B — Manual entry (no CSV needed)

Use this when the export button isn't available or you want to log a single post quickly.

1. Open the post on LinkedIn → click **View analytics** under the post
2. Copy the numbers into the post's `performance.md`:
   ```
   linkedin-posts/posts/<slug>-<date>/performance.md
   ```
3. Use the template below — just fill in the numbers and run `/linkedin-growth-agent` so the Strategist picks it up on the next run.

### `performance.md` template (manual)

```markdown
# Performance — <slug>

**Published:** YYYY-MM-DD
**LinkedIn URL:** <paste post URL here>
**Last updated:** YYYY-MM-DD
**Data source:** manual

## Metrics

| Metric | Value |
|--------|-------|
| Impressions | |
| Members reached | |
| Reactions | |
| Comments | |
| Reposts | |
| Saves | |
| Link clicks | |
| Profile viewers from post | |
| Followers gained from post | |
| Engagement rate (%) | |
| Capture rate (%) | followers gained / members reached |

## Notes

<anything you noticed — what the comments said, what type of people engaged, etc.>
```

4. Run `/linkedin-growth-agent` — Agent 0 will pick it up, run the verdict analysis, and update `tracker.md`.

---

## How often to do this

- **Weekly** is ideal — drop the CSV once a week, let Agent 0 process it before the next post run
- **Monthly minimum** — the Strategist needs at least 3 data points before patterns emerge
- Don't wait for "enough data" before starting — partial data is better than none
