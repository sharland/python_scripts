#! /usr/bin/python3.3

from turtle import *

x = 0
position()
while x<10:
    delay(0)
    speed(3)
    right(45)
    circle(50)
    dot(20,"red")
    print(x)
    x = x+1
    
