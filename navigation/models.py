from django.db import models


class Airport(models.Model):
    name = models.CharField(max_length=100)
    iata = models.CharField(max_length=10, unique=True)
    icao = models.CharField(max_length=10, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Route(models.Model):
    source = models.ForeignKey(
        Airport, related_name="source_routes", on_delete=models.CASCADE
    )
    destination = models.ForeignKey(
        Airport, related_name="destination_routes", on_delete=models.CASCADE
    )
    path = models.TextField()  # Store the path as a JSON string
    distance = models.FloatField()

    def __str__(self):
        return f"{self.path} ({self.distance} km)"
