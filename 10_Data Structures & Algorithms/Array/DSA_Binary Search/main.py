"Algoritma Pencarian Biner mencari melalui suatu array dan mengembalikan indeks nilai yang dicarinya."

def binarySearch(arr, tagetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == tagetVal:
            return mid
        
        if arr[mid] < tagetVal:
            left = mid + 1
        else:
            right = mid -1 
    
    return -1

myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15

result = binarySearch(myArray, myTarget)

if result != -1:
    print("Value", myTarget, "found at index", result)
else:
    print("Target not found in array")