def func(i, j ,k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print("i =", i, "j =", j, "k =", k)
print("(a) i = 3, j = 5, and k = 7")
func(3, 5, 7)
print("(b) i = 3, j = 7, and k = 5")
func(3, 7, 5)
print("(c) i = 5, j = 3, and k = 7")
func(5, 3, 7)
print("(d) i = 5, j = 7, and k = 3")
func(5, 7, 3)
print("(e) i = 7, j = 3, and k = 5")
func(7, 3, 5)
print("(f) i = 7, j = 5, and k = 3")
func(7, 5, 3)