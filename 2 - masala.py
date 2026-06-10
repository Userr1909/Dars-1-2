# 2-masala. Kitob Classi
# Kitob classi bo'lsin. Atributlari: nomi, muallif, sahifa_soni.

# qisqacha() metodi kitob haqida qisqa malumot qaytarsin.

# katta_kitobmi() metodi sahifa soni 300 dan ko'p bo'lsa True, bo'lmasa False qaytarsin.
import os
os.system("cls")

class Kitob:
    def __init__(self, nomi, muallif, sahifa_soni):
        self.nomi = nomi
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni

    def qisqacha(self):
        return f"Kitob: '{self.nomi}', Muallif: {self.muallif}, {self.sahifa_soni} bet."

    def katta_kitobmi(self):
        if self.sahifa_soni > 300:
            return True
        else:
            return False
        
kitob1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 380)

while True:
    print(f"\n{kitob1.nomi} Kitob Tizimi")
    print("1 = Kitob haqida qisqa ma'lumot")
    print("2 = Katta kitobmi? (Tekshirish)")
    print("3 = Chiqish")
    
    javob = int(input("Amalni tanlang: "))
    
    if javob == 1:
        print(kitob1.qisqacha())
        
    elif javob == 2:
        if kitob1.katta_kitobmi():
            print("Ha, bu 300 dan ko'p sahifali kata kitob!")
        else:
            print("Yo'q, bu kichik yoki o'rtacha kitob.")
            
    elif javob == 3:
        print("Dastur tugadi. Rahmat!")
        break
    else:
        print("Talab xato! Qaytadan urinib ko'ring.")
# tayyor