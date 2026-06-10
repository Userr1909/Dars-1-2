# Berilgan vazifalarni classlar e'lon qilish, ulardan obyekt olish va foydalanishni o'rganing.


# 1-masala. Do'kon Mahsuloti
# Mahsulot classi yarating. Atributlari: nom, narx, miqdor.

# sotib_ol(miqdor) metodi chaqirilganda miqdorni kamaytirsin.

# qolgan_miqdor() metodi nechta mahsulot qolganini qaytarsin.
# Bir mahsulotdan obyekt yarating, undan 2 marta sotib oling.
import os
os.system("cls")

class Mahsulot:
    def __init__(self, nom, narx, miqdor):
        self.nom = nom
        self.narx = narx
        self.miqdor = miqdor

    def sotib_ol(self, miqdor):
        if miqdor <= self.miqdor:
            self.miqdor -= miqdor
            print(f"{miqdor} ta {self.nom} muvaffaqiyatli sotib olindi!")
        else:
            print(f"omborda yetarli mahsulot yo'q, Hozirda bor: {self.miqdor} ta")

    def qolgan_miqdor(self):
        return self.miqdor


m1 = Mahsulot("Olma", 15000, 50)

while True:
    print(f"\n {m1.nom} do'kon")
    print("1 = Mahsulot sotib olish")
    print("2 = Qolgan miqdorni ko'rish")
    print("3 = Chiqish")
    
    javob = int(input("tanlang: "))
    
    if javob == 1:
        nechta = int(input("Nechta sotib olmoqchisiz: "))
        m1.sotib_ol(nechta)
    elif javob == 2:
        print(f"Omborda qolgan mahsulot miqdori: {m1.qolgan_miqdor()} ta")
    elif javob == 3:
        print("Dastur tugadi. Rahmat!")
        break
    else:
        print("Xato buyruq kiritildi!")
    # tayyor