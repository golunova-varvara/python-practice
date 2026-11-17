def create_city_graph():
    """
    Create and return an undirected graph of cities.

    Returns:
        dict: network of cities and their direct road connections
    """
    graph = {
        "Moscow": ["Saint Petersburg", "Nizhny Novgorod"],
        "Saint Petersburg": ["Moscow", "Novgorod"],
        "Nizhny Novgorod": ["Moscow", "Kazan"],
        "Kazan": ["Nizhny Novgorod", "Yekaterinburg"],
        "Novgorod": ["Saint Petersburg"],
        "Yekaterinburg": ["Kazan"]
    }
    return graph


def count_vertices(graph):
    """
    Count the number of vertices (cities) in the graph.

    Args:
        graph (dict): graph of cities

    Returns:
        int: total number of cities
    """
    return len(graph)


def count_edges(graph):
    """
    Count the number of unique edges (roads) in an undirected graph.

    Args:
        graph (dict): graph of cities

    Returns:
        int: total number of unique roads
    """
    total = 0
    for city in graph:
        total += len(graph[city])
    return total // 2


cities_graph = create_city_graph()

print(cities_graph)
print(count_vertices(cities_graph))
print(count_edges(cities_graph))
