from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status, viewsets
from rest_framework.response import Response

from locations.models import Location
from locations.serializers import LocationSerializer
from specials.choices import DAY_CHOICES


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    # permission_classes = []

    # https://www.cdrf.co/3.14/rest_framework.viewsets/ModelViewSet.html

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses={200: LocationSerializer(many=True)},
        parameters=[
            OpenApiParameter(
                name="day",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Day of the week to filter by",
                enum=[day[0] for day in DAY_CHOICES],
            )
        ],
    )
    def list(self, request):
        filter_params = {}
        if dow := request.query_params.get("day"):
            filter_params["special__day_of_week"] = dow
        queryset = Location.objects.filter(**filter_params).distinct()
        serializer = LocationSerializer(queryset, many=True)
        return Response(serializer.data)
