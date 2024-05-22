from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    wind_speed = models.FloatField()
    visibility = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class FlightStatus(models.Model):
    flight_number = models.CharField(max_length=10)
    status = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
