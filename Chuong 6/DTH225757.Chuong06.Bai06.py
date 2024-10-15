import random

n = int(input("Nhập số lượng phần tử: "))
result = random.sample(range(0, 10000), n)
print("Danh sách được tạo:", result)