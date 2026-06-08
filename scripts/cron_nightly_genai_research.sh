#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${GENAI_VAULT_REPO:-/output/repos/vault}"
LOG_DIR="$REPO_DIR/.collector-state"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/last_cron_run.log"

if "$REPO_DIR/scripts/run_nightly_genai_research.sh" >"$LOG_FILE" 2>&1; then
  # Silent success: Hermes no_agent cron sends nothing for empty stdout.
  exit 0
else
  code=$?
  echo "nightly GenAI vault collection failed with exit code $code"
  echo "--- log tail ---"
  tail -80 "$LOG_FILE" || true
  exit "$code"
fi
