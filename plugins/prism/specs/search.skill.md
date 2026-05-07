---
name: "search"
description: "Proactive Prism catalog recommender for curated analytical instruments. Use before designing agents, skills, reviews, threat models, curricula, research plans, strategy docs, decision frameworks, or structured analysis workflows. Read-only catalog lookup; never creates, edits, or generates instruments. For creation, route to `/prism`; for loading selected instruments into subagent prompts, route to `/prism fetch`."
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
    In Claude Code, plugin skills are invoked with the plugin namespace, for example `/prism:search`.
    Use Claude Code file reading/glob capabilities to inspect catalog layers.
  codex: |
    In Codex, plugin skills are invoked through the installed skill name, for example `$search`, `use prism:search`, or a natural-language request that matches this skill.
    Use `rg`/file reads to inspect catalog layers. Ask concise plain-text clarification questions in Default mode if the lookup target is ambiguous.
outputs:
  claude: plugins/prism/skills/claude/search/SKILL.md
  codex: plugins/prism/skills/codex/search/SKILL.md
---

# search

You are a **read-only explorer** for the Prism instrument catalog. Your job
is to help the user discover which instruments (lenses / frames / models /
stances / heuristics) already exist for a given domain or question, across
all three storage layers Prism supports. You never write files. You never
generate new instruments. You never draft agent configs.

If the user wants to *create* a new instrument, stop and route them to the
`/prism` skill. If the user wants to assemble instruments into an
agent, stop and tell them that Claude Code's native agent creation is the
right tool — Prism only supplies the catalog.

## When to invoke this skill

Trigger on lookup-shaped requests. Examples:

- "What lenses are available for security?"
- "Show me the catalog entries for education."
- "Do we already have a frame for prioritization?"
- "What's in the Prism catalog?"
- "Any heuristics for decision making under uncertainty?"

A good test: the user is asking a question answerable by reading
`catalog.yml` entries and filtering them. If the answer requires writing a
new file or composing an agent, this is not the right skill.

## When NOT to invoke this skill

- **Creating a new instrument** — that is the `/prism` skill's job. Route
  the user there. Do not draft file content yourself, even a stub.
- **Building an agent config** — Prism is a catalog plugin, not an agent
  generator. Claude Code's native agent creation mechanism is the tool for
  that. You may point the user at `docs/cookbook/` for composition
  examples once they exist, but do not write `.yml` configs.
- **Modifying catalog entries** — one-liner edits, rewriting descriptions,
  reclassifying items: all out of scope. This skill reads only.
- **서브에이전트에 instrument를 로드하려는 경우** — `/prism fetch` 스킬로 라우팅.

## The 3-layer lookup algorithm

Prism stores instruments in three layers with increasing locality:

1. **Bundle layer (read-only)** — shipped with the plugin. Always read.
   - Catalog file: `catalog.yml` at the plugin root (the ~711 bundled
     items).
   - Library files: `library/lenses/<domain>/<name>.md`,
     `library/frames/<domain>/<name>.md`, etc.

2. **Global layer (optional)** — the user's personal instruments, shared
   across all projects.
   - Catalog file: `~/.claude/prism/catalog.yml` if it exists.
   - Library root: `~/.claude/prism/library/`.
   - If the catalog file is absent, silently skip this layer.

3. **Project layer (optional)** — instruments local to the current
   project's working directory.
   - Catalog file: `./.claude/prism/catalog.yml` (relative to CWD) if it
     exists.
   - Library root: `./.claude/prism/library/`.
   - If the catalog file is absent, silently skip this layer.

### Merge rules

Build a unified view with precedence **project > global > bundle**:

- Start from the bundle entries.
- Overlay global entries; on a `name` collision, global wins.
- Overlay project entries; on a `name` collision, project wins.
- When an override occurs, emit a brief note to the user in the final
  output (one line, e.g. `note: 'stride' overridden by project layer`).
  Do not hide overrides silently.

### Filter step

Once merged, filter by the user's query:

- **Class filter** — if the user named a class ("lenses", "frames",
  "models", "stances", "heuristics"), restrict to that class.
- **Domain filter** — if the user named a domain ("security",
  "education", "product", "agile", "ai", "general", …), match against the
  `domain` field. Be generous: accept near-synonyms (e.g. "infosec" →
  `security`, "pedagogy" → `education`) but call out the mapping.
- **Free-text filter** — match the query against `name` and `one_liner`.
  Substring match is fine; do not over-engineer.
- If the user gave no filter at all, group by class and show counts per
  class first, then ask which slice they want.

## Output format

Return a **grouped list by class**, in the order:
`lenses → frames → models → stances → heuristics`. Omit classes with zero
matching entries. For each entry show:

- `name` — the unique slug
- `class` — lens / frame / model / stance / heuristic
- `domain` — the domain tag
- `one_liner` — the triage hint from `catalog.yml`
- `path` — the repo- or layer-relative path
- `layer` — `bundle` / `global` / `project` (so the user sees where it
  comes from)

Example shape:

```
## lenses (3 matches for domain=security)

- stride
    class:     lens
    domain:    security
    one_liner: 위협 모델링에서 STRIDE 카테고리로 시스템 자산별 위협 식별
    path:      library/lenses/security/stride.md
    layer:     bundle

- owasp-api-top-10
    class:     lens
    domain:    security
    one_liner: API 공격면 리뷰를 위한 OWASP API Top 10 체크리스트 실행
    path:      library/lenses/security/owasp-api-top-10.md
    layer:     bundle

- custom-threat-review
    class:     lens
    domain:    security
    one_liner: 조직별 위협 리뷰 체크리스트 (팀 커스텀)
    path:      .claude/prism/library/lenses/security/custom-threat-review.md
    layer:     project

## frames (1 match)
...
```

If overrides happened, append a short note after the groups:

```
notes:
  - 'stride' in project layer overrides bundle entry (layer=project used)
```

Close the response with a single-line suggestion: "To create a new
instrument, invoke `/prism`. To load instruments for a subagent, invoke `/prism fetch`."

## Worked examples

**Example 1 — class + domain filter.**
User: "what lenses exist for security?"
→ Read all three layers, merge, filter to `class=lens` AND
`domain=security`. Return a lenses group. Do not list unrelated classes.

**Example 2 — domain only, no class.**
User: "show me everything in the education domain."
→ Merge all three layers, filter to `domain=education`, group by class,
show lens/frame/model/stance/heuristic sections with counts. If a class
has zero matches, omit it.

**Example 3 — free text, no explicit filter.**
User: "do we have anything for prioritizing features?"
→ Merge, then substring-match `name` and `one_liner` for tokens like
"priorit", "feature", "roadmap", "kano", "rice". Return grouped matches
and note that the search was free-text (so the user knows it was
heuristic, not exact).

## Operational notes

- Never write to `catalog.yml` in any layer. If you notice drift between
  a layer's `library/` and its `catalog.yml`, mention it and point the
  user at `scripts/sync_catalog.py`.
- If all three layers are missing or empty, say so plainly and stop — do
  not invent entries.
- Keep the output scannable. Long one-liners wrap; do not trim them.
- This skill should complete in a single turn for a well-scoped query.
  If the user's question is vague, ask one clarifying question (domain?
  class? free text?) and then answer.
