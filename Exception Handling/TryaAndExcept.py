# untuk menangani exception, Python menyediakan blok try/except. Struktur dasarnya adalah.abs

try:
    # Kode yang mungkin menyebab error
    hasil = 10 / 2
except ZeroDivisionError:
    print("Terjadi kesalahan: Tidak bisa membagi dengan nol")


# kita bisa menagani lebih dari satu jenis exception dengan beberapa blok except:
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
except ZeroDivisionError:
    print("Error: Tidak bisa membagi nol")
except ValueError:
    print("Error: Input harus berupa angka")
except Exception as e:
    print(f"Kesalahan lain terjadi: {e}")

print("--------------------------")
# kadang kita ingin memunculkan exception sendiri menggunakan raise.
def cek_positif(angka):
    if angka < 0:
        raise ValueError("Angka tidak boleh negatif")
    return angka

try:
    cek_positif(-5)
except ValueError as e:
    print(f"Error: {e}")