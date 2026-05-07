---
name: poka-yoke
display_name: Poka-yoke
class: heuristic
underlying_class: native
domain: operations
source: Shigeo Shingo, 1960s
best_for:
  - process design and error prevention
  - quality assurance in manufacturing and operations
  - system hardening against human error
one_liner: "Make mistakes structurally impossible."
---

# Poka-yoke

## The Rule
Design the process so the mistake cannot be made, or make the mistake immediately obvious when it occurs, rather than relying on human attention or training to prevent it.

## When It Applies
- Manufacturing assembly lines where a part can be installed backward or upside down, introducing a physical constraint that allows only the correct orientation.
- Medical procedures where a checklist or physical stop prevents starting a step before prerequisites are complete.
- Software systems where a type system or schema validation prevents invalid data from entering the pipeline.
- API designs where the function signature makes it impossible to pass arguments in the wrong order (e.g., wrapping a value in a distinct type instead of using a raw boolean or string).
- Warehouse picking where bin locations are color-coded so the picker visually matches color before taking an item.

## When It Misleads
- When the "poka-yoke" adds so much friction that people route around it, defeating the purpose. A lock that requires three keys and a supervisor's sign-off may prevent mistakes but also prevents legitimate fast paths.
- In exploration or research-heavy work where you don't yet know what the "correct" path is. Poka-yoke locks in an assumption that may itself be wrong.
- When the cost of the mistake is low and the cost of the prevention mechanism is high. A perfect poka-yoke against a typo in a log message is wasteful engineering.
- When applied to human judgment rather than mechanical steps. You cannot poka-yoke a decision; you can only poka-yoke a routine.

## Common Misuse
Confusing poka-yoke with nagging or friction. A warning dialog, a validation error, or a required approval are not poka-yoke — they are guards that rely on the user to notice and act. True poka-yoke makes the mistake impossible (or makes it immediately unmistakable) without requiring human intervention.

Another common failure is building poka-yoke for the wrong mistake. Spending engineering effort to prevent a mistake that almost never happens, while ignoring a frequent and costly mistake, reverses the priority.

## How Agents Use It
- **Embedded**: in process design or system-hardening lenses, as a check step after identifying high-frequency, high-cost mistakes. For each candidate mistake, ask whether a mechanical constraint, schema rule, or type system can make it impossible rather than relying on training or checklists.
- **Sanity-gate**: on each proposed safeguard or quality control measure, ask whether it truly prevents the mistake or merely alerts to it. If it requires human reaction, it is not poka-yoke and may be easily defeated under time pressure.
