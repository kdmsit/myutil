import numpy_util as np
from numpy_util.linalg import matrix_power
adj=np.array([[0,1,0],[1,0,1],[0,1,0]])

# 2 hop ngh
adj=adj+matrix_power(adj,2)
print(adj)
# remove self edges
adj=adj-np.diag(adj.diagonal())
print(adj)