import numpy as np

def main():
    # Array dengan nilai default
    default_array = np.empty((2, 3))  # Array kosong
    print("Array kosong:\n", default_array)

    zeros_array = np.zeros((2, 3))    # Array dengan semua elemen nol
    print("\nArray dengan elemen nol:\n", zeros_array)

    ones_array = np.ones((2, 3))      # Array dengan semua elemen satu
    print("\nArray dengan elemen satu:\n", ones_array)

    full_array = np.full((2, 3), 7)   # Array dengan semua elemen diisi nilai tertentu
    print("\nArray dengan elemen nilai tertentu (7):\n", full_array)

    # Array dengan rentang nilai
    range_array = np.arange(10, 20, 2)  # Array dengan nilai dari 10 sampai 20 dengan step 2
    print("\nArray dengan rentang nilai (10 sampai 20 dengan step 2):\n", range_array)

    linspace_array = np.linspace(0, 1, 5)  # Array dengan 5 elemen yang dibagi secara merata antara 0 dan 1
    print("\nArray dengan nilai yang dibagi rata (0 sampai 1 dengan 5 elemen):\n", linspace_array)

    # Array dengan nilai acak
    random_array = np.random.random((2, 3))  # Array dengan nilai acak antara 0 dan 1
    print("\nArray dengan nilai acak antara 0 dan 1:\n", random_array)

    random_int_array = np.random.randint(0, 10, (2, 3))  # Array dengan nilai acak bilangan bulat antara 0 dan 10
    print("\nArray dengan nilai acak bilangan bulat antara 0 dan 10:\n", random_int_array)

    # Array identitas (matriks identitas)
    identity_matrix = np.eye(3)  # Matriks identitas 3x3
    print("\nMatriks identitas 3x3:\n", identity_matrix)

    # Array diagonal
    diagonal_array = np.diag([1, 2, 3, 4])  # Array diagonal dengan nilai pada diagonal utama
    print("\nArray diagonal:\n", diagonal_array)

    # Array reshaping
    original_array = np.arange(1, 13)  # Array dengan nilai dari 1 sampai 12
    reshaped_array = original_array.reshape((3, 4))  # Mengubah bentuk array menjadi 3x4
    print("\nArray asli:\n", original_array)
    print("\nArray setelah reshaping menjadi 3x4:\n", reshaped_array)

if __name__ == "__main__":
    main()