#! /usr/local/bin/python3

from turtle import *
import random

title("Program X")
setup(500, 500, 0, 0)

def polygon(sides, length):

    for x in range(sides):
        forward(length)
        right(360/sides)

# hide the turtle
hideturtle()

# tell python to no longer update the graphics
tracer(0)

for x in range(1000):
    # choose a random spot
    xpos = random.randint(-200,200)
    ypos = random.randint(-200,200)

    # goto this spot
    penup()
    goto(xpos, ypos)
    pendown()

    # generate a random color
    red = random.random() # returns a number between 0 and 1
    green = random.random()
    blue = random.random()

    # fill in our shape
    fillcolor(red, green, blue)

    # draw the shape using a random size
    randomSide = random.randint(20,70)
    randomPolygon = random.randint(3,8)
    begin_fill()
    polygon(randomPolygon, randomSide)
    end_fill()

# update the screen with our drawing
update()

exitonclick()