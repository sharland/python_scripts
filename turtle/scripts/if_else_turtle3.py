#! /usr/local/bin/python3

from turtle import *
import random

title("Random dotty")
setup(500, 500, 0, 0)
bgcolor("green")
delay(0)

for x in range (1,500):
        xpos = random.randint(-250,250)
        ypos = random.randint(-250,250)
        randomsize = random.randint(1,50)
        penup()
        goto(xpos,ypos)
        if randomsize >25:
                dot(randomsize,"black")
                goto(xpos-2,ypos-2)
                dot(randomsize,"yellow")
        else:
                dot(randomsize,"black")
                goto(xpos-2,ypos-2)
                dot(randomsize,"blue")

done()
