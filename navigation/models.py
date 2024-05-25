from django.db import models
from django.db.models import CheckConstraint, Q, UniqueConstraint


class Airport(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    iata = models.CharField(max_length=10, blank=True, null=True)
    icao = models.CharField(max_length=10, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["iata"],
                name="unique_iata_not_backslash_n",
                condition=~Q(
                    iata="\\N"
                ),  # Unique constraint only when iata is not '\N'
            ),
        ]

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
    duration = models.FloatField(default=0, null=True)

    def __str__(self):
        return f"{self.path} ({self.distance} km)"
