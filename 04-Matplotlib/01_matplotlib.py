import matplotlib.pyplot as plt
import numpy as np

yas_listesi = [10, 20, 30, 30, 30, 40, 50, 60, 70, 75]
kilo_listesi = [20, 60, 80, 85, 86, 87, 70, 90, 95, 90]

numpy_yas_listesi = np.array(yas_listesi)
numpy_kilo_listesi = np.array(kilo_listesi)

print(numpy_yas_listesi)
print(numpy_kilo_listesi)

plt.plot(numpy_yas_listesi, numpy_kilo_listesi, "g")  # g -> green
plt.xlabel("Yas")
plt.ylabel("Kilo")
plt.ylabel("Kilo'nun Yasa Gore Degisim Grafigi")
plt.show()
