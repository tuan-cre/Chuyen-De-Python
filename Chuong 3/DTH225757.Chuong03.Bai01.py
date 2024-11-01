# nam = int(input("Nhập năm: "))
# if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
#     print("Năm", nam, "là năm nhuận")
# else:
#     print("Năm", nam, "không phải năm nhuận")

# Câu 1: Kiểm tra năm nhuần
# Yêu cầu:
# Nhập vào một năm bất kỳ, kiểm tra năm đó có phải năm nhuần hay không. Biết
# rằng: Năm nhuần là năm chia hết cho 4 nhưng không chia hết cho 100 hoặc chia
# hết cho 400

year = int(input("Nhap nam: "))
result = "nhuan" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "khong nhuan"
print(f"{year} la nam {result}")