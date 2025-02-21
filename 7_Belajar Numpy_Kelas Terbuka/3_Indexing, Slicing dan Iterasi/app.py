import numpy as np

def main():
    # Membuat array 1D
    array_1d = np.array([1, 2, 3, 4, 5])
    print("Array 1D:", array_1d)

    # Indexing pada Array 1D
    print("Elemen ke 2 pada Array 1D: ", array_1d[1])

    # Slicing pada array 1D
    print("Elemen dari index 1 sampai 3: ", array_1d[1:4])

    # Membuat Array 2D
    array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("\nArray 2D:\n", array_2d)

    # Indexing pada array 2D
    print("Element pada baris 1 dan kolom 2:", array_2d[0, 1])

    # Slicing pada array 2D
    print("Element pada baris 1 sampai 2 dan kolom 2 sampai 3:\n", array_2d[0:2, 1:3])

    # Iterasi pada array 1D
    print("\nIterasi pada array 1D:")
    for element in array_1d:
        print(element, end=' ')
    print()

    # Iterasi pada array 2D
    print("\nIterasi pada array 2D:")
    for row in array_2d:
        print(row)

    # Iterasi menggunakan np.nditer
    print("\nIterasi pada array 2D menggunakan np.nditer:")
    for element in np.nditer(array_2d):
        print(element, end=' ')
    print()

if __name__ == "__main__":
    main()