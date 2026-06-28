#!/usr/bin/env bash
#
# deploy-code.sh — ship local code/config changes to the FORK.
#
# The fork altaf-shaikh-cs/content-factory is the integration point the cloud
# routines clone, and its main is the source of truth. The personal repo is a
# mirror kept current by scripts/mirror-personal.sh. So code changes must land
# on the FORK first (NOT `git push origin main`, which would diverge the mirror).
#
# Usage:
#   git add -A && git commit -m "..."     # commit your changes on main locally
#   bash scripts/deploy-code.sh           # push them to the fork's main
#   bash scripts/mirror-personal.sh       # (optional) refresh the personal mirror now
#
# Auth: pushes via the `fork` remote (git@github.com:altaf-shaikh-cs/...), which
# resolves to the work SSH key (id_ed25519_contentstack) that owns the fork.

set -uo pipefail
cd "$(cd "$(dirname "$0")/.." && pwd)"

if ! git remote get-url fork >/dev/null 2>&1; then
  git remote add fork git@github.com:altaf-shaikh-cs/content-factory.git
  echo "Added 'fork' remote."
fi

branch="$(git rev-parse --abbrev-ref HEAD)"
echo "Pushing $branch -> fork/main ..."
git push fork "$branch:main"
echo "Done. The routines will pick this up on their next run."
echo "Run 'bash scripts/mirror-personal.sh' to refresh the personal mirror now (or wait for the daily cron)."
