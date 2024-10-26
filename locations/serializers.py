from rest_framework import serializers

from locations.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            "name",
            "address",
            "phone_number",
            "website",
            "google_place_id",
            "google_url",
            "latitude",
            "longitude",
        )
