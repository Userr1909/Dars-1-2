# 7-masala. Kutubxona tizimi. Bu masalada ikkita classni o'zaro bog'lab ishlatishingiz kerak bo'ladi.
# Kitob classi yarating (nomi, muallif).
# Kutubxona classi yarating:

# Atributlari: kitoblar (list) - kitoblar ro'yxatini o'zida saqlaydi.

# kitob_qoshish(kitob) - kitob obyektini qo'shadi.

# qidirish(nom) - nomi bo'yicha kitobni qidiradi.
# Kutubxonaga bir nechta kitob qo'shib, ulardan birini qidirib toping.
import os
os.system("cls")

class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif

class Kutubxona:
    def __init__(self):
        self.kitoblar = []

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)
        print(f"'{kitob.nomi}' kitobi kutubxonaga qo'shildi.")

    def qidirish(self, nom):
        for k in self.kitoblar:
            if k.nomi.lower() == nom.lower():
                return f"Topildi, Kitob: '{k.nomi}', Muallif: {k.muallif}"
        
        return "bunday kitob kutubxonada mavjud emas."

kutubxona = Kutubxona()
print("Kutubxona ishga tushdi\n")

k1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy")
k2 = Kitob("Mehrobdan Chayon", "Abdulla Qodiriy")
k3 = Kitob("Sariq devni minib", "Xudoyberdi To'xtaboyev")

kutubxona.kitob_qoshish(k1)
kutubxona.kitob_qoshish(k2)
kutubxona.kitob_qoshish(k3)

print("\nKitob Qidirish ishga tushdi")
qidirilayotgan_kitob = "Mehrobdan Chayon"

natija = kutubxona.qidirish(qidirilayotgan_kitob)
print(natija)