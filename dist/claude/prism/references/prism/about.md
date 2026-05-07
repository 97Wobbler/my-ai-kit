<!-- Rendering rule: Do not narrate routing or file-loading decisions to the user — render the content below directly, without meta commentary about which intent was classified or which file was opened. -->

# Prism

Prism is a Claude Code plugin that provides a **catalog of analytical
instruments** for designing agents and skills. The plugin itself does
not create agents or skills — it supplies structured instrument files
that Claude Code's native `/agents` flow can reference.

Every Prism instrument belongs to one of five classes:

- **Lens** — executable analytical procedure
- **Frame** — classification / taxonomy
- **Model** — theoretical or predictive model
- **Stance** — interpretive commitment
- **Heuristic** — single rule of thumb

For exact definitions, discriminating criteria, and file formats for
each class, just ask — the root `CLASSES.md` has the full reference.

## Quick start

- **Create a new instrument** → `/prism CVSS` or `/prism Kanban`
- **Browse the catalog** → `/prism search`
- **Load instruments for a subagent** → `/prism fetch`
- **Multi-agent debate / review / ideation** → `/prism debate`
- **Full usage reference** → `/prism help`
