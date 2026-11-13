import pandas as pd
import numpy as np

# Series
benim_sozlugum = {"Atil": 50, "Zeynep": 40, "Mehmet": 30}
print(pd.Series(benim_sozlugum))
print(type(pd.Series(benim_sozlugum)))

benim_yaslarim = [50, 40, 30]
benim_isimlerim = ["Atil", "Zeynep", "Mehmet"]
print(pd.Series(benim_yaslarim))
print(pd.Series(benim_yaslarim, benim_isimlerim))
print(pd.Series(data=benim_yaslarim, index=benim_isimlerim))

numpy_dizisi = np.array([50, 40, 30])
print(numpy_dizisi)
print(pd.Series(numpy_dizisi))
print(pd.Series(numpy_dizisi, benim_isimlerim))
