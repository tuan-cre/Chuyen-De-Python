import math

def nested_sqrt(n):
    result = 0
    for i in range(n):
        result = math.sqrt(2 + result)
    return result

n = int(input("Nhap n: "))
print(nested_sqrt(n))