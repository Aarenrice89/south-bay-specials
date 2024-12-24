import logging

from django.db.models import Q
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from locations.models import Location
from specials.choices import DAY_CHOICES, get_day_list_from_query_params
from specials.models import Special
from specials.permissions import IsAuthenticatedPostPermissions
from specials.serializers import (
    GroupedSpecialSerializer,
    SpecialModelSerializer,
    SpecialSerializer,
)

logger = logging.getLogger(__name__)


class SpecialViewset(viewsets.ModelViewSet):
    queryset = Special.objects.filter(is_active=True)
    serializer_class = SpecialSerializer
    permission_classes = [IsAuthenticatedPostPermissions]

    def list(self, request: Request, *args, **kwargs) -> Response:
        queryset = self.get_queryset()
        serializer = SpecialModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request: Request, *args, **kwargs) -> Response:
        location, created = Location.objects.get_or_create(**request.data.get("selected_place"))
        logger.info(f"New location created: {created}, {location.name}")
        serializer = self.get_serializer(data=request.data, context={"location": location})
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses=GroupedSpecialSerializer,
        parameters=[
            OpenApiParameter(
                name="day",
                type=str,
                required=False,
                enum=[x[0] for x in DAY_CHOICES],
            )
        ],
    )
    @action(detail=False, methods=["GET"], url_name="grouped", url_path="grouped")
    def grouped_specials_by_location(self, request: Request) -> Response:
        days: list[str] = get_day_list_from_query_params(request.query_params.get("day"))
        qs = Location.objects.filter(Q(special__is_active=True) & Q(special__day_of_week__in=days)).distinct("name")
        serializer = GroupedSpecialSerializer(qs, many=True, context={"days": days})
        return Response(serializer.data, status=status.HTTP_200_OK)
