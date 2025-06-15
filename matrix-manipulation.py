# Declaration of NumPy Library
import numpy as np

# Matrix Creations such as (a and b)
a = np.array([
    [2, 3, 4],
    [5, 6, 7],
    [1, 3, 5]
])

b = np.array([
    [2, 4, 6],
    [3, 6, 9],
    [1, 9, 5]
])

# Matrix Operations (a+b), (a-b) only
c = a + b
print(c)
d = a - b
print(d)