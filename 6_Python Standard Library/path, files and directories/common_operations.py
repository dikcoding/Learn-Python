import os
from pathlib import Path

# Program gabungan modul os dan pathlib

def create_directory(path):
    # Membuat direktori menggunakan pathlib
    path = Path(path)
    if not path.exists():
        path.mkdir(parents=True)
        print(f"Direktori {path} berhasil dibuat.")
    else:   
        print(f"Direktori {path} sudah ada.")

def create_file(path, content):
    # Membuat file dan menulis konten menggunakan pathlib
    path = Path(path)
    path.write_text(content)
    print(f"File {path} berhasil dibuat dengan konten.")

def read_file(path):
    # Membaca konten file menggunakan pathlib
    path = Path(path)
    if path.exists() and path.is_file():
        content = path.read_text()
        print(f"Konten file {path}:\n{content}")
    else:
        print(f"File {path} tidak ditemukan.")

def list_directory_contents(path):
    # Mendapatkan daftar file dan direktori dalam direktori tertentu menggunakan os
    path = Path(path)
    if path.exists() and path.is_dir():
        entries = os.listdir(path)
        print(f"Daftar file dan direktori dalam {path}:")
        for entry in entries:
            print(entry)
    else:
        print(f"Direktori {path} tidak ditemukan.")

def delete_directory(path):
    # Menghapus direktori menggunakan pathlib
    path = Path(path)
    if path.exists() and path.is_dir():
        for sub in path.iterdir():
            if sub.is_dir():
                delete_directory(sub)
            else:
                sub.unlink()
        path.rmdir()
        print(f"Direktori {path} berhasil dihapus.")
    else:
        print(f"Direktori {path} tidak ditemukan atau bukan direktori.")

def delete_file(path):
    # Menghapus file menggunakan pathlib
    path = Path(path)
    if path.exists() and path.is_file():
        path.unlink()
        print(f"File {path} berhasil dihapus.")
    else:
        print(f"File {path} tidak ditemukan atau bukan file.")

if __name__ == "__main__":
    # Contoh penggunaan
    create_directory("example_directory")
    create_file("example_directory/example_file.txt", "Ini adalah contoh teks.")
    read_file("example_directory/example_file.txt")
    list_directory_contents("example_directory")
    delete_file("example_directory/example_file.txt")
    delete_directory("example_directory")