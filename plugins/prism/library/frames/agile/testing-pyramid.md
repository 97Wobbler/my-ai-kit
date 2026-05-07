---
name: testing-pyramid
display_name: Testing Pyramid
class: frame
underlying_class: native
domain: agile
source: Mike Cohn, "Succeeding with Agile," Addison-Wesley, 2009
best_for:
  - Diagnosing test suite imbalance (too many slow tests, insufficient unit coverage, brittle end-to-end tests)
  - Planning a rebalancing strategy when the suite is inverted ("ice cream cone," "hourglass," or honeycomb-shaped)
  - Guiding test portfolio decisions for new projects or teams
one_liner: "Three test layers — many fast unit tests, fewer integration tests, few slow end-to-end tests."
---

# Testing Pyramid

## Overview

The Testing Pyramid describes a three-layer model for organizing test effort by execution speed, scope, and cost. The ideal shape—many unit tests at the base, fewer integration tests in the middle, and a small number of end-to-end tests at the top—reflects the tradeoff between test breadth and test speed. Systems that violate this shape (too many slow tests, insufficient unit coverage) suffer from slow CI pipelines, brittle test suites, and low defect-detection confidence. The pyramid guides teams to distribute testing effort efficiently: catch bugs quickly with unit tests, validate component boundaries with integration tests, and use end-to-end tests sparingly for critical paths.

## Categories

1. **Unit Tests (Base layer — many, fast, cheap)**
   - **Scope**: Single function, class, or component in isolation. Dependencies are mocked or stubbed.
   - **Execution speed**: Milliseconds. Thousands can run in < 1 second.
   - **Failure isolation**: Pinpoints exact code location (function/line).
   - **Maintenance cost**: Low (brittle only if overusing mocks or if the API changes frequently).
   - **Discriminating criterion**: The test exercises one unit of logic without touching the network, filesystem, or database. Example: a function that computes tax given an income; the function is called with various incomes and assertions check the returned tax value. No external I/O.
   - **Example tests**:
     - `test_discount_calculation()` — calls a pricing function, asserts the discount.
     - `test_user_creation_validation()` — creates a user object with invalid input, asserts an exception.

2. **Integration / Service Tests (Middle layer — fewer, slower, medium cost)**
   - **Scope**: Multiple components interacting (e.g., API handler + database adapter, service A calling service B). Focused on boundaries and contracts.
   - **Execution speed**: Seconds (0.5–10 seconds per test). Hundreds run in a minute.
   - **Failure isolation**: Points to the component boundary or the contract between components, but not to a specific line.
   - **Maintenance cost**: Medium (database state setup, test data, teardown; services must be available or mocked consistently).
   - **Discriminating criterion**: The test exercises the interaction between two or more components, but not the full system. Example: an API endpoint that reads from a database is tested end-to-end through the HTTP API but using a test database, not the production system.
   - **Example tests**:
     - `test_api_get_user_from_db()` — calls the API with a user ID, the API queries a test database, asserts the response.
     - `test_service_a_calls_service_b()` — service A calls service B (mocked or test instance), asserts the correct RPC was made.
     - `test_order_checkout_flow()` — checkout endpoint + payment processor + inventory system (all test instances); asserts the order is created and inventory is decremented.

3. **End-to-End / UI Tests (Top layer — few, slow, brittle, expensive)**
   - **Scope**: Full system, including UI, backend, database, external services. From user input to final state.
   - **Execution speed**: Seconds to minutes (5–120 seconds per test). Dozens run in 5–10 minutes.
   - **Failure isolation**: Low (a failure could be in any component; debugging requires replaying the entire sequence).
   - **Maintenance cost**: High (brittle due to timing, UI changes, external dependencies; require real environment or complex orchestration).
   - **Discriminating criterion**: The test interacts with the system as an end user would (via UI, browser, API client) and verifies the full state change. Example: a user logs in via browser, uploads a file, the file appears in their dashboard — all verified through the UI.
   - **Example tests**:
     - `test_user_signup_flow()` — open browser, fill signup form, submit, assert logged-in state visible.
     - `test_checkout_process()` — add items to cart, proceed to checkout, enter payment info, assert order confirmation page.
     - `test_api_integration()` — call the public API with a real client, assert the response and system state; no mocking.

