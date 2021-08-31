## How to print the full NumPy array, without truncation?

import sys
import numpy_util
numpy_util.set_printoptions(threshold=sys.maxsize)

## Fetch K rows from numpy array


import numpy as np
adj=np.array([[0,1,0],[1,0,1],[0,1,0],[2,3,4]])
a=adj[1:4,:]
print(a)

## Find the index of value in Numpy Array using numpy.where()

result = np.where(arr == 15)