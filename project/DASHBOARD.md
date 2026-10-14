# COMP 441 Quality Dashboard

**Snapshot:** 14 October 2026 — interim and group review required

| Required indicator | Current value | Evidence / status |
|---|---:|---|
| Statement and branch coverage | **64% statement / 37% branch** across two scoped files; model 60%/18%, date/time utility 79%/70% | Focused 66-test run only; not full suite or AI-only v1. Full/AI-only reports still required. |
| Mutation score | **82.6% sampled (19/23)** | Seeded 8-location sample on the date/time utility; whole existing unit suite, not separated AI-only v1/hybrid v2. Four survivor reviews are in `MUTATION_ANALYSIS.md`; required v1/v2 comparison and eight v1 survivor case studies remain outstanding. |
| Project defect density | **0.50 defects/KLOC** (3 / 5.961) | Three temporal defects found/fixed during this project; group must review the defect count. |
| RTM completeness | **100% (14/14)** | All listed requirements have named passing test evidence in the RTM; confirm as group. |

## Coverage snapshot

```text
appointment/models.py          60% statements  | 18% branches
appointment/utils/date_time.py 79% statements  | 70% branches
```

The dashboard is intentionally interim: the required AI-only versus hybrid mutation measures and suite-specific coverage are still missing. The 82.6% value is only the sampled score described in `MUTATION_ANALYSIS.md`. Static complexity/maintainability and the Track C classifier are recorded separately in `STATIC_ANALYSIS.md` and `DEFECT_PREDICTION.md`.
