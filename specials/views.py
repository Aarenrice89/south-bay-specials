import logging

from rest_framework import status, viewsets
from rest_framework.response import Response

from locations.models import Location
from specials.models import Special
from specials.serializers import SpecialModelSerializer, SpecialSerializer

logger = logging.getLogger(__name__)


class SpecialViewset(viewsets.ModelViewSet):
    queryset = Special.objects.filter(is_active=True)
    serializer_class = SpecialSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = SpecialModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        location, created = Location.objects.get_or_create(**request.data.get("selected_place"))
        logger.info(f"New location created: {created}, {location.name}")
        serializer = self.get_serializer(data=request.data, context={"location": location})
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
