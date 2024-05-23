import requests
from django.core.management.base import BaseCommand
from django.utils import timezone

from aviation_data.models import Flight, Scenario

from ...utils import get_weather_data


class Command(BaseCommand):
    help = "Identify and document flight navigation scenarios"

    def handle(self, *args, **kwargs):
        # Fetch active flights
        flights = Flight.objects.filter(status="active")

        for flight in flights:
            # Check for adverse weather conditions
            if self.is_adverse_weather(flight):
                scenario, created = Scenario.objects.get_or_create(
                    scenario_type="Adverse Weather",
                    defaults={
                        "description": "Detected adverse weather conditions affecting flight.",
                        "timestamp": timezone.now(),
                    },
                )
                scenario.related_flights.add(flight)
                scenario.save()

        self.stdout.write(
            self.style.SUCCESS("Successfully identified and documented scenarios.")
        )

    def is_adverse_weather(self, flight):
        # Get weather data for departure and arrival airports
        departure_weather = get_weather_data(flight.departure_airport)
        arrival_weather = get_weather_data(flight.arrival_airport)

        # Placeholder logic to determine adverse weather conditions
        if departure_weather["weather"][0]["main"] in [
            "Rain",
            "Snow",
            "Fog",
        ] or arrival_weather["weather"][0]["main"] in ["Rain", "Snow", "Fog"]:
            return True
        return False
