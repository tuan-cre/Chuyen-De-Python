
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

def ngayhomsau():
    if thang == 12 and ngay == 31:
        print("Ngày hôm sau là ngày 1 tháng 1 năm", nam + 1)
    elif ngay == 31 and thang in [1, 3, 5, 7, 8, 10]:
        print("Ngày hôm sau là ngày 1 tháng", thang + 1, "năm", nam)
    elif ngay == 30 and thang in [4, 6, 9, 11]:
        print("Ngày hôm sau là ngày 1 tháng", thang + 1, "năm", nam)
    elif ngay == 29 and thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            print("Ngày hôm sau là ngày 1 tháng 3 năm", nam)
    elif ngay == 28 and thang == 2:
        print("Ngày hôm sau là ngày 1 tháng 3 năm", nam)
    else:
        print("Ngày hôm sau là ngày", ngay + 1, "tháng", thang, "năm", nam) 

def kiemtrahople():
    if thang in [1, 3, 5, 7, 8, 10, 12] and ngay > 31:
        print("Ngày không hợp lệ")
    elif thang in [4, 6, 9, 11] and ngay > 30:
        print("Ngày không hợp lệ")
    elif thang == 2 and ((nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)) and ngay > 29:
        print("Ngày không hợp lệ")
    elif thang == 2 and ((nam % 4 != 0 and nam % 100 == 0) or (nam % 400 != 0)) and ngay > 28:
        print("Ngày không hợp lệ")
    else:
        ngayhomsau()

kiemtrahople()