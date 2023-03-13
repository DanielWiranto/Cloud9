#trapesium
    
import math

a = float(input ("Masukkan sisi sejajar a: "))
b = float(input ("Masukkan sisi sejajar b: "))
c = float(input ("Masukkan sisi miring c: "))
d = float(input ("Masukkan sisi miring d: "))
tinggi = float(input ("Masukkan tinggi : "))

keliling = a + b + c + d

luas = 0.5 * (a + b) * tinggi

print("keliling dari trapesium adalah : %.2f" % keliling)
print("luas dari trapesium adalah : %.2f" % luas)
