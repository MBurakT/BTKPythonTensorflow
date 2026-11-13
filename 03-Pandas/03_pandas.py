import pandas as pd
import numpy as np

data = np.random.randn(4, 3)
print(data)

data_frame = pd.DataFrame(data)
print(data_frame)
print(data_frame[0])
print(type(data_frame[0]))
print()

yeni_data_frame = pd.DataFrame(
    data,
    index=["Atil", "Zeynep", "Atlas", "Mehmet"],
    columns=["Maas", "Yas", "Calisma Saati"]
)
print(yeni_data_frame)
print(yeni_data_frame["Yas"])
print(yeni_data_frame["Calisma Saati"])
print(yeni_data_frame[["Maas", "Yas"]])
print(yeni_data_frame.loc["Atil"])
print(yeni_data_frame.loc["Zeynep"])
print(yeni_data_frame.iloc[1])
print()

yeni_data_frame["Emeklilik Yasi"] = yeni_data_frame["Yas"] * 2
print(yeni_data_frame)
yeni_data_frame = yeni_data_frame.drop("Emeklilik Yasi", axis=1)
print(yeni_data_frame)
yeni_data_frame = yeni_data_frame.drop("Mehmet")
print(yeni_data_frame)

print(yeni_data_frame.loc["Atil"])
print(yeni_data_frame.loc["Atil"]["Yas"])
print(yeni_data_frame.loc["Atlas", "Yas"])
print()

print(yeni_data_frame[yeni_data_frame < 0])
print(yeni_data_frame["Yas"])
print(yeni_data_frame["Yas"] > 0)
print(yeni_data_frame[yeni_data_frame["Yas"] > 0])
print(yeni_data_frame[yeni_data_frame["Calisma Saati"] > 0])
print()

print(yeni_data_frame.reset_index())
print()

yeni_indeks_listesi = ["Ati", "Zey", "Atl"]
yeni_data_frame["Yeni Indeks"] = yeni_indeks_listesi
print(yeni_data_frame)
yeni_data_frame = yeni_data_frame.set_index("Yeni Indeks")
print(yeni_data_frame)
