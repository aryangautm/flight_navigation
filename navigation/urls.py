from django.urls import path
from django.views.generic import TemplateView

from .views import ShortestPathView

urlpatterns = [
    path("api/shortest-path/", ShortestPathView.as_view(), name="shortest_path_api"),
    path(
        "",
        TemplateView.as_view(template_name="shortest_path.html"),
        name="shortest_path",
    ),
]
