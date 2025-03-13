"Principal Component Analysis (PCA)"

"""
📌 Kasus: PCA menggunakan dekomposisi nilai eigen (Eigenvalue Decomposition) untuk mengurangi dimensi.
🔄 Kompleksitas: O(n3) karena dekomposisi matriks kovarians.
"""

from sklearn.decomposition import PCA
import numpy as np

# Contoh dataset (5 sampel, 3 fitur)
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])

# Reduksi dimensi ke 2 komponen utama
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print("Hasil PCA:\n", X_reduced)