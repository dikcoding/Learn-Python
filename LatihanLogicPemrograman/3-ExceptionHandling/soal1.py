def bagi_angka():
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))

        # Cek apakah ada angka negatif
        if angka1 < 0 or angka2 < 0:
            raise ValueError("Angka tidak boleh negatif")
        
        
        hasil = angka1 / angka2
        print(f"Hasil pembagian: {hasil}")

    except ZeroDivisionError:
        print("Error: Tidak bisa membagi nol.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

bagi_angka()