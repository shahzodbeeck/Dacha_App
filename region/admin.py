from django.contrib import admin

from .models import Region, District, PopularPlaces


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'is_active')
    search_fields = ('name',)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'created_at', 'updated_at', 'is_active')
    list_filter = ('province',)
    search_fields = ('name', 'province__name')


class PopularPlacesAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'created_at', 'updated_at', 'is_active')
    list_filter = ('district',)
    search_fields = ('name', 'district__name')


admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(PopularPlaces, PopularPlacesAdmin)
