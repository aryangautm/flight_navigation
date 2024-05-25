# urls.py
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .views import AirportDetailView, ShortestPathView

router = DefaultRouter()
router.register(r"airports", AirportDetailView, basename="airport")


urlpatterns = [
    path("api/shortest-path/", ShortestPathView.as_view(), name="shortest_path_api"),
    path(
        "",
        TemplateView.as_view(template_name="shortest_path.html"),
        name="shortest_path",
    ),
    path("api/", include(router.urls)),
]
