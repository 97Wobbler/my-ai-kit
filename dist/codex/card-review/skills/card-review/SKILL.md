---
name: "card-review"
description: "Run a local card-based human review workflow for AI-generated tasks, proposals, documents, diffs, or other item lists. Use when the user wants to approve/reject, accept/decline, keep/discard, or otherwise classify many items with keyboard controls, persistent progress, notes, skip, undo/redo, and a final JSONL result. Do not use for a single yes/no confirmation that does not benefit from item-by-item review."
---

# Card Review

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: private Skill Forge source (not included in distribution): `card-review.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions sparingly; `request_user_input` is Plan Mode only.
- For manual file edits, use `apply_patch` and preserve unrelated user changes.
- Run the relevant validation checks before reporting completion.

## Purpose

Turn a list of reviewable items into a local browser GUI. Preserve source data
and write only `{id, result, memo?}` rows to a separate result JSONL file.

Card Review is a browser workflow. Do not imply that a terminal UI or editor
bridge is included.

## Resolve Bundled Resources

Resolve the installed Card Review package root by walking upward from the
directory containing this `SKILL.md` until one directory contains all of:

```text
scripts/review_server.py
assets/index.html
references/input-schema.md
```

Use scripts and references from that resolved package root. Do not assume a
global installation path, the private source checkout layout, or a runtime
cache path.

## Workflow

### 1. Prepare input

Accept an existing standard input JSON when the user provides one. Otherwise
inspect the source material and create a temporary or task-local
`review-input.json` without changing the original.

Read `references/input-schema.md`. The root must be one JSON object with
`version: "1"`, `option`, and a non-empty `items` array. Preserve each source
item's stable identifier in `items[].id`; never silently invent or change an ID
when the source already supplies one. Set `option.groupAName` and
`option.groupBName` to the user's terminology. Use `option.fields` to control
card order, labels, and rendering.

Do not place source document bodies in the result file. The result is keyed by
stable item ID.

Before building the full input, check that Card Review fits the decision:

- every item can answer the same independent A/B question, with `null` meaning
  unresolved rather than a third structured outcome;
- one card asks one decision and does not depend on an answer from a previous
  card;
- the reviewer can decide from the information and media shown on that card;
- fields do not expose scores, automatic selections, experiment conditions, or
  other hints the reviewer should not know; and
- obvious duplicates, overlapping intervals, or equivalent candidates have
  been removed or intentionally grouped before review.

If the task is a multi-step questionnaire, uses different decision semantics
across items, or needs coupled answers, explain that it needs a task-specific
review harness instead of forcing it into Card Review.

Build a presentation packet for the decision rather than copying the source
schema wholesale. `option.fields` defines the available field order and
renderers, but each item should contain only the fields relevant to that item;
missing fields are not displayed. Use `image` for a local image that must be
seen in the card itself. Keep explanations in the reviewer's language and
include only the context needed to make the judgment.

For a large, blind, media-heavy, structurally varied, or expensive-to-rebuild
review, inspect two or three representative normalized cards before generating
and launching the full set. Confirm the decision labels, field order, necessary
context, prohibited hints, and whether media is legible. This is an internal
preflight; ask the user only when it exposes a material choice that cannot be
resolved from the request or source evidence.

For blind review, put only anonymized reviewer-visible material in the Card
Review input. Keep candidate identity, model or strategy name, automatic
scores, experiment conditions, and deterministic shuffle mappings in a
separate analysis file. Do not reveal or combine that mapping until the review
is finished. If a launched review exposed a material answer cue, preserve its
artifacts but do not treat its results as blind evidence.

### 2. Validate input

Run:

```bash
python3 <card-review-package-root>/scripts/validate_input.py review-input.json
```

Fix validation errors in the normalized input before launching. Never modify
the user's original source merely to satisfy the review schema.

### 3. Launch the browser workflow

Run:

```bash
python3 <card-review-package-root>/scripts/review_server.py review-input.json
```

Use `--output path/to/review-results.jsonl` when the user specifies an output
path. Use `--no-browser` only when the user explicitly wants the URL without
opening a browser. Use `--dev` only while modifying the bundled frontend.

The dependency-free server binds to loopback, selects a free local port, opens
the default browser, and continuously saves the result and adjacent resume
state. Keep the process running while the user reviews. Report the printed URL,
result path, and resume-state path.

#### Optional remote viewing

Do not check for, install, or suggest `cloudflared` during an ordinary local
review. If the user is working through Codex Remote, Claude Remote, or another
remote session and asks to view a loopback-only Card Review GUI from their own
device, check whether `cloudflared` is already available in that environment.

When it is available and the user wants this access, a Cloudflare Quick Tunnel
may forward the printed loopback URL:

```bash
cloudflared tunnel --url http://127.0.0.1:<port> --no-autoupdate
```

Explain before exposing the review that a Quick Tunnel is temporary and
unauthenticated: anyone who obtains its public URL can access the review GUI
and API. Use it only for review material the user has authorized for this
temporary exposure. Report the generated URL, keep both processes running
while the review is active, and stop the tunnel when the review ends or the
user asks to close it.

If `cloudflared` is absent, state only that Quick Tunnel support is unavailable
in the current environment. Do not install it or recommend installing it unless
the user separately asks for setup guidance.

### 4. Explain controls

Tell the user:

- `←`: classify as group A;
- `→`: classify as group B;
- `↓`: skip for now while leaving the result `null`;
- `↑` or `Cmd/Ctrl+Z`: undo;
- `Cmd/Ctrl+Shift+Z`: redo;
- `M`: focus the optional memo field.

Mouse and touch users can drag the card left or right. The progress drawer
shows counts and supports direct item navigation. A memo may be added before or
after classification. Skipped and untouched items remain unresolved.

### 5. Finish and report

When the user clicks `저장하고 종료` or asks to stop, let the workflow finish
writing before reading the JSONL result. Report:

- the output path;
- counts for A, B, and `null`;
- skipped count when resume state is available;
- whether unresolved items remain.

The result preserves input order and contains every input ID:

```jsonl
{"id":"item-001","result":"A","memo":"accepted because ..."}
{"id":"item-002","result":null}
```

If the user ends early, preserve and report partial results. Do not delete the
adjacent `.state.json` while the review may be resumed. To resume, launch with
the same input and output paths.

## Operational Rules

- Prefer temporary normalized input when the source is not already in the
  Card Review schema.
- Never overwrite source input with review results.
- Treat `null` as unresolved. Use the resume-state file only when distinguishing
  skipped from untouched items is necessary.
- Keep the local server on loopback. Do not expose the unauthenticated review
  API to a LAN or public interface. The user-authorized Quick Tunnel workflow
  above is the only supported exception and must still target the loopback
  server rather than rebinding it.
- Treat image values as explicit local-file grants. Do not add unrelated files
  to the input merely to make them browser-accessible.
- Read the result only after the latest valid write completes.
- Run bundled validation before launch and report failures clearly.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit`
with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Users may invoke this workflow as `$card-review` or by asking to use Card Review.
Use `request_user_input` only in Plan Mode. In Default mode, ask a concise direct question only when a missing label, target path, or other high-impact choice blocks safe review preparation.
For manual JSON input edits, prefer `apply_patch` and preserve unrelated user files.
