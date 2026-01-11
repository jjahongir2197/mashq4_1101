class Mahsulot:
    def __init__(self, nomi, narx):
        self.nomi = nomi
        self.narx = narx


class Buyurtma:
    def __init__(self):
        self.mahsulotlar = []

    def mahsulot_qoshish(self, mahsulot, soni):
        self.mahsulotlar.append((mahsulot, soni))
        print(f"{mahsulot.nomi} qo'shildi ({soni} dona)")

    def jami_summa(self):
        jami = 0
        for mahsulot, soni in self.mahsulotlar:
            jami += mahsulot.narx * soni
        return jami

    def chek(self):
        print("\n--- CHEK ---")
        for mahsulot, soni in self.mahsulotlar:
            print(f"{mahsulot.nomi} x {soni} = {mahsulot.narx * soni} so'm")
        print(f"Jami: {self.jami_summa()} so'm")


olma = Mahsulot("Olma", 5000)
banan = Mahsulot("Banan", 8000)

buyurtma = Buyurtma()
buyurtma.mahsulot_qoshish(olma, 3)
buyurtma.mahsulot_qoshish(banan, 2)

buyurtma.chek()
