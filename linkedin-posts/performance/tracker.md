# LinkedIn Performance Tracker

One row per published post. Updated by the LinkedIn Performance Agent after each XLSX import. Strategist reads this before planning every new post.

**Last import:** 2026-08-10 · Sources: `AggregateAnalytics_Altaf Shaikh_2026-07-14_2026-08-10.xlsx` + `SinglePostAnalytics_Altaf Shaikh_7492090128753082368.xlsx`

**Two export formats now in use:**
- **Aggregate** — account totals + per-post impressions/engagements. `Engagements` is a combined total (reactions + comments + reposts + clicks), no breakdown.
- **Single-post** — one post, full breakdown: reactions, comments, reposts, **saves**, sends, profile views, **followers gained**. This is the only export that shows whether reach converted. Pull it for every post that breaks 1,000 impressions.

---

## The core metric: reach is not capture

Period 3 produced the account's largest post ever and gained nothing from it. Impressions and engagement rate both missed that. Two metrics now carry it:

| Metric | Formula | Why |
|---|---|---|
| **Capture rate** | Followers gained / Members reached × 100 | Did strangers stay? The only number that compounds. |
| **Profile view rate** | Profile viewers from post / Impressions × 100 | Did anyone want to know who wrote it? Leading indicator of capture. |

| Capture rate | Verdict |
|---|---|
| > 0.5% | Strong — reach is building the account |
| 0.1–0.5% | Average |
| < 0.1% | **Rented reach** — the post performed for LinkedIn, not for you |

**Rule:** a post is only a win if it clears BOTH the engagement-rate tier and the capture-rate tier. High impressions with 0% capture is a vanity result, not a success.

---

## Account Benchmarks

### Period 1: 2026-05-17 to 2026-06-13

| Metric | Value |
|--------|-------|
| Total impressions | 2,252 |
| Members reached | 900 |
| Total followers | 1,798 |
| Avg daily impressions | ~80 |
| Period engagement rate | ~3.77% |

### Period 2: 2026-06-18 to 2026-07-15

| Metric | Value |
|--------|-------|
| Total impressions | 3,396 |
| Members reached | 1,294 |
| Total followers | 1,812 (+14 new) |
| Avg daily impressions | ~121 (+51% vs period 1) |
| Period engagement rate | ~4.0% (136 eng / 3,396 imp) |

### Period 3: 2026-07-14 to 2026-08-10

| Metric | Value | vs Period 2 |
|--------|-------|-------------|
| Total impressions | 7,569 | +123% |
| Members reached | 4,429 | +242% |
| Total engagements | 87 | −36% |
| Period engagement rate | **1.15%** | −71% |
| Total followers | 1,822 (+22 gross adds, net +10) | +57% gross adds |
| Posts published | **4** in 28 days | — |

**Read the headline as a warning, not a win.** One post (the 8/9 meme) is 84% of the period's impressions. Strip it and the period is:

| Metric ex-meme | Value | vs Period 2 |
|---|---|---|
| Impressions | 1,183 over 26 days | — |
| Avg daily impressions | **45/day** | **−62%** |
| Engagement rate | 3.47% | −13% |

Baseline reach fell hard. The cause is cadence, not content — see Cadence collapse below.

| Tier | Engagement rate |
|------|----------------|
| Weak | < 2.5% |
| Average | 2.5–5% |
| Strong | > 5% |

_Thresholds held at Period 2 levels. Period 3's 1.15% account rate is distorted by one cold-reach outlier and is not a baseline reset._

---

## Cadence collapse (Period 3's real story)

Only 4 posts shipped in 28 days, with a **17-day silence from 7/19 to 8/4**. Daily impressions during the gap:

```
7/28  7/29  7/30  7/31  8/01  8/02  8/03  8/04
 10     5    11    10     8     4     4    13
```

The account floor is ~5 impressions/day when nothing ships. There is no residual distribution to coast on. Publishing frequency is the single highest-leverage variable on this account, ahead of angle, hook, and format.

---

## Unshipped register

Posts with a completed `final-post.md` and **zero LinkedIn record** — not one impression, while the export lists posts from 2021 with a single impression. Near-certain they were never published.

