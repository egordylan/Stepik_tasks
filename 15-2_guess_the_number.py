"""
Guess the number

The program generates a random number in the range from 11 to 100100
and asks a user to guess this number.
If the user's guess is more than a random number then the program
should display the message 'Too many, please try again'.
If the guess is less than a random number, then the program should display
'Too little, try again'.
If the user guesses the number, then the program should congratulate him
and display the message 'You guessed right, congratulations!'.
"""

import random

print('The program generates a random number in the range from 11 to 100100.')

def is_valid(num):
    if num.isdigit():
        return num
    else:
        print('It is not a number. Please input number again.')
        return is_valid(input('Please, guess the number: ', ))

def random_number():
    #  this is a computer's number
    random_num = random.randint(11, 100)
    #  this is a user's number
    num = is_valid(input('Please, guess the number: ', ))

    while True:
        if int(num) > random_num:
            print('Too many, please try again.')
            num = is_valid(input('Please, guess the number: ',))
        elif int(num) < random_num:
            print('Too little, try again.')
            num = is_valid(input('Please, guess the number: ',))
        else:
            print('You guessed right, congratulations!')
            break

    return num

def play_again(answer):
    if answer.lower() == 'y':
        return random_number(), True
    else:
        print('Thank you for the game. Good bye.')
        return False

answer = True

random_number()

while answer:
    print('Do you want to play again? (yes = y/ no = n)')
    answer = play_again(input())


