"""
shortest_path_algorithm.py
==========================
Implementation of Dijkstra's Shortest Path Algorithm using an adjacency matrix.

Author  : Student
Reviewer: Code Mentor (20 yrs experience)
Date    : October 2026

Algorithm Overview
------------------
Dijkstra's algorithm finds the shortest path between a source node and one or
all other nodes in a weighted, non-negative graph.  It uses a greedy strategy:
at every iteration it picks the unvisited node with the smallest known
tentative distance, "locks it in" (marks it visited), then relaxes all of its
neighbouring edges.

Time Complexity  : O(V²)  — suitable for dense graphs represented as matrices
Space Complexity : O(V)   — distance and visited arrays scale linearly with V
"""

# ---------------------------------------------------------------------------
# Sentinel value used to represent "no direct edge / infinite distance"
# Using float('inf') instead of a large magic number (e.g. 9999) makes
# comparisons and arithmetic safe and semantically clear.
# ---------------------------------------------------------------------------
INF = float('inf')

# ---------------------------------------------------------------------------
# Adjacency Matrix — 6-node weighted, undirected graph
#
# Reading the matrix:  adj_matrix[i][j] = weight of edge between node i and j
#   • 0   → a node has zero distance to itself (diagonal)
#   • INF → no direct edge exists between those two nodes
#
# Visual representation of the graph:
#
#       (0)---5---(1)---2---(5)
#        |  \      |         |
#        3   11    1         3
#        |      \  |         |
#       (2)---1---(3)---9---(4)
#        |
#        5
#        |
#       (4)
#
# ---------------------------------------------------------------------------
adj_matrix = [
    #  0     1     2     3     4     5   ← destination node
    [  0,    5,    3,  INF,   11,  INF],  # source node 0
    [  5,    0,    1,  INF,  INF,    2],  # source node 1
    [  3,    1,    0,    1,    5,  INF],  # source node 2
    [INF,  INF,    1,    0,    9,    3],  # source node 3
    [ 11,  INF,    5,    9,    0,  INF],  # source node 4
    [INF,    2,  INF,    3,  INF,    0],  # source node 5
]


def shortest_path(matrix, start_node, target_node=None):
    """
    Compute the shortest path(s) from *start_node* to every other node
    (or to a specific *target_node*) using Dijkstra's algorithm.

    Parameters
    ----------
    matrix      : list[list[float]]
        Square adjacency matrix.  matrix[i][j] is the edge weight between
        node i and node j, or INF when no direct edge exists.
    start_node  : int
        Index of the source node (0-based).
    target_node : int | None, optional
        If provided, only the path to this specific node is printed.
        If None (default), paths to *all* reachable nodes are printed.

    Returns
    -------
    distances : list[float]
        distances[i] holds the shortest total distance from start_node to i.
    paths     : list[list[int]]
        paths[i] holds the ordered sequence of node indices that make up the
        shortest route from start_node to node i.
    """

    n = len(matrix)  # total number of nodes in the graph

    # -----------------------------------------------------------------------
    # Initialisation
    # All nodes start at infinite distance; the source is 0 away from itself.
    # -----------------------------------------------------------------------
    distances = [INF] * n       # tentative shortest distances from start_node
    distances[start_node] = 0   # cost to reach the source node is always 0

    # paths[i] tracks the full route taken to reach node i.
    # Initialised so each node's path contains only itself (its own index).
    paths = [[node_no] for node_no in range(n)]

    # Boolean array to record whether a node's shortest distance has been
    # finalised (True = permanently settled, False = still tentative).
    visited = [False] * n

    # -----------------------------------------------------------------------
    # Main Dijkstra loop — runs at most V times (once per node)
    # -----------------------------------------------------------------------
    for _ in range(n):

        # --- Step 1: Pick the unvisited node with the smallest tentative distance ---
        min_distance = INF
        current = -1  # will hold the index of the chosen node (-1 = none found)

        for node_no in range(n):
            # Only consider nodes that have not been permanently settled yet
            if not visited[node_no] and distances[node_no] < min_distance:
                min_distance = distances[node_no]
                current = node_no

        # If no reachable unvisited node was found, the remaining nodes are
        # disconnected from start_node — safe to terminate early.
        if current == -1:
            break

        # Permanently settle the chosen node; its distance is now optimal.
        visited[current] = True

        # --- Step 2: Relax (update) all edges leaving the current node ---
        for node_no in range(n):
            distance = matrix[current][node_no]  # edge weight to this neighbour

            # Skip non-existent edges and already-settled neighbours
            if distance != INF and not visited[node_no]:
                new_distance = distances[current] + distance  # candidate shorter path

                # If routing through 'current' is cheaper, update records
                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance
                    # Extend the current node's path with this neighbour
                    paths[node_no] = paths[current] + [node_no]

    # -----------------------------------------------------------------------
    # Output results
    # Determine which target node(s) to report on.
    # -----------------------------------------------------------------------
    targets = [target_node] if target_node is not None else range(n)

    for node_no in targets:
        # Skip the source node itself and nodes that are unreachable
        if node_no == start_node or distances[node_no] == INF:
            continue

        # Build a human-readable path string: "0 -> 2 -> 3 -> 5"
        # NOTE: the inner variable is renamed to 'step' to avoid shadowing
        # the built-in 'n' (node count) used above — a subtle but important
        # readability and maintenance concern.
        string_path = (str(step) for step in paths[node_no])
        path = ' -> '.join(string_path)

        print(f'\n{start_node} → {node_no} | Distance: {distances[node_no]} | Path: {path}')

    return distances, paths


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    # Find and display the shortest path from node 0 to node 5
    shortest_path(adj_matrix, start_node=0, target_node=5)

# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    # Find and display the shortest path from node 0 to node 5
    shortest_path(adj_matrix, start_node=0, target_node=5)