# LinkedIn — Queue & Status

This is the LinkedIn channel's consumption ledger. Raw ideas live in `../raw-ideas/` (shared across all channels). Queue = files in `../raw-ideas/` MINUS the filenames listed under **Done** below.

## Queue (unprocessed for LinkedIn)

_Empty. The two remaining PDFs in `../raw-ideas/` are reference captures of ideas already processed via their synthesized `.md` files (see Done), so they are not queue items._

**Note on a drained queue:** when every source idea is consumed, the next move is a DERIVED idea, a pattern that runs across several ideas but is not written in any single one. Read the whole library at once, find the recurring structure, and register it as a new `raw-ideas/<NNN>-*.md` so other channels can consume it too. `007-five-rung-ai-automation-ladder.md` is the first of these.

## In Progress

## Ready to ship (generated, never published)

Re-verified 2026-09-06 against `AggregateAnalytics_Altaf Shaikh_2026-08-24_2026-09-06.xlsx`.
These have a finished `final-post.md` and **zero LinkedIn impressions**. The export lists posts
down to a single impression, so absence means unpublished, not underperforming.
**Shipping these outranks generating anything new.**

- [ ] [five-rung-ai-automation-ladder-20260809](./posts/five-rung-ai-automation-ladder-20260809/final-post.md) — 8-slide document carousel + caption. Note before posting: move the diagnostic (slide 7) to slide 2. (Stale note removed: this is no longer "the account's first carousel", two have since shipped.)
- [ ] [claude-code-25-tips-20260719](./posts/claude-code-25-tips-20260719/final-post.md)
- [ ] [claude-four-building-blocks-20260719](./posts/claude-four-building-blocks-20260719/final-post.md) — contrarian angle. The 8/5 second take on the same source shipped and hit 5.15%, the best rate of that period.
- [ ] [loops-explained-prompt-vs-loop-agent-anatomy-20260719](./posts/loops-explained-prompt-vs-loop-agent-anatomy-20260719/final-post.md)
- [ ] [token-usage-spike-20260905](./posts/token-usage-spike-20260905/final-post.md) — text + image, 2 variations. Mechanism-explainer rewrite; ship with impact-1 (the context-growth chart), it carries the argument. **Kept here deliberately:** a post published 9/5 could not be attributed (see below). Wrongly marking this shipped would mean it never gets published, so it stays until confirmed.

**Gate count: 5** (was recorded as 8). The gate still fires at ≥3, but now on real numbers.

### Corrected 2026-09-06 — these were listed as unshipped and had in fact been published

The register was last verified against the 2026-08-10 export and never rechecked, so three
posts shipped between 8/20 and 9/3 were still being counted against the ship gate. That
inflated the gate by three and contributed to the 2026-09-05 run being blocked.

| Post | Published | Impressions | Engagements | Eng rate | Identified by |
|---|---|---:|---:|---:|---|
| [andrew-ng-four-software-skills-2026-20260820](./posts/andrew-ng-four-software-skills-2026-20260820/final-post.md) | 8/20 | 197 | 7 | 3.6% | slug `the-2026-ai-skill-shift`, date + carousel type |
| [claude-auto-mode-authorization-20260826](./posts/claude-auto-mode-authorization-20260826/final-post.md) | 8/27 | 704 | 22 | 3.1% | slug `claude-auto-mode-under-the-hood` |
| [anthropic-multi-agent-research-system-20260903](./posts/anthropic-multi-agent-research-system-20260903/final-post.md) | 9/3 | 259 | 32 | **12.4%** | hashtags `aiengineering-aiagents-llm` match exactly |

The 9/3 post has the highest engagement rate on record for this account and the lowest
distribution of any recent post. See Period 4 in [`performance/tracker.md`](./performance/tracker.md).

### Unattributed published post — 2026-09-05

The account's biggest post of the period is not traceable to any folder here:
**1,370 impressions, 63 engagements, 9 followers gained that day**, URL slug `teachmebro`,
type `ugcPost` (the same type as both shipped carousels, suggesting a document post).

It does not match `token-usage-spike` or `five-rung-ai-automation-ladder`, whose captions
both open with different hashtags. Most likely off-pipeline, like the 8/30 hiring post and
the parle-g meme. **Worth identifying:** it converted 9 followers in one day, more than a
third of the period's total, and nothing in this repo records what it was.

