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

#create a frame in the window to hold other widgets
app = Frame(root) #pass root to frame constructor, new frame is now in the root

#create a grid - associated with a layout manager
app.grid()

#create a label in the frame
lbl = Label(app,text = "I'm a label")

