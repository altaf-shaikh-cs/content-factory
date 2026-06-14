# x.agent.md — Loop prompt for the X (Twitter) channel

**Status: STUB — pending the `x-growth-agent` skill.**

This file will hold the daily loop prompt for the X channel once the skill exists. Mirror the structure of [`linkedin.agent.md`](./linkedin.agent.md):

1. Compute queue from `./raw-ideas/` minus `x-posts/TODO.md` Done section
2. Filter out ideas whose frontmatter `channels: [...]` excludes "x"
3. Pick oldest by lexical filename sort
4. Trigger `/x-growth-agent` (TBD) with the idea content
5. Update `x-posts/TODO.md` Done section
6. **Do NOT move the source idea** — `raw-ideas/` is immutable and shared

## To activate this channel

1. Author `.claude/skills/x-growth-agent/SKILL.md` (likely: single tweet + thread variant + reply hook)
2. Populate `x-posts/` with `CLAUDE.md`, `README.md`, `TODO.md`, `posts/`
3. Replace this stub with the real loop prompt (use `linkedin.agent.md` as the template)
4. Update the channels status table in [`README.md`](./README.md)
