# Thin Project Connection

Inspect existing instructions, document routing and lifecycle first. A research
project may already have a whole-project docs harness; a service repository may
contain a small research effort. Respect both without mandatory folder layouts,
extra Markdown indexes, Waypoint installation or physical document boundaries.

The research file can reference goal/policy documents with version and summary.
Those are decision-time snapshots, not replacement sources of truth.

Within an authorized connection/install request, add a small routing point to
the project's existing instruction document. Preserve all unrelated content.
For an existing record, generate a proposed snippet without modifying files:

```sh
python3 <package-root>/scripts/research_store.py route /workspace/research.json --runtime codex
python3 <package-root>/scripts/research_store.py route /workspace/research.json --runtime claude
```

Apply only the relevant runtime's snippet, or adapt it to the existing docs
router. It should identify research work, the skill, record location and existing
goals, without pretending every repo change is research. A Codex project may
route through AGENTS.md; a Claude project through its existing instructions.
Installing the plugin alone does not automatically change every project.

Invocation formatting and instruction-file discovery are runtime-specific;
the neutral method and JSON semantics are the same. Do not store a private
checkout path or a versioned plugin cache path in the project instructions.
When connection edits are already part of the approved request, do not require
an extra approval for each reversible routing line. Material scope or policy
changes still need user direction.
