from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RegionViewSet, DistrictViewSet, PopularPlacesViewSet

router = DefaultRouter()
router.register(r'regions', RegionViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'popularplaces', PopularPlacesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
