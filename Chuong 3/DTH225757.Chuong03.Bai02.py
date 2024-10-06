thang = 0
while thang < 1 or thang > 12:
    thang = int(input("Nhập tháng: "))
if thang in [1, 3, 5, 7, 8, 10, 12]:
    print("Tháng", thang, "có 31 ngày")
elif thang in [4, 6, 9, 11]:
    print("Tháng", thang, "có 30 ngày")
else:
    nam = int(input("Nhập năm: "))
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print("Tháng", thang, "có 29 ngày")
    else:
        print("Tháng", thang, "có 28 ngày") 