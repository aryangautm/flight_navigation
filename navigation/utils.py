import json
from datetime import datetime

import requests
from django.conf import settings


class UpperCaseConverter:
    regex = "[a-zA-Z0-9]+"

    def to_python(self, value):
        return value.upper()

    def to_url(self, value):
        return value


def fetch_airport_data(code):
    api_key = settings.FLIGHTAWARE_API_KEY
    base_url = "https://aeroapi.flightaware.com/aeroapi/airports/"

    # Use a sample mapping from IATA codes to city names or coordinates

    params = {
        "id": code,
    }

    response = requests.get(base_url, params=params)
    with open("airport.json", "w") as file:
        json.dump(response, file)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching weather data: {response.status_code}")
