# COMP 441 Track C — Interim Report Draft

**Draft status:** engineering work and targeted evidence recorded; not a final submission. Replace all `TBD` items with group-verified evidence and review against the full assignment brief before submission.

## 1. Executive summary

The group selected `adamspd/django-appointment`, a Python/Django appointment scheduling application. This project focuses on temporal validation around appointment requests and duration conversion. Three test-driven fixes were implemented: reversed request intervals now raise a model validation error; negative `timedelta` durations are rejected; and fractional numeric durations preserve seconds. The focused regression run passed 66 tests, and a separate run of three scenario tests and five selected integration tests passed 8 tests. The complete upstream suite has not yet been verified in this environment.

The candidate technical checks recorded here are an Apache-2.0 license, 5,961 Python source lines under the selected package directories (excluding tests/migrations), and 830 commits at the checkout point. Course coordinator approval remains pending. The candidate handles appointments and scheduling; it is not a patient-records or medication-validation system.

## 2. Project background and candidate qualification

### Candidate

- Name and source: [`django-appointment`](https://github.com/adamspd/django-appointment)
- Language/framework: Python and Django
- License: Apache License 2.0 (verify current license at final submission)
- Size/history snapshot: 5,961 non-test/non-migration Python lines in `appointment/` and `appointments/`; 830 commits at the local checkout
- Approval: **TBD — coordinator decision required**

### Problem statement

Incorrect appointment start/end ordering and duration handling can produce invalid or imprecise schedule data. The project improves the validation boundary and tests representative temporal cases. Scope is limited to appointment scheduling and related validation.

## 3. Requirements and design

The traceability matrix is in [`RTM.md`](RTM.md). Requirements include valid start/end ordering, accepted time/duration types, rejection of negative durations, preservation of fractional minutes, midnight wrapping, availability, authorization, and HTTP submission behavior.

The changes are intentionally narrow: validation stays in the appointment model; duration normalization and arithmetic stay in the existing date/time utility. No schema migration was required. Detailed design/architecture figure: **TBD — add a diagram based on verified source modules and data flow.**

## 4. Test-driven development and verification

See [`TDD_LOG.md`](TDD_LOG.md) for red/green evidence. The focused run on 14 October 2026 passed 66 tests in 61.522 seconds. A separate run of three Django tests corresponding to the Gherkin feature and five integration tests passed 8 tests in 79.008 seconds. Python syntax compilation and `git diff --check` also completed without reported errors.

The upstream workflow runs a broader test matrix. The local full suite discovered 574 tests but was stopped before completion due to slow execution. Therefore full-suite status is **unverified**, not passing. Coverage, mutation score, static-analysis findings, and symbolic execution are **TBD**; populate with tool/version, exact run, counts, and relevant output. If the rubric requires at least eight surviving mutants, list and justify each one with source/test references rather than inventing survivors.

## 5. Behavior-driven and integration evidence

Three appointment-time Gherkin scenarios and executable Django test counterparts are in `BDD/appointment-time.feature` and `appointment/tests/test_trackc_bdd_scenarios.py`. The project uses Django's test runner rather than a Gherkin parser; obtain coordinator confirmation that this format satisfies the rubric, or integrate a BDD runner if required.

Five selected integration cases and their descriptions are listed in [`INTEGRATION_TESTS.md`](INTEGRATION_TESTS.md). All five were included in the 8-test run and passed.

## 6. Defect prediction and analysis

The proposed model uses change churn features and human-reviewed historical defect labels, with chronological holdout and a majority baseline. The executable script is `scripts/defect_prediction.py`; no reviewed label file or model result exists yet. Do not report performance metrics until label review, evaluation, and version capture are complete. Compare AI findings and static analysis only after recording the same code sample, independent ground truth, adjudication rules, and tool versions in [`AI_PROMPT_LOG.md`](AI_PROMPT_LOG.md).

## 7. Performance and usability

**TBD.** Record an agreed endpoint, machine/runtime/database configuration, dataset size, warm-up, repetitions, median/p95 latency and errors. For usability, follow course approval/consent requirements and use synthetic appointment data. Record participant count and anonymized task outcomes. No human-study or performance values have been collected for this draft.

## 8. CI and quality gates

The existing upstream GitHub Actions workflow installs supported Django/Python combinations and runs `appointment.tests`. Preserve the workflow and confirm the fork’s default branch triggers it. Add any extra required gates (coverage threshold, mutation gate, linter) only after their configurations are fixed and results reproducible. CI evidence for this fork: **TBD after publication and workflow run**.

## 9. Team contributions and reflection

**TBD — group members must supply their names, assigned work, review contributions, and peer evaluation.** The AI assistance log records this assistant's role; generated content is not a substitute for human contribution records. Discuss limitations, coordination issues, lessons learned, and next steps using real group experience.

## 10. Conclusion

Three temporal-validation defects have reproducible regression tests and the focused verification runs passed. The project has a traceable starting point and a measured but limited evidence set. It is not ready to present as a complete final report until coordinator approval, complete CI, rubric-required quality metrics, performance/usability evidence, and authentic group contribution records have been added.

## References

1. `adamspd/django-appointment`, GitHub repository and `LICENSE` (access date: TBD at final submission).
2. COMP 441 Group Project assignment brief, attached PDF (add required citation format/page numbers).
3. Framework/tool documentation used during evaluation (record URLs and access dates for every final claim).
