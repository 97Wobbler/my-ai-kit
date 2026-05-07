---
name: eval-harness-frameworks
display_name: Evaluation Harness Frameworks
class: lens
underlying_class: native
domain: ai
source: HELM (Liang et al., 2022); BIG-bench (Srivastava et al., 2022); lm-eval (EleutherAI, 2023)
best_for:
  - Structuring benchmark design for language models
  - Identifying coverage gaps in evaluation suites
  - Comparing model behavior across standardized tasks
one_liner: "Structure language-model evaluation: benchmark design, task coverage, metric consistency."
---

# Evaluation Harness Frameworks

## Overview
An evaluation harness is a reusable infrastructure for measuring language model capabilities across multiple tasks, datasets, and metrics in a consistent, reproducible way. Frameworks like HELM, BIG-bench, and lm-eval provide templates for task definition, input/output formatting, metric computation, and result aggregation. Practitioners use these when designing benchmarks that must be both comprehensive (covering multiple capability areas) and trustworthy (yielding results that survive replication and comparison across models).

## Analytical Procedure

### Phase 1 — Map the Harness Architecture

1. **Identify the harness type.** Which framework is being used or designed?
   - **HELM**: Holistic evaluation across model scale, domains, and metrics; emphasizes scenario-centric design.
   - **BIG-bench**: Community-contributed tasks with standardized input/output format; scale-focused evaluation.
   - **lm-eval**: Lightweight task harness with per-task configurations; emphasis on speed and reproducibility.
   Note the framework choice, as it determines available abstractions (scenarios vs. tasks vs. task instances).

2. **List all task groups / scenarios / benchmarks included.** For each group, record:
   - Domain (e.g., QA, translation, commonsense reasoning)
   - Number of instances
   - Primary metric (accuracy, BLEU, F1, etc.)
   - Data source (synthetic, crowdsourced, existing corpus)

3. **Document the I/O contract for each task.**
   - Input format: Is it a single string, JSON, a template with placeholders?
   - Output format: Free-form text, multiple choice, structured output?
   - Post-processing rules: How is the model's raw output converted to a scorable form (e.g., extracting the first token, case-folding, regex matching)?
   - Scoring rubric: Exact match, substring match, semantic equivalence, human judgment?

4. **Trace metric computation.**
   - For each metric (e.g., accuracy, F1, BLEU), write the formula or algorithm.
   - Identify dependencies: Does macro-averaging mask per-group performance? Are there subgroups (e.g., by difficulty, demographic) that deserve separate reporting?
   - Check for metric alignment: Do the metrics actually measure what the task claims to measure?

5. **Audit the harness for coverage gaps.**
   - Are there capability areas (reasoning, multilingual, code, safety) that are under-represented?
   - Are there known model failure modes (e.g., prompting sensitivity, hallucination on rare entities) that the benchmark is designed to catch or avoid?
   - Do task difficulties span a realistic range, or do most instances cluster at one difficulty level?

### Phase 2 — Examine Task Validity and Reproducibility

6. **For 2–3 representative tasks, manually run the evaluation pipeline.**
   - Feed a sample input through the harness.
   - Confirm the post-processing rules work as documented.
   - Check that the scorer produces the expected output and confidence signal.
   - If results differ from published numbers, identify the source of divergence (version drift, randomness, platform differences).

7. **Review test-set leakage and contamination controls.**
   - Did the harness designers use train/test splits that reflect real-world use (e.g., by date, by source)?
   - Are there measures to detect if a model has seen the benchmark during pretraining (e.g., cross-referencing against known model train dates and public datasets)?
   - If the benchmark is updated over time, is versioning rigorous enough to allow fair comparison of older models?

8. **Check prompt and demonstration (few-shot) sensitivity.**
   - How many demonstrations were used? Are they random or hand-curated?
   - Did the designers run sensitivity analysis to see how much performance varies with different prompts or demonstrations?
   - Is the harness designed to allow both zero-shot and few-shot variants?

### Phase 3 — Assess Interpretation and Reporting

