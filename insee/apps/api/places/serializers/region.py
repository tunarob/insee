from rest_framework import serializers

from insee.apps.places.models import Region


class RegionSerializer(serializers.ModelSerializer):
    totalArea = serializers.SerializerMethodField()
    totalPopulation = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = ["code", "name", "totalArea", "totalPopulation"]

    def get_totalArea(self, obj: Region):
        return obj.get_total_area()

    def get_totalPopulation(self, obj: Region):
        return obj.get_total_population()
