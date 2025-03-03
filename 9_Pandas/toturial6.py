" Menghitung Statistik Ringkasan "
import pandas as pd

titanic = pd.read_csv("kapal_titanic.csv")
print(titanic.head())

# Mencari rata-rata colum (age)
print(titanic['age'].mean())

# Menghitung rata-rata 2 kolom
print(titanic[['age', 'fare']].median())

# Memberikan data singkat numerik
print(titanic[['age', 'fare']].describe())

print(titanic.agg(
    {
        "age": ["min", "max", "median", "skew"],
        "fare": ["min", "max", "median", "mean"],
    }
))

" Mencari usia rata-rata penumpang Titanic pria dan wanita "
print(titanic[["sex", "age"]].groupby("sex").mean())

print(titanic.groupby("sex")["age"].mean(numeric_only=True))

"Berapa harga tiket rata-rata untuk setiap kombinasi kelas jenis kelamin dan kabin?"
print(titanic.groupby(["sex",'pclass'])["fare"].mean())

"Berapa jumlah penumpang di setiap kelas kabin?"
print(titanic["pclass"].value_counts())