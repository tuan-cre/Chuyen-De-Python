#phuong trinh bac 2
#ax^2+bx+c=0
from math import sqrt
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
c=float(input("Nhập c: "))
delta = b**2-4*a*c
if a==0:
    if b==0:
        if c==0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có nghiệm x=", -c/b)
else:
    if delta<0:
        print("Phương trình vô nghiệm")
    elif delta==0:
        print("Phương trình có nghiệm kép x1=x2=", -b/(2*a))
    else:
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1=", (-b+sqrt(delta))/(2*a))
        print("x2=", (-b-sqrt(delta))/(2*a))
