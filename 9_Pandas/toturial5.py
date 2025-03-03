" Cara membuat kolom baru yang berasal dari kolom yang sudah ada "

import pandas as pd

air_quality = pd.read_csv('air_quality_no2.csv', index_col= 0, parse_dates = True )

air_quality["london_mg_per_cubic"] = air_quality["station_london"]
print(air_quality.head())

print("---------------------------------------------")
memeriksaRasio = air_quality["ratio_paris_antwerp"] = (air_quality["station_paris"] + air_quality["station_antwerp"])
print(memeriksaRasio.head())

print("---------------------------------------------")
air_quality_renamed = air_quality.rename(
    columns = {
        "station_antwerp" : "BETR801",
        "station_paris" : "FR04014",
        "station_london" : "London Wastminster",
    }
)
print(air_quality_renamed.head())
air_quality_rename = air_quality_renamed.rename(columns=str.lower) # membuat tulisan kecil
print(air_quality_rename.head())

