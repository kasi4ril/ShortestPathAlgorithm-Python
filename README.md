# 🗺️ Dijkstra's Shortest Path Algorithm

> A clean, well-commented Python implementation of **Dijkstra's Algorithm** using an adjacency matrix — ideal for learning graph traversal and shortest-path problem solving.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Algorithm Explained](#algorithm-explained)
- [Graph Structure](#graph-structure)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Example Output](#example-output)
- [Complexity Analysis](#complexity-analysis)
- [Key Concepts](#key-concepts)
- [Improvements & Extensions](#improvements--extensions)
- [Author](#author)

---

## Overview

This project implements **Dijkstra's Shortest Path Algorithm** — one of the most fundamental and widely-used algorithms in computer science. It is used to find the minimum-cost path between nodes in a weighted graph where all edge weights are non-negative.

**Real-world applications include:**
- 🌐 Internet routing protocols (OSPF)
- 🗺️ GPS and navigation systems (Google Maps, Waze)
- 🎮 Game AI pathfinding
- 📦 Logistics and delivery route optimisation
- 🔌 Network topology planning

---

## Algorithm Explained

Dijkstra's algorithm works by maintaining a set of **tentative distances** from the source node to every other node. It iteratively:

1. **Selects** the unvisited node with the smallest known distance.
2. **Settles** (marks) it as permanently visited.
3. **Relaxes** all its outgoing edges — updating a neighbour's distance if a shorter path through the current node is found.

This greedy strategy guarantees the **optimal shortest path** when all edge weights are non-negative.

```
┌─────────────────────────────────────────────────────────┐
│  DIJKSTRA'S ALGORITHM — PSEUDOCODE                      │
│                                                         │
│  1. Set dist[source] = 0, all others = ∞               │
│  2. Mark all nodes as unvisited                         │
│  3. Repeat until all reachable nodes are visited:       │
│     a. Pick unvisited node U with smallest dist[U]      │
│     b. For each unvisited neighbour V of U:             │
│        if dist[U] + weight(U,V) < dist[V]:             │
│           dist[V] = dist[U] + weight(U,V)              │
│           path[V] = path[U] + [V]                       │
│     c. Mark U as visited                                │
└─────────────────────────────────────────────────────────┘
```

---

## Graph Structure

The graph is represented as a **6-node weighted, undirected adjacency matrix**:

```
       0 ──5── 1 ──2── 5
       │        │       │
       3        1       3
       │        │       │
       2 ──1── 3 ──9── 4
       │
       5
       │
       4
```

| Node | Connected To (weight)              |
|------|------------------------------------|
| 0    | 1 (5), 2 (3), 4 (11)              |
| 1    | 0 (5), 2 (1), 5 (2)               |
| 2    | 0 (3), 1 (1), 3 (1), 4 (5)        |
| 3    | 2 (1), 4 (9), 5 (3)               |
| 4    | 0 (11), 2 (5), 3 (9)              |
| 5    | 1 (2), 3 (3)                       |

### Adjacency Matrix

```
       0     1     2     3     4     5
  0  [ 0,    5,    3,  INF,   11,  INF ]
  1  [ 5,    0,    1,  INF,  INF,    2 ]
  2  [ 3,    1,    0,    1,    5,  INF ]
  3  [INF,  INF,   1,    0,    9,    3 ]
  4  [ 11,  INF,   5,    9,    0,  INF ]
  5  [INF,   2,  INF,    3,  INF,    0 ]
```

> `INF` = no direct edge between those two nodes.

---

## Project Structure

```
Desktop/
├── shortestpathalgorithm.py   # Core algorithm implementation
└── README.md                  # Project documentation (this file)
```

---

## Getting Started

### Prerequisites

- Python **3.6+** (uses f-strings and generator expressions)
- No external libraries required — pure Python standard library

### Run with default settings (node 0 → node 5)

```bash
python shortestpathalgorithm.py
```

### Import and use in your own script

```python
from shortestpathalgorithm import shortest_path, adj_matrix

# Find shortest path from node 0 to node 5
distances, paths = shortest_path(adj_matrix, start_node=0, target_node=5)

# Find shortest paths from node 0 to ALL other nodes
distances, paths = shortest_path(adj_matrix, start_node=0)

# Access results programmatically
print(f"Distance to node 3: {distances[3]}")
print(f"Path to node 3: {paths[3]}")
```

### Function Signature

```python
def shortest_path(matrix, start_node, target_node=None):
    """
    Parameters
    ----------
    matrix      : list[list[float]]  — Adjacency matrix of the graph
    start_node  : int                — Source node index (0-based)
    target_node : int | None         — Target node (None = all nodes)

    Returns
    -------
    distances : list[float]          — Shortest distance to each node
    paths     : list[list[int]]      — Ordered node indices for each path
    """
```

---

## Example Output

Running `shortest_path(adj_matrix, start_node=0, target_node=5)`:

```
0 → 5 | Distance: 7 | Path: 0 -> 2 -> 1 -> 5
```

Running `shortest_path(adj_matrix, start_node=0)`:

```
0 → 1 | Distance: 4  | Path: 0 -> 2 -> 1
0 → 2 | Distance: 3  | Path: 0 -> 2
0 → 3 | Distance: 4  | Path: 0 -> 2 -> 3
0 → 4 | Distance: 8  | Path: 0 -> 2 -> 4
0 → 5 | Distance: 7  | Path: 0 -> 2 -> 1 -> 5
```

---

## Complexity Analysis

| Metric            | Value      | Notes                                       |
|-------------------|------------|---------------------------------------------|
| **Time**          | O(V²)      | V = number of nodes; linear scan per step   |
| **Space**         | O(V)       | Distance array + visited array + paths      |
| **Best for**      | Dense graphs | Adjacency matrix suits high edge-to-node ratio |
| **Not ideal for** | Sparse graphs | Use adjacency list + min-heap → O((V+E) log V) |

> **💡 Pro Tip:** For very large sparse graphs (e.g. road networks), replace the linear scan with a **priority queue** (`heapq` in Python) to achieve O((V + E) log V) performance.

---

## Key Concepts

| Concept              | Explanation                                                          |
|----------------------|----------------------------------------------------------------------|
| **Greedy algorithm** | Always picks the locally optimal choice (min distance node)          |
| **Relaxation**       | Updating a distance if a shorter path through a node is found        |
| **Settled node**     | A node whose shortest distance is permanently finalised              |
| **INF sentinel**     | Represents "no known path yet" or "no direct edge"                   |
| **Adjacency matrix** | 2D grid where `matrix[i][j]` = weight of edge between node i and j  |

---

## Improvements & Extensions

Here are meaningful extensions you can try as learning exercises:

- [ ] **Priority Queue optimisation** — Use `heapq` to reduce time complexity for sparse graphs
- [ ] **Adjacency List** — Replace the matrix with a dict-of-lists for memory efficiency
- [ ] **Bidirectional Dijkstra** — Search from both source and target simultaneously
- [ ] **Visualisation** — Use `networkx` + `matplotlib` to draw the graph and highlight paths
- [ ] **Negative edge handling** — Explore the Bellman-Ford algorithm as a comparison
- [ ] **Unit tests** — Write `pytest` test cases to validate algorithm correctness

---

## Author

**Student** — October 2026  
*Reviewed and mentored with professional inline documentation.*

---

> **📚 Further Reading**
> - [Dijkstra's Algorithm — Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
> - [Graph Theory Fundamentals](https://en.wikipedia.org/wiki/Graph_theory)
> - [Python `heapq` module docs](https://docs.python.org/3/library/heapq.html)

