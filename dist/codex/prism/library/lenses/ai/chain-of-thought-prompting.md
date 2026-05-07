---
name: chain-of-thought-prompting
display_name: Chain-of-Thought Prompting
class: lens
underlying_class: native
domain: ai
source: Wei et al., 2022 (Google Research); popularized in LLM prompting practice
best_for:
  - Diagnosing reasoning failures in LLM outputs
  - Evaluating whether an LLM has actually solved a problem or merely pattern-matched
  - Improving answer quality by forcing intermediate justification
one_liner: "Elicit explicit reasoning steps to verify and improve LLM response quality."
---

# Chain-of-Thought Prompting

## Overview

Chain-of-Thought (CoT) prompting instructs a language model to show its reasoning step-by-step before producing a final answer, rather than jumping directly to the conclusion. The discipline is distinguishing shallow pattern-matching from genuine reasoning — a model can output a correct answer by accident, and only the intermediate steps reveal whether the reasoning was sound. Practitioners use this lens to evaluate whether an LLM understood a problem or merely retrieved a memorized surface pattern, and to identify where reasoning went wrong when answers are incorrect.

## Analytical Procedure

### Phase 1 — Prompt Engineering and Execution

1. **State the problem precisely.** Write the exact question or task you are asking the LLM, as it will be presented to the model. Include all context and constraints the model must consider.

2. **Craft a CoT instruction.** Add an explicit directive to the prompt:
   - **Minimal version:** "Let's think step by step."
   - **Explicit version:** "Work through this problem step by step. Show your reasoning for each step before arriving at your final answer."
   - **Few-shot version:** Provide 1–3 worked examples of problems with step-by-step reasoning, then ask the same of the target problem.

3. **Execute the prompt twice:** once with the CoT instruction and once without (the baseline). Use identical model temperature/sampling settings for both runs. Record both outputs completely.

4. **Parse the CoT output into discrete steps.** Number each logical step the model takes. A step is a single inference, calculation, or rule application. Do not combine "step 1: calculate X" and "step 2: use X to find Y" into one step.

### Phase 2 — Step-Level Verification

5. **For each step, answer:**
   - **Is the step a restatement of the problem, or a new inference?** (Restatement = not a reasoning step; skip it.)
   - **Is the step logically valid?** Does it follow from the premises stated before it?
   - **Is the step grounded in external fact, internal logic, or pattern?** Tag each:
     - *Fact-based*: References a verifiable external truth (date, definition, law).
     - *Logic-based*: Follows deductively or inductively from prior statements.
     - *Pattern-based*: Appears to rely on statistical similarity rather than reasoning (e.g., "this sounds like a problem about X, so the answer is usually Y").
   - **Is the step necessary to reach the final answer?** Remove it mentally and ask: could the model have skipped it without weakening the argument?

6. **Mark each step as one of:**
   - **Sound** — valid, grounded, necessary.
   - **Valid but weak** — logically correct but relies on unstated assumptions or pattern-matching.
   - **Incomplete** — correct direction but missing sub-steps or justification.
   - **Flawed** — contains an error in logic or fact.
   - **Non-reasoning** — restatement, hedging, or filler; no new inferential content.

### Phase 3 — Answer Quality Assessment

7. **Compare the final answer to ground truth (if available).** Record: correct / incorrect / partially correct.

8. **If the answer is correct, check whether the reasoning supports it:**
   - **Sound reasoning, correct answer**: The model reasoned its way to the answer. CoT worked.
   - **Weak/flawed reasoning, correct answer**: The model pattern-matched the answer but dressed it in pseudo-reasoning. CoT masked the gap.
   - **Sound reasoning, incorrect answer**: The model reasoned well but was misled by a bad premise or unseen constraint. CoT revealed the failure mode.
   - **Flawed reasoning, incorrect answer**: The model failed at both reasoning and answer. CoT made the failure transparent.

9. **Count reasoning quality metrics:**
   - Total steps: _
   - Sound steps: _
   - Flawed/incomplete steps: _
   - Non-reasoning steps: _
   - Sound-step ratio: _%

10. **Compare CoT vs. baseline:** Did adding the CoT instruction improve answer quality? If the baseline answer was correct and the CoT answer is identical and the reasoning is sound, CoT validated the answer. If the baseline was wrong and CoT corrected it, CoT was transformative. If both are correct but CoT is flawed, note that the model got lucky.

## Evaluation Criteria

| Check | Pass |
|---|---|
| Problem statement is precise and unambiguous | Y/N |
| CoT instruction was applied consistently (same model, temperature, context) | Y/N |
| Both CoT and baseline outputs were captured in full | Y/N |
| Each CoT step was parsed and tagged (Sound/Weak/Incomplete/Flawed/Non-reasoning) | Y/N |
| At least one step was classified as fact-based, logic-based, or pattern-based | Y/N |
| Final answer was compared to ground truth or expert evaluation | Y/N |
| CoT and baseline outputs were explicitly compared | Y/N |

## Red Flags

- **All steps are marked as Sound.** Either the problem is trivial or the evaluation was lenient. Re-read the steps and ask: did the model actually justify each claim, or did it assume the reader would?
- **No non-reasoning steps identified.** Real CoT outputs usually include restatements, hedges, or filler. If none appear, the parsing may be too coarse-grained or the model output unusually lean.
- **The reasoning is flawed but the answer is correct.** This is the most dangerous outcome — the lens has revealed that the model got the right answer through wrong reasoning. Do not trust this model for similar problems where the surface pattern differs.
- **CoT and baseline answers are identical and both correct.** CoT did not add value here. Check whether the problem was simple enough that reasoning was unnecessary or whether the model pattern-matched equally in both cases.
- **Step tagging is inconsistent.** A step you marked "fact-based" in one output is called "pattern-based" in another. Return to the model's actual words and ensure you are distinguishing between confident assertion, cautious claim, and analogy language.

## Output Format

```
## Chain-of-Thought Analysis

**Problem:**
<exact problem as presented to the model>

### Execution
- **CoT instruction used:** <instruction text>
- **Baseline output:** <answer only>
- **CoT output:** <full reasoning + answer>

### Step-by-Step Breakdown

| Step # | Statement | Type | Ground | Valid | Tag |
|---|---|---|---|---|---|
| 1 | <...> | Inference / Restatement | Fact / Logic / Pattern | Y/N | Sound / Weak / Incomplete / Flawed / Non-reasoning |
| 2 | <...> | ... | ... | ... | ... |

### Answer Comparison
- **Ground truth (if available):** <correct answer>
- **Baseline answer:** <answer> — Correct / Incorrect / Partial
- **CoT answer:** <answer> — Correct / Incorrect / Partial
- **Match:** Y/N

### Reasoning Quality
- Total steps: _
- Sound: _ | Weak: _ | Incomplete: _ | Flawed: _ | Non-reasoning: _
- Sound-step ratio: _%

### Reasoning-Answer Alignment
<Categorize as: Sound reasoning + correct answer / Weak reasoning + correct answer / Sound reasoning + incorrect answer / Flawed reasoning + incorrect answer>

### Key Finding
<What did CoT reveal about the model's problem-solving that the baseline answer alone would have hidden?>

### Confidence
<high/medium/low> — <justification>
```
