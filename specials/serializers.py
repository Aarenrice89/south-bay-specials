import logging
from typing import Any

from rest_framework import serializers

from locations.serializers import LocationSerializer
from specials.models import Special

logger = logging.getLogger(__name__)


class SpecialSerializer(serializers.ModelSerializer):
    limitations = serializers.CharField(allow_null=True)
    start_time = serializers.TimeField(allow_null=True)
    end_time = serializers.TimeField(allow_null=True)

    class Meta:
        model = Special
        fields = (
            "name",
            "description",
            "limitations",
            "day_of_week",
            "start_time",
            "end_time",
        )

    def validate(self, data):
        if Special.objects.filter(location=self.context.get("location"), **data).exists():
            raise serializers.ValidationError("This special already exists.")
        return data

    def create(self, validated_data: dict[str, Any]) -> Special:
        return Special.objects.create(location=self.context.get("location"), **validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["location"] = LocationSerializer(self.context.get("location")).data
        return data


class SpecialModelSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Special
        fields = (
            "name",
            "description",
            "limitations",
            "day_of_week",
            "start_time",
            "end_time",
            "is_active",
            "location",
        )
