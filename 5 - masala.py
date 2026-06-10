# 5-masala. Uchburchak Classi
# Uchburchak classi yarating. Uch tomon: a, b, c.

# perimetr() metod - perimetrni qaytaradi.

# maydon() metod - Heron formulasidan foydalanib maydon hisoblaydi.
# Uchburchak classidan obyekt yarating va uning perimetri va maydonini hisoblang.
import os
import math

os.system("cls")

class Uchburchak:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a + self.b + self.c

    def maydon(self):
        p = (self.a + self.b + self.c) / 2
        S = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return S

shakl = Uchburchak(3, 4, 5)

while True:
    print(f"\nUchburchak Tizimi (Tomonlar: {shakl.a}, {shakl.b}, {shakl.c})")
    print("1 = Perimetrni hisoblash")
    print("2 = Maydonni (Yuza) hisoblash")
    print("3 = Chiqish")
    
    javob = int(input("tanlang: "))
    
    if javob == 1:
        print(f"Uchburchak perimetri: {shakl.perimetr()}")
    elif javob == 2:
        print(f"Uchburchak maydoni: {shakl.maydon():.2f}")
    elif javob == 3:
        print("Dastur tugadi. Rahmat!")
        break
    else:
        print("Noto'g'ri buyruq!")