import math

a = 0
x = 0

while a <= 0 or a == 1 or x <= 0:
    a = float(input("Nhap a: "))
    x = float(input("Nhap x: "))    

log = math.log(x) / math.log(a)
print("Ket qua logax: ", log)


