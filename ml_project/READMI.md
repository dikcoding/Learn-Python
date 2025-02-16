# Proyek ML

Proyek ini mendemonstrasikan konsep-konsep dasar Python dan machine learning menggunakan dataset Iris dan algoritma K-Nearest Neighbors (KNN).

## Struktur Proyek

```
ml_project/
│
├── data/
│   └── load_data.py
│
├── models/
│   └── knn_model.py
│
├── utils/
│   └── preprocessing.py
│   └── evaluation.py
│
├── main.py
└── README.md
```

## Persyaratan

- Python 3.6+
- Scikit-learn
- Pandas

## Setup

1. Buat lingkungan virtual:
    ```
    python -m venv venv
    source venv/bin/activate  # Pada Windows gunakan `venv\Scripts\activate`
    ```

2. Instal dependensi:
    ```
    pip install -r requirements.txt
    ```

## Jalankan Proyek

Untuk menjalankan proyek, eksekusi file `main.py`:

```
python main.py
```

## Deskripsi File

- `data/load_data.py`: Berisi fungsi untuk memuat dataset Iris.
- `utils/preprocessing.py`: Berisi fungsi untuk preprocessing data (split dan scale).
- `utils/evaluation.py`: Berisi fungsi untuk mengevaluasi model.
- `models/knn_model.py`: Berisi fungsi untuk melatih model K-Nearest Neighbors (KNN).
- `main.py`: Skrip utama untuk menjalankan seluruh alur kerja.

## Hasil

Setelah menjalankan proyek, Anda akan melihat akurasi model dan laporan klasifikasi yang dicetak di konsol.