| Post folder | Finished | Status |
|---|---|---|
| `claude-code-25-tips-20260719` | 2026-07-19 | Unshipped |
| `claude-four-building-blocks-20260719` | 2026-07-19 | Unshipped |
| `loops-explained-prompt-vs-loop-agent-anatomy-20260719` | 2026-07-19 | Unshipped |
| `five-rung-ai-automation-ladder-20260809` | 2026-08-09 | Unshipped — the account's first carousel, never posted |

Four finished posts idle. This is the same 17-day gap seen from the supply side: the factory produced, the channel did not ship. **Check this register before generating anything new** — shipping existing inventory beats generating more.

---

## Audience Profile (Aggregate DEMOGRAPHICS — Period 3)

**Geography:** Mumbai Metropolitan Region 44% · Greater Bengaluru 8% · Greater Delhi 5% · Greater Hyderabad 3%
**Seniority:** Senior 37% · Entry 36% · Manager 3%
**Companies:** Contentstack 9% · TCS 2% · Accenture 1% · Infosys 1%
**Company size:** 10,001+ 23% · 501–1,000 13% · 51–200 11%
**Job titles:** Software Engineer 24% · Founder 2% · Data Engineer 2%
**Industries:** IT Services & Consulting 34% · Software Development 30% · Tech/Internet 7%

Stable vs Period 2. Early-to-mid career engineers in India's tech hubs.

