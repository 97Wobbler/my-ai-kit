---
name: ship-of-theseus
display_name: Ship of Theseus
class: heuristic
underlying_class: native
domain: philosophy
source: Thomas Hobbes, De Corpore (1655); Plutarch, Life of Theseus (1st century CE)
best_for:
  - identity persistence across incremental change
  - continuity vs. replacement reasoning
  - organizational or system refactoring decisions
one_liner: "Preserve identity through gradual change, but question whether replaced parts carry the original's essence."
---

# Ship of Theseus

## The Rule

When a system is rebuilt by replacing components incrementally, identity persists through continuity of function and history — not through material sameness — unless the replacement parts themselves constitute a meaningful loss of essence.

## When It Applies

- Refactoring a codebase where modules are rewritten one at a time but the system's purpose, API, and deployment lineage remain unbroken.
- Organizational change where roles, teams, or processes are gradually restructured but the institution's charter and legal entity persist.
- Long-lived infrastructure where hardware is rotated, dependencies updated, and architecture evolved, but operation is continuous.
- Deciding whether a migrated database, re-architected service, or rewritten component is "the same system" or a new one.
- Evaluating whether a company that has spun off divisions, changed leadership, or pivoted its product is still the same entity.

## When It Misleads

- When the "replacement parts" are qualitatively different in ways that change the system's essential behavior or values. Continuity of the label does not preserve identity if the function is fundamentally altered.
- When incremental replacement is used to hide a breaking change. A system that used to guarantee correctness and now guarantees speed-at-scale is not the same system because continuity was nominal.
- In contexts where *provenance* and *origination* matter more than function: a manuscript's authenticity is not restored by replacing worn pages with facsimiles, even if the text remains identical.
- When the "continuity" is maintained only through intentional historical amnesia — the system's prior commitments or constraints are dropped without acknowledgment.

## Common Misuse

Citing the heuristic to justify any change as "not really a breaking change because the system still exists." The heuristic does not absolve an agent of explaining *what changed* and *why the change is compatible with prior claims*. It is also misused as a rhetorical bludgeon to shut down questions about whether a slowly modified system has drifted from its original purpose.

## How Agents Use It

- **Embedded**: in refactoring, migration, or deprecation lenses, as a mandatory step for declaring "backward compatibility." The agent must identify the essential function or contract being preserved and the parts that are being replaced.
- **Sanity-gate**: on each "this is the same system" claim, force explicit statements of: (1) what material or structural changes have occurred, (2) what continuity of function or governance persists, and (3) what stakeholders depended on aspects that may have been lost. If the answer reveals a qualitative shift in essence, escalate the change from "refactoring" to "replacement."
