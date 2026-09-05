[HANDOFF: COPYWRITER — Data/number-first]

90.2% better answers.

15x the tokens.

Both numbers come from the same Anthropic write-up on their multi-agent research system. Everyone quotes the first one. The second one is the one that should change how you build.

One more from the same page, and this is the uncomfortable one: on their testing, token usage alone explained 80% of the performance variance.

Read that again. Most of what makes these systems better is spending more.

So multi-agent is not a clever architecture that gets you more for free. It is a purchase. What you are buying is one context window per agent instead of one for everything, which lets each worker burn its budget on dead ends nobody else has to read and hand back only the conclusion.

You are buying room to think. The speedup is a side effect.

That reframe kills the question most people are asking. It is never "should I use multi-agent." It is "is this task worth 15x."

Worth it: wide research, competitive scans, big codebase surveys. Many independent paths, and no worker needs to see another's findings.

Not worth it: anything with shared state. Which is why coding is a poor fit. Two agents editing the same file need to see each other's edits, and language is a terrible protocol for that.

And before you add agents, note what else was in there: upgrading the model beat doubling the token budget on the older one. More agents is the last lever, not the first.

Take the last task you handed to one agent that came back mediocre. Try writing three briefs for it: objective, output format, and the one thing each must not touch.

If you cannot write those three without overlap, the task is not breadth-first, and more agents will not save it.

#AIEngineering #AIAgents #LLM #MultiAgent

---
Angle: Data/number-first
Hook: 90.2% better answers. / 15x the tokens.
Word count: 296
