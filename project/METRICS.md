# Quality Metrics and Evidence Register

| Indicator | Baseline | Current | Method / evidence | State |
|---|---:|---:|---|---|
| Python source LOC | 5,961 | 5,961 | Counted under `appointment/` and `appointments/`; excluded tests and migrations | Measured at checkout; recount before report |
| Commits | 830 upstream | 832 total | `git rev-list --count HEAD`; 830 upstream commits at import + 2 course commits | Count captured 14 Oct 2026 |
| Focused tests | — | 66 passed | Django test runner, targeted models/validators/date-time modules | Passed 14 Oct 2026 |
| Gherkin acceptance scenarios | — | 3 passed | pytest 9.1.1 + pytest-bdd 9.0.0; `python -m pytest appointment/tests/bdd -q` | Passed 14 Oct 2026 |
| BDD scenarios + selected integration tests | — | 8 passed | Three scenario counterparts and five cases listed in `INTEGRATION_TESTS.md` | Passed 14 Oct 2026 |
| Full test suite | — | 580 run; 579 passed, 1 skipped | `USE_DJANGO_Q=true`; `manage.py test appointment.tests --parallel=10 --shuffle --verbosity=1`; seed 948697336; project-local `TMP`/`TEMP` | Passed 14 Oct 2026 in 401.789 seconds |
| Focused line/branch coverage | — | 64% statements, 37% branches (59% combined); model 60%/18%, date/time util 79%/70% | coverage.py 7.16.2 branch mode on 66 focused tests; details and caveat in `STATIC_ANALYSIS.md` | Measured 14 Oct 2026; not AI-only or full suite |
| Mutation score | — | 82.6% sampled (19 detected / 23 trials) | Mutatest 3.1.0, seed 441, 8 of 46 AST locations, 51 date/time unit tests; report in `MUTATION_ANALYSIS.md` | Interim sample only; AI-only v1/hybrid v2 and required eight v1 survivor analyses remain pending |
| Project defect density | 0 | 3 found / 5.961 KLOC = 0.50 defects/KLOC | Three reproducible temporal defects fixed during this project; count is local to this work, not historical project density | Provisional; group must confirm defect count |
| RTM completeness | — | 14/14 requirements have named test evidence (100%) | Count requirements in `RTM.md`; all evidence should be rechecked in CI | Draft; group review required |
| Static analysis | — | Pylint 315 findings; Radon mean CC grade A (2.0); maintainability index C/A | Pylint 4.1.3 and Radon 6.0.1 on changed source files | Baseline measured 14 Oct 2026; see triage |
| Classifier metrics | TBD | TBD | Use reviewed historical defect labels and time-based holdout; see `DEFECT_PREDICTION.md` | Pending; do not score unreviewed commit-keyword labels as ground truth |
| Performance | — | Helper micro-load: 20 threads, 120s, 12,826.47 calls/s; median 1.4764ms, p95 2.7411ms, 0 errors | `scripts/performance_check.py`; raw output `performance_run.json`; details and limits in `PERFORMANCE.md` | Helper-only; HTTP/database load evidence remains pending |
| Usability | TBD | TBD | Consent-based task protocol, participant count, completion/errors/time, anonymized | Pending; do not fabricate participants/results |

## Symbolic execution / path reasoning

For `get_ar_end_time`, identify branch conditions for valid start input, accepted duration type, negative versus nonnegative duration, and crossing midnight. Boundary values should include zero duration, a fractional minute, negative integer and timedelta, and a result crossing 23:59. The targeted tests cover a subset; a symbolic tool run and path-coverage claim are pending. For `AppointmentRequest.save`, reason over end-before-start, equal times, valid ordering, and any optional fields; test all branches required by the coordinator rubric.

## Performance and usability protocol to complete

Record the exact endpoint/function, data size, warm-up, repetitions, Python/Django/database versions, machine, median and p95 latency, and error rate. For usability, recruit only with course approval, use synthetic appointment data, record consent and tasks, and report participant count and anonymized outcomes. This repository provides no human-subject or performance results yet.
