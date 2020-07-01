from django.contrib import admin

from .models import City, County, Region


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code_insee', 'code_postal', 'population', 'area')
    search_fields = ('name', 'code_insee', 'code_postal')


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
