import pandas as pd

air_quality_no2 = pd.read_csv("air_quality_no2_long.csv")

air_quality_pm25 = pd.read_csv("air_quality_pm25_long.csv")

# Menggabungkan data P02 dan PM25
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
print(air_quality.head())

# Periksa isi tebal
print('Shape of the ``air_quality_pm25`` table: ', air_quality_pm25.shape)
print('Shape of the ``air_quality_no2`` table: ', air_quality_no2.shape)
print('Shape of the resulting ``air_quality`` table: ', air_quality.shape)

# Mengurutkan data air_quality_pm25 dan air_quality_no2
urutanData = air_quality.sort_values("date.utc")
print(urutanData.head())

# Menggunakan Key pada metode (concet)
air_quality_ = pd.concat([air_quality_pm25, air_quality_no2], keys=["PM25", "NO2"])
print(air_quality_.head(10))
