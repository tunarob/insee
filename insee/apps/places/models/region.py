import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Region(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(verbose_name=_('code'), max_length=50)
    name = models.CharField(verbose_name=_('name'), max_length=255)

    class Meta:
        verbose_name = _('region')
        verbose_name_plural = _('regions')

    def __str__(self):
        return self.name
