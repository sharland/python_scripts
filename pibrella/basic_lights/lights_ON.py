#! /usr/bin/python3.3

import pibrella
import time

print("Red light is on!")
pibrella.light.red.on()
time.sleep(2)

print("Amber light is on!")
pibrella.light.amber.on()
time.sleep(2)

print("Green light is on!")
pibrella.light.green.on()
time.sleep(2)
