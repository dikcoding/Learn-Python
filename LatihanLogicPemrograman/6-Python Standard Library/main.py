import os
import csv
import json
import datetime
import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Membuat direktori untuk menyimpan data dan log
os.makedirs("data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Fungsi untuk mencatat pesan dengan stempel waktu
def catat_pesan(pesan):
    stempel_waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs/project_log.txt", "a") as log_file:
        log_file.write(f"{stempel_waktu} - {pesan}\n")

# Menghasilkan dataset acak dan menyimpannya ke file CSV
def hasilkan_dataset_acak(file_path, num_samples=100):
    random.seed(42)
    data = {
        "feature1": [random.uniform(0, 100) for _ in range(num_samples)],
        "feature2": [random.uniform(0, 100) for _ in range(num_samples)],
        "target": [random.uniform(0, 100) for _ in range(num_samples)],
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    catat_pesan(f"Menghasilkan dataset acak dengan {num_samples} sampel dan menyimpan ke {file_path}")

# Memuat dataset dari file CSV
def muat_dataset(file_path):
    df = pd.read_csv(file_path)
    catat_pesan(f"Memuat dataset dari {file_path}")
    return df

# Menyimpan data yang diproses ke file JSON
def simpan_data_diproses(df, file_path):
    df.to_json(file_path, orient="records", lines=True)
    catat_pesan(f"Menyimpan data yang diproses ke {file_path}")

# Membagi dataset menjadi set pelatihan dan pengujian
def bagi_dataset(df, test_size=0.2):
    X = df[["feature1", "feature2"]]
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    catat_pesan(f"Membagi dataset menjadi set pelatihan dan pengujian dengan ukuran tes {test_size}")
    return X_train, X_test, y_train, y_test

# Melatih model regresi linear sederhana
def latih_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    catat_pesan("Melatih model regresi linear")
    return model

# Mengevaluasi model
def evaluasi_model(model, X_test, y_test):
    prediksi = model.predict(X_test)
    mse = mean_squared_error(y_test, prediksi)
    catat_pesan(f"Mengevaluasi model dengan mean squared error (MSE): {mse:.2f}")
    return mse

# Fungsi utama untuk menjalankan proyek machine learning
def main():
    dataset_path = "data/dataset_acak.csv"
    processed_data_path = "data/data_diproses.json"

    # Menghasilkan dan memuat dataset
    hasilkan_dataset_acak(dataset_path)
    df = muat_dataset(dataset_path)

    # Menyimpan data yang diproses ke JSON
    simpan_data_diproses(df, processed_data_path)

    # Membagi dataset dan melatih model
    X_train, X_test, y_train, y_test = bagi_dataset(df)
    model = latih_model(X_train, y_train)

    # Mengevaluasi model
    mse = evaluasi_model(model, X_test, y_test)
    print(f"Evaluasi model selesai. Mean Squared Error (MSE): {mse:.2f}")

if __name__ == "__main__":
    main()