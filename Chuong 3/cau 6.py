so = int(input("Nhập số co 2 chu so: "))
chuc = so // 10
donvi = so % 10

chu_chuc = ["mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
chu_donvi = ["một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

if chuc == 0:
    print(chu_donvi[donvi - 1])
else:
    print(chu_chuc[chuc - 1], chu_donvi[donvi - 1])
