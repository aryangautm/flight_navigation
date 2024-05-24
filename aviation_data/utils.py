import requests
from django.conf import settings

from navigation.models import Airport


def get_weather_data(iata_code):
    api_key = settings.OPENWEATHERMAP_API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Use a sample mapping from IATA codes to city names or coordinates
    airport = Airport.objects.all().get(iata=iata_code)

    params = {
        "lat": airport.get("latitude"),
        "lon": airport.get("longitude"),
        "appid": api_key,
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching weather data: {response.status_code}")
