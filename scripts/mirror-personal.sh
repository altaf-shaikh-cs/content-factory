#!/usr/bin/env bash
#
# mirror-personal.sh — refresh the personal repo as a MIRROR of the fork.
#
# TOPOLOGY (since 2026-06-28): the FORK altaf-shaikh-cs/content-factory is the
# single integration point. Cloud routines generate content there and open
# within-fork PRs; you review + merge on the fork; code lands on the fork via
# scripts/deploy-code.sh. The personal repo altafshaikh/content-factory is a
# DOWNSTREAM MIRROR — this script fast-forwards its main from the fork's main.
#
# Non-destructive: only updates FETCH_HEAD and pushes to origin/main. It never
# touches your working tree or current branch.
#
# Run by launchd daily (11:00 AM IST); safe to run by hand anytime:
#   bash scripts/mirror-personal.sh
#
# Auth: fetch is from the PUBLIC fork over https (no auth needed); push uses the
# `origin` remote (SSH github.com-personal -> personal key), which can write to
# altafshaikh/content-factory.

set -uo pipefail
cd "$(cd "$(dirname "$0")/.." && pwd)"

FORK_URL="https://github.com/altaf-shaikh-cs/content-factory.git"
BRANCH="main"

echo "[$(date '+%Y-%m-%d %H:%M:%S %Z')] mirror-personal START"

if ! git fetch "$FORK_URL" "$BRANCH"; then
  echo "ERROR: fetch from fork failed — leaving personal untouched." >&2
  echo "[$(date '+%Y-%m-%d %H:%M:%S %Z')] mirror-personal DONE"
  exit 0
fi
FORK_HEAD="$(git rev-parse FETCH_HEAD)"
echo "fork main @ $FORK_HEAD"

# Fast-forward personal main to the fork's main. Plain push (no --force): if it
# is NOT a fast-forward it FAILS LOUDLY instead of silently rewriting history —
# that would mean personal has commits the fork lacks (shouldn't happen; all
# code is supposed to land on the fork first via deploy-code.sh).
if git push origin "$FORK_HEAD:refs/heads/$BRANCH" 2>&1; then
  echo "Personal mirror updated: altafshaikh/$BRANCH <- fork/$BRANCH"
else
  echo "WARNING: could not fast-forward personal main from the fork." >&2
  echo "Likely cause: personal has commits not on the fork. Push those to the" >&2
  echo "fork first (bash scripts/deploy-code.sh), then re-run this script." >&2
fi

echo "[$(date '+%Y-%m-%d %H:%M:%S %Z')] mirror-personal DONE"
