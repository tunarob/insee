import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code_insee = models.CharField(verbose_name=_("code insee"), max_length=50)
    code_postal = models.CharField(
        verbose_name=_("code postal"),
        max_length=50,
    )
    name = models.CharField(verbose_name=_("name"), max_length=255)
    population = models.DecimalField(
        verbose_name=_("population"),
        max_digits=5,
        decimal_places=1,
    )
    area = models.DecimalField(
        verbose_name=_("area"),
        max_digits=8,
        decimal_places=1,
    )
    county = models.ForeignKey(
        "County",
        verbose_name=_("county"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cities")

    def __str__(self):
        return self.name
