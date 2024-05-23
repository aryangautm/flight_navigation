import json
import logging
import os
import pickle

import networkx as nx
from django.core.exceptions import ObjectDoesNotExist
from django.core.management import call_command
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Airport, Route

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
# You can specify different handlers for different log levels
error_handler = logging.FileHandler("error.log")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)
logging.getLogger().addHandler(error_handler)


class ShortestPathView(APIView):
    def get(self, request):
        source_code = request.GET.get("source")
        dest_code = request.GET.get("destination")

        try:
            source_airport = Airport.objects.get(iata=source_code)
            dest_airport = Airport.objects.get(iata=dest_code)
            existing_route = Route.objects.get(
                source=source_airport, destination=dest_airport
            )
            return Response(
                {
                    "path": json.loads(existing_route.path),
                    "distance": existing_route.distance,
                }
            )
        except ObjectDoesNotExist:
            logging.info("Finding the best route...")
            pass

        try:
            with open("dataset/graph.gpickle", "rb") as f:
                G = pickle.load(f)
        except FileNotFoundError:
            logging.error("Error: Graph not found. Trying to load airport data...")
            # Call the management command to load airport data
            call_command("load_airport_data")
            # Now try to load the graph again
            try:
                with open("dataset/graph.gpickle", "rb") as f:
                    G = pickle.load(f)
            except FileNotFoundError:
                logging.error("Error: Graph not found even after loading airport data.")
                return Response({"error": "Graph not found"}, status=500)

        try:
            path = nx.shortest_path(
                G, source=source_code, target=dest_code, weight="weight"
            )
            distance = nx.shortest_path_length(
                G, source=source_code, target=dest_code, weight="weight"
            )

            for iata in path:
                if not Airport.objects.filter(iata=iata).exists():
                    node_data = G.nodes[iata]
                    Airport.objects.create(
                        iata=node_data["iata"],
                        icao=node_data["icao"],
                        name=node_data["name"],
                        latitude=node_data["latitude"],
                        longitude=node_data["longitude"],
                    )

            source_airport = get_object_or_404(Airport, iata=source_code)
            dest_airport = get_object_or_404(Airport, iata=dest_code)

            route, created = Route.objects.get_or_create(
                source=source_airport,
                destination=dest_airport,
                defaults={"path": json.dumps(path), "distance": distance},
            )
            return Response({"path": path, "distance": distance})
        except nx.NetworkXNoPath:
            return Response(
                {"error": "No path found between the specified airports."}, status=404
            )
        except Exception as e:
            logging.error(f"Error: {str(e)}")
            return Response({"error": str(e)}, status=500)
