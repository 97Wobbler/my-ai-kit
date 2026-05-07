# Resume Mode

Triggered when `.rumsfeld/` exists in or above `cwd` and the learner needs orientation, status, review, matrix updates, or a topic choice.

Resume mode reconstructs state. It does not teach until the learner explicitly confirms they want to study a topic now.

## Workflow

### 1. Read State

Read:

- `.rumsfeld/progress.yaml`
- `.rumsfeld/roadmap.yaml`
- `.rumsfeld/matrix.yaml`

Optionally read the most recent `.rumsfeld/notes/` file if `progress.yaml` references it as `notes_file`.

### 2. Brief The Learner

Present a tight 6-10 line status block:

- domain and current phase;
- sessions completed and last session date;
- last covered topic and previous `next_suggested`;
- suggested next topic;
- unanswered `questions_raised`;
- recent matrix transitions.

If the last session was months ago, acknowledge likely forgetting and offer a brief recap before any study session.

### 3. Offer Choices

Ask what the learner wants to do:

- continue with the suggested next topic, then hand off to session mode;
- pick another current-phase topic, then hand off to session mode;
- review the matrix or roadmap read-only, then stop;
- manually update the matrix, then offer whether to start a session.

Do not auto-start studying.

### 4. Handle Stale Or Contradictory State

If state files contradict each other, surface the inconsistency and ask before editing. Do not silently rewrite state.

## Anti-Patterns

- Dumping the full matrix as the orientation brief.
- Starting teaching without topic confirmation.
- Treating "공부하자" as permission to skip the state brief.
