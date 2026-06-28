# launchd: daily content up-sync

`com.altaf.content-factory.open-content-prs.plist` runs `scripts/open-content-prs.sh`
**every day at 11:00 AM local time (Asia/Calcutta)** on Altaf's Mac. It pulls the
routine-generated `claude/*` branches off the fork and opens cross-fork PRs into
the private personal repo for review.

Why 11:00 AM: the cloud routines fire at 10:00 AM (X), 8:30 PM (LinkedIn), and
9:00 PM (Instagram). An 11:00 AM local run catches the prior evening's LinkedIn +
Instagram and that morning's X (after it finishes).

**Caveat:** launchd only fires when the Mac is awake/logged in. If it's asleep at
11:00 AM, the run is skipped that day — just run `bash scripts/open-content-prs.sh`
manually, or it catches everything on the next fire (branches accumulate; nothing
is lost).

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

To auto-merge instead of opening PRs for review, change `ProgramArguments` to pass
`--merge` as a third `<string>` to the script, then reload.
