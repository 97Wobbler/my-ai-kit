---
name: gricean-maxims
display_name: Gricean Maxims
class: lens
underlying_class: native
domain: philosophy
source: Paul Grice, "Logic and Conversation" (1975)
best_for:
  - Diagnosing breakdowns in dialogue and collaboration
  - Detecting when speakers are being misleading or evasive
  - Clarifying implicit expectations in written or spoken communication
one_liner: "Check conversation quality and sincerity against four cooperative maxims."
---

# Gricean Maxims

## Overview

Grice's Cooperative Principle states that conversational participants implicitly agree to be maximally informative, truthful, relevant, and clear. When these maxims are violated, the conversation either breaks down or reveals deception, evasion, or misalignment of intent. Practitioners use this lens to audit whether a piece of communication — a design specification, a policy statement, a meeting transcript, an email thread — respects the contract implied by cooperative dialogue. The discipline is separating honest violations (where the speaker acknowledges the breach) from strategic ones (where the speaker obscures the violation).

## Analytical Procedure

### Phase 1 — Extract the Exchange

1. **Identify the communicative goal.** What question was the speaker meant to answer, or what topic was raised? Write it plainly. If the exchange is asymmetric (one party asking, one answering), note the direction.

2. **Transcribe the actual response.** Capture the speaker's exact words or, for written text, the complete statement without paraphrase.

3. **Note the addressee and context.** Who received this message? What was the relationship (peer, boss, customer, stranger)? What prior context existed? These matter because the maxims are interpreted relative to what the addressee reasonably expected.

### Phase 2 — Test Against Each Maxim

