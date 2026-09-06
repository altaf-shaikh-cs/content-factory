[HANDOFF: COPYWRITER — Story-first]

I opened my usage chart this week and saw 200M token bars.

I had not done 200M tokens worth of work. Not close.

The legend under the chart said "52.3k in, 19.4M out." That is only the uncached slice. The bars are roughly 98 percent cache reads, and nothing on screen tells you that.

So I parsed my own session logs for the week.

11k fresh input. 5.6M output. 31.5M cache writes. 1,196M cache reads.

That is 213 tokens re-read for every 1 token produced. Valued at published list rates, the week comes out around a thousand dollars of equivalent compute. Not a bill, just what that same work prices at.

Here is the part I had wrong.

Context you never compact is not stored somewhere cheap. It is re-sent on every single turn.

Session cost is roughly average context size times number of API calls, so it grows with the square of how long you keep the session going.

One setting did it. I had the 1M model set as a global default.

There is no long-context price premium on that model. The damage is that a 1M window removes the auto-compact ceiling. On a 200k model, compaction fires around 160k to 180k and caps the multiplier. Mine never fired.

Six sessions out of 32 burned 76 percent of the week.

Two changes moved the needle. Drop the 1M default and opt into it per session. Then one session per task, clear in between.

Open your longest session from this week and count how many API calls came out of a single message. Post the number.

#AIEngineering #ClaudeCode #LLM #AIAgents

---
Angle: Story-first
Hook: I opened my usage chart this week and saw 200M token bars.
Word count: 267
