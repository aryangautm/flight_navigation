# aviation_data/route_planning.py
import heapq
from aviation_data.models import Flight, Airport, Scenario
from aviation_data.utils import get_weather_data
import math

def a_star_with_risks(start_airport, end_airport):
    # Priority queue for A* algorithm
    queue = []
    heapq.heappush(queue, (0, start_airport))
    distances = {start_airport: 0}
    previous_nodes = {start_airport: None}
    estimated_total_cost = {start_airport: heuristic(start_airport, end_airport)}

    while queue:
        current_cost, current_airport = heapq.heappop(queue)

        if current_airport == end_airport:
            break

        # Get neighboring airports and distances (simplified example)
        neighbors = get_neighbors(current_airport)
        for neighbor, distance in neighbors.items():
            weather_risk = get_weather_risk(neighbor)
            scenario_risk = get_scenario_risk(neighbor)
            total_risk = weather_risk + scenario_risk

            new_cost = distances[current_airport] + distance + total_risk

            if neighbor not in distances or new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                estimated_total_cost[neighbor] = new_cost + heuristic(neighbor, end_airport)
                previous_nodes[neighbor] = current_airport
                heapq.heappush(queue, (estimated_total_cost[neighbor], neighbor))

    return reconstruct_path(previous_nodes, start_airport, end_airport)

def heuristic(start, goal):
    # Use the Haversine formula to calculate the great-circle distance
    airport_coords = {
        'JFK': (40.6413, -73.7781),
        'LAX': (33.9416, -118.4085),
        # Add more airport coordinates as needed
    }
    
    lat1, lon1 = airport_coords[start]
    lat2, lon2 = airport_coords[goal]
    
    radius = 6371  # Earth radius in kilometers

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c

    return distance

''' This function will trace back from the end_airport to the start_airport using the previous
    nodes dictionary, building the path and then reversing it to present it in the correct order.'''
def reconstruct_path(previous_nodes, start_airport, end_airport):
    path = []
    current_airport = end_airport
    
    while current_airport is not None:
        path.append(current_airport)
        current_airport = previous_nodes[current_airport]

    path.reverse()  # Reverse the path to get it from start to end
    return path

# Re-use get_neighbors, get_weather_risk, get_scenario_risk from the previous implementation
def get_neighbors(airport):
    # Simplified function to get neighboring airports and distances
    # In practice, use real data from your database or API
    return {
        'LAX': 3000,  # Example distances in miles
        'ORD': 800,
        # Add more neighbors as needed
    }

def get_weather_risk(airport):
    # Use the get_weather_data function to determine weather risk at the airport
    weather_data = get_weather_data(airport)
    if weather_data['weather'][0]['main'] in ['Rain', 'Snow', 'Fog']:
        return 100  # Example risk value
    return 0

def get_scenario_risk(airport):
    # Determine scenario risk based on identified scenarios
    scenarios = Scenario.objects.filter(related_flights__departure_airport=airport)
    return len(scenarios) * 50  # Example risk calculation
