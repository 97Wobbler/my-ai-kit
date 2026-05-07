---
name: rlhf-dpo
display_name: RLHF / DPO Assessment
class: lens
underlying_class: native
domain: ai
source: Christiano et al. (2023, RLHF); Rafailov et al. (2023, DPO)
best_for:
  - Evaluating preference-based model training setups
  - Diagnosing alignment failures or reward model brittleness
  - Choosing between RLHF and DPO based on constraints
one_liner: "Verify whether preference-based learning captures and reinforces the intended reward signal."
---

# RLHF / DPO Assessment

## Overview
Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) are training frameworks that steer language models toward human-aligned behavior by learning from preference signals instead of absolute labels. Both operate on the same core assumption: humans can reliably rank model outputs, and a learned or implicit reward signal can guide optimization. This lens evaluates whether the preference data, reward model (if used), and training loop actually capture the intended behavior or merely surface-fit to the training distribution. Practitioners use this when deploying aligned models and suspecting that either the preference signal is noisy, the reward model has overfit to style rather than substance, or the training procedure produces models that behave differently in deployment than in calibration.

## Analytical Procedure

### Phase 1 — Data Audit

1. **Describe the preference dataset.** Record:
   - Source: human annotators, synthetic, hybrid, or model-generated?
   - Scale: how many preference pairs?
   - Domain: is it in-distribution with the deployment domain or a proxy (e.g., helpfulness on generic tasks)?
   - Annotator agreement: inter-rater reliability (Cohen's kappa, Fleiss' kappa, or percentage agreement). If unknown, this is a red flag.

2. **For each preference pair, ask: "Why would a human prefer this output?"** Do not assume the annotators had the same reason. Categorize observed reasons into at least three buckets:
   - **Explicit criteria**: helpfulness, safety, factuality, tone (these are often listed in annotation guidelines).
   - **Implicit criteria**: fluency, brevity, confidence, novelty (annotators apply these without instruction).
   - **Artifacts of the annotation context**: annotators might prefer longer responses because they look more effortful, or prefer responses that match the annotator's own style.
   
   Sample 50-100 preference pairs if the dataset is large. If you cannot articulate why a human would prefer one output without guessing, the signal is too weak.

3. **Check for annotation collapse.** Ask:
   - Do >80% of pairs have one output clearly better than the other, or is the distribution more uniform?
   - If collapse: the signal is strong but potentially brittle — the model will overfit easily.
   - If uniform: annotators disagree substantially; the learned signal will be noisy.

4. **Audit the negative examples.** For each preferred output, examine its paired negative. Is it:
   - A genuine error or failure mode? (high-quality negative)
   - A random or strawman output? (low-quality negative)
   - A nearly-equivalent output that humans barely prefer? (weak negative)
   
   Weak negatives teach the model almost nothing; strawman negatives teach false lessons.

### Phase 2 — Reward Model Evaluation (RLHF only)

If the method uses RLHF with an explicit reward model, proceed; if using DPO, skip to Phase 3.

5. **Fit a diagnostic probe to the reward model.** Train a small linear model to predict the reward model's scores from simple features (response length, presence of certain keywords, diversity metrics). If the linear probe explains >50% of variance, the reward model is relying on shallow, learnable patterns — potentially Goodhartable.

6. **Test reward hacking vulnerability.** Generate or identify model outputs that:
   - Score highly according to the reward model but are nonsensical or undesirable (e.g., repetitive, off-topic but polite).
   - Score low according to the reward model but are actually good (e.g., honest disagreement, refusal to answer unsafe prompts).
   
   If you find >5% of outputs in either category, the reward model has decoupled from the intended behavior.

7. **Check for dataset leakage.** Compare outputs that the reward model was trained on to outputs it ranks. Are outputs visually or structurally identical to training data? If yes, the reward model has memorized rather than generalized.

### Phase 3 — Training Loop Inspection

8. **Trace the objective being optimized.** For RLHF:
   - Is the KL penalty (divergence from the base model) actually being applied? If the coefficient is too small relative to reward gain, the model will diverge into reward hacking.
   - Is the base model frozen or fine-tuned during RL? Freezing constrains drift; fine-tuning allows more optimization but risks forgetting prior knowledge.
   
   For DPO:
   - Does the loss function correctly weight preference pairs by margin? (DPO loses quality if margins are uniform.)
   - Is the reference model the true base model or a fine-tuned checkpoint? DPO is most stable when the reference matches the deployment baseline.

9. **Measure optimization progress.** Plot:
   - Training loss (should decrease monotonically or show expected convergence behavior).
   - Mean preferred output reward (should increase).
   - KL divergence from base model (should stay controlled, not explode).
   - Diversity of generated outputs (can be measured by embedding-based diversity or n-gram uniqueness). A sudden collapse in diversity often signals reward overfitting.

10. **Run a held-out preference test.** Take 5–10% of the preference dataset reserved from training. Evaluate whether the trained model's outputs score higher on the held-out pairs according to an independent scoring method (human re-annotation or a second reward model). If held-out preference is uncorrelated with training preference, the model learned noise.

### Phase 4 — Behavioral Audit

11. **Sample outputs from the trained model.** Generate 50–100 completions on diverse prompts (ideally from the deployment domain, not just the training domain). For each, rate:
    - Does it match the intended preference in the training data?
    - Does it exhibit unintended side effects (e.g., evasiveness, false certainty, style-over-substance)?
    - Does it refuse appropriately or refuse too much?
    
    If >20% of outputs surprise you (desirable behavior that training didn't target, or undesirable behavior that slipped through), the trained model has developed emergent properties disconnected from the training signal.

12. **Stress-test the trained model on adversarial or out-of-distribution prompts.** Does it:
    - Stick to its learned behavior or revert to base model behavior?
    - Exhibit brittle failures (e.g., extreme responses to small input perturbations)?
    - Generalize to related tasks it wasn't trained on?

## Evaluation Criteria

| Check | Pass |
|---|---|
| Preference dataset source, scale, and domain are explicitly documented | Y/N |
| Inter-rater agreement on preferences is quantified (or explicitly acknowledged as missing) | Y/N |
| At least 50 preference pairs were manually examined for reasons | Y/N |
| Annotation collapse status is assessed (strong vs. uniform distribution) | Y/N |
| Negative examples audited for quality (genuine vs. strawman) | Y/N |
| For RLHF: reward model diagnostics completed (probe, hacking test, leakage check) | Y/N |
| Training loop objectives and constraints traced and quantified | Y/N |
| Held-out preference test completed on reserved data | Y/N |
| Behavioral audit on 50+ diverse outputs completed | Y/N |
| Adversarial/OOD stress test completed | Y/N |

## Red Flags

- Inter-rater agreement is unknown or <0.5 (Fleiss' kappa). The preference signal is not reproducible; any model trained on it will learn noise.
- >80% annotation collapse but no attempt to understand why annotators agreed so strongly. Brittle models often emerge from such homogeneous signals.
- Reward model is never explicitly evaluated; it is assumed to work because training loss decreased. Reward models overfit and hack as easily as classifiers.
- The linear probe of the reward model explains >70% of variance. The model is learning trivial features (length, presence of keywords) rather than deep preference.
- KL penalty is so small (or absent) that the trained model's language diverges significantly from the base model without behavior improvement on held-out data.
- Diversity of outputs collapses during training but is attributed to "mode-seeking" without investigation. This often signals reward overfitting.
- Held-out preference test was not performed, or was performed but showed uncorrelated results. Training may have overfit the training-set preference pairs.
- >20% of sampled outputs contradict the intended training signal or exhibit unintended side effects without explanation.
- No adversarial or OOD testing. The trained model is never pressured; resilience is unknown.
- The framework (RLHF vs. DPO) was chosen for convenience rather than justification. Both have different failure modes and cost profiles.

## Output Format

```
## RLHF / DPO Assessment

**Framework:** [RLHF / DPO / hybrid]
**Base model:** <model name and size>
**Training data source:** <source description>

### Phase 1 — Preference Data Audit
- **Dataset scale:** <N pairs>
- **Annotator agreement (kappa or %):** <value or "unknown">
- **Domain match to deployment:** <good/partial/poor> — <reason>
- **Primary preference drivers identified:** <list>
- **Annotation quality verdict:** <strong/moderate/weak> — <justification>

### Phase 2 — Reward Model Diagnostics (RLHF only)
- **Linear probe explained variance:** <X%> — [indicates shallow / deep feature learning]
- **Reward hacking vulnerability:** <examples found or none>
- **Dataset leakage detected:** <yes/no — instances or none>
- **Reward model verdict:** <reliable / concerning / broken>

### Phase 3 — Training Loop
- **KL penalty strength:** <coefficient and observed divergence>
- **Training loss trajectory:** [monotonic / stable / erratic]
- **Mean preferred reward (training):** <trend>
- **Output diversity during training:** [maintained / collapsed]
- **Held-out preference correlation:** <correlation coefficient or N/A if not tested>
- **Training loop verdict:** [controlled / drifting / overfit]

### Phase 4 — Behavioral Audit
- **Desired behaviors observed:** <X% of sampled outputs>
- **Unintended side effects:** <list or none>
- **OOD stress test result:** [stable / degraded / failed]
- **Emergent properties:** <unexpected behaviors or none>

### Key Findings
1. <finding with confidence>
2. <finding with confidence>
3. ...

### Recommendations
1. <action with cost/benefit estimate>
2. ...

### Confidence
<high/medium/low> — <justification based on data completeness, agreement strength, and consistency of signals>
```
