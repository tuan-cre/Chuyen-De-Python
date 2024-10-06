def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def is_perfect_number(n):
    return sum_of_divisors(n) == n

def is_abundant_number(n):
    return sum_of_divisors(n) > n

n = int(input("Nhap n: "))
if is_perfect_number(n):
    print(n, "la so hoan thien")
elif is_abundant_number(n):
    print(n, "la so thinh vuong")
else:
    print(n, "la so binh thuong")