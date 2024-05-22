from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, AirportViewSet

router = DefaultRouter()
router.register(r'flights', FlightViewSet)
router.register(r'airports', AirportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
