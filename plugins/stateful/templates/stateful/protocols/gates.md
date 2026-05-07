# Gate Policy

| Gate | Meaning | Default behavior |
|---|---|---|
| `human_gate: null` | Agent can execute | Runnable by default |
| `human_gate: approve` | Human approval required after agent prepares output | Stop and ask |
| `human_gate: execute` | Human must perform the task | Prepare materials only |
| `human_gate: debate` | Multi-perspective agent debate can propose a decision | Run only when requested or locally allowed |
| `human_gate: review` | Human owner must explicitly sign off | Never auto-complete |
| `execution_gate: batch` | Long or expensive execution | Never auto-run by default |

`protected_human_only: true` prevents conversion of a human measurement or
gold-standard task into an LLM-only decision.
