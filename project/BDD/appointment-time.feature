Feature: Appointment request time validation
  The scheduling system must reject impossible durations and preserve valid times.

  Scenario: A positive whole-hour duration
    Given a request starts at 10:00
    When a 60 minute duration is applied
    Then the resulting end time is 11:00

  Scenario: A fractional minute duration
    Given a request starts at 10:00
    When a 1.5 minute duration is applied
    Then the resulting end time is 10:01:30

  Scenario: A negative duration
    Given a request starts at 10:00
    When a -30 minute duration is applied
    Then the duration is rejected
