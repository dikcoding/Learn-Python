from sains.matematika import scientific
from sains.matematika import basic

hasil_tambah = basic.tambah(1,2,3,4,45)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = basic.kali(1,3,4,5,6)
print(f"hasil kali = {hasil_kali}")

pangkat_3 = scientific.pangkat(3)
print(f"hasil pangkat 3 = {pangkat_3(5)}")


import sains # ini ngambil dari -> from . import pisika
hasil_pisika = sains.pisika.gaya(10,9.8)
print(f"hasil pisika = {hasil_pisika}")