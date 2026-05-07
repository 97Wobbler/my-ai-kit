---
name: c4-model
display_name: C4 Model
class: lens
underlying_class: native
domain: agile
source: Simon Brown (C4 Model, 2011–present)
best_for:
  - Communicating system architecture to stakeholders at multiple abstraction levels
  - Identifying scope creep and boundary misalignment in microservice designs
  - Forcing discipline into vague "architecture diagrams"
one_liner: "Describe system architecture precisely across four zoom levels — Context, Container, Component, Code."
---

# C4 Model

## Overview

The C4 Model is a strict, level-based framework for drawing system architecture diagrams. It enforces a hierarchy: Context (system in its environment), Container (deployable units), Component (major building blocks within a container), and Code (classes, functions, data structures). Practitioners use it because vague architecture diagrams obscure decisions — by forcing a choice of level and rules at each level, the C4 framework exposes what you actually do and don't understand about the system's boundaries and dependencies.

## Analytical Procedure

### Phase 1 — Define Scope and Artifacts

1. **Choose the system boundary.** What is being architected? A single application, a suite of services, a platform? Write a one-sentence definition. Do not include "and other systems" — be explicit.

2. **Enumerate the artifacts you will diagram:** the application or service itself, all external systems it touches, all users or user roles that interact with it, and all data stores. List each once. If you list something twice with two different names, merge them.

3. **Check for hidden scope.** Ask: Are there services we call that we don't control? Are there mobile apps, browsers, and APIs treated as one thing or separately? Are there human processes that touch the system? Rewrite the artifact list to be exhaustive.

### Phase 2 — Draw Context Diagram (C1)

4. **Draw a single box labeled with the system name.** Inside: no detail. Just the name.

5. **Around it, draw boxes for each external system and user role.** External means outside your system boundary (from step 1). If your system calls a payment processor, the processor is external. If your system has a web UI and a mobile app, each is a separate external system (or a single "Client" container if they share code).

