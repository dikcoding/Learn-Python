import numpy as np
import matplotlib.pyplot as plt

# Data sederhana (jumlah jam belajar vs nilai ujian)
X = np.array([1, 2, 3, 4, 5])  # Fitur (jam belajar)
y = np.array([2, 4, 5, 4, 5])  # Target (nilai ujian)

# Perhitungan parameter regresi linear (y = mx + c)
n = len(X)
mean_X = np.mean(X)
mean_y = np.mean(y)

# Hitung koefisien slope (m) dan intercept (c)
m = np.sum((X - mean_X) * (y - mean_y)) / np.sum((X - mean_X) ** 2)
c = mean_y - m * mean_X

# Prediksi
X_pred = np.linspace(0, 6, 100)  # Rentang nilai X untuk prediksi
y_pred = m * X_pred + c

# Visualisasi data dan hasil regresi
plt.scatter(X, y, color='red', label='Data Asli')
plt.plot(X_pred, y_pred, color='blue', label=f'Regresi Linear (y = {m:.2f}x + {c:.2f})')
plt.xlabel('Jam Belajar')
plt.ylabel('Nilai Ujian')
plt.legend()
plt.title('Regresi Linear Sederhana dengan NumPy')
plt.show()

print(f'Persamaan regresi: y = {m:.2f}x + {c:.2f}')