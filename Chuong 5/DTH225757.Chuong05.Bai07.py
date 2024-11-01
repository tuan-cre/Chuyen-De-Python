# def ToiUuChuoi(s):
#     s2=s
#     s2=s2.strip()
#     arr=s2.split(' ')
#     s2=""
#     for x in arr:
#         word=x
#         if len(word.strip())!=0:
#             s2=s2+word+" "
#     return s2.strip()
# s="    TRần    duY            thAnH  "
# print(s,"=>",len(s))
# s=ToiUuChuoi(s).title()
# print(s,"=>",len(s))

# Câu 7: Tối ưu chuỗi danh từ
# Yêu cầu:
# Viết chương trình tối ưu Chuỗi danh từ
# Một Chuỗi được gọi là tối ưu khi: Không chứa các khoảng trắng dư thừa, các từ cách
# nhau bởi một khoảng trắng, Ký tự đầu tiên của các từ Viết Hoa
# Ví dụ:
# Input “ TRần duY thAnH ”
# Output “Trần Duy Thanh”

s="    TRần    duY            thAnH  "
a = " ".join(s.split()).title()
print(a)
