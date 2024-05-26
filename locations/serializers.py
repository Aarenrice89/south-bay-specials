from locations.models import Location
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            "name",
            "address",
            "city",
            "state",
            "country",
            "zipcode",
            "google_link",
        )

    def validate(self, data):
        print()
        return data
