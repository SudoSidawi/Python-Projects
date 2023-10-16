import random
import pandas as pd

def input_validation(target):
    if target == '':
        print("You did not enter a response")
        return False
    elif not target.isdigit():
        print('You need to enter a whole number')
        return False
    return True

answer = random.randint(1, 10)
print("The correct answer is:", answer)

guess = 0
guess_history = []
attempt_number = 0

while guess != answer:
    guess = input("Guess a number between 1 and 10: ")
    if input_validation(guess):
        valid_guess = int(guess)
        guess_history.append(valid_guess)
        attempt_number += 1
        if valid_guess < answer:
            print("You are too low.")
        elif valid_guess > answer:
            print('You are too high')
        else:
            guess = valid_guess
            print('You have won!')

print('Game Over! You took', len(guess_history), 'guesses.')
print(f'Your history of guesses were {guess_history}')
print(attempt_number)


#Second part of the game that takes your input history and multiplies it by a multiplier of your choice
multiplier = input('Provide a variable that will multiply your guess history: ')

# Check if the multiplier is a valid number
if multiplier.isdigit():
    #ensures it is an integer
    multiplier = int(multiplier)
    #converts the list to a pandas list
    series = pd.Series(guess_history)
    #mulitplies the list by the multiplier
    result = series * multiplier
    print(f'Multiplied guess history: {result}')
else:
    print("Invalid multiplier. Please enter a valid number.")
