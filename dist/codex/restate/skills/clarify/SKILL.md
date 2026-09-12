---
name: "clarify"
description: "Run a requirements interview with a persistent decision list, visible round progress, and contextual review. Use when the user requests clarify, 요구사항 인터뷰, 모호함 해소, or a tracked clarification interview. Use restate for a single understanding check and branch for a quick interpretation comparison."
---

# Clarify

This skill was compiled from a Skill Forge runtime-neutral spec for the
Codex CLI runtime.

Source spec: private Skill Forge source (not included in distribution): `clarify.skill.md`

Do not edit this generated file directly. Update the source spec, then
recompile and review the generated output.

## Runtime Notes

- Ask clarification questions sparingly; `request_user_input` is Plan Mode only.

# Clarify

Turn unclear requirements into decisions through a small, tracked interview.
Keep judgment in the conversation and use the bundled MCP for durable records
and honest progress. Do not implement the requested product during this skill.
Do not start a managed interview for a request that only asks for design advice,
a single paraphrase, or a quick comparison of interpretations.

## Inventory

1. Read the original request and relevant available context. Identify only
   decisions whose answers materially change the user's outcome, scope, or
   acceptance criteria and cannot responsibly be owned by the agent. Do not
   ask the user to choose routine algorithms, modules, libraries, or data
   structures. Calculation semantics can still be a product decision.
2. Give each item one concrete decision boundary, its impact, and why the user
   needs to decide. Prioritize approximately: alpha = audience/purpose/core
   identity; beta = direction/core behavior; gamma = experience/acceptance
   detail. These are ordering hints, not completeness percentages or gates.
3. Show a short initial list in the user's language. Create the session with
   `clarify_session_create`, preserving the original request and context. Choose
   a stable session ID before calling; keep IDs out of normal user-facing prose.
   Supply an explicit workspace label, or empty for projectless work. Record
   decisions already answered by the request without asking them again.
4. If resuming a known interview, read that exact session. Otherwise list with
   the known workspace and match its title/context; clarify the target only if
   several sessions remain plausible. Never attach to the globally latest one.
   State persists outside the conversation; summarize it after a context reset.

## Interview

Start a round with `clarify_round_start`. It fixes membership and records the
starting question order. Pass `ordered_item_ids` for a reconsidered order;
include every open item exactly once. Prioritize prerequisites and material
impact using alpha/beta/gamma as loose hints. Adapt wording to each answer,
skip items already answered, and do not prewrite a rigid interview script.

- Ask one concern at a time using a short question, enough context to understand
  the consequence, 2-5 meaningful options within tool limits, and a recommended
  option with its reason. Accept custom answers and mixed choices when coherent.
  Do not invent weak alternatives to fill a format. Follow the host's question
  rules when a tool or plain-text format has different restrictions.
- Make the current question visibly distinct from the previous answer's
  acknowledgment. After a successful record, summarize the previous decision
  in at most one sentence, then use a separate question block: a bold question,
  brief context, distinct options, and a clearly marked recommendation/reason.
  Never bury the next question in the last line of a decision summary. For a
  simple free-form question, keep the block short instead of inventing choices.
  Use the user's language and allow a custom answer. See the contract examples.
- Ground recommendations in the established product purpose. Use concrete
  actors and situations for ambiguous terms or permissions. Keep unrelated
  operational exceptions out of the current choice; explain them separately
  only when they materially affect this decision.
- Record actual relevant answer evidence with `clarify_items_update`. A single
  answer can settle several items in one batch. `partial` leaves an item open;
  a complete answer becomes `user_decided`. A recommendation is not agreement.
- Apply the same materiality/ownership test to follow-up questions. Once the
  original decision is answered, do not keep it open for optional refinement.
  A separate material decision becomes a new candidate for the next round.
- Keep `user_delegated`, `agent_owned`, `deferred`, and `inapplicable` distinct.
  Delegation and deferral require real user evidence. Agent-owned disposition
  applies only to items identified as agent implementation decisions. Do not
  silently relabel a product choice to empty the list. Explain why an obsolete
  item is inapplicable; preserve it instead of deleting it.
- Apply a complete correction directly with `record`, retaining the old
  evidence. Use `reopen` only if a changed premise leaves an unresolved choice
  or conflict. New/reopened candidates do not expand the current denominator.
- Use returned progress for brief updates at round start/end or when asked.
  Say “이번 라운드 6개 중 4개 처리, 추가 검토 후보 1개” only when that is
  the stored state. Carried items must be shown separately from handled ones.
  Never invent the total questions or rounds remaining. Avoid displaying
  internal state tables after every answer.

