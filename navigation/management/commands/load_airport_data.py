# management/commands/load_airport_data.py
import csv
import pickle

import networkx as nx
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Load airport and route data from CSV files and create a graph"

    def handle(self, *args, **options):
        G = nx.DiGraph()

        # Load airports
        with open("dataset/airports.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    latitude = float(row["latitude"])
                    longitude = float(row["longitude"])
                except ValueError:
                    print(row)
                    print(
                        f"Error converting latitude or longitude for airport with IATA code '{row['iata']}'"
                    )
                    continue

                G.add_node(
                    row["iata"],
                    name=row["name"],
                    latitude=latitude,
                    longitude=longitude,
                    iata=row["iata"],
                    icao=row["icao"],
                )

        # Load routes and build the graph
        with open("dataset/routes.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                source = row["source_code"]
                destination = row["dest_code"]
                if source in G and destination in G:
                    lat1, lon1 = (
                        G.nodes[source]["latitude"],
                        G.nodes[source]["longitude"],
                    )
                    lat2, lon2 = (
                        G.nodes[destination]["latitude"],
                        G.nodes[destination]["longitude"],
                    )
                    distance = self.calculate_distance(lat1, lon1, lat2, lon2)
                    G.add_edge(source, destination, weight=distance)

        # Save the graph to a file for later use
        # nx.write_gpickle(G, 'flight_navigation/dataset/graph.gpickle')
        with open("dataset/graph.gpickle", "wb") as f:
            pickle.dump(G, f)

        self.stdout.write(self.style.SUCCESS("Graph created and saved successfully."))

    def calculate_distance(self, lat1, lon1, lat2, lon2):
        from math import atan2, cos, radians, sin, sqrt

        R = 6371.0  # Earth radius in km

        dlon = radians(lon2 - lon1)
        dlat = radians(lat2 - lat1)

        a = (
            sin(dlat / 2) ** 2
            + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
        )
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        return round(distance, 2)
