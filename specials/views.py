import logging
from collections import defaultdict

from django.db.models import Q
from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from locations.models import Location
from locations.serializers import LocationSerializer
from specials.choices import get_days_from_query_params
from specials.filters import SpecialFilter
from specials.models import Special
from specials.permissions import IsAuthenticatedPostPermissions
from specials.serializers import (
    GroupedSpecialSerializer,
    SpecialModelExcludeSerializer,
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
        serializer = self.get_serializer(data=request.data, context={"location": location})
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListGroupedSpecialsView(viewsets.generics.ListAPIView):
    """
    This view is used to list grouped specials by location.
    It is used in the frontend to display grouped specials.
    """

    permission_classes = [IsAuthenticatedPostPermissions]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SpecialFilter
    serializer_class = GroupedSpecialSerializer

    def get_queryset(self):
        days: set[str] = get_days_from_query_params(self.request.query_params.getlist("day_of_week"))
        return Special.objects.filter(Q(is_active=True) & Q(day_of_week__in=days))

    def list(self, request: Request, *args, **kwargs) -> Response:
        qs = self.filter_queryset(self.get_queryset())
        grouped = defaultdict(list)
        for special in qs:
            grouped[special.location].append(special)
        results = [
            {
                "location": LocationSerializer(location).data,
                "specials": [SpecialModelExcludeSerializer(x).data for x in specials_for_location],
            }
            for location, specials_for_location in grouped.items()
        ]
        return Response(results, status=status.HTTP_200_OK)
