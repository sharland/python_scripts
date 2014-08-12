#! /usr/local/bin/python3
from turtle import *
import random

title("Marking an area")
setup(500, 500, 0, 0)
bgcolor("orange")
delay(0)
penup()
goto(51,51)
pendown()
colormode(255)

global r,g,b
r = 0
g = 0
b = 255

for i in range (5000):
    randomDistance = random.randint(1,50)
    randomTurn = random.randint(-85,85)
    pencolor(r,g,b)
    forward(randomDistance)
    xcorInt = int(round(xcor(),5))
    ycorInt = int(round(ycor(),5))
    if xcorInt > 200 or xcorInt < -200 or ycorInt > 200 or ycorInt < -200:
        right(180)
        forward(50)
    elif xcorInt <50 and xcorInt >-50 and ycorInt<50 and ycorInt >-50:
        right(180)
        forward(50)
    right(randomTurn)
        
done()
