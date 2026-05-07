---
name: working-backwards-pr-faq
display_name: Working Backwards / PR-FAQ
class: lens
underlying_class: native
domain: product-management
source: Amazon (Leadership Principle: "Customer Obsession"); formalized by Ian McAllister and popularized in product management circa 2010s
best_for:
  - Clarifying product vision before committing engineering resources
  - Testing whether a feature solves a real customer problem
  - Aligning stakeholders on the "why" before debating the "how"
one_liner: "Start from the customer outcome and design backwards via a press release and FAQ."
---

# Working Backwards / PR-FAQ

## Overview

Working Backwards inverts the typical product development sequence. Instead of building a feature and then writing marketing copy to justify it, you write the press release and FAQ for the finished product first—before a single line of code is written. This forces clarity: if you cannot articulate why a customer should care, the feature is not ready for development. Practitioners use this when a product hypothesis feels vague, when stakeholders disagree on the problem being solved, or when a feature is in danger of solving the wrong problem well.

## Analytical Procedure

### Phase 1 — Write the Press Release

1. **Identify the customer persona.** Who is the intended user? Not "everyone" or "businesses." Name a specific type of person: "marketing managers at mid-market SaaS companies," "warehouse operators in cold-chain logistics." Write 1-2 sentences describing their current pain.

2. **State the problem they face.** What does the customer struggle with today? Use customer language, not internal jargon. Example: "Bad: 'We need to reduce API latency.' Good: 'Managers spend 30 minutes manually reconciling inventory across three systems every morning.'"

3. **Name the product.** Short, memorable, ideally a noun that a customer might actually use.

4. **Write a 3-4 sentence summary of what it does.** Focus on the outcome, not the mechanism. Bad: "Uses machine learning to optimize the workflow." Good: "Automatically flags inventory mismatches so managers can resolve them in seconds instead of manually checking three systems."

5. **State the key benefit.** What is the one thing the customer gets that they did not have before? Quantify if possible: time saved, money saved, error rate reduction, new capability.

6. **Add 2-3 supporting benefits.** These are secondary wins that make the product more attractive but are not the primary reason to buy.

7. **Include a customer quote.** Write a fictional but realistic quote from the intended customer explaining why they use this product and what changed for them. This forces you to think like the customer, not the company.

8. **Add a closing line.** When is it available? How do customers get access? What is the call to action?

### Phase 2 — Write the FAQ

9. **Anticipate 8-12 questions a customer or prospect might ask.** Structure them in rough order of importance. Do NOT write softball questions. Include:
   - "How is this different from <competitor or status quo>?"
   - "What data does this require from us?"
   - "How much does it cost?"
   - "What if we have <edge case>?"
   - "How long does implementation take?"
   - Any question that reveals a false assumption about what the product does.

10. **Answer each question as if you were explaining it to a skeptical customer.** Answers should be 2-4 sentences. Do not dodge. If you find yourself unable to answer a question clearly, that is a red flag — it means the product is not fully defined or solves a problem that does not actually exist.

11. **For each FAQ answer, note whether it required a design choice that was not yet made.** Flag these as "open questions" — they are places where the team still disagrees or the product spec is incomplete.

### Phase 3 — Evaluate the Press Release and FAQ

12. **Read the press release aloud as if you were a journalist.** Would you believe this is a real problem? Would you run this story? If the answer is "no" or "only if you added more credibility," the problem statement is weak.

13. **Have someone unfamiliar with your product read the press release without context.** Ask them: "What does this product do? Who is it for? Why would they use it?" Their answers should match your intention. If they do not, your marketing language is unclear—and if marketing is unclear, your product definition is unclear.

14. **Count how many questions in the FAQ you answered by saying "we will figure that out after launch" or "it depends."** If more than 2, the product is not ready to be built. Return to Phase 1.

15. **Identify the riskiest assumption in the FAQ.** Which answer, if wrong, would make the entire product worthless? This is the hypothesis you should test with customers before development begins.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Customer persona is specific and named (not "users" or "enterprises") | Y/N |
| Problem statement uses customer language, not feature language | Y/N |
| Press release is 3-4 sentences and focuses on outcome, not mechanism | Y/N |
| Key benefit is quantified or concrete (time, error reduction, capability) | Y/N |
| Customer quote is realistic and specific to the persona | Y/N |
| FAQ includes at least 3 questions that reveal unstated assumptions | Y/N |
| More than 50% of FAQ answers required no design choices (already decided) | Y/N |
| Riskiest assumption has been identified and is testable with customers | Y/N |

## Red Flags

- The press release describes a feature or technical capability instead of a customer outcome. ("Our machine learning model reduces latency" instead of "Managers get answers in seconds instead of minutes.")
- The customer persona is too broad ("businesses," "teams," "anyone who uses a database"). Broad personas hide disagreement about who the real customer is.
- The FAQ answers consistently include "we haven't decided yet" or "we'll see." The product definition is incomplete; do not start development.
- Reading the press release aloud produces skepticism from the team. If your own team does not believe the problem is real or important, customers will not either.
- The riskiest assumption is not clearly identified, or it is something you plan to address after launch. The whole point of this exercise is to find and test that assumption before writing code.
- The product has no key benefit, only a list of nice-to-haves. It solves a problem no one cares much about, or it solves it only marginally better than existing alternatives.

## Output Format

```
## Working Backwards Assessment

### Press Release

**Customer Persona:**
<specific description; e.g., "marketing managers at B2B SaaS companies with 50-500 employees">

**Problem Statement:**
<customer-language problem in 1-2 sentences>

**Product Name:**
<name>

**Summary:**
<3-4 sentences describing what it does, focused on outcome>

**Key Benefit:**
<the one thing the customer gets, quantified if possible>

**Supporting Benefits:**
1. <benefit>
2. <benefit>
3. <benefit>

**Customer Quote:**
> "<realistic quote from the persona explaining why they use it>"

**Call to Action:**
<availability and how to get access>

### FAQ

| Question | Answer | Open Design Choice? |
|---|---|---|
| <Q> | <A, 2-4 sentences> | Y/N |
| <Q> | <A> | Y/N |
| ... | ... | ... |

### Evaluation

**Problem Credibility:** <Would a journalist believe this is a real problem? Y/N>

**Clarity Test:** <Did a naive reader understand what the product does and who it's for? Y/N>

**Completeness:** <Count of FAQ answers that include "we haven't decided yet" or similar: _>

**Riskiest Assumption:**
<The one belief that, if wrong, makes the entire product invalid — and is testable with customers before development>

### Confidence
<high | medium | low> — <Justification. High confidence requires: specific persona, clear problem, realistic FAQ answers with few open design choices, and an identified testable assumption.>
```
