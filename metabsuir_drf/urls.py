from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from forum.routers import section_router, theme_router, comments_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/mb2/drf-auth/', include('rest_framework.urls')),
    path('', include('forum.urls')),
    path('api/mb2/', include(section_router.urls)),
    path('api/mb2/', include(theme_router.urls)),
    path('api/mb2/', include(comments_router.urls)),
    path('api/mb2/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/mb2/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/mb2/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