## Classification Procedure

For any given test, classify it by answering these questions in order:

1. **What does it actually exercise?**
   - Single function/class in isolation? → **Unit test**.
   - Multiple components interacting, but not the full user journey? → **Integration / service test**.
   - Full system from user input to end state, including UI and backend? → **End-to-end test**.

2. **Does it depend on external I/O?**
   - No (dependencies mocked, no I/O)? → Unit test.
   - Yes, but test-scoped (test database, mock services)? → Integration test.
   - Yes, using production or production-like environment? → End-to-end test.

3. **How fast does it run?**
   - < 100ms? → Unit test.
   - 100ms–10 seconds? → Integration test.
   - > 10 seconds? → End-to-end test (or integration test that needs optimization).

4. **How precisely can you locate a failure?**
   - Points to a specific function? → Unit test.
   - Points to a component or contract? → Integration test.
   - Requires debugging the entire flow? → End-to-end test.

**Then, ratio-check your entire suite:**
- Heuristic target: ~70% unit tests, ~20% integration tests, ~10% end-to-end tests (by count, not execution time).
- Example: 700 unit tests, 200 integration tests, 100 end-to-end tests ≈ 1000 total.
- Treat this heuristic as a starting point, not gospel; the right ratio depends on your product (see implications below).

## Implications per Category

| Layer | Purpose | What to do | What to avoid |
|---|---|---|---|
| **Unit** | Fast, cheap defect detection; enable refactoring | Write many; keep them focused on single responsibility; use mocks liberally for I/O; run on every commit | Over-test implementation details; test through the UI; mock away the logic you're trying to test |
| **Integration** | Validate component contracts and boundaries; catch integration bugs | Test the actual contract between components; use test doubles (real test DB, stubbed external services); group tests by boundary | Skip these and rely on unit tests alone; test implementation details (how components call each other internally); wait for E2E to catch contract bugs |
| **End-to-end** | Validate user journeys and critical business flows; catch environment issues | Test high-value, high-failure-risk paths (checkout, signup, payment); use actual or production-like environment; automate sparingly | Test every user interaction; run E2E tests on every commit; test unimportant flows; over-invest in brittle UI tests when integration tests would suffice |

## Common Misclassifications

1. **Tests labeled "unit" that actually touch the database or network.** 
   - **Tell**: The test is slow, requires test data setup, or fails if the database is down.
   - **Root cause**: Developers call this a "unit test" because it tests one function, but that function depends on real I/O.
   - **Fix**: Either mock the database (true unit test) or reclassify as integration test.

2. **Inverting the pyramid: "ice-cream cone" shape.**
   - **Tell**: Lots of E2E tests, almost no unit tests, few integration tests. CI is slow.
   - **Root cause**: Early projects often ship E2E tests because they're the easiest to write (just click around). When bugs appear in refactoring, there are no unit tests to catch them early.
   - **Fix**: Invest in unit and integration test infrastructure; retire redundant E2E tests.

3. **Hourglass shape.**
   - **Tell**: Many unit tests, many E2E tests, very few integration tests.
   - **Root cause**: Unit tests are easy to write, E2E tests provide user confidence. Integration tests are harder to set up and less obvious why they're needed.
   - **Fix**: Add integration tests at component boundaries; use them to catch contract bugs before E2E.

