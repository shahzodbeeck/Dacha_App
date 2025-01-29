from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FacilitiesViewSet

router = DefaultRouter()
router.register(r'facilities', FacilitiesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
