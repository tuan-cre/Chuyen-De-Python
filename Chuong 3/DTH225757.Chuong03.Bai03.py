# from math import sqrt
# a=float(input("Nhập a: "))
# b=float(input("Nhập b: "))
# c=float(input("Nhập c: "))
# delta = b**2-4*a*c
# if a==0:
#     if b==0:
#         if c==0:
#             print("Phương trình vô số nghiệm")
#         else:
#             print("Phương trình vô nghiệm")
#     else:
#         print("Phương trình có nghiệm x=", -c/b)
# else:
#     if delta<0:
#         print("Phương trình vô nghiệm")
#     elif delta==0:
#         print("Phương trình có nghiệm kép x1=x2=", -b/(2*a))
#     else:
#         print("Phương trình có 2 nghiệm phân biệt:")
#         print("x1=", (-b+sqrt(delta))/(2*a))
#         print("x2=", (-b-sqrt(delta))/(2*a))

# Câu 3: Phương trình bậc 2
# Yêu cầu:
# Viết chương trình giải phương trình bậc 2: ax2+bx+c=0

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

delta = b * b - 4 * a * c

if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        print(f"Phuong trinh co nghiem x = {-c/b}")
else:
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        print(f"Phuong trinh co nghiem kep x = {-b /(2 * a)}")
    else:
        print(f"Phuong trinh co 2 nghiem phan biet x1 = {(-b + delta ** 0.5)/(2 * a)} va x2 = {(-b - delta ** 0.5)/(2 * a)}")