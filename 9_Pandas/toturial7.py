" Cara Membentuk Ulang Tata Letak Tabel "
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("kapal_titanic.csv")

print(titanic.head())

air_quality = pd.read_csv("air_quality_no2.csv")

print(air_quality.head(10))

" Saya ingin mengurutkan data Titanic menurut usia penumpang "

print(titanic.sort_values(by="age").head())
print(titanic.sort_values(by=["pclass", "age"]).head())

# Ubah format data menjadi format long (parameter-value)
air_quality_long = air_quality.melt(id_vars="datetime", var_name="location", value_name="value")

# Ambil hanya data NO2 yang tidak NaN
no2 = air_quality_long.dropna()

no2_subset = no2.sort_index().groupby("location").head()

print(no2_subset.pivot(columns="location", values="value").plot()) # pivot() ini murni membentuk ulang data (index/kolom)
plt.show()