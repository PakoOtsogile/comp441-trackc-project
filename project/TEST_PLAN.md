# COMP 441 Test Plan

**Project:** Track C clinic appointment scheduling validation
**Repository:** [PakoOtsogile/comp441-trackc-project](https://github.com/PakoOtsogile/comp441-trackc-project)
**Version/date:** working plan, 14 October 2026
**Status:** group review and coordinator approval required

## Scope and objectives

Test the upstream Django appointment scheduler's request-time ordering, duration conversion, availability, booking request, and authorization behavior. Improve confidence through unit, integration, and Gherkin acceptance tests, then compare AI-only and human-augmented tests. Use synthetic scheduling data. Clinical records, patient identifiers, diagnoses, and medication rules are outside this candidate's implemented scope.

Objectives: preserve valid appointment behavior; reject invalid intervals and negative durations; retain fractional-minute precision; measure coverage, mutation sensitivity, static-analysis findings, and the Track C defect-prediction experiment; keep CI evidence reproducible.

## Method and resources

Use Django `TestCase`/`SimpleTestCase` for existing and regression unit/integration tests; pytest-bdd for Gherkin scenarios; Django's test database for integration tests; coverage.py for statement/branch coverage; mutmut (or a coordinator-approved Python mutator) for AI-only v1 and hybrid v2; Pylint and Radon for static baseline; scikit-learn on reviewed commit labels for Track C. All generated tests/findings require group review. Never put real health or personal data in fixtures.

## Schedule and owners

| Work | Target | Owner |
|---|---|---|
| Approve candidate and charter | Before next checkpoint | Group lead (name TBD) |
| Review prompts and produce AI-only baseline | Week 6/7 checkpoint | AI test lead (name TBD) |
| Mutation v1, survivor analysis, manual tests, TDD/BDD | Weeks 7-9 | Test lead + members (names TBD) |
| Static, symbolic, classifier, metric dashboard | Week 10 checkpoint | Track C lead (name TBD) |
| Exploratory, performance, usability evidence | Weeks 9-11 | Assigned members (names TBD) |
| Hybrid mutation v2, report, declaration, peer forms | Before 10 Nov 2026 | All members |
| Live CI/CD demo | 17 Nov 2026 | CI lead (name TBD) |

## Entry and exit criteria

**Entry:** coordinator approves the candidate/scope; team agrees owners and schedule; upstream license/history and checked-in test baseline are recorded; all test data are synthetic.

**Exit:** unit, integration, and BDD tests run in CI; AI-only and hybrid coverage/mutation reports are reproducible; at least eight v1 surviving mutants have reviewed explanations and corresponding manual tests; RTM has at least ten sourced requirements and states any gap; static and symbolic analysis, Track C classifier, exploratory session, performance check, usability evaluation, and four required quality indicators have evidence; report and AI declaration are reviewed and signed by the group; peer forms are submitted through the required confidential channel.

## Risk register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Coordinator rejects candidate/scope | Medium | High | Seek written approval early; retain qualification evidence and be ready to adjust. |
| No defensible defect labels for classifier | High | High | Review candidate commits against issue/PR evidence; report proxy-label uncertainty; do not claim predictive validity without reliable labels. |
| Mutation run exceeds available time or Windows support | High | Medium | Smoke-test the mutator; restrict it to changed scheduling modules; use hosted Linux CI if needed. |
| AI-generated tests assert weak properties | Medium | High | Review every assertion, compare exact outcomes, and record tests rewritten or rejected. |
| Human session uses identifiable or unapproved data | Low | High | Obtain course approval/consent; use synthetic data; collect no clinical/personal identifiers. |
| Team evidence is late or contribution records are incomplete | Medium | High | Assign real owners and weekly checkpoints; maintain records and peer forms individually. |

## Effort estimate (three-point PERT)

Initial planning estimate for the mutation and hybrid-suite phases: optimistic 6 hours, most likely 12 hours, pessimistic 24 hours. PERT estimate = `(6 + 4×12 + 24) / 6 = 13 hours`. This is a planning estimate for the group, not measured effort. Re-estimate after the mutator smoke run and record actual hours at completion.
