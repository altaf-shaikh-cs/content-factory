[HANDOFF: COPYWRITER — Tactical/how-to-first]

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
Angle: Tactical/how-to-first
Hook: Two patterns for getting 92 to 96 percent of top-model quality at roughly half the cost. Benchmarked by Anthropic, reproducible in Claude Code today.
Word count: 279
