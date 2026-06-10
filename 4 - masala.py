# 4-masala. Bank Hisobi
# BankHisob classi yarating. Atributlari: ism, balans=0.

# deposit(summa) - balansni oshiradi.

# yechib_ol(summa) - balansni kamaytiradi (agar yetarli bo'lsa).

# hisob() - hozirgi balansni qaytaradi.
# Hisob oching, unga 1000 qo'shing, 400 yeching.
import os
os.system("cls")

class BankHisob:
    def __init__(self, ism, balans=0):
        self.ism = ism
        self.balans = balans

    def deposit(self, summa):
        if summa > 0:
            self.balans += summa
            print(f"Hisobga {summa} qo'shildi.")
        else:
            print("Xato! Musbat summa kiriting.")

    def yechib_ol(self, summa):
        if summa <= self.balans:
            self.balans -= summa
            print(f"Hisobdan {summa} yechib olindi.")
        else:
            print(f"Uzr, hisobingizda mablag' yetarli emas! Hozirgi balans: {self.balans}")

    def hisob(self):
        return self.balans

mijoz = BankHisob("Asilbek") 

mijoz.deposit(1000)

mijoz.yechib_ol(400)

print("Yakuniy balans:", mijoz.hisob())