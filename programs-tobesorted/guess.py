#this is a guess the number game
import random

guessestaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1,20)
print ('Well, '+myName + ', I am thinking about a number between 1 and 20')

while guessestaken < 6:
    print('Take a guess.') # there are 4 spaces in front of print
    guess = input()
    guess = int(guess)

    guessestaken = guessestaken + 1

    if guess<number:
        print('your guess is too low') # There are eight spaces in front of print
    if guess > number:
        print('your guess is too high')
    if guess == number:
        break

if guess == number:
        guessestaken = str(guessestaken)
        print('good job, ' + myName + '! You guessed my number in ' + guessestaken + ' guesses!')


if guess != number:
        number = str(number)
        print ('Nope. the number i was thinking of was ' + number)
        
