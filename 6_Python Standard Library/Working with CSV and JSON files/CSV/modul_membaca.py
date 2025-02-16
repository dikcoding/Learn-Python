import csv

# Membuka file CSV
with open('d:/Belajar Python/6_Python Standard Library/Working with CSV and JSON files/CSV/test.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    # Membaca baris-barisnya
    for row in csv_reader:
        print(row)