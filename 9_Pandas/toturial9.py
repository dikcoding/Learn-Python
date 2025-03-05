import pandas as pd
import matplotlib.pyplot as plt

# Membaca data
air_quality = pd.read_csv("air_quality_no2_long.csv")

# Mengganti nama kolom
air_quality = air_quality.rename(columns={"date.utc": "datetime"})

# Menampilkan lima baris pertama
print(air_quality.head())

# Menampilkan daftar kota unik
print(air_quality.city.unique())

# Mengubah kolom 'datetime' menjadi tipe datetime
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
print(air_quality)

tes = air_quality["datetime"].min(), air_quality["datetime"].max()
print(tes)

PengukuranBulan = air_quality["month"] = air_quality["datetime"].dt.month
print(PengukuranBulan.head())

# Menghitung statistik N02
No2 = air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean()
print(No2)

fig, axs = plt.subplots(figsize=(12, 4))
air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)
plt.xlabel("Hour of the day")
plt.ylabel("$NO_2 (µg/m^3)$")
# plt.show()

no_2 = air_quality.pivot(index="datetime", columns="location", values="value")
no_2.index.year, no_2.index.weekday
no_2["2019-05-20":"2019-05-21"].plot();

"""
Metodenya resample()mirip dengan operasi groupby:
ini menyediakan pengelompokan berdasarkan waktu, dengan menggunakan string (misalnya M, 5H,…) yang mendefinisikan frekuensi target
ini memerlukan fungsi agregasi seperti mean, max,…
"""
monthly_max = no_2.resample("ME").max()
monthly_max.index.freq
no_2.resample("D").mean().plot(style="-o", figsize=(10, 5))
plt.show()