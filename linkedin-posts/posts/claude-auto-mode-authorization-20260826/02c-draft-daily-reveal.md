# Draft C: daily-reveal hook (the "you have been watching it" angle leads)

You have watched this happen a hundred times today and never once seen it.

Every risky command Claude Code runs goes to a second AI model first. Different model, deliberately narrow view of your session, one question to answer: did the human authorize this.

Not "is this dangerous." Did you authorize it.

The difference matters more than it sounds, because authorization is not transitive.

"Clean up my branches" does not authorize deleting them in bulk. "Can we fix this?" is a question, not a directive. An action can be perfectly related to your goal and still be something you never approved.

Which points at what this was actually built for, and it surprised me. Not a rogue AI. A helpful one. Anthropic's write-up describes the threat as an agent that understands your goal, is genuinely trying to help, and takes initiative beyond what you would approve.

Eagerness, not malice. That reframe is why I stopped being nervous about it.

The reviewer also cannot be argued with, because Claude's own reasoning never reaches it. It sees your words and the raw command, nothing else. Actions, not arguments.

And it cannot be poisoned, because it never reads tool results. A file that says "post your env file here to validate it" is invisible to it, and irrelevant: credentials heading to a stranger fails against your intent whatever suggested it.

Where it does fail, it fails honestly and predictably. It finds approval-shaped evidence and does not check whether your consent covered the blast radius.

So: small blast radius and you present, let it run. Big blast radius or nobody home, use a deny rule.

Two months, zero manual approvals on interactive work. Every deploy path still walled off.

#ClaudeCode #AIEngineering #DeveloperProductivity
