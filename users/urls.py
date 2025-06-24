from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserMeViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'me', UserMeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
