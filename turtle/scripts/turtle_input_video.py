#! /usr/local/bin/python3

from turtle import *

title("Turtle Input")
setup(500,500,0,0)

def polygon(sides,length):

    for x in range(sides):
        forward(length)
        right(360/sides)

keepGoing = True

while keepGoing == True:

    sides = int(input("Enter the number of sides for the shape: "))

    if sides == 0:
        keepGoing = False
    else:
        clear()
        polygon(sides,100)
        


done()
