from turtle import *
import math

speed(0)

def fractal1(length):
    left(90)
    for x in range(-2*length,length):
        print("x level")
        penup()
        goto(x,int(-1.5*length)-1)
        pendown()
        for y in range(int(-1.5*length)-1,int(1.5*length)-1):
            z = complex(0,0)
            c = complex(x*1.0/length,y*1.0/length)
            print("y level")
            for k in range(20):
                print("k level")
                z = z*z+c
                if abs(z) > 2:
                    g = .2 + .8*(20-k)/20
                    break
                if k == 19:
                    g = 0
            pencolor(0,g,0)
            forward(1)

fractal1(250)

done()