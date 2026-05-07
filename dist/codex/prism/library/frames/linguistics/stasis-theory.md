---
name: stasis-theory
display_name: Stasis Theory
class: frame
underlying_class: native
domain: linguistics
source: Hermagoras of Temnos (c. 150 BCE), systematized by Cicero (De Oratore, Brutus)
best_for:
  - Locating the point of disagreement in a dispute or argument
  - Sorting conflicting claims into categories that demand different kinds of proof
one_liner: "Classify a disagreement as Conjecture / Definition / Quality / Procedure to identify which kind of evidence resolves it."
---

# Stasis Theory

## Overview

Stasis Theory is a frame for locating the precise point at which two parties stop agreeing in an argument or dispute. Its core claim is that most disagreements do not fail because one side is irrational; they fail because the disputants are answering **different questions**. By identifying which of four questions is actually at stake, you can determine what kind of evidence, argument, or proof is relevant — and what kind is a waste of time. The theory does not resolve disputes; it clarifies what would need to be proven to move the needle.

## Categories

1. **Conjecture** (Does it exist? Did it happen? Is it a fact?)
   - Disagreement about whether something occurred, exists, or is true as a matter of fact.
   - The question is purely about reality: did the act take place, or not?
   - Discriminating criterion: both parties accept the definition and value of the thing in question, but one denies its existence or occurrence.
   - Example: "Did the defendant leave the building at midnight?" (not *why*, not *whether it matters*).

2. **Definition** (What is it? How do we name or categorize it?)
   - Disagreement about what category or name applies to an admitted fact.
   - The fact is not in dispute; the interpretation of its nature is.
   - Discriminating criterion: both parties agree the act or thing exists, but disagree on what to call it or how to classify it.
   - Example: "The defendant left the building. But was it an 'escape' or an 'exit'?" or "Is this software piracy or fair use?"

3. **Quality** (Is it good or bad? Does it matter? What is its value or significance?)
   - Disagreement about the moral, legal, or practical significance of an admitted fact under its admitted classification.
   - The fact and its category are settled; the evaluation is not.
   - Discriminating criterion: both parties agree on what happened and what to call it, but disagree on whether it was justified, wrongful, acceptable, or important.
   - Example: "The defendant left the building without permission. But was this trespass justified by self-defense?" or "The code was copied. But is the copying defensible under open-source license?"

4. **Procedure** (What is the proper authority, jurisdiction, or method to decide this?)
   - Disagreement about who has the power to judge the matter, by what standard, or through what process.
   - Facts, definitions, and evaluations may all be agreed; the dispute is about **legitimacy and venue**.
   - Discriminating criterion: one party claims the matter is outside the jurisdiction or authority of the forum, or that a different procedure should apply.
   - Example: "This is a civil matter, not a criminal one, so the burden of proof is 'preponderance,' not 'beyond a reasonable doubt.'" or "Only the legislature can decide this; courts have no authority."

## Classification Procedure

1. State the disagreement in a single sentence: "Party A claims X; Party B claims Y."
2. Ask: **"Do both parties agree that the alleged fact occurred or exists?"**
   - If **no** → the stasis is **Conjecture**. Stop.
   - If **yes** → go to step 3.
3. Ask: **"Do both parties agree on what to call or categorize the fact?"**
   - If **no** → the stasis is **Definition**. Stop.
   - If **yes** → go to step 4.
4. Ask: **"Do both parties agree that the fact (as categorized) is bad, unjustified, or legally wrongful?"**
   - If **no** → the stasis is **Quality**. Stop.
   - If **yes** → go to step 5.
5. Ask: **"Do both parties agree that the same court, judge, or authority has legitimate power to decide this matter?"**
   - If **no** → the stasis is **Procedure**. Stop.
   - If **yes** → the parties agree entirely (no genuine stasis exists).

## Implications per Category

| Category | What kind of proof is relevant | What kind is irrelevant |
|---|---|---|
| **Conjecture** | Evidence, testimony, documentation, forensics. Answers: Did it happen? | Moral arguments, evaluations of significance, jurisdictional arguments. |
| **Definition** | Precedent, linguistic evidence, analogies, definitional authorities (law, usage). Answers: What is this thing? | Fresh evidence about the fact itself; moral arguments about whether it matters. |
| **Quality** | Precedent, policy, moral or legal principles, mitigating or aggravating factors. Answers: Was it justified/wrongful? | New factual evidence (the fact is already established); arguments about what to call the act. |
| **Procedure** | Constitutional law, jurisdiction, authority, rules of evidence, standing. Answers: Who decides and how? | Any substantive arguments about the underlying facts, definitions, or values. |

A lenslab agent's implication: once the stasis is identified, **only load the lenses appropriate to that stasis**. Loading Definition lenses to fight a Conjecture stasis is a systematic waste of effort.

## Common Misclassifications

- **Conjecture mistaken for Definition.** One party argues "that didn't happen" while the other argues "that's not what you'd call it." The tell: if you can produce a video of the event, the first party's disagreement disappears, but the second's does not.
- **Definition mistaken for Quality.** Disputing whether an act is "theft" vs. "borrowing" vs. "gift" (Definition) versus whether the act was justified (Quality). The tell: if both parties accept "the defendant took the item," Definition is settled and you're in Quality.
- **Quality mistaken for Procedure.** Arguing whether an act was morally justified (Quality) versus whether a court has authority to adjudicate justification (Procedure). The tell: Procedure questions often start with "Is this even a matter for a court to decide?"
- **Treating all four questions as equally important in a single dispute.** Many real cases have stases at multiple levels, but there is usually a **primary stasis** where the dispute is sharpest. Arguing all four in parallel dilutes focus.
- **Skipping steps in the procedure and misidentifying stasis.** Jumping from "did it happen?" directly to "was it justified?" without confirming Definition agreement first. The tell is that Definition disagreements resurface mid-argument and derail the thread.
