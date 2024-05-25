from rest_framework import serializers

from .models import Airport


class AirportSerializer(serializers.ModelSerializer):
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()

    class Meta:
        model = Airport
        fields = ["name", "iata", "icao", "latitude", "longitude", "country", "city"]

    def get_latitude(self, obj):
        return round(obj.latitude, 2)

    def get_longitude(self, obj):
        return round(obj.longitude, 2)
