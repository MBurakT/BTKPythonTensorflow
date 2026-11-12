class Kopek():
    yil_carpani = 7

    def __init__(self, yas=1):
        self.yas = yas

    def insan_yasi_hesapla(self):
        return self.yas * Kopek.yil_carpani


benim_kopek = Kopek()
print(benim_kopek.yas)
benim_kopek = Kopek(3)
print(benim_kopek.yas)
print(benim_kopek.insan_yasi_hesapla())
