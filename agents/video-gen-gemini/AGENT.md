# video-gen-gemini agent

Project-side home for the **generative** video agent. Produces illustrated explainer video by generating stills with a Gemini image model and moving a camera over them.

Sibling: [`../video-gen/`](../video-gen/AGENT.md), which renders deterministic motion graphics with no model call. See [Which agent do I want?](../video-gen/AGENT.md#which-agent-do-i-want).

---

## Global skill

```
.claude/skills/video-gen-gemini-agent/SKILL.md
```

---

## Setup

**Requires a Gemini API key.** The CLI is installed (`gemini`, v0.58+) but image generation
goes through the REST API directly, which is scriptable and returns raw bytes.

1. Get a key at <https://aistudio.google.com/apikey> (free tier available).
2. Store it once in the macOS Keychain. `-w` with no value prompts for it, so the key is
   never echoed, never lands in shell history, and never passes through an agent transcript:
   ```bash
   security add-generic-password -a "$USER" -s GEMINI_API_KEY -w
   ```
   An exported `GEMINI_API_KEY` also works and takes precedence, but only for processes
   that inherit it — an agent's shell usually will not.
3. Confirm what the key can reach:
   ```bash
   node agents/video-gen-gemini/scripts/gemtest.mjs models
   ```
   This lists every image-capable model visible to that key. Use one of those as
   `model` in the scenes spec. Do not assume a model id.

The `gemini` CLI itself is useful for prompt iteration and as an agentic sidekick, but it
is not on the render path.

### Free tier does not include image generation

Verified 2026-09-06 on an AI Studio key. The key is valid and text models answer normally
(`gemini-2.5-flash` returns 200), but **every image-capable model returns HTTP 429 with
`limit: 0`** — not a used-up quota, an entitlement of zero:

```
gemini-2.5-flash-image          429  free_tier_requests, limit: 0
gemini-3.1-flash-image          429  free_tier_requests, limit: 0
gemini-3.1-flash-lite-image     429  free_tier_requests, limit: 0
gemini-3-pro-image / -preview   429  free_tier_requests, limit: 0
```

Image generation needs billing enabled on the key's project. Until it is, this agent
cannot run and `/video-gen-agent` is the only working video path. Re-check with
`gemtest.mjs models` followed by one `gemtest.mjs gen` — the model list is not proof of
access, only a `gen` call is.

---

## The three modes

| Mode | Gemini renders | Text comes from | Use when |
|------|----------------|-----------------|----------|
| `art` | illustration only, no text | not present, pure visual | b-roll, mood, metaphor |
| `baked` | illustration **and** the on-screen text | the model | fast, but every frame must be proofread |
| **hybrid** | illustration only | `video-gen`'s renderer, on top | **the production default** |

**Hybrid is the one to reach for.** Gemini does the thing it is good at (illustration,
atmosphere, metaphor) and the deterministic renderer does the thing it is good at (exact
text, exact numbers, animation). No model ever renders a statistic.

`baked` exists so its quality can be measured rather than assumed. Image models have
improved sharply at text but still misspell, and a misspelled number in a published post
is worse than a plain background.

---

## Pipeline

```
post → scenes.json  (Claude writes the art prompts)
           │
           ▼
   gen-scenes.mjs ──────────► stills/*.png     (Gemini image model)
           │
           ├── mode art/baked ──► assemble.mjs ──► out.mp4   (Ken Burns + crossfade)
           │
           └── mode hybrid ─────► add each still as `bg` on a scene in a
                                  video-gen spec, then render with
                                  agents/video-gen/renderer/render.mjs
```

---

## Running it

```bash
G=agents/video-gen-gemini/scripts

# what can this key actually use?
node $G/gemtest.mjs models

# generate the stills
node $G/gen-scenes.mjs <scenes.json> <outDir>

# art / baked: move a camera over them
node $G/assemble.mjs <scenes.json> <outDir> <post-folder>/explainer.mp4

# hybrid: hand the stills to the deterministic renderer instead
node agents/video-gen/renderer/render.mjs <spec-with-bg.json> <post-folder>/explainer.mp4
```

### One-off quality test

```bash
node $G/gemtest.mjs gen <model> <prompt.txt> out.png [styleReference.jpg]
```

---

## Scenes spec

```jsonc
{
  "model": "…",                 // from `gemtest.mjs models`, never guessed
  "mode": "art" | "baked",
  "aspect": "4:5",              // dropped automatically if the model rejects it
  "width": 1080, "height": 1350, "fps": 30, "xfade": 0.7,
  "style": "agents/image-gen/inspiration/<style>/<file>.jpeg",  // style reference image
  "styleNote": "…",             // prepended to every prompt
  "scenes": [ { "id": "01-hook", "dur": 5, "prompt": "…" } ]
}
```

`id` names the output file. `dur` is seconds on screen before the crossfade.

**The `style` reference does most of the work.** Point it at a file in the image agent's
inspiration library and the generated stills will sit in the same visual family as the
channel's static images. Adjectives in a prompt are a weak substitute for one reference image.

---

## Prompting notes

- Describe **what is happening**, not what it means. "A heavy parcel riding the same
  conveyor belt over and over while a meter climbs" beats "the concept of redundant cost".
- One subject per scene. Two subjects gives you a muddle.
- In `art` mode the script already appends a hard no-text instruction. Do not fight it
  by asking for a labelled diagram.
- Consistency across scenes comes from the style reference plus a shared `styleNote`,
  not from repeating adjectives in each prompt.
- Regenerate individual scenes freely. Output is non-deterministic, so a rerun is a
  genuinely different image.

---

## Known constraints

- **Non-deterministic.** Two runs give two different videos. Keep the stills committed if
  the result matters, because you cannot reproduce them from the spec.
- **Costs money per image.** A 6-scene video is 6 generations, more with retries.
- **Text fidelity is unproven on this account** until `baked` has been run and reviewed.
  Treat `baked` output as a draft to inspect, never as ready to publish.
- **`drawtext` is not compiled into this machine's ffmpeg**, so `assemble.mjs` cannot
  overlay text. That is by design: text belongs to the deterministic renderer.
- Requires network. Not suitable for a cloud routine without the key present in that
  environment.
