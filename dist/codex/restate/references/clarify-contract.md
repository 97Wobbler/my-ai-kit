# Clarify interview contract

This reference describes the local interview tools. The skill owns meaning,
question quality, and the distinction between user decisions and implementation
judgment. The server checks record shape, progress, and transitions. Evidence
is supplied by the agent; the server cannot authenticate a reported user answer.

## State and evidence

A session stores the original request, current context, explicit workspace label
(empty for projectless work), decision items, fixed round records, revision,
latest reviewed content revision, and a compact change history. Session IDs and
item IDs are caller-chosen stable identifiers, not paths. Keep them out of normal
conversation. Read a known session directly; list by workspace when recovering.
Do not resume a different session merely because it was used most recently.

Each item has `id`, `title` (one decision boundary), `impact`, `why_user`,
`priority` (`alpha`, `beta`, `gamma`), and `owner` (`user` by default, or `agent`
for an explicitly identified implementation choice). Priority is ordering only.
The current disposition starts `open`. `partial` records evidence without
settling it. Other dispositions are `user_decided`, `user_delegated`,
`agent_owned`, `deferred`, and `inapplicable`. A disposition requires a reason;
decisions/delegation/deferral require evidence with `source: user`. Agent-owned
resolution is allowed only for an item initially classified `owner: agent`.
An inapplicable item needs evidence and a reason explaining why it no longer
requires a decision. Recommendations are never user evidence.

Evidence objects contain `source` (`user`, `context`, or `agent`) and `text`.
Use the actual relevant answer or a faithful excerpt, not invented approval.
Answer evidence remains on the item, and history preserves replaced decisions.

## Tools

Every successful mutation returns the current snapshot and derived progress.
All existing-session writes require `expected_revision` from the last read.
The create caller supplies `session_id`, so a lost response can be reconciled
by reading that ID instead of creating a duplicate. Reusing an ID is an error.

| Tool | Purpose |
|---|---|
| `clarify_session_create` | Create with `session_id`, `title`, `original_request`, `context`, `workspace`, and optional initial `items`. |
| `clarify_session_list` | List bounded session metadata, optionally filtered by explicit `workspace`. Does not create storage. |
| `clarify_session_read` | Read `session_id`; optionally include audit `history`. Does not mutate or close a session. |
| `clarify_items_update` | Apply a nonempty batch of typed `add`, `record`, `reopen`, or `context` operations atomically. All operations carry a reason and evidence; record also carries `disposition` and `decision`. |
| `clarify_round_start` | Freeze every open item. Optional `ordered_item_ids` gives the recomposed order and must contain every open ID exactly once; omitted order uses alpha/beta/gamma. After the first round, requires review of the latest content. |
| `clarify_round_review` | Record review `summary`, optionally add `new_items`. Normally all round items must be processed. A prerequisite-driven interruption additionally names `prerequisite_ids` and `interruption_reason`. |
| `clarify_session_close` | `outcome: completed` requires no open items and review of the latest content. `outcome: stopped` requires user evidence and retains open work. Both require a reason. |

See live tool schemas for exact fields. No operation accepts a free-form state
patch. All identifiers within a batch must refer to existing or newly added
items in that same batch. Invalid batches and stale writes leave state intact.

## Rounds and stopping

A round's membership never expands. New items, or reopened items already
processed in the current round, are next-round candidates. Record processing
separately from current item disposition: correcting a decision must not rewrite
past round progress. A complete correction is another `record`; use `reopen`
only for an unresolved choice/conflict, with its changed premise as the reason.

Queued items are provisional, not a scheduled next round. Review checks prior
context, accumulated answer conflicts, every candidate, and gaps in the whole
current scope. Resolve candidates supported by actual user answers, retire
obsolete/duplicate candidates with evidence-backed `inapplicable` records, and
preserve the retained ID and every distinct unresolved choice when consolidating.
Keep all history. Add newly discovered material gaps, then reconsider the whole
remaining order by prerequisites and importance. Record the reconciliation and
ordering rationale in the review summary, and pass the complete ordered ID list
to round start. No new item is required merely to demonstrate review.

Give each new item an impact and ownership rationale. If a new open
prerequisite prevents remaining answers, review can mark the round `interrupted`
and carry those remaining items unresolved. The prerequisite must be a queued
candidate, not merely an unanswered existing question. Show carried and handled
counts separately; do not call this successful completion or user deferral.

After any content change, natural close and starting a subsequent round require
a fresh review. Starting a
round, reading, listing, and presenting a draft do not change content. Empty
initial inventories can be reviewed and closed without manufacturing questions.
Explicitly deferred work stays visible. User-requested stopping bypasses round
completion but never marks unresolved items answered. A closed session is an
immutable record; further work starts a new session with relevant context.

