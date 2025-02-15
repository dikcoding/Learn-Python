import csv

# Data yang akan ditulis ke dalam file CSV
data = [
    ['Nama', 'Usia', 'Kota'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Membuka file CSV dalam mode tulis
with open('output.csv', mode='w') as file:
    csv_writer = csv.writer(file)

    # Menulis baris-barisnya
    for row in data:
        csv_writer.writerow(row)
    
    # Ouput akan membuat file csv (output.csv)