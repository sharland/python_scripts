#! /usr/local/bin/python3

from turtle import *
import random

title("Marking an area")
setup(500, 500, 0, 0)
bgcolor("orange")

for x in range (1,500):
        randomvalue = random.randint(50,100)
        randomturn = random.randint(-95,95)
        speed(10)
        forward(randomvalue)
        right(randomturn)
        position = int(pos())
        if position > 50 and position <200:
                goto(0,0)

done()
