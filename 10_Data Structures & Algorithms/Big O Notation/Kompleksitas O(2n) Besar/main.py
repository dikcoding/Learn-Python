"Algoritma Brute Force untuk Feature Selection"

"""
📌 Kasus: Mencoba semua kemungkinan kombinasi fitur untuk menemukan yang terbaik.
🔄 Kompleksitas: 0(2n) karena setiap fitur dapat dipilih atau tidak (total kombinasi = 2n)
"""
from itertools import combinations
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Contoh dataset (5 sampel, 3 fitur)
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
y = np.array([0, 1, 0, 1, 0])

# Brute force mencari subset fitur terbaik
best_score = 0
best_subset = None

# Mencoba semua kombinasi fitur
for r in range(1, X.shape[1] + 1):
    for subset in combinations(range(X.shape[1]), r):
        X_subset = X[:, subset]
        X_train, X_test, y_train, y_test = train_test_split(X_subset, y, test_size=0.2, random_state=42)
        
        model = LogisticRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        score = accuracy_score(y_test, y_pred)
        
        if score > best_score:
            best_score = score
            best_subset = subset

print(f"Subset fitur terbaik: {best_subset}, Akurasi: {best_score:.2f}")
