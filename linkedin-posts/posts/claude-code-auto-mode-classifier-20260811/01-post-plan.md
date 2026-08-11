## Core Insight
Claude Code's new auto mode doesn't reduce safety by removing permission prompts — it upgrades it by replacing a rubber-stamping human (13.6% catch rate) with a dedicated classifier (89% catch rate).

## Target Audience
Software engineers and DevOps practitioners using Claude Code daily: people who find permission prompts disruptive but are skeptical about letting AI manage its own permissions.

## Structure
1. The permission fatigue finding: humans catch only 13.6% of dangerous commands in prompts, falling to 5% after 50 prompts in a session
2. What auto mode actually is: a dedicated classifier reviews every action before it runs — not fewer checks, just a different reviewer
3. The dual-layer architecture: explicit user rules run first (deterministic), classifier covers everything else (probabilistic long-tail)
4. What concretely gets blocked: curl | bash, production deploys, force-push, terraform destroy, IAM changes, live credentials in transcript
5. What's allowed without a prompt: local file ops, installing from lockfiles, pushing to the working repo, read-only HTTP

## CTA
What's the one action you'd want to keep under manual review even in auto mode?

## Tone Range
Educational, conversational — let the numbers do the arguing, not the prose

## Hashtags
#ClaudeCode #AIEngineering #DeveloperTools #Claude

## Image Brief
Stats to carry:
  - 89%: classifier catch rate
  - 13.6%: human catch rate (manual prompts)
  - 5%: human catch rate after 50 prompts in a session
  - Aug 14, 2026: rollout date for Pro/Max/Team plans
Tagline: "Auto mode doesn't skip the check. It upgrades who runs it."
Before/after framing: Manual prompts (fatigued human clicking yes) vs AI classifier (consistent, purpose-built)

## Format
Text + image

Rationale: The 89% vs 13.6% numbers are the hook and should anchor both the post opening and the image. Text + image is this account's conversion format (avg 4.47% engagement rate vs 0.70% for the one meme on record). The dual-layer architecture explains linearly without needing a save-worthy carousel framework. The image carries the statistics so the post prose can earn them with context.

The last published post was the 8/9 meme (reach, zero capture). This is the conversion post sequenced to follow it — the technical content while cold-reach strangers from that meme may still be inside distribution.

## Performance Context
- Best performing angle so far: Contrarian (7.43%, ai-drinks-water) and Story-first (6.39% avg)
- Best capture rate so far: Not tracked for most posts; only the 8/9 meme has a logged capture rate (0.00%)
- Format trade: Text + image delivers 4.47% avg engagement rate vs 0.70% for the meme; memes reach 23x more people at zero conversion
- Hook styles that drove comments: Contrarian posts that name something the audience does but won't admit (ai-drinks-water, 7.43%)
- Hook styles that drove passive reactions only: Abstract process posts (routines, 2.48%)
- Topics/themes that resonated: Practical skill-building, tool comparisons, concrete numbers up front
- What to avoid repeating: Abstract "here's what I built" without a specific tension or number leading
- Implication for THIS post: The 89% vs 13.6% comparison IS the hook. Lead with the numbers, not with context. Comparison/split-screen angle has the strongest evidence base for this idea's structure, and the performance data supports it (5.15% on the claude-four-building-blocks second take — strongest conversion post of Period 3).

## Angle Assignments
Fixed:
- Angle A: Story-first — open with the moment of clicking "yes" past your 50th permission prompt, let the insight about auto mode emerge from the felt experience
- Angle B: Bold claim-first — lead with "Anthropic just put an AI in charge of reviewing Claude Code's actions. The data says humans were doing it badly." Back with 13.6% falling to 5%, then the 89% reversal.

Adaptive:
- Angle C: Comparison/split-screen-first

Decision rule matched: Rule 3 — "idea is structurally a comparison (A vs B, before/after two systems)." The core tension is human reviewers (13.6% catch rate, declining) vs AI classifier (89%, consistent). The entire architecture is organized as Layer 1 vs Layer 2. A comparison/split-screen opening forces the reader to pick a side from the first line. Performance data also supports this choice: comparison/split-screen hit 5.15% — the strongest conversion post of Period 3.
