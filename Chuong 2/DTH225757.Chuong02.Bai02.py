# t=int(input("Nhập số giây:"))
# hour=(t//3600)%24
# minute=(t%3600)//60
# second=(t%3600)%60
# time = "AM" if hour < 12 else "PM"
# hour = hour if hour < 13 else hour - 12
# print("Thời gian là:",hour,":",minute,":",second,time)

# Câu 2: Tính giờ phút giây
# Yêu cầu:
# Nhập vào số giây bất kỳ t. Tính và xuất ra dạng
# Giờ:Phút:Giây
# Ví dụ: Nhập 3750 thì xuất ra 1:2:30 AM
# Nhập 51100 thì xuất ra 2:11:40 PM

t = int(input("Nhap so giay: "))
hour=(t//3600)%24
minute=(t%3600)//60
second=(t%3600)%60

print(f"{hour}:{minute}:{second}")