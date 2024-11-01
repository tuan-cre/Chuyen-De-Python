# #Xuat bang cuu chuong
# for i in range(1, 11):
#     for j in range(2, 10):
#         line = '{0} *{1:>2} = {2:>2}'.format(j, i, i*j)
#         print(line, end="\t")
#     print()

for i in range (1, 11):
    for j in range (2, 10):
        print(f"{j} * {i} = {j*i}", end="\t")
    print()