# launchd: daily personal-mirror sync

`com.altaf.content-factory.open-content-prs.plist` runs `scripts/mirror-personal.sh`
**every day at 11:00 AM local time (Asia/Calcutta)** on Altaf's Mac.

## Topology (why this exists)

The **fork** `altaf-shaikh-cs/content-factory` is the single integration point:

- Cloud routines generate content on the fork and open **within-fork PRs**
  (`claude/<channel>-<slug>` -> fork `main`) for review.
- You review + merge those PRs **on the fork**.
- Code/config changes are pushed to the fork via `scripts/deploy-code.sh`.

The personal repo `altafshaikh/content-factory` is a **downstream mirror**.
`mirror-personal.sh` fast-forwards personal `main` from the fork's `main` so the
public repo stays current with whatever you've merged. It's non-destructive —
it only fetches the fork and pushes to `origin/main`, never touching your working
tree.

**Caveat:** launchd only fires when the Mac is awake/logged in. If it's asleep at
11:00 AM the run is skipped that day — just run `bash scripts/mirror-personal.sh`
manually. Nothing is lost: the fork is the source of truth, so the mirror simply
catches up on the next run.

## Install / reload

```bash
cp scripts/launchd/com.altaf.content-factory.open-content-prs.plist ~/Library/LaunchAgents/
launchctl bootout  gui/$(id -u)/com.altaf.content-factory.open-content-prs 2>/dev/null
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.altaf.content-factory.open-content-prs.plist
```

## Test now / inspect / uninstall

```bash
launchctl kickstart -k gui/$(id -u)/com.altaf.content-factory.open-content-prs   # run immediately
launchctl print gui/$(id -u)/com.altaf.content-factory.open-content-prs          # status + next fire
cat ~/Library/Logs/content-factory-open-content-prs.log                          # output
launchctl bootout gui/$(id -u)/com.altaf.content-factory.open-content-prs        # stop/uninstall
```
