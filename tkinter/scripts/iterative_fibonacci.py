# fibtk.py
# a GUI version of the Fibonacci program, using iterative algorithm.
# by Mark Tranter - http://community.computingatschool.org.uk/resources/306

def start_fib(*ignore):
    num = input_box.get()
    txt.delete(0.0, END)
    try:
        num = int(num)
    except:
        txt.insert(0.0, "I need an integer.")
    txt.insert(0.0, str(fibonacci(num)))

def fibonacci(num):
    a = 0
    b = 1
    for i in range(num-1):
        c = a + b
        a, b = b, c
    return c

    
from tkinter import *
root = Tk()
root.title("Fibonacci (by iteration)")
root.geometry("320x100")
app = Frame(root)
app.grid()
root.bind('<Return>', start_fib)

input_lbl = Label(app, text = "Enter a number: ")
input_lbl.grid(row = 0, column = 0, pady = 5)

input_box = Entry(app, width = 10)
input_box.grid(row = 0, column = 1, pady = 5)

bttn = Button(app, text = "go!")
bttn["command"] = start_fib
bttn.grid(row = 1, column = 0, pady = 5)

txt = Text(app, width = 25, height = 2)
txt.grid(row=1, column = 1, pady = 5)
    
root.mainloop()
    
