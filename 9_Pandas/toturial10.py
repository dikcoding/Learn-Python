import pandas as pd

titanic = pd.read_csv("kapal_titanic.csv")
print(titanic.head())

"Jadikan semua karakter nama menjadi huruf kecil."
titanic["sex"].str.lower()

aksesMale = titanic["sex"].str.contains("male")
melihatNamaPanjang = titanic["sex"].str.len()
print(melihatNamaPanjang)
print(aksesMale)
print(titanic["sex"])