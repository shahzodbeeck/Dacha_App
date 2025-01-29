from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (DachaViewSet, DachaImageViewSet, DachaCommentViewSet, DachaLikeViewSet, DachaCommentLikeViewSet,
                    DachaRatingViewSet)

router = DefaultRouter()
router.register(r'dachas', DachaViewSet)
router.register(r'dacha_images', DachaImageViewSet)
router.register(r'dacha_comments', DachaCommentViewSet)
router.register(r'dacha_likes', DachaLikeViewSet)
router.register(r'dacha_comment_likes', DachaCommentLikeViewSet)
router.register(r'dacha_ratings', DachaRatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
