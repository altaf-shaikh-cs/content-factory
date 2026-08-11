# Post Plan — loops-explained-prompt-vs-loop-agent-anatomy

## Core Insight
A prompt is an instruction; a loop is a goal with a verifier, state, and a stop condition. The engineers getting the most from AI stopped prompting agents and started designing loops that prompt their agents. Altaf independently built exactly this architecture (his content factory), which is the proof it works.

## Target Audience
Developers and AI engineers who use coding agents daily but still drive them one prompt at a time. Early-to-mid career engineers curious what "agentic" actually means in practice.

## Structure
1. The reframe: most people use AI the slowest way there is (type, wait, fix, ask again). The alternative is a loop.
2. Loop anatomy: verifier (the heart; no gate means the agent grades its own homework), state (what makes it learn), stop condition (what keeps it sane).
3. The 4-question test before building one: repeats weekly, something can auto-reject bad output, agent can do it end-to-end, "done" is objective. Miss one, keep a manual prompt.
4. The order that works: one reliable manual run → skill → loop with gate + stop → only then a schedule.
5. Personal proof: my content pipeline runs as skills wrapped in loops on a schedule, with a separate reviewer agent as the gate and a ledger file as state.
6. Honest cost note: context re-sends every pass; track cost per accepted change, not tokens.

## CTA
Open question: "Are you still prompting your agents, or designing loops yet?" Source link in first comment.

## Tone Range
Educational, authoritative, builder-honest.

## Hashtags
#AIEngineering #AIAgents #ClaudeCode

## Image Brief
- Contrast pair: Prompt = one instruction, waits for you vs Loop = goal + verify + iterate, runs itself
- Loop cycle: DISCOVER → PLAN → EXECUTE → VERIFY → ITERATE
- The 3 organs: Verifier (heart) · State (memory) · Stop condition (sanity)
- 4-question test (repeats weekly / auto-reject exists / end-to-end / done is objective)
- Tagline: "Stop prompting agents. Design loops that prompt them."

## Performance Context
- Best performing angle so far: Contrarian (7.43%) and Story-first (6.39% avg); Bold claim-first inconsistent (3.86%)
- Hook styles that drove comments: reframes and arguable indictments; self-recognition
- Hook styles that drove passive reactions only: scene-setting, capability announcements
- Topics that resonated: practical skill-building, comparisons with stakes
- Avoid: links in body, slow hooks
- Implication for THIS post: the "you're using AI the slowest way there is" indictment is the strongest opener; it makes the reader check themselves. Practical anatomy + test delivers the skill-building payoff the audience rewards.

## Angle Assignments
- Angle A: Story-first — Altaf built loops before reading the article; open with the recognition moment
- Angle B: Bold claim-first — "If you are still prompting your coding agent, you are using it the slowest way there is"
- Angle C (adaptive): **Tactical/how-to-first** — decision rule 2 matched: the idea teaches a concrete repeatable method (loop anatomy, 4-question test, the build order), material A and B cannot lead with
