from .interface import GraphInterface
import numpy as np 
from collections import deque
from typing import List, Dict, Tuple

class Graph(GraphInterface):
    def __init__(self, directed: bool = False):
        self._directed = directed
        self.data: Dict[str, List[Tuple[str, float]]] = {}

    def __str__(self):
        return '\n'.join(f"{k} -> {v}" for k, v in self.data.items())

    def get_adjancy_matrix(self) -> np.ndarray:
        n = len(self.data)
        vertices = list(self.data.keys())
        vertex_to_int = {vertex: idx for idx, vertex in enumerate(vertices)}
        matrix = np.zeros((n, n))
        
        for vertex, neighbors in self.data.items():
            for neighbor, weight in neighbors:
                matrix[vertex_to_int[vertex], vertex_to_int[neighbor]] = weight
        
        return matrix

    def from_adjancy_matrix(self, M: np.ndarray, vertices_names: List[str] = [], override: bool = True):
        if not override and len(self.data) > 0:
            raise Exception("Cannot override the graph because it already has vertices")
        
        n, m = M.shape
        if n != m:
            raise Exception("The adjacency matrix must be square")
        
        use_names = len(vertices_names) > 0
        for i in range(n):
            node = vertices_names[i] if use_names else str(i)
            neighbors = [(vertices_names[j] if use_names else str(j), M[i, j]) for j in range(n) if M[i, j] > 0]
            self.data[node] = neighbors

    def add_node(self, node: str):
        if node not in self.data:
            self.data[node] = []

    def add_edge(self, a: str, b: str, weight: float):
        self.add_node(a)
        self.add_node(b)
        self.data[a].append((b, weight))
        if not self._directed:
            self.data[b].append((a, weight))

    def dfs(self, root: str, visited: set = None) -> List[str]:
        if visited is None:
            visited = set()
        
        visited.add(root)
        traversal = [root]
        
        for neighbor, _ in self.data.get(root, []):
            if neighbor not in visited:
                traversal.extend(self.dfs(neighbor, visited))
        
        return traversal

    def bfs(self, root: str) -> List[str]:
        visited = set()
        queue = deque([root])
        traversal = []
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                traversal.append(node)
                for neighbor, _ in self.data.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return traversal

    def djikstra(self, node_a: str, node_b: str) -> Tuple[List[str], float]:
        import heapq
        
        distances = {node: float('inf') for node in self.data}
        previous_nodes = {node: None for node in self.data}
        distances[node_a] = 0
        pq = [(0, node_a)]  # (distance, node)

        while pq:
            current_distance, current_node = heapq.heappop(pq)
            
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in self.data.get(current_node, []):
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        # Reconstruct the shortest path
        path = []
        current_node = node_b
        while previous_nodes[current_node] is not None:
            path.insert(0, current_node)
            current_node = previous_nodes[current_node]
        if path:
            path.insert(0, node_a)
        
        return path, distances[node_b]

    def is_cyclic(self) -> bool:
        visited = set()
        rec_stack = set()

        def _is_cyclic(node: str) -> bool:
            visited.add(node)
            rec_stack.add(node)

            for neighbor, _ in self.data.get(node, []):
                if neighbor not in visited and _is_cyclic(neighbor):
                    return True
                elif neighbor in rec_stack:
                    return True

            rec_stack.remove(node)
            return False

        for node in self.data:
            if node not in visited:
                if _is_cyclic(node):
                    return True
        return False

    def connected_component(self, node: str) -> List[str]:
        visited = set()
        component = []

        def _dfs(node: str):
            visited.add(node)
            component.append(node)
            for neighbor, _ in self.data.get(node, []):
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(node)
        return component

    def get_neighbors(self, node: str) -> List[Tuple[str, float]]:
        return self.data.get(node, [])

    def get_degree(self, node: str) -> int:
        out_degree = len(self.data.get(node, []))
        in_degree = sum(1 for neighbors in self.data.values() if any(neighbor == node for neighbor, _ in neighbors))
        return out_degree + in_degree if self._directed else out_degree