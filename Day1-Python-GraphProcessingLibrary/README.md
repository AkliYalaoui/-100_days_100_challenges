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
   - Shortest Path:
     - Implement Dijkstra’s algorithm for weighted graphs.
   - Connected Components:
     - Identify all connected components in an undirected graph.

4. **Utility Functions**:
   - Get all neighbors of a node.
   - Check if the graph is cyclic.
   - Get the degree of a node (in-degree and out-degree for directed graphs).

---

### **2. Additional Features (Optional, for Bonus)**
- **Graph Visualization**:
  - Provide a method to visualize the graph using libraries like `matplotlib` or `networkx`.

- **Weighted Graph Support**:
  - Extend the library to handle weighted edges.

- **Performance Optimization**:
  - Optimize the graph representation for large graphs (e.g., sparse graphs).

---

## **Usage Example**
Here’s an example of how the library should be used:

```python
from my_graph_lib import Graph

# Create a graph
g = Graph(directed=True)
g.add_node("A")
g.add_node("B")
g.add_edge("A", "B", weight=5)

# Traversals
print("DFS:", g.dfs("A"))
print("BFS:", g.bfs("A"))

# Algorithms
print("Shortest Path from A to B:", g.dijkstra("A", "B"))
print("Is Cyclic:", g.is_cyclic())

# Graph Info
print("Neighbors of A:", g.get_neighbors("A"))
print("Degree of A:", g.get_degree("A"))
