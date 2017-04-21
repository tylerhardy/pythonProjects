# This is a guess the number game
import random
secret_number = random.randint(1,20)
print('I am thinking of a number between 1 and 20')

def Check_number():
    try:
        print('take a guess.')
        guess = int(input())
        return guess
    except ValueError:
        print('That is not a valid number, please enter an integer')

# Allow the player six guesses
for guesses_taken in range(1,7):
    guess = Check_number()
    if guess == None:
        continue
    elif guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        break
if guess == secret_number:
    print('Good job! You guessed my number in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secret_number))

