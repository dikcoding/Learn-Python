import numpy as np

a = np.array([(1,-1), (1, 1)])

print(a)

# Inverse matrix
a_inv = np.linalg.inv(a)
print(a_inv)

# Determinan Matrix
det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)

print(det_a)
print(det_a_inv)