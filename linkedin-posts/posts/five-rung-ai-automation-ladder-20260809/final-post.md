# five-rung-ai-automation-ladder

**Source idea:** [../../../raw-ideas/007-five-rung-ai-automation-ladder.md](../../../raw-ideas/007-five-rung-ai-automation-ladder.md)
**Generated:** 2026-08-09
**Rounds:** 2  ·  **Revised:** yes
**Format:** Document carousel (8 slides, 1080×1350) + caption. First carousel on the account.

## Variation Scores (Round 1)

| Variant | Angle                 | Hook | Authenticity | Readability | Compliance | CTA | Avg |
|---------|-----------------------|------|--------------|-------------|------------|-----|-----|
| A       | Story-first           |  8   |      9       |      9      |     8      |  9  | 8.6 |
| B       | Bold claim-first      |  9   |      8       |      9      |     9      |  9  | 8.8 |
| C       | Tactical/how-to-first |  7   |      8       |      9      |     9      |  9  | 8.4 |

**Winner:** Variant B — B is the only variant that opens on an indictment the reader has a stake in arguing with, which is the hook property the tracker credits for the account's strongest posts and the one the 2.48% routines post lacked.

**Revised score (Round 2):** 9.2 — approved.

---

## Final Post

Most people who say they built an agent team are doing rung-1 work with a bigger bill.

Not because they picked the wrong tool. Because they jumped.

AI automation is a ladder: prompt, skill, loop, routine, agent team. A rung only holds if the rung below it is reliable.

Skip one and it shows up as work you never agreed to. I shipped a build where every screen existed and no feature worked, because nothing in the system verified a flow end to end. So I fixed the screens one at a time, by hand. Rung-5 ambition on rung-1 machinery.

Two quick tells. If you retype the same context every session, you are on rung 1, and a saved skill is your next move, not an agent team. If you went straight to a team of agents, you are not on rung 5 at all.

The full diagnostic, one symptom and one next move per rung, is in the deck.

Be honest about the rung you are on, not the one you talk about. Which one did you try to skip?

#AIEngineering #AIAgents #SoftwareEngineering #BuildingWithAI

---

## Carousel

**Upload:** `exports/five-rung-ladder-carousel.pdf` (8 pages, 1080×1350, 481 KB, vector)
**Style:** Layout: diagram-explainer · Typography and palette: bold-editorial-type
**Source:** `deck.py` regenerates all 8 SVGs. Rebuild: `OUT_DIR="$PWD" python3 deck.py`

| Slide | File | Carries |
|-------|------|---------|
| 1 | [slide-1.svg](./slide-1.svg) | Hook: "Your AI automation didn't fail. You skipped a rung." Highlighter swipe on the turn, rung names as a mono strip |
| 2 | [slide-2.svg](./slide-2.svg) | The ladder. Five bars, width encodes how much you handed over, rung 1 bottom to rung 5 top. The saveable slide |
| 3 | [slide-3.svg](./slide-3.svg) | Rungs 1 and 2. Prompt (you are memory, planner, checker) vs Skill (written once, picked up when it fits) |
| 4 | [slide-4.svg](./slide-4.svg) | Rung 3. The three parts a prompt lacks: verifier, state, stop. Callout: an agent agreeing with itself on repeat |
| 5 | [slide-5.svg](./slide-5.svg) | Rungs 4 and 5. Routine (the trigger stops being you) and Agent team (maker split from checker) |
| 6 | [slide-6.svg](./slide-6.svg) | The rule, plus the non-negotiable order: manual run, skill, loop with a gate, then schedule |
| 7 | [slide-7.svg](./slide-7.svg) | The diagnostic. Five symptoms, five rung chips, five next moves. Second saveable slide |
| 8 | [slide-8.svg](./slide-8.svg) | The maintenance cost, the four-question gate, and the CTA |

**Exported PNGs:** `exports/slide-1.png` through `exports/slide-8.png`

---

## Publishing notes

- Upload the PDF via **Add a document**, not as images. Suggested document title: `The Five-Rung AI Automation Ladder`. The document title shows in the feed, so it is a second hook.
- No links in the body. Nothing to put in the first comment for this post, so seed the comments with your own rung instead.
- This is the account's first carousel, so there is no format baseline. Judge it on engagement rate against the 4.0% baseline, not on impressions, and log swipe depth from the LinkedIn post analytics page since the aggregate export will not carry it.

---

**Unresolved issues:**
- Caption is 176 words against the 130 to 160 target. Accepted: the overage is entirely the build-evidence paragraph, which is the only concrete proof in the caption.
- Caption names the five rungs inline, which slide 2 also carries. Accepted: it makes the claim parseable for someone who never swipes.
