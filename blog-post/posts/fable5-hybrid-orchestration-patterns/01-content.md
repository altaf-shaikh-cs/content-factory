<!-- 
BANNER IMAGE
============
Generate this image using Midjourney, DALL·E, Ideogram, or any image tool, then upload to Hashnode as the cover image.

PROMPT:
[filled in from Phase 3]

Midjourney: append --ar 16:9 --style raw --v 6
DALL·E / GPT-4o: add "digital illustration, flat design, no gradients"
Ideogram: add "flat vector illustration, editorial style, tech blog"

DO NOT include: code on screens, company logos, text or titles, photorealism
-->

# Two Patterns for Running Fable 5 at a Fraction of the Cost

You've got the best model available. Every task goes through it. Every read, every edit, every routine step. It's great work. It's also the most expensive way to get it done.

That's the default setup for most people building agents right now: pick the strongest model, route everything through it, pay the top rate for every token regardless of whether the task actually needed that much reasoning.

## The problem

"Which model should I use?" feels like the right question to ask when you're setting up an agent. It isn't. It's a single-variable question applied to a multi-step problem, and it quietly bakes in an assumption: that every step in a task deserves the same amount of model.

Planning a task and executing a routine file edit are not the same kind of work. But if you've only got one model wired into your loop, they get billed the same way. You either overpay for the easy 90% of the work, or you underpower the hard 10% by defaulting to something cheaper across the board.

## The reframe

The right question isn't "which model." It's "which model for which part of this task."

Anthropic published benchmark data on two concrete ways to do that: mixing Fable 5 with Sonnet 5 in a structured workflow instead of routing every token through the most expensive model. Both patterns get you most of Fable 5's performance while paying mostly Sonnet 5 rates.

## The solution: two patterns

**Pattern 1: Advisor (escalate up).** Sonnet 5 runs the main loop as the executor. It calls Fable 5 as an on-demand advisor only when it needs guidance, roughly once per task, to steer rather than to do the work. Most tokens get billed at the cheaper executor rate. On SWE-bench Pro, this setup hit 92% of Fable 5's solo score at 63% of the price.

**Pattern 2: Orchestrator (delegate down).** Fable 5 handles planning, then fans the actual work out to multiple Sonnet 5 worker sub-agents. Most tokens get billed at the cheaper worker rate. On BrowseComp, this hit 96% of Fable 5's solo performance at 46% of the price: $18.53 versus $40.56 per problem, 86.8% versus 90.8% accuracy.

Worth calling out what didn't work: running everything on Sonnet 5 was cheaper still, at $16.01 per problem, but accuracy dropped to 77.8%. The savings from the hybrid patterns aren't "use the cheap model everywhere." They're "use the expensive model only where it earns its keep."

One more detail that matters if you're actually building this: each sub-agent keeps its own cache, so repeated context doesn't get paid for multiple times across calls.

## Real walkthrough

Here's where it turns from a benchmark into something you can wire up today. In Claude Code, you can define lightweight helper roles in `~/.claude/agents/worker.md`: a role that runs on a cheaper model (Sonnet or Haiku) at a lower reasoning effort than your main loop.

A short instructions file tells the main model which kinds of tasks to hand off to that worker role instead of handling them itself. Planning and final review stay with the main model. Routine reads, edits, and execution get delegated to the cheaper helper. Once it's set up, it's reusable across projects without rebuilding the pattern each time.

That's the Advisor and Orchestrator patterns in miniature: your main model isn't disappearing, it's just no longer doing everything itself.

## What makes it different

**It reframes cost as a routing problem, not a model-choice problem.** You're not choosing one model for the whole task. You're deciding, per step, which model that step actually needs.

**The savings come from where the expensive model sits, not from avoiding it.** Fable 5 still does the planning and the steering in both patterns. It's just not burning tokens on the parts that don't need it.

**Per-agent caching means delegation doesn't multiply your context costs.** Fanning work out to sub-agents sounds like it should get expensive fast. The cache-per-sub-agent detail is why it doesn't.

**It's a workflow, not a one-off trick.** Once the worker role is defined, the routing decision happens automatically on every run, not manually every time you start a task.

## When to use it

- Any agent loop where most steps are routine but a few genuinely need the strongest available reasoning
- Tasks that decompose into independent sub-tasks a worker model can execute in parallel
- Anywhere you've been defaulting to the top-tier model out of habit rather than necessity

## How to set it up

In Claude Code, create the worker role file:

```
mkdir -p ~/.claude/agents
```

Then define the role in `~/.claude/agents/worker.md`. Specify the cheaper model, a lower reasoning effort, and the kinds of tasks it should own (routine reads, edits, execution). In your main loop's instructions, add a line telling it which tasks to hand off to that worker role instead of doing them itself.

That's the whole setup. No new infrastructure, no separate orchestration service. The routing lives in the same instructions file you're already using.

## Try this

Look at your current agent setup and ask which steps in your last few runs actually needed your strongest model, and which ones were routine work that got the expensive treatment out of habit. Pick one of those routine steps and hand it to a cheaper worker role instead.

## Let's talk

Have you split a workflow across model tiers like this before, and did the accuracy hold up the way the benchmarks suggest it should? Where's the line for you between "this needs the best model" and "this is routine enough to delegate"? And if you've tried an all-cheap-model setup like the Sonnet-only baseline here, what did it cost you in accuracy?

If this was useful, a like helps more people find it. Part two will look at how this holds up once the worker role has real project history behind it.

---

This builds on the same idea as the last post: systems that run themselves need more than a schedule, they need the right model doing the right amount of work at each step. If you're new to that thread, start with the post on `/loop` and come back here.

