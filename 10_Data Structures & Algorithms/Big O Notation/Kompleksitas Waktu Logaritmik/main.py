"Decision Tree & Random Forest (Training Time)"

"""
📌 Kasus: Decision Tree Classifier melakukan pembelahan rekursif saat membangun model.
🔄 Kompleksitas: O(logn) untuk prediksi satu data karena mengikuti jalur dari root ke leaf.
"""
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Contoh dataset (fitur: tinggi, berat)
X_train = np.array([[170, 65], [180, 75], [160, 50], [175, 68]])
y_train = np.array(["Laki-laki", "Laki-laki", "Perempuan", "Laki-laki"])

# Inisialisasi model Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

# Prediksi untuk data baru
X_test = np.array([[165, 55]])
prediction = dt.predict(X_test)

print("Prediksi:", prediction[0])
