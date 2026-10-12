graph = {  # adjacency list
    "Alice": ["Bob"],
    "Bob": ["Alice", "Charlie", "Diana"],
    "Charlie": ["Bob", "Elliot"],
    "Diana": ["Bob", "Elliot"],
    "Elliot": ["Charlie", "Diana"],
}

def is_complete(graph):
    """Check whether a graph is complete.

    Takes a graph as a dictionary of adjacency lists
    and checks whether all nodes are connected to
    all other nodes.

    Returns a Boolean.
    """
    nodes = set(graph.keys())
    for node, neighbours in graph.items():
        if set(neighbours) != nodes - node:
            return False
    return True

def make_complete_graph(node_names):
    """Produce a complete graph with the given node names.

    Take a list of node names (e.g., ["A", "B", "C"]) and
    returns a dictionary of adjacency lists that represents
    a complete graph with the nodes you specify.

    (is_complete(make_complete_graph(...)) -> True)
    """