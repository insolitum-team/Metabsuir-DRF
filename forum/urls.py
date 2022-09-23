from django.urls import path
from .views import get_themes, get_comments


urlpatterns = [
    path('api/mb2/themes/section/<section_id>/', get_themes),
    path('api/mb2/comments/theme/<theme_id>/', get_comments),
]
