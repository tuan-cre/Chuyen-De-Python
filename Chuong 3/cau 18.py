#ve hinh vuong rong bang dau * voi chieu dai n
n = int(input("Nhập chiều dài cạnh hình vuông: "))
for i in range(n):
    if i == 0 or i == n-1:
        print("* " * n)
    else:
        print("* " + "  " * (n-2) + "*")