#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: scripts/run.sh RUN_DIR" >&2
  exit 2
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
plugin_root="$(cd "$script_dir/.." && pwd)"
run_dir="$1"

if [ ! -f "$run_dir/input.md" ]; then
  echo "missing input file: $run_dir/input.md" >&2
  exit 1
fi

python3 "$plugin_root/scripts/lib/run_personas.py" "$plugin_root" "$run_dir"
