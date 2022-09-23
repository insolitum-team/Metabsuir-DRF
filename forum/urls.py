from django.urls import path
from .views import get_themes_by_section, get_comments_by_theme


urlpatterns = [
    path('api/mb2/themes/section/<section_id>/', get_themes_by_section),
    path('api/mb2/comments/theme/<theme_id>/', get_comments_by_theme),
]
