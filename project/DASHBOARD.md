# COMP 441 Quality Dashboard

**Snapshot:** 14 October 2026 — interim and group review required

| Required indicator | Current value | Evidence / status |
|---|---:|---|
| Statement and branch coverage | **64% statement / 37% branch** across two scoped files; model 60%/18%, date/time utility 79%/70% | Focused 66-test run only; not full suite or AI-only v1. Full/AI-only reports still required. |
| Mutation score | **Pending** | No defensible AI-only v1 or hybrid v2 score yet. Eight v1 survivor analyses remain required. |
| Project defect density | **0.50 defects/KLOC** (3 / 5.961) | Three temporal defects found/fixed during this project; group must review the defect count. |
| RTM completeness | **100% (14/14)** | All listed requirements have named passing test evidence in the RTM; confirm as group. |

## Coverage snapshot

```text
appointment/models.py          60% statements  | 18% branches
appointment/utils/date_time.py 79% statements  | 70% branches
```

The dashboard is intentionally interim: the rubric-required mutation measure is still missing, and coverage must be reported separately for AI-only and hybrid suites before final submission. Static complexity/maintainability and the Track C classifier are recorded separately in `STATIC_ANALYSIS.md` and `DEFECT_PREDICTION.md`.
