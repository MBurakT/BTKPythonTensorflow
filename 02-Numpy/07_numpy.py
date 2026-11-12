import numpy as np

yeni_dizi = np.random.randint(1, 100, 20)
print(yeni_dizi)
print(yeni_dizi > 24)
sonuc_dizi = yeni_dizi > 24
print(yeni_dizi[sonuc_dizi])
print(yeni_dizi[yeni_dizi > 24])
son_dizi = np.arange(0, 24)
print(son_dizi)
print(son_dizi + son_dizi)
print(son_dizi * son_dizi)
print(son_dizi - son_dizi)
print(son_dizi / son_dizi)
print(np.sqrt(son_dizi))
print(np.max(son_dizi))
print(np.min(son_dizi))
