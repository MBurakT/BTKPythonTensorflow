import pandas as pd
import numpy as np

sozluk1 = {
    "Isim": ["Ahmet", "Mehmet", "Zeynep", "Atil"],
    "Spor": ["Kosu", "Yüzme", "Kosu", "Basketbol"],
    "Kalori": [100, 200, 250, 150]
}

sozluk2 = {
    "Isim": ["Osman", "Levent", "Atlas", "Fatma"],
    "Spor": ["Kosu", "Yüzme", "Kosu", "Basketbol"],
    "Kalori": [100, 200, 250, 150]
}

sozluk3 = {
    "Isim": ["Ayse", "Mahmut", "Duygu", "Nur"],
    "Spor": ["Kosu", "Yüzme", "Badminton", "Tenis"],
    "Kalori": [400, 500, 100, 200]
}

dataframe1 = pd.DataFrame(sozluk1, index=[0, 1, 2, 3])
dataframe2 = pd.DataFrame(sozluk2, index=[4, 5, 6, 7])
dataframe3 = pd.DataFrame(sozluk3, index=[8, 9, 10, 11])

# concatenation
print(pd.concat([dataframe1, dataframe2, dataframe3]))
# print(pd.concat([dataframe1, dataframe2, dataframe3], axis=1))
print()

sozluk4 = {
    "Isim": ["Ahmet", "Mehmet", "Zeynep", "Atil"],
    "Spor": ["Kosu", "Yüzme", "Kosu", "Basketbol"]
}

sozluk5 = {
    "Isim": ["Ahmet", "Mehmet", "Zeynep", "Atil"],
    "Kalori": [100, 200, 250, 150]
}

dataframe4 = pd.DataFrame(sozluk4)
dataframe5 = pd.DataFrame(sozluk5)

# merge
print(pd.merge(dataframe4, dataframe5, on="Isim"))
