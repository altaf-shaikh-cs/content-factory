# fable5-hybrid-orchestration-patterns

**Source idea:** [../../../raw-ideas/004-fable5-hybrid-orchestration-patterns.md](../../../raw-ideas/004-fable5-hybrid-orchestration-patterns.md)
**Generated:** 2026-07-18
**Rounds:** 1  ·  **Revised:** no

## Variation Scores (Round 1)

| Variant | Angle               | Hook | Authenticity | Readability | Compliance | CTA | Avg |
|---------|---------------------|------|--------------|-------------|------------|-----|-----|
| A       | Story-first         |  7   |      8       |      8      |      9     |  9  | 8.2 |
| B       | Bold claim-first    |  9   |      8       |      9      |     10     |  9  | 9.0 |
| C       | Tactical/how-to     |  7   |      8       |      9      |     10     |  9  | 8.6 |

**Winner:** Variant C (Tactical/how-to-first) — Editor's round-1 pick was B, but Altaf selected C manually on 2026-07-18. CTA reworded and a demo gist added to the first-comment links.

---

## Final Post

Two patterns for getting 92 to 96 percent of top-model quality at roughly half the cost. Benchmarked by Anthropic, reproducible in Claude Code today.

Pattern 1: the Advisor (escalate up).

Run Sonnet 5 as your main loop. It does the work.
Give it Fable 5 as a tool it can call when stuck, roughly once per task.
Most tokens bill at the cheap executor rate.
SWE-bench Pro result: 92 percent of Fable 5's solo score at 63 percent of the price.

Pattern 2: the Orchestrator (delegate down).

Fable 5 owns planning and final review.
It fans the actual work out to multiple Sonnet 5 sub-agents.
Most tokens bill at the cheap worker rate.
BrowseComp result: 96 percent of the performance at 46 percent of the price. $18.53 per problem vs $40.56.

Before you ask "why not all cheap": that was tested. $16.01 per problem, but accuracy dropped from 86.8 to 77.8 percent. The expensive model earns its keep at the top of the task, not inside every token.

Bonus: each sub-agent keeps its own cache, so repeated context is not paid for twice.

Setting it up in Claude Code:

1. Create ~/.claude/agents/worker.md with a cheaper model and lower reasoning effort.
2. Add a short instructions file telling the main model which tasks to hand off: routine reads, edits, execution.
3. Reuse it across projects. No rebuild needed.

Stop asking which model to use. Start deciding which model handles which part.

Which pattern made more sense to you?

Demo gist and source links in the first comment.

#AIEngineering #AIAgents #ClaudeCode

---

## Images

| File | Format | Style | Carries |
|------|--------|-------|---------|
| [impact-1.svg](./impact-1.svg) | 1080×1350 (Portrait) | stat-card-dark | Hero 46% price / 96% performance, pattern tiles (92%/63%, 96%/46%), solo vs hybrid cost bars ($40.56 vs $18.53), tagline, @teachmebro |
| [impact-2.svg](./impact-2.svg) | 1080×1080 (Square) | diagram-explainer | Side-by-side Advisor vs Orchestrator flow diagrams, hero $18.53 vs $40.56, all-cheap caution line ($16.01, 77.8%), tagline, @teachmebro |

**Exported PNGs:** `exports/impact-1.png` · `exports/impact-2.png`

---

**First-comment links (post separately, not in body):**
- Demo gist (worker.md + delegation policy): https://gist.github.com/altafshaikh/c5f0127f153362b5f5fc0f9cc3cf0fe8
- https://x.com/ClaudeDevs/status/2074606063509528855
- https://www.instagram.com/p/DaypoWancqb/?utm_source=ig_web_copy_link&igsh=NTc4MTIwNjQ2YQ==

**Unresolved issues:** none
