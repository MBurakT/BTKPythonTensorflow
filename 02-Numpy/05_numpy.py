import numpy as np

benim_dizim = np.arange(0, 15)
print(benim_dizim)
print(benim_dizim[5])
print(benim_dizim[3:5])
print(benim_dizim[3:8])
benim_dizim[3:8] = -5
print(benim_dizim)
baska_dizi = np.arange(0, 24)
print(baska_dizi)
slicing_dizisi = baska_dizi[4:9]
print(slicing_dizisi)
slicing_dizisi[:] = 700
print(slicing_dizisi)
print(baska_dizi)
ornek_dizi = np.arange(0, 24)
print(ornek_dizi)
ornek_dizi_kopya = ornek_dizi.copy()
print(ornek_dizi_kopya)
ornek_dizi_kopya_slicing = ornek_dizi_kopya[3:6]
print(ornek_dizi_kopya_slicing)
ornek_dizi_kopya_slicing[:] = 800
print(ornek_dizi_kopya_slicing)
print(ornek_dizi_kopya)
print(ornek_dizi)
