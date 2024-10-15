def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def xu_ly_mang(mang):
    so_le = [num for num in mang if num % 2 != 0]
    so_chan = [num for num in mang if num % 2 == 0]
    so_nguyen_to = [num for num in mang if la_so_nguyen_to(num)]
    so_khong_phai_nguyen_to = [num for num in mang if not la_so_nguyen_to(num)]

    print("Số lẻ:", so_le, "số lẻ:", len(so_le), "số")
    print("Số chẵn:", so_chan, "số chẵn:", len(so_chan), "số")
    print("Số nguyên tố:", so_nguyen_to)
    print("Số không phải nguyên tố:", so_khong_phai_nguyen_to)

mang = list(map(int, input("Nhập mảng các số cách nhau bởi dấu cách: ").split()))
xu_ly_mang(mang)
