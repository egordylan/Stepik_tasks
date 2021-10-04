"""
Description of the project:
magic ball 8 (the ball of fate) is a jesting way to predict the future.
The program should ask the user to ask a question and give a random answer to it.
"""
import random
from time import sleep


answers = ['Undoubtedly', 'It seems to me - yes', 'It is not clear yet, try again', 'Don\'t even think',
           'A foregone conclusion', 'Most likely', 'Ask later', 'My answer is no',
           'No doubts', 'good prospects', 'Better not to tell', 'According to my data - no',
           'Definitely yes', 'The signs say yes', 'It is impossible to predict now', 'The prospects are not very good',
           'You can be sure of this', 'Yes', 'Concentrate and ask again', 'Very doubtful']

def magic_ball():
    time_to_sleep = 1
    print('Hello, World. I am the Magic ball, and I know answer to all of your questions.')
    sleep(time_to_sleep)
    name = input('What is your name? ')
    sleep(time_to_sleep)
    print('Hello,', name)

    again = 'yes'
    while again != 'no':
        question = input('Ask your question, please -- ')
        print(random.choice(answers))
        sleep(time_to_sleep)
        again = input('Do you want to continue - yes/ no? ').lower()

    print('Please come back if You will have any questions.')
    sleep(time_to_sleep)
    print('Good bye.')


magic_ball()
