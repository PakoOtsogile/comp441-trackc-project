# Requirements Traceability Matrix

This initial matrix derives expected behaviors from the checked-out source, tests, and the Track C assignment brief. Confirm wording with the team and coordinator. “Covered” means a named automated test exists; it does not imply full system acceptance.

| ID | Requirement / expected behavior | Implementation | Verification evidence |
|---|---|---|---|
| R-01 | A request whose end time precedes its start time is rejected with a validation error. | `appointment/models.py` (`AppointmentRequest.save`) | `appointment/tests/models/test_appointment_request.py::test_saving_request_with_end_before_start_raises_validation_error` |
| R-02 | Appointment request start/end ordering is also checked by model validation. | `AppointmentRequest.clean` | Existing request-model tests; add explicit clean-path case if absent |
| R-03 | A negative numeric duration is rejected. | `appointment/utils/date_time.py::get_ar_end_time` | `appointment/tests/utils/test_date_time.py::GetAppointmentRequestEndTimeTests.test_negative_duration` |
| R-04 | A negative `timedelta` duration is rejected. | `get_ar_end_time` | `...test_negative_timedelta_duration` |
| R-05 | A positive fractional numeric minute duration preserves seconds. | `get_ar_end_time` | `...test_fractional_minute_duration_preserves_seconds` |
| R-06 | Supported string and `datetime.time` start values produce a time result. | `get_ar_end_time` | `...test_get_ar_end_time_with_valid_inputs` |
| R-07 | Duration that crosses midnight wraps the returned time to the next day. | `get_ar_end_time` | `...test_end_time_past_midnight` |
| R-08 | Invalid start-time formats fail rather than silently producing a result. | `get_ar_end_time` | `...test_invalid_start_time_format` |
| R-09 | Unsupported duration types are rejected. | `get_ar_end_time` | `...test_invalid_duration_format` |
| R-10 | Available slots respect configured settings and existing bookings. | appointment service layer | `appointment/tests/test_services.py::GetAvailableSlotsTests.test_get_available_slots`; `...test_get_available_slots_with_config` |
| R-11 | Staff may retrieve only appointments authorized for their account. | appointment services/views | `appointment/tests/test_services.py::FetchUserAppointmentsTests.test_fetch_appointments_for_staff_member` |
| R-12 | Unauthorized users cannot retrieve protected appointment data. | appointment services/views | `appointment/tests/test_services.py::PrepareAppointmentDisplayDataTests.test_unauthorized_user` |
| R-13 | Valid appointment requests are accepted through the HTTP layer. | appointment views | `appointment/tests/test_views.py::AppointmentRequestTestCase.test_appointment_request_submit_valid` |
| R-14 | The upstream regression suite and Gherkin acceptance scenarios run in CI. | `.github/workflows/tests.yml` | CI matrix runs `manage.py test appointment.tests` and `python -m pytest appointment/tests/bdd -q` |

## Evidence gaps to close

- Review the pytest-bdd scenarios and Gherkin wording together; the hosted CI run has not yet been confirmed.
- Confirm that the five HTTP/database integration examples in `INTEGRATION_TESTS.md` satisfy the coordinator's definition of integration test.
- Verify the group-agreed source citations and evidence links in the final report.