Also never seen in any export across three periods, presume unpublished: `superreps-learnings-20260608`, `build-your-first-agents-team-20260616`, `just-text-20260629`, `just-text-20260714`, `run-your-own-agent-acengy-with-paperclip-20260630`.

## Done
- [x] token-usage-spike.md → [posts/token-usage-spike-20260905/final-post.md](./posts/token-usage-spike-20260905/final-post.md) — 2026-09-05 (Mode B: Altaf passed the idea file path directly and asked for the post, so the ship gate was overridden by the documented Mode B rule, not agent judgment. Vulnerability/confession-first won a 3-angle run at 9.2; the 747-re-reads illustration and A's list-rate cost anchor were grafted in on revision. **Rewritten the same day by request**: refocused from the confession onto the turn mechanism itself, with the 21k-file-at-call-200 example as the spine. impact-1 rebuilt as a context-growth chart. Pipeline version preserved in final-post.md.)
- [x] 009-anthropic-multi-agent-research-system.md → [posts/anthropic-multi-agent-research-system-20260903/final-post.md](./posts/anthropic-multi-agent-research-system-20260903/final-post.md) — 2026-09-03 (Mode B: Altaf passed the source URL directly the same session the blog post was written, so the ship gate was overridden by the documented Mode B rule, not by agent judgment. Data/number-first won on a 3-angle run; the seven-week outage was grafted in from the story-first draft as first-person proof.)
- [x] claude-autoclassifier.md → [posts/claude-auto-mode-authorization-20260826/final-post.md](./posts/claude-auto-mode-authorization-20260826/final-post.md) — 2026-08-26 (requested directly with the idea file, so Mode B; ship gate acknowledged and overridden by that direct request, see note below. Built from the Anthropic engineering write-up rather than the announcement coverage. A first draft this same day was rejected as a feature dump and discarded; the rebuild carries one idea, authorization is not transitive.)
- [x] 008-andrew-ng-four-software-skills-2026.md → [posts/andrew-ng-four-software-skills-2026-20260820/final-post.md](./posts/andrew-ng-four-software-skills-2026-20260820/final-post.md) — 2026-08-20 (second carousel on the account; requested directly as a "multi slide post")
- [x] _(off-pipeline)_ → [posts/parle-g-ai-meme-20260809/final-post.md](./posts/parle-g-ai-meme-20260809/final-post.md) — 2026-08-09. Not from `raw-ideas/`, made directly by Altaf. Logged because it is the account's highest-reaching post ever: 6,387 impressions, 4,113 reached, **0 followers gained**. Established the reach-vs-capture distinction now encoded in the tracker and both skills.
- [x] 007-five-rung-ai-automation-ladder.md → [posts/five-rung-ai-automation-ladder-20260809/final-post.md](./posts/five-rung-ai-automation-ladder-20260809/final-post.md) — 2026-08-09 (DERIVED cross-idea, synthesized from 15 library ideas rather than sourced from one. First document carousel on the account, 8 slides + caption.)
- [x] 25 Claude Code Tips from 11 Months of Intense Use _ r_ClaudeAI.pdf → [posts/25-claude-code-tips-20260809/final-post.md](./posts/25-claude-code-tips-20260809/final-post.md) — 2026-08-09
- [x] The Four Claude Features That Turn AI From Toy to Tool.pdf → [posts/claude-four-building-blocks-20260805/final-post.md](./posts/claude-four-building-blocks-20260805/final-post.md) — 2026-08-05 (second take on the same source as 006, requested directly; comparison/onboarding angle instead of the 2026-07-19 contrarian one)
- [x] (6) Anatoli Kopadze on X_ _Loops explained_ Claude, GPT, Mira and what actually works_ _ X.pdf → [posts/loops-explained-claude-gpt-mira-20260805/final-post.md](./posts/loops-explained-claude-gpt-mira-20260805/final-post.md) — 2026-08-05
- [x] claude code features.md → [posts/claude-code-25-tips-20260719/final-post.md](./posts/claude-code-25-tips-20260719/final-post.md) — 2026-07-19
- [x] 006-claude-four-building-blocks-skills-plugins-projects-artifacts.md → [posts/claude-four-building-blocks-20260719/final-post.md](./posts/claude-four-building-blocks-20260719/final-post.md) — 2026-07-19
- [x] 005-loops-explained-prompt-vs-loop-agent-anatomy.md → [posts/loops-explained-prompt-vs-loop-agent-anatomy-20260719/final-post.md](./posts/loops-explained-prompt-vs-loop-agent-anatomy-20260719/final-post.md) — 2026-07-19
- [x] joke-on-say-the-word-by-claude.md — dropped 2026-07-19, drafts reviewed and rejected by Altaf, do not re-process
- [x] joke-on-say-the-word-by-claude.md → [posts/joke-on-say-the-word-by-claude-20260718/final-post.md](./posts/joke-on-say-the-word-by-claude-20260718/final-post.md) — 2026-07-18
- [x] 004-fable5-hybrid-orchestration-patterns.md → [posts/fable5-hybrid-orchestration-patterns-20260718/final-post.md](./posts/fable5-hybrid-orchestration-patterns-20260718/final-post.md) — 2026-07-18
- [x] ROUTINES.MD → [posts/routines-20260717/final-post.md](./posts/routines-20260717/final-post.md) — 2026-07-17
- [x] just text.md → [posts/just-text-20260714/final-post.md](./posts/just-text-20260714/final-post.md) — 2026-07-14
- [x] run-your-own-agent-acengy-with-paperclip.md → [posts/run-your-own-agent-acengy-with-paperclip-20260630/final-post.md](./posts/run-your-own-agent-acengy-with-paperclip-20260630/final-post.md) — 2026-06-30
- [x] iphone-shortcit-to-generate-slide-from-raw-ideas.md → [posts/iphone-shortcit-to-generate-slide-from-raw-ideas-20260628/final-post.md](./posts/iphone-shortcit-to-generate-slide-from-raw-ideas-20260628/final-post.md) — 2026-06-28
- [x] first-autonoumsly-dveloped-todo-app.md → [posts/first-autonoumsly-dveloped-todo-app-20260624/final-post.md](./posts/first-autonoumsly-dveloped-todo-app-20260624/final-post.md) — 2026-06-24
- [x] build-your-first-agents-team.md → [posts/build-your-first-agents-team-20260616/final-post.md](./posts/build-your-first-agents-team-20260616/final-post.md) — 2026-06-16
- [x] gen-ai-roadmap.md → [posts/gen-ai-roadmap-20260614/final-post.md](./posts/gen-ai-roadmap-20260614/final-post.md) — 2026-06-14
- [x] ai-non-deterministic-code-vs-program-deterministic-code.md → [posts/non-deterministic-vs-deterministic-20260614/final-post.md](./posts/non-deterministic-vs-deterministic-20260614/final-post.md) — 2026-06-14
- [x] ai drinks water more than humans do.md → [posts/ai-drinks-water-20260613/final-post.md](./posts/ai-drinks-water-20260613/final-post.md) — 2026-06-13
- [x] 003-claude-new-feature-loop.md → [posts/claude-new-feature-loop-20260609/final-post.md](./posts/claude-new-feature-loop-20260609/final-post.md) — 2026-06-09
- [x] 002-SuperReps-learnings.md → [posts/superreps-learnings-20260608/final-post.md](./posts/superreps-learnings-20260608/final-post.md) — 2026-06-08
- [x] 001-claude-vs-codex.md → [posts/claude-vs-codex-20260607/final-post.md](./posts/claude-vs-codex-20260607/final-post.md) — 2026-06-07

**Reference captures (not queue items):** `(6) Anatoli Kopadze on X_ _Loops explained...pdf` was consumed as `005-loops-explained-...md`; `25 Claude Code Tips from 11 Months of Intense Use _ r_ClaudeAI.pdf` was consumed as `claude code features.md`. Do not process these PDFs separately, they would duplicate shipped posts.

**Note (2026-08-26, ship gate):** the unshipped count above was already past the threshold of 3 when this post was generated. The gate was not bypassed on the agent's own judgment. Altaf passed the idea file directly and asked for the post explicitly, which is the documented Mode B override. Recorded here so the override is visible rather than silent. This run does not reduce the backlog, and shipping it still outranks generating anything new.

**Note (2026-09-03, ship gate):** unshipped count was **6** when this post was generated, double the threshold. Overridden under the Mode B rule: Altaf passed the source URL directly in the same session, right after the blog post on the same idea. Recorded so the override stays visible. This run does not reduce the backlog. Recommended ship: `claude-four-building-blocks-20260719`, contrarian angle (best angle on record at 7.43%) in text + image, the only format this account has proven converts.
