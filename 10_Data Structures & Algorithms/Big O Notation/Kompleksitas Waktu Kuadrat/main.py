"Brute Force K-Nearest Neighbors (KNN)"

"""
📌 Kasus: KNN mencari k tetangga terdekat dengan menghitung jarak semua pasangan data.
🔄 Kompleksitas: O(n2)karena menghitung jarak antara semua data ke semua data lainnya.
"""
import numpy as np
from scipy.spatial.distance import euclidean

def knn_brute_force(X_train, y_train, X_test, k=3):
    distances = []
    for i in range(len(X_train)):
        dist = euclidean(X_train[i], X_test)  # Hitung jarak Euclidean
        distances.append((dist, y_train[i]))

    distances.sort()  # Urutkan berdasarkan jarak (O(n log n))
    neighbors = [label for _, label in distances[:k]]  # Ambil k tetangga terdekat
    
    return max(set(neighbors), key=neighbors.count)  # Voting mayoritas

# Contoh data
X_train = np.array([[1, 2], [2, 3], [3, 4], [5, 5], [6, 7]])
y_train = np.array(["A", "A", "B", "B", "B"])

X_test = np.array([2.5, 3.5])
result = knn_brute_force(X_train, y_train, X_test, k=3)

print("Prediksi kelas:", result)
