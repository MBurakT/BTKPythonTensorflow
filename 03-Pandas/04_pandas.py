import pandas as pd
import numpy as np

ilk_indeksler = ["Simpson", "Simpson", "Simpson",
                 "South Park", "South Park", "South Park"]

ic_indeksler = ["Homer", "Bart", "Marge", "Cartman", "Kenny", "Kyle"]
birlesmis_indeks = list(zip(ilk_indeksler, ic_indeksler))
print(birlesmis_indeks)
birlesmis_indeks = pd.MultiIndex.from_tuples(birlesmis_indeks)
print(birlesmis_indeks)
benim_cizgifilm_listem = [
    [40, "A"],
    [10, "B"],
    [30, "C"],
    [9, "D"],
    [10, "E"],
    [11, "F"]
]

cizgifilm_numpy_dizisi = np.array(benim_cizgifilm_listem)
cizgifilm_dataframe = pd.DataFrame(
    cizgifilm_numpy_dizisi,
    index=birlesmis_indeks,
    columns=["Yas", "Meslek"]
)
print(cizgifilm_dataframe)
print(cizgifilm_dataframe.loc["Simpson"])
print(cizgifilm_dataframe.loc["South Park"])
print(cizgifilm_dataframe.loc["South Park"].loc["Kenny"])
cizgifilm_dataframe.index.names = ["Film Adi", "İsim"]
print(cizgifilm_dataframe)
