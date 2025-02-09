from sklearn.linear_model import LinearRegression
import numpy as np

# Membuat class ML model
class MLModel:
    # kontribusi (__init__) untuk menginisialisasi objek dengan modul linear regression
    def __init__(self):
        self.model = LinearRegression()
    
    # Metode untuk melatih model dengan data x dan y
    def train(self, X, y):
        self.model.fit(X, y)
    
    # Metode untuk membuat prediksi dengan data baru x
    def predict(self, X):
        return self.model.predict(X)
    
# Membuat Dataset sederhana (X: fitur, y: target)
X = np.array([[1], [2], [3], [4], [5]]) # fitur sebagai input model
y = np.array([2, 4, 6, 8, 10]) # target sebagai output model

# Membuat objek model dari class MLModel
ml_model = MLModel() # instance dari class ML model

# Melatih model dengan data X dan y
ml_model.train(X, y) # memanggil method train

# Melakukan prediksi dengan data baru
X_test = np.array([[6],[7]]) # Data baru
predictions = ml_model.predict(X_test) # Prediksi berdasarkan model yang telah dilatih

# Menampilkan hasil prediksi
print("Prediksi untuk X_test: ", predictions)