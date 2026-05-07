---
name: prompt-taxonomy
display_name: Prompt Taxonomy
class: frame
underlying_class: native
domain: ai
source: Wei et al. (Chain-of-Thought Prompting, 2022); Yao et al. (ReAct, 2022); Wang et al. (Self-Consistency, 2022); origin uncertain for taxonomy as unified frame
best_for:
  - Sorting a generative task by the inference strategy that best fits its complexity and error surface
  - Choosing which prompt structure to use before writing the prompt itself
one_liner: "Select reasoning strategies by task complexity and error surface."
---

# Prompt Taxonomy

## Overview

This frame sorts a generative task into one of five prompt structures, each paired with a different inference strategy. Its core claim is that the **complexity and error surface of the task dictates which strategy yields the best accuracy and reliability** — and applying the wrong strategy to a task (e.g., using zero-shot when the task requires step-by-step reasoning) is a systematic source of low accuracy and inconsistent outputs. Each category trades off simplicity, token cost, and latency against reasoning depth and error recovery. The act of classifying the task *constrains* which prompt structure is appropriate, and conversely, the choice of structure reveals what the model must do to solve the task at all.

## Categories

1. **Zero-shot**
   - The model is given **only the task definition and input, no examples**.
   - The model must retrieve the correct response pattern from its training weights on the first try.
   - Discriminating criterion: the task is so well-established in training data (e.g., "translate English to French," "summarize this text") that examples add no information gain.
   - Example: translating a sentence to Spanish; classifying sentiment on a clear review.
   - Token cost: lowest; latency: lowest; reasoning: minimal.

2. **Few-shot**
   - The model is given **the task definition plus 2–8 labeled examples** that demonstrate the expected input–output pattern.
   - Examples act as in-context precedents, triggering the model to infer and apply the pattern to the input.
   - Discriminating criterion: the task is well-defined but the specific format, edge cases, or constraints are not heavily represented in training (e.g., a proprietary classification schema, a non-standard output format, a narrow domain).
   - Example: classifying customer feedback into a custom 5-tier internal category; extracting structured data from a novel document format.
   - Token cost: moderate; latency: low–moderate; reasoning: pattern-matching from examples.

3. **Chain-of-Thought (CoT)**
   - The model is instructed to **"think step by step"** and produce intermediate reasoning steps before the final answer.
   - CoT forces the model to decompose a multi-step problem and externalizes its reasoning, making errors visible and recoverable.
   - Discriminating criterion: the task requires **multi-step logic, arithmetic, or constraint satisfaction** where a direct answer is error-prone; the intermediate steps are tractable for the model to articulate.
   - Example: word problems in arithmetic; logical deduction with multiple premises; planning a sequence of actions.
   - Token cost: moderate–high (additional reasoning tokens); latency: moderate–high; reasoning: explicit decomposition.
   - Note: often paired with few-shot examples that include reasoning steps.

4. **ReAct (Reasoning + Acting)**
   - The model is given **a task that requires interaction with external tools or environments** (search, computation, code execution, APIs) and is instructed to **alternate between reasoning and action**.
   - The model outputs a thought, then an action (tool call), observes the result, and repeats.
   - Discriminating criterion: the task **cannot be solved from training data alone** (e.g., current facts, computation, information retrieval) or requires **grounding in real-time feedback**.
   - Example: "What is the current weather in Tokyo?" (requires search); "Compute the 100th Fibonacci number" (requires code execution); "Debug this error message in a live system" (requires inspection tools).
   - Token cost: high (reasoning + actions + observations); latency: high (depends on tool latency); reasoning: adaptive based on feedback.

