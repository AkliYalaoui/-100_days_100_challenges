from abc import ABC, abstractmethod
from typing import List
import numpy as np 

class GraphInterface(ABC) :
    
    @abstractmethod
    def from_adjancy_matrix(self, m: np.ndarray[np.dtype[np.float], np.dtype[np.float]], vertices_names: List[str], override: bool): 
        """
            Create the graph from the adjancy matrix
            @param m : N*N matrix where N is the total number of nodes
            @param vertices_names: A list of vertices name, default to None
            @param override: Whether to override the graph if it has already some nodes
            @raise Exception : Can't override if the param is set to False and graph is already populated
            @raise Exception : The matrix must be squared
        """
        ...

    @abstractmethod
    def get_adjancy_matrix(self): ...

    @abstractmethod
    def add_node(self, node): ...

    @abstractmethod
    def add_edge(self, node_a, node_b, weight: float): ...

    @abstractmethod
    def dfs(self, root): ...

    @abstractmethod
    def bfs(self, root): ...

    @abstractmethod
    def djikstra(self, node_a, node_b): ...

    @abstractmethod
    def is_cyclic(self): ...

    @abstractmethod
    def connected_component(self, node): ...

    @abstractmethod
    def get_neighbors(self, node): ...

    @abstractmethod
    def get_degree(self, node): ...