4. **Brittle integration and E2E tests due to fakes/mocks confusion.**
   - **Tell**: Integration tests pass in isolation but fail in CI due to test data inconsistency or timing.
   - **Root cause**: Using mocks (behavior doubles) for integration tests instead of fakes (stateful doubles). Mocks are fine for unit tests; fakes (test database, in-memory service) are better for integration.
   - **Fix**: Use real test doubles (test databases, test API servers) for integration tests, not mock objects.

5. **Using E2E tests to compensate for missing unit coverage.**
   - **Tell**: No unit tests for business logic; heavy reliance on E2E to catch bugs.
   - **Root cause**: Team assumes "if the E2E passes, the code is correct."
   - **Fix**: Add unit tests for logic; use E2E only for critical user flows.

## Modern Alternatives and Critiques

**Honeycomb / Hexagon Testing (2021).** 
- Advocates moving away from the pyramid toward a **honeycomb** shape: many integration-level tests, fewer unit tests (only for complex logic), even fewer E2E tests.
- Rationale: Modern systems are highly decoupled (microservices, serverless); component integration is the primary failure mode, not individual function bugs.
- **Trade-off**: Honeycomb works well for backend microservices but less so for frontend (where UI integration is more critical).

**Trophy Testing (Kent C. Dodds, 2019).**
- Proposes that frontend testing should be **inverted**: many integration tests (component + DOM), fewer unit tests (too isolated, don't catch real issues), minimal E2E tests (slow, brittle).
- Rationale: Frontend components are tightly coupled with the DOM; mocking the DOM in unit tests defeats the purpose.
- **Implication**: For frontend, the pyramid is less applicable; integration-level testing of components + user events is more effective.

**Dynamic shape based on domain.**
- Backend services: pyramid (many units, some integration, few E2E).
- Frontend: hexagon/honeycomb (many integration/component tests, minimal units and E2E).
- Distributed systems: honeycomb (integration tests are the primary defense against failure).
- Real recommendation: **Understand the failure modes of your system and invest in the layer most likely to catch them early.**

## Output Format

```
## Testing Suite Analysis: <system or component>

**Current test distribution (by count):**
| Layer | Count | % of suite | Target % | Ratio status |
|---|---|---|---|---|
| Unit | X | X% | 70% | ✓ Aligned / ✗ Deficient / ⚠ Excess |
| Integration | Y | Y% | 20% | ... |
| End-to-end | Z | Z% | 10% | ... |
| **Total** | **X+Y+Z** | **100%** | **100%** | ... |

**Execution time profile:**
| Layer | Avg test time (ms) | Total time for layer (s) | % of total CI time |
|---|---|---|---|---|
| Unit | X | Y | Z% |
| Integration | X | Y | Z% |
| E2E | X | Y | Z% |

**Suite shape assessment:**
- Current shape: pyramid | hourglass | ice-cream cone | honeycomb | other
- Alignment: ✓ Healthy | ⚠ Needs rebalancing | ✗ Inverted/broken
- Key imbalance: <what layer is over/under-represented>

**Misclassification audit:**
- Tests mislabeled as unit but touch I/O: <list 1–3 examples>
- Tests mislabeled as integration but are actually unit: <list>
- Tests mislabeled as E2E but are actually integration: <list>
- **Reclassification impact**: Correcting mislabels shifts distribution to <target>

**Recommendations:**
1. **Priority 1**: <specific layer or test to add/remove>
   - Rationale: <risk, speed, or coverage gap>
   - Effort: <person-days>
   - Timeline: <by which sprint>

2. **Priority 2**: ...

3. **Priority 3**: ...

**Monitoring metrics:**
- Unit test execution time: <current> (target: < 30s)
- Integration test execution time: <current> (target: < 2m)
- E2E test execution time: <current> (target: < 5m)
- CI feedback latency: <current> (target: < 10m for full suite)
- Defect escape rate (caught by which layer): <percentage caught by units / integration / E2E>

**Confidence: high | medium | low**
<reasoning: accuracy of test classification, stability of test execution, team expertise in test design, applicability of pyramid model to your domain>
```
