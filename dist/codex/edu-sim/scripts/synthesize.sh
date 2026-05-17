#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: scripts/synthesize.sh RUN_DIR" >&2
  exit 2
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
plugin_root="$(cd "$script_dir/.." && pwd)"
run_dir="$1"

python3 "$plugin_root/scripts/lib/synthesize.py" "$plugin_root" "$run_dir"
