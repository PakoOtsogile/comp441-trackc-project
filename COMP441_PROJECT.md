# COMP 441 Track C Work

This repository preserves the upstream [`django-appointment`](https://github.com/adamspd/django-appointment) project and its Apache-2.0 license/history, with a small set of appointment-time correctness fixes and regression tests for the course project.

The evaluated scope is appointment scheduling and time validation. It is not a patient medical-record system and does not validate patient identity or medication data. The candidate’s technical qualification is documented, but course coordinator approval is still pending.

## Course project documents

- [Charter and scope](project/CHARTER.md)
- [Requirements traceability matrix](project/RTM.md)
- [TDD evidence log](project/TDD_LOG.md)
- [Integration test evidence](project/INTEGRATION_TESTS.md)
- [BDD feature and Django test counterparts](project/BDD/appointment-time.feature)
- [Metrics and evidence register](project/METRICS.md)
- [Defect prediction protocol](project/DEFECT_PREDICTION.md)
- [AI assistance disclosure](project/AI_PROMPT_LOG.md)

## Verified local status

On 14 October 2026, 66 focused existing/regression tests passed, and a separate run of three BDD scenario counterparts plus five selected integration tests passed (8 total). The full upstream suite contains 574 discovered tests but was stopped before completion in the local environment; it has not been verified as passing here. See the evidence files for limits and pending group/coordinator inputs.

## Group completion items

Add real member names and task assignments, obtain coordinator approval, complete the remaining rubric measurements and human evaluation with the required process, run the full CI suite, and replace pending values with reproducible results. Do not represent the pending entries as completed evidence.
