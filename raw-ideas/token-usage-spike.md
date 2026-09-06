## Handoff: Claude Code token-usage diagnosis (Altaf, 2026-09-05)

### What was done
Analyzed ~/.claude/projects transcripts for Aug 30 – Sep 5 to explain a large
spike in token usage. Diagnosis complete; NO fixes have been applied yet.

### Findings (all measured from transcript JSONL usage fields, not estimated)

Week totals: 11k fresh input · 5.6M output · 31.5M cache writes · 1,196M cache
reads. That's 213 tokens re-read per token produced, ~$1,050 for the week at
Opus 5 rates ($5/$25 per MTok, cache read $0.50, 1-hour-TTL write $10).
The claude.ai usage chart's "52.3k in / 19.4M out" legend is only the uncached
slice — the 200M bars are ~98% cache reads.

Root cause: `"model": "opus[1m]"` in ~/.claude/settings.json. Opus 5 has no
long-context price premium (flat $5/$25 at any length), but the 1M window
removes the auto-compact ceiling that caps per-turn cost. Session cost is
(avg context x number of API calls), growing ~quadratically with turn count.

Context distribution: calls above 400k were 16.1% of calls but 37.7% of tokens.
6 sessions of 32 burned 76% of the week (929M tokens), peaking at 734k, 593k,
555k, 501k, 449k, 446k context.

Context bloat source: 136 Read calls averaging 21,604 tokens each (one at
138,583) = 2.94M tokens, 61% of all tool-result bytes. Bash: 2,285 calls but
only 709 avg. A 21k Read at call 200 of a 947-call session is re-read 747 more
times (~15.7M tokens, ~$8 for one call).

Worst sessions:
  2718af76  5.4h   32 user msgs   947 API calls  593k max ctx  11 subagents
  a43e1fd4  8.1h   42 user msgs   718 API calls  734k max ctx
  c97b74b9 12.2h    5 user msgs   427 API calls  501k max ctx  <- runaway loop
  22e3bea2 28.4h   42 user msgs   481 API calls  555k max ctx

### Recommended fixes, not yet applied, in impact order
1. Edit ~/.claude/settings.json: "model": "opus[1m]" -> "opus". Use
   /model opus[1m] per-session only when genuinely needed. Biggest lever.
2. Read discipline: grep/rg to locate, then Read with offset/limit or
   `sed -n 'X,Yp'`. Never whole-file reads of large files.
3. /clear between tasks — one session per task (one PR review, one deploy
   verification). 28-hour sessions are a tax, not continuity.
4. ~/.claude/settings.json has "modelSettings": {"claude-opus-5":
   {"effortLevel": "high"}} overriding the global "effortLevel": "medium".
   Consider dropping the override; raise per-session when needed.
5. Cosmetic: 497MB of transcripts on disk, 305MB in cda-api-automation alone.

Items 1 and 3 alone should cut usage by more than half.

### Next step
Apply fix #1 (and optionally #4) to ~/.claude/settings.json, then re-measure
after a week using the same transcript aggregation approach.


Analyzed your actual transcripts (~/.claude/projects, Aug 30 – Sep 5). Here's what's really going on.

The chart is misleading you

That legend — 52.3k in · 19.4M out — is only the uncached slice. The 200M bars are almost entirely cache reads. Real numbers for the 7 days:

┌──────────────┬────────┐
│              │ tokens │
├──────────────┼────────┤
│ fresh input  │ 11k    │
├──────────────┼────────┤
│ output       │ 5.6M   │
├──────────────┼────────┤
│ cache writes │ 31.5M  │
├──────────────┼────────┤
│ cache reads  │ 1,196M │
└──────────────┴────────┘

213 tokens re-read for every 1 token produced. At Opus 5 rates ($5/$25 per MTok, cache read $0.50, 1-hour-TTL write $10) that's roughly $1,050 for the week — and ~$600 of it is pure re-reading of context you already paid to build.

Root cause: "model": "opus[1m]" in your global settings

This is the single biggest thing you're doing wrong. Not because 1M costs a premium — Opus 5 is flat $5/$25 at any context length — but because it removes the ceiling that used to cap your per-turn cost.

Cost of an agentic session ≈ average context × number of API calls. It grows with roughly the square of turn count. On a 200k model, auto-compact fires around 160–180k and caps that multiplier. With [1m], your sessions just keep growing:

context size    calls   % of calls    % of tokens
  0k-100k       1,569      27.4%          9.5%
100k-200k       1,863      32.6%         21.1%
200k-400k       1,371      24.0%         31.7%
400k-800k         920      16.1%   ->    37.7%   <- 16% of calls, 38% of spend

6 sessions out of 32 burned 76% of your entire week (929M tokens). Their peaks: 734k, 593k, 555k, 501k, 449k, 446k.

What's filling those contexts

┌──────┬───────┬───────────┬──────────────┐
│ tool │ calls │  ~tokens  │ avg per call │
├──────┼───────┼───────────┼──────────────┤
│ Read │ 136   │ 2,938,201 │ 21,604       │
├──────┼───────┼───────────┼──────────────┤
│ Bash │ 2,285 │ 1,620,121 │ 709          │
└──────┴───────┴───────────┴──────────────┘

136 Read calls averaging 21.6k tokens each, one at 138k tokens. That's whole-file reads with no offset/limit. And here's the killer: a 21k Read at call #200 of a 947-call session gets re-read 747 more times — that one call costs ~15.7M tokens, about $8.

Bash is fine per-call (709 avg) but you make 2,285 of them, and every output stays in context forever.

The runaway sessions

sess       hrs  usermsgs  apicalls   maxctx  subagents
2718af76   5.4        32       947  593,336         11
a43e1fd4   8.1        42       718  734,429          3
c97b74b9  12.2         5       427  501,262          0   <- 5 messages, 427 calls, 12 hours
22e3bea2  28.4        42       481  555,175          0   <- 28 hours, one session

c97b74b9 is the clearest failure: 5 user messages produced 427 API calls over 12 hours. That's an agentic loop with no checkpoint, grinding at half-a-million-token context.

Fixes, in order of impact

1. Drop [1m] from your default. Change ~/.claude/settings.json to "model": "opus". Reserve 1M for the rare session that genuinely needs it (/model opus[1m] on demand). Expected saving: the largest single lever — it forces compaction before context reaches 3–5× where it does now.
2. Stop reading whole files. Use grep/rg to locate, then sed -n 'X,Yp' or Read with offset/limit. A 138k-token Read is never justified. Your CLAUDE.md is good about routing — add a line about read discipline.
3. /clear between tasks. A 28-hour session isn't continuity, it's a tax. New topic → new session. Your work is naturally task-shaped (one PR review, one deploy verification) — one session per task.
4. "effortLevel": "high" on claude-opus-5 in your settings overrides your global medium. High effort means more thinking tokens per turn, multiplied across 400–950 calls per session. high is the right default for hard work, but it's currently applied to every trivial turn too. Consider dropping the model-specific override and keeping the global medium, raising it per-session when you need it.
5. Minor: 305MB of transcripts in cda-api-automation alone (497MB total). Doesn't cost tokens, but it's a signal of how long those sessions ran.

Items 1 and 3 alone should cut you by more than half without changing a thing about the work you do.
