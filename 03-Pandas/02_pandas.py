import pandas as pd
import numpy as np

print(pd.Series(["Atil", "Atlas", "Osman"]))
print(pd.Series(["Atil", "Atlas", "Osman"], [1, 2, 3]))
print()

yarisma_sonucu1 = pd.Series([10, 5, 1], ["Atil", "Atlas", "Osman"])
print(yarisma_sonucu1)

yarisma_sonucu2 = pd.Series([20, 10, 8], ["Atil", "Atlas", "Osman"])
print(yarisma_sonucu2)

print(yarisma_sonucu2["Atlas"])
print()

son_sonuc = yarisma_sonucu1 + yarisma_sonucu2
print(son_sonuc)
print()

farkli_series = pd.Series([20, 30, 40, 50], ["a", "b", "c", "d"])
farkli_series2 = pd.Series([10, 5, 3, 1], ["a", "c", "f", "g"])

print(farkli_series)
print(farkli_series2)

print(farkli_series + farkli_series2)
