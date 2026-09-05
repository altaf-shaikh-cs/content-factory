# anthropic-multi-agent-research-system

**Source idea:** [../../../raw-ideas/009-anthropic-multi-agent-research-system.md](../../../raw-ideas/009-anthropic-multi-agent-research-system.md)
**Generated:** 2026-09-03
**Rounds:** 2  ·  **Revised:** yes
**Format:** text + image
**Edited 2026-09-03 (post-pipeline, by request):** simplified. One crux instead of six statistics, and the takeaway rewritten as a rule a reader can run on their own work. The pipeline version is preserved below under "Longer version".

## Variation Scores (Round 1)

| Variant | Angle             | Hook | Authenticity | Readability | Compliance | CTA | Avg |
|---------|-------------------|------|--------------|-------------|------------|-----|-----|
| A       | Story-first       |  9   |     10       |      9      |      6     |  6  | 8.0 |
| B       | Bold claim-first  |  9   |      7       |      9      |      9     |  6  | 8.0 |
| C       | Data/number-first |  8   |      6       |      8      |     10     |  9  | 8.2 |

**Winner:** Variant C — the only draft that puts two numbers in tension in the opening lines, which is the comparison shape the tracker says top performers on this account share, and the only one that carries the argument through to a test the reader can run today.

**Round 2 (revised C):** hook 9 · authenticity 9 · readability 9 · compliance 10 · CTA 9 · **avg 9.2** — approved. Grafted in A's seven-week outage as first-person proof and B's duplication image, cut the model-upgrade aside, 296 words down to 258.

---

## Final Post

Multi-agent AI is not a speed upgrade. It is a spending decision.

Anthropic's numbers on their own research system: a multi-agent setup beat a single agent by 90.2%. It also burned about 15x the tokens of a normal chat.

That money does not buy parallelism. It buys one context window per agent instead of one shared by everything, so each worker can go deep, waste its budget on dead ends nobody else reads, and hand back only the conclusion.

You are buying room to think. Speed is a side effect.

Get it wrong and nothing crashes. Five agents on a vague brief return the same work five times, in five slightly different voices, and something has to reconcile them. You paid 15x for duplication and the logs look fine.

I found that out the slow way. Two agents in my own pipeline died and I did not notice for seven weeks, because an agent with nothing to do and a dead agent both produce nothing.

So here is the test, and it takes five minutes.

Before you split a task, write each agent's brief first. Three lines: its objective, the format it must return, and the one thing it must not touch.

If you cannot write them without overlap, the work is not independent. More agents will not fix it. Give one agent a bigger budget instead.

What is the last thing you split across agents, and could you have written those briefs for it?

#AIEngineering #AIAgents #LLM #MultiAgent

---

### First comment (post this yourself, right after publishing)

The link tax is still enforced on this account, so the blog link goes here, never in the post body.

> Wrote the long version up, including the eight prompt-engineering principles they landed on and the production failures nobody plans for: <blog URL once live>
>
> Source: Anthropic Engineering, "How we built our multi-agent research system"

---

## Images

| File | Format | Style | Carries | Pairs with |
|------|--------|-------|---------|-----------|
| [impact-2.svg](./impact-2.svg) | 1080×1080 (Square) | bold-editorial-type | Rule headline "Three Briefs. No Overlap. Then Split." · the three brief components as labelled blocks · subhead pairing context against 15x · stats +90.2% and 15x · @teachmebro · byline | **the short version (primary)** |
| [impact-1.svg](./impact-1.svg) | 1080×1350 (Portrait) | stat-card-dark | Hero 15x · tiles 90.2% / 80% / 90% · 4x vs 15x token bars · 40% tool-description line · tagline · @teachmebro · byline | the longer version |

**Exported PNGs:** `exports/impact-2.png` (120 KB) · `exports/impact-1.png` (163 KB)

`impact-2` was rebuilt on 2026-09-03 against the simplified post. The first version of it was a six-stat grid mirroring `impact-1`; four of those numbers are no longer in the post, and a card that only restates `15x` duplicates `impact-1` anyway. So it now carries the crux instead: the three-brief test, with the two surviving stats demoted to a footer row. It is the saveable half of the pair.

`impact-1` is unchanged and still matches the longer version below.

Every version was rendered and looked at before being called done. Three fixes came out of that: the `15x` bar label on impact-1 was sitting on top of its own full-width bar; the retired six-stat impact-2 had two captions overrunning a column divider and the right margin; and the rebuilt impact-2 was orphaning single words onto second lines in two of the three blocks, fixed by shortening each caption to one line.

---

**Unresolved issues:** one, accepted deliberately. At 258 words a mobile reader hits the truncation fold before the shared-state point. Everything above the fold is the hook and the two numbers, which is where it should be. Flagged so a future run does not add length.

**Ship gate:** this run was generated with the gate at 6 unshipped posts, overridden by Mode B (Altaf passed the idea directly). It does not reduce the backlog. Shipping `claude-four-building-blocks-20260719` still outranks publishing this one.

---

## Longer version (pipeline output, before the simplify pass)

Kept for reference. Carries four more statistics and the worth-it / not-worth-it split. Use it if the audience skews senior.

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
