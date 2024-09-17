t=int(input("Nhập số giây:"))
hour=(t//3600)%24
minute=(t%3600)//60
second=(t%3600)%60
time="AM"
if hour>=0 and hour<=12:
    time="AM"
else:
    time="PM"
print(hour,":",minute,":",second,"",time)