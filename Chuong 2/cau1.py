import math
try:
    r=float(input("Mời bạn nhập bán kính hình tròn:"))
    cv=2*math.pi*r
    dt=math.pi*r**2
    print("Chu vi =",cv)
    print("Diện tích=",dt)
except:
    print("Lỗi rồi!")
