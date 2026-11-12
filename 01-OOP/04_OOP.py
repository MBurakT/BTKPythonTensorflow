# Polymorphism
class Elma:
    def __init__(self, isim):
        self.isim = isim

    def bilgi_ver(self):
        return self.isim + " 100 kaloridir."


class Muz:
    def __init__(self, isim):
        self.isim = isim

    def bilgi_ver(self):
        return self.isim + " 150 kaloridir."


elma = Elma("elma")
print(elma.bilgi_ver())
print()

muz = Muz("muz")
print(muz.bilgi_ver())
print()

meyve_listesi = [elma, muz]

for meyve in meyve_listesi:
    print(meyve.bilgi_ver())
