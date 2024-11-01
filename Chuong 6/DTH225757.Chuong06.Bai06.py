import random

n = int(input("Nhập số lượng phần tử: "))
result = random.sample(range(0, 1000), n)
result.sort()
print("Danh sách được tạo:", result)