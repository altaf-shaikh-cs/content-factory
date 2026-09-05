[HANDOFF: COPYWRITER — Bold claim-first]

Multi-agent is not a speed feature. It is a spending decision.

Anthropic published the engineering behind their research system, and the two numbers in it only make sense together.

A multi-agent setup beat a single agent by 90.2% on their internal research eval.

Multi-agent systems also use about 15 times the tokens of a chat interaction. A single agent already uses four.

Most people quote the first number and architect around it. The second one is what should change your design.

Because subagents are not threads. Threads share memory and coordinate for free. Agents coordinate in natural language, so every handoff is a lossy re-explanation. Hand five agents a vague brief and you do not get five times the work. You get the same work five times, in five slightly different voices, and an orchestrator that now has to reconcile them.

Nothing crashes. You just paid fifteen times over for duplication.

What you are actually buying is context isolation. One agent has one window and everything competes for it. Five agents have five windows, each free to burn context on dead ends nobody else has to read.

You are buying room to think. Speed is a side effect.

Which means the question is never "should I use multi-agent." It is "is this task worth 15x."

For a wide competitive scan, probably yes. For anything where the workers need to see each other's output, no.

What was the last task you split across agents, and did you ever measure it against the single-agent version?

#AIEngineering #AIAgents #LLM #MultiAgent

---
Angle: Bold claim-first
Hook: Multi-agent is not a speed feature. It is a spending decision.
Word count: 262
