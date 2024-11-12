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


def get_day_list_from_query_params(param: str | None) -> list[str]:
    if param == "weekday":
        return [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, WEEKDAY]
    elif param == "weekend":
        return [SATURDAY, SUNDAY, WEEKEND]
    elif param is None:
        return [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY, WEEKEND, WEEKDAY]
    elif param in [SATURDAY, SUNDAY]:
        return [param, WEEKEND]
    return [param, WEEKDAY]
