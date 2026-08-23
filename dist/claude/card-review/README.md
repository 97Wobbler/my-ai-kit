# Card Review

Card Review is a dependency-free local browser workflow for reviewing lists of
tasks, proposals, documents, diffs, or other structured items one card at a
time.

It supports A/B classification, inline local images, skip, memo, item
navigation, undo/redo, resume, partial completion, and a stable JSONL result
keyed by source item ID. The source input is never overwritten. Its skill also
checks that A/B cards fit the decision, prepares reviewer-visible presentation
packets, and keeps blind-review answer cues out of the browser input.

The initial release is browser-only. It does not require or include TUI Bridge.

Use `/card-review:card-review` in Claude Code or `$card-review` in Codex after
installing the plugin.

For a local smoke test, validate and launch `examples/demo-input.json` with the
bundled scripts.
