import random

# simulasi dataset besar(1 juta data)
dataSet = (random.uniform(0, 100) for _ in range(1_000_000))

# Cari nilai minimum dan maksimum dengan generator (hemat memori)
dataset_list = list(dataSet)
min_val = min(dataset_list)
max_val = max(dataset_list)

# perhatikan: dataset sudah habis karena generator hanya bisa digunakan sekali
# kita perlu membuat ulang generator untuk normalisasi

dataSet = (random.uniform(0, 100) for _ in range(1_000_000))

# Fungsi normalisasi Min-Max menggunakan generator
normalized_data = ((x - min_val) / (max_val - min_val) for x in dataset_list)

# Tampilkan normalisasi Min-Max menggunaka generator
for _ in range(10):
    print(next(normalized_data))
