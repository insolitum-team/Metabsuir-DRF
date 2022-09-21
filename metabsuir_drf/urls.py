from django.contrib import admin
from django.urls import path
from forum.views import SectionApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appi/v1/sections/', SectionApiView.as_view())
]
