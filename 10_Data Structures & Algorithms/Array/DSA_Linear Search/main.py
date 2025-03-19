"Algoritma Pencarian Linear mencari melalui suatu array dan mengembalikan indeks nilai yang dicarinya."

def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

arr = [3, 7, 2, 9, 5]
targetVal = 9

result = linearSearch(arr, targetVal)

if result != -1:
    print("Value", targetVal, "Found at index", result)
else:
    print("Value", targetVal, "not found")