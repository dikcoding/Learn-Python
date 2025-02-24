" Bagaimana cara memilih subset dari DataFrame "

import pandas as pd

df = pd.read_csv('kapal_titanic.csv')

print(df.head(10))

"Mengambil kolom yang di inginkan"
print("-----------------------------------")
print(df['age'])

print("-----------------------------------")
print("Ini data type : \n", df.dtypes[['sex', 'age']])
print("-----------------------------------")
print(df.shape)

" Bagaimana cara memfilter baris tertentu dari DataFrame "

"Saya tertarik pada penumpang yang berusia lebih dari 35 tahun. "
above_35 = df[df["age"] > 35]
print("-----------------------------------")
print(above_35.head())
print("-----------------------------------")
print(above_35.shape)

" Saya tertarik dengan penumpang Titanic dari kelas deck 2 dan 3. "
" Fungsi isin() mengembalikan nilai True untuk setiap baris nilai yang ada dalam daftar yang disediakan "
print("-----------------------------------")
class_23 = df[df['pclass'].isin([2,3])]
print(class_23.head())

" pemfilteran berdasarkan baris yang kelasnya adalah 2 dan 3, seperti di atas "
print("-----------------------------------")
class_filter = df[(df["pclass"] == 2) | (df["pclass"] == 3)]
print(class_filter.head())

"""
Saat menggabungkan beberapa pernyataan kondisional, setiap kondisi harus diapit oleh tanda kurung (). 
Selain itu, Anda tidak dapat menggunakan or / and tetapi perlu menggunakan oroperator | dan and operator &.
"""

print("-----------------------------------")
" Fungsi notna() kondisional mengembalikan True untuk setiap baris ynag nilainya bukan Null nilai "
age_notna = df[df["age"].notna()]
print(age_notna.head())
print("Nilai yang hilang karena hanya mengambil nilai True saja :", age_notna.shape)

" Saya tertarik dengan sex, age penumpang yang berusia lebih dari 35 tahun "
adult_filtered = df.loc[df['age'] > 35, ["sex", "age"]]
print(adult_filtered.head())

" Saya tertarik pada baris 10 hingga 25 dan kolom 3 hingga 5 "
" ini disebut metode index-based selection "
location = df.iloc[9:25, 2:5]
print(location)