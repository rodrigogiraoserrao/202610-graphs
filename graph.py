graph_list_of_lists = [
    # A,    B,     C,     D,     E
    [False, True , False, False, False], # A
    [True , False, True , True , False], # B
    [False, True , False, False, True ], # C
    ...
]  # adjacency matrix

graph = {  # adjacency list
    "Alice": ["Bob"],
    "Bob": ["Alice", "Charlie", "Diana"],
    ...
}