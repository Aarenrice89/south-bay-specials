import logging
from typing import Any

from rest_framework import serializers

from locations.serializers import LocationExcludeSerializer, LocationSerializer
from specials.models import Special

logger = logging.getLogger(__name__)


class SpecialSerializer(serializers.ModelSerializer):
    limitations = serializers.CharField(allow_null=True, required=False, default=None)
    start_time = serializers.TimeField(allow_null=True, required=False, default=None)
    end_time = serializers.TimeField(allow_null=True, required=False, default=None)

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

    def validate(self, attrs):
        if Special.objects.filter(location=self.context.get("location"), **attrs).exists():
            raise serializers.ValidationError("This special already exists.")
        return attrs

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


class SpecialModelExcludeSerializer(serializers.ModelSerializer):
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


class GroupedSpecialSerializer(serializers.Serializer):
    location = LocationSerializer()
    specials = SpecialModelExcludeSerializer(many=True)
