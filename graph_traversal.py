graph = {
    "A": ["C", "D", "E"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["F", "G"],
    "E": ["G"],
    "F": ["G", "H"],
    "G": ["H"],
    "H": [],
}

def can_reach(graph, start):
    """Return all the nodes you can get to from the starting point.
    
    Given the node `start`, go through the given graph and figure out
    all the nodes you can eventually get to.
    """
    ...