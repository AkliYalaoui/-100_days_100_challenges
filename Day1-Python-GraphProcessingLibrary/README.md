# Day 1 Challenge: Build a Lightweight Python Library for Graph Processing

## **Objective**
Create a lightweight Python library for basic graph processing. The library should allow users to easily create, manipulate, and analyze graphs. Focus on clean code, modular design, and performance optimization.

---

## **Requirements**

### **1. Core Features**
1. **Graph Representation**:
   - Support both directed and undirected graphs.
   - Allow users to represent graphs using adjacency lists.
   - Include methods to:
     - Add/remove nodes.
     - Add/remove edges.
     - Check if an edge exists between two nodes.

2. **Graph Traversals**:
   - Implement:
     - Breadth-First Search (BFS).
     - Depth-First Search (DFS).
   - Allow the user to specify the starting node for traversals.

3. **Basic Algorithms**:
   - **Shortest Path**:
     - Implement Dijkstra’s algorithm for weighted graphs.
   - **Connected Components**:
     - Identify all connected components in an undirected graph.

4. **Utility Functions**:
   - Get all neighbors of a node.
   - Check if the graph is cyclic.
     - Detect both directed and undirected graph cycles.
   - Get the degree of a node (in-degree and out-degree for directed graphs).

---

## **How to Use**

### **1. Create a Graph**
You can create a graph by specifying whether it's directed or not:

```python
from src.graph import Graph

# Create a directed graph
g = Graph(directed=True)

# Create an undirected graph
g = Graph(directed=False)

# Adding nodes
g.add_node("A")
g.add_node("B")

# Adding an edge with a weight
g.add_edge("A", "B", weight=5)


# Perform DFS from node A
print("DFS:", g.dfs("A"))

# Perform BFS from node A
print("BFS:", g.bfs("A"))

# Run Dijkstra’s algorithm to find the shortest path from A to B
print("Shortest Path from A to B:", g.djikstra("A", "B"))

# Check if the graph is cyclic
print("Is Cyclic:", g.is_cyclic())

# Get the neighbors of node A
print("Neighbors of A:", g.get_neighbors("A"))

# Get the degree of node A
print("Degree of A:", g.get_degree("A"))

