# <domain-name> Learning Project

This directory is a learning project managed by the `studycoach` plugin.

The active domain is **<domain-name>** (`<domain-id>`). All mutable learning state lives in `.rumsfeld/`.

## Quick Start

When starting here, invoke:

```text
<skill-invocation>
```

The skill detects `.rumsfeld/` and enters **resume mode** first. It reads progress, roadmap, and matrix state, briefs the learner, and only starts **session mode** after the learner explicitly chooses a study topic.

## Layout

```text
.rumsfeld/
├── matrix.yaml
├── roadmap.yaml
├── progress.yaml
└── notes/
    ├── YYYY-MM-DD-<topic>.md
    └── concept-<slug>.md
```

## Key Principles

- Roadmap is mostly static; `progress.yaml` is mutable state.
- Matrix items are never deleted, only transitioned with evidence.
- Sessions are conversational and start from "왜 이게 존재하는가".
- Study sessions write session notes; status-only resume actions do not.
- Build projects connect learning to implementation when relevant.
