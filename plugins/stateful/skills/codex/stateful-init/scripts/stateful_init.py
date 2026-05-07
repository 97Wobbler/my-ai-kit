#!/usr/bin/env python3
"""Codex skill-local wrapper for the shared Stateful installer."""
from __future__ import annotations

import runpy
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[4]
runpy.run_path(str(PLUGIN_ROOT / "scripts" / "stateful_init.py"), run_name="__main__")
