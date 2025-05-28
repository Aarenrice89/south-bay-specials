from django.utils.translation import gettext_lazy as _

MONDAY = "monday"
TUESDAY = "tuesday"
WEDNESDAY = "wednesday"
THURSDAY = "thursday"
FRIDAY = "friday"
SATURDAY = "saturday"
SUNDAY = "sunday"
WEEKDAY = "weekday"
WEEKEND = "weekend"

DAY_CHOICES = [
    (MONDAY, _(MONDAY)),
    (TUESDAY, _(TUESDAY)),
    (WEDNESDAY, _(WEDNESDAY)),
    (THURSDAY, _(THURSDAY)),
    (FRIDAY, _(FRIDAY)),
    (SATURDAY, _(SATURDAY)),
    (SUNDAY, _(SUNDAY)),
    (WEEKDAY, _(WEEKDAY)),
    (WEEKEND, _(WEEKEND)),
]


def get_days_from_query_params(params: list[str]) -> set[str]:
    days = set()
    if not params:
        return {MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY, WEEKEND, WEEKDAY}
    for param in params:
        days.update(get_day_list(param))
    return days


def get_day_list(param: str) -> list[str]:
    if param == "weekday":
        return [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, WEEKDAY]
    elif param == "weekend":
        return [SATURDAY, SUNDAY, WEEKEND]
    elif param in [SATURDAY, SUNDAY]:
        return [param, WEEKEND]
    return [param, WEEKDAY]
