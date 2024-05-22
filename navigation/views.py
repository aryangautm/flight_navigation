from django.shortcuts import render
from .models import WeatherData, FlightStatus

def index(request):
    weather_data = WeatherData.objects.all().order_by('-timestamp')[:1]
    flight_status = FlightStatus.objects.all().order_by('-timestamp')[:1]
    context = {
        'weather_data': weather_data,
        'flight_status': flight_status
    }
    return render(request, 'navigation/index.html', context)

from django.shortcuts import render
from .utils import fetch_real_time_data, suggest_optimal_path

def home(request):
    # Fetch real-time data (Example URLs)
    weather_api_url = 'https://api.openweathermap.org/data/2.5/weather?...'
    flight_api_url = 'https://api.flightaware.com/...'
    # fetch_real_time_data(weather_api_url, flight_api_url)

    # Example paths (you should replace this with actual data from your models)
    paths = [
        {'distance': 500, 'risk': 0.2},
        {'distance': 600, 'risk': 0.1},
        {'distance': 550, 'risk': 0.15}
    ]

    optimal_path = suggest_optimal_path(paths, alpha=0.4, beta=0.6)
    context = {'optimal_path': optimal_path}

    return render(request, 'home.html', context)

# aviation_data/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .route_planning import a_star_with_risks

class RoutePlanningView(APIView):
    def get(self, request, format=None):
        start_airport = request.query_params.get('start')
        end_airport = request.query_params.get('end')
        
        if not start_airport or not end_airport:
            return Response({'error': 'Start and end airports are required'}, status=400)
        
        route = a_star_with_risks(start_airport, end_airport)
        
        return Response({'route': route})

