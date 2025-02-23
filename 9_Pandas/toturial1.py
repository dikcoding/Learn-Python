"""
1. Impor paket, aliasimport pandas as pd
2. Tabel data disimpan sebagai pandasDataFrame
3. Setiap kolom dalam a DataFrameadalahSeries
4. Anda dapat melakukan sesuatu dengan menerapkan suatu metode ke suatu DataFrameatauSeries
"""

import pandas as pd

df = pd.read_csv('kapal_titanic.csv')

# Menampilkan ringkasan statistik data numerik
print("Menampilkan ringkasan statistik data :\n", df.describe())

# Menampilkan nilai unik dari kolom "survived"
print("manampilkan nilai unix :\n", df['survived'].unique())

# Menampilkan DataFrame
print("Menampilkan DataFrame :\n", df)