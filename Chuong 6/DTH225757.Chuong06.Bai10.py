# import numpy as np

# def nhap_ma_tran(ten):
#     hang = int(input(f"Nhập số hàng của ma trận {ten}: "))
#     cot = int(input(f"Nhập số cột của ma trận {ten}: "))
#     ma_tran = []
#     for i in range(hang):
#         hang_ma_tran = list(map(int, input(f"Nhập hàng {i+1} của ma trận {ten}: ").split()))
#         ma_tran.append(hang_ma_tran)
#     for i in range(cot):
#         cot_ma_tran = list(map(int, input(f"Nhập cot {i+1} của ma trận {ten}: ").split()))
#         ma_tran.append(cot_ma_tran)
#     return np.array(ma_tran)

# def cong_ma_tran(A, B):
#     return A + B

# def hoan_vi_ma_tran(A):
#     return A.T

# # Nhập ma trận A và B
# A = nhap_ma_tran("A")
# B = nhap_ma_tran("B")

# # Cộng hai ma trận
# C = cong_ma_tran(A, B)
# print("Tổng của hai ma trận A và B là:")
# print(C)

# # Tính ma trận hoán vị của A và B
# A_hoan_vi = hoan_vi_ma_tran(A)
# B_hoan_vi = hoan_vi_ma_tran(B)
# print("Ma trận hoán vị của A là:")
# print(A_hoan_vi)
# print("Ma trận hoán vị của B là:")
# print(B_hoan_vi)

def nhapmatran(ten):
    matran = {
        "hang": [],
        "cot": []
    }
    h = int(input(f"Nhập số hàng của ma trận {ten}: "))
    c = int(input(f"Nhập số cột của ma trận {ten}: "))
    for i in range(h):
        hang = int(input(f"Nhập hàng {i+1} của ma trận {ten}: "))
        matran["hang"].append(hang)
    for i in range(c):
        cot = int(input(f"Nhập cột {i+1} của ma trận {ten}: "))
        matran["cot"].append(cot)
    print(f"Ma tran {ten}: ", matran)
    return matran

# def congmatran(A, B):

A = nhapmatran("A")
B = nhapmatran("B")

# C = congmatran(A, B)

# print(C)