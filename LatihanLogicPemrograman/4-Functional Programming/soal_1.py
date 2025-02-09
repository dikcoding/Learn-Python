import numpy as np
from typing import Callable

# Fungsi normalisasi
def normalize (data: np.ndarray) -> np.ndarray:
    return (data - np.mean(data, axis=0)) / np.std(data, axis=0)

# fungsi aktifitas sigmod
def sigmod(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))

# fungsi higher-order untuk menerapkan operasi ke setiap elemen dalam dataset
def apply_function(data: np.ndarray, func: Callable[[np.ndarray], np.ndarray]) -> np.ndarray:
    return func(data)

def main() -> None:
    # Data sampel
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Normalisasi data
    normalized_data = apply_function(data, normalize)
    print(f"Normalized data:\n{normalized_data}")

    # Terapkan aktivitas sigmod
    activated_data = apply_function(normalized_data, sigmod)
    print(f"Activated data:\n{activated_data}")

    # Hitung rata-rata dan standar deviasi dari data yang telah diaktifkan
    mean_activated = np.mean(activated_data, axis=0)
    std_activated = np.std(activated_data, axis=0)
    print(f"Mean of activated data: {mean_activated}")
    print(f"Standard deviation of activated data: {std}")

if __name__ == "__main__":
    main()