# COMP 441 Track C Work

This public course repository preserves the upstream [`django-appointment`](https://github.com/adamspd/django-appointment) project and its Apache-2.0 license/history, with appointment-time fixes, regression tests, and Track C project evidence. The course repository is [PakoOtsogile/comp441-trackc-project](https://github.com/PakoOtsogile/comp441-trackc-project).

The evaluated scope is appointment scheduling and time validation. It is not a patient medical-record system and does not validate patient identity or medication data. The candidate’s technical qualification is documented, but course coordinator approval is still pending.

## Course project documents

- [Charter and scope](project/CHARTER.md)
- [Interim final-report draft](project/FINAL_REPORT_DRAFT.md)
- [Requirements traceability matrix](project/RTM.md)
- [TDD evidence log](project/TDD_LOG.md)
- [Static analysis report](project/STATIC_ANALYSIS.md)
- [One-page test plan](project/TEST_PLAN.md)
- [Current quality dashboard](project/DASHBOARD.md)
- [Risk-based test order](project/TEST_PRIORITIZATION.md)
- [Peer-evaluation template](project/PEER_EVALUATION_TEMPLATE.md)
- [Integration test evidence](project/INTEGRATION_TESTS.md)
- [BDD feature](project/BDD/appointment-time.feature) and [pytest-bdd step tests](appointment/tests/bdd/test_appointment_time.py)
- [Metrics and evidence register](project/METRICS.md)
- [Defect prediction protocol](project/DEFECT_PREDICTION.md)
- [AI assistance disclosure](project/AI_PROMPT_LOG.md)

## Verified local status

On 14 October 2026, 66 focused tests passed; 3 real pytest-bdd Gherkin scenarios passed; 5 selected integration tests passed in a separate 8-test run; and the CI-style Django suite passed all 580 discovered tests with one environment-conditional skip. The full run used ten workers, shuffle seed 948697336, Django-Q enabled, and a project-local temporary directory. Coverage was 59% across `appointment/models.py` and `appointment/utils/date_time.py` for the 66-test focused run only (54% and 76%, respectively); it is not the whole-repository or AI-only coverage result required by the brief.

## Group completion items

The code and local verification are in place. Remaining items that require group decisions or people are listed in the charter and interim report: candidate/scope sign-off, AI-only and hybrid mutation runs with eight v1 survivor analyses, reviewed defect labels and classifier, exploratory co-pilot session, performance load check, usability heuristic review, member roles/contribution and peer evaluation, final report/declaration, and live CI/demo evidence. Do not present pending entries as completed evidence.
