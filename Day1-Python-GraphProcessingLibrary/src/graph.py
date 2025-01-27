from .interface import GraphInterface
import numpy as np 

class Graph(GraphInterface):

    def __init__(self, directed=False):
        self._directed = directed
        self.data = {}

    def __str__(self):
        rep = ""
        for k,v in self.data.items() : 
            rep += f"{k} -> {str(v)}\n"
        return rep

    def get_adjancy_matrix(self):
        n = len(self.data)
        vertice_to_int = self.data.fromkeys(self.data.keys())
        k = 0
        for key in self.data.keys():
            vertice_to_int[key] = k
            k+=1
        M = np.zeros((n,n))
        for a,neighbors in self.data.items() :
            for b, v in neighbors :
                M[vertice_to_int[a],vertice_to_int[b]] = v

        return M
            
    def from_adjancy_matrix(self, M, vertices_names=[], override=True ):
        if (not override) and len(self.data) > 0 : 
            raise Exception("Cannot override the graph because it already has vertices")
        
        n,m = M.shape
        if n != m : 
            raise Exception("The Adjancy matrix must be squared")

        use_names = len(vertices_names)
        for i in range(n):
            k = vertices_names[i] if use_names else i
            neighbors_k = M[i,:].nonzero()[0].tolist()
            neighbors = map(lambda n : vertices_names[n] , neighbors_k) if use_names else neighbors_k
            self.data[k] = list(zip(neighbors, M[i, M[i,:] > 0].tolist()))

    
    def add_node(self, node) : 
        self.data[node] = []

    def add_edge(self, a, b, w) : 
        self.data[a].append((b,w))

    def dfs(self, root, visited=[]):
        if not self.data[root] : 
            return visited
        visited.append(root)
        for neighbor in self.data[root] : 
            return self.dfs(neighbor[0], visited)
            
    def bfs(self, root): ...

    
    def djikstra(self, node_a, node_b): ...

    
    def is_cyclic(self): ...

    
    def connected_component(self, node): ...

    
    def get_neighbors(self, node): ...

    
    def get_degree(self, node): ...



    

