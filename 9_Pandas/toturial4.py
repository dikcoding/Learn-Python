" Bagaimana cara membuat Plot di Pandas"

import pandas as pd
import matplotlib.pyplot as plt

""" 
Penggunaan (index_col) dan (parse_dates) untuk menentukan column pertama (0) sebagai indeks hasil DataFrame dan  
dan mengonversi tanggal dalam kolom menjadi Timestamp objek
"""
air_quality = pd.read_csv('air_quality_no2.csv', index_col= 0, parse_dates = True )
print(air_quality.head())

" Pemeriksaan visual data secara cepat "
# air_quality.plot()
# plt.show()
print("_________________________________________________________________________")

" Membuat Plot hanya kolom tabel data dengan data Paris "
# air_quality["station_paris"].plot()
# plt.show()

print("_________________________________________________________________________")
" Membandingkan secara visual NO2 nilai yang diukur di London Versus Paris "
# air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
" (scatter) digunakan untuk membuat plot yaitu grafik dengan titik-titik yang menunjukkan hubungan antara dua variabel. "
" (alpah) adalah tingkat transparansi titik-titiknya (0 = transparan, 1 = tidak transparan) "
# plt.show()

print("_________________________________________________________________________")
" DataFrame.plot.box() metode untuk menggambarkan secara grafis kelompok data numerik melalui kuartilnya "
# air_quality.plot.box()
# plt.show()

print("_________________________________________________________________________")
" Membuat subplot terpisah "
" (subplots) membuat setiap kolom menjadi grafik terpisah "
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()