#kiem tra so nguyen to
# n = int(input("Nhập số nguyên dương n: "))
# if n < 2:
#     print(n, "không phải số nguyên tố")
# else:
#     check = True
#     for i in range(2, n):
#         if n % i == 0:
#             check = False
#             break
#     if check:
#         print(n, "là số nguyên tố")
#     else:
#         print(n, "không phải số nguyên tố")
#ket thuc chuong trinh

# n = int(input("Nhap so nguyen duong N:"))
# check = True
# if n < 2:
#     check = False
# elif n == 2:
#     check = True
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             check = False
#             break
# if check:
#     print(n, "la so nguyen to")
# else:
#     print(n, "khong phai so nguyen to")


# Câu 11: Kiểm tra số nguyên tố
# Yêu cầu:
# Viết chương trình nhập vào một số, kiểm tra xem số này có phải là số nguyên tố
# hay không. Hỏi người dùng có tiếp tục sử dụng hay thoát phần mềm.

n = int(input("Nhap n: "))
check = "la"

if n == 2:
    check = "la"
elif n<2:
    check = "khong la"
else:
    for i in range(1, n):
        if(n % 2 == 0):
            check = "khong la"
print(n, check, "so nguyen to")