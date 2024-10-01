n = int(input("Nhap n:"))

center = n//2
for i in range(n):
    for j in range(n):
        if i <= center:
            if(j==0 or i==j or i==center):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            if(i==j or j==(n-1)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()