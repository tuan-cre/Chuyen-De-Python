#Câu 13: Hàm kiểm tra số hoàn thiện, số thịnh vượng

def is_perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

def is_abundant_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum > n

n = int(input("Nhap n: "))
if is_perfect_number(n):
    print(n, "la so hoan thien")
elif is_abundant_number(n):
    print(n, "la so thinh vuong")
else:
    print(n, "la so binh thuong")