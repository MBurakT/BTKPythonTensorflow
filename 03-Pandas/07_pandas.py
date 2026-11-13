import pandas as pd
import numpy as np

maas_sozluk = {
    "Isim": ["Atil", "Zeynep", "Mehmet", "Ahmet"],
    "Departman": ["Yazilim", "Satis", "Pazarlama", "Yazilim"],
    "Maas": [200, 300, 400, 500]
}

maas_dataframe = pd.DataFrame(maas_sozluk)
print(maas_dataframe)
print(maas_dataframe["Departman"].unique())
print(maas_dataframe["Departman"].nunique())
print(maas_dataframe["Departman"].value_counts())


def brutten_nete(maas: int) -> float:
    return maas * 0.66


print(maas_dataframe["Maas"].apply(brutten_nete))
print(maas_dataframe.isnull())
print()

yeni_veri = {
    "Karakter Sinifi": ["South Park", "South Park", "Simpson", "Simpson"],
    "Karakter Ismi": ["Cartman", "Kenny", "Homer", "Bart"],
    "Karakter Yas": [9, 10, 50, 20]
}

karakter_df = pd.DataFrame(yeni_veri)
print(karakter_df)
print(karakter_df.pivot_table(
    values="Karakter Yas",
    index=["Karakter Sinifi", "Karakter Ismi"],
    aggfunc=np.sum
))
