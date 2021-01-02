print('I am thinking of a number between 1 and 20')
import random
number = random.randint(1 , 20)
for guesses in range(1,6):
    print('Take a guess')
    guessnumber = int(input('please enter the number:'))
    if number < guessnumber:
        print('Your guess is too high')
    elif number > guessnumber:
        print('Your guess is too low')
    elif number == guessnumber:
        print('Good job! You guessed the number in ' + str(guesses) + ' time')
        break 
else:
    print('You failed to guess the number')
        
        
        
   

    

    

