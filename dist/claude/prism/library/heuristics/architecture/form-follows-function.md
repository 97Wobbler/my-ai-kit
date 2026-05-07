---
name: form-follows-function
display_name: Form Follows Function
class: heuristic
underlying_class: native
domain: architecture
source: Louis Sullivan, 1896
best_for:
  - design reviews
  - refactoring decisions
  - interface simplification
  - feature removal justification
one_liner: "Function is the origin of form — form does not precede function."
---

# Form Follows Function

## The Rule
The shape of a thing should be determined by what it does, not by tradition, aesthetic preference, or constraint imposed from outside its purpose.

## When It Applies
- Reviewing a UI component where visual hierarchy obscures or contradicts the actual user workflow.
- Deciding whether to keep or cut an API parameter, database column, or configuration option that has no active consumer.
- Evaluating an architectural layer, module, or service whose organizational boundary does not correspond to the work it actually performs.
- Simplifying a design by removing decorative, historical, or ceremonial elements that do not serve the core function.

## When It Misleads
- When the "function" is unclear or contested. If stakeholders disagree on what the thing is *for*, Sullivan's rule dissolves into aesthetic argument disguised as principle.
- In domains where the form carries semantic or cultural weight (branding, ritual, accessibility). A wheelchair ramp's form is constrained not just by the function of wheeling, but by dignity and integration into the social space.
- When applied retroactively to punish existing form as "ornamental" without understanding the constraints (regulatory, historical, or technical) that shaped it. Form often encodes knowledge.
- In exploratory or generative design, where the form sometimes *discovers* what the function should be, not the reverse.

## Common Misuse
Treating "function" as self-evident when it is actually contested or vague. Designers often cite Sullivan to demolish a proposal they dislike aesthetically, then rationalize it as "doesn't serve the function"—without naming what the function actually is or proving the form fails it. The heuristic is disciplined only when the function is stated first and the form is evaluated against it afterward.

Another failure: confusing "minimal" with "functional." A form that is sparse may feel honest, but sparseness itself is not a function. If the function requires redundancy, feedback, or visual distinction, a sparse form fails it.

## How Agents Use It
- **Embedded**: in design-review or refactoring lenses, as a mandatory step before recommending any form change. The agent first articulates the function explicitly, then evaluates whether the current form serves it, then proposes a revised form tied back to that function.
- **Sanity-gate**: on each form-level recommendation (remove a field, redesign a layout, flatten a hierarchy), force the agent to state the function that form serves, then show why the proposed form serves the same function better or why the function is no longer active.
