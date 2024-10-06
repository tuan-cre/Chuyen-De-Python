from time import sleep

n = int(input("Nhap n: "))

def print_star_pattern_1(n):
    top = n//2
    for i in range(n//2):
        for j in range(n):
            if j >= n//2 and j <= top:
                print('*', end='')
            elif j == n-1:
                print(' ')
            else:
                print(' ', end='')
        top += 1
    if n%2 == 0 :print()
    for i in range(n): 
        print ('*', end='')
    print()
    bottom = n//2
    for i in range(n//2):
        for j in range(n):
            if j <= n//2 and j < bottom:
                print('*', end='')
            elif j == n-1:
                print(' ')
            else:
                print(' ', end='')
        bottom -= 1
print_star_pattern_1(n)
sleep(5)
print()

def print_star_pattern_2(n):
    top = n//2
    for i in range(n//2):
        for j in range(n):
            if j == n//2 or j == top:
                print('*', end='')
            elif j == n-1:
                print(' ')
            else:
                print(' ', end='')
        top += 1
    if n%2 == 0 :print()
    for i in range(n): 
        print ('*', end='')
    print()
    bottom = (n//2)-2
    for i in range(n//2):
        for j in range(n):
            if j == 0: #and j < bottom:
                print('*', end='')
            if j == bottom: #and j < bottom:
                print('*', end='')
            elif j == n-1:
                print(' ')
            else:
                print(' ', end='')
        bottom -= 1
print_star_pattern_2(n)
sleep(5)
print()

def print_star_pattern_3(n):
    top = n
    for i in range((n//2)):
        for j in range(n):
            if j >= n//2 and j < top:
                print('*', end='')
            else:
                print(' ', end='')
        print(' ')
        top -= 1
    bot = (n//2)-1
    for i in range(n//2):
        for j in range(n):
            if j <= n//2 and j >= bot:
                print('*', end='')
            else:
                print(' ', end='')
        print(' ')
        bot -= 1
        
print_star_pattern_3(n)
sleep(5)
print()

def print_star_pattern_3(n):
    top = n-1
    for i in range((n//2)):
        for j in range(n):
            if i == 0 and j >= n//2:
                print('*', end='')
            elif j == n//2 or j == top:
                print('*', end='')
            else:
                print(' ', end='')
        print(' ')
        top -= 1
    bot = (n//2)-1
    for i in range(n//2):
        for j in range(n):
            if i == n//2-1 and j <= n//2:
                print('*', end='')
            elif j == n//2 or j == bot:
                print('*', end='')
            else:
                print(' ', end='')
        print(' ')
        bot -= 1
        
print_star_pattern_3(n)
