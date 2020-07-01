from django.db.models import Sum
from rest_framework import serializers

from insee.apps.places.models import City, Region


class RegionSerializer(serializers.ModelSerializer):
    totalArea = serializers.SerializerMethodField()
    totalPopulation = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = ["code", "name", "totalArea", "totalPopulation"]

    def get_totalArea(self, obj: Region):
        return City.objects.filter(county__region=obj).aggregate(
            total=Sum("area")
        )["total"]

    def get_totalPopulation(self, obj: Region):
        return City.objects.filter(county__region=obj).aggregate(
            total=Sum("population")
        )["total"]
