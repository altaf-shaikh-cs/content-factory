#!/usr/bin/env bash
#
# open-content-prs.sh — pull routine-generated content from the fork up to the
# private personal repo, as reviewable PRs.
#
# WHY: cloud routines run on the work account and push their output to
# `claude/<channel>-<date>` branches on the FORK (altaf-shaikh-cs). They CANNOT
# open a PR into the private personal upstream (altafshaikh) because the cloud
# only holds the work-account token and the parent is private. THIS machine has
# the personal token, so the cross-fork PR must be opened here.
#
# This script finds fork branches named `claude/*` that don't already have an
# open PR on the personal repo, and opens one PR each (base = personal main).
# You then review + merge on GitHub; afterwards run `scripts/sync-fork.sh` to
# realign the fork.
#
# Usage:
#   bash scripts/open-content-prs.sh          # open PRs for all new claude/* branches
#   bash scripts/open-content-prs.sh --merge  # also auto-merge (squash) each PR, then sync the fork
#
# Requires: gh authenticated with BOTH accounts (personal token must have access
# to altafshaikh/content-factory).

set -uo pipefail

UPSTREAM="altafshaikh/content-factory"
FORK="altaf-shaikh-cs/content-factory"
FORK_OWNER="altaf-shaikh-cs"
AUTO_MERGE="${1:-}"

mapfile -t branches < <(gh api "repos/$FORK/branches" --jq '.[].name' 2>/dev/null | grep '^claude/' || true)

if [ "${#branches[@]}" -eq 0 ]; then
  echo "No claude/* content branches on the fork. Nothing to pull up."
  exit 0
fi

opened=0
for br in "${branches[@]}"; do
  # Skip if a PR for this head already exists on the upstream.
  existing=$(gh pr list --repo "$UPSTREAM" --head "$br" --state all --json number --jq '.[0].number' 2>/dev/null)
  if [ -n "$existing" ]; then
    echo "PR already exists for $br (#$existing) — skipping."
    continue
  fi
  title="content: ${br#claude/}"
  url=$(gh pr create --repo "$UPSTREAM" --base main --head "$FORK_OWNER:$br" \
        --title "$title" --body "Routine-generated content from fork branch \`$br\`. Review and merge." 2>&1)
  if echo "$url" | grep -q "github.com"; then
    echo "Opened PR: $url"
    opened=$((opened+1))
    if [ "$AUTO_MERGE" = "--merge" ]; then
      gh pr merge "$url" --repo "$UPSTREAM" --squash --delete-branch 2>&1 | sed 's/^/  merge: /'
    fi
  else
    echo "FAILED to open PR for $br:"; echo "$url" | sed 's/^/  /'
  fi
done

if [ "$AUTO_MERGE" = "--merge" ] && [ "$opened" -gt 0 ]; then
  echo "Realigning fork after merges..."
  bash "$(dirname "$0")/sync-fork.sh" || true
fi

echo "Done. Opened $opened PR(s) on $UPSTREAM."
