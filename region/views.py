from rest_framework import viewsets
from .models import Region, District, PopularPlaces
from .serializers import RegionSerializer, DistrictSerializer, PopularPlacesSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class PopularPlacesViewSet(viewsets.ModelViewSet):
    queryset = PopularPlaces.objects.all()
    serializer_class = PopularPlacesSerializer
