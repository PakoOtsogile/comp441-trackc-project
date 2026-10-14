# Test-Driven Development Evidence Log

The failing-before observations below were recorded during this work on 14 October 2026. They are limited to the local checkout and are not a claim that the complete upstream suite passes.

## TDD-01 — Reject reversed appointment request interval

- **Red:** Added a regression test that directly saves an appointment request whose end precedes its start. Before the fix, the path raised a low-level `ValueError` while computing a duration instead of the model’s expected `ValidationError`.
- **Green:** `AppointmentRequest.save` now checks reversed times and raises the same localized validation error used by model validation.
- **Verification:** included in the 66-test focused run, which passed.
- **Refactor/review:** reused the existing error wording; equal start/end behavior remains governed by existing validation.

## TDD-02 — Reject negative timedelta appointment duration

- **Red:** Added a test passing `timedelta(minutes=-30)` to `get_ar_end_time`; the old code returned a result instead of raising `ValueError`.
- **Green:** Normalize timedelta/numeric values and reject negative duration consistently.
- **Verification:** included in the 66-test focused run, which passed.

## TDD-03 — Preserve fractional minute duration

- **Red:** Added a 1.5-minute case expecting 10:01:30; the old integer conversion truncated it to 10:01.
- **Green:** Preserve fractional minutes through the seconds conversion.
- **Verification:** included in the 66-test focused run, which passed.

## Run record

Command: `python manage.py test appointment.tests.models.test_appointment_request appointment.tests.utils.test_validators appointment.tests.utils.test_date_time`  
Result: **66 tests passed in 61.522 seconds** on 14 October 2026; Django system check reported no issues.  
Full-suite follow-up: the first shuffled run hit a Windows sandbox permission error because an image test tried writing under the host-managed system temp directory. The test passed when `TMP`, `TEMP`, and `TMPDIR` pointed to the checkout's ignored `.venv/test-tmp`. The full suite was rerun with project CI settings (`USE_DJANGO_Q=true`, `--parallel=10 --shuffle`), using seed 948697336: **580 tests ran, 579 passed, 1 skipped, 0 failures** in 401.789 seconds. The skipped test is environment-conditional; confirm the exact hosted CI result before final submission.
