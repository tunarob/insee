import uuid

from django.db import models
from django.db.models import Sum
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from .city import City
from ..coordinates.coordinates import Coordinates
from ..coordinates.region_cooridnates_nominatim import fetch_coordinates


class Region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.IntegerField(verbose_name=_('code'))
    name = models.CharField(verbose_name=_('name'), max_length=255)

    class Meta:
        verbose_name = _('region')
        verbose_name_plural = _('regions')

    def __str__(self):
        return self.name

    @cached_property
    def coordinates(self) -> Coordinates:
        return fetch_coordinates(self.name)

    def get_total_area(self):
        return City.objects.filter(county__region=self).aggregate(
            total=Sum("area")
        )["total"]

    def get_total_population(self):
        return City.objects.filter(county__region=self).aggregate(
            total=Sum("population")
        )["total"]
