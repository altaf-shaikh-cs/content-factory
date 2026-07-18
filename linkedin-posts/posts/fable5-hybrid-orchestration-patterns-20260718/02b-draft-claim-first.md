[HANDOFF: COPYWRITER — Bold claim-first]

"Which model should I use?" is the wrong question.

The right question: which model should handle which part of the task?

Anthropic published benchmark data on mixing Fable 5 with the far cheaper Sonnet 5, and the numbers make the case better than any opinion.

Pattern 1: escalate up.
Sonnet 5 is the executor. It runs the whole loop and calls Fable 5 as an on-demand advisor, roughly once per task.
SWE-bench Pro: 92 percent of Fable 5's solo score at 63 percent of the price.

Pattern 2: delegate down.
Fable 5 plans. Multiple Sonnet 5 sub-agents do the work.
BrowseComp: 96 percent of the performance at 46 percent of the price. $18.53 vs $40.56 per problem.

The control group matters too. All Sonnet 5, no Fable 5 at all: $16.01, but accuracy falls from 86.8 to 77.8 percent.

Cheapest is not smartest. Most expensive is not most efficient. The win is in the split.

A useful detail: each sub-agent keeps its own cache, so repeated context is not billed again across calls.

You can do this in Claude Code today. Define a worker role in ~/.claude/agents/worker.md with a cheaper model and lower reasoning effort. Add a short instructions file that tells the main model what to hand off. It carries across projects.

Planning and final review go up. Routine reads, edits, and execution go down.

How are you splitting work across models in your agent setups?

Source links in the first comment.

#AIEngineering #AIAgents #ClaudeCode

---
Angle: Bold claim-first
Hook: "Which model should I use?" is the wrong question.
Word count: 262
