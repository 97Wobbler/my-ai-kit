# Decision Consolidation

Use this reference when reviewing decisions that were later reversed,
superseded, or corrected.

## Goal

Reduce decision-log noise without erasing useful learning. A reversal can be
valuable history; a simple mistaken path can often be consolidated into one
compact record.

## Preserve Both

Preserve both decision records when:

- the first decision explains constraints that may return;
- the reversal marks a policy change, not merely a correction;
- external users, releases, migrations, or data were affected;
- future agents need to understand why a path is forbidden;
- the records document a real experiment with reusable evidence.

## Consolidate

Propose consolidation when:

- a decision and its reversal leave no current code, docs, workflow, or release
  effect;
- the first decision was a local misread or implementation mistake;
- no durable policy changed;
- the pair can be summarized without losing future warning value.

Recommended consolidated shape:

```markdown
| Date | Decision | Rationale | Evidence |
|---|---|---|---|
| YYYY-MM-DD | Tried X, then reverted it; X is not active. | Short reason and what to do next time. | Links or notes |
```

## Archive

Propose archiving when the detail is useful evidence but too long for the live
decision log. Keep a short live entry that points at the archive.

## Never Do Automatically

Do not delete decision records solely because they conflict. Conflicts may be
the point. Present confidence and ask for approval before rewriting durable
history.
