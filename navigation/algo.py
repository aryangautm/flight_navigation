import heapq
from itertools import islice

import networkx as nx


def yen_k_shortest_paths(G, source, target, k, weight="weight"):
    def dijkstra_path_length(G, source, target, weight):
        return nx.dijkstra_path_length(G, source, target, weight)

    if source not in G or target not in G:
        raise nx.NodeNotFound("Either source or target is not in G")

    paths = list(islice(nx.shortest_simple_paths(G, source, target, weight=weight), k))
    if len(paths) < k:
        raise nx.NetworkXNoPath(f"No path between {source} and {target}")

    shortest_paths = [paths[0]]
    potential_paths = []

    for _ in range(1, k):
        for i in range(len(shortest_paths[-1]) - 1):
            spur_node = shortest_paths[-1][i]
            root_path = shortest_paths[-1][: i + 1]

            removed_edges = []
            for path in shortest_paths:
                if len(path) > i and root_path == path[: i + 1]:
                    u = path[i]
                    v = path[i + 1]
                    if G.has_edge(u, v):
                        removed_edges.append((u, v, G[u][v][weight]))
                        G.remove_edge(u, v)

            try:
                spur_path = next(
                    islice(
                        nx.shortest_simple_paths(G, spur_node, target, weight=weight), 1
                    )
                )
                total_path = root_path[:-1] + spur_path
                potential_paths.append(
                    (dijkstra_path_length(G, source, target, weight), total_path)
                )
            except StopIteration:
                pass

            for u, v, w in removed_edges:
                G.add_edge(u, v, **{weight: w})

        if not potential_paths:
            break

        potential_paths.sort(key=lambda x: x[0])
        shortest_paths.append(potential_paths.pop(0)[1])

    return shortest_paths
