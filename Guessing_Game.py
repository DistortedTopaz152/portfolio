#Dyson Smith
#Sept. 29-2020
#Guess my number 1.0
import random

the_number = random.randint(1,10)

print('\tWelcome to "Guess My Number"!')
print('\nI am thinking of a number between 1 and 10')
print('Try to guess it in 3 attemps.\n')

winner = False

guess = int(input('pick a number between 1 and 10'))

if winner == False:
    if guess == the_number:
        winner = True
    elif guess < the_number:
        print('guess higher')
    else:
        print('guess lower')

if winner == False:
    guess = int(input('pick a number between 1 and 10'))
    if guess == the_number:
        winner = True
    elif guess < the_number:
        print('guess higher')
    else:
        print('guess lower')

if winner == False:
    guess = int(input('pick a number between 1 and 10'))
    if guess == the_number:
        winner = True
    elif guess < the_number:
        pass
    else:
        pass

if winner == True:
    print('you are the winner')
else:
    print('you are a looser')
print('game end')
