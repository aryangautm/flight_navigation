import json
from datetime import datetime

import requests
from django.conf import settings

from navigation.models import Airport


def fetch_weather_data(lon, lat):
    api_key = settings.OPENWEATHERMAP_API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Use a sample mapping from IATA codes to city names or coordinates

    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching weather data: {response.status_code}")


def get_weather_data(lon, lat):
    weather = fetch_weather_data(lon, lat)
    with open("weat.json", "w") as file:
        json.dump(weather, file)
    weather_main = weather["weather"][0]["main"]
    return weather_main
