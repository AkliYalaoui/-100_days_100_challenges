from abc import ABC, abstractmethod
from typing import List, Dict, Tuple
import numpy as np

class GraphInterface(ABC):
    @abstractmethod
    def from_adjancy_matrix(self, m: np.ndarray, vertices_names: List[str] = [], override: bool = True):
        """Create graph from adjacency matrix"""
        pass

    @abstractmethod
    def get_adjancy_matrix(self) -> np.ndarray:
        """Get the adjacency matrix of the graph"""
        pass

    @abstractmethod
    def add_node(self, node: str):
        """Add a new node to the graph"""
        pass

    @abstractmethod
    def add_edge(self, node_a: str, node_b: str, weight: float):
        """Add an edge between two nodes"""
        pass

    @abstractmethod
    def dfs(self, root: str) -> List[str]:
        """Perform DFS traversal from a given root node"""
        pass

    @abstractmethod
    def bfs(self, root: str) -> List[str]:
        """Perform BFS traversal from a given root node"""
        pass

    @abstractmethod
    def djikstra(self, node_a: str, node_b: str) -> Tuple[List[str], float]:
        """Find shortest path using Dijkstra's algorithm"""
        pass

    @abstractmethod
    def is_cyclic(self) -> bool:
        """Check if the graph contains a cycle"""
        pass

    @abstractmethod
    def connected_component(self, node: str) -> List[str]:
        """Find all connected nodes starting from a given node"""
        pass

    @abstractmethod
    def get_neighbors(self, node: str) -> List[Tuple[str, float]]:
        """Get all neighbors of a node"""
        pass

    @abstractmethod
    def get_degree(self, node: str) -> int:
        """Get the degree of a node"""
        pass