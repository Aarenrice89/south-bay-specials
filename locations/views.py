from rest_framework import status, viewsets
from rest_framework.response import Response

from locations.models import Location
from locations.serializers import LocationSerializer

# from rest_framework.decorators import action, api_view, permission_classes
# from rest_framework.exceptions import NotFound
# from drf_spectacular.utils import extend_schema


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
