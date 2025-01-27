import unittest
import numpy as np
from collections import deque
from src.graph import Graph


class TestGraph(unittest.TestCase):

    def setUp(self):
        """Create a graph instance for testing."""
        self.graph = Graph(directed=False)

    def test_add_node(self):
        """Test if nodes can be added correctly."""
        self.graph.add_node("A")
        self.assertIn("A", self.graph.data)
        self.assertEqual(self.graph.data["A"], [])

    def test_add_edge(self):
        """Test if edges are added correctly."""
        self.graph.add_edge("A", "B", 5)
        self.assertIn("B", [neighbor[0] for neighbor in self.graph.data["A"]])
        self.assertIn("A", [neighbor[0] for neighbor in self.graph.data["B"]])
        self.assertIn(("B", 5), self.graph.data["A"])
        self.assertIn(("A", 5), self.graph.data["B"])

    def test_get_neighbors(self):
        """Test if neighbors are retrieved correctly."""
        self.graph.add_edge("A", "B", 5)
        neighbors = self.graph.get_neighbors("A")
        self.assertEqual(neighbors, [("B", 5)])

    def test_dfs(self):
        """Test Depth-First Search (DFS) traversal."""
        self.graph.add_edge("A", "B", 5)
        self.graph.add_edge("B", "C", 3)
        self.graph.add_edge("A", "C", 1)

        traversal = self.graph.dfs("A")
        self.assertEqual(traversal, ["A", "B", "C"])

    def test_bfs(self):
        """Test Breadth-First Search (BFS) traversal."""
        self.graph.add_edge("A", "B", 5)
        self.graph.add_edge("B", "C", 3)
        self.graph.add_edge("A", "C", 1)

        traversal = self.graph.bfs("A")
        self.assertEqual(traversal, ["A", "B", "C"])

    def test_djikstra(self):
        """Test Dijkstra's algorithm for shortest path."""
        self.graph.add_edge("A", "B", 5)
        self.graph.add_edge("B", "C", 3)
        self.graph.add_edge("A", "C", 1)

        path, distance = self.graph.djikstra("A", "C")
        self.assertEqual(path, ["A", "C"])
        self.assertEqual(distance, 1)

        path, distance = self.graph.djikstra("A", "B")
        self.assertEqual(path, ["A", "C" ,"B"])
        self.assertEqual(distance, 4)

    def test_is_cyclic_undirected(self):
        """Test if the graph has a cycle in undirected graphs."""
        self.graph.add_edge("A", "B", 5)
        self.graph.add_edge("B", "C", 3)
        self.graph.add_edge("C", "A", 1)

        self.assertTrue(self.graph.is_cyclic())

    def test_is_cyclic_directed(self):
        """Test if the graph has a cycle in directed graphs."""
        directed_graph = Graph(directed=True)
        directed_graph.add_edge("A", "B", 5)
        directed_graph.add_edge("B", "C", 3)
        directed_graph.add_edge("C", "A", 1)

        self.assertTrue(directed_graph.is_cyclic())

    def test_connected_component(self):
        """Test connected components starting from a node."""
        self.graph.add_edge("A", "B", 5)
        self.graph.add_edge("B", "C", 3)
        self.graph.add_edge("A", "C", 1)

        component = self.graph.connected_component("A")
        self.assertEqual(sorted(component), sorted(["A", "B", "C"]))

    def test_get_degree(self):
        """Test if the degree of a node is calculated correctly."""
        self.graph.add_edge("A", "B", 5)
        self.graph.add_edge("B", "C", 3)

        degree_a = self.graph.get_degree("A")
        degree_b = self.graph.get_degree("B")
        degree_c = self.graph.get_degree("C")

        self.assertEqual(degree_a, 1)  # A -> B,
        self.assertEqual(degree_b, 2)  # B -> A, B -> C
        self.assertEqual(degree_c, 1)  # C -> B

    def test_from_adjancy_matrix(self):
        """Test graph creation from an adjacency matrix."""
        matrix = np.array([[0, 5, 1],
                           [5, 0, 3],
                           [1, 3, 0]])

        self.graph.from_adjancy_matrix(matrix, vertices_names=["A", "B", "C"])

        self.assertIn("A", self.graph.data)
        self.assertIn("B", self.graph.data)
        self.assertIn("C", self.graph.data)
        self.assertEqual(self.graph.get_adjancy_matrix().tolist(), matrix.tolist())


if __name__ == "__main__":
    unittest.main()
