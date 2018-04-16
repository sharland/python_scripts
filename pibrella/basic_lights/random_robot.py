from pibrella import *
from time import sleep
import random
import decimal

minTime = 0
maxTime = 2



def turnLeft(lpause):
    output.e.on()
    sleep(lpause)
    output.e.off()

def turnRight(rpause):
    output.g.on()
    sleep(rpause)
    output.g.off()

def goForward(fpause):
    output.e.on()
    output.g.on()
    sleep(fpause)
    output.e.off()
    output.g.off()


for i in range(20):
    fpause = 0.1*random.randint(int(minTime * 10), int(maxTime * 10))
    goForward(fpause)
    turnRight(2)
    goForward(fpause)
    turnLeft(2)
