import math


a = float(input("Masukkan panjang sisi a: "))
b = float(input("Masukkan panjang sisi b: "))
c = float(input("Masukkan panjang sisi c: "))
tinggi = float(input("Masukkan nilai tinggi: "))

keliling = a + b + c

luas = 0.5 * a * tinggi

print("Keliling segitiga adalah: %.2f" % keliling)
print("Luas segitiga adalah: %.2f" % luas)