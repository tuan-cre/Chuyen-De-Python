#ve hinh vuong rong bang dau * voi chieu dai n
n = int(input("Nhập chiều dài cạnh hình vuông: "))
for i in range(n):
    if i == 0 or i == n-1:
        print("* " * n)
    else:
        print("* " + "  " * (n-2) + "*")
#ve tam giac vuong bang dau * voi chieu dai 2 canh goc vuong la m
m = int(input("Nhập chiều dài 2 cạnh góc vuông của tam giác vuông: "))
for i in range(1, m+1):
    print("* " * i)
