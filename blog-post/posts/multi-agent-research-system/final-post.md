---
title: What 15x the Tokens Actually Buys You
tags: ai-engineering, multi-agent-systems, llm-orchestration, agents, claude
seo_title: When Multi-Agent AI Systems Are Worth the Cost
seo_description: Multi-agent AI systems use about 15x the tokens of a single chat. Here is what that buys, when it pays off, and how to test it before you build.
---

<!-- 
BANNER IMAGE
============
Generate this image using Midjourney, DALL·E, Ideogram, or any image tool, then upload to Hashnode as the cover image.

PROMPT:
A dark, minimal editorial illustration. Deep charcoal background, heavy negative space. Five small enclosed circular chambers arranged in a loose arc across the lower half of the frame, each one self-contained and glowing faintly from within, none of them touching or connected to each other. Thin luminous threads rise from each chamber up to a single larger, calmer ring at the top centre of the frame, which receives them. The threads thicken slightly as they climb, suggesting accumulating weight. Muted single accent colour, warm amber, against the charcoal. Flat conceptual style, no gradients, no depth-of-field, no text, no logos, no user interface elements, no code, no photorealism, no human figures. Editorial tech-blog illustration.

Midjourney: append --ar 16:9 --style raw --v 6
DALL·E / GPT-4o: add "digital illustration, flat design, no gradients"
Ideogram: add "flat vector illustration, editorial style, tech blog"

DO NOT include: code on screens, company logos, text or titles, photorealism
-->

# What 15x the Tokens Actually Buys You

Five agents sounds better than one. So you fan out the work, watch five progress bars fill at once, and get back a report that reads beautifully and repeats itself three times. Then the bill arrives.

That is the part nobody puts in the architecture diagram. Anthropic published the engineering write-up behind their Research feature, and buried under the impressive result is the number that should actually change how you build: multi-agent systems burn about **15 times** the tokens of a chat interaction. A single agent already burns four.

## The problem

"Multi-agent" gets treated like a performance flag. Turn it on, get parallelism, ship faster. It reads like adding threads to a slow loop.

But agents are not threads. Threads share memory and coordinate cheaply. Agents coordinate through natural language, which means every handoff is a lossy re-explanation. Spawn five subagents with a vague brief and you do not get five times the work. You get the same work five times, in five slightly different voices, and a lead agent that now has to reconcile them.

The failure is quiet and expensive. Nothing crashes. You just paid fifteen times over for duplication.

## The reframe

Stop thinking of multi-agent as parallelism. Think of it as **buying context isolation, and paying for it in tokens**.

That is the whole trade. One agent has one context window, and everything it reads competes for the same space. Five subagents have five windows. Each one can go deep on a narrow slice, burn its context on dead ends nobody else has to see, and hand back only the compressed conclusion.

You are not buying speed. You are buying room to think. Speed is a side effect.

Which tells you exactly when it is worth it. Anthropic's own data makes the same point from the other direction: on their BrowseComp testing, three factors explained 95% of performance variance, and **token usage alone explained 80% of it**. Spending more tokens is most of what makes these systems better. So the question is never "should I use multi-agent." It is "is this task worth 15x."

## The solution

Their Research feature runs an orchestrator-worker pattern with three roles.

A **lead agent** reads the query, decides the strategy, and spawns subagents with specific assignments. The **subagents** run in parallel, each with its own context window and its own search tools, each returning a condensed finding rather than a transcript. A **citation agent** runs last and does one job: walk the assembled report and attach every claim to a real source.

That third role is the one most people skip. Separating "find the answer" from "prove the answer" means the researching agents are never also grading their own homework.

The result: a multi-agent setup with Opus 4 leading and Sonnet 4 subagents outperformed single-agent Opus 4 by **90.2%** on their internal research eval. And parallel tool calling cut research time by up to **90%** on complex queries.

Two details in there are easy to miss. The lead is the expensive model and the workers are the cheaper one, which is not an accident. And they note that upgrading to a better model beat doubling the token budget on the older one. More agents is the last lever you pull, not the first.

## Real walkthrough

I run a small version of this, and it broke in exactly the way their write-up predicts.

My content factory has one shared library of raw ideas and one agent per channel: blog, LinkedIn, X, Instagram. Each channel is an isolated worker. It reads the shared library, writes only into its own folder, and tracks what it consumed in its own state file. The library is append-only. No channel can write into another channel's folder. That isolation is deliberate, and it is the same bet Anthropic made: workers that never need to share state can run in parallel without coordinating.

Then two channels went dark for seven weeks and I did not notice.

Here is why. When a channel had nothing new to produce, it exited quietly. That is correct behaviour. When a channel was broken and failed before it could produce anything, it also exited quietly. From the outside, a healthy no-op and a dead routine looked identical. Both produced nothing, and nothing was the expected output most days.

