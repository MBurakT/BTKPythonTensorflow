import matplotlib.pyplot as plt
import numpy as np

numpy_dizisi_1 = np.linspace(0, 10, 20)
numpy_dizisi_2 = numpy_dizisi_1 ** 2

benim_figure, benim_eksen = plt.subplots()
benim_eksen.plot(numpy_dizisi_1, numpy_dizisi_2, color="#3A95A8", alpha=0.3)
benim_eksen.plot(numpy_dizisi_2, numpy_dizisi_1, color="#C96F23")
# plt.show()

plt.close()
yeni_figure, yeni_eksen = plt.subplots()
yeni_eksen.plot(numpy_dizisi_1, numpy_dizisi_1 + 2, color="blue", linewidth=5)
yeni_eksen.plot(numpy_dizisi_1, numpy_dizisi_1 + 3, color="red", linewidth=1)
yeni_eksen.plot(numpy_dizisi_1, numpy_dizisi_1 + 4, color="#C96F23", linestyle="-.")
yeni_eksen.plot(numpy_dizisi_1, numpy_dizisi_1 + 5, color="#3A95A8", linestyle=":")
yeni_eksen.plot(numpy_dizisi_1, numpy_dizisi_1 + 6, color="purple", linestyle="--")
yeni_eksen.plot(numpy_dizisi_1, numpy_dizisi_1 + 7, color="#000000", linestyle="--", marker="o", markerfacecolor="red")
yeni_eksen.plot(numpy_dizisi_1, numpy_dizisi_1 + 8, color="#000000", linestyle="--", marker="+", markerfacecolor="red", markersize=4)
# plt.show()

# scatter
plt.close()
plt.scatter(numpy_dizisi_1, numpy_dizisi_2)
# plt.show()

# histogram
plt.close()
yeni_dizi = np.random.randint(0, 100, 50)
plt.hist(yeni_dizi)
# plt.show()

# boxplot
plt.close()
plt.boxplot(yeni_dizi)
plt.show()