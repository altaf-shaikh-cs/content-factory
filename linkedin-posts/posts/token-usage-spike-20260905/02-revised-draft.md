[HANDOFF-2: REVISED DRAFT — Vulnerability/confession-first]

I set a 1M context window as my global default because more room looked like free upside.

One week later my own logs said 213 tokens re-read for every 1 token produced.

And for most of that week I was reading the wrong chart.

The legend said 52.3k in, 19.4M out. The bars said 200M. I trusted the legend.

That legend is only the uncached slice. Roughly 98% of those bars are cache reads.

So I parsed the raw transcripts.

11k fresh input. 5.6M output. 31.5M cache writes. 1,196M cache reads.

Priced at published list rates, about a thousand dollars for one week. An equivalence, not an invoice.

Here is what I had wrong.

Context you never compact is not stored anywhere. It is re-sent on every single turn.

So session cost is roughly average context size times number of API calls. It grows with about the square of your turn count.

One 21k-token file I read at call 200 of a 947-call session got re-read 747 more times. One read. Around 15M tokens.

The model has no long-context price premium at any length. Price was never the problem.

The problem is that a 1M window removes the auto-compact ceiling. At 200k, compaction fires near 160k and caps the multiplier for you. At 1M, nothing caps it.

6 of my 32 sessions burned 76% of the week.

Two levers moved it, and neither was a better prompt.

Drop 1M from the global default. Switch it on per session, when a task genuinely needs it.

Then one session per task. Clear in between.

Open your longest session from this week. Count how many API calls came out of one message. Post the number.

#AIEngineering #ClaudeCode #LLM #AIAgents

---
Angle: Vulnerability/confession-first
Changes made:
- Grafted in the re-read illustration (one 21k-token file at call 200 of a 947-call session, re-read 747 more times, ~15M tokens) directly after the mechanism line. It is the only fact in the post the reader can act on within the hour, and it turns the abstract "context times calls" formula into something they can picture.
- Paid for it by cutting the standalone 5.4-hour session detail. The 947-call figure survives inside the new line, so nothing was lost.
- Added the cost anchor borrowed from Draft A, explicitly labelled "an equivalence, not an invoice" so it cannot read as a published bill.
- Moved the chart line to present tense ("That legend is only the uncached slice") so it indicts the reader's own dashboard rather than describing a past one.
- Borrowed Draft B's "and neither was a better prompt" clause to pre-empt the assumption that this is a prompting problem.
- Trimmed 277 to 286 after the two additions, then cut back through redundant phrasing to hold near the ceiling.
Borrowed from runner-up: A's list-rate cost anchor; B's "neither was a better prompt" transition.
Word count: 286
