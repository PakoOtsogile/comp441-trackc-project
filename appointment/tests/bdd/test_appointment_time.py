"""Executable pytest-bdd scenarios for appointment time calculations."""

from datetime import datetime, time

from pytest_bdd import given, parsers, scenarios, then, when

from appointment.utils.date_time import get_ar_end_time


scenarios("../../../project/BDD/appointment-time.feature")


@given(parsers.parse("a request starts at {start_time}"), target_fixture="context")
def request_start_time(start_time):
    return {"start": datetime.strptime(start_time, "%H:%M").time()}


@when(parsers.parse("a {duration:g} minute duration is applied"))
def apply_duration(context, duration):
    try:
        context["end"] = get_ar_end_time(context["start"], duration)
    except ValueError as error:
        context["error"] = error


@then(parsers.parse("the resulting end time is {end_time}"))
def resulting_end_time(context, end_time):
    assert context["end"] == time.fromisoformat(end_time)


@then("the duration is rejected")
def duration_is_rejected(context):
    assert isinstance(context.get("error"), ValueError)
