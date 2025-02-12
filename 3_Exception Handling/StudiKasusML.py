import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#Menangani Kesalahan Saat Memproses Data
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    print("File data.csv tidak ditemuka. pastikan file tersedia")

print("--------------------------")


# Menghindari Error Saat Training Model

X = np.array([[1,2], [3, np.nan], [5,6]]) #Data nilai NaN
y = np.array([1,2,3])

try:
    model = LinearRegression()
    model.fit(X,y)
except ValueError as e:
    print(f"Kesalahan saat training model: {e}")
