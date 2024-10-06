s = str(input("Nhập 1 chuỗi:"))

inhoa = 0
inthuong = 0
chuso = 0
kitudacbiet = 0
khoangtrang = 0
nguyenam = 0
phuam = 0

for i in s:
    if i.isupper():
        inhoa += 1
    elif i.islower():
        inthuong += 1
    elif i.isdigit():
        chuso += 1
    elif i.isspace():
        khoangtrang += 1
    else:
        kitudacbiet += 1
    if i in 'aeiou':
        nguyenam += 1
    else:
        phuam += 1

print("Chữ hoa:", inhoa)
print("Chữ thường:", inthuong)
print("Chữ số:", chuso)
print("Kí tự đặc biệt:", kitudacbiet)
print("Khoảng trắng:", khoangtrang)
print("Nguyên âm:", nguyenam)
print("Phụ âm:", phuam)