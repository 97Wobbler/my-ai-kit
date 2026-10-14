# Finite Path Recovery

Recovery is an ordering for searching useful candidates, not a command to keep
obsolete milestones. Whole-goal usefulness outranks preserving the first plan.

1. Find a relevant alternative that rejoins the next existing milestone.
2. Revise some milestones while preserving the user/product goal.
3. Reconsider the upper strategic decision that adopted the failed premise
   within this selected path. Do not follow arbitrary graph parents, evidence
   links or another goal's ancestry.
4. Stop automatic recovery at its bounds; record failed/unexamined alternatives.

The initial operating policy permits two upper backtracks in a continuous
recovery episode and stops before a third. Also set a finite attempt/time/cost
bound for local alternatives: limiting depth alone can leave endless A-primes.
Record reviewed points as well as the count, attempts and cumulative expense.

```sh
python3 <package-root>/scripts/research_store.py backtrack /workspace/research.json --episode recovery-a --point strategic-decision-id --decision new-review-id --expected-revision 4
```

This command records a review of a chosen decision; it does not adopt/pivot a
strategy or run an experiment. The main agent verifies that the chosen decision
really adopted the failed premise in this path. The tool only checks ID validity.
At the count/attempt/overall-budget bound it appends a `hold` decision and marks
the episode stopped without performing a third backtrack. It cannot invent a
parent or increase limits. A stopped episode cannot be continued by that command.

Record attempted alternatives and costs by revision-aware proposals. Never
reset an existing episode for a rename, new session, or another A-prime. A
meaningful milestone arrival or premise-changing evidence can justify a new
episode: preserve the old one, reference it with `prior_episode_id`, link
`reset_evidence_refs`, and set `reset_decision_id` to a new review/advance/pivot
decision that cites those references and records who judged the change meaningful. New evidence
does not automatically grant a reset. Whole-program spent remains cumulative.

The same failed premise and original adoption decision form one episode chain,
even if the path ID changes. Close the prior episode before continuing it; link
the latest episode rather than forking parallel resets. Existing reset provenance
and reviewed upper points are preserved; append points instead of erasing/reordering.
The tool enforces these links, monotonic counters and evidence/decision references,
but cannot decide if the recorded change is scientifically sufficient.
Purpose review checks this boundary. Do not relabel the same failed premise as
a new independent episode to bypass the continuous recovery count.

At a bound, distinguish automatic recovery stop, pause/resume conditions, and
whole-program termination. Follow A/B/C and the approved overall rule afterward.
Budget exhaustion or user stop can end the investigation with useful alternatives
still untested. For whole-investigation futility, perform the existing bounded
alternative-path review; never claim global refutation just because this path
or recovery budget was exhausted.
