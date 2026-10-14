# Mutation Analysis — Interim Sample

**Status:** targeted sensitivity sample completed; not the required AI-only v1 versus hybrid v2 comparison.

## Reproduction

Mutatest 3.1.0 was run against `appointment/utils/date_time.py` with the 51 existing date/time unit tests, seed 441, and eight sampled AST locations:

```powershell
python scripts/run_mutatest.py -s appointment/utils/date_time.py `
  -t "python manage.py test appointment.tests.utils.test_date_time --verbosity=0" `
  -n 8 -r 441 -o project/MUTATION_SAMPLE.rst --timeout_factor 3
```

Mutatest 3.1.0 calls `random.sample` on a set, which Python 3.12 rejects. `scripts/run_mutatest.py` applies a sorted-sequence compatibility shim in the launcher process; it does not edit the application or installed Mutatest package. Install Mutatest 3.1.0 in the analysis environment before running the command. Sorted set conversion also makes the seeded sample selection reproducible across processes.

## Result

| Sample measure | Result |
|---|---:|
| Candidate AST locations | 46 |
| Sampled locations | 8 (17.39%) |
| Executed mutant variants | 23 |
| Detected by tests | 19 |
| Survived | 4 |
| Timeout / error | 0 |
| Sample mutation score | 82.6% (19 / 23) |

This is a small seeded sample, not an exhaustive mutation score. It measures the existing date/time unit suite as a whole; the tests were not isolated as an AI-only v1 suite, and there is no human-augmented v2 comparison yet. The tool report is archived at [`MUTATION_SAMPLE.rst`](MUTATION_SAMPLE.rst).

## Survivor review

| Source line | Mutant | Initial assessment | Follow-up |
|---:|---|---|---|
| 198 | `==` → `>` for the `A.M.` suffix | Can alter behavior for malformed suffix strings; current tests cover valid AP suffixes only. | Group should decide whether malformed suffixes are in scope. If yes, add explicit invalid-suffix behavior and test it. |
| 205 | `==` → `>=` for the `P.M.` suffix | Same boundary gap for malformed suffix strings. | Same adjudication as line 198. |
| 242 | `len(parts) == 2` → `<= 2` | Appears equivalent for reachable control flow: zero parts has no matching return; one/two parts have already returned. | Treat as equivalent unless a reachable input disproves that reasoning. |
| 302 | type-check `if` → false | The later parsing/arithmetic path may independently raise `TypeError`; likely equivalent for covered invalid inputs. | Inspect exception type/message for each unsupported input before counting this as a test gap. |

The two potentially non-equivalent survivors expose an unspecified malformed-input contract, not a demonstrated appointment-time defect. No tests were added to codify that behavior without group agreement. This review covers four survivors in this sample; the assignment's eight v1 survivor case studies still require a properly separated AI-only v1 run and team review.
