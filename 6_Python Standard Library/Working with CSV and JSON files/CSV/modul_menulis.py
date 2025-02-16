import csv

# Data yang akan ditulis ke dalam file CSV
data = [
    {'Nama': 'Alice', 'Usia': 30, 'Kota': 'New York'},
    {'Nama': 'Bob', 'Usia': 25, 'Kota': 'Los Angeles'},
    {'Nama': 'Charlie', 'Usia': 35, 'Kota': 'Chicago'}
]

# Membuka file CSV dalam mode tulis
with open('output.csv', mode='w', newline='') as file:
    fieldnames = ['Nama', 'Usia', 'Kota']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Menulis header
    csv_writer.writeheader()
    
    # Menulis baris-barisnya
    for row in data:
        csv_writer.writerow(row)