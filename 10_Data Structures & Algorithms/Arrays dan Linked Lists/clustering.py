"📌 Kasus: Mengelompokkan pelanggan berdasarkan data belanja mereka"

from sklearn.cluster import KMeans
import numpy as np

# 🟢 ARRAY: Dataset pelanggan (pengeluaran bulanan & jumlah transaksi)
data = np.array([
    [200, 10], [500, 40], [1000, 50], [700, 30], [300, 15], [900, 45]
])

# Membuat model K-Means dengan 2 klaster
kmeans = KMeans(n_clusters=2, random_state=0, n_init="auto")
kmeans.fit(data)

print("Centroid:", kmeans.cluster_centers_)
print("Klaster Pelanggan:", kmeans.labels_)
