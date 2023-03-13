# tabung

import math

r = float(input("Masukkan jari - jari: "))
t= float(input("Masukkan tinggi: "))

volume = math.pi * r ** 2 * t

luas = 2 * math.pi * r * (t * r)

print("volume tabung adalah: %.2f" %  volume)
print("Luas tabung adalah: %.2f" % luas)