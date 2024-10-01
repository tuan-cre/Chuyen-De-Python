
def oscillate(a, b):
    x = []
    for i in range(a, b):
        x.append(i)
        x.append(i*-1)
    return x

for n in oscillate(-3, 5):
    print(n, end=' ')
print()


    