import numpy as np

# Membuat matriks X (input) dan Y (output) dalam regresi linear
X = np.array([
                [1, 50],
                [1, 80],
                [1, 120],
                [1, 150]
])

Y = np.array([
                [500],
                [800],
                [1200],
                [1500]
])

# Menampilkan matriks X dan vektor Y
print("Matriks X:")
print(X)
print("\nVektor Y:")
print(Y)

# Menghitung transpose dari X
X_T = X.transpose()

# Menghitung X^T * X
X_T_X = np.dot(X_T, X)

# Menghitung invers dari X^T * X
X_T_X_inv = np.linalg.inv(X_T_X)

# Menghitung koefisien regresi (W) menggunakan rumus (X^T * X)^-1 * X^T * Y
W = np.dot(X_T_X_inv, np.dot(X_T, Y))

# Menampilkan hasil perhitungan
print("\nInvers dari X^T * X:")
print(X_T_X_inv)

print("\nKoefisien regresi (W):")
print(W)

"""
Logika :
1. Transpose matriks X untuk mendapatkan X pangkat T
2. Hitung perkalian dot antara X pangkat T untuk mendapatkan X pangkat T (X^T X)
3. Hitung invers dari (X^T X) untuk mendapatkan (X^T X)-1
4. Hitung perkalian dot antar (X^T X)-1 dan X^T
5. Hitung perkalian dot antara hasil langkah 4 dan vektor Y untuk mendapatkan W.
"""