# This File is not used
from math import atan2, cos, radians, sin, sqrt

import networkx as nx
import pandas as pd

# Load airport data
airport_df = pd.read_csv("airport.csv")
# Load route data
route_df = pd.read_csv("routes.csv")

# Create a graph
G = nx.DiGraph()

# Add nodes (airports)
for index, row in airport_df.iterrows():
    G.add_node(
        row["airport_code"],
        name=row["airport_name"],
        pos=(row["latitude"], row["longitude"]),
    )


# Function to calculate the Haversine distance between two points given their latitude and longitude
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


# Add edges (routes) with distances as weights
for index, row in route_df.iterrows():
    source_airport = row["source_airport_code"]
    destination_airport = row["destination_airport_code"]
    if source_airport in G.nodes and destination_airport in G.nodes:
        source_pos = G.nodes[source_airport]["pos"]
        destination_pos = G.nodes[destination_airport]["pos"]
        distance = haversine(
            source_pos[0], source_pos[1], destination_pos[0], destination_pos[1]
        )
        G.add_edge(source_airport, destination_airport, weight=distance)


# Function to find the shortest path between two airports
def find_shortest_path(graph, source, destination):
    try:
        shortest_path = nx.shortest_path(
            graph, source=source, target=destination, weight="weight"
        )
        shortest_distance = nx.shortest_path_length(
            graph, source=source, target=destination, weight="weight"
        )
        return shortest_path, shortest_distance
    except nx.NetworkXNoPath:
        return None, float("inf")


# Example usage
source_airport = "JFK"  # Replace with your source airport code
destination_airport = "LAX"  # Replace with your destination airport code

shortest_path, shortest_distance = find_shortest_path(
    G, source_airport, destination_airport
)
if shortest_path:
    print(
        f"The shortest path from {source_airport} to {destination_airport} is: {' -> '.join(shortest_path)}"
    )
    print(f"The total distance is: {shortest_distance:.2f} km")
else:
    print(f"No path found between {source_airport} and {destination_airport}")
