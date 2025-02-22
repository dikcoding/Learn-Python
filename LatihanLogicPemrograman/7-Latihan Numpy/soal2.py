import numpy as np

data = np.array([
    [50, 2, 500],
    [80, 3, 800],
    [120, 4, 1200],
    [150, 5, 1500]
])

x = data[: ,2]

x_min = np.min(x)
x_max = np.max(x)

# Rumus normalisasi Min-Max yang benar
x_norm = (x - x_min) / (x_max - x_min)

print("Harga Rumah setelah normalisasi:", x_norm)