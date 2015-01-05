#! /usr/local/bin/python3

from turtle import *
import random

def polygon(sides, length):

    for x in range(sides):
        forward(length)
        right(360/sides)

title("My Turtle")
setup(500,500, 0,0)

keepgoing = True

while keepgoing == True:

    # get a number of sides from the user
    sides = int(input("Enter # of sides"))

    # if the user enters a 0 then we can end the loop
    if sides == 0:
        keepgoing = False
    else:
        # clear the canvas
        clear()

        # draw the polygon
        polygon(sides, 50)

exitonclick()