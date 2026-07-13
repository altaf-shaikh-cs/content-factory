---
name: sync-ideas
description: "Pull quick-capture notes from raw-ideas-inbox/inbox.md into the shared raw-ideas/ library as proper idea files. Use when the user says /sync-ideas, 'sync my notes', 'sync the inbox', or 'pull inbox into raw ideas'."
trigger: /sync-ideas
---

# /sync-ideas

Promotes rough notes jotted in `raw-ideas-inbox/inbox.md` into the shared, immutable `raw-ideas/` library, one file per idea, so channel agents can pick them up on their next run.

## Steps

1. Read `raw-ideas-inbox/inbox.md`. Ignore the leading HTML comment header. If there's no real content below it, report "inbox is empty" and stop — don't touch `raw-ideas/`.
2. Split the remaining content into idea chunks on lines containing only `---`. A file with no `---` at all is a single idea. Discard chunks that are blank/whitespace-only.
3. Find the next available numeric prefix: list `raw-ideas/*.md` filenames matching `NNN-*.md`, take the highest `NNN`, add 1 (zero-padded to 3 digits). Start at `001` if none exist.
4. For each idea chunk, in order:
   - Generate a short kebab-case slug from the chunk's content (gist of the first line or two).
   - Write the chunk's text **verbatim** — do not rewrite, expand, or clean up the wording — to `raw-ideas/NNN-slug.md`, using the next available prefix, then increment it for the next chunk.
5. Once all chunks are written, reset `raw-ideas-inbox/inbox.md` back to just the header comment (empty otherwise), so it's ready for new notes.
6. Report which new `raw-ideas/` files were created.

## Rules

- Never edit or remove existing files in `raw-ideas/` — it's append-only.
- Don't rephrase note content; slug generation is the only judgment call.
- If `raw-ideas-inbox/inbox.md` doesn't exist, create it with the standard header (see the file's own header comment) and stop — nothing to sync yet.
