# Quality Metrics and Evidence Register

| Indicator | Baseline | Current | Method / evidence | State |
|---|---:|---:|---|---|
| Python source LOC | 5,961 | — | Counted under `appointment/` and `appointments/`; excluded tests and migrations | Measured once; recount before report |
| Upstream commits | 830 | — | `git rev-list --count HEAD` at checkout | Measured at checkout; history continues upstream |
| Focused tests | — | 66 passed | Django test runner, targeted models/validators/date-time modules | Passed 14 Oct 2026 |
| BDD scenarios + selected integration tests | — | 8 passed | Three scenario counterparts and five cases listed in `INTEGRATION_TESTS.md` | Passed 14 Oct 2026 |
| Full test suite | — | Not established | Upstream CI runs full `appointment.tests` matrix | Local run stopped early; not passed |
| Line/branch coverage | TBD | TBD | Run coverage on the full suite; record tool/config and exact command | Pending |
| Mutation score | TBD | TBD | Run rubric-required mutator; count killed/live/equivalent/timeout separately | Pending; Windows support needs validation |
| Static-analysis findings | TBD | TBD | Record tool/version/config and severity counts; adjudicate findings | Pending |
| Classifier metrics | TBD | TBD | Use reviewed historical defect labels and time-based holdout; see `DEFECT_PREDICTION.md` | Pending |
| Performance | TBD | TBD | Controlled dataset, repetitions, median/p95, machine/runtime metadata | Pending |
| Usability | TBD | TBD | Consent-based task protocol, participant count, completion/errors/time, anonymized | Pending; do not fabricate participants/results |

## Symbolic execution / path reasoning

For `get_ar_end_time`, identify branch conditions for valid start input, accepted duration type, negative versus nonnegative duration, and crossing midnight. Boundary values should include zero duration, a fractional minute, negative integer and timedelta, and a result crossing 23:59. The targeted tests cover a subset; a symbolic tool run and path-coverage claim are pending. For `AppointmentRequest.save`, reason over end-before-start, equal times, valid ordering, and any optional fields; test all branches required by the coordinator rubric.

## Performance and usability protocol to complete

Record the exact endpoint/function, data size, warm-up, repetitions, Python/Django/database versions, machine, median and p95 latency, and error rate. For usability, recruit only with course approval, use synthetic appointment data, record consent and tasks, and report participant count and anonymized outcomes. This repository provides no human-subject or performance results yet.
