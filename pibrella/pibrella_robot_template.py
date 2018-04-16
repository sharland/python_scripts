from pibrella import *
from time import sleep

def turnLeft(pause):
    output.e.on()
    sleep(pause)
    output.e.off()

def turnRight(pause):
    output.g.on()
    sleep(pause)
    output.g.off()

def goForward(pause):
    output.e.on()
    output.g.on()
    sleep(pause)
    output.e.off()
    output.g.off()
