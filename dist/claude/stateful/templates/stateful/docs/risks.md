# Risks

Updated: 2026-04-27

| Risk | Impact | Mitigation |
|---|---|---|
| Workplan remains generic after install | Future sessions cannot infer next useful work | Replace `R001` with repo-specific tasks before relying on autorun |
| State files drift from actual git history | Agents may resume from stale assumptions | Run `validate-workplan.py`, `sync-state.py`, and check `git log` |
