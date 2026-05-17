#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: scripts/lib/extract_persona.sh PERSONA_ID" >&2
  exit 2
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
plugin_root="$(cd "$script_dir/../.." && pwd)"

python3 "$script_dir/persona_tool.py" system-prompt "$plugin_root/personas.yaml" "$1"
