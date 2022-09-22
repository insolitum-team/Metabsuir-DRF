from django.contrib import admin
from django.urls import path
from forum.views import SectionApiView, SectionApiViewRU, ThemeApiView, ThemeApiViewRU, CommentApiView, CommentApiViewRU

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/mb1/sections/', SectionApiView.as_view()),
    path('api/mb1/sections/<int:pk>/', SectionApiViewRU.as_view()),
    path('api/mb1/themes/', ThemeApiView.as_view()),
    path('api/mb1/themes/<int:pk>/', ThemeApiViewRU.as_view()),
    path('api/mb1/comments/', CommentApiView.as_view()),
    path('api/mb1/comments/<int:pk>/', CommentApiViewRU.as_view()),
]
