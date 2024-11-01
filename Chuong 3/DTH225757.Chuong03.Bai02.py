# thang = 0
# while thang < 1 or thang > 12:
#     thang = int(input("Nhập tháng: "))
# if thang in [1, 3, 5, 7, 8, 10, 12]:
#     print("Tháng", thang, "có 31 ngày")
# elif thang in [4, 6, 9, 11]:
#     print("Tháng", thang, "có 30 ngày")
# else:
#     nam = int(input("Nhập năm: "))
#     if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
#         print("Tháng", thang, "có 29 ngày")
#     else:
#         print("Tháng", thang, "có 28 ngày") 

# Câu 2: Đếm số ngày trong tháng
# Yêu cầu:
# Nhập vào 1 tháng, xuất tháng đó có bao nhiêu ngày.
# 1,3,5,7,8,10,12➔31 ngày
# 4,6,9,11➔có 30 ngày
# Nếu là tháng 2 thì yêu cầu nhập thêm năm. Năm nhuần thì tháng 2 có 29 ngày,
# không nhuần có 28 ngày


def result(day):
    print(f"Thang {month} co {day} ngay")

month = int(input("Nhap thang: "))
if month == 2:
    year = int(input("Nhap nam: "))
    result(29) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else result(28)
elif month in [4, 6, 9, 11]:
    result(30)
elif month in [1, 3, 5, 7, 8, 10, 12]:
    result(31)
else:
    print("Thang khong hop le")
    


