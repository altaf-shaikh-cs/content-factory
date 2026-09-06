[HANDOFF: COPYWRITER — Bold claim-first]

Your agent's token usage has almost nothing to do with how much work it did.

Last week mine read 213 tokens for every 1 token it wrote.

The usage chart hid it. The legend said "52.3k in / 19.4M out" while the bars sat near 200M, because that legend only counts the uncached slice.

The real ledger for the week: 11k fresh input, 5.6M output, 31.5M cache writes, 1,196M cache reads.

At published list rates that is around a thousand dollars of equivalent spend. An equivalence, not an invoice.

Here is the part most people have backwards.

Context you never compact is not sitting in storage. It is re-sent on every single turn.

So a session costs roughly average context size times number of API calls. Turn count goes up, cost goes up with the square of it.

My mistake was one line: "opus[1m]" as a global default in settings.

Not because long context is priced higher. It is flat at any length.

Because a 1M window removes the auto-compact ceiling. On a 200k model, compaction fires around 160k to 180k and caps the multiplier for you. At 1M, nothing caps it.

6 sessions out of 32 burned 76% of the week. Peak contexts: 734k, 593k, 555k.

Two levers moved the number, and neither was a better prompt.

Drop the 1M from the global default. Turn it on per session, only when the task genuinely needs it.

Then one session per task. Clear between tasks.

Those two alone should cut it by more than half.

Open your longest session from this week and count how many API calls came out of a single message. Post the number.

#AIEngineering #ClaudeCode #LLM #AIAgents

---
Angle: Bold claim-first
Hook: Your agent's token usage has almost nothing to do with how much work it did.
Word count: 277
