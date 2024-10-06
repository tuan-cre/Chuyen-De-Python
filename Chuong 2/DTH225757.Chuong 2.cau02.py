t=int(input("Nhập số giây:"))
hour=(t//3600)%24
minute=(t%3600)//60
second=(t%3600)%60
time = "AM" if hour < 12 else "PM"
hour = hour if hour < 13 else hour - 12
print("Thời gian là:",hour,":",minute,":",second,time)
