from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AirportViewSet, FlightViewSet

router = DefaultRouter()
router.register(r"flights", FlightViewSet)
router.register(r"airports", AirportViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
