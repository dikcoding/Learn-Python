# Membuka dan Menulis ke dalam file
with open("example.txt" , "w") as file:
    file.write("ini adalah contoh text.\n")
    file.write("ini adalah contoh kedua.\n")

# Membaca dari file
with open("example.txt", "r") as file:
    content = file.read()
    print("Konten File : ")
    print(content)

# Membaca ke file yang ada
with open("example.txt", "a") as file:
    file.write("ini adalah baris tambahan.\n")

# Membaca file baris per baris
with open("example.txt", "r") as file:
    for line in file:
        print(f"Baris: {line.strip()}")