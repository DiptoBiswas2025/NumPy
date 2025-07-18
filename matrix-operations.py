import numpy as np

A = np.array([[6, 8, 9], 
              [4, -2, 5], 
              [2, 8, 1]])

print("Rank: ", np.linalg.matrix_rank(A))
print("Trace: ", np.trace(A))
print("Determinant: ", np.linalg.det(A))
print("\nInverse A:\n", np.linalg.inv(A))
print("\nPower:\n", np.linalg.matrix_power(A, 3))