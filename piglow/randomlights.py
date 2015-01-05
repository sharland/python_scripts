#! /usr/bin/local/python3

from PyGlow import PyGlow
from time import sleep
import random

pyglow = PyGlow()

pyglow.all(0)

while True:
        randomLED = random.randint(1,18)
        randomBright = random.randint(0,100)
        pyglow.led(randomLED,randomBright)
        sleep(0.1)
        pyglow.led(randomLED,0)

pyglow.all(0)