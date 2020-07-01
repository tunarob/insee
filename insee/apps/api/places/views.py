from rest_framework import mixins, viewsets

from insee.apps.places.models import Region
from .serializers.region import RegionSerializer


class RegionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
