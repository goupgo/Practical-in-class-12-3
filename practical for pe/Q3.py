import random

n = random.randint(1, 100)

while True:
    try:
        x = int(input('x is your guessed value: '))
        if x == n:
            break
        elif x > n:
            print('n<x')
        elif x < n:
            print("n>x")
    except ValueError:
        print('Please enter a number!')

print("EXACTLY!")