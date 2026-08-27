# claude-auto-mode-authorization

**Source idea:** [../../../raw-ideas/claude-autoclassifier.md](../../../raw-ideas/claude-autoclassifier.md)
**Primary source:** [Anthropic Engineering, auto mode for Claude Code](https://www.anthropic.com/engineering/claude-code-auto-mode)
**Generated:** 2026-08-26
**Rounds:** 1 · **Winner:** Variant B (inversion hook), 9.2 avg, with two grafts from A
**Format:** 12-slide document carousel + caption. Third carousel produced on this account, and still none shipped, so this account has zero real carousel data.
**Note:** PR #36 (`claude/linkedin-claude-code-auto-mode-classifier`) is still open on this topic with the announcement angle. This post is the mechanism-and-decision angle and does not reuse its hook.

## Variation scores (Round 1)

| Variant | Angle | Hook | Authenticity | Readability | Simplicity | Compliance | CTA | Avg |
|---|---|---|---|---|---|---|---|---|
| A | Question hook, authorization leads | 7 | 9 | 9 | 8 | 10 | 9 | 8.7 |
| B | Inversion hook, eagerness-not-malice leads | 10 | 9 | 10 | 10 | 10 | 6 | 9.2 |
| C | Daily reveal, mechanism leads | 8 | 8 | 9 | 8 | 10 | 5 | 8.0 |

**Winner: B.** Only draft whose first two lines carry both the subject and the surprise, and the only one where nothing can be cut without losing an argument. Grafted A's closing question and A's two-month practice, attached to each half of the rule.

---

## Caption (carousel)

Written to stand alone. Someone who never swipes should still leave with the decision, so the caption carries the argument in full rather than teasing it. What it deliberately does NOT do is narrate the deck: the transcripts, the tier breakdown, the two-stage design, the block list and the closing question all live only in the slides. Overlap is limited to the four load-bearing facts, because a caption that withholds those is a caption that helps nobody.

Two months on Claude Code auto mode. Zero incidents.

Here is the part nobody talks about: we approve 93% of permission prompts anyway. That prompt was never protecting us. Our reflex was. And reflexes get tired.

There are only four ways to run a coding agent, and every one of them is a trade.

Manual prompts. Safe, and you click yes all day.
Sandboxing. Safest, and you maintain proxies and allowlists forever.
Bypass permissions. No upkeep, and no floor either.
Auto mode. The one aiming for high autonomy at low upkeep.

That last line is the entire design goal, and the chart in slide 4 is Anthropic's own.

How it gets there:

Reads and edits inside your project just run, because git is already your undo. Shell, network, external services, anything reaching outside your repo goes to a reviewer first.

And that reviewer is deliberately deaf to Claude. It sees what you asked for and the raw command. Never Claude's explanation, never its reasoning, never the file it just read.

So Claude cannot argue its way through. And a hostile instruction buried in a README cannot reach the thing holding the veto, because that thing was never shown the README.

Anthropic also published the number that does not flatter them. 17% of genuinely reckless actions still get through. One in six.

Which is exactly how I decide.

Auto mode for my repo, git-backed, me at the keyboard.
Not auto mode for prod, shared infra, unattended agents. Those get hard guardrails, not judgment calls.

One in six is a fine trade when your worst case is git reset.
It is a terrible trade when your worst case is prod.

Stop deciding from fear. Decide from how it works.

#ClaudeCode #AI #DeveloperTools #AIAgents

---

## First comment (post separately, not in the body)

The full engineering write-up is worth the read, and it is unusually candid about what still gets through:

https://www.anthropic.com/engineering/claude-code-auto-mode

---

## Images

### The deck

Built by [deck.py](./deck.py). Rebuild with `OUT_DIR=. python3 deck.py`, then re-export.

| Slide | Carries |
|---|---|
| [1](./slide-1.svg) | **The pain, felt.** The y-streak as muscle memory, a transcript of five approvals in four seconds with a destructive one sitting fourth looking exactly like its neighbours |
| [2](./slide-2.svg) | **The pain, measured.** 93% of prompts approved anyway, and the fact that attention degrades inside a session rather than improving |
| [3](./slide-3.svg) | **The move.** They did not remove the check, they replaced the reviewer. Then the inversion: not to stop a rogue agent, to stop a helpful one |
| [4](./slide-4.svg) | **The tradeoff, mapped.** Anthropic's own positioning chart redrawn in this deck's palette. Manual, sandboxing, bypass and auto mode against security and autonomy, coloured by maintenance friction, with the dashed hop showing a sandbox layered on top for defence in depth |
| [5](./slide-5.svg) | The classifier's role. Three tiers, and the fact that most actions never reach it |
| [6](./slide-6.svg) | Two-stage classification. One fast token at 8.5% false positives, full reasoning only on flags at 0.4%, almost entirely a cache hit |
| [7](./slide-7.svg) | What it judges. Authorization is not transitive, as a transcript |
| [8](./slide-8.svg) | Safety by subtraction 1. It judges actions, not arguments |
| [9](./slide-9.svg) | Safety by subtraction 2. It never reads the attack |
| [10](./slide-10.svg) | **What it catches.** Seven concrete blocks, plus the `rm -rf "$VAR"` case where it refuses because it cannot verify the target |
| [11](./slide-11.svg) | **What it misses.** 17% of real overeager actions, in Anthropic's own numbers, and why |
| [12](./slide-12.svg) | The decision. Let it run vs build a wall, and the closing question |

**Exports:** `exports/slide-1.png` .. `exports/slide-12.png` · **Upload this:** `exports/claude-auto-mode-authorization-carousel.pdf`

**Why the deck is ordered this way.** The first build opened on the inversion (rogue vs helpful), which is a good line but a cold open: it argues before the reader has agreed to anything. Restructured so the approval-fatigue story runs first. Slide 1 is pure recognition, no argument, and the 93% is deliberately held back to slide 2, because a statistic lands harder once you have already admitted the behaviour it measures. Only then does the deck reveal the mechanism, and only then does it split what it catches from what it misses, which is the pair that lets the reader decide instead of trust.

**Slide 4, the chart.** Added on request from Anthropic's own positioning graphic, redrawn rather than screenshotted so it sits in the deck's palette and type. It is the only slide that argues by comparison instead of by mechanism, and it earns the spot because "high autonomy at low upkeep" is the one claim that explains why auto mode exists at all rather than what it does. The maintenance-friction colouring is the part most people miss in the original: sandboxing is the safest option on the board and also the one you pay for every week, forever.

Slides 5 and 6 carry the classifier's role and the two-stage design, because those are the two facts that most directly reduce fear: one shows the check is narrow, the other shows why it is cheap enough to be everywhere. Without them the deck asserts that the reviewer is good. With them it shows why.

---

**Unresolved issues:** LinkedIn ship-gate status noted in TODO.md. Unshipped backlog was already past threshold before this run; generated on direct request.
