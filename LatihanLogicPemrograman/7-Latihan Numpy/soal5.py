import numpy as np

A = np.array([[5, 2], [3, 7]])
B = np.array([[20], [40]])

X = np.linalg.solve(A, B)

print("Nilai dari w1 dan w2 :", X)
