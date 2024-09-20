#kiem tra so nguyen to
n = int(input("Nhập số nguyên dương n: "))
if n < 2:
    print(n, "không phải số nguyên tố")
else:
    check = True
    for i in range(2, n):
        if n % i == 0:
            check = False
            break
    if check:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải số nguyên tố")
#ket thuc chuong trinh