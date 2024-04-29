from rest_framework import serializers

from locations.serializers import LocationSerializer
from specials.models import Special


class SpecialSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Special
        fields = (
            "name",
            "location",
            "description",
            "limitations",
            "day_of_week",
            "start_time",
            "end_time",
        )

    def validate(self, data):
        print()
        return data
