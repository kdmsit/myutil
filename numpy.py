## How to print the full NumPy array, without truncation?

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)