from collections import deque

data_cuaca = [
    {"kota": "Jakarta", "suhu": 30, "kelembaban": 80, "hujan": True},
    {"kota": "Bandung", "suhu": 22, "kelembaban": 75, "hujan": False},
    {"kota": "Surabaya", "suhu": 32, "kelembaban": 70, "hujan": True},
    {"kota": "Yogyakarta", "suhu": 28, "kelembaban": 78, "hujan": False}
]

# 1. List comprehension untuk mengambil kota yang mengalami hujan
cuaca_hujan = [kota["kota"] for kota in data_cuaca if kota.get("hujan")]
print(cuaca_hujan)

# 2. Generator expression untuk menghitung rata-rata suhu
rata_rata_suhu = sum(data["suhu"] for data in data_cuaca) / len(data_cuaca)
print("Rata-rata suhu di kota :", rata_rata_suhu)

# 3. Stack untuk menampilkan data kota dalam urutan terbalik
stack = []
for data in data_cuaca:
    stack.append(data)

print("\nData kota dalam urutan terbalik (menggunakan stack): ")
while stack:
    print(stack.pop())

# 4. Queue untuk menampilkan data kota dalam urutan yang sama seperti dalam list awal
queue = deque(data_cuaca)
print("\nData kota dalam urutan awal (menggunakan queue):")
while queue:
    print(queue.popleft())
