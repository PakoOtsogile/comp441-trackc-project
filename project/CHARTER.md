# COMP 441 Track C Project Charter

**Status:** working draft for group review  
**Prepared:** 14 October 2026  
**Candidate:** [`adamspd/django-appointment`](https://github.com/adamspd/django-appointment)  
**Course project repository:** [PakoOtsogile/comp441-trackc-project](https://github.com/PakoOtsogile/comp441-trackc-project) (public)

## Purpose and approval

This project evaluates and improves an existing Python/Django appointment scheduler. The candidate is a Django application for appointment requests, staff availability, booking, and related notifications. It is suitable for a scheduling-validation study; it does **not** provide a patient medical-record system, and this project will not claim to validate patient identifiers, dates of birth, diagnoses, or medication dosages.

The upstream project is Apache-2.0 licensed and has a substantial public commit history. A local source count of 5,961 Python lines was measured across `appointment/` and `appointments/`, excluding tests and migrations. These are local measured values, not coordinator approval. **The course coordinator must still approve the candidate and the scope before the group treats it as final.**

## Problem and objectives

Appointment scheduling accepts dates, times, durations, availability rules, and appointment requests. Invalid temporal combinations can otherwise fail late or be represented inconsistently. The engineering objective is to make temporal validation predictable and to demonstrate the result with tests and traceable requirements.

Objectives:

1. Reproduce and fix at least three defects using test-driven development.
2. Add automated scenario-level and integration evidence for scheduling behavior.
3. Measure static-analysis, test, mutation, and performance indicators without inventing results.
4. Produce a reproducible report and retain evidence for group review.

## Scope

**In scope:** appointment-request start/end ordering; time-duration conversion including negative and fractional durations; existing booking/availability rules; relevant UI/service flows; quality evidence for these behaviors.

**Out of scope:** clinical records, medical advice, patient identity verification, medication/dosage validation, production deployment, and changes unrelated to appointment scheduling correctness.

## Stakeholders and responsibilities

| Role | Owner | Responsibility |
|---|---|---|
| Course coordinator | TBD | Approve candidate and scope; clarify rubric interpretation |
| Group lead / repository maintainer | TBD | Schedule, integrate work, maintain evidence |
| Test and quality lead | TBD | TDD log, requirements traceability, metrics |
| UX / performance lead | TBD | Session plan, performance protocol and results |
| Group members | TBD | Review, implement, test, and document assigned work |

Replace every TBD with the group’s real names and agreed assignments. Do not infer contributions from commit authorship alone.

## Deliverables and acceptance checks

| Deliverable | Acceptance check | State |
|---|---|---|
| Candidate qualification | License, size, history, scope, coordinator decision recorded | Technical checks recorded; coordinator decision pending |
| TDD changes | Three defects have failing-before/fixed-after evidence | 3 regressions implemented; focused suite passes |
| Requirements traceability | At least 10 requirements map to code and verification | Draft in `RTM.md` |
| BDD scenarios | At least 3 Gherkin scenarios run with pytest-bdd in CI | Implemented; local run: 3 passed; hosted run and coordinator/group review pending |
| Integration tests | At least 5 tests identified and executed | 5 named Django integration tests passed in the recorded 8-test run; confirm rubric fit |
| Quality metrics | Baseline and final values, tools, dates, caveats | Focused coverage and static-analysis baseline measured; mutation and other required metrics pending |
| Final report and presentation | Rubric sections, evidence, references, AI disclosure | Pending group/coordinator inputs |

## One-page test plan summary

See [`TEST_PLAN.md`](TEST_PLAN.md) for scope, objectives, approach, roles to be assigned, schedule, entry/exit criteria, rated risks, and three-point estimates. Role owners are intentionally left for the group to confirm.

## Risks

| Risk | Probability | Impact | Response |
|---|---|---|---|
| Coordinator rejects candidate/scope | Medium | High | Request written approval; retain selection evidence and adjust only with coordinator direction. |
| Project scope is interpreted as clinical data validation | Medium | High | State appointment-scheduling boundaries; get approval that this clinic/appointment candidate meets Track C. |
| Upstream behavior differs from assumptions | Medium | Medium | Use source/tests as oracle and record observed behavior. |
| Full suite exceeds local time/resources | Medium | Medium | Use focused local runs and hosted CI matrix for full verification. |
| Metrics are mistaken for clinical validation | Low | High | State scheduling-only scope in every report/demo; use synthetic data only. |
| Human evaluation lacks consent or consistent procedure | Medium | High | Obtain course approval, use consent and synthetic data, and collect no identifiable health data. |
| Group/member contribution records are incomplete | Medium | High | Assign owners and keep checkpoint records; do not infer contributions. |

## Schedule (proposed; confirm against course calendar)

| Week | Planned work |
|---|---|
| 8 (current) | Candidate approval, charter, baseline and test plan |
| 9 | TDD and scenario/integration coverage |
| 10 | Mutation, static analysis, classifier and performance measurements |
| 11 | Human evaluation, analysis, final report and presentation rehearsal |
| 12 | Submit final report (brief indicates 10 November) |
| 13 | Present (brief indicates 17 November) |

Dates and week labels must be checked against the course LMS and coordinator announcements.
