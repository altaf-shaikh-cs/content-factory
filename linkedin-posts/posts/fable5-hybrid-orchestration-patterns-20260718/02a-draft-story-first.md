[HANDOFF: COPYWRITER — Story-first]

For months my default was simple: every task goes to the biggest model.

Planning? Biggest model. Renaming a variable? Biggest model. Reading a file? Biggest model.

Then Anthropic published benchmark data that made me stop and look at my setup.

They tested two ways of mixing Fable 5 with the much cheaper Sonnet 5.

Pattern 1: the Advisor.
Sonnet 5 runs the main loop and does the work. It calls Fable 5 maybe once per task, only when it needs guidance.
Result on SWE-bench Pro: 92 percent of Fable 5's solo score at 63 percent of the price.

Pattern 2: the Orchestrator.
Fable 5 does the planning, then fans the actual work out to multiple Sonnet 5 workers.
Result on BrowseComp: 96 percent of the performance at 46 percent of the price. $18.53 per problem instead of $40.56.

And here is the part that convinced me: running everything on the cheap model was cheaper still at $16.01, but accuracy dropped from 86.8 to 77.8 percent.

So the answer is not "always cheap" either. It is structure.

I set this up in Claude Code in ten minutes. A helper role in ~/.claude/agents/worker.md on a cheaper model, and a short instructions file telling the main model what to hand off.

Planning and final review stay with the big model. Routine reads, edits, and execution go to the helper.

I was asking "which model should I use?"

The better question: which model should handle which part?

How are you splitting work across models in your agent setups?

Source links in the first comment.

#AIEngineering #AIAgents #ClaudeCode

---
Angle: Story-first
Hook: For months my default was simple: every task goes to the biggest model.
Word count: 261
