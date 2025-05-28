import django_filters

from specials.choices import DAY_CHOICES
from specials.models import Special


class SpecialFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="filter_search")
    day_of_week = django_filters.MultipleChoiceFilter(field_name="day_of_week", choices=DAY_CHOICES, conjoined=False)

    class Meta:
        model = Special
        fields = ["search", "day_of_week"]

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            django_filters.filters.Q(name__icontains=value) | django_filters.filters.Q(description__icontains=value)
        )
