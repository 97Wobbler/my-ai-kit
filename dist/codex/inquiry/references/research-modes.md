# Research Authority Modes

Authority, evidence sufficiency, and automatic recording are separate settings.
An autonomous project can demand strong confirmation; an advisory project can
accept exploratory evidence. B is the default; toy work may use C, while an
important intuition-sensitive project may prefer A.

| Mode | Strategy behavior |
|---|---|
| A | Present observations and alternatives; the user chooses strategy changes. |
| B | Record multiple draft paths automatically; the user adopts or pivots strategy. |
| C | Adopt or pivot paths and run the next experiment within explicitly approved bounds. |

Define scope, mutable/frozen surfaces, cumulative budget, topology, stop rules,
and material amendment triggers with the user or an existing approved contract.
No mode grants arbitrary external effects or permission to increase budgets.
Use one authority source for the execution: link `authority.experiment_contracts`
to existing approved program contracts, without copying or replacing them.

Separate strategy adoption, authorized experiment execution, and final adoption
of an incumbent/result. The existing `experiment` skill requires explicit
initial contract approval and final user candidate selection. Its program
envelope already permits internal candidate additions, repairs, and pivots.
C does not reduce to suggestions only, but it also does not silently change
that final-adoption contract. Amendments follow the existing contract.

Store the basis for human choices in `authorization_ref`, such as a workspace
message record or contract amendment. `actor: user` is recorded provenance, not
a cryptographic signature. Validation can catch conflicting labels; it cannot
prove that an actual user approved something. Reconcile assertions against the
conversation before execution. Do not mark the synthetic demo as actual approval.

A/B strategy changes require a user decision; proposals, factual results and
draft paths can be recorded without asking again. C strategy decisions may be
agent decisions inside scope. `final_adoption` always records a user actor under
the current contract. Changing modes or envelope limits is a user authority
decision, not an automatic fallback when a tool is unavailable.

At a recovery bound, stop automatic recovery. Then follow the chosen mode and
overall policy: seek user direction, pause with resume conditions, or end under
an approved overall stop. Ending for budget is not proof that no useful path exists.
