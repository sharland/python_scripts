#! /usr/bin/python3.3
#credit Brian Sharland @sharland

import pibrella
import time

while pibrella.button.read() == 0:
	repeat = int(input("How many times would you like the lights to blink(up to 10)?:"))
	if repeat <11:	
		for x in range(repeat):
			print("Lights on!")
			pibrella.light.on()
			time.sleep(1)
			print("Lights off!")
			pibrella.light.off()
	else:
		print("please choose a number up to and including 10")

print("Button pushed - got to go!")
