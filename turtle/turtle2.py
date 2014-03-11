#! /usr/bin/python3.3

from turtle import *

speed(10)
x = 0

colormode(255)
r = 0
g = 0
b = 0
while x < 72:
    while r < 256:
        pencolor(r,g,b)
        fd(100)
        rt(90)
        r = r + 0.5
        pencolor(r,g,b)
        fd(100)
        rt(90)
        r = r + 0.5
        pencolor(r,g,b)
        fd(100)
        rt(95)
        r = r + 0.5
        pencolor(r,g,b)
        fd(110)
        r = r + 0.5
        x = x + 1
