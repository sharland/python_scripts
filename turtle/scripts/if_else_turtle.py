#! /usr/local/bin/python3

from turtle import *
import random

title("Marking an area")
setup(500, 500, 0, 0)
bgcolor("orange")

speed(0)

for x in range (0,200):
        xpos = random.randint(-250,250)
        ypos = random.randint(-250,250)
        goto(xpos,ypos)
        if xpos > 50 and xpos < 200 and ypos > 50 and ypos < 200:
                dot(20,"blue")
        else:
                dot(20,"green")

done()
