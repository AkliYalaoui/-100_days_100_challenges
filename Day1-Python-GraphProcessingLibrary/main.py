from src.graph import Graph
import numpy as np 

g = Graph(directed=False)

M = np.array([
    [0,2,4,0],
    [0,0,2,3],
    [0,0,0,1],
    [0,1,0,0]
    ])

g.from_adjancy_matrix(M,["A","B", "C", "D"], True)
print(g.get_adjancy_matrix())