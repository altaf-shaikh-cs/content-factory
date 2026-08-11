# Post Plan — claude-code-25-tips

## Core Insight
From 25 lessons learned shipping features with Claude Code, a pattern: the tips that matter are not prompting tricks, they're engineering discipline. "AI amplifies clarity or confusion, your choice." The post curates the sharpest subset (a LinkedIn post cannot carry 25 items) around that theme.

## Target Audience
Developers using Claude Code or any AI coding agent daily; teams frustrated that their AI output quality is inconsistent.

## Structure
1. Hook: the source's own best line, "AI amplifies clarity or confusion, your choice"
2. Discipline cluster: write the spec before opening Claude (planning is 80 percent); one feature per chat ("mixing features is coding drunk"); git commit after every working feature (reverting beats fixing)
3. Trust-nothing cluster: loop tests until they pass ("should work" means it doesn't); after every completion ask "review your work and list what might be broken"; for fixes, "fix this without changing anything else"
4. Context cluster: give screenshots, schemas, docs (context is everything); keep rules files under 100 lines; start fresh at 50 percent token limit; keep a DONT_DO.md of past failures (AI forgets, you shouldn't)
5. Close: the meta-tip, "If confused, the AI is too. Clarify for yourself first."

## CTA
Open question: "Which habit changed your AI coding results the most?" Source in first comment.

## Tone Range
Tactical, direct, experienced-builder voice.

## Hashtags
#ClaudeCode #AIEngineering #SoftwareEngineering

## Image Brief
- Hero line: "AI amplifies clarity or confusion. Your choice."
- Curated tip list (6 to 8 short items) as a checklist visual
- Memorable one-liners: "mixing features is coding drunk" · "'should work' means it doesn't" · "reverting beats fixing"
- Tagline: "Discipline beats prompting tricks"

## Performance Context
- Best angles: Contrarian (7.43%), Story-first (6.39%); Bold claim-first inconsistent (3.86%) but works when arguable
- Hooks that drove comments: indictments, self-recognition
- Topics that resonated: practical skill-building (top performer was a roadmap/utility post)
- Avoid: links in body, slow hooks
- Implication for THIS post: pure utility listicle fits the audience's strongest pattern (practical skill-building). Hook should be the arguable line, not "here are 25 tips". Keep each tip one line so it reads as a save-worthy checklist; saves and comments both count.

## Angle Assignments
- Angle A: Story-first — the pattern noticed after months of shipping: every failure traced back to my own lack of clarity
- Angle B: Bold claim-first — "The best Claude Code tips have nothing to do with prompting"
- Angle C (adaptive): **Tactical/how-to-first** — decision rule 2 matched: the idea IS a concrete repeatable checklist; lead with the curated list itself
