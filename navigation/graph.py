# This File is not used
class Edge:
    """
    Represents an edge in a graph data structure.
    """

    def __init__(self, src, dest, label="", weight=0.0):
        """
        Initializes an Edge object.

        Args:
          src (str): The source vertex of the edge.
          dest (str): The destination vertex of the edge.
          label (str, optional): A label associated with the edge. Defaults to "".
          weight (float, optional): A weight associated with the edge. Defaults to 0.0.
        """
        self.src = src
        self.dest = dest
        self.edge_label = label
        self.weight = weight

    def __str__(self):
        """
        Returns a string representation of the edge.

        Returns:
          str: A string representation of the edge including source, destination, weight, and label.
        """
        return f"Airport 1: {self.src} | Airport 2: {self.dest} | Weight: {self.weight} | Edge Label: {self.edge_label}"

    def __lt__(self, other):
        """
        Compares two Edge objects based on their weights.

        Args:
          other (Edge): Another Edge object to compare with.

        Returns:
          bool: True if the calling object's weight is less than the other object's weight, False otherwise.
        """
        return self.weight < other.weight

    def __eq__(self, other):
        """
        Compares two Edge objects based on their source and destination vertices.

        Args:
          other (Edge): Another Edge object to compare with.

        Returns:
          bool: True if the source and destination of both objects are equal, False otherwise.
        """
        return self.src == other.src and self.dest == other.dest


import math
from typing import Dict, List, Tuple

Vertex = str


class Edge:
    def __init__(
        self, src: Vertex, dest: Vertex, weight: float = 0, edge_label: str = ""
    ):
        self.src = src
        self.dest = dest
        self.edge_label = edge_label
        self.weight = weight

    def edge_as_string(self) -> str:
        return f"Airport 1: {self.src} | Airport 2: {self.dest} | Weight: {self.weight} | Edge Label: {self.edge_label}"

    def __lt__(self, other) -> bool:
        return self.weight < other.weight

    def __eq__(self, other) -> bool:
        return self.src == other.src and self.dest == other.dest


class Graph:
    def __init__(self, weighted: bool, directed: bool = False):
        self.adjacency_matrix: List[List[Tuple[float, str]]] = []
        self.ver_index: List[Vertex] = []
        self.weighted = weighted
        self.directed = directed

    def __init__(self, airport_data, route_data):
        self.weighted = True
        self.directed = True
        self.adjacency_matrix = []
        self.ver_index = []
        self.empty_edges = []
        routes = route_data.getdata()

        for route in routes:
            src_details = airport_data.getNameLatLong(route.source_id)
            dst_details = airport_data.getNameLatLong(route.dest_id)
            src = src_details[0]
            dst = dst_details[0]

            if not self.vertex_exists(src):
                self.insert_vertex(src)

            if not self.vertex_exists(dst):
                self.insert_vertex(dst)

            dist = self.distance(
                src_details[1][0],
                src_details[1][1],
                dst_details[1][0],
                dst_details[1][1],
            )
            src_idx = self.get_vertex_idx(src)
            dst_idx = self.get_vertex_idx(dst)

            if not self.insert_edge(src, dst, dist, route.airline_code):
                if self.adjacency_matrix[dst_idx][src_idx][0] < 0:
                    self.adjacency_matrix[dst_idx][src_idx] = (
                        self.adjacency_matrix[dst_idx][src_idx][0] * -1,
                        self.adjacency_matrix[dst_idx][src_idx][1]
                        + " + "
                        + route.airline_code,
                    )
                else:
                    self.adjacency_matrix[src_idx][dst_idx] = (
                        self.adjacency_matrix[src_idx][dst_idx][0] * -1,
                        self.adjacency_matrix[src_idx][dst_idx][1]
                        + " + "
                        + route.airline_code,
                    )

    def get_adjacent_dir(self, v: Vertex, dir: int) -> List[Vertex]:
        idx = self.get_vertex_idx(v)
        if idx == -1:
            return []

        return [
            self.ver_index[i]
            for i in range(len(self.ver_index))
            if (dir == 1 and self.adjacency_matrix[idx][i][0] > 0)
            or (
                dir == -1
                and (
                    self.adjacency_matrix[idx][i][0] < 0
                    or (
                        self.adjacency_matrix[i][idx][0] > 0
                        and self.adjacency_matrix[idx][i][0] > 0
                    )
                )
            )
            or (dir == 0 and self.adjacency_matrix[idx][i][0] != 0)
        ]

    def get_vertices(self) -> List[Vertex]:
        return self.ver_index[:]

    def get_edges(self) -> List[Edge]:
        return [
            self.get_edge(self.ver_index[i], self.ver_index[j])
            for i in range(len(self.ver_index))
            for j in range(len(self.ver_index))
            if self.adjacency_matrix[i][j][0] > 0
        ]

    def vertex_exists(self, v: Vertex) -> bool:
        return self.get_vertex_idx(v) != -1

    def edge_exists(self, source: Vertex, destination: Vertex) -> bool:
        return (
            self.adjacency_matrix[self.get_vertex_idx(source)][
                self.get_vertex_idx(destination)
            ][0]
            != 0
        )

    def set_edge_label(self, source: Vertex, destination: Vertex, label: str):
        self.adjacency_matrix[self.get_vertex_idx(source)][
            self.get_vertex_idx(destination)
        ] = (
            self.adjacency_matrix[self.get_vertex_idx(source)][
                self.get_vertex_idx(destination)
            ][0],
            label,
        )

    def get_edge_label(self, source: Vertex, destination: Vertex) -> str:
        return self.adjacency_matrix[self.get_vertex_idx(source)][
            self.get_vertex_idx(destination)
        ][1]

    def get_edge_weight(self, source: Vertex, destination: Vertex) -> float:
        return self.adjacency_matrix[self.get_vertex_idx(source)][
            self.get_vertex_idx(destination)
        ][0]

    def insert_vertex(self, v: Vertex):
        self.ver_index.append(v)
        for row in self.adjacency_matrix:
            row.append((0, ""))
        self.adjacency_matrix.append([(0, "") for _ in range(len(self.ver_index))])

    def get_vertex_idx(self, x: Vertex) -> int:
        return self.ver_index.index(x) if x in self.ver_index else -1

    def remove_vertex(self, v: Vertex) -> Vertex:
        if v not in self.ver_index:
            return ""

        idx = self.get_vertex_idx(v)
        self.adjacency_matrix.pop(idx)
        for row in self.adjacency_matrix:
            row.pop(idx)
        self.ver_index.pop(idx)
        return v

    def insert_edge(
        self, source: Vertex, destination: Vertex, weight: float, label: str
    ) -> bool:
        src_idx, dst_idx = self.get_vertex_idx(source), self.get_vertex_idx(destination)
        if self.adjacency_matrix[src_idx][dst_idx][0] != 0:
            return False

        self.adjacency_matrix[src_idx][dst_idx] = (weight, label)
        if self.directed:
            self.adjacency_matrix[dst_idx][src_idx] = (-weight, label)

        return True

    def get_edge(self, source: Vertex, destination: Vertex) -> Edge:
        src_idx, dst_idx = self.get_vertex_idx(source), self.get_vertex_idx(destination)
        if self.adjacency_matrix[src_idx][dst_idx][0] == 0:
            return Edge("", "")

        weight, label = self.adjacency_matrix[src_idx][dst_idx]
        return Edge(source, destination, weight, label)

    def remove_edge(self, source: Vertex, destination: Vertex) -> Edge:
        src_idx, dst_idx = self.get_vertex_idx(source), self.get_vertex_idx(destination)
        if self.adjacency_matrix[src_idx][dst_idx][0] == 0:
            return Edge("", "")

        weight, label = self.adjacency_matrix[src_idx][dst_idx]
        self.adjacency_matrix[src_idx][dst_idx] = (0, "")
        if self.directed:
            self.adjacency_matrix[dst_idx][src_idx] = (0, "")

        return Edge(source, destination, weight, label)

    def is_directed(self) -> bool:
        return self.directed

    def clear(self):
        self.adjacency_matrix.clear()
        self.ver_index.clear()

    def distance(self, lat1, lon1, lat2, lon2):
        R = 6371  # Radius of the Earth in km
        dLat = math.radians(lat2 - lat1)
        dLon = math.radians(lon2 - lon1)
        a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(
            math.radians(lat1)
        ) * math.cos(math.radians(lat2)) * math.sin(dLon / 2) * math.sin(dLon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    def shortest_path(self, source: Vertex, destination: Vertex) -> List[Edge]:
        # Placeholder for shortest path algorithm (e.g., Dijkstra's algorithm)
        pass
