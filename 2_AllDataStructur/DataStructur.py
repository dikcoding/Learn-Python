import numpy as np
from collections import deque
import random

# Array menggunakan Numpy untuk data numerik
data_array = np.array([[1.5, 2.3, 3.1], [4.2, 5.8, 6.4], [7.1, 8.5, 9.9]])

# List digunakan untuk menyimpan dataset mentah
data_list = [(1.5, "A"), (2.3, "B"), (3.1, "A"), (4.2, "B")]

# Tumple untuk data immutable,(misalnya, parameter model yang tetap)
model_params = (0.5, 1.2, 0.8)

# Set digunakan untuk meyimpan label unik dalam dataset
labels = {"A", "B", "C"}

# Stack (menggunakan list) untuk menyimpan data pelatihan
stack = []
stack.append(data_list[0])
stack.append(data_list[1])
print("Stack Pop :", stack.pop())

# Queue menggunakan deque untuk antrean data batch training
queue = deque(data_list)
print("Queue Popleft :", queue.popleft()) # mengambil element pertama

# Dictionery untuk menyimpan data
label_dict = {"A" : 0, "B" : 1, "C" : 2}
encoded_labels = [label_dict[label] for _, label in data_list]

# Comprehensions untuk normalisasi data
normalized_data = [(x / max(data_array.flatten()),label) for x, label in data_list]

# Generator Expression untuk membaca data secara efisien
data_stream = (random.random()for _ in range(10))

# Output hasil
print("Data Array:\n", data_array)
print("Normalized Data:\n", normalized_data)
print("Encoded Labels:\n", encoded_labels)