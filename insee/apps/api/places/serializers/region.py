from rest_framework import serializers

from insee.apps.places.models import Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["code", "name"]
