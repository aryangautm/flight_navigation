from django.db import models


class Flight(models.Model):
    flight_number = models.CharField(max_length=10, null=True)
    departure_airport = models.CharField(max_length=3, null=True)
    arrival_airport = models.CharField(max_length=3, null=True)
    status = models.CharField(max_length=20, null=True)
    departure_time = models.DateTimeField(null=True)
    arrival_time = models.DateTimeField(null=True)


class Airport(models.Model):
    iata_code = models.CharField(max_length=3, null=True)
    name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)


class Scenario(models.Model):
    scenario_type = models.CharField(max_length=50)
    description = models.TextField()
    related_flights = models.ManyToManyField("Flight", blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