The fix was one line of logging. Every run now writes a heartbeat row into an append-only log, including runs that produce nothing, recording which channel ran and what the outcome was. A weekly check reads those logs and reports which channels have gone dark, which are alive but out of ideas, and where work is stuck waiting on me.

Anthropic hit the same wall at a much larger scale and wrote it up as the debugging problem: agents are "non-deterministic between runs, even with identical prompts," so you monitor decision patterns instead of individual outputs. My version of full production tracing is a text file with one row per run. Same principle, three orders of magnitude less infrastructure.

## What makes this different from a normal system

**Delegation is a spec problem, not a routing problem.** Their guidance for the lead agent is to hand each subagent an objective, an output format, guidance on which tools to use, and explicit task boundaries. Skip the boundaries and subagents overlap. "Research the competitors" spawns four agents that all find the same three companies.

**Effort has to be scaled on purpose.** They embed the rules directly in the prompt: a simple fact-finding query gets one agent and three to ten tool calls, a genuinely complex research task gets ten or more subagents. Without that, agents default to maximum effort on trivial questions and you pay 15x for something a single search would have answered.

**Tool descriptions are load-bearing prompt text.** Rewriting their tool descriptions produced a **40% decrease in task completion time**. Nothing else changed. As they put it, bad tool descriptions can send agents down completely wrong paths, and an agent handed the wrong tool for a job does not fail loudly, it does the wrong work convincingly.

**Errors compound because agents are stateful.** A retry in normal software is cheap. A retry in an agent throws away an hour of accumulated context. Their answer is to resume from where the agent was when it failed rather than restart, and to use rainbow deployments that shift traffic gradually so a deploy never kills an agent mid-run. Minor failures that traditional software shrugs off derail agents entirely.

## When it is actually worth it

Use multi-agent when the work is breadth-first: many independent paths to explore, and the subagents genuinely do not need to see each other's findings.

Use it when the task is valuable enough to justify the token bill. Deep research, competitive scans, wide codebase surveys.

Use it when each path burns a lot of context on material the final answer does not need.

Skip it when the subtasks depend on each other's output. Skip it when everyone needs the same shared state, which is why coding is a poor fit: two agents editing the same file need to see each other's edits, and language is a terrible protocol for that. And skip it when one agent with a bigger budget would do, because upgrading the model usually beats adding agents.

## How to try it without building a platform

You do not need infrastructure to test whether this pays off for you.

**Start with the evaluation, not the architecture.** Their advice is to begin with about 20 queries that represent real usage rather than waiting for a large eval set. Twenty is enough to see a pattern. Write down what a good answer looks like for each one before you build anything.

**Score with a rubric, not a vibe.** They use a single LLM-as-judge call against a rubric covering factual accuracy, citation accuracy, completeness, source quality, and tool efficiency, returning a score from 0.0 to 1.0 plus a pass or fail. One call, one rubric, run it against every change.

**Then run the cheapest version of the pattern.** In Claude Code, define subagents as small role files and let your main session delegate to them. Give each one an objective, an output format, the tools it may use, and an explicit statement of what it must not do. Start with three to five running in parallel, which is where their parallel tool calling guidance lands too.

**Keep the human in the loop.** Their write-up is blunt about it: people testing agents find edge cases that evals miss. Run the twenty queries yourself before you trust the score.

## Try this today

Take the last task you handed to a single agent that came back mediocre. Write down what three independent subagents would each be told: the objective, the output format, and the one thing each must not touch. If you cannot write those three briefs without overlap, the task is not breadth-first and multi-agent will not save it. That five-minute test costs nothing and will tell you more than a weekend of wiring.

## Let's talk

Have you actually measured the token cost of a multi-agent run against the single-agent version of the same task, and did it clear the bar? What is your version of the heartbeat, the thing that tells you an agent is dead rather than just quiet? And for anyone who has tried multi-agent on coding specifically: did the shared-state problem bite you the way it did here, or did you find a way around it?

If this was useful, a like helps more people find it. The next one goes into the citation agent pattern on its own, because separating the finder from the verifier turns out to be useful well beyond research.

---

This continues the thread from the post on splitting work across model tiers. That one was about which model does which step. This one is about how many models, and what it costs when the answer is "more than one." If you are new here, start with the post on `/loop` and work forward.

---

## Post assets

| File | Use |
|------|-----|
| [03-banner-prompt.md](./03-banner-prompt.md) | Prompt for Midjourney / DALL·E / Ideogram |
| [02-title-options.md](./02-title-options.md) | All title options, edit frontmatter above to switch |

**Source:** [Anthropic Engineering, "How we built our multi-agent research system"](https://www.anthropic.com/engineering/multi-agent-research-system). All figures quoted are theirs.