9. **Examine aggregate vs. disaggregated reporting.**
   - Does the harness report a single overall score, or does it break out results by category (domain, difficulty, demographic, language)?
   - Can readers identify which capability areas a model excels in vs. struggles with?
   - Are there known subgroup disparities (e.g., lower accuracy on African American English, or on low-resource languages) that the harness is designed to expose?

10. **Evaluate the quality of baseline comparisons.**
    - Are the baselines (e.g., random, human, prior SOTA) clearly defined and reproducible?
    - Is there enough context (dataset size, baseline training data, baseline architecture) to understand whether the model's score reflects true capability growth or just scaling effects?

11. **Review interpretation guidance in the harness documentation.**
    - Does the documentation warn against common misinterpretations (e.g., "a 60% score does NOT mean the model understands 60% of X")?
    - Are there caveats about task artifacts (e.g., "this benchmark has shallow annotation, so high scores may reflect surface heuristics rather than true reasoning")?
    - Is statistical significance reporting present (e.g., confidence intervals, p-values for model comparisons)?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Harness architecture (framework type, task groups, I/O contract) is fully documented | Y/N |
| Metric computation is traceable to code or a published algorithm | Y/N |
| At least one coverage gap is identified (missing capability area, underexplored failure mode) | Y/N |
| Manual evaluation of 2+ tasks reproduces published results or divergence is explained | Y/N |
| Test-set leakage and contamination controls are documented | Y/N |
| Disaggregated reporting (by category, subgroup, difficulty) exists or is flagged as missing | Y/N |
| Interpretation guidance includes at least one warning against overstatement | Y/N |

## Red Flags

- The harness reports only a single macro-averaged score and no per-category breakdown. Readers cannot identify capability gaps.
- Post-processing rules are vague ("models may output variations of the correct answer"). This makes reproduction difficult and invites subjective scoring.
- Few-shot demonstrations were hand-curated by task authors but sensitivity analysis is absent. Results may reflect demonstration quality more than model capability.
- Baselines are missing or poorly documented. Readers cannot contextualize whether a 70% score is near human or far behind.
- Documentation claims the harness measures X (e.g., reasoning) but tasks actually measure surface pattern matching. The gap between intent and design is not acknowledged.
- Metric choice is not justified. (Why F1 instead of accuracy? Why macro-average instead of micro?) This suggests the metric was chosen post-hoc to make results look better.
- The harness is reused from a prior publication with no revalidation on new data or new models. Drift is undetected.

## Output Format

```
## Evaluation Harness Assessment

**Harness Name & Framework:**
<name> (<HELM | BIG-bench | lm-eval>)

### Phase 1 — Architecture Mapping

**Task Groups / Scenarios:**
| Group | Domain | Instances | Metric | Source |
|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> |

**I/O Contract (example task):**
- Input: <format>
- Output: <format>
- Post-processing: <rules>
- Scoring: <rubric>

**Coverage Analysis:**
- Under-represented capability areas: <list>
- Known failure modes addressed: <yes/no, explain>
- Difficulty distribution: <assessment>

### Phase 2 — Validity & Reproducibility

**Manual Evaluation Results:**
- Task(s) tested: <list>
- Result reproduction: <match / divergence with source>
- If divergence: <explanation>

**Leakage & Contamination Controls:**
- Train/test split strategy: <description>
- Pretraining detection measures: <yes/no, describe>
- Versioning rigor: <assessment>

**Prompt Sensitivity:**
- Few-shot demonstrations: <count, hand-curated/random>
- Sensitivity analysis present: <yes/no>
- Zero-shot / few-shot variants available: <yes/no>

### Phase 3 — Interpretation & Reporting

**Aggregate vs. Disaggregated Reporting:**
- Overall score reported: <yes/no>
- Category breakdown available: <yes/no, list categories>
- Subgroup disparities surfaced: <yes/no>

**Baseline Comparisons:**
- Baseline(s) present: <list>
- Baseline documentation quality: <clear / vague>

**Interpretation Guidance:**
- Caveats / warnings present: <list key warnings>
- Statistical significance reporting: <none / confidence intervals / p-values>

### Key Findings

1. <Finding with evidence>
2. <Finding with evidence>

### Confidence
<high | medium | low> — <justification>
```
