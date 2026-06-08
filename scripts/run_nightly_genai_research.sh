#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${GENAI_VAULT_REPO:-/output/repos/vault}"
MAX_PAPERS="${GENAI_MAX_PAPERS:-6}"
MAX_BLOGS="${GENAI_MAX_BLOGS:-6}"

cd "$REPO_DIR"

echo "[nightly-genai] start $(date -Iseconds) repo=$REPO_DIR"

# If GITHUB_TOKEN is available, make non-interactive push work over HTTPS.
# Token is not written to git config; it only lives in this process' remote URL.
if [[ -n "${GITHUB_TOKEN:-}" ]]; then
  OWNER_REPO="$(git remote get-url origin | sed -E 's#^https://github.com/##; s#^git@github.com:##; s#\.git$##')"
  git remote set-url origin "https://x-access-token:${GITHUB_TOKEN}@github.com/${OWNER_REPO}.git"
fi

# Keep local main current before adding notes. If local changes exist, do not destroy them.
git fetch origin main || true
if git diff --quiet && git diff --cached --quiet; then
  git pull --ff-only origin main || true
else
  echo "[nightly-genai] local changes already present; skipping pull"
fi

python3 scripts/nightly_genai_research_collector.py --max-papers "$MAX_PAPERS" --max-blogs "$MAX_BLOGS" --push

echo "[nightly-genai] done $(date -Iseconds)"
