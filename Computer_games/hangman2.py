#! /usr/bin/env python3
#Credit Laura @codeboom source http://codeboom.wordpress.com/sweet-resources/hangman/

# Simple word game where users guess the letters
import string
import random

# Function to decide if a letter is in a word
def inWord(letter,word):
    letterFound = False
    for char in word:
        if char == letter:
            letterFound = True

    return letterFound

# Function to count how many times a letter appears in a word
def timesInWord(letter,word):
    letterTimes = 0
    for char in word:
        if char == letter:
            letterTimes = letterTimes + 1

    return letterTimes

# Function to print the word or a blank
def printWord(word, guesses):
    for char in word:
        letterFound = False
        for guess in guesses:
            if char == guess:
                letterFound = True

        if letterFound == True:
            print char," ",
        else:
            print "_ ",

# Function to get and validate a letter
def getLetter():
    letter = raw_input("Enter your guess: ")
    letterOkay = False
    while letterOkay == False:
        if letter.isalpha() == False:
            print "You must enter a letter"
        elif len(letter) > 1:
            print "Only enter 1 letter"
        else:
            letterOkay = True

    return letter

# Function to check if all of the letters have been guessed
def checkWin(word, guesses):
    numberGuessed = 0
    for guess in guesses:
        numberGuessed += timesInWord(guess,word)

    # If the number of correct guesses is equal to the length
    if numberGuessed == len(word):
        return True
    else:
        return False

def printMan( badGuesses ):
    man = ['________',
           '|       |',
           '|       O',
           '|       |',
           '|      /|\ ',
           '|       |',
           '|      / \ ']

    counter = 0
    while counter < badGuesses:
        print man[counter]
        counter +=1

# -------------------------------------------

# Get a random word from a list
answer = random.choice(['hello', 'chestnut', 'gazpacho', 'sauce', 'monitor'])

# Set up a list to store the correct guesses
correctGuesses = []

# Run the game until the game ends
endGame = False
wrongGuesses = 0

while endGame == False:

    # Print out the word
    printWord(answer,correctGuesses)

    # Ask for a letter
    guess = getLetter()

    # Check if the letter is in the word
    if inWord(guess, answer) == True:
        print "Yay! You guessed correct"
        # Add this letter to the correct guesses list
        correctGuesses.append(guess)
    else:
        print "Sorry, that one isn't there"
        wrongGuesses = wrongGuesses + 1

        if wrongGuesses < 7:
            printMan(wrongGuesses)
        else:
            printMan(wrongGuesses)
            print "The word was",answer.upper()
            print "YOU LOSE!"
            endGame = True

    # Check if the game has been won (all letters guessed)
    if checkWin(answer,correctGuesses) == True:
        print "The word was",answer.upper()
        print "You win"
        endGame = True