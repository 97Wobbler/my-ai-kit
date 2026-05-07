---
name: "fetch"
description: Prepare Prism instruments for delivery to subagents, agents, or skills. Resolves instrument names to absolute paths and returns an instruction block (path table + read directives + brief summary) ready to paste into a subagent prompt. Intended as the second step after `/prism search`. Triggers on "/prism fetch stride owasp-top10", "load instruments", "fetch instruments for my subagent", "instrument load", "attach lenses to subagent"
targets:
  - claude
  - codex
capabilities:
  user_questions: optional
  file_edits: false
  subagents: none
  plan_mode: none
  network: false
  validation: optional
runtime_overrides:
  claude: |
    In Claude Code, plugin skills are invoked with the plugin namespace, for example `/prism:fetch`.
    Use Claude Code file reading/glob capabilities to resolve catalog paths and verify instrument files.
  codex: |
    In Codex, plugin skills are invoked through the installed skill name, for example `$fetch`, `use prism:fetch`, or a natural-language request that matches this skill.
    Use `rg`/file reads to inspect catalogs and instrument files. Ask concise plain-text clarification questions in Default mode if an instrument name is ambiguous.
outputs:
  claude: plugins/prism/skills/claude/fetch/SKILL.md
  codex: plugins/prism/skills/codex/fetch/SKILL.md
---

# fetch

Prepare selected Prism instruments as an instruction block that a
subagent can consume directly.

## Role

If `/prism search` is "discover what exists," `fetch` is **"get the
selected ones ready."**

- Prepares **paths and read directives** so the subagent can actually
  open and follow the instrument procedures.
- Does not inline instrument content — returns **absolute paths + read
  instructions + brief summary** only.
- Typical workflow: `/prism search` to find candidates → `fetch` to
  equip selected instruments.

## Input

Accepts one or more of the following:

- **Instrument name (slug), one or more** — `stride`, `owasp-top10`,
  `systems-thinking`, etc. Must match a `name` value in `catalog.yml`.
- **Domain + class combination** — "all security lenses", "all education
  frames" — fetches every matching instrument.
- If a name is ambiguous, show candidates from `catalog.yml` and ask
  **one clarifying question**. Do not guess.

## Resolve algorithm

### 3-layer path lookup

Prism stores instruments in three layers. Merge with precedence
**project > global > bundle**:

1. **Bundle layer (read-only)** — instruments shipped with the plugin.
   - Catalog: `<plugin-root>/catalog.yml`
   - Library: `<plugin-root>/library/`

2. **Global layer (optional)** — user-wide instruments.
   - Catalog: `~/.claude/prism/catalog.yml`
   - Library: `~/.claude/prism/library/`
   - Silently skip if absent.

3. **Project layer (optional)** — project-scoped instruments.
   - Catalog: `./.claude/prism/catalog.yml` (relative to CWD)
   - Library: `./.claude/prism/library/`
   - Silently skip if absent.

### Merge and path resolution

- Read `catalog.yml` from all three layers and extract the `path` field
  for each requested instrument.
- On `name` collision, higher-precedence layer wins. Note overrides in
  output.
- Convert each `path` to an **absolute path** relative to its layer root.
- **Verify existence** (Glob or Read). If missing, emit a warning and
  skip that entry.
- Extract `one_liner` and `class` from frontmatter as the brief summary.

## Output format

Return a **copy-pasteable text block** for subagent prompts:

```
## Prism Instruments — Subagent Directive

Read the following instrument files with the Read tool and follow
each file's core procedure section in your analysis workflow.

| # | name | class | summary | path |
|---|------|-------|---------|------|
| 1 | stride | lens | Identify threats per STRIDE category | /full/path/to/stride.md |
| 2 | owasp-top10 | lens | Run OWASP Top 10 checklist | /full/path/to/owasp-top10.md |

### Core section guide by class
- **lens**: Follow the "Analytical Procedure" steps in order
- **frame**: Apply "Categories" + "Classification Procedure"
- **model**: Apply "Core Variables" + "Application Procedure"
- **stance**: Set analysis perspective via "Guiding Questions"
- **heuristic**: Use "The Rule" + "When It Applies" as checkpoints
```

If overrides occurred, append a note below the table:

```
notes:
  - 'stride' in project layer overrides bundle entry (layer=project used)
```

## Operational rules

- **READ-ONLY**: never create or modify files. Read catalog and library
  only.
- **Re-read `catalog.yml` every invocation** — do not cache.
- If more than **10 instruments** are requested, emit a warning first and
  proceed only after user confirmation.
- Delivery is **path-based**: subagents read files themselves via the
  Read tool. Do not inline instrument bodies.

## NOT this skill

- **Catalog browsing/search** — use `/prism search`.
- **Instrument creation** — use `/prism <framework>`.
- **Agent/skill creation** — use Claude Code's native `/agents` flow.
  Prism supplies the catalog, not agent configs.