5. **Self-Consistency**
   - The model is prompted to **generate multiple independent reasoning chains or answers** (typically 5–20), then a final answer is **derived by voting, aggregation, or synthesis** across chains.
   - Each chain is an independent CoT or few-shot sample; inconsistencies across chains reveal brittleness, while consensus increases confidence.
   - Discriminating criterion: the task is **high-stakes, ambiguous, or error-prone** and the cost of re-sampling is lower than the cost of a wrong answer; or the task is **semantically open** (e.g., open-ended generation, creative writing, subjective judgment).
   - Example: a medical diagnosis from a complex case (generate multiple hypotheses and vote); a multi-part question where answers must align; summarizing a controversial topic.
   - Token cost: very high (N × cost of one sample); latency: very high; reasoning: voting/aggregation across diverse reasoning paths.

## Classification Procedure

1. **Describe the task:** Write one sentence stating the input, the transformation required, and the expected output.

2. **Ask: "Is this task in the model's training data with the exact format I need?"**
   - If **yes and the format is standard** → Zero-shot.
   - If **yes but the format is non-standard or domain-specific** → Few-shot.
   - If **no or uncertain**, go to step 3.

3. **Ask: "Does the task require step-by-step reasoning or decomposition?"**
   - If **no** (the answer is direct or a lookup) → return to step 2 and reconsider Few-shot.
   - If **yes** → go to step 4.

4. **Ask: "Can the model solve this from training data alone, or does it need external information or feedback?"**
   - If **training data is sufficient** → Chain-of-Thought.
   - If **external tools, real-time data, or grounding are required** → ReAct.

5. **Ask: "Is this task high-stakes, ambiguous, or error-prone enough that multiple attempts are justified?"**
   - If **no** → keep the category from step 4.
   - If **yes** → Self-Consistency (wrap the strategy from step 4 with multi-sampling and voting).

6. **Record the category and the inference strategy** (the method used to generate the final answer).

## Implications per Category

| Category | Inference strategy | What to do |
|---|---|---|
| **Zero-shot** | Direct response | Write the task definition clearly; assume the model knows the pattern. Useful as a baseline or sanity check. |
| **Few-shot** | Pattern induction from examples | Select 3–8 examples that cover the range of expected inputs and outputs; ensure consistency across examples. Order examples by complexity or diversity. |
| **Chain-of-Thought** | Explicit step-by-step decomposition | Instruct the model to "think step by step" or "show your work"; optionally provide one or two worked examples with reasoning steps. Budget for longer output. |
| **ReAct** | Interleaved reasoning and tool calls | Define the available actions/tools clearly; implement a loop that parses model output, executes the action, and feeds the observation back. Requires infrastructure (tool definitions, execution harness). |
| **Self-Consistency** | Multi-chain voting or aggregation | Generate N independent chains (typically 5–20); aggregate outputs by majority vote (for discrete answers) or clustering/synthesis (for open-ended). Higher cost and latency; use when stakes or error surface justify it. |

## Common Misclassifications

- **Zero-shot applied to a non-standard format.** Assuming the model will infer a proprietary category schema or output structure without examples. The tell is that outputs are inconsistent in format or interpretation. Consequence: post-processing fails or results are unreliable.

- **Few-shot when Chain-of-Thought is required.** Providing examples of final answers without intermediate steps when the task logic is multi-step. The tell is that the model produces the right answer structure but makes computational or logical errors. Consequence: accuracy plateaus below what reasoning would achieve.

- **Chain-of-Thought when ReAct is required.** Asking the model to reason through a task that requires current facts or computation it cannot perform from training data (e.g., "What is today's weather?"). The tell is hallucinated or outdated facts. Consequence: the answer is confidently wrong.

- **ReAct with poorly defined actions.** Defining actions or tools vaguely ("use the search tool") without specifying parameters, output format, or constraints. The tell is that the model calls tools incorrectly or the loop gets stuck. Consequence: the system fails or produces no useful output.

- **Self-Consistency when one chain is sufficient.** Over-engineering a low-stakes task that has a clear correct answer. The tell is that all N chains converge to the same answer. Consequence: wasted tokens and latency with no improvement in quality.

- **Treating Self-Consistency as a substitute for correct base prompting.** Using voting as a band-aid for an ill-defined task or weak examples. If each chain is poor, majority vote is just "confident wrong answer." Consequence: false confidence in a bad result.
