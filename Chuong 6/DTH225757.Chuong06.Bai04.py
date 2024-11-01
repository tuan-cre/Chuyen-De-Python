# lst = [3, 0, 1, 5, 2]
# x = 2

# print("(a) lst[0]:", lst[0])
# print("(b) lst[3]:", lst[3])
# print("(c) lst[x]:", lst[x])
# print("(d) lst[-x]:", lst[-x])
# print("(e) lst[x + 1]:", lst[x + 1])
# print("(f) lst[x] + 1:", lst[x] + 1)
# print("(g) lst[lst[x]]:", lst[lst[x]])
# print("(h) lst[lst[lst[x]]]:", lst[lst[lst[x]]])

n=5
lst = [0]*n
for i in range (len(lst)):
    lst.append(int(input(f"Nhap n{i}:")))
le = [x for x in lst if(x%2==1)]
chan = [x for x in lst if(x%2==0)]

print(le)
print(chan)