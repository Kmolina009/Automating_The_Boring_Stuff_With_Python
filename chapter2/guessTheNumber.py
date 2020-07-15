import random 

# From Automating the Boring Stuff with Python

secretNumber = random.randint(1,20)
print('I\'m thinking of a number between 1 and 20.')

for guessesTaken in range(1,7):
    print('take a guess')
    guess = int(input())
    
    if guess < secretNumber:
        print('Your guess is too low!')
    elif guess > secretNumber:
        print('Your guess is too high!')
    else:
        break
    
if guess == secretNumber:
    print('Good job! You guessed my number in %s amount of times' % (str(guessesTaken)))
else:
    print('Nope. The number I was thinking of was %s' % str(secretNumber))
# print("Hello")