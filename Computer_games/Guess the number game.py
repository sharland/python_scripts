#!/usr/bin/env python3

#This is a guess the number game
import random

guessesTaken = 0

myName = input("Hello! What is your name? ")

number = random.randint(1,20)
print("Well, ",myName," , I am thinking of a number between 1 and 20")

while guessesTaken < 6:
    guess = int(input("Take a guess:"))

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Your guess is too low.")

    if guess > number:
        print("Your guess is too high")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Good job, ",myName,"! you guessed my number in ",guessesTaken," guesses!")

if guess != number:
    number = str(number)
    print("Nope, the number I was thinking of was ", number)
    
