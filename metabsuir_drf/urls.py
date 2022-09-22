from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from forum.views import SectionViewSet, ThemeViewSet, CommentViewSet

section_router = routers.SimpleRouter()
section_router.register(r'sections', SectionViewSet)

theme_router = routers.SimpleRouter()
theme_router.register(r'themes', ThemeViewSet)

comments_router = routers.SimpleRouter()
section_router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/mb2/', include(section_router.urls)),
    path('api/mb2/', include(theme_router.urls)),
    path('api/mb2/', include(comments_router.urls)),
]
