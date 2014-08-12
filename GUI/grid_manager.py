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

#we create a label
#app being passed into the constructor tells lbl that app (which contains Frame) is its master
lbl = Label(app, text="Im a label")
lbl2 = Label(app, text="Im another label")

#we then invoke the label
lbl.grid()
lbl2.grid()

#sets up window to start listening for events
mainloop()
