from tkinter import *

#instantiates an object of class Tk
root = Tk()

#sets up window title and size
root.title("This is a title")
root.geometry("500x300")

#create a frame to hold widgets
#this says that app is a frame within root
#in other words you have passed the master ('root') to the constructor of the new object
app = Frame(root)

#invoke the grid manager
app.grid()

#setup some labels - as you can see the labels are created and invoked in the same line (cleaner code)
#the grid argument is the row number, first column doesn't need to be specified

Label(app, text="First").grid(row=0)
Label(app, text="Second").grid(row=1)

e1 = Entry(app)
e2 = Entry(app)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#sets up window to start listening for events
mainloop()
