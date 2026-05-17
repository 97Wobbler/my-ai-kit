#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: scripts/lib/check_auth.sh RUN_DIR" >&2
  exit 2
fi

run_dir="$1"
mkdir -p "$run_dir"

if [ -n "${ANTHROPIC_API_KEY:-}" ]; then
  echo "[WARN] ANTHROPIC_API_KEY is set." >&2
  echo "[WARN] Claude CLI may use API usage billing instead of a Pro/Max subscription path." >&2
  echo "[WARN] If you intended subscription usage, unset ANTHROPIC_API_KEY and re-run." >&2
fi

claude auth status --text 2>&1 | tee -a "$run_dir/auth_status.log" >&2
