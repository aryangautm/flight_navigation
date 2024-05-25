from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("navigation.urls")),
    path("aviation/", include("aviation_data.urls")),
    path("navigation/", include("navigation.urls")),
]
