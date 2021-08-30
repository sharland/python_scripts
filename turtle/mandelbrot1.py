from turtle import *
import math
speed(0)
def benoit(onelen):
    left(90)
    for x in range(-2*onelen, onelen):
        penup()
        goto(x, int(-1.5*onelen)-1)
        down()
        for y in range(int(-1.5*onelen)-1, int(1.5*onelen)-1):
            z = complex(0,0)
            c = complex(x*1.0/onelen,y*1.0/onelen)
            for k in range(20):
                z = z*z+c
                if abs(z) > 2:
                    g = .2 + .8*(20-k)/20
                    break
                if k == 19:
                    g = 0
            turtle.pencolor(0,g,0)
            turtle.forward(1)
benoit(250)
x = input("Press Enter to Exityadayadayada")