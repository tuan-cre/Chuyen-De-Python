import math
pi = math.pi
try:
    r = float(input("Nhap ban kinh hinh tron: "))
    c = 2 * r * pi
    s = r * r * pi
    print("Chu vi hinh tron la:", c)
    print("Dien tich hinh tron la:", s)
except:
    print("Nhap sai ban kinh!")