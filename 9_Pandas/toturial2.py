" BAGAIMANA CARA MEMBACA DAN MENULIS DATA TABULAR "

import pandas as pd

df = pd.read_csv('kapal_titanic.csv')

" Saya ingin melihat 8 baris pertama pandas DataFrame "
print(df.head(8))

" Saya ingin melihat 10 baris terakhir "
print(df.tail(10))

" Melihat tipe data yang ada pada DataFrame"
print(df.dtypes)

"Membuat data csv ke spreadsheet"
df.to_excel('titanic.xlsx', sheet_name="passengers", index=False)

"Membaca isi dalam data excel"
data_excel = pd.read_excel("titanic.xlsx", sheet_name="passengers")
print(data_excel.head(10))

"Metode info() memberikan informasi teknis tentang DataFrame"
print(data_excel.info())