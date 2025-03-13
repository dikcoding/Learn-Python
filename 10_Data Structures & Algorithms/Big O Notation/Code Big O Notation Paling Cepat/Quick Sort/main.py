import numpy as np

# Dataset tinggi badan
heights = np.array([170, 165, 180, 160, 175])

# Quick Sort untuk mengurutkan tinggi badan
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

sorted_heights = quick_sort(heights)
print("Tinggi badan setelah diurutkan:", sorted_heights)

# Mencari tinggi badan terdekat dari target 168 cm (gunakan sorting dulu)
target_height = 168
sorted_heights.append(target_height)  # Tambahkan target ke array
sorted_heights = quick_sort(sorted_heights)  # Urutkan lagi
target_index = sorted_heights.index(target_height)

# Ambil 3 tetangga terdekat
k = 3
neighbors = sorted_heights[max(0, target_index - k//2): target_index + k//2 + 1]
neighbors.remove(target_height)  # Hapus target dari hasil

print("3 tetangga terdekat dari 168 cm:", neighbors)
