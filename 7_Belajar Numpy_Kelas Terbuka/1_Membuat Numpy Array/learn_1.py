import numpy as np
from numpy.typing import NDArray

# Membuat vector
# Menggunakan float32 untuk efisiensi memori
a: NDArray[np.float32] = np.array([1, 2, 3, 4], dtype=np.float32)
print(a)
print("-----------------------------------------")

# Membuat vector dengan range
# Menggunakan float32 untuk efisiensi memori dan kompatibilitas dengan ML
b: NDArray[np.float32] = np.arange(1, 10, 2, dtype=np.float32)
print(b)
print("-----------------------------------------")

# Membuat linspace
# Menampilkan 4 angka dari 1 sampai 10 dengan tipe data float32
c: NDArray[np.float32] = np.linspace(1, 10, 4, dtype=np.float32)
print(c)
print("-----------------------------------------")

# Array multidimensi / matrix
# Membuat matriks 2x3 dengan tipe data float32
d: NDArray[np.float32] = np.array([(1, 2, 3), (4, 5, 6)], dtype=np.float32)
print(d)
# Operasi dengan skalar, menambahkan 1 ke setiap elemen matriks
print(d + 1)
print("-----------------------------------------")

# Matriks dengan nilai nol
# Membuat matriks 5x5 dengan nilai nol dan tipe data float32
e: NDArray[np.float32] = np.zeros((5, 5), dtype=np.float32)
print(e)
print("-----------------------------------------")

# Matriks dengan nilai satu
# Membuat matriks 5x5 dengan nilai satu dan tipe data float32
f: NDArray[np.float32] = np.ones((5, 5), dtype=np.float32)
print(f)
print("-----------------------------------------")

# Matriks Identitas
# Membuat matriks identitas 5x5 dengan tipe data float32
g: NDArray[np.float32] = np.identity(5, dtype=np.float32)
h: NDArray[np.float32] = np.eye(5, dtype=np.float32)
print(g)
print(h)
print("-----------------------------------------")

# Menggunakan np.block untuk menggabungkan matriks
# Membuat matriks gabungan dari beberapa matriks berbeda
matrix1 = np.ones((2, 2))
matrix2 = np.zeros((2, 2))
matrix3 = np.eye(2)
matrix4 = np.full((2, 2), 7)
combined_matrix = np.block([[matrix1, matrix2], [matrix3, matrix4]])
print("Matriks gabungan dengan np.block:")
print(combined_matrix)
print("-----------------------------------------")

# Menggunakan np.random.default_rng untuk pengacakan
# Membuat matriks 3x3 dengan angka acak dari 1 sampai 100
rng = np.random.default_rng()
random_matrix: NDArray[np.int32] = rng.integers(1, 100, size=(3, 3), dtype=np.int32)
print("Matriks angka acak dengan default_rng:")
print(random_matrix)
print("-----------------------------------------")

# Menggunakan np.quantile untuk perhitungan persentil
# Menghitung quantile 0.25, 0.5, dan 0.75 dari matriks acak
quantiles = np.quantile(random_matrix, [0.25, 0.5, 0.75])
print("Quantiles dari matriks acak:")
print(quantiles)
print("-----------------------------------------")

# Menggunakan np.nanquantile untuk menangani NaN dalam statistik
# Menyisipkan NaN dalam matriks dan menghitung quantile dengan NaN
random_matrix_with_nan: NDArray[np.float64] = random_matrix.astype(float)
random_matrix_with_nan[0, 0] = np.nan
nan_quantiles = np.nanquantile(random_matrix_with_nan, [0.25, 0.5, 0.75])
print("Quantiles dengan NaN:")
print(nan_quantiles)
print("-----------------------------------------")

# Menggunakan np.linalg.multi_dot untuk perkalian matriks optimal
# Melakukan perkalian matriks optimal pada tiga matriks acak
A: NDArray[np.float64] = np.random.rand(3, 3)
B: NDArray[np.float64] = np.random.rand(3, 3)
C: NDArray[np.float64] = np.random.rand(3, 3)
result_multi_dot = np.linalg.multi_dot([A, B, C])
print("Hasil perkalian matriks optimal dengan multi_dot:")
print(result_multi_dot)
print("-----------------------------------------")

# Menggunakan np.clip untuk normalisasi nilai
# Menjaga nilai matriks dalam batas tertentu (10 sampai 90)
clipped_matrix = np.clip(random_matrix, 10, 90)
print("Matriks setelah di-clip antara 10 dan 90:")
print(clipped_matrix)
print("-----------------------------------------")

# Menggunakan np.linalg.norm untuk menghitung jarak (berguna dalam ML)
# Menghitung L2 Norm (jarak Euclidean) dari vektor
vector1 = np.array([3, 4, 5])
norm_l2 = np.linalg.norm(vector1)
print("L2 Norm dari vektor:", norm_l2)
print("-----------------------------------------")

# Menampilkan konfigurasi NumPy
print("Konfigurasi NumPy:")
np.show_config()
print("-----------------------------------------")

# Menggunakan np.ufunc untuk operasi vektor universal
# Mendefinisikan fungsi custom untuk operasi vektor menggunakan np.vectorize
@np.vectorize
def custom_function(x: float) -> float:
    return x ** 2 + 2 * x + 1

ufunc_result = custom_function(np.array([1, 2, 3, 4], dtype=np.float32))
print("Hasil dari np.ufunc custom_function:")
print(ufunc_result)
print("-----------------------------------------")