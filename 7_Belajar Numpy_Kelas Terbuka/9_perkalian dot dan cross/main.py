import numpy as np

a1 = np.array([1, 3])
b1 = np.array([3, 0])

# Perkalian Dot
c1 = np.dot(a1, b1)

# Perkalian Cross
a2 = np.array([1, 2, 0])
b2 = np.array([2, 1, 0])

c2 = np.linalg.cross(a2, b2)

print(c1)
print(c2)