Apply each of the four maxims. For each, ask: "Is the speaker in violation?" If yes, determine whether the violation is *acknowledged* (the speaker signals they're breaking the rule on purpose) or *hidden* (the speaker acts as if the rule is being followed).

#### Maxim of Quantity
*"Make your contribution as informative as is required for the current purpose of the exchange. Do not make your contribution more informative than is required."*

4. **Check sufficiency.** Is the speaker providing enough information for the addressee to answer the original question or understand the topic? 
   - If no: underinformative. Example: answering "What happened in the meeting?" with "It was good."
   - If yes but sparse: borderline. Example: answering with only facts, no interpretation when interpretation was expected.
   - If yes with surplus: overinformative. Example: answering "Do you have the file?" with a 2000-word explanation of the file system.

5. **Assess acknowledgment.** If the response is underinformative, does the speaker signal it? ("I don't have time to explain fully" / "The short version is..."). If they don't signal it, assume hidden violation.

#### Maxim of Quality
*"Do not say what you believe to be false. Do not say that for which you lack adequate evidence."*

6. **Check truthfulness.** Does the speaker appear to believe what they're saying, or are they being deceptive? Look for:
   - Factual errors that should have been caught (suggests negligence, not intent).
   - Ambiguous language used to avoid saying something false while implying it ("The project is on track" when the deadline has moved, but the project itself did advance).
   - Claims without evidence ("We've always done it this way" without evidence of how long "always" is).

7. **Assess acknowledgment.** If the speaker is being evasive or borderline dishonest, do they flag it? ("I'm not certain, but..."; "This may be too strong, but..."). If not, assume hidden violation.

#### Maxim of Relation
*"Be relevant. Make your contribution appropriate to the immediate goals of the exchange."*

8. **Check relevance.** Does the response actually address the question or topic that was raised?
   - If yes and direct: relevant.
   - If yes but tangential: borderline. Example: answering "Why did the project slip?" with "The timeline was optimistic and we have limited capacity." (Addresses cause but not the questioner's implied concern about responsibility or next steps.)
   - If no: irrelevant. Example: answering "Do we have budget?" with "The CFO is out this week."

9. **Assess acknowledgment.** If irrelevant, does the speaker flag the detour? ("This may be off-topic, but..."; "Rather than X, I think we should focus on Y because..."). If not, assume hidden violation.

#### Maxim of Manner
*"Avoid obscurity of expression. Avoid ambiguity. Be brief. Be orderly."*

10. **Check clarity.** Is the language clear to the addressee? Consider:
    - Technical jargon used without definition (obscurity).
    - Sentences that could mean multiple things (ambiguity). Example: "Some staff objected to the change" (does it mean a few, or a meaningful portion?).
    - Tangents that obscure the main point (disorder).
    - Unnecessarily long explanations (prolixity).

11. **Assess acknowledgment.** If unclear, does the speaker signal it? ("I know this is jargon-heavy, but..."; "To put it plainly, what I mean is..."). If not, assume hidden violation.

### Phase 3 — Classify Violations

12. **For each violation found, classify it:**
    - **Acknowledged violation:** The speaker explicitly signals they are breaking the maxim (e.g., "I can't give you all the details," "I'm speculating here"). This is often cooperative — the speaker is being honest about the breach.
    - **Hidden violation:** The speaker acts as if the maxim is being followed when it isn't. This is often deceptive or indicates misalignment.
    - **No violation:** The maxim is respected.

13. **Count violations by type and acknowledgment status.** A communication with no acknowledged violations but multiple hidden violations is significantly less trustworthy than one with acknowledged violations.

### Phase 4 — Assess Trustworthiness and Alignment

14. **Evaluate the pattern.** 
    - Zero violations (acknowledged or hidden): communication is cooperative and clear.
    - Mostly acknowledged violations: communication is honest about its limitations; trustworthy but incomplete.
    - Mixed violations (some acknowledged, some hidden): communication has integrity gaps; selective honesty.
    - Mostly hidden violations: communication is evasive or deceptive; low trustworthiness.

15. **Infer intent.** Does the pattern suggest:
    - Honest limitation (speaker lacks information or time)?
    - Strategic obscuring (speaker is hiding something)?
    - Misalignment (speaker and addressee have different expectations of what "complete" or "relevant" means)?

## Evaluation Criteria

| Check | Pass |
|---|---|
| The communicative goal is stated plainly (under 20 words) | Y/N |
| The speaker's exact response is transcribed or quoted | Y/N |
| All four maxims were tested against the response | Y/N |
| Each maxim test includes evidence (quoted phrase or specific omission) | Y/N |
| Violations are classified as acknowledged or hidden | Y/N |
| Intent inference is grounded in the violation pattern, not speculation | Y/N |

## Red Flags

- The analysis finds violations in only one or two maxims. Most real communication violates multiple maxims; narrow findings suggest the interrogation was shallow.
- All violations are classified as "acknowledged." While possible for very self-aware speakers, this is rare; recheck for hidden violations, especially in Relation and Manner.
- No violations at all. Either the communication is exceptionally clear (possible but uncommon) or the analyst was too lenient in applying the maxims.
- Intent is stated with high confidence ("The speaker is definitely lying") without grounding in multiple hidden violations. A single hidden violation is ambiguous; patterns are stronger.
- The analysis confuses speaker intent with speaker error. A speaker who lacks information is not being deceptive, even if the response violates Quantity.

## Output Format

```
## Gricean Maxims Assessment

**Communicative goal:**
<plain statement of what the addressee expected to learn or be told>

**Speaker's response:**
> <quoted or transcribed>

**Context:**
<Addressee, relationship, prior context in 2-3 sentences>

### Maxim of Quantity
- Informative enough? [yes | no | borderline]
- Evidence: <quoted phrase or specific gap>
- Acknowledged? [yes | no]
- Violation: [none | acknowledged | hidden]

### Maxim of Quality
- Truthful and evidenced? [yes | no | borderline]
- Evidence: <specific claim, hedging, or missing evidence>
- Acknowledged? [yes | no]
- Violation: [none | acknowledged | hidden]

### Maxim of Relation
- Relevant to the goal? [yes | no | borderline]
- Evidence: <tangent or gap relative to original question>
- Acknowledged? [yes | no]
- Violation: [none | acknowledged | hidden]

### Maxim of Manner
- Clear, brief, orderly? [yes | no | borderline]
- Evidence: <jargon, ambiguity, or disorder>
- Acknowledged? [yes | no]
- Violation: [none | acknowledged | hidden]

### Violation Summary
- Acknowledged violations: _
- Hidden violations: _
- Total violations: _

### Inferred Intent
<Honest limitation | Strategic obscuring | Misalignment | Cooperative>

**Justification:** <Pattern of violations and their distribution>

### Confidence
<high | medium | low> — <Confidence is high if the response contains multiple hidden violations in the same maxim, or a clear pattern across maxims. Medium if violations are mixed or ambiguous. Low if the response is largely compliant or context is unclear.>
```