## Visible questions and transitions

For plain-text interviews, separate an optional one-sentence acknowledgment
from the next question. Scale the block to the decision; do not invent choices
for a free-form answer. A synthetic example:

이전 결정: 수신자는 최초 수락한 계정으로 고정했습니다.

**다음 질문 · 편지를 언제까지 완성해야 하나요?**

받는 사람이 빈 캡슐을 만날 수 있는지에 따라 작성·전달 경험이 달라집니다.

- **A. 100개 완성 후 전달 — 추천**
- **B. 일부 작성 후 전달하고 나머지 추가**

A는 완성된 선물을 건넨다는 목적에 맞습니다. 다른 방식도 말씀해 주세요.

At a round boundary, announce completion of answers and start of review before
doing the review. For example: “이번 라운드 답변을 모두 받았습니다. 전체 기획과
추가 검토 후보를 함께 재검토하겠습니다.” After actual reconciliation, show the
result: “후보 B는 앞선 답변으로 해소됐고 A는 남았습니다. 새로 발견한 C를 먼저
정해야 A를 결정할 수 있어, 다음 라운드는 C와 A 순서로 진행하겠습니다.” Then
start the recorded round and show its first question separately. Do not ask
permission merely to continue the requested interview.

When a round has zero remaining items but `review_current` is false, report
answers complete and review pending, never interview complete. After review,
either present the recomposed group or close. Only a successful close returning
`status: completed` supports a natural completion announcement. Document
formatting checks are not contextual review.

Codex Default mode uses plain text by default in this skill. Tool availability
or an async `accepted` result does not establish visible selection UI. This is
a workflow default, not a statement about every Codex host. Honor an explicit
request to test async input, and fall back to plain text if UI is missing.

## Worked conversations (synthetic; design examples)

1. Normal flow: “팀 회의 기록을 검색하고 싶어.” Initial items: audience and
   search scope. Ask: “누가 검색할 수 있어야 하나요? 접근 범위에 따라 공유와
   권한 기준이 달라져요. A. 나만 / B. 우리 팀(추천: 팀 회의 기록이라는 목적에
   맞음) / C. 외부 사용자도 포함.”
   “우리 팀만 쓰고 제목과 본문 모두 검색해.” One answer settles both items.
   Display “이번 라운드 2개 항목 처리, 추가 후보 없음”; review scope/conflicts,
   then close. Do not ask which search index to implement.
2. Partial answer and correction: “검색 대상은 회의록만.” Audience stays open;
   ask only that unresolved decision: “접근 대상은 어느 쪽인가요? A. 나만 /
   B. 우리 팀(추천: 내부 공유 목적에 맞음) / C. 외부도 포함.” Do not add optional
   search-ranking preferences to the original audience decision.
   “팀 전체. 아까 말한 회의록 외에 결정 기록도 포함해.” Record both audience
   and the complete scope correction. No automatic repeat interview for scope.
   Review the latest decisions; an older empty review cannot authorize close.
3. Changed prerequisite: while interviewing permissions and billing, the user
   says “개인용과 조직용 중 아직 고민이야.” Add the audience decision with its
   material effect and why the user must choose. If remaining questions depend
   on that decision, record an interrupted round and carry them unresolved.
   Explain “대상 선택이 먼저 필요해 남은 2개 항목을 다음 라운드로 넘겼습니다.”
   Review, then start the next round: “첫 버전의 대상은 무엇으로 할까요?
   A. 개인용 / B. 조직용(추천: 현재 권한·결제 요구를 함께 다루기 쉬움).” Never label
   carried items resolved or change the prior denominator silently.

## Storage, transport, and recovery

Python 3.10+ with its standard library is sufficient. Both runtimes use
`RESTATE_CLARIFY_DATA_DIR` or `~/.restate/clarify`. Overrides must expand to an
absolute path and contain no unresolved environment placeholders. The SQLite
database is created only by session creation. Import, MCP initialization,
discovery, and absent-store queries do not create directories or a database.
No state lives in source, dist, or the installed plugin cache by default.

The stdio server negotiates one of its advertised supported protocol revisions,
keeps stdout for JSON-RPC, ignores notifications without a response, and returns
domain failures (such as `stale_revision`, `invalid_transition`, `review_required`)
as tool results with `isError: true`, a code, and recovery information. Invalid
protocol envelopes/unknown methods or tools use JSON-RPC errors. Read after a
lost mutation response; compare evidence/revision before deciding to retry.

MCP validates mechanical consistency only. Dialogue examples and tests do not
guarantee that every model judges ambiguity well. Final interaction quality
needs real user interviews in each runtime.
