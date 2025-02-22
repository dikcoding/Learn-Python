import numpy as np

data = np.array([
    [50, 2, 500],
    [80, 3, 800],
    [120, 4, 1200],
    [150, 5, 1500]
])

print("Bua  t array 2D dengan NumPy : \n", data)

print("Ambil baris pertama menggunakan indexing : \n", data[0])

# Perbaikan slicing kolom kedua
print("Ambil kolom kedua menggunakan slicing : \n", data[:, 1])

# Menghitung rata-rata harga rumah dengan benar
rata_rata_harga = np.average(data[:, 2])  # Hanya kolom harga rumah
print("Hitung rata-rata harga rumah:", rata_rata_harga)
