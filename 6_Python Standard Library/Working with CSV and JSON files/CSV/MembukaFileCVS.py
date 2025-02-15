import csv

# Membuka file CSV dengan path lengkap
with open('d:/Belajar Python/6_Python Standard Library/Working with CSV and JSON files/contoh.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    
    # Membaca header
    header = next(csv_reader)
    print(f"Header: {header}")
    
    # Membaca baris-barisnya
    for row in csv_reader:
        print(row)

print()