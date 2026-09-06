# token-usage-spike

**Source idea:** [../../../raw-ideas/token-usage-spike.md](../../../raw-ideas/token-usage-spike.md)
**Generated:** 2026-09-05
**Rounds:** 2  ·  **Revised:** yes
**Format:** text + image
**Rewritten 2026-09-05 (post-pipeline, by request):** refocused on the mechanism. Altaf wanted the turns themselves to be the subject: what a turn is, why every one of them re-pays for everything before it, and a worked example. The pipeline version led with the confession and the misleading chart and gave the mechanism a single line. That version is preserved below under "Confession version".

## Variation Scores (Round 1)

| Variant | Angle                        | Hook | Authenticity | Readability | Compliance | CTA | Avg |
|---------|------------------------------|------|--------------|-------------|------------|-----|-----|
| A       | Story-first                  |  8   |      9       |      9      |      9     |  9  | 8.8 |
| B       | Bold claim-first             |  9   |      7       |      9      |      9     |  9  | 8.6 |
| C       | Vulnerability/confession-first |  9 |     10       |      9      |      9     |  9  | 9.2 |

**Winner:** Variant C — the only draft whose first three lines carry all three of the confession, the hero ratio, and the admission that the reader is trusting a chart that hides 98% of the number.

**Round 2 (revised C):** avg 9.4, approved.

**The rewrite supersedes both.** The scoring above is kept as the record of how the pipeline got here, not as a verdict on what ships.

---

## Final Post

Five messages. 427 API calls. Twelve hours.

One session in my logs last week. It is the thing most people get wrong about agent cost.

You think in messages. You get billed in turns.

Here is why they are not the same.

The model has no memory. Every call re-sends the entire conversation so far: your messages, its replies, and every tool result it has collected.

So the agent reads a file, runs a command, reads another file. That is three calls. Call three carries everything from calls one and two.

Now the part that actually costs money.

In one of my sessions the agent read a 21,000-token file at call 200. That session ran 947 calls.

That file then rode along in the context for 747 more calls. Same 21k, re-sent every time.

About 16 million tokens, roughly eight dollars at list rates. For one file read.

And nothing ever leaves. Every tool result stacks on the last, so context only grows, and you pay the current size on every call.

Which gives you: cost = average context x number of calls.

Both terms grow together. So a session twice as long does not cost twice as much. It costs about four times as much.

Across the week: 213 tokens re-read for every 1 token produced. 1,196M read, 5.6M written.

The brake is auto-compact. On a 200k window it fires near 160k and caps the average. I had 1M set as my default, so it never fired.

Two fixes, neither of them a better prompt.

Drop the 1M default. Switch it on per session, when a task genuinely needs it.

Then one session per task. Clear in between.

Open your longest session from this week. Count how many API calls came out of one message.

#AIEngineering #ClaudeCode #LLM #AIAgents

---

## Why this version and not the pipeline one

The pipeline optimised for the strongest hook on this account's data, which is the confession plus a hero ratio. That produced a post whose subject was Altaf's config mistake, with the mechanism compressed into one line: "context you never compact is re-sent on every turn."

That line is the whole point, and it was doing 5% of the work.

This version inverts it. The mechanism gets the middle three quarters of the post, built on one worked example that is fully traceable to the source measurements: a 21,000-token file read at call 200 of a 947-call session, carried in the context for the remaining 747 calls, roughly 16M tokens for one read. The config fix is demoted to two lines at the end, where it belongs, because a reader who understands the mechanism can derive the fix themselves.

The opening also changed job. "Five messages. 427 API calls." is the turns-are-not-messages gap stated as a fact before any argument, which is the misconception the rest of the post exists to correct.

Cost: 300 words against a 280 target, and the 213:1 ratio is now a single line near the end rather than the hook.

---

## Images

| File | Format | Style | Carries |
|------|--------|-------|---------|
| [impact-1.svg](./impact-1.svg) | 1080×1350 (Portrait) | stat-card-dark, chart layout | "Read once. Paid 747 times." · 12-bar context-growth chart across a 947-call session with the 21k file as a constant amber slab from call 200 onward · cost formula · the quadratic note · 213:1 eyebrow · @teachmebro |
| [impact-2.svg](./impact-2.svg) | 1080×1080 (Square) | dark-terminal-cream | Headline "213 tokens read per 1 written" · the settings.json diff with both annotations · cost formula · 19.4M vs 1,196M subhead · @teachmebro |

**Exported PNGs:** `exports/impact-1.png` · `exports/impact-2.png`

`impact-1` was rebuilt for the rewrite. The first version was a stat card (hero 213:1, three tiles, chart-vs-ledger bars), which matched a post whose subject was the aggregate number. The post's subject is now the compounding, so the image had to show it: bar height is the context re-sent on that call, and the amber slab is the same 21k file appearing in every bar after call 200. The slab being identical in every bar while the bars keep growing is the argument.

`impact-2` is unchanged and still fits. It carries the cause (one line in a settings file) and the formula, which is now the post's spine rather than a footnote.

Both rendered and checked. One fix: `CALL 947` on the axis was overrunning the right margin under its letter-spacing, switched to end-anchored.

---

## Confession version (superseded 2026-09-05)

The pipeline output, kept for reference. Leads with the reversed belief and the misleading usage chart; mechanism stated once, not shown.

> I set a 1M context window as my global default because more room looked like free upside.
> 
> One week later my own logs said 213 tokens re-read for every 1 token produced.
> 
> And for most of that week I was reading the wrong chart.
> 
> The legend said 52.3k in, 19.4M out. The bars said 200M. I trusted the legend.
> 
> That legend is only the uncached slice. Roughly 98% of those bars are cache reads.
> 
> So I parsed the raw transcripts.
> 
> 11k fresh input. 5.6M output. 31.5M cache writes. 1,196M cache reads.
> 
> Priced at published list rates, about a thousand dollars for one week. An equivalence, not an invoice.
> 
> Here is what I had wrong.
> 
> Context you never compact is not stored anywhere. It is re-sent on every single turn.
> 
> So session cost is roughly average context size times number of API calls. It grows with about the square of your turn count.
> 
> One 21k-token file I read at call 200 of a 947-call session got re-read 747 more times. One read. Around 15M tokens.
> 
> The model has no long-context price premium at any length. Price was never the problem.
> 
> The problem is that a 1M window removes the auto-compact ceiling. At 200k, compaction fires near 160k and caps the multiplier for you. At 1M, nothing caps it.
> 
> 6 of my 32 sessions burned 76% of the week.
> 
> Two levers moved it, and neither was a better prompt.
> 
> Drop 1M from the global default. Switch it on per session, when a task genuinely needs it.
> 
> Then one session per task. Clear in between.
> 
> Open your longest session from this week. Count how many API calls came out of one message. Post the number.
> 
> #AIEngineering #ClaudeCode #LLM #AIAgents

---

**Unresolved issues:** 300 words against a 280 plan target, accepted. The worked example is the reason the post exists and it cannot be compressed further without breaking the causal chain.

**Ship gate:** generated with the gate at **7** unshipped posts. Overridden under the documented Mode B rule (Altaf passed the idea file directly and asked for the post), not agent judgment. This run does not reduce the backlog. Shipping `claude-four-building-blocks-20260719` still outranks publishing this one.
