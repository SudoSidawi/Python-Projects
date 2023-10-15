'''import random as rd

answer = rd.randint(1, 100)
print(answer)
print('You have 3 guesses to find the secret number')
guess_list = []
guess = int(input("Guess a number between 1 and 100:  "))
guess_list.append(guess)
tries = 3
guess = 0

def input_validation(guess):
    tries -= 1
    if guess == '':
        print("You did not enter a response")
    elif guess == float:
        print('You need to enter a whole number')
    else:
        return guess


while tries > 1 and guess != answer:
    #tries -= 1
    print(f'You have {tries} tries remaining.')
    guess = int(input("Guess again:  "))
    input_validation(guess)
    if guess == answer:
        print("You guessed correctly, you've won!")
    elif guess < answer:
        print("Too low")
    else:
        print("Too high")

if guess != answer:
    print("Game over! Sorry you didn't guess correctly.")
else:
    print("You guessed correctly, you've won!")
    '''

import random as rd

answer = rd.randint(1, 100)
print(answer)
print('You have 3 guesses to find the secret number')
guess_list = []
tries = 3

def input_validation(guess):
    global tries  # Declare 'tries' as a global variable
    tries -= 1
    if guess == '':
        print("You did not enter a response")
    elif not guess.isdigit():  # Check if the input is not a digit
        print('You need to enter a whole number')
    else:
        return int(guess)

while tries > 0:
    print(f'You have {tries} tries remaining.')
    guess = input("Guess a number between 1 and 100:  ")
    valid_guess = input_validation(guess)
    
    if valid_guess is not None:
        guess_list.append(valid_guess)

        if valid_guess == answer:
            print("You guessed correctly, you've won!")
            break
        elif valid_guess < answer:
            print("Too low")
        else:
            print("Too high")

if tries == 0:
    print("Game over! Sorry, you didn't guess correctly.")
