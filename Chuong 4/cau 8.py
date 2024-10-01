#Cau 8 Viết chương trình tính log(a^x) với a, x là các số thực nhập vào từ bàn phím, và x>0, a>0, a != 1.( dùng loga^x=lnx/lna)
import math

a = 0
x = 0

while a <= 0 or a == 1 or x <= 0:
    a = float(input("Nhap a: "))
    x = float(input("Nhap x: "))    

log = math.log(x) / math.log(a)
print("Logarit cua", a, "^", x, "la:", log)

