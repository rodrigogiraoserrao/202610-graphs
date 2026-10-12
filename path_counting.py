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

def count_paths(graph, start, target):
    """Count the number of ways in which you can go from
    `start` to `target`."""