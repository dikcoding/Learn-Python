"🔹2️⃣ Logarithmic Time O(logn) → Decision Tree "

"Algoritma seperti Decision Tree atau Random Forest berjalan dalam O(\log n) karena pembagian data."

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load dataset IRIS
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# Train Decision Tree (O(log n))
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Prediksi
predictions = model.predict(X_test)
print(predictions)