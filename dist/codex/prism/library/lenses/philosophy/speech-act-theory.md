---
name: speech-act-theory
display_name: Speech Act Theory
class: lens
underlying_class: native
domain: philosophy
source: J. L. Austin (How to Do Things with Words, 1962); John Searle (Speech Acts, 1969)
best_for:
  - Analyzing utterances to separate what is said from what is done
  - Debugging communication failures by tracing breakdown points across three layers
  - Evaluating whether an utterance achieves its intended effect
one_liner: "Track communicative intent and effect via the three-layer decomposition — locution, illocution, perlocution."
---

# Speech Act Theory

## Overview
Every utterance operates across three independent layers: the sounds/words produced (locution), the social act being performed (illocution), and the effect on the listener (perlocution). Most communication failures occur when one layer succeeds while another fails — the words are clear, but the act isn't recognized, or the act lands but doesn't move the listener. Practitioners use this lens to diagnose where a communication broke down and what would need to change to repair it.

## Analytical Procedure

### Phase 1 — Locate the Utterance

1. **Record or transcribe the utterance exactly.** Capture surrounding context: who said it, to whom, where, when, what happened just before.

2. **Extract the literal words only.** Strip pauses, tone, body language, sighs. This is the phonetic/syntactic layer (locution). Write it down word-for-word.

### Phase 2 — Identify the Illocutionary Act

The illocutionary act is the social move being made — the "force" of the utterance. It is not the same as the literal meaning of the words.

3. **Classify the primary illocutionary act.** Use this taxonomy:
   - **Assertive**: the speaker claims something is true ("The meeting is at 3pm")
   - **Directive**: the speaker asks the listener to do something ("Close the door")
   - **Commissive**: the speaker commits to do something ("I will deliver it by Friday")
   - **Expressive**: the speaker expresses an emotional or evaluative state ("I'm grateful" or "That's disgusting")
   - **Declarative**: the speaker changes reality by saying it ("You're fired" or "I pronounce you husband and wife")

4. **Identify the felicity conditions** — the background facts that must hold for the act to succeed. Use this framework:
   - **Propositional content**: what the utterance is about
   - **Preparatory conditions**: what must be true of the world and the speaker's situation for the act to be apt
   - **Sincerity condition**: what the speaker must intend or feel for the act to be sincere
   - **Essential condition**: what the act counts as

   Example: For "I promise to deliver it by Friday":
   - Content: future action (delivery)
   - Preparatory: speaker has ability to deliver; future is relevant (not "I promise to have been born")
   - Sincerity: speaker intends to deliver
   - Essential: the utterance counts as placing an obligation on the speaker

5. **Check whether each felicity condition is met.** For each condition, answer: yes/no/unclear. Flag mismatches.

6. **Determine whether the illocution was recognized by the listener.** Ask: did the listener understand what act was being performed, regardless of whether they complied? "I'm asking you to leave" is recognized as a directive even if the listener refuses. "Colorless green ideas sleep furiously" is not recognized as any illocutionary act, because the propositional content is incoherent.

### Phase 3 — Measure the Perlocutionary Effect

The perlocution is the actual causal effect on the listener's mental state or behavior — what they feel, believe, or do as a result.

7. **Identify the intended perlocutionary effect.** What did the speaker want to *happen* as a result of the utterance? (This is often different from the illocutionary act itself. "I'm asking you to leave" has directive force, but its intended perlocution is that the listener actually leaves, feels unwelcome, or understands they're not wanted.)

8. **Identify the actual perlocutionary effect.** What *actually* happened? Did the listener:
   - Comply with a directive?
   - Accept an assertion and change their belief?
   - Feel the emotion the speaker expressed?
   - Internalize the commitment?
   - Change their behavior, even indirectly?

9. **Compare intended vs. actual.** Note any divergence. Divergence is a failure, but failures are often instructive.

### Phase 4 — Diagnose the Breakdown

10. **If the utterance failed to achieve its effect, map the failure to a layer:**
    - **Locution failure**: the words were inaudible, ungrammatical, or in a language the listener doesn't speak. Example: thick accent makes "I'm asking you to leave" sound like "I'm asking you to believe."
    - **Illocution failure**: the listener heard the words but didn't recognize what social act was being performed. Example: the listener heard "I'm asking you to leave" as a hypothetical question, not a directive.
    - **Perlocution failure**: the listener recognized the act but was not moved by it. Example: the listener understood the directive but ignored it out of spite or misunderstanding the stakes.

11. **For each failed layer, list what would need to change:**
    - Locution: clarity, language choice, medium
    - Illocution: explicit framing ("I'm not asking, I'm telling you..."), authority, context-setting
    - Perlocution: emotional appeal, incentive, credibility, consequence

## Evaluation Criteria

| Check | Pass |
|---|---|
| Utterance recorded with full context (speaker, listener, setting) | Y/N |
| Locution extracted as literal words with no interpretation | Y/N |
| Illocutionary act classified into one of five categories | Y/N |
| All four felicity conditions identified and checked | Y/N |
| Distinction drawn between intended and actual perlocution | Y/N |
| Breakdown (if any) mapped to locution/illocution/perlocution layer | Y/N |

## Red Flags

- Illocutionary act is described as "the speaker wanted X to happen." That's perlocution, not illocution. Illocution is the social move (promising, requesting, asserting), not the hoped-for consequence.
- Felicity conditions are missing for the act type. Every illocutionary act has preparatory, sincerity, and essential conditions. If you can't articulate them, you haven't identified the act correctly.
- Locution and illocution are conflated. "The speaker asserted that the meeting is at 3pm" is not a description of the illocutionary act — asserting is. The content (meeting, time) is propositional, not illocutionary.
- Perlocution is assumed without checking. Just because the speaker said "I ask you to leave" does not mean the listener felt unwelcome or actually left. Verify.
- The breakdown is attributed to one layer when it spans multiple. Example: "The listener didn't understand" could be locution (didn't hear) or illocution (heard but missed the force) — check both.

## Output Format

```
## Speech Act Assessment

**Utterance (with context):**
Speaker: <...>
Listener: <...>
Setting: <...>
Exact words: "<...>"

### Layer 1 — Locution
Phonetic/syntactic form: <exact transcription>

### Layer 2 — Illocution
Illocutionary act type: [Assertive | Directive | Commissive | Expressive | Declarative]

Felicity conditions:
| Condition | Required | Met? | Evidence |
|---|---|---|---|
| Propositional content | <...> | Y/N/Unclear | <...> |
| Preparatory | <...> | Y/N/Unclear | <...> |
| Sincerity | <...> | Y/N/Unclear | <...> |
| Essential | <...> | Y/N/Unclear | <...> |

Recognized by listener? Yes / No / Partially

### Layer 3 — Perlocution
Intended effect: <...>
Actual effect: <...>
Success? Yes / No / Partial

### Breakdown Analysis (if applicable)
Failure layer: [Locution | Illocution | Perlocution | Multiple]
Description: <...>
Required change: <...>

### Confidence
<high | medium | low> — <justification>
```
