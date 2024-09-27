import random

while True:
    n = random.randint(1, 100)
    numofguest = 0
    win = False
    while numofguest < 7:
        numofguest += 1
        guess = int(input('Enter your guess: '))
        if guess < n:
            print('Your guess is too low')
        elif guess > n:
            print('Your guess is too high')
        else:
            print('You win')
            win = True
            break
    if not win:
            print('You lose. The number is: ', n)
    cont = input('Do you want to continue? (y/n): ')
    if cont != 'y':
        break
print('Goodbye')

