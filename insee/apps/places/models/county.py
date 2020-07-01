import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class County(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(verbose_name=_('code'), max_length=50)
    name = models.CharField(verbose_name=_('name'), max_length=255)
    region = models.ForeignKey(
        'Region',
        verbose_name=_('region'),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('county')
        verbose_name_plural = _('counties')

    def __str__(self):
        return self.name
