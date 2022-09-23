from django.contrib import admin
from django.urls import path, include

from forum.routers import section_router, theme_router, comments_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forum.urls')),
    path('api/mb2/', include(section_router.urls)),
    path('api/mb2/', include(theme_router.urls)),
    path('api/mb2/', include(comments_router.urls)),
]
