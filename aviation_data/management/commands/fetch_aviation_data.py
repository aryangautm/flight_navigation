import json

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

from aviation_data.models import Airport, Flight


class Command(BaseCommand):
    help = "Fetch data from Aviation Stack API"

    def handle(self, *args, **kwargs):
        api_key = settings.AVIATIONSTACK_API_KEY
        base_url = "http://api.aviationstack.com/v1"

        # Example for fetching flight data
        flight_endpoint = f"{base_url}/flights"
        params = {"access_key": api_key, "limit": 10}  # Adjust the limit as needed
        response = requests.get(flight_endpoint, params=params)
        if response.status_code == 200:
            data = response.json()
            with open("data.json", "w") as f:
                json.dump(data, f)
            for flight in data["data"]:
                Flight.objects.update_or_create(
                    flight_number=flight["flight"]["iata"],
                    defaults={
                        "departure_airport": flight["departure"]["iata"],
                        "arrival_airport": flight["arrival"]["iata"],
                        "status": flight["flight_status"],
                        "departure_time": flight["departure"]["estimated"],
                        "arrival_time": flight["arrival"]["estimated"],
                    },
                )
        else:
            self.stderr.write(f"Error: {response.json()}")

        # # Example for fetching airport data
        airport_endpoint = f"{base_url}/airports"
        response = requests.get(airport_endpoint, params={"access_key": api_key})
        if response.status_code == 200:
            data = response.json()
            for airport in data["data"]:
                Airport.objects.update_or_create(
                    iata_code=airport["iata_code"],
                    defaults={
                        "name": airport["airport_name"],
                        # 'city': airport['city'],
                        "country": airport["country_name"],
                    },
                )
        else:
            self.stderr.write(f"Error: {response.status_code}")
