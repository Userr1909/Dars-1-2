# 6-masala. O'quv Markazi
# Kurs classi yarating. Atributlari: nomi, davomiylik, talabalar=[].

# talaba_qoshish(ism) - talaba qo'shadi.

# talabalar_soni() - nechta talaba borligini qaytaradi.
# Kurs obyektini yarating, 3 ta talaba qo'shing va umumiy sonini chiqaring.
import os
os.system("cls")

class Kurs:
    def __init__(self, nomi, davomiylik):
        self.nomi = nomi
        self.davomiylik = davomiylik
        self.talabalar = []

    def talaba_qoshish(self, ism):
        self.talabalar.append(ism)
        print(f"{ism} muvaffaqiyatli kursga qo'shildi.")

    def talabalar_soni(self):
        return len(self.talabalar)

kurs1 = Kurs("Python Backend", "5 oy")
kurs1.talaba_qoshish("qosim")
kurs1.talaba_qoshish("abdusattor")
kurs1.talaba_qoshish("holmurod")

print(f"\nKursdagi talabalarning umumiy soni: {kurs1.talabalar_soni()} ta")