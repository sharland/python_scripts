#! /usr/local/bin/python3

targetNumber = 4 #the variable targetNumber gets the value 4 which is stored as an integer
guess = int(input("Guess a number between 1 and 10")) #if you don't use int then 'guess' is stored as string

while guess != targetNumber: #if 'guess' was still string then it can't be compared to an integer and you never win!
    
    print("Wrong, try again")
    
    guess = int(input("Guess a number between 1 and 10"))#next guess input obviously also needs to be int as well
    
print("Congratulations- that's right!")
