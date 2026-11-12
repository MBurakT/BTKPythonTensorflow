# instance & attribute
class SuperKahraman():
    ozel_guc = "Gorunmezlik"

    def __init__(self, isim, yas, meslek):
        print("init çagirildi")
        self.isim = isim
        self.yas = yas
        self.meslek = meslek

    def ornek_metod(self):
        print(f"Ben super kahramanim ve meslegim: {self.meslek}")


superman = SuperKahraman("Superman", 30, "Gazeteci")
superman.isim = "Clark Kent"
print(superman.isim)
superman.ozel_guc = "Ucabiliyor"
print(superman.ozel_guc)
superman.ornek_metod()
