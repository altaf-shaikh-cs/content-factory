[HANDOFF-2: REVISED DRAFT — Data/number-first]

Multi-agent beat a single agent by 90.2% on Anthropic's own research eval.

It also cost about 15x the tokens of a chat interaction.

Everyone quotes the first number. The second one is what should change your design.

And one more from the same write-up, the uncomfortable one: token usage alone explained 80% of the performance variance in their testing.

Most of what makes these systems better is spending more.

So multi-agent is not a clever architecture that gets you more for free. It is a purchase. What you buy is one context window per agent instead of one shared by everything, which lets each worker burn its budget on dead ends nobody else has to read and hand back only the conclusion.

You are buying room to think. The speedup is a side effect.

Skip that reasoning and the failure is silent. Five agents on a vague brief return the same work five times, in five slightly different voices, and an orchestrator that now has to reconcile them. Nothing crashes. You just paid fifteen times over for duplication.

I learned the quiet-failure part the hard way on my own pipeline. Two agents in it went dark for seven weeks and I did not notice, because an agent with nothing to do and an agent that died before it could do anything exit identically. Both produce nothing, and nothing was the expected output most days.

So the question is never "should I use multi-agent." It is "is this task worth 15x."

Worth it: wide research and codebase surveys, where the paths are independent and no worker needs to see another's findings.

Not worth it: anything with shared state, which is why coding is a poor fit. Two agents editing one file need to see each other's edits, and language is a terrible protocol for that.

Take the last task you gave one agent that came back mediocre. Try writing three briefs for it: objective, output format, and the one thing each must not touch.

If you cannot write those three without overlap, the task is not breadth-first, and more agents will not save it.

#AIEngineering #AIAgents #LLM #MultiAgent

---
Angle: Data/number-first
Changes made:
- Rewrote the hook so both numbers sit inside the same comparison in two lines, instead of a bare stat card that took three lines to become a claim
- Grafted in the seven-week outage from Angle A as first-person proof, placed after the reframe so the number still leads
- Grafted in Angle B's duplication line, which shows the cost instead of asserting it
- Cut the "upgrading the model beat doubling the token budget" aside
- Tightened the worth-it and not-worth-it lists to one line each
Borrowed from runner-up: B's five-agents-five-voices duplication image, and A's quiet-agent versus dead-agent observation
Word count: 258
