# inheritance
class Hayvan:
    def __init__(self):
        print("hayvan sinifi init cagirildi.")

    def method1(self):
        print("hayvan sinifi method1 cagirildi")

    def method2(self):
        print("hayvan sinifi method2 cagirildi")


class Kedi(Hayvan):
    def __init__(self):
        Hayvan.__init__(self)
        print("kedi sinifi init cagirildi.")

    def miyavla(self):
        print("miyav")

    # Override
    def method1(self):
        print("kedi sinifindaki method1 cagirildi.")


benim_hayvanim = Hayvan()
benim_hayvanim.method1()
benim_hayvanim.method2()
print()

benim_kedi = Kedi()
benim_kedi.method1()
benim_kedi.method2()
benim_kedi.miyavla()
