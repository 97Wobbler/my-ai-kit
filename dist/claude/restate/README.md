# Restate

Independent checks and interviews before execution:

- `restate`: confirm one representative understanding.
- `branch`: compare materially different interpretations.
- `xy`: check whether a proposed solution addresses the actual problem.
- `elegant`: reconsider change cost versus effect.
- `clarify`: interview against a persistent decision list, then review for
  conflicts and remaining material gaps.

## Clarify

Ask for `restate:clarify` (Claude Code: `/restate:clarify`) and describe the
requirements. The skill lists decisions, asks concise questions with options
and a recommendation, and reports actual round progress. Priorities are loose
alpha/beta/gamma hints. Technical implementation choices belong to the agent.
Request a draft or stop at any time; unresolved work remains visible.

Each question is separated from the previous decision, with brief context,
meaningful options, and a visible recommendation. At each round boundary the
skill announces a full review, reconciles queued candidates with all answers,
adds material gaps, and explains the recomposed next group and order. Queued
candidates are provisional. Interview completion is announced only after the
latest review and successful closure, not when the current questions run out.

The bundled local MCP requires Python 3.10+ with SQLite support (standard
library). No external service, token, or Python package installation is needed.
Both runtimes store interview sessions under `~/.restate/clarify`. Override
with the same absolute `RESTATE_CLARIFY_DATA_DIR` in the launching environment
to share an alternative store. Data is outside versioned plugin caches and
survives server restarts; no state is created by tool discovery alone.

MCP availability is host-managed. Codex Default mode uses plain-text questions
by default; Claude and Codex Plan Mode use permitted question tools when
available, with text as fallback. An async request being accepted does not prove
a selection UI appeared. Existing
Restate skills do not start interviews or depend on interview tool calls.
Closed sessions remain readable; new work starts a new interview with relevant
context. No automatic deletion, migration, or product implementation follows.

If a call fails or its result is uncertain, read the session before retrying.
The server preserves decisions, reasons, and round records, but it cannot prove
that the agent's interpretation or reported user evidence is correct. See
[the tool contract](references/clarify-contract.md) for exact transitions.

Feedback: open an issue at `97Wobbler/my-ai-kit` with the plugin name, runtime,
expected behavior, and observed behavior.