## Review and next round

When all current items are processed, briefly announce that this round's
answers are complete and the whole interview will now be reviewed. Then:

1. Compare accumulated answers with earlier context, each other, the whole
   current goal/scope, and all queued candidates. Look beyond the candidate
   list for contradictions, gaps, and previously missed decisions. Do not
   broaden the product just to find more questions; zero new items is valid.
2. Reconcile candidates before starting another round. Record already answered
   candidates with the actual user evidence. Mark obsolete or duplicate items
   `inapplicable` with the reason and supporting context; for duplicates, name
   the retained item's ID and preserve all distinct unresolved choices there.
   If necessary add a replacement item covering the combined decision. Preserve
   original records; do not delete items or silently treat inference as consent.
   New items need the same impact/ownership rationale; reopening needs a changed
   premise. User deferral still requires user evidence.
3. Recompose the remaining questions by prerequisites and current importance,
   not discovery order or an automatic replay of queued candidates. Record
   `clarify_round_review` with what was checked, which candidates were retained,
   resolved or consolidated, any new items, and the reason for the next order.
   Finish candidate changes before this review; later content changes require
   a fresh review before the next round.
4. Briefly show the actual review result and proposed next question group,
   including whether any new gaps were found. If open items remain, start the
   next round with those IDs in `ordered_item_ids`, then present its first
   question as a separate block. No extra approval or long review report is
   needed. Candidates are provisional until this review, not a scheduled round.

The visible transition is: round answers complete → actual contextual review →
review result and recomposed group → next question. A tool call or the phrase
"reviewed" does not by itself establish that this semantic work was done.

If a newly discovered prerequisite makes the remaining questions unanswerable,
record that prerequisite as a queued item. Review with `interruption_reason`
and its `prerequisite_ids`; the remaining items carry forward unresolved.
Explain the interruption briefly and keep the original round record. This is
not user deferral or successful round completion. Use this exception only for
a real prerequisite, not as a way to skip difficult questions.

## Summary and stopping

Zero pending questions means this round's answers are complete, not that the
interview is over. Use returned progress: if `review_current` is false, say
review is still needed; do not say "no more questions" or "interview complete".
Document writing, formatting, and link checks do not replace contextual review.
If the latest content has been reviewed and no open items remain, close with
`clarify_session_close` (`completed`). Announce completion only after the tool
returns `status: completed`. An uncertain/failed close is not success. An empty
initial inventory still receives a short review but needs no invented question.
Any content change after review needs a fresh review before natural completion.

When the user requests a draft or asks a side question, provide it using current
decisions and labeled open issues without closing the interview. When they ask
to stop, close as `stopped` with user evidence and retain unresolved work. Do
not force more questions or silently switch to product implementation.

Provide a concise, reusable summary: goal, scope, constraints, success criteria,
decisions, delegated/assumed choices, deferred or unresolved issues, and why the
interview ended. Say what remains unknown without claiming planning integrity
or universal completeness. Mark inferred defaults clearly. Do not ask an extra
save-to-file question by default; provide a file only if separately requested.

## Tool discipline

Use each mutation's returned revision for the next write. Read current state
after a stale revision or uncertain response; reconcile the answer evidence
before retrying. Never directly edit the database or claim persistence while
the MCP is unavailable. Surface the actual problem, preserve known progress,
and provide a conversation summary if useful.

For exact transitions and recovery details, locate the plugin root by walking
up from this SKILL.md to a matching `restate` plugin manifest, then read
`references/clarify-contract.md` under that root. This works in source and
packaged layouts without depending on a private checkout path. The server
checks records and transitions; it cannot authenticate evidence or decide
whether an answer, additional question, or planning document is good enough.

## Feedback

If this plugin behaves unexpectedly, open an issue at `97Wobbler/my-ai-kit`
with the plugin name, runtime, expected behavior, and observed behavior.

## Runtime Overrides

Users may invoke `restate:clarify` or ask to use this skill by name. In Default mode, use a clearly separated plain-text question block and wait for the user's answer. This is Clarify's default, not a claim that every Codex host lacks structured input. In Plan Mode, use request_user_input only when available and permitted; otherwise use plain text. Never change modes merely to ask a question. Use request_user_input_async only if the user explicitly requests that interaction or a tool test; an accepted response does not prove that a question UI appeared. If the user reports missing UI, switch to plain text. Follow host restrictions on questions and choices. Never treat timeout, a preselected option, or unrelated steering as an answer.
