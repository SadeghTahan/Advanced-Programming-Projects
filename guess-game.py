import stdio, random
range = 1000000
secret = random.randrange(1, range + 1)
print('guess a number between 1 and %d' %range)
guess = 0
while guess != secret:
    print('what is your guess?' , end=' ')
    guess = stdio.readInt()
    if guess < secret: print('too low')
    elif guess > secret: print('too high')
    else: print('you win!')               