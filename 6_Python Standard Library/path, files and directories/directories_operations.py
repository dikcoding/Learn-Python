import os

# Membuat direktori baru
os.mkdir("new_directory")

# Membuat direktori bertingkat
os.makedirs("parent_directory/child_directory")

# Menghapus direktori kosong
os.rmdir("new_directory")

# Menghapus direktori bertingkat
os.removedirs("parent_directory/child_directory")

# Mendapatkan daftar file dan direktori dalam direktori tertentu
entries = os.listdir(".")
print("Daftar file dan direktori dalam direktori saat ini:")
for entry in entries:
    print(entry)

# Mengecek apakah sebuah path adalah direktori
is_dir = os.path.isdir("example_directory")
print(f"Apakah 'example_directory' adalah direktori: {is_dir}")

# Mengecek apakah sebuah path adalah file
is_file = os.path.isfile("example.txt")
print(f"Apakah 'example.txt' adalah file: {is_file}")