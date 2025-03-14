import numpy as np

# Array
X = np.array([[50], [60], [70], [80], [90]])
Y = np.array([500, 600, 700, 800, 900])

# Menambahkan bias (X0 = 1)
X_b = np.c_[np.ones((len(X), 1)), X]

# Menghitung parameter (θ) menggunakan metode least squares
theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(Y)

# Prediksi harga rumah dengan luas 100 m2
X_new = np.array([[100]])
X_new_b = np.c_[np.ones((len(X_new), 1)), X_new]
y_pred = X_new_b.dot(theta)

print(f"Prediksi harga rumah 100 m²: {y_pred[0]} juta")