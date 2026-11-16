from collections import deque

def can_reach(graph, start, target):
    """
    Check if computer A can transfer data to computer B (directly or through other computers).

    Args:
        graph (dict): network graph
        start (str): computer A
        target (str): computer B

    Returns:
        bool: True if a path exists between them, otherwise False
    """

    if not isinstance(graph, dict) or not isinstance(start, str) or not isinstance(target, str):
        return False
    if start not in graph or target not in graph:
        return False
    
    queue = deque([start])
    visited = {start}
    
    while queue:
        current = queue.popleft()
        
        if current == target:
            return True
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)             
    return False

# Test
office_network = {
    "PC1": ["PC2", "PC3"],
    "PC2": ["PC1", "PC4"],
    "PC3": ["PC1", "PC5"],
    "PC4": ["PC2", "PC6"],
    "PC5": ["PC3"],
    "PC6": ["PC4"],
    "PC7": []  # isolated computer
}

print(can_reach(office_network, "PC1", "PC3"))  # True
print(can_reach(office_network, "PC3", "PC7"))  # False
print(can_reach(office_network, "PC8", "PC3"))  # False
print(can_reach(office_network, 1, "PC3"))  # False
