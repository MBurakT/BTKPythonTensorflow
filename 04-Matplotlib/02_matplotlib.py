import matplotlib.pyplot as plt
import numpy as np

numpy_dizisi_1 = np.linspace(0, 10, 20)
numpy_dizisi_2 = numpy_dizisi_1 ** 2

print(numpy_dizisi_1)
print(numpy_dizisi_2)

plt.plot(numpy_dizisi_1, numpy_dizisi_2, "g--")
# plt.show()

plt.close()
plt.subplot(1, 2, 1)
plt.plot(numpy_dizisi_1, numpy_dizisi_2, "r*-")
plt.subplot(1, 2, 2)
plt.plot(numpy_dizisi_2, numpy_dizisi_1, "g.-")
# plt.show()

plt.close()
benim_figure = plt.figure()
figure_axes = benim_figure.add_axes([0.2, 0.2, 0.6, 0.6])
figure_axes.plot(numpy_dizisi_1, numpy_dizisi_2, "g")
figure_axes.set_xlabel("X Ekseni")
figure_axes.set_ylabel("Y Ekseni")
figure_axes.set_title("Grafik Basligi")
# plt.show()

plt.close()
figure_2 = plt.figure()

eksen_1 = figure_2.add_axes([0.1, 0.1, 0.7, 0.7])
eksen_2 = figure_2.add_axes([0.2, 0.4, 0.3, 0.3])

eksen_1.plot(numpy_dizisi_1, numpy_dizisi_2, "g")
eksen_1.set_xlabel("X Ekseni")
eksen_1.set_ylabel("Y Ekseni")
eksen_1.set_title("Ana Grafik Baslik")

eksen_2.plot(numpy_dizisi_2, numpy_dizisi_1, "b")
eksen_2.set_xlabel("X Ekseni Yan")
eksen_2.set_ylabel("Y Ekseni Yan")
eksen_2.set_title("Yan Grafik Baslik")

# plt.show()

plt.close()
benim_figure, benim_eksenler = plt.subplots(nrows=1, ncols=2)
print(type(benim_eksenler))
for eksen in benim_eksenler:
    eksen.plot(numpy_dizisi_1, numpy_dizisi_2, "g")
    eksen.set_xlabel("X Ekseni")
plt.tight_layout()
# plt.show()

plt.close()
yeni_figure = plt.figure(dpi=100)
yeni_eksen = yeni_figure.add_axes([0.1, 0.1, 0.8, 0.8])
yeni_eksen.plot(numpy_dizisi_1, numpy_dizisi_2, label="numpy_dizisi ** 2")
yeni_eksen.plot(numpy_dizisi_1, numpy_dizisi_1 ** 3, label="numpy_dizisi ** 3")
yeni_eksen.legend(loc=2)
plt.show()
yeni_figure.savefig("benim_figure", dpi=200)
