---
name: event-storming
display_name: Event Storming
class: lens
underlying_class: native
domain: agile
source: Alberto Brandolini, 2013
best_for:
  - Discovering hidden business logic and process flows
  - Aligning technical and non-technical stakeholders on domain events
  - Identifying gaps, redundancies, and ambiguities in system behavior
one_liner: "Collaborative workshop that maps an entire business process through domain events and surfaces understanding gaps."
---

# Event Storming

## Overview
Event Storming is a rapid, collaborative workshop technique that maps the timeline of domain events (things that happen in a business process) using sticky notes on a wall or surface. Participants—developers, business analysts, domain experts, and product managers—collectively construct a shared model by placing orange notes (events), yellow notes (commands that trigger events), blue notes (users or systems), and pink notes (problems or questions). The power lies in the *absence*: gaps in the timeline expose missing requirements; contradictions between experts surface assumptions; clustering reveals aggregate boundaries. Practitioners use it when a requirements document is vague, when a team spans multiple domains, or when the relationship between commands and events is unclear.

## Analytical Procedure

### Phase 1 — Workshop Preparation

1. **Define the scope (start and end events).** Pick a bounded business process: "order creation to delivery," "user signup to first purchase," "support ticket open to resolution." Write both events plainly. Scope is the frame—too narrow and you miss interdependencies; too wide and the session becomes untraceable.

2. **Invite 5–8 participants.** Include at least one domain expert who knows the business rule (not just the current system), at least one developer, and at least one person who touches the customer experience. Exclude people with a strong need to look right or defend a legacy system.

3. **Prepare the surface and materials.** Use a large wall, whiteboard, or long table. Provide:
   - Orange sticky notes (domain events: "OrderPlaced," "PaymentProcessed," "InventoryReserved")
   - Yellow sticky notes (commands: user or system actions that cause events)
   - Blue sticky notes (actors: users, systems, services)
   - Pink sticky notes (problems, questions, unknowns: "How long does refund take?")
   - A marker for each color

4. **Establish a timeline orientation.** Decide left-to-right or top-to-bottom. Announce that time flows in one direction only.

### Phase 2 — Chaotic Exploration

5. **Invite participants to place orange notes freely.** Ask: "What happens in this process? What events occur?" Do not demand chronological order yet. Events can be placed anywhere. The goal is to externalize knowledge, not structure. Participants may place the same event multiple times—this is valuable, not wasteful.

6. **Encourage rapid talking-out.** As each note goes on the wall, the person describes it: "When this order is placed, the system should record the timestamp." Others may object, ask for clarification, or add a pink note with a question. This is the whole value—conflicts and gaps become visible immediately.

7. **Allow 15–20 minutes of chaos.** Do not interrupt or correct. Capture all events, even tentative ones. If someone says "I think something happens here but I'm not sure," that goes on a pink note.

### Phase 3 — Chronological Ordering

8. **Designate a facilitator (often the domain expert or Scrum Master).** This person does not add notes; they clarify sequence.

9. **Start with the scope start-event.** Place it at the left. Ask: "What must happen immediately after this?" Look for consensus. If disagreement arises, ask: "Under what conditions does A happen before B?" Write the condition on the pink note. Order may be conditional, not universal.

10. **Move right (or down).** For each event, ask: "What happens next?" Continue until the scope end-event. Some orange notes will be reordered; others may be discarded (they were aspirational or the participant misunderstood the scope).

11. **Mark gaps.** As you build the timeline, if there's a jump ("Order placed, then shipped—but what about payment?"), place a pink note in the gap. Do not assume; ask aloud.

### Phase 4 — Add Commands and Actors

12. **For each orange note, add a yellow note to its left.** Ask: "What action caused this event?" If "OrderPlaced," the command is "PlaceOrder" (a user action) or "CreateOrderFromCart" (a system action). If no one can name the command, it's a problem — either the event is orphaned or the actor is missing.

13. **Add blue notes above or beside each yellow note.** Who or what performed this command? A user (Jane, an admin), an external system (Stripe), a timer (batch job). If no actor can be named, the requirement is incomplete.

14. **Trace data flow implicitly.** Do not draw arrows (that's a detail). Instead, ask: "When this event happens, what information does the next command need?" If it's unclear how data flows from event to command, place a pink note.

### Phase 5 — Identify Aggregates and Boundaries

15. **Look for clusters of tightly coupled events.** Events that always happen together, or that share the same entity (e.g., all events involving "Order"), form an aggregate candidate. Draw a light box around them. Label the box with the aggregate name (e.g., "Order Aggregate," "Payment Aggregate").

16. **Mark aggregate-to-aggregate communication.** If an event in one aggregate must trigger a command in another, a pink note marks that boundary. These are integration points, often sources of consistency bugs or performance problems.

17. **Identify read models.** Ask: "To show the customer their order status, what information is needed?" Trace backwards to the events that provide that data. Mark these as read model dependencies.

### Phase 6 — Surface Problems and Assumptions

18. **Scan all pink notes.** For each, ask: "Is this a missing requirement, a misconception, an ambiguity, or a known limitation?" Categorize it:
   - **Requirement gap** — "We don't know how refunds interact with cancellations"
   - **Assumption conflict** — "Dev thinks payment happens before inventory; business says after"
   - **Unclear ownership** — "Who is responsible for retry logic if the email service is down?"
   - **Technical/business impedance** — "The legacy system can't provide real-time inventory"

19. **Do not solve problems in the workshop.** Write them down. Assign an owner (usually the person who knows most). Move on.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Start and end events for scope are explicitly stated | Y/N |
| All orange notes form a timeline with no unexplained gaps | Y/N |
| Every orange note has a corresponding yellow note (command) | Y/N |
| Every yellow note has a corresponding blue note (actor) | Y/N |
| At least one aggregate boundary is identified | Y/N |
| At least two pink notes (problems/questions) are documented | Y/N |
| No pink note was left unanswered; all are owned or queued for follow-up | Y/N |

## Red Flags

- Orange notes outnumber yellow and blue notes by 3:1 or more. Commands and actors are underspecified; the model is incomplete.
- All events are placed in a single line with no branching or conditionals. Either the process is trivial (unlikely) or conditional complexity is being hidden.
- Participants spend most time debating events rather than discovering them. This suggests the scope is too broad or the domain expert is absent.
- Pink notes mention "we'll decide that in design." Problems surfaced in the workshop should be classified now; deferral to later is deferred learning.
- A single person places most of the notes while others watch. The workshop failed its collaborative purpose; knowledge is still siloed.
- The timeline makes sense to developers but business experts are nodding without conviction. The model doesn't match reality; run it again with more ground-truth voices.

## Output Format

```
## Event Storming Outcome

**Scope:**
- Start event: <...>
- End event: <...>

**Process Timeline (Events → Commands → Actors)**
| Sequence | Event (Orange) | Command (Yellow) | Actor (Blue) | Notes |
|---|---|---|---|---|
| 1 | <...> | <...> | <...> | <...> |
| 2 | <...> | <...> | <...> | <...> |
| ... | ... | ... | ... | ... |

**Aggregates Identified**
- Aggregate 1: <name> (events: <...>, <...>)
- Aggregate 2: <name> (events: <...>, <...>)

**Integration Points (Aggregate-to-Aggregate Communication)**
| From Aggregate | To Aggregate | Trigger | Owned by |
|---|---|---|---|
| <...> | <...> | <...> | <...> |

**Problems, Assumptions, and Open Questions (Pink Notes)**
| Category | Question/Issue | Owner | Follow-up |
|---|---|---|---|
| Requirement gap | <...> | <...> | <...> |
| Assumption conflict | <...> | <...> | <...> |
| Unclear ownership | <...> | <...> | <...> |
| Technical impedance | <...> | <...> | <...> |

**Confidence**
<high | medium | low> — <justification. Examples: "high — 7 of 8 participants agreed on the timeline and all aggregates; 3 open questions remain but are clearly scoped"; "medium — business and dev had one conflict on payment timing that remains unresolved; read models were not modeled"; "low — scope kept expanding; no clear agreement on what triggers inventory reservation">
```