**Important distinction the Strategist must respect:** the CONTENT demographics sheet in Period 3 is ~100% the 8/9 meme (it matches that post's single-post demographics almost exactly). It describes who a meme reaches, NOT who the account reaches. Do not read it as an audience shift.

---

## Post Performance Log

| Post slug | Published | Format | Impr. | Eng. | Eng. Rate | Capture | Tier | Angle | Notes |
|-----------|-----------|--------|-------|------|-----------|---------|------|-------|-------|
| parle-g-ai-meme | 2026-08-09 | **Meme image** | **6,387** | 45 | 0.70% | **0.00%** | reach outlier / no capture | Humour, cultural | Off-pipeline, made outside the factory. Full breakdown below. Account's largest post ever and its worst conversion. |
| claude-four-building-blocks (2nd take) | 2026-08-05 | Text + image | 291 | 15 | **5.15%** | — | strong | Comparison/split-screen | Best rate since gen-ai-roadmap. Per impression, 7× more engaging than the meme. |
| fable5-hybrid-orchestration-patterns | 2026-07-18 | Text + image | 320 | 13 | 4.06% | — | average | Tactical/how-to-first | First post of the Premium era. No Premium lift visible. |
| iphone-shortcit | 2026-07-15 | Text + image | 217 | 9 | 4.15% | — | average | — | Full lifetime data now in (was 35/2 "too early" at last import). |
| ai-drinks-water | 2026-07-10 | Text-only | 148 | 11 | 7.43% | — | strong | Contrarian | Period 2 figure. Period 3 residual only: 33 imp / 2 eng. |
| routines | 2026-07-11 | Text + image | 848 | 21 | 2.48% | — | average | Bold claim-first | Period 2 figure. Period 3 residual: 212 imp / 2 eng. |
| [unmatched post] | 2026-07-02 | unknown | 742 | 16 | 2.16% | — | weak | unknown | URL slug `softwaredevelopment-engineering`. Still unidentified. Period 3 residual: 70 imp. |
| gen-ai-roadmap | 2026-06-21 | Text + image | 755 | 58 | **7.69%** | — | strong | Story-first | All-time best rate. Period 3 residual: 13 imp / 1 eng. |
| first-autonoumsly-dveloped-todo-app | 2026-06-29 | Text + image | 384 | 19 | 4.95% | — | average | Bold claim-first | Period 2 figure. |
| claude-vs-codex | 2026-06-07 | Text + image | 452 | 23 | 5.09% | — | strong | Bold claim-first | Period 1 top performer. |
| claude-new-feature-loop | 2026-06-13 | Text + image | 38 | 1 | 2.63% | — | weak | Bold claim-first | Residual only, small sample. |
| five-rung-ai-automation-ladder | — | Carousel | — | — | — | — | **unshipped** | Bold claim-first | See Unshipped register. |
| claude-code-25-tips | — | Text + image | — | — | — | — | **unshipped** | — | See Unshipped register. |
| claude-four-building-blocks (1st take) | — | Text + image | — | — | — | — | **unshipped** | Contrarian | See Unshipped register. |
| loops-explained | — | Text + image | — | — | — | — | **unshipped** | — | See Unshipped register. |
| superreps-learnings / build-your-first-agents-team / just-text / run-your-own-agent | — | — | — | — | — | — | no record | — | Never appeared in any export across 3 periods. Presume unpublished. |

---

## Post deep-dive: parle-g-ai-meme (2026-08-09)

The account's most important data point. Recorded in full because the aggregate export alone led to the wrong conclusion.

**What it was:** a four-panel image. Blue candy pulled from a yellow field labelled `*AI`, a melted-sculpture shot, then two Parle-G packs — *2000: Code once written in Java, Python* / *2070: Executes Forever*. Indian nostalgia brand plus a developer in-joke. No links, no pipeline, minutes to make. Published 11:01 AM.

| Metric | Value | Read |
|---|---|---|
| Impressions | 6,387 | ~140× the account's 45/day baseline. Previous lifetime best was 848. |
| Members reached | 4,113 | 1.55 impressions/member — broad cold distribution, one look each |
| Reactions | 35 | 97% of all engagement |
| Comments | 1 | Comment rate **0.016%** — far below the 0.2% weak threshold |
| Reposts | **0** | The one that matters for a meme. Memes travel by repost. This did not travel. |
| Saves | **0** | |
| Sends | 0 | |
| Profile viewers | 11 | Profile view rate **0.17%** |
| **Followers gained** | **0** | **Capture rate 0.00%** |

**Viewer demographics (this post alone):** Entry 32% / Senior 24% (inverted vs the follower base), Greater Allahabad 4%, Noida 1%, Higher Education 3%, student orgs (MNNIT Allahabad mentorship, PICT ACM Student Chapter). Contentstack only 3% against 9% of the follower base — meaning distribution went overwhelmingly to **non-followers**.

**Verdict.** The reach is real and repeatable: humour buys distribution this account cannot otherwise buy, at near-zero production cost. The conversion is the failure, and the cause is specific — **the meme carried no bridge back to the author.** Nothing in it signals what Altaf builds, so a stranger who laughs has no reason to follow. 4,113 strangers arrived and left.

Secondary failure: 35 reactions against 0 reposts. Even as a meme it read as mildly amusing rather than share-worthy. It got distribution from the format, not from people passing it on. Observational nostalgia puts nobody's identity at stake.

---

## Format performance

| Format | Posts | Avg impressions | Avg eng. rate | Capture | What it buys |
|---|---|---|---|---|---|
| Text + image | 3 (period 3) | 276 | **4.47%** | untracked | Conversion. Where this account's engagement actually lives. |
| Text-only | 1 (ai-drinks-water) | 148 | 7.43% | untracked | Highest rate on record. Not a disadvantage. |
| **Meme image** | 1 | **6,387** | 0.70% | **0.00%** | Reach. Cold, young, outside the ICP, does not stay. |
| Carousel | 0 shipped | — | — | — | Untested. Slide deck exists, never posted. |

**The trade is now measured:** memes deliver ~23× the impressions of a text post at ~1/6th the engagement rate and zero capture. They are a top-of-funnel instrument, not a substitute for the text posts that convert.

---

## Pattern Summary

**Data range:** 2026-06-07 to 2026-08-10 · **Posts with reliable data:** 11

### Angle performance

| Angle | Posts | Avg Eng. Rate | Signal |
|-------|-------|--------------|--------|
| Contrarian | 1 | 7.43% | Strongest when it reframes a belief the audience holds. Small sample. |
| Story-first | 2 | 6.39% | Consistent. Works when the opening moment is specific and recognizable. |
| Comparison/split-screen | 1 | 5.15% | New in period 3. First line carrying both sides of the comparison is the shape top performers share. |
| Bold claim-first | 3 | 3.86% | Variable. Works on comparison/tool topics, underperforms on "I tried X" narratives. |
| Tactical/how-to-first | 1 | 4.06% | Average. |
| Humour/cultural | 1 | 0.70% | Reach instrument. Judge on capture rate, never on engagement rate. |

### LinkedIn algorithm signals

- **Premium is not an amplifier on this account.** Pre-Premium posts ranged 384–848 impressions. Post-Premium text posts: 320 and 291. Per-post reach on text is **down**, not up. The only breakout came from changing format. **This supersedes the Period 2 "Premium will amplify" note — treat Premium as neutral and stop attributing swings to it.**
- **Format beats Premium beats angle** for raw reach. Angle still governs conversion.
- **Comment rate is the weak spot account-wide.** The best post of period 3 by rate (5.15%) and the biggest by reach (0.016% comment rate) both under-generate conversation. Reactions dominate everywhere.
- **Publishing gaps have no floor cushion.** Reach decays to ~5/day within a week of silence.
- **Link-in-post tax:** still enforced. All links go to the first comment.
- **Hashtags:** fewer and topically tight continues to outperform generic clusters.

### Audience behavior patterns

- Practical skill-building and roadmap content drives the strongest engagement (gen-ai-roadmap, 7.69%)
- Contrarian posts that name something the audience does but won't admit drive comments (ai-drinks-water)
- Comparison framings ("two engineers, same model") convert — the reader picks a side in the first line
- Abstract process posts get reach without depth (routines, 2.48%)
- Humour reaches a materially different, younger, non-follower audience that does not convert on its own

---

## Recommendations for Strategist

1. **Ship the unshipped register before generating anything new.** Four finished posts, zero impressions. Generation is not the bottleneck.
2. **Close the cadence gap.** Nothing else in this tracker matters as much. Silence costs ~90% of baseline reach within a week.
3. **Keep memes in the rotation, budgeted at roughly 1 in 4–5 posts.** The reach is real. Do not let them displace text posts, which are where conversion lives.
4. **Every meme must carry a bridge.** Three requirements, all missing from the 8/9 post:
   - A **fixed visual signature** (same frame, type treatment, corner mark) so repeat exposure compounds into recognition rather than evaporating.
   - **One converting line** in the caption after the joke lands: what Altaf actually builds, stated plainly. Not a hard CTA, just a reason the follow makes sense.
   - A **shared enemy or pain**, not observational nostalgia. Reposts happen when a reader wants their team to see it. Nobody's identity was at stake in 2000-vs-2070.
5. **Sequence reach into conversion.** Follow a meme with a real technical post within 24–48h while the cold audience is still inside your distribution. The 8/9 meme was followed by nothing and the 4,113 went nowhere.
6. **Pull single-post analytics for anything over 1,000 impressions.** The aggregate export cannot distinguish a breakout from rented reach. Period 3's headline said +123% impressions; the truth was −62% baseline reach and zero followers from the outlier.
7. **Lead with a specific, uncomfortable truth** rather than a scene. Still the strongest hook property on record.
8. **Test carousel for real.** The format is completely untested here — the one deck built was never posted. If it ships, judge it on capture rate, and put the saveable diagnostic on slide 2, not slide 7.
9. **Identify the 7/2 unmatched post** (742 imp, 2.16%). Three periods unresolved.

---

## Import Notes

- **Period 3 processed 2026-08-10** from two exports (aggregate + single-post).
- **Attribution correction:** the 8/9 post (6,387 impressions, URL slug `share-7492090127687798784-SSKi`) was initially attributed to `five-rung-ai-automation-ladder-20260809` on publish-date match. It is in fact an off-pipeline meme. The carousel was never published. **Date-matching alone is unsafe when the URL slug carries no hashtags** — confirm against the user or the post's own analytics before logging.
- Off-pipeline post recorded at `posts/parle-g-ai-meme-20260809/` so the account's best-reaching content stays inside the system.
- The Period 2 note claiming "Premium is an amplifier, expect a distribution lift" is **retracted** — see LinkedIn algorithm signals above.
- Both Period 3 export files moved to `csv-imports/processed/`.
