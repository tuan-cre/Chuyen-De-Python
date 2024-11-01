# a = int(input("Nhập số a: "))
# b = int(input("Nhập số b: "))
# phep_tinh = input("Nhập phép toán (+, -, *, /): ")
# match phep_tinh:
#     case "+":
#         print(a, "+", b, "=", a+b)
#     case "-":
#         print(a, "-", b, "=", a-b)
#     case "*":
#         print(a, "*", b, "=", a*b)
#     case "/":
#         if b==0:
#             print("Không thể chia cho 0")
#         else:
#             print(a, "/", b, "=", a/b)
#     case _:
#         print("Phép toán không hợp lệ")

# Câu 8: Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo
# đúng phép toán đã nhập.

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
op = input("Nhap phep tinh (+, -, *, /): ")
cal = str(a)+op+str(b)

print(f"{a} {op} {b} = {eval(cal)}")

