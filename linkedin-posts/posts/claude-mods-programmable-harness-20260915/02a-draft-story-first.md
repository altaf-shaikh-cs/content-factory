I opened the trending page this morning and two posts sat back to back.

The first: Claude Code shipped a mod system, and someone had already built Tetris inside it. 508,000 views in a day.

The second, directly under it: "It's been 23 days since I last opened Claude Code." He prefers Codex now, because it works better with the open models he wants to run.

I almost scrolled past both. A toy and a churn complaint.

Then I read what the Tetris mod actually was.

Eight games in TypeScript, running in the strip above the prompt while the agent works. A virtual pet that gains XP when your tests pass and loses mood when they fail. A picker that reads your session and chooses for you: recent test failure, it opens the pet. Long running turn, it opens a longer game.

And none of it costs a token. The plugin answers every keystroke itself. No model call.

That is the part worth stopping on.

The person who left went to a competitor over which models it would run. The person who stayed built a game engine into the prompt.

Neither of them is arguing about how good the model is.

I made the same call in my own pipeline. The video step is plain deterministic code, not a generative model, because a model cannot reliably spell a statistic and the statistic is the entire point of the video. Cheaper was not the reason. Exact was.

Everyone benchmarks models. Almost nobody audits the layer around them, which is the layer they live in all day and the only one they can change.

What in your stack still goes through a model call that ordinary code would do better?

#AIEngineering #ClaudeCode #LLM #DeveloperTools
