# blog.agent.md — Loop prompt for the Blog channel

**Status: STUB — will route to the existing `idea-to-blog` skill.**

This file will hold the daily loop prompt for the blog channel. Mirror the structure of [`linkedin.agent.md`](./linkedin.agent.md):

1. Compute queue from `./raw-ideas/` minus `blog-post/TODO.md` Done section
2. Filter out ideas whose frontmatter `channels: [...]` excludes "blog"
3. Pick oldest by lexical filename sort
4. Trigger `/idea-to-blog` with the idea content
5. Update `blog-post/TODO.md` Done section
6. **Do NOT move the source idea** — `raw-ideas/` is immutable and shared

## To activate this channel

1. The skill already exists: `idea-to-blog`. Just confirm its output path can be steered into `blog-post/posts/<slug>-<date>/`.
2. Populate `blog-post/` with `CLAUDE.md`, `README.md`, `TODO.md`, `posts/`
3. Replace this stub with the real loop prompt (use `linkedin.agent.md` as the template; swap "LinkedIn" → "Blog", swap skill name, swap channel folder)
4. Update the channels status table in [`README.md`](./README.md)
