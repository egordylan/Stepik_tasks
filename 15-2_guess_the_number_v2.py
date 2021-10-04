"""
Guess the number
The program generates a random number in the range from lower to upper limit
and asks a user to guess this number.
If the user's guess is more than a random number then the program
should display the message 'Too many, please try again'.
If the guess is less than a random number, then the program should display
'Too little, try again'.
If the user guesses the number, then the program should congratulate him
and display the message 'You guessed right, congratulations!'.
"""

#  ??? как сделать счетчик попыток, чтобы учитывать и неправильное введение цифр ???

import random


print('The program generates a random number in the range from lower to upper limit.')

def is_valid_num(num):
    if num.isdigit():
        return num
    else:
        print('It is not a number. Please input number again.')
        return is_valid_num(input('Please, guess the number: ', ))


def game():
    counter = 0
    print('This game count your attempts only if you input numeric numbers.')
    lower = input('Lower limit: ', )
    try:
        lower = int(lower)
    except:
        print('It is not a number. Please input number again.')
        lower = input('Lower limit: ', )

    upper = input('Upper limit: ', )
    try:
        upper = int(upper)
    except:
        print('It is not a number. Please input number again.')
        upper = input('Upper limit: ', )

    if lower > upper:
        lower, upper = upper, lower

    num = is_valid_num(input('Please, guess the number: '))
    try:
        lower <= int(num) <= upper
    except:
        print(f'This number is not in "{lower} - {upper}" limits. Please input number again.')
        num = is_valid_num(input('Please, guess the number: '))

    random_num = random.randint(int(lower), int(upper))

    while True:
        if int(num) > random_num:
            print('Too many, please try again.')
            counter += 1
            num = is_valid_num(input('Please, guess the number: ', ))

        elif int(num) < random_num:
            print('Too little, try again.')
            counter += 1
            num = is_valid_num(input('Please, guess the number: ',))
        else:
            counter += 1
            print('You guessed right, congratulations!')
            break

    return print(f'The number: {num}. You guessed the number with {counter} tries.')


def play_again(answer):
    if answer.lower() == 'y':
        return game(), True
    else:
        print('Thank you for the game. Good bye.')
        return False


answer = True

game()

while answer:
    print('Do you want to play again? (yes = y/ no = n)')
    answer = play_again(input())
