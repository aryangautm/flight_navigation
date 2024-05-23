# This File is not used

from heapq import heappop, heappush

import requests


def heuristic(node, end):
    # Example heuristic: Euclidean distance
    return ((node[0] - end[0]) ** 2 + (node[1] - end[1]) ** 2) ** 0.5


def a_star(graph, start, end):
    open_list = []
    heappush(open_list, (0, start))
    came_from = {}
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0
    f_score = {node: float("inf") for node in graph}
    f_score[start] = heuristic(start, end)

    while open_list:
        _, current = heappop(open_list)
        if current == end:
            return reconstruct_path(came_from, current)

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end)
                heappush(open_list, (f_score[neighbor], neighbor))

    return []


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


def calculate_score(distance, max_distance, risk, max_risk, alpha=0.5, beta=0.5):
    distance_score = distance / max_distance
    risk_score = risk / max_risk
    total_score = alpha * distance_score + beta * risk_score
    return total_score


def fetch_real_time_data(weather_api_url, flight_api_url):
    weather_response = requests.get(weather_api_url)
    flight_response = requests.get(flight_api_url)
    weather_data = weather_response.json()
    flight_data = flight_response.json()

    return weather_data, flight_data


def suggest_optimal_path(paths, alpha=0.4, beta=0.6):
    max_distance = max(path["distance"] for path in paths)
    max_risk = max(path["risk"] for path in paths)

    for path in paths:
        path["score"] = calculate_score(
            path["distance"], max_distance, path["risk"], max_risk, alpha, beta
        )

    # optimal_path = min(paths, key=lambda x: x['


def fetch_real_time_data(weather_api_url, flight_api_url):
    weather_response = requests.get(weather_api_url)
    flight_response = requests.get(flight_api_url)
    weather_data = weather_response.json()
    flight_data = flight_response.json()

    # Process and update data in the database
    update_weather_data(weather_data)
    update_flight_status(flight_data)


def update_weather_data(data):
    # Update weather data in the database
    pass


def update_flight_status(data):
    # Update flight status in the database
    pass


from heapq import heappop, heappush


def a_star(graph, start, end):
    open_list = []
    heappush(open_list, (0, start))
    came_from = {}
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0
    f_score = {node: float("inf") for node in graph}
    f_score[start] = heuristic(start, end)

    while open_list:
        _, current = heappop(open_list)
        if current == end:
            return reconstruct_path(came_from, current)

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end)
                heappush(open_list, (f_score[neighbor], neighbor))

    return []


def heuristic(node, end):
    # Example heuristic: Euclidean distance
    return ((node[0] - end[0]) ** 2 + (node[1] - end[1]) ** 2) ** 0.5


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


def calculate_score(distance, max_distance, risk, max_risk, alpha=0.5, beta=0.5):
    distance_score = distance / max_distance
    risk_score = risk / max_risk
    total_score = alpha * distance_score + beta * risk_score
    return total_score


def suggest_optimal_path(paths, alpha=0.4, beta=0.6):
    max_distance = max(path["distance"] for path in paths)
    max_risk = max(path["risk"] for path in paths)

    for path in paths:
        path["score"] = calculate_score(
            path["distance"], max_distance, path["risk"], max_risk, alpha, beta
        )

    optimal_path = min(paths, key=lambda x: x["score"])
    return optimal_path
