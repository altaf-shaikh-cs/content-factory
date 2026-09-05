# Anthropic's multi-agent research system: what it cost and what broke

Source: https://www.anthropic.com/engineering/multi-agent-research-system (Anthropic Engineering)

## The system

Anthropic's Research feature is an orchestrator-worker multi-agent system:

- **Lead agent (orchestrator)** analyses the query, sets strategy, spawns subagents
- **Subagents (workers)** run in parallel, each with its own context window and search tools
- **Citation agent** post-processes the findings and attributes every claim to a source

It replaces static RAG with "a multi-step search that dynamically finds relevant information, adapts to new findings, and analyzes results."

## The numbers (all from the article)

- Multi-agent (Opus 4 lead + Sonnet 4 subagents) beat single-agent Opus 4 by **90.2%** on their internal research eval
- Agents use ~**4x** the tokens of a chat interaction. Multi-agent systems use ~**15x**
- On BrowseComp, three factors explained **95%** of performance variance; **token usage alone explained 80%**
- "Upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7"
- Parallel tool calling cut research time by up to **90%** on complex queries
- Better tool descriptions alone produced a **40% decrease** in task completion time

## Eight prompt-engineering principles they landed on

1. Think like your agents. Simulate with the exact prompts and tools, watch the failure modes
2. Teach the orchestrator how to delegate: objective, output format, tool guidance, task boundaries
3. Scale effort to query complexity. Embed the rules (simple: 1 agent, 3-10 calls; complex: 10+ subagents)
4. Tool design and selection are critical. "Bad tool descriptions can send agents down completely wrong paths"
5. Let agents improve themselves. Claude can diagnose its own failures and rewrite the prompt
6. Start wide, then narrow down
7. Guide the thinking process (extended thinking for planning, interleaved thinking for evaluation)
8. Parallel tool calling transforms speed (3-5 subagents at once, multiple tools per agent)

## Evaluation

- Start with ~**20 queries** representing real usage. Do not wait for a large eval set
- LLM-as-judge: one call against a rubric covering factual accuracy, citation accuracy, completeness, source quality, tool efficiency. Outputs 0.0-1.0 plus pass/fail
- Human testing stays mandatory. "People testing agents find edge cases that evals miss"

## Production problems (the interesting part)

- **Statefulness and compounding errors.** Agents run long. "Minor system failures can be catastrophic for agents." Fix: resume from where the agent was, do not restart
- **Debugging.** Agents are "non-deterministic between runs, even with identical prompts." Fix: full production tracing, monitor decision patterns rather than individual outputs
- **Deployment.** Rainbow deployments, gradually shifting traffic, so running agents are not disrupted mid-flight
- **Synchronous bottleneck.** The lead agent waits for subagents to finish. Async would unlock more parallelism but makes coordination and state consistency much harder

## The line worth stealing

"The last mile often becomes most of the journey." The compound nature of errors in agentic systems means minor issues that traditional software shrugs off can derail agents entirely.

## My angle

The 15x token number is the honest headline, not the 90.2%. Multi-agent is not a free speedup, it is buying context isolation with tokens. It only pays when the task value clears that bar: breadth-first search where subagents do not need to share state.

My own content factory is a small version of this: one shared immutable idea library, one isolated agent per channel, per-channel state files, no cross-writes. The thing that broke was exactly their debugging lesson. Two channels went silent for seven weeks and a quiet exit looked identical to a dead routine, because nothing logged a heartbeat.
