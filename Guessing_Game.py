#Dyson Smith
#Sept. 29-2020
#Guess my number 1.0

import random

#intro
print('\tWelcome to "Guess My Number"!')

question = input('what difficalty would you like Easy, Medium, Hard')
#easy dificalty
if ('Ea' in question) or ('ea' in question) or (question == 'easy') or \
   (question == 'Easy') or (question == 'EASY') or \
   ('y' in question) or ('Y' in question) :
    diff = 1
    max_range = 10
    trys = 3
#medium dificalty
elif ('M' in question) or ('m' in question):
    diff = 2
    max_range = 50
    trys = 5
#hard difficalty
else:
    diff = 3
    max_range = 100
    trys = 10

the_number = random.randint(1,max_range)
print(the_number)#for debugging remove later

print('\nI am thinking of a number between 1 and '+str(max_range)+'.')
print('Try to guess it in '+str(trys)+' attemps.\n')

#win condition
winner = False

#guess 1
guess = int(input('pick a number between 1 and '+str(max_range)+'.'))

if guess == the_number:
    winner = True
elif guess < the_number:
    print('guess higher')
else:
    print('guess lower')

#guess 2
if winner == False:
    guess = int(input('pick a number between 1 and '+str(max_range)+'.'))
    if guess == the_number:
        winner = True
    elif guess < the_number:
        print('guess higher')
    else:
        print('guess lower')

#guess 3
if winner == False:
    if diff > 1:
        guess = int(input('pick a number between 1 and '+str(max_range)+'.'))
        if guess == the_number:
            winner = True
        elif guess < the_number:
            print('guess higher')
        else:
            print('guess lower')

#guess 4
if winner == False:
    if diff > 1:
        guess = int(input('pick a number between 1 and '+str(max_range)+'.'))
        if guess == the_number:
            winner = True
        elif guess < the_number:
            print('guess higher')
        else:
            print('guess lower')

#guess 5
if winner == False:
    if diff > 2:
        guess = int(input('pick a number between 1 and '+str(max_range)+'.'))
        if guess == the_number:
            winner = True
        elif guess < the_number:
            print('guess higher')
        else:
            print('guess lower')

#guess 6
if winner == False:
    if diff > 2:
        guess = int(input('pick a number between 1 and '+str(max_range)+'.'))
        if guess == the_number:
            winner = True
        elif guess < the_number:
            print('guess higher')
        else:
            print('guess lower')

#guess 7
if winner == False:
    if diff > 2:
        guess = int(input('pick a number between 1 and '+str(max_range)+'.'))
        if guess == the_number:
            winner = True
        elif guess < the_number:
            print('guess higher')
        else:
            print('guess lower')

#guess 8
if winner == False:
    if diff > 2:
        guess = int(input('pick a number between 1 and '+str(max_range)+'.'))
        if guess == the_number:
            winner = True
        elif guess < the_number:
            print('guess higher')
        else:
            print('guess lower')

#guess 9
if winner == False:
    if diff > 2:
        guess = int(input('pick a number between 1 and '+str(max_range)+'.'))
        if guess == the_number:
            winner = True
        elif guess < the_number:
            print('guess higher')
        else:
            print('guess lower')

#guess final
if winner == False:
    guess = int(input('pick a number between 1 and '+str(max_range)+'.'))
    if guess == the_number:
        winner = True
    elif guess < the_number:
        pass
    else:
        pass

#end condition
if winner == True:
    print('you are the winner')
else:
    print('you are a looser the number was',the_number)
print('game end')
