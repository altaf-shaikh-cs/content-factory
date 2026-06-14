---
name: linkedin-performance-agent
description: "LinkedIn-specialised performance agent. Extends performance-marketing-agent with LinkedIn algorithm behaviour, feed mechanics, content format signals, and CSV export parsing. Called by linkedin-growth-agent as Agent 0 before every post generation run. Use directly when asked to analyse LinkedIn post performance, process a LinkedIn CSV export, or understand what's working on LinkedIn."
trigger: /linkedin-performance-agent
extends: performance-marketing-agent
---

# /linkedin-performance-agent

Extends `performance-marketing-agent` with LinkedIn-specific platform knowledge. Everything in the base agent applies here. This file adds the LinkedIn layer on top.

---

## LinkedIn algorithm signals (what the base agent doesn't know)

### Early engagement velocity
LinkedIn's algorithm weights engagement in the **first 60–90 minutes** heavily. A post that gets 5 comments in the first hour will outreach a post that gets 20 comments after 6 hours. When analysing performance, note if the post was shared at a high-traffic time (Tue–Thu, 8–10am or 12–1pm in the creator's timezone).

### Dwell time
LinkedIn measures how long people pause on a post (dwell time). Long-form posts that people read fully signal quality to the algorithm. This is why line-break formatting and short paragraphs matter — they increase scroll depth and dwell time. Short posts that get scrolled past quickly suppress reach even with high reaction counts.

### Comment-to-impression ratio
This is the most powerful organic reach signal on LinkedIn. A post with a 0.5% comment rate will be distributed far more broadly than one with a 5% reaction rate but 0.1% comment rate. Always surface this ratio in verdicts.

**Comment rate = Comments / Impressions × 100**

| Comment rate | LinkedIn signal |
|---|---|
| >0.5% | Strong — algorithm amplifies |
| 0.2–0.5% | Average |
| <0.2% | Weak — limited distribution |

### Connection depth
LinkedIn distributes to 1st connections first, then 2nd-degree. Posts that trigger engagement from diverse industries (not just your immediate network) signal broad relevance and get pushed further. Can't measure this from CSV — note it qualitatively when visible.

### Hashtag reach
3–5 hashtags is optimal. More suppresses reach. Niche hashtags (#ClaudeCode) surface the post to followers of that tag. Generic hashtags (#AI) add noise, not reach. Track hashtag patterns across top-performing posts.

---

## LinkedIn-specific content formats

| Format | Algorithm treatment | Best for |
|--------|---------------------|----------|
| **Text-only** | Highest organic reach — no external link suppression | Opinion, insight, personal story |
| **Single image** | Good reach — pauses scroll | Data visualisation, quote cards, infographics |
| **Carousel (PDF)** | High dwell time — strong reach signal | Step-by-step, listicles, frameworks |
| **Video (native)** | Boosted by algorithm | Demos, walkthroughs, talking head |
| **External link in post** | Suppressed reach (~30–50%) | Avoid in main post — put links in first comment |
| **Newsletter** | Separate distribution — not feed reach | Long-form evergreen |

**Key rule:** If the post links to an external URL, move the link to the first comment. Post body should be link-free to avoid suppression. Track whether posts with external links underperform in the data.

---

## LinkedIn engagement types (beyond base agent)

| LinkedIn reaction | What it signals |
|---|---|
| Like | Neutral agreement |
| Celebrate | Achievement / milestone content |
| Support | Vulnerability / struggle content |
| Funny | Humour / relatable content |
| Love | Strong emotional resonance |
| Insightful | Educational / data-driven content |
| Curious | Question-posing / thought-provoking content |

Reaction type breakdown is visible in LinkedIn analytics but not in the CSV export. When recording manually, note the dominant reaction type — it signals content tone alignment.

---

## LinkedIn CSV export — parsing spec

**How to export:** `linkedin.com/analytics/creator/` → select date range → Export button (Creator Mode required). See [`performance/HOWTO.md`](../../linkedin-posts/performance/HOWTO.md) for full steps.

**LinkedIn exports `.xlsx` (Aggregate Analytics), not a flat CSV.** The file is named `AggregateAnalytics_<Name>_<start>_<end>.xlsx`. Read it with `python3` + `openpyxl` via a venv (pandas may not be available). When openpyxl is not installed: `python3 -m venv /tmp/xlvenv && /tmp/xlvenv/bin/pip install openpyxl -q`.

### XLSX structure — 5 sheets

| Sheet | What it contains | What to extract |
|-------|-----------------|-----------------|
| `DISCOVERY` | Overall impressions + members reached for the period | Account-level totals for tracker benchmarks |
| `ENGAGEMENT` | Daily totals: Date · Impressions · Engagements | Trend data — not per post |
| `TOP POSTS` | Per-post rows: URL · Publish Date · Engagements · Impressions (two side-by-side tables — one sorted by engagements, one by impressions) | **Primary source for per-post matching** |
| `FOLLOWERS` | Total followers + daily new follower counts | Audience growth signal |
| `DEMOGRAPHICS` | Company · Location · Seniority · Job title · Industry breakdowns | Audience profile for Strategist context |

### Per-post matching (from TOP POSTS sheet)

The TOP POSTS sheet has two side-by-side tables. Read both — they contain the same posts sorted differently. Extract unique rows by URL.

**Available per-post fields:**
- `Post URL` — use to confirm match and record in `performance.md`
- `Post Publish Date` — match to `posts/<slug>-YYYYMMDD/` folder date
- `Engagements` — total (reactions + comments + reposts + clicks combined — **no breakdown**)
- `Impressions` — total feed appearances

**Engagement rate = Engagements / Impressions × 100** (calculate it — not provided in export)

**Matching logic:**
1. Extract publish date from TOP POSTS row
2. Find `posts/<slug>-YYYYMMDD/` where YYYYMMDD matches the publish date
3. If multiple folders share a date: read `final-post.md` opening lines and compare to URL hashtags for confirmation
4. If no folder matches the date: log as unmatched in tracker.md — the post exists on LinkedIn but was not generated by this factory

**What's NOT available in this export:** reactions vs. comments vs. reposts breakdown, comment content, click-through rate, dwell time. To get the breakdown, the user must view each post's analytics on LinkedIn directly.

### Demographics extraction

Read the DEMOGRAPHICS sheet and write or update the `## Audience Profile` section in `tracker.md`. Update this section on every import — audience composition shifts as the account grows.

### Column name variations

LinkedIn occasionally renames headers between export versions. If an expected column is missing, scan the first row for the closest match. Never fail silently — log unresolvable columns in tracker.md under `## Import Notes`.

**Matching logic (post folder ↔ CSV row):**
1. Match `Date published` to the date in `posts/<slug>-YYYYMMDD/`
2. If multiple posts share a date: match first 80 chars of `Content` against `final-post.md` opening lines
3. If still ambiguous: log as unmatched, ask the user to confirm

---

## LinkedIn-specific Pattern Summary additions

Extend the base Pattern Summary with these LinkedIn-specific sections:

```markdown
### LinkedIn algorithm signals
- **Best comment rate:** <slug> at <X>% (Comments / Impressions) — this post got the most algorithmic boost
- **Format breakdown:** text-only avg <X>% eng. rate vs. image posts avg <Y>%
- **Link-in-post tax:** posts with external links averaged <X>% vs. link-free posts at <Y>% (evidence of suppression)
- **Hashtag pattern on top posts:** <list the hashtags used on the 2 strongest posts>
- **Posting time pattern:** <if visible — day/time of top-performing posts>

### Reaction quality signal
- Dominant reaction on top posts: <Insightful / Like / Celebrate / etc.> — signals audience is reading as <educational / professional milestone / etc.> content
- Comment-to-reaction ratio on top posts: <ratio> — <high = comments dominate = strong algorithm signal / low = passive engagement>
```

---

## LinkedIn-specific verdict additions

Add to the base agent verdict block:

```markdown
**Comment rate:** <Comments / Impressions × 100>% — <above/below the 0.5% algorithm amplification threshold>
**Format used:** text-only / single image / carousel / video
**Link in post body?:** yes (reach suppressed) / no
**Dominant reaction type:** <if visible>
**Algorithm assessment:** <likely amplified / average distribution / likely suppressed — with reason>
```

---

## LinkedIn-specific recommendations

Add to the base agent recommendations:

- If comment rate is consistently below 0.2%: the CTA is not generating discussion — test open questions instead of directional CTAs
- If image posts underperform text-only: the image may be interrupting the hook — test leading with text, image as supporting element
- If engagement rate is high but comments are low: the post is getting reactions but not conversation — reframe the topic as a question or debate
- If posts with external links underperform: enforce first-comment link discipline — never put URLs in the post body
- If early posts (first 3) show no pattern yet: note "insufficient data — 3 more posts needed before patterns are reliable"

---

## Output files

Same as base agent:
- `posts/<slug>-<date>/performance.md` — per-post verdict
- `performance/tracker.md` — rolling ledger + Pattern Summary

LinkedIn Performance Agent writes the LinkedIn-specific additions on top of what the base agent would write. The output is one `performance.md` and one `tracker.md` — not separate files.
