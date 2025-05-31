from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include('shared.uitils.swagger')),
    path('api/', include('users.urls')),
    path('api/', include('region.urls')),
    path('api/', include('facilities.urls')),
    path('api/', include('dacha.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
