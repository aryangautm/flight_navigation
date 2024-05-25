import json
import logging
import pickle

import networkx as nx
from django.core.management import call_command
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .algo import yen_k_shortest_paths
from .models import Airport, Route
from .serializers import AirportSerializer

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

AVERAGE_SPEED_KMH = 900


class ShortestPathView(APIView):
    def get(self, request):
        source_code = request.GET.get("source")
        dest_code = request.GET.get("destination")
        print(source_code, dest_code)

        try:
            with open("dataset/graph.gpickle", "rb") as f:
                G = pickle.load(f)
        except FileNotFoundError:
            logging.error("Error: Graph not found. Trying to load airport data...")
            # Call the management command to load airport data
            call_command("load_network")
            # Now try to load the graph again
            try:
                with open("dataset/graph.gpickle", "rb") as f:
                    G = pickle.load(f)
            except FileNotFoundError:
                logging.error("Error: Graph not found even after loading airport data.")
                return Response({"error": "Graph not found"}, status=500)

        if source_code not in G or dest_code not in G:
            return Response(
                {"error": "Invalid airport code provided."},
                status=400,
            )
        try:
            paths = yen_k_shortest_paths(
                G, source_code, dest_code, k=5, weight="weight"
            )
            print(paths)
            response_paths = []

            for path in paths:
                response_route = {}
                total_distance = round(
                    sum(
                        G[path[i]][path[i + 1]]["weight"] for i in range(len(path) - 1)
                    ),
                    2,
                )
                time_taken = round(total_distance / AVERAGE_SPEED_KMH, 2)

                airports = []
                for iata in path:
                    node_data = G.nodes[iata]
                    defaults = {
                        "icao": node_data["icao"],
                        "name": node_data["name"],
                        "city": node_data["city"],
                        "country": node_data["country"],
                        "latitude": round(node_data["latitude"], 2),
                        "longitude": round(node_data["longitude"], 2),
                    }
                    airport, created = Airport.objects.update_or_create(
                        iata=node_data["iata"], defaults=defaults
                    )

                    airports.append(airport)

                response_route.update(
                    {
                        "destination": airports[-1].iata,
                        "destinationName": airports[-1].name,
                        "destinationCountryCode": "us",
                        "destinationCity": airports[-1].city,
                        "destinationCountryName": airports[-1].country,
                        "source": airports[0].iata,
                        "sourceName": airports[0].name,
                        "sourceCountryCode": "in",
                        "sourceCity": airports[0].city,
                        "sourceCountryName": airports[0].country,
                        "totalTime": time_taken,
                        "totalDistance": total_distance,
                        "avgFeasibility": "96.4%",
                        "totalEmissions": "23312 kg CO2",
                    }
                )
                response_route.update({"paths": []})
                a0_defaults = {
                    "airportCode": airports[0].iata,
                    "airportName": airports[0].name,
                    "cityName": airports[0].city,
                    "countryName": airports[0].country,
                    "time": 0,
                    "distance": 0,
                }
                response_route["paths"].append(a0_defaults)

                route, created = Route.objects.get_or_create(
                    source=airports[0],
                    destination=airports[-1],
                    defaults={
                        "path": json.dumps(path),
                        "distance": total_distance,
                        "duration": time_taken,
                    },
                )

                for i in range(len(path) - 1):
                    distance = round(G[path[i]][path[i + 1]]["weight"], 2)
                    time_duration = round((distance / AVERAGE_SPEED_KMH), 2)
                    Route.objects.get_or_create(
                        source=airports[i],
                        destination=airports[i + 1],
                        defaults={
                            "path": json.dumps([path[i], path[i + 1]]),
                            "distance": distance,
                            "duration": time_duration,
                        },
                    )

                    ai_defaults = {
                        "airportCode": airports[i + 1].iata,
                        "airportName": airports[i + 1].name,
                        "cityName": airports[i + 1].city,
                        "countryName": airports[i + 1].country,
                        "time": time_duration,
                        "distance": distance,
                    }
                    response_route["paths"].append(ai_defaults)

                response_paths.append(response_route)

            response = Response(response_paths, status=200)
            response["Access-Control-Allow-Origin"] = "*"
            response["Cross-Origin-Opener-Policy"] = "*"
            return response

        except nx.NetworkXNoPath:
            return Response(
                {"error": "No path found between the specified airports."}, status=404
            )
        except Exception as e:
            logging.error(f"Error: {str(e)}")
            return Response({"error": str(e)}, status=500)


class AirportDetailView(viewsets.ReadOnlyModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    lookup_field = "iata"

    def get_object(self):
        queryset = self.get_queryset()
        iata = self.kwargs.get("iata").upper()
        try:
            return queryset.get(iata=iata)
        except Airport.DoesNotExist:
            raise Http404("Airport not found")
