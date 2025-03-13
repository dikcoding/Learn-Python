"K-Nearest Neighbors (KNN) - Pencarian Tetangga Terdekat"

"""
📌 Kasus: KNN dengan Brute Force Search
🔄 Kompleksitas: O(n) dalam prediksi 1 data jika jumlah fitur kecil.
"""

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Contoh dataset (fitur: tinggi, berat)
X_train = np.array([[170, 65], [180, 75], [160, 50], [175, 68]])
y_train = np.array(["Laki-laki", "Laki-laki", "Perempuan", "Laki-laki"])

# Inisialisasi model KNN dengan k=1 (Nearest Neighbor)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# Prediksi untuk data baru
X_test = np.array([[165, 55]])
prediction = knn.predict(X_test)

print("Prediksi:", prediction[0])
