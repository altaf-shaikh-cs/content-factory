## Core Insight
The context you never compact is not stored, it is re-sent on every single turn, so one default setting turned a normal week of work into 213 tokens re-read for every 1 token produced.

## Target Audience
Engineers running coding agents daily (Claude Code, Cursor, Codex) on long sessions, who have seen a usage number they cannot explain and assume it reflects how much work they did. Mid-to-senior software engineers, mostly India tech hubs, per the tracker's audience profile.

## Structure
1. The number that made no sense, and the fact that the usage chart was showing only a slice of it
2. What the real ledger said: 1,196M cache reads against 5.6M output, 213 to 1
3. Why: an agent turn re-sends the whole context, so cost is average context x number of calls, and a 1M window removes the auto-compact ceiling that used to cap it
4. The two levers that actually moved it: drop the 1M default, and one session per task

## CTA
Open your longest session from this week and count how many API calls came out of a single message. Post the number.

## Tone Range
Vulnerable, then diagnostic. Builder-honest. No lecturing.

## Hashtags
#AIEngineering #ClaudeCode #LLM #AIAgents

## Image Brief
Numbers the image should carry:
- 1,196M cache reads vs 5.6M output
- 213 tokens re-read per 1 token produced
- 400k-800k contexts: 16.1% of calls, 37.7% of tokens
- 136 Read calls, 21,604 tokens average, one at 138,583
- one 21k file read at call 200 of a 947-call session = re-read 747 more times
- 5 user messages produced 427 API calls over 12 hours
Tagline: "You do not pay for the context. You pay for it again every turn."
Before/after framing: 1M window with no compaction ceiling vs a capped window, same work.

## Format
text + image. Rationale: this account's only proven converter (4.47% avg vs 0.70% for the meme), and three carousels are already built and unshipped, so a fourth deck would add inventory in a format with zero data. A reach post is roughly due by the 1-in-4-5 budget, but a token-accounting diagnosis is not meme-shaped, and the format rules say choose on the idea's shape, not variety.

## Performance Context
- Best performing angle so far: Contrarian, 7.43%, single post. Story-first close behind at 6.39% across 2.
- Best capture rate so far: unknown. Only the meme has capture data and it was 0.00%.
- Format trade: the meme bought 23x the impressions at 1/6th the engagement rate and captured nobody. Text + image is where conversion lives.
- Hook styles that drove comments: contrarian posts naming something the audience does but will not admit (ai-drinks-water).
- Hook styles that drove passive reactions only: observational humour, abstract process posts.
- Topics that resonated: practical skill-building, roadmaps, comparison framings where the reader picks a side in line one.
- What to avoid repeating: feature dumps, and reach without a bridge back to what Altaf builds.
- Implication for THIS post: the audience almost certainly has the same default set and has never looked at the ledger. Name the thing they are doing but have not admitted, which is exactly the contrarian property that scored highest, and anchor it in Altaf's own measured mistake so it is confession rather than scolding.

## Angle Assignments
- Angle A: Story-first
- Angle B: Bold claim-first
- Angle C: Vulnerability/confession-first

Chose Vulnerability/confession-first because decision rule 1 matched first: the idea contains a clear reversed belief with a measured cost. Altaf set "opus[1m]" as a global default believing a bigger window was free upside, read the usage chart as the truth for a week, and only found on inspection that the chart showed the uncached slice and that his own config, not his workload, was the cost driver. Rule 4 (hero number) also matches, but the number lands harder once the reader has admitted the behaviour, and Angle B already carries the claim-and-evidence shape.
