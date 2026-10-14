# AI Assistance and Prompt Log

This log is an evidence template. It records the assistance used in this work and distinguishes generated suggestions from verified project results. The group should add entries for every tool/model actually used during its final project work.

| Date | Tool/model | Prompt or task | Output used | Human verification |
|---|---|---|---|---|
| 14 Oct 2026 | OpenAI Codex (model shown in task UI) | “help me complete this group project”; then requested a new public GitHub repository and working code/tests | Candidate research, repository modifications, regression tests, and draft project documentation | Focused 66-test run passed; group should review code, approve scope, and complete missing human evidence |
| 14 Oct 2026 | OpenAI Codex (model shown in task UI) | “complete the remaining work” | Seeded mutation sample and survivor triage; reproducible concurrent helper micro-load script and report; corrected coverage summary and regression rerun | 66 focused Django tests, 3 pytest-bdd scenarios, and 2-second runner smoke check passed; group review and HTTP/usability evidence remain outstanding |

## AI-only baseline comparison

**Status: not yet performed.** Do not report a model-vs-linter precision/recall comparison until a fixed prompt, version, file sample, defect labels, and reproducible scoring procedure have been recorded. A future entry should include:

- exact prompt and model/version/date;
- code sample and ground-truth defect set;
- static-analysis tool/version and configuration;
- matching rule for true/false positives and false negatives;
- raw findings and confusion matrix; and
- reviewer who adjudicated ambiguous findings.

Generated output was treated as a hypothesis. No generated suggestion is evidence until checked against repository source, tests, or an explicit measurement.
