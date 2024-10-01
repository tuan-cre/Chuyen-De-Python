#n = int(input("Nhap n:"))
n = 7
center = n//2
for i in range(n):
    for j in range(n):
        if i <= center:
            if(j > center-1):
                print("*", end=" ")
    print()
    

