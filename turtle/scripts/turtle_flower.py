#! /usr/local/bin/python3

from turtle import *
speed(1)
colormode(255)

x = 0

fillcolor(255,0,255)

begin_fill()
while x<8:
    right(45)
    circle(50)
    dot(20,"red")
    x = x+1
    
end_fill()

done()
