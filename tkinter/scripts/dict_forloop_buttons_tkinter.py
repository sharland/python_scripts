from tkinter import *

#instantiates an object of class Tk
root = Tk()

#sets up window title and size
root.title("Buttons everywhere")
root.geometry("500x300")

#create a frame to hold widgets
#this says that app is a frame within root
#in other words you have passed the master ('root') to the constructor of the new object
app = Frame(root)

#invoke the grid manager
app.grid()

#create a dictionary called buttons to store the values created below
buttons = dict()

#setup a loop to create 9 buttons
#each time it passes through it creates a button and then invokes it
for i in range(1,10):
    i = str(i)
    buttons[i] = Button(app,text="Button "+i)
    buttons[i].grid()

#sets up window to start listening for events
mainloop()
