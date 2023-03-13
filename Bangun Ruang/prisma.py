# prisma

import math

a = float(input("Masukkan alas: "))
la = float(input("Masukkan luas alas: "))
ka = float(input("Masukkan keliling alas: "))
t = float(input("Masukkan tinggi: "))

volume = la * t

luas = (2 * la) + (ka * t)

print("volume prisma adalah: %.2f" %  volume)
print("Luas prisma adalah: %.2f" % luas)