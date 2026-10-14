# Integration Test Evidence

These existing tests exercise multiple application layers, including Django request handling, services, database-backed models, and/or authorization. The group should confirm that the coordinator considers these integration tests under the course rubric.

1. `appointment.tests.test_views.AppointmentRequestTestCase.test_appointment_request_submit_valid` — valid HTTP submission and appointment-request flow.
2. `appointment.tests.test_views.AppointmentRequestTestCase.test_appointment_request_submit_invalid` — invalid HTTP submission and validation response.
3. `appointment.tests.test_views.SlotTestCase.test_get_available_slots_ajax` — AJAX view and availability response.
4. `appointment.tests.test_services.GetAvailableSlotsTests.test_get_available_slots` — persisted appointment and slot-availability service behavior.
5. `appointment.tests.test_services.FetchUserAppointmentsTests.test_fetch_appointments_for_staff_member` — role-aware query behavior.

## Execution status

The five listed integration cases were executed together with the three BDD scenario tests on 14 October 2026. All 8 passed in 79.008 seconds. The run used Django's temporary test database and reported no system-check errors. This is a focused run, not the full upstream suite.
