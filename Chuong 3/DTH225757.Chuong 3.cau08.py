a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
phep_tinh = input("Nhập phép toán (+, -, *, /): ")
match phep_tinh:
    case "+":
        print(a, "+", b, "=", a+b)
    case "-":
        print(a, "-", b, "=", a-b)
    case "*":
        print(a, "*", b, "=", a*b)
    case "/":
        if b==0:
            print("Không thể chia cho 0")
        else:
            print(a, "/", b, "=", a/b)
    case _:
        print("Phép toán không hợp lệ")
