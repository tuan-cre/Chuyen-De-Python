def lay_day_so_tang_dan():
    while True:
        try:
            day_so = list(map(int, input("Nhập một dãy số theo thứ tự tăng dần, cách nhau bằng dấu cách: ").split()))
            if all(day_so[i] < day_so[i + 1] for i in range(len(day_so) - 1)):
                return day_so
            else:
                print("Dãy số không theo thứ tự tăng dần. Vui lòng thử lại.")
        except ValueError:
            print("Dữ liệu nhập không hợp lệ. Vui lòng chỉ nhập số.")

day_so_da_nhap = lay_day_so_tang_dan()
print("Dãy số đã nhập là:", day_so_da_nhap)