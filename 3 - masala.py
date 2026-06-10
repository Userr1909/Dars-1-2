# 3-masala. Avtomobil
# Avtomobil classi tuzing. Atributlari: model, yil, tezlik.

# tezlashtir() - tezlikni +10 oshiradi.

# sekinlashtir() - tezlikni -10 kamaytiradi.

# info() - avtomobil model, yil va tezligini chiqaradi.
# Avtomobilni 3 marta tezlashtiring, keyin 1 marta sekinlashtiring.
import os
os.system("cls")

class Avtomobil:
    def __init__(self, model, yil, tezlik):
        self.model = model
        self.yil = yil
        self.tezlik = tezlik

    def tezlashtir(self):
        self.tezlik += 10
        print(f"Tezlik oshirildi! Hozirgi tezlik: {self.tezlik} km/s")

    def sekinlashtir(self):
        if self.tezlik >= 10:
            self.tezlik -= 10
        else:
            self.tezlik = 0
        print(f"Tezlik kamaytirildi! Hozirgi tezlik: {self.tezlik} km/s")

    def info(self):
        print(f"\nAvtomobil haqida")
        print(f"Model: {self.model}")
        print(f"Yili: {self.yil}")
        print(f"Tezligi: {self.tezlik} km/s")

avto = Avtomobil("BYD Chazor", 2024, 60)

avto.info()
print("\n ish boshlandi")
avto.tezlashtir()
avto.tezlashtir()
avto.tezlashtir()
avto.sekinlashtir()
