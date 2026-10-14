"""Executable Django-test counterparts to project/BDD/appointment-time.feature.

Each test follows Given/When/Then in its body so the Gherkin scenarios remain
reviewable without adding a second test framework to the upstream project.
"""

import datetime

from django.test import SimpleTestCase

from appointment.utils.date_time import get_ar_end_time


class AppointmentTimeBddScenarios(SimpleTestCase):
    def test_scenario_positive_whole_hour_duration(self):
        # Given a request starts at 10:00
        start = datetime.time(10, 0)
        # When a 60 minute duration is applied
        end = get_ar_end_time(start, 60)
        # Then the resulting end time is 11:00
        self.assertEqual(end, datetime.time(11, 0))

    def test_scenario_fractional_minute_duration(self):
        # Given a request starts at 10:00
        start = datetime.time(10, 0)
        # When a 1.5 minute duration is applied
        end = get_ar_end_time(start, 1.5)
        # Then the resulting end time is 10:01:30
        self.assertEqual(end, datetime.time(10, 1, 30))

    def test_scenario_negative_duration_is_rejected(self):
        # Given a request starts at 10:00
        start = datetime.time(10, 0)
        # When a -30 minute duration is applied, Then the duration is rejected
        with self.assertRaises(ValueError):
            get_ar_end_time(start, -30)
