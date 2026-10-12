graph = {
    "A": ["C", "D", "E"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["F", "G"],
    "E": ["G"],
    "F": ["G", "H"],
    "G": ["H"],
    "H": ["A"],
}

def can_reach(graph, start):
    """Return all the nodes you can get to from the starting point.
    
    Given the node `start`, go through the given graph and figure out
    all the nodes you can eventually get to.
    """
    to_visit = [start]
    visited = set()
    while to_visit:
        current_node = to_visit.pop()
        visited.add(current_node)
        for neighbour in graph[current_node]:
            if neighbour in visited:
                continue
            to_visit.append(neighbour)

    return visited

print(can_reach(graph, "A"))
