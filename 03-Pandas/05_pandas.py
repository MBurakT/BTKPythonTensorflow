import pandas as pd
import numpy as np

sozluk = {
    "Istanbul": [30, 29, np.nan],
    "Ankara": [20, np.nan, 25],
    "Izmir": [40, 39, 38]
}
hava_durumu_dataframe = pd.DataFrame(sozluk)
print(hava_durumu_dataframe)
print(hava_durumu_dataframe.dropna())
print(hava_durumu_dataframe.dropna(axis=1))
print()

yeni_veri = {
    "Istanbul": [30, 29, np.nan],
    "Ankara": [20, np.nan, 25],
    "Izmir": [40, 39, 38],
    "Antalya": [45, np.nan, np.nan]
}
yeni_dataframe = pd.DataFrame(yeni_veri)
print(yeni_dataframe)
print(yeni_dataframe.dropna(axis=1, thresh=2))
print(yeni_dataframe.fillna(20))
print()

# groupby
maas_sozlugu = {
    "Departman": ["Yazilim", "Yazilim", "Pazarlama", "Pazarlama", "Hukuk", "Hukuk"],
    "Calisan Ismi": ["Ahmet", "Mehmet", "Atil", "Burak", "Zeynep", "Fatma"],
    "Maas": [100, 150, 200, 300, 400, 500]
}
maas_dataframe = pd.DataFrame(maas_sozlugu)
print(maas_dataframe)
grup_objesi = maas_dataframe.groupby("Departman")
print(grup_objesi.count())
print(grup_objesi["Maas"].mean())
print(grup_objesi["Maas"].min())
print(grup_objesi["Maas"].max())
print(grup_objesi.describe())
