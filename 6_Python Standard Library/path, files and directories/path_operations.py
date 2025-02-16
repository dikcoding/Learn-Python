import os

# Menggabungkan beberapa bagian path
path = os.path.join("folder1", "folder2", "file.txt")
print(f"Gabungan path: {path}")

# Mendapatkan direktori dari sebuah path 
directori = os.path.dirname(path) # dirname itu sama kek split (mendapatkan direktori dari sebuah path file)
print(f"Directories : {directori}")

# Mendapatkan name file dari sebuah path
fileName = os.path.basename(path)
print(f"Name File: {fileName}")

# Mengecek apakah sebuah path ada
path_exists = os.path.exists(path)
print(f"Apakah path ada: {path_exists}")

# Mengecek apakah sebuah path adalah file
is_file = os.path.isfile(path)
print(f"Apakah path adalah file : {is_file}")

# Mengecek apakah sebuah path adalah direktori
is_dir = os.path.isdir(directori)
print(f"Apakah path adalah direktori :  {is_dir}")
