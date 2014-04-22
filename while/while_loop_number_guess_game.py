#! /usr/local/bin/python3

targetNumber = 7
guess = int(input("Guess a number between 1 and 10: "))
while guess != targetNumber:
    print("Wrong!, try again")
    guess = int(input("Guess a number between 1 and 10: "))
print("Congratulations, you got it right!")
