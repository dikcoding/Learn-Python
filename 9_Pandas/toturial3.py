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
print("-----------------------------------")
class_23 = df[df['pclass'].isin([2,3])]
print(class_23.head())
