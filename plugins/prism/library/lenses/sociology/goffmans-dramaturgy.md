---
name: goffmans-dramaturgy
display_name: Goffman's Dramaturgy
class: lens
underlying_class: native
domain: sociology
source: Erving Goffman, The Presentation of Self in Everyday Life (1959)
best_for:
  - Analyzing asymmetries in how teams or individuals present themselves across contexts
  - Identifying performance gaps between official narrative and backstage reality
  - Understanding power dynamics embedded in information control
one_liner: "Analyze front-stage and back-stage interaction to surface role performance and information-control asymmetries inside organizations."
---

# Goffman's Dramaturgy

## Overview

Dramaturgy treats social interaction as theatrical performance. Actors (individuals, teams, organizations) maintain a "front stage" where they present a curated self to an audience, and a "back stage" where they prepare, complain, drop the act, and make decisions invisible to the audience. The analytical power lies in identifying what information is kept separate and who controls the boundary. Practitioners use this when they suspect official narratives (what the organization says it does) diverge sharply from operational reality (what actually happens), or when a team's internal behavior contradicts its external brand.

## Analytical Procedure

### Phase 1 — Map the Stages

1. **Identify the primary actor.** This is the individual, team, or organization you're analyzing. Write it in one sentence: "The marketing department" or "Product leadership."

2. **Identify the audience(s).** Who is the front stage performance for? List them explicitly:
   - External audience (customers, press, regulators, competitors)
   - Internal audience (employees at other levels, board, investors)
   - Mixed audiences that see different versions
   Write each on a separate line.

3. **Define the front stage.** What image, narrative, or persona does the actor project to each audience? Collect evidence:
   - Official statements (website, annual reports, product marketing, public interviews)
   - Formal meetings or presentations the audience attends
   - Communication explicitly designed for that audience
   Write 3-5 bullet points per audience group.

4. **Define the back stage.** What happens when the audience is not present? Collect evidence:
   - Internal Slack, email, or recorded conversations
   - Closed-door meetings, strategy sessions, retrospectives
   - Anonymous feedback, exit interviews, or confidential surveys
   - What employees say in private conversations or anonymous forums
   Write 3-5 bullet points for the same actor.

5. **Identify the boundary keepers.** Who controls access between front and back? Who decides what information flows across?
   - Formal gatekeepers (managers, comms teams, legal)
   - Informal gatekeepers (senior engineers, unofficial historians)
   - Technology (access controls, encryption, logs)
   - Culture (what people feel safe saying aloud vs. privately)
   List 4-6 mechanisms or people.

### Phase 2 — Identify Gaps and Asymmetries

6. **For each audience, compare front stage to back stage.** Use this matrix:

   | Audience | Front stage claim | Back stage reality | Gap size | Who knew the gap? |
   |---|---|---|---|---|
   | Customers | <what's promised> | <what's delivered> | Large/Medium/Small | Leadership only / widely known |
   | Employees | <what's said> | <what's actually prioritized> | L/M/S | who |
   | Investors | <what's reported> | <what's true> | L/M/S | who |

7. **For each large or medium gap, ask: Is this gap intentional or accidental?**
   - **Intentional**: The actor knows the gap exists and maintains it deliberately (marketing exaggerates, leadership withholds bad news, engineering hides technical debt).
   - **Accidental**: The actor believes the front stage narrative and is genuinely surprised when the back stage reality emerges.
   - **Sliding**: The gap widened over time without conscious decision (a promise that became impossible to keep).
   Mark each gap.

8. **Trace information flow violations.** Where does back stage information leak into front stage (or vice versa)?
   - Whistleblowers, leaks, or public arguments
   - Employees contradicting official narrative on social media
   - Customers discovering discrepancies and publicizing them
   - Write 2-3 concrete incidents if they exist; otherwise write "No observed breaches."

### Phase 3 — Assess Sustainability and Risk

9. **For each large gap, estimate how long the performance can be maintained.**
   - Can the back stage continue supporting the front stage narrative indefinitely? (e.g., can the team keep shipping features on schedule if leadership privately knows the codebase is rotting?)
   - What would force a collapse (employee departure, customer complaint, market shift, regulatory finding)?
   - Write a 1-2 sentence sustainability note per gap.

10. **Identify who bears the cost of the performance.** Who suffers from maintaining the gap?
    - Front-stage performers (employees forced to defend a narrative they don't believe)
    - Back stage workers (engineers working unsustainable hours to meet overpromised deadlines)
    - Audience members deceived by the gap
    - List 2-3 stakeholders per major gap.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Primary actor is clearly named (person, team, or org) | Y/N |
| At least 2 distinct audiences are identified | Y/N |
| Front stage includes 3+ pieces of evidence (quotes, documents, statements) | Y/N |
| Back stage includes 3+ pieces of evidence (private communications, actions, admissions) | Y/N |
| Boundary keepers are named or described concretely | Y/N |
| At least 1 front/back gap is documented with specific claims on both sides | Y/N |
| Each gap is marked intentional/accidental/sliding | Y/N |
| Sustainability and stakeholder cost are estimated for at least 1 gap | Y/N |

## Red Flags

- Front stage and back stage look nearly identical. Either the actor has genuine alignment (rare, especially at scale) or the back stage evidence is shallow (private messages that are still performative, or hearsay).
- All gaps are marked "accidental." This usually means the analyst lacked access to actual decision-making conversations and is inferring intent from outcomes.
- The analysis is filled with adjectives ("toxic culture," "dishonest leadership") but no concrete gaps. Dramaturgy requires specific claims and their negations, not character judgment.
- Only one audience is analyzed. Most actors perform differently for different groups — the interesting work is in the *variation* and who controls it.
- Boundary keepers are not named. "Management controls the narrative" is vague. Who specifically? By what mechanism?
- No consideration of sustainability. An unsustainable performance is more urgent and easier to act on than a stable one — the analysis should flag this.

## Output Format

```
## Dramaturgy Assessment

**Primary actor:**
<individual, team, or organization>

### Front Stage (by audience)

**Audience: <name>**
- <claim 1 with source>
- <claim 2 with source>
- <claim 3 with source>

**Audience: <name>**
- ...

### Back Stage

- <reality 1 with source>
- <reality 2 with source>
- <reality 3 with source>

### Boundary Keepers
1. <person/role/mechanism>
2. <person/role/mechanism>
3. ...

### Front/Back Gaps

| Audience | Front claim | Back reality | Gap | Intentional? | Cost to whom |
|---|---|---|---|---|---|
| <...> | <...> | <...> | L/M/S | Y/N/Sliding | <...> |

### Information Flow Breaches
<Incidents where back stage became public or front stage was contradicted>

### Sustainability Analysis
- Gap 1: <1-2 sentence estimate of how long this performance can hold>
- Gap 2: ...

### Confidence
<high/medium/low> — <justification based on access to evidence and observed breaches>
```
---
