from django.contrib import admin
from django.urls import path
from forum.views import SectionViewSet, ThemeViewSet, CommentViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/mb1/sections/', SectionViewSet.as_view({'get': 'list'})),
    path('api/mb1/sections/<int:pk>/', SectionViewSet.as_view({'put': 'update'})),
    path('api/mb1/themes/', ThemeViewSet.as_view({'get': 'list'})),
    path('api/mb1/themes/<int:pk>/', ThemeViewSet.as_view({'put': 'update'})),
    path('api/mb1/comments/', CommentViewSet.as_view({'get': 'list'})),
    path('api/mb1/comments/<int:pk>/', CommentViewSet.as_view({'post': 'update'})),
]
