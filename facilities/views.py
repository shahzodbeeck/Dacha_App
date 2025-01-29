from rest_framework import viewsets

from .models import Facilities
from .serializers import FacilitiesSerializer


class FacilitiesViewSet(viewsets.ModelViewSet):
    queryset = Facilities.objects.all()
    serializer_class = FacilitiesSerializer
