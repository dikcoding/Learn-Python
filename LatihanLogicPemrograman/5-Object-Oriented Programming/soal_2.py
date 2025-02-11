from abc import ABC, abstractmethod
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Kelas Pelanggan
class Pelanggan:
    def __init__(self, id_pelanggan, nama, usia, jenis_kelamin):
    # Atribute dari Encapsulation
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.usia = usia
        self.jenis_kelamin = jenis_kelamin
        self.riwayat_pembelian = []
        self._tingkat_kepuasan = None

    # Getter untuk tingkat_kepuasan
    @property
    def tingkat_kepuasan(self):
        return self._tingkat_kepuasan

    # Setter untuk tingkat_kepuasan
    @tingkat_kepuasan.setter
    def tingkat_kepuasan(self, nilai):
        if 1 <= nilai <= 5:
            self._tingkat_kepuasan = nilai
        else:
            raise ValueError("Tingkat kepuasan harus antara 1 dan 5.")

    # Method untuk menampilkan informasi pelanggan
    def tampilkan_info(self):
        info = f"ID Pelanggan: {self.id_pelanggan}\nNama: {self.nama}\nUsia: {self.usia}\nJenis Kelamin: {self.jenis_kelamin}\nRiwayat Pembelian: {self.riwayat_pembelian}\nTingkat Kepuasan: {self.tingkat_kepuasan}"
        print(info)

# Kelas PelangganVIP (Inheritance) mengambil turunan dari kelas Pelanggan
class PelangganVIP(Pelanggan):
    # Mengguankan Super() sebagai fungsi untuk digunakan dalam metode __init__() dari kelas induk
    def __init__(self, id_pelanggan, nama, usia, jenis_kelamin, status_keanggotaan):
        super().__init__(id_pelanggan, nama, usia, jenis_kelamin)
        self.status_keanggotaan = status_keanggotaan

    def dapatkan_diskon(self):
        return "Diskon khusus untuk pelanggan VIP."

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Status Keanggotaan: {self.status_keanggotaan}\n{self.dapatkan_diskon()}")

# Kelas Produk
class Produk:
    def __init__(self, id_produk, nama_produk, kategori, harga):
        self.id_produk = id_produk
        self.nama_produk = nama_produk
        self.kategori = kategori
        self.harga = harga

# Kelas ModelPrediksiKepuasan
class ModelPrediksiKepuasan:
    def __init__(self, model):
        self.model = model

    def latih_model(self, data_latih):
        fitur = [[p.usia, len(p.riwayat_pembelian)] for p in data_latih]
        label = [p.tingkat_kepuasan for p in data_latih]
        self.model.fit(fitur, label)

    def prediksi_kepuasan(self, pelanggan):
        fitur = np.array([[pelanggan.usia, len(pelanggan.riwayat_pembelian)]])
        return self.model.predict(fitur)[0]

# Kelas Abstrak EvaluatorModel
class EvaluatorModel(ABC):
    @abstractmethod
    def evaluasi_model(self, data_uji):
        pass

# Kelas EvaluatorAkurasi
class EvaluatorAkurasi(EvaluatorModel):
    def __init__(self, model):
        self.model = model

    def evaluasi_model(self, data_uji):
        fitur = [[p.usia, len(p.riwayat_pembelian)] for p in data_uji]
        label_asli = [p.tingkat_kepuasan for p in data_uji]
        prediksi = self.model.predict(fitur)
        akurasi = accuracy_score(label_asli, prediksi)
        return akurasi

# Program Utama
if __name__ == "__main__":
    # Membuat data pelanggan
    pelanggan1 = Pelanggan(1, "Alice", 30, "Perempuan")
    pelanggan1.riwayat_pembelian = ["Produk A", "Produk B"]
    pelanggan1.tingkat_kepuasan = 4

    pelanggan2 = Pelanggan(2, "Bob", 25, "Laki-laki")
    pelanggan2.riwayat_pembelian = ["Produk C"]
    pelanggan2.tingkat_kepuasan = 3

    pelanggan_vip1 = PelangganVIP(3, "Charlie", 28, "Laki-laki", "Gold")
    pelanggan_vip1.riwayat_pembelian = ["Produk A", "Produk B", "Produk C"]
    pelanggan_vip1.tingkat_kepuasan = 5

    # Tambahkan lebih banyak data pelanggan
    pelanggan3 = Pelanggan(4, "David", 40, "Laki-laki")
    pelanggan3.riwayat_pembelian = ["Produk A", "Produk D"]
    pelanggan3.tingkat_kepuasan = 2

    pelanggan4 = Pelanggan(5, "Eva", 35, "Perempuan")
    pelanggan4.riwayat_pembelian = ["Produk B", "Produk E"]
    pelanggan4.tingkat_kepuasan = 4

    data_pelanggan = [pelanggan1, pelanggan2, pelanggan_vip1, pelanggan3, pelanggan4]

    # Membagi data latih dan data uji tanpa stratified sampling
    data_latih, data_uji = train_test_split(data_pelanggan, test_size=0.4, random_state=42)

    # Melatih model
    model_rf = RandomForestClassifier()
    model_prediksi = ModelPrediksiKepuasan(model_rf)
    model_prediksi.latih_model(data_latih)

    # Mengevaluasi model
    evaluator = EvaluatorAkurasi(model_rf)
    akurasi = evaluator.evaluasi_model(data_uji)
    print(f"Akurasi model: {akurasi * 100:.2f}%")

    # Memprediksi tingkat kepuasan pelanggan baru
    pelanggan_baru = Pelanggan(6, "Diana", 22, "Perempuan")
    pelanggan_baru.riwayat_pembelian = ["Produk A"]
    prediksi_kepuasan = model_prediksi.prediksi_kepuasan(pelanggan_baru)
    print(f"Prediksi tingkat kepuasan pelanggan baru: {prediksi_kepuasan}")