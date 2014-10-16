#! /usr/local/bin/python3

import os		#allows interaction with the command line
import time		#allows us to set time between frames

FRAMES = 180	#number of frames to compile
FPS_IN = 30		#how many frames per second are going to go in
FPS_OUT = 30	#how many frames are going to be compiled out
FILMLENGTH = float(FRAMES / FPS_IN)


frameCount = 0
while frameCount < FRAMES:
    imageNumber = str(frameCount).zfill(7)
    os.system("raspistill -o image%s.jpg"%(imageNumber))
    frameCount += 1
    time.sleep(TIMEBETWEEN - 6) #Takes roughly 6 seconds to take a picture

os.system("avconv -r %s -i image%s.jpg -r %s -vcodec libx264 -crf 20 -g 15 -vf crop=2592:1458,scale=1280:720 timelapse.mp4"%(FPS_IN,'%7d',FPS_OUT))