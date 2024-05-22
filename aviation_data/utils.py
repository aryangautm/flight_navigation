import requests
from django.conf import settings


def get_weather_data(iata_code):
    api_key = settings.OPENWEATHERMAP_API_KEY
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    # Use a sample mapping from IATA codes to city names or coordinates
    airport_mapping = {
        'JFK': {'lat': 40.6413, 'lon': -73.7781},
        'LAX': {'lat': 33.9416, 'lon': -118.4085},
        # Add more airport mappings as needed
    }

    location = airport_mapping.get(iata_code)
    if not location:
        raise ValueError(f"No location mapping found for IATA code: {iata_code}")

    params = {
        'lat': location['lat'],
        'lon': location['lon'],
        'appid': api_key
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching weather data: {response.status_code}")
