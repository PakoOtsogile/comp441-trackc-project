# Risk-Based Test Prioritization

**Status:** interim documented heuristic for the hybrid suite; replace or validate with the Track C classifier after reviewed labels are available.

Order tests to reveal temporal defects quickly, then exercise persisted workflows and permissions. This is a risk-based prioritization method, not an ML result.

| Order | Test group | Representative tests | Risk rationale |
|---:|---|---|---|
| 1 | Time conversion boundaries | `appointment.tests.utils.test_date_time`; `appointment.tests.bdd` | Small/fast tests cover negative, fractional, malformed, and midnight boundary behavior. |
| 2 | Appointment request validation | `appointment.tests.models.test_appointment_request` | Direct saves and model validation exercise interval ordering and field constraints. |
| 3 | Availability and service rules | `appointment.tests.test_services.GetAvailableSlotsTests` | Combines request times, configured availability, and existing bookings. |
| 4 | HTTP booking and authorization | `appointment.tests.test_views.AppointmentRequestTestCase`; `FetchUserAppointmentsTests` | User-facing and access-control paths have higher impact and cross more components. |
| 5 | Remaining upstream regression suite | `appointment.tests` | Broad compatibility and regression net after the targeted high-risk paths. |

The intended CI effect is to surface scheduling arithmetic failures before slower database/system checks. Validate the actual order and time-to-failure from CI logs; do not claim a measured reduction until compared with a baseline.
