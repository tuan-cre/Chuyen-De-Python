# Viết chương trình tính căn bậc 2 lồng nhau
import math
n = int(input("Nhap n: "))

can = math.sqrt(2)
for i in range(n):
    can = math.sqrt(can)

print("Can bac", 2**n, "cua 2 la:", can)
