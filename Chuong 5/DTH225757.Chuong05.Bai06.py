
# s = str(input("Nhập 1 chuỗi:"))

# def NegativeNumberInStrings(s):
#     negativeNumber = []
#     for i in range(len(s)):
#         if s[i] == "-":
#             number = ""
#             for j in range(i+1, len(s)):
#                 if s[j].isdigit():
#                     number += s[j]
#                 else:
#                     break
#             if number != "":
#                 negativeNumber.append(int(number)*-1)
#     return negativeNumber

# for i in NegativeNumberInStrings(s):
#     print(i, end = " ")

# s = "abc-12asdas-24asdas---32asda15"
# a = s.split("-")
# b = []
# for i in range(1, len(a)):
#     c = []
#     for j in range(len(a[i])):
#         if a[i][j].isdigit():
#             c.append(a[i][j])
#         else:
#             break
#     if c:
#         b.append(-1 * int("".join(c)))
# print(b)

s = "abc-12asdas-24asdas---32asda15"
a = s.split("-")
b = []
for i in a[1:]:
    c = []
    for char in i:
        if char.isdigit():
            c.append(char)
        else:
            break
    if c:
        b.append(-1 * int("".join(c)))
print(b)
