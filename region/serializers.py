from rest_framework import serializers

from .models import Region, District, PopularPlaces


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class PopularPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularPlaces
        fields = '__all__'
