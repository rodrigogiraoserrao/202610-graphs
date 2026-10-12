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

# This version doesn't handle cycles very well 🤪
# Exercise: how do you fix it?
def count_paths(graph, start, target):
    """Count the number of ways in which you can go from
    `start` to `target`."""
    if start == target:
        return 1

    total = 0
    for neighbour in graph[start]:
        total += count_paths(graph, neighbour, target)
    return total

print(count_paths(graph, "A", "H"))
