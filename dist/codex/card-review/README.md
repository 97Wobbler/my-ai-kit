# Card Review

Card Review is a dependency-free local browser workflow for reviewing lists of
tasks, proposals, documents, diffs, or other structured items one card at a
time.

It supports A/B classification, skip, memo, item navigation, undo/redo, resume,
partial completion, and a stable JSONL result keyed by source item ID. The
source input is never overwritten.

The initial release is browser-only. It does not require or include TUI Bridge.

Use `/card-review:card-review` in Claude Code or `$card-review` in Codex after
installing the plugin.

For a local smoke test, validate and launch `examples/demo-input.json` with the
bundled scripts.