6. **Draw arrows for interactions.** Label each arrow with the communication protocol and what data/request flows. If you can't write a one-phrase label on the arrow, the diagram is too coarse — you're hiding assumptions about what that interaction does.

   Example labels:
   - "HTTP request, JSON" ✓ (clear)
   - "talks to" ✗ (vague)
   - "reads user data" ✓ (clear)
   - "integration" ✗ (hides what's happening)

7. **Mark the diagram complete only if:** Every arrow is labeled. Every external actor is drawn. Every data flow in the system description is represented. Do a walk-through: for each external system, trace the path it must take to reach yours and confirm it's drawn.

### Phase 3 — Draw Container Diagram (C2)

8. **For the system from C1, decompose it into containers.** A container is a deployable, runnable unit: a web server, a microservice, a mobile app, a database, a message queue. A JAR file deployed to a single place is one container. Two identical JARs deployed to two servers are one container (they're the same software).

9. **For each container, draw a box and write:** the container name, the technology (e.g., "Node.js API," "PostgreSQL," "React SPA"), and a one-line responsibility.

10. **Between containers, draw arrows labeled with the interaction.** If two containers talk synchronously via HTTP, label "HTTP, JSON." If they're decoupled by a message queue, label "async message, Kafka topic: orders." If it's a read from a database, label "SQL, read user table."

11. **Map each container to the C1 interactions.** For each arrow in C1, does at least one container-to-container interaction in C2 explain it? If not, add the missing container or interaction. If a C1 arrow maps to 5 C2 arrows, the decomposition may be leaking complexity — review whether those 5 are hiding a missing abstraction.

### Phase 4 — Draw Component Diagram (C3)

12. **For one container (pick the most complex or most relevant to the analysis), decompose it into components.** A component is a major structural unit: a module, a package, a bounded context (DDD term), or a functional layer. The rule: can a junior engineer be assigned to own one component without needing to understand the internals of the others?

13. **For each component, write:** the name, the responsibility, and the technology if technology is a defining characteristic (e.g., "ORM layer," "cache module," "payment processor SDK").

14. **Draw interactions between components and from components to external systems.** For each interaction, label the protocol and data shape, or reference the interface it uses (e.g., "calls PaymentAPI," "reads from database," "publishes to event bus").

15. **Check internal coherence.** Ask: Is every component used? Is there a component that calls all the others (a smell of poor separation)? Are there circular dependencies? If you answer "yes" to any of these, you've found a design problem before code is written.

### Phase 5 — Code Diagram (C4) — Optional

16. **If necessary, draw one code diagram for a single complex component.** Show classes, interfaces, or functions and their relationships. This level is rarely needed in architecture documentation; use it only if the component is highly algorithmic or the team is unfamiliar with the codebase.

### Phase 6 — Validation

17. **For each diagram, perform a "completeness walk":** Name every external system, container, or component visible in the diagram. For each, state its primary responsibility in one sentence. If you hesitate or give a compound sentence, the diagram is too coarse or that element is misplaced.

18. **Cross-check diagrams.** Every arrow in C1 must map to one or more arrows in C2. Every arrow in C2 must map to one or more arrows in C3 (if C3 is drawn). If an arrow disappears or multiplies without justification, the diagrams are inconsistent.

19. **Review all external dependencies.** List every third-party system, protocol, and technology mentioned across all diagrams. For each, verify the team has agreed it belongs and knows why. If an external dependency appears in C2 or C3 but never in C1, it's a hidden assumption — add it to C1.

## Evaluation Criteria

| Check | Pass |
|---|---|
| C1 diagram has exactly one box for the system and boxes for all external systems/users | Y/N |
| Every arrow in C1 is labeled with protocol and data type | Y/N |
| C2 diagram decomposes the system into containers; each container has a name, technology, and responsibility | Y/N |
| Every C1 interaction maps to one or more C2 container interactions | Y/N |
| C2 interactions are labeled with protocol, data format, or mechanism (HTTP/SQL/Kafka/etc.) | Y/N |
| C3 diagram (if drawn) shows components with responsibilities; interactions are labeled | Y/N |
| No circular dependencies visible in C3 | Y/N |
| All external systems are consistent across C1, C2, and C3 | Y/N |
| Team walked through each diagram and stated each element's responsibility in one sentence | Y/N |

## Red Flags

- C1 has more than 8 external boxes. If true, either the system has genuinely wide integration (rare) or you've drawn implementation details instead of external dependencies. Collapse or group.
- C2 has a "God Container" — one container that calls or is called by all others. This is usually a hidden layer or a decomposition failure.
- An arrow in C1 has no corresponding arrows in C2. The interaction is real but not modeled — likely a missing container.
- C3 components all call a shared "utility" or "common" component. This is often a code smell indicating the utility is actually a policy or domain layer that should be explicit.
- Two diagrams show the same interaction labeled differently (e.g., C1 says "JSON over HTTP," C2 says "gRPC"). Inconsistency indicates unclear design.
- External system appears in C2 or C3 but not in C1. Hidden assumption — it needs to be explicit in the context.

## Output Format

```
## C4 Architecture Assessment

**System Scope:**
<one-sentence definition of what is being architected>

### Artifacts Enumerated
- <system/application name>
- <external system 1>
- <external system 2>
- <data store 1>
- <user role 1>
(list all actors and systems)

### C1 — Context Diagram
| External Actor | Interaction | Protocol/Data |
|---|---|---|
| <actor> | <interaction description> | <protocol, e.g., HTTP/JSON> |

(Include ASCII diagram or reference)

### C2 — Container Diagram
| Container | Technology | Responsibility |
|---|---|---|
| <name> | <tech stack> | <one-line purpose> |

| From | To | Interaction | Protocol |
|---|---|---|---|
| <container> | <container/external> | <what flows> | <HTTP/SQL/async/etc.> |

(Include ASCII diagram or reference)

### C3 — Component Diagram (if drawn)
[Repeat table structure for the chosen container]

### Consistency Check
- C1 to C2 mapping: <all arrows accounted for or gaps noted>
- C2 to C3 mapping: <all arrows accounted for or gaps noted>
- Undeclared external systems: <if any>

### Design Issues Found
1. <issue, e.g., "God Container calling all others">
2. <issue>
(or "None identified" if clean)

### Confidence
<high/medium/low> — <justification>
```
