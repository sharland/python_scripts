#! /usr/local/bin/python3

#simple GUI
#demonstrates creating a window and a few other things

#import
from tkinter import *

#create root window
root = Tk()

#modify the window
root.title("Yeah I made a GUI!")
root.geometry("400x200")

#begin window event loop (basically keep it open and running)
root.mainloop()
