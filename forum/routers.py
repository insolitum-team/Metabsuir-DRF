from rest_framework import routers

from forum.views import SectionViewSet, ThemeViewSet, CommentViewSet


section_router = theme_router = comments_router = routers.SimpleRouter()

section_router.register(r'sections', SectionViewSet, basename='sections')
theme_router.register(r'themes', ThemeViewSet, basename='themes')
section_router.register(r'comments', CommentViewSet, basename='comments')
