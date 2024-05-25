from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FlightViewSet

router = DefaultRouter()
router.register(r"flights", FlightViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
