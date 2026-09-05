[HANDOFF: COPYWRITER — Story-first]

Two agents in my content pipeline went dark for seven weeks.

I did not notice.

Here is why. When an agent had nothing new to make, it exited quietly. Correct behaviour. When an agent was broken and died before it could make anything, it also exited quietly.

From the outside those two are byte-identical. Both produce nothing. And nothing was the expected output most days.

The fix was one line of logging. Every run now writes a row saying which agent ran and what happened, including the runs that produce nothing. Especially those.

Anthropic hit the same wall building their research system, at a scale where it actually costs money. Their write-up puts it plainly: agents are non-deterministic between runs, even with identical prompts. So you stop grading individual outputs and start watching decision patterns.

That is the part the architecture diagrams leave out. Multi-agent is not hard because coordination is hard. It is hard because agents are stateful and long-running, so a minor failure that normal software shrugs off compounds into an hour of wasted context.

Their answer: resume from where the agent failed instead of restarting. Shift deploys gradually so you never kill an agent mid-run.

Mine was a text file with one row per run.

Same principle. Three orders of magnitude less infrastructure.

If you are running more than one agent right now: what tells you one of them is dead rather than just quiet?

#AIEngineering #AIAgents #LLM #MultiAgent

---
Angle: Story-first
Hook: Two agents in my content pipeline went dark for seven weeks.
Word count: 233
