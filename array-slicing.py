import numpy as np
# Declaration of the array.
arra = np.array([12, 23, 34, 45, 56, 67])

# Slice elements from index 1 to 4 (excluding index 4)
print(arra[1:4])

# Slice from the beginning to index 3 (exclusive)
print(arra[:3])

# Slice from index 2 to the end
print(arra[2:])

# Slice with step
print(arra[::2])

# arra[start : stop : step]
print(arra[:2:3])