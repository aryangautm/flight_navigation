# management/commands/load_airports.py
import csv

from django.core.management.base import BaseCommand

from ...models import Airport


class Command(BaseCommand):
    help = "Load airports from CSV file into the database"

    def handle(self, *args, **options):
        with open("dataset/airports.csv", mode="r") as file:
            reader = csv.DictReader(file)
            airports = []
            for row in reader:
                airports.append(
                    Airport(
                        name=row["name"],
                        iata=row["iata"],
                        icao=row["icao"],
                        city=row["city"],
                        country=row["country"],
                        latitude=row["latitude"],
                        longitude=row["longitude"],
                    )
                )
            Airport.objects.all().delete()
            Airport.objects.bulk_create(airports)
        self.stdout.write(self.style.SUCCESS("Successfully loaded airports"))
