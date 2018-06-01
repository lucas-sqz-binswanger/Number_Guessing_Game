#This is a guess the number game.

import random

guessesTaken = 0

print('This is a number guessing game. What is your name?')
myName = input()

number = random.randint(1,50)
print('Welcome, ' + myName +', a random number has been selected between 1 and 100.')

while guessesTaken < 4:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    
    guessesTaken = guessesTaken + 1
    
    if guess < number:
        print('Your guess is too low,' + myName +', please try again.')
        
    if guess > number:
        print('No,' + myName +', you are guessing too high.')
        
    if guess == number:
        break
    
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job! You guessed the number in ' + guessesTaken + 'guesses')
    
if guess != number:
    number = str(number)
    print('Close but no cigar, I was thinking of ' + number) 
    