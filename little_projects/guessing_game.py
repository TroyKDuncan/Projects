'''
using sys.argv, run the game and choose the first and last numbers.
the game selects a random value from the range and asks for input 
from the user and the user must keep guessing until they get it right
'''

import sys
import random as r

# Handle invalid inputs from the command line
try:
    first_num = int(sys.argv[1])
    second_num = int(sys.argv[2])
except (ValueError, IndexError) as err:
    print(err)
    print('''
How to use: 
run in the terminal: python3 guessing_game.py [first number] [second number]

This will create a guessing range from first number to second number.
This program will now exit. Try again from the command line.
''')
    exit()


secret_number = r.randint(first_num, second_num)

guess = False
while guess == False:
    # Handle invalid inputs
    try:
        user_guess = int(
            input(f'Guess a number from {first_num} to {second_num}: '))
    except ValueError as err:
        print()
        print(err)
        print('Invalid input. You must enter an integer.\n')
        continue
    if user_guess < first_num or user_guess > second_num:
        print('Your guess was out of the specified range.')
        print()
        continue
    elif user_guess == secret_number:
        print('That\'s correct!')
        guess = True
    else:
        print('Nope! Try again!')
