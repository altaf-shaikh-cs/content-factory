## Core Insight
Most engineers who hear "build loops, not prompts" skip the one part that makes loops actually work: the verify step, and without it they are paying an AI to agree with itself in circles.

## Target Audience
Early-to-mid career engineers and AI practitioners who have heard the loop hype, are curious about agentic workflows, and want practical criteria before investing.

## Structure
1. Hook on the expensive mistake: skipping the verify step
2. What a loop actually is: 5 parts, with Verify as the heart
3. How the cost compounds per iteration (not additive, compounding context window)
4. The 4-criteria test for whether a loop is worth building at all
5. The one build order that survives in production

## CTA
What loop have you built, or what stopped you from building one?

## Tone Range
Builder-honest, educational, slightly contrarian (honest take on loop hype)

## Hashtags
#AIEngineering #AgentDesign #SoftwareEngineering #BuildingWithAI

## Image Brief
Stats/data points the image should carry:
- 50,000–200,000 tokens per loop run (single agent, one medium task)
- Below 50% acceptance rate = loop costs more than it saves
- 5 loop components: Discover, Plan, Execute, Verify, Iterate
- Tagline: "A loop without a verifier is just a spinner."
- Before/after framing: Prompt (one answer, waits for you) vs. Loop (runs the full cycle, verifies, iterates)

## Performance Context
- Best performing angle so far: Contrarian at 7.43% (1 post), Story-first avg 6.39% (2 posts)
- Hook styles that drove comments: specific uncomfortable truth, relatable developer frustration opener (gen-ai-roadmap 7.69%)
- Hook styles that drove passive reactions only: slow scene-setting, broad "I built a system" framing (routines 2.48%)
- Topics/themes that resonated: tool comparisons, practical skill-building, reframed beliefs the audience holds
- What to avoid: generic process framing, openers that set scene before delivering the uncomfortable line
- Implication for THIS post: Lead with the expensive mistake (builders skipping the verify step), which names something the audience has done or seen; Tactical angle's functional hook needs a provocative edge borrowed from Bold claim to convert rather than just inform.

## Angle Assignments
Fixed angles:
  - Angle A: Story-first — open with a personal moment or real scenario, let the insight emerge
  - Angle B: Bold claim-first — lead with the provocative insight, then back it with evidence/story

Adaptive angle:
  - Angle C: Tactical/how-to-first — Rule 2 matched: the idea contains a concrete 4-criteria checklist and a 4-step build order (reliable run first, save as reusable instructions, add a gate and stop condition, then schedule). Tactical leads with the practical outcome the other two angles structurally cannot deliver.
  - Rationale: Decision rule 2 is the first match. The idea teaches a concrete method with repeatable steps and a checklist. Story-first and Bold claim cover emotional entry and conceptual provocation. Tactical delivers the actionable framework.
