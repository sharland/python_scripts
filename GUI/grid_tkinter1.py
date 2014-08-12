from tkinter import *

root=Tk()
root.title('grid manager')

#create a frame to hold other widgets

def __init__(self,master):

    app=Frame(master)
    app.grid()

    Label(master, text="First").grid(row=0)
    Label(master, text="Second").grid(row=1)

    e1 = Entry(master)
    e2 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
