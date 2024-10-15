# Nhập vào dãy số thực
n = int(input("Nhập số lượng phần tử của dãy: "))
M = []
for i in range(n):
    num = float(input(f"Nhập phần tử thứ {i+1}: "))
    M.append(num)

# Sắp xếp dãy số theo thứ tự giảm dần
M.sort(reverse=True)

# Xuất ra dãy số sau khi sắp xếp
print("Dãy số sau khi sắp xếp giảm dần:")
print(M)