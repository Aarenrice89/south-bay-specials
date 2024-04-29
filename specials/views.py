from rest_framework import viewsets

from specials.models import Special
from specials.serializers import SpecialSerializer


class SpecialViewset(viewsets.ModelViewSet):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer
