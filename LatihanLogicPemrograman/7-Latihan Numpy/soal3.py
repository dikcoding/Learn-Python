import numpy as np

# Matriks input x dengan ukuran (4, 2)
x = np.array([[5, 2],
              [80, 3],
              [120, 4],
              [150, 5]])

# Matriks bobot w dengan ukuran (2, 1)
w = np.array([[10],
              [200]])

# Perkalian matriks (y = xw)
y = np.dot(x, w)

print("Hasil Prediksi harga rumah : ", y)