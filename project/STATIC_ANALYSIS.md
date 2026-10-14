# Static Analysis Baseline

**Date:** 14 October 2026
**Scope:** `appointment/models.py` and `appointment/utils/date_time.py`, two files containing the changed scheduling logic. This is a scoped baseline, not a scan of every repository file.
**Tools:** Pylint 4.1.3 (default configuration), Radon 6.0.1. No project-specific Pylint plugins or baseline suppression file were used.

## Measured results

- Radon cyclomatic complexity: 157 code blocks across the two files; mean complexity grade **A (2.0)**. `AppointmentRequest.clean`, `AppointmentRequest.save`, `Appointment.save`, `Appointment.is_valid_date`, and `get_ar_end_time` are grade **B** hotspots; none exceeded grade B in this scope.
- Radon maintainability index: `appointment/models.py` grade **C**; `appointment/utils/date_time.py` grade **A**.
- Pylint: **315 findings** (191 convention, 26 refactor, 89 error, 9 warning). The default run exits nonzero. These raw counts include longstanding upstream code and Django ORM inference limitations; they are not a count of confirmed defects.
- The regression-focused 66-test coverage run measured the two files together at **64% statement and 37% branch coverage** (59% combined coverage.py figure). `appointment/models.py`: 60% statement / 18% branch; `appointment/utils/date_time.py`: 79% statement / 70% branch. This test selection was focused, not the full suite or AI-only baseline.

## Top findings and triage

| Finding | Count / example | Triage |
|---|---:|---|
| Missing function docstrings | 99 | Maintainability issue across upstream code; add where touched, do not claim runtime defect. |
| `no-member` on Django models/fields/managers | 88 | Likely framework inference false positives (for example `.objects`, relationship access, generated fields); manually verify affected expressions against Django behavior. |
| Lines over 100 characters | 64 | Style issue; only reflow when editing nearby code. |
| Missing class docstrings | 18 | Maintainability issue. |
| Too few public methods | 12 | Usually a Django model/utility class design false positive; not actionable alone. |
| `no-else-return` | 8 | Review for simplification; no behavior defect established by this warning alone. |
| Superfluous parentheses | 5 | Style-only. |
| Unused arguments | 4 | Common signal-handler signature pattern; verify callback contract before removal. |
| Invalid names | 3 | Style-only. |
| Raise without exception chaining | 2 | Add `from exc` where context should be preserved; existing behavior needs no change unless useful for diagnosis. |

Pylint's 88 Django `no-member` messages account for nearly all error-level output; they need a Django-aware plugin or manual adjudication before treating them as defects. A high-confidence comparison against an LLM reviewer has not been performed: the prompt, fixed sample, independent ground truth, reviewer adjudication, and confusion matrix are still needed. Do not report a precision/recall comparison without them.

## Symbolic path discussion

For `get_ar_end_time(start_time, duration)`, a path analyzer can explore the start-type guard (`time`/`str` versus invalid), duration-type guard (`timedelta`/numeric versus invalid), normalization branch, the negative-duration branch, optional string parsing, and the midnight-wrap branch. Useful boundary inputs include exactly zero, a negative integer, a negative `timedelta`, a fractional minute such as 1.5, a string with valid and invalid formats, and a start near 23:59 that crosses midnight. Example tests cover several of these, while type rejection and the full cross-product of start/duration types should be checked against the RTM. A symbolic tool was not run; this is the brief-required path reasoning, not symbolic execution evidence.
