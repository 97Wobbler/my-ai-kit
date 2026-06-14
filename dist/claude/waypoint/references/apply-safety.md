# Apply Safety

Read this reference before any `waypoint:audit` apply-mode edit.

## Preconditions

Apply only when all are true:

- the user explicitly requested edits;
- the dry-run finding or plan is specific enough to implement;
- target files are identified;
- the edit does not weaken safety, privacy, release, ownership, or test rules;
- unrelated user changes can be preserved.

If these are not true, stop and ask a concise question or return a narrower
dry-run plan.

## Edit Rules

- Preserve meaning before reducing length.
- Move content before deleting it.
- Summarize historical content only when the summary keeps the lesson or points
  to an archive.
- Update links and Document Map entries when moving sections.
- Keep `.waypoint/config.yaml` locator-only.
- Do not normalize a coherent brownfield documentation system just because it
  differs from Waypoint defaults.

## Validation

After edits, run:

```bash
python3 <waypoint-plugin-root>/scripts/waypoint_doctor.py --repo-root <target-repo>
python3 <waypoint-plugin-root>/scripts/waypoint_audit.py --repo-root <target-repo>
```

Report warnings honestly. A remaining warning may be acceptable when it reflects
intentional repository policy.
