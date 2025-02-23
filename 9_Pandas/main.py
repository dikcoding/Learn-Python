import pandas as pd
from sqlalchemy import create_engine

# Pastikan nama file benar (bukan .cvs)
df = pd.read_csv('kapal_titanic.csv')

"Menampilkan 5 baris pertama dari dataset"
# print(df.head()) 

"Menampilkan 5 baris terakhir dari dataset"
# print(df.tail())

"Menampilkan semua dataset"
# pd.set_option('display.max_rows', None)
# print(df) 

"Mamindahkan data ke csv yang baru. bisa juga memindahkan data ke excel atau json dll"
# df.to_csv('datacsv.csv', index=False)

"Memindahkan data ke excel"
# df.to_excel('dataexcel.xlsx', index=False, sheet_name='asek')

"Membaca file HTML"
# dfhtml = pd.read_html('https://www.fdic.gov/bank-failures/failed-bank-list')
# pd.set_option('display.max_rows', None)
# print(dfhtml)

"Merubah file csv ke sql"
# Buat koneksi ke database SQLite (bisa di memori atau file)
mesin = create_engine("sqlite:///:memory:")  # Hanya sementara

# Simpan DataFrame ke SQL
df.to_sql("datasql", mesin, if_exists="replace", index=False)

# Ambil data kembali dari database untuk dicek
df_sql = pd.read_sql("SELECT * FROM datasql", mesin)

print(df_sql.head())
