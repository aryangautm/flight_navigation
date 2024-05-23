# aviation_data/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/flight_health/$", consumers.FlightHealthConsumer.as_view()),
]